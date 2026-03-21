# SAS Advanced Figure & Table Code - Publication Ready
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## 1. Spline Plot Generation

### 1.1 Get mean values for reference

```sas
proc means data=adsl noprint;
    var age base_tumvol surg2gks_mos bed;
    output out=means_adsl mean=age_mean tumvol_mean surgmos_mean bed_mean;
run;
```

### 1.2 Create prediction dataset for IGF-1 spline

```sas
data pred_igf;
    if _n_=1 then set means_adsl;
    do base_igf1i = 0.5 to 6 by 0.1;
        age = age_mean;
        base_tumvol = tumvol_mean;
        surg2gks_mos = surgmos_mean;
        bed = bed_mean;
        sex = "F";
        earlygks_fl = "N";
        plan_type = "TARGETED";
        output;
    end;
run;
```

### 1.3 Score using PLM

```sas
proc plm restore=phreg_spline_igf;
    score data=pred_igf out=pred_igf_scored / ilink;
run;
```

### 1.4 Plot spline

```sas
ods graphics on / reset width=7in height=5in imagename="Spline_IGF1I";

proc sgplot data=pred_igf_scored;
    series x=base_igf1i y=pred / lineattrs=(thickness=2);
    xaxis label="Baseline IGF-1 Index";
    yaxis label="Predicted Relative Risk";
run;

ods graphics off;
```

---

## 2. BED Spline Plot

### 2.1 Fit model with BED spline

```sas
proc phreg data=adtte_ttrrem;
    class sex(ref="F")
          earlygks_fl(ref="N")
          plan_type(ref="TARGETED")
          / param=ref;

    effect spl_bed = spline(bed / naturalcubic basis=tpf(noint));
    
    model aval*cnsr(1) =
        age
        sex
        base_igf1i
        base_tumvol
        surg2gks_mos
        spl_bed
        earlygks_fl
        plan_type;
    store out=phreg_spline_bed;
run;
```

### 2.2 Create prediction dataset

```sas
data pred_bed;
    if _n_=1 then set means_adsl;
    do bed = 40 to 140 by 1;
        age = age_mean;
        base_tumvol = tumvol_mean;
        surg2gks_mos = surgmos_mean;
        base_igf1i = 2.0;
        sex = "F";
        earlygks_fl = "N";
        plan_type = "TARGETED";
        output;
    end;
run;

proc plm restore=phreg_spline_bed;
    score data=pred_bed out=pred_bed_scored / ilink;
run;
```

### 2.3 Plot

```sas
ods graphics on / reset width=7in height=5in imagename="Spline_BED";

proc sgplot data=pred_bed_scored;
    series x=bed y=pred / lineattrs=(thickness=2);
    xaxis label="Biologically Effective Dose";
    yaxis label="Predicted Relative Risk";
run;

ods graphics off;
```

---

## 3. Forest Plot from Cox Results

### 3.1 Process PHREG output

```sas
data forest_input;
    set cox_pe;
    where Parameter ne "Intercept";
    HR = HazardRatio;
    LowerCI = HRLowerCL;
    UpperCI = HRUpperCL;
run;
```

### 3.2 Create labels

```sas
data forest_input;
    set forest_input;
    length VarLabel $60;
    if Parameter = "age" then VarLabel = "Age";
    else if Parameter = "base_igf1i" then VarLabel = "Baseline IGF-1 Index";
    else if Parameter = "base_tumvol" then VarLabel = "Tumor Volume";
    else if Parameter = "surg2gks_mos" then VarLabel = "Surgery-to-GKS Interval";
    else if Parameter = "bed" then VarLabel = "Biologically Effective Dose";
    else if Parameter = "earlygks_flY" then VarLabel = "Early vs Delayed GKS";
    else if Parameter = "plan_typeWHOLE_SELLA" then VarLabel = "Whole-Sella vs Targeted";
    else if Parameter = "sexM" then VarLabel = "Male vs Female";
    else VarLabel = Parameter;
run;
```

### 3.3 Forest plot

```sas
ods graphics on / reset width=8in height=6in imagename="Forest_Cox_Remission";

proc sgplot data=forest_input noautolegend;
    scatter y=VarLabel x=HR / xerrorlower=LowerCI xerrorupper=UpperCI
            markerattrs=(symbol=squarefilled size=8);
    refline 1 / axis=x lineattrs=(pattern=shortdash);
    xaxis type=log label="Hazard Ratio (95% CI)";
    yaxis discreteorder=data label="";
run;

ods graphics off;
```

---

## 4. Calibration Plot

### 4.1 Create 3-year binary outcome

```sas
proc sql;
    create table rem3 as
    select a.usubjid, a.aval, a.cnsr,
           case
               when a.cnsr = 0 and a.aval <= 1095 then 1
               when a.aval > 1095 then 0
               when a.cnsr = 1 and a.aval <= 1095 then .
               else 0
           end as y3_rem
    from adtte as a
    where a.paramcd = "TTRREM";
quit;
```

### 4.2 Merge with baseline

```sas
proc sql;
    create table model3 as
    select a.*, b.y3_rem
    from adsl as a
    left join rem3 as b
    on a.usubjid = b.usubjid
    where b.y3_rem in (0,1);
quit;
```

### 4.3 Logistic model

```sas
proc logistic data=model3 descending;
    class sex(ref="F")
          earlygks_fl(ref="N")
          plan_type(ref="TARGETED")
          / param=ref;
    model y3_rem =
        age
        base_igf1i
        base_tumvol
        surg2gks_mos
        bed
        sex
        earlygks_fl
        plan_type;
    output out=pred3 p=pred_prob;
run;
```

### 4.4 Decile grouping

```sas
proc rank data=pred3 out=pred3_grp groups=10;
    var pred_prob;
    ranks decile;
run;
```

### 4.5 Calculate observed vs predicted

```sas
proc means data=pred3_grp noprint;
    class decile;
    var pred_prob y3_rem;
    output out=calib3 mean=mean_pred mean_obs;
run;

data calib3;
    set calib3;
    where decile ne .;
run;
```

### 4.6 Plot calibration

```sas
ods graphics on / reset width=6in height=6in imagename="Calibration_3Y_Remission";

proc sgplot data=calib3;
    scatter x=mean_pred y=mean_obs / markerattrs=(symbol=circlefilled size=10);
    series x=mean_pred y=mean_obs / lineattrs=(thickness=2);
    lineparm x=0 y=0 slope=1 / lineattrs=(pattern=shortdash);
    xaxis label="Mean Predicted 3-Year Remission Probability" values=(0 to 1 by 0.1);
    yaxis label="Observed 3-Year Remission Probability" values=(0 to 1 by 0.1);
run;

ods graphics off;
```

---

## 5. Decision Curve Analysis (DCA)

### 5.1 Define thresholds

```sas
data thresholds;
    do pt = 0.05 to 0.80 by 0.01;
        output;
    end;
run;
```

### 5.2 Cross-product

```sas
proc sql;
    create table dca_input as
    select a.*, b.pt
    from pred3 as a, thresholds as b;
quit;
```

### 5.3 Calculate TP/FP

```sas
data dca_input;
    set dca_input;
    if pred_prob >= pt then pred_pos = 1;
    else pred_pos = 0;

    if pred_pos = 1 and y3_rem = 1 then tp = 1; else tp = 0;
    if pred_pos = 1 and y3_rem = 0 then fp = 1; else fp = 0;
run;
```

### 5.4 Net benefit by threshold

```sas
proc sql;
    create table dca_model as
    select pt,
           count(*) as n,
           sum(tp) as tp,
           sum(fp) as fp,
           (calculated tp / calculated n)
           - (calculated fp / calculated n) * (pt / (1 - pt)) as net_benefit
    from dca_input
    group by pt
    order by pt;
quit;
```

### 5.5 Treat-all / Treat-none

```sas
data dca_none;
    set thresholds;
    net_benefit = 0;
    strategy = "Treat None";
run;

proc sql noprint;
    select mean(y3_rem) into :event_rate from pred3;
quit;

data dca_all;
    set thresholds;
    event_rate = &event_rate.;
    net_benefit = event_rate - (1 - event_rate) * (pt / (1 - pt));
    strategy = "Treat All";
run;

data dca_model2;
    set dca_model;
    strategy = "Model";
run;
```

### 5.6 Combine and plot

```sas
data dca_plot;
    set dca_model2 dca_all dca_none;
run;

ods graphics on / reset width=7in height=5in imagename="DCA_3Y_Remission";

proc sgplot data=dca_plot;
    series x=pt y=net_benefit / group=strategy lineattrs=(thickness=2);
    xaxis label="Threshold Probability";
    yaxis label="Net Benefit";
run;

ods graphics off;
```

---

## 6. Table 1: Baseline Characteristics

### 6.1 Continuous variables

```sas
proc means data=adsl n median q1 q3;
    class plan_type;
    var age base_igf1i base_tumvol surg2gks_mos margindose bed fup_mos;
    ods output summary=table1_cont;
run;
```

### 6.2 Categorical variables

```sas
proc freq data=adsl;
    tables plan_type*sex
          plan_type*knospgr
          plan_type*earlygks_fl
          plan_type*medhold_cat
          / chisq norow nocol nopercent;
    ods output CrossTabFreqs=table1_cat;
run;
```

### 6.3 Export to RTF

```sas
ods rtf file="table1.rtf" style=journal;

title "Table 1. Baseline Characteristics by Plan Type";

proc report data=adsl nowd;
    column plan_type age sex base_igf1i base_tumvol surg2gks_mos bed fup_mos;
    define plan_type / group "Plan Type";
    define age / analysis median "Age, Median";
    define sex / display "Sex";
    define base_igf1i / analysis median "Baseline IGF-1 Index, Median";
    define base_tumvol / analysis median "Tumor Volume, Median";
    define surg2gks_mos / analysis median "Surgery-to-GKS Interval, Median";
    define bed / analysis median "BED, Median";
    define fup_mos / analysis median "Follow-up, Median";
run;

ods rtf close;
```

---

## 7. Cox Regression Table

### 7.1 Run Cox model

```sas
proc phreg data=adtte_ttrrem;
    class sex(ref="F")
          earlygks_fl(ref="N")
          plan_type(ref="TARGETED")
          / param=ref;
    model aval*cnsr(1) =
        age
        sex
        base_igf1i
        base_tumvol
        surg2gks_mos
        bed
        earlygks_fl
        plan_type
        / rl;
    ods output ParameterEstimates=cox_pe;
run;
```

### 7.2 Format for publication

```sas
data cox_table;
    set cox_pe;
    where Parameter ne "Intercept";

    length Variable $60 HR_CI $50;

    if Parameter = "age" then Variable = "Age";
    else if Parameter = "base_igf1i" then Variable = "Baseline IGF-1 Index";
    else if Parameter = "base_tumvol" then Variable = "Tumor Volume";
    else if Parameter = "surg2gks_mos" then Variable = "Surgery-to-GKS Interval";
    else if Parameter = "bed" then Variable = "Biologically Effective Dose";
    else if Parameter = "earlygks_flY" then Variable = "Early vs Delayed GKS";
    else if Parameter = "plan_typeWHOLE_SELLA" then Variable = "Whole-Sella vs Targeted";
    else if Parameter = "sexM" then Variable = "Male vs Female";
    else Variable = Parameter;

    HR_CI = cats(put(HazardRatio, 6.2), " (",
                 put(HRLowerCL, 6.2), ", ",
                 put(HRUpperCL, 6.2), ")");
run;
```

### 7.3 Export to RTF

```sas
ods rtf file="cox_table_remission.rtf" style=journal;

title "Table 2. Multivariable Cox Regression for Time to Endocrine Remission";

proc report data=cox_table nowd;
    column Variable HazardRatio HRLowerCL HRUpperCL ProbChiSq HR_CI;
    define Variable / display "Variable";
    define HR_CI / display "Hazard Ratio (95% CI)";
    define ProbChiSq / display "P Value" format=pvalue6.4;
run;

ods rtf close;
```

---

## 8. Export High-Resolution Images

```sas
ods listing gpath="C:\your_output_path";
ods graphics / reset imagename="KM_TTRREM_EARLYGKS" 
               imagefmt=png width=7in height=5in;

proc lifetest data=adtte_ttrrem 
              plots=survival(atrisk=0 to 60 by 12 cb=hw test);
    time aval*cnsr(1);
    strata earlygks_fl;
run;
```

---

## Recommended Output Order

### Tables
1. Table 1: Baseline characteristics
2. Table 2: Cox model for remission
3. Table 3: Cox model for hypopituitarism

### Figures (Main Text)
1. Figure 1: Study flow diagram
2. Figure 2: KM for remission
3. Figure 3: KM for hypopituitarism
4. Figure 4: Spline for IGF-1
5. Figure 5: Spline for BED
6. Figure 6: Forest plot

### Supplementary
1. Calibration plot
2. Decision curve analysis
3. Love plot (covariate balance)
4. Missing data summary

---

*Document created: 2026-03-21*
*Version: SAS Advanced Figure & Table Code*
