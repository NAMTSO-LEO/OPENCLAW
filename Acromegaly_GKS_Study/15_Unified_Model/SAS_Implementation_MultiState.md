# SAS Implementation Guide for Multi-State Model

## Quick Start Code Framework

---

## 1. Data Preparation

### 1.1 Create Analysis Dataset

```sas
/* Step 1: Define states */
proc sql;
  create table analysis_set as
  select 
    patient_id,
    date_diagnosis,
    date_surgery,
    case when eor = 'GTR' then 'SurgeryRem' 
                              else 'SurgeryResid' end as state_surgery,
    date_radiation,
    margin_dose,
    knosp_grade,
    tumor_volume,
    preop_igf1,
    age,
    /* State at each time point */
    case when missing(date_surgery) then 'Active'
         else 'SurgeryRem' end as state_12mo,
    case when missing(date_radiation) then calculated state_12mo
         else 'RTRem' end as state_24mo
  from initial_data;
quit;

/* Step 2: Create time-dependent dataset for Cox */
data tte_data;
  set analysis_set;
  
  /* Time to remission (from any state) */
  if not missing(date_remission) then do;
    event = 1;
    time = (date_remission - date_diagnosis) / 30.4; /* months */
    event_type = 'remission';
  end;
  else if not missing(date_death) then do;
    event = 1;
    time = (date_death - date_diagnosis) / 30.4;
    event_type = 'death';
  end;
  else do;
    event = 0;
    time = (date_censor - date_diagnosis) / 30.4;
    event_type = 'censor';
  end;
  
  /* Convert Knosp to numeric */
  knosp_num = input(knosp_grade, 2.);
  
  /* IGF-1 index */
  igf1i = preop_igf1 / upper_limit_normal;
  
  /* Age group */
  if age < 33 then age_group = 'young';
  else age_group = 'older';
run;
```

---

## 2. Kaplan-Meier Analysis

```sas
/* Basic KM for time to remission */
proc lifetest data=tte_data plots=survival;
  time time * event(0);
  strata margin_dose_group;
  where event_type = 'remission';
  title "Time to Endocrine Remission by Radiation Dose";
run;

/* Nelson-Aalen cumulative hazard */
proc lifetest data=tte_data plots=nelson;
  time time * event(0);
  strata treatment_modality;
  title "Cumulative Hazard by Treatment Type";
run;
```

---

## 3. Cox Proportional Hazards

### 3.1 Univariate

```sas
proc phreg data=tte_data;
  class treatment_modality knosp_group;
  model time * event(0) = knosp_num igf1i age_group margin_dose / 
                         ties=exact risklimits;
  strata center;
  title "Univariate Cox: Predictors of Remission";
run;
```

### 3.2 Multivariate with Spline

```sas
/* Using PROC TRANSREG for spline basis */
proc transreg data=tte_data dummy;
  model identity(igf1i) = spline(igf1i / nknots=4);
  output out=spline_data coefficients;
run;

/* Then run Cox with spline terms */
proc phreg data=spline_data;
  model time * event(0) = knosp_num igf1i_spline1 igf1i_spline2 
                          age_group margin_dose / ties=exact;
  title "Multivariate Cox with Spline for IGF-1";
run;
```

---

## 4. Competing Risk Analysis (Fine-Gray)

```sas
/* Note: SAS doesn't have built-in Fine-Gray - use PHREG with cause=1 */
proc phreg data=tte_data;
  model time * hypopit_event(0) = age_group margin_dose knosp_num 
                                  / eventcode=1;
  strata center;
  title "Subdistribution Hazard for Hypopituitarism";
run;

/* Alternative: Cumulative incidence macro */
/* See: https://support.sas.com/kb/25/013.html */
```

---

## 5. Multi-State Model (via PROC MCME - Markov Chain)

*Note: SAS doesn't have native multi-state. Recommend R `msm` package.*

### SAS workaround: Stratified KM by state

```sas
/* State-specific analysis */
proc lifetest data=tte_data plots=survival;
  time time_to_state2 * state2_event(0);
  strata knosp_group;
  title "Time from Surgery to Radiation by Knosp Grade";
run;

proc lifetest data=tte_data plots=survival;
  time time_to_remission * remission_event(0);
  strata treatment_modality;
  title "Time to Remission by Treatment Type";
run;
```

---

## 6. Propensity Score / Overlap Weighting

```sas
/* Step 1: Propensity model */
proc logistic data=patient_data;
  class treatment_modality(ref='Surgery') 
        knosp_group(ref='0-2') 
        prior_surgery(ref='none');
  model treatment = age knosp_group prior_surgery preop_igf1;
  output out=ps_data predprob=ps;
run;

/* Step 2: Overlap weights */
data weighted_data;
  set ps_data;
  /* Overlap weighting */
  if treatment = 'GKRS' then weight = ps / (ps + 0.5);
  else weight = (1-ps) / (1-ps + 0.5);
  
  /* Stabilized weights */
  /* For more accurate implementation, use IPTW macro */
run;

/* Step 3: Weighted analysis */
proc phreg data=weighted_data;
  class treatment_modality;
  model time * event(0) = treatment_modality / risklimits;
  weight weight;
  title "Weighted Cox Analysis";
run;
```

---

## 7. Forest Plot

```sas
/* Create HR dataset manually then use SGPLOT */
data hr_plot;
  input Variable $ Effect Lower Upper;
  /* Example data */
datalines;
Knosp (per grade) 1.45 1.12 1.89
IGF-1 Index (per 1) 1.28 1.05 1.56
Age (<33 vs >33) 0.72 0.54 0.96
Margin Dose (per Gy) 0.95 0.91 0.99
;
run;

proc sgplot data=hr_plot;
  scatter x=Effect y=Variable / xerrorbar=(lower upper);
  refline 1 / axis=x;
  xaxis label="Hazard Ratio (95% CI)";
  title "Forest Plot: Predictors of Endocrine Remission";
run;
```

---

## 8. Validation: Internal-External Cross-Validation

```sas
/* Leave-one-center-out validation */
%macro iecv(center_id);
  proc phreg data=full_data outnet outpred;
    model time * event(0) = knosp_num igf1i age margin_dose;
    where center ne &center_id;
    id patient_id;
  run;
  
  /* Apply to held-out center */
  proc phreg data=full_data outpred;
    model time * event(0) = knosp_num igf1i age margin_dose;
    where center = &center_id;
    id patient_id;
  run;
  
  /* Calculate AUC */
  /* (use proc logistic or proc nlmixed) */
%mend;

%iecv(1); /* Repeat for each center */
```

---

## 9. Figures Checklist

| Figure | SAS Code | Description |
|--------|----------|-------------|
| 1 | `proc lifetest plots=survival` | KM curves by treatment |
| 2 | `proc sgplot` | Cumulative incidence (competing risk) |
| 3 | `proc sgplot` | Forest plot |
| 4 | `proc sgplot` | Spline plot for continuous variables |
| 5 | `proc sgplot` | Calibration plot |
| 6 | `proc sgplot` | Time-dependent AUC |

---

## 10. Key Macros

### 10.1 Time-Dependent Covariate Macro

```sas
%macro tdc(dsn=, timevar=, event=, start=, stop=, covar=);
  /* Create time-dependent covariate for Cox */
  data &dsn._tdc;
    set &dsn.;
    if &timevar <= &start and &stop > &start then &covar._td = 0;
    else if &timevar > &start then &covar._td = 1;
  run;
%mend;
```

---

## Notes

1. **Multi-state modeling**: SAS is limited. Recommend R `msm` package for final analysis
2. **Competing risks**: Use Fine-Gray via `proc phreg` with `eventcode=`
3. **Validation**: IECV requires macro loop over centers

---

*Created: 2026-03-21*
*For use with your multicenter GKS data*