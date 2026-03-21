# SAS Figure Generation Code - Publication Quality
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Prerequisites

### Required Datasets
- `adsl` - Subject-level analysis dataset
- `adtte` - Time-to-event dataset with PARAMCD, AVAL, CNSR
- `adendo` - Longitudinal endocrine information

### Required Variables in adsl
- EARLYGKS_FL - Early Gamma Knife indicator
- PLAN_TYPE - Treatment planning type
- KNOSPGR - Knosp grade
- BASE_IGF1I - Baseline IGF-1 index
- BED - Biologically effective dose

---

## Figure 1: Study Flow Diagram

*Note: Flow diagram is typically created using PowerPoint or other tools. SAS can generate summary statistics.*

```sas
/* Generate summary counts for flow diagram */
proc freq data=adsl;
 tables siteid / nocum;
 ods output onewayfreqs=site_freq;
run;

proc means data=adsl n mean std q1 q3 median;
 var age base_igf1i base_tumvol;
 ods output summary=demog_summary;
run;
```

---

## Figure 2: Kaplan–Meier - Endocrine Remission by Early GKS

### Step 1: Merge stratification variable

```sas
proc sql;
 create table adtte_ttrrem as
 select a.*, b.earlygks_fl
 from adtte as a
 left join adsl as b
 on a.usubjid = b.usubjid
 where a.paramcd = "TTRREM";
quit;
```

### Step 2: Generate KM plot

```sas
ods graphics on / reset width=7in height=5in imagename="KM_TTRREM_EARLYGKS";

proc lifetest data=adtte_ttrrem 
    plots=survival(atrisk=0 to 60 by 12 cb=hw test);
    time aval*cnsr(1);
    strata earlygks_fl;
    format earlygks_fl $8.;
run;

ods graphics off;
```

---

## Figure 3: Kaplan–Meier - New Hypopituitarism by Plan Type

### Step 1: Merge stratification variable

```sas
proc sql;
 create table adtte_tthypo as
 select a.*, b.plan_type
 from adtte as a
 left join adsl as b
 on a.usubjid = b.usubjid
 where a.paramcd = "TTHYPO";
quit;
```

### Step 2: Generate KM plot

```sas
ods graphics on / reset width=7in height=5in imagename="KM_TTHYPO_PLANTYPE";

proc lifetest data=adtte_tthypo 
    plots=survival(atrisk=0 to 60 by 12 cb=hw test);
    time aval*cnsr(1);
    strata plan_type;
run;

ods graphics off;
```

---

## Alternative: KM by IGF-1 Index Tertiles

### Create tertile groups

```sas
proc rank data=adsl out=adsl_rank groups=3;
    var base_igf1i;
    ranks igf1i_tertile;
run;

data adsl_rank;
    set adsl_rank;
    length igf1i_grp $12;
    if igf1i_tertile = 0 then igf1i_grp = "Low";
    else if igf1i_tertile = 1 then igf1i_grp = "Middle";
    else if igf1i_tertile = 2 then igf1i_grp = "High";
run;

/* Merge to adtte */
proc sql;
 create table adtte_ttrrem_igf as
 select a.*, b.igf1i_grp
 from adtte as a
 left join adsl_rank as b
 on a.usubjid = b.usubjid
 where a.paramcd = "TTRREM";
quit;

/* KM plot */
ods graphics on / reset width=7in height=5in imagename="KM_TTRREM_IGF1I";

proc lifetest data=adtte_ttrrem_igf 
    plots=survival(atrisk=0 to 60 by 12 cb=hw test);
    time aval*cnsr(1);
    strata igf1i_grp;
run;

ods graphics off;
```

---

## Figure 4: Multivariable Cox Regression

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

---

## Figure 5: Restricted Cubic Spline

### Method 1: Using EFFECT statement with PLOTS

```sas
proc phreg data=adtte_ttrrem plots(overlay)=survival;
    class sex(ref="F")
          earlygks_fl(ref="N")
          plan_type(ref="TARGETED")
          / param=ref;

    effect spl_igf1i = spline(base_igf1i / naturalcubic basis=tpf(noint) details);
    
    model aval*cnsr(1) =
        age
        sex
        spl_igf1i
        base_tumvol
        surg2gks_mos
        bed
        earlygks_fl
        plan_type
        / rl;

    ods output ParameterEstimates=pe_spline_igf;
run;
```

### Method 2: Using STORE + PLM for custom plots

```sas
proc phreg data=adtte_ttrrem;
    class sex(ref="F")
          earlygks_fl(ref="N")
          plan_type(ref="TARGETED")
          / param=ref;

    effect spl_igf1i = spline(base_igf1i / naturalcubic basis=tpf(noint));
    
    model aval*cnsr(1) =
        age
        sex
        spl_igf1i
        base_tumvol
        surg2gks_mos
        bed
        earlygks_fl
        plan_type;
    store out=phreg_spline_igf;
run;

/* Create prediction dataset with IGF-1 range */
data pred_igf1;
    do base_igf1i = 0.5 to 5.0 by 0.1;
        age = 45;
        sex = "M";
        base_tumvol = 2.5;
        surg2gks_mos = 12;
        bed = 50;
        earlygks_fl = "Y";
        plan_type = "TARGETED";
        output;
    end;
run;

/* Generate predictions */
proc plm source=phreg_spline_igf;
    score data=pred_igf1 out=pred_out / ilink;
run;

/* Plot using SGPLOT */
proc sgplot data=pred_out;
    band x=base_igf1i lower=lower upper=upper / fillattrs=(color=gray transparency=0.7);
    series x=base_igf1i y=predicted / lineattrs=(color=blue thickness=2);
    refline 1 / axis=y lineattrs=(pattern=dash);
    xaxis label="Baseline IGF-1 Index";
    yaxis label="Hazard Ratio for Remission";
    title "Nonlinear Association between IGF-1 Index and Remission";
run;
```

---

## Forest Plot from Cox Results

```sas
/* Combine estimates from Cox model */
data forest_data;
    set cox_pe;
    /* Format for forest plot */
    keep parameter estimate hazardratio lower upper;
run;

/* Forest plot using SGPLOT */
proc sgplot data=forest_data;
    scatter x=estimate y=parameter / xerrorlower=lower xerrorupper=upper 
            markerattrs=(symbol=circlefilled size=8);
    refline 1 / axis=x lineattrs=(pattern=dash);
    xaxis label="Hazard Ratio (95% CI)";
    yaxis label="Variable" reverse;
    title "Multivariable Predictors of Endocrine Remission";
run;
```

---

## Calibration Plot (External Macro)

*Note: Requires %calibration macro or use validated packages*

```sas
/* If using %calibration macro */
%calibration(data=adtte_ttrrem, 
             response=REMISS, 
             predicted=pred, 
             time=TTRREM, 
             nevent=50, 
             nrefit=200)
```

---

## Love Plot (Covariate Balance)

```sas
/* Generate SMD before/after weighting */
/* Before weighting */
proc means data=adsl;
    var age base_igf1i base_tumvol;
    output out=before_mean;
run;

/* After weighting */
proc means data=adsl_wtd;
    var age base_igf1i base_tumvol;
    output out=after_mean;
run;

/* Combine and calculate SMD */
data love_plot;
    merge before_mean after_mean;
    /* Calculate standardized mean differences */
run;

/* Plot */
proc sgplot data=love_plot;
    scatter x=smd_before y=variable / markerattrs=(color=red symbol=circle);
    scatter x=smd_after y=variable / markerattrs=(color=blue symbol=square);
    refline 0.1 / axis=x lineattrs=(pattern=dash);
    xaxis label="Standardized Mean Difference";
    yaxis label="Covariate";
    title "Covariate Balance: Before vs After Overlap Weighting";
run;
```

---

## Tips for Publication Quality

### Image Resolution
```sas
ods listing gpath="C:\output\" image_dpi=300;
ods graphics on / imagename="figure1" image_dpi=300;
```

### Fonts and Style
```sas
ods html style=htmlblue;
proc template;
    define style styles.mystyle;
        parent = styles.htmlblue;
        style graphwalls / frameborder=0;
    end;
run;
```

---

*Document created: 2026-03-21*
*Version: SAS Figure Generation Code*
