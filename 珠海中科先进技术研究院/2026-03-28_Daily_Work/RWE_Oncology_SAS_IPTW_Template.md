# SAS PS/IPTW Oncology Survival Analysis Template
## Complete Workflow for Real-World Evidence

---

## 📋 Overview

This template provides a complete SAS implementation for **Propensity Score (PS) / Inverse Probability Treatment Weighting (IPTW)** analysis in oncology survival studies (OS/PFS).

**Target Population**: Oncology RWE studies with time-to-event outcomes

**Key Features**:
- PROC PSMATCH (modern approach)
- Stabilized IPTW with formula
- Balance diagnostics (SMD + Love Plot)
- Weighted Cox regression
- Trimming option

---

## 🔄 Part 1: Data Preparation

```sas
/******************************************************************************
* PART 1: DATA PREPARATION
* Purpose: Prepare analysis dataset with required variables
*****************************************************************************/

* Example dataset structure;
data analysis_data;
    set derived.analysis_dataset; /* Your ADaM dataset */
    
    * Define treatment indicator (1 = treated, 0 = control);
    where trt01an in (1, 0) and length(trt01an) > 0;
    
    * Define outcome variables;
    /* Overall Survival: CNSREAS = 'DEATH' or AVAL for time */
    format os_censor $1.;
    if CNSREAS = 'DEATH' then os_censor = '1';
    else if CNSREAS ne '' then os_censor = '0';
    else os_censor = '';
    
    /* OS time (days) */
    os_time = AVAL; /* Time to event/censor in days */
    
    /* PFS: PROGRESSION or DEATH */
    format pfs_censor $1.;
    if CNSREAS in ('PROGRESSION', 'DEATH') then pfs_censor = '1';
    else if CNSREAS ne '' then pfs_censor = '0';
    else pfs_censor = '';
    
    pfs_time = AVAL;
    
    * Define cohort variables;
    /* Index date = first treatment date */
    index_date = trt01stdt;
    
    /* Covariates for PS model */
    age = AGE;
    sex = SEX;
    race = RACE;
    bmi = BMIBL;
    baseline_ecog = ECOG; /* ECOG performance status */
    prior_lines = NLINES; /* Number of prior lines */
    baseline_lab = LABVAL; /* Key lab value */
    
    * Additional baseline covariates as needed;
    keep SUBJID trt01an os_censor os_time pfs_censor pfs_time 
          age sex race bmi baseline_ecog prior_lines baseline_lab;
run;
```

---

## 🔄 Part 2: Propensity Score Model

```sas
/******************************************************************************
* PART 2: PROPENSITY SCORE MODEL
* Purpose: Build PS model using logistic regression or PROC PSMATCH
*****************************************************************************/

* Method 1: Using PROC LOGISTIC (traditional approach);
proc logistic data=analysis_data descending;
    class trt01an(ref='0') sex(ref='F') race;
    model trt01an = age sex race bmi baseline_ecog prior_lines baseline_lab;
    output out=ps_scores pred=ps_prob;
run;

* Method 2: Using PROC PSMATCH (modern, preferred);
proc psmatch data=analysis_data;
    class trt01an sex race;
    psvar = trt01an;
    psmodel trt01an(ref='0') = age sex race bmi baseline_ecog prior_lines baseline_lab;
    match distance=ps;
    * Alternatively: propensity;
    output out(psmatch)=psmatch_data;
run;

* Keep PS scores for IPTW calculation;
data ps_data;
    set ps_scores; /* from LOGISTIC or PSMATCH */
    keep SUBJID trt01an ps_prob;
run;
```

---

## 🔄 Part 3: Stabilized IPTW Calculation

```sas
/******************************************************************************
* PART 3: STABILIZED IPTW CALCULATION
* Purpose: Calculate stabilized weights with formula
*****************************************************************************/

* Step 3a: Calculate numerator (P(T) - treatment model only);
proc logistic data=analysis_data descending;
    model trt01an = ; * Intercept only (numerator model - no covariates);
    output out=numerator num=prob_numerator;
run;

* Step 3b: Calculate denominator (P(T|X) - full model);
proc logistic data=analysis_data descending;
    class trt01an(ref='0') sex race;
    model trt01an = age sex race bmi baseline_ecog prior_lines baseline_lab;
    output out=denominator num=prob_denominator;
run;

* Step 3c: Calculate stabilized weights;
data iptw_data;
    merge numerator(keep=SUBJID prob_numerator) 
          denominator(keep=SUBJID prob_denominator);
    by SUBJID;
    
    * Stabilized Weight Formula:
    /* 
       SW = P(T) / P(T|X)
       
       Where:
       - P(T) = probability of treatment from numerator model (marginal)
       - P(T|X) = probability of treatment from denominator model (conditional)
    */
    
    if trt01an = 1 then do;
        /* Numerator: P(T=1) = proportion treated */
        /* Denominator: P(T=1|X) from full model */
        stab_weight = prob_numerator / prob_denominator;
    end;
    else if trt01an = 0 then do;
        /* For control: (1-P(T=1)) / (1-P(T=1|X)) */
        stab_weight = (1 - prob_numerator) / (1 - prob_denominator);
    end;
    
    * Trimming: Trim weights at 1st and 99th percentiles to reduce极端值 impact;
    * (Optional - only if needed);
    /*
    proc means data=iptw_data noprint;
        var stab_weight;
        output out=pctl p1=p1 p99=p99;
    run;
    */
    
    * Create trimmed weights (example);
    if stab_weight > 10 then stab_weight = 10; /* Manual trimming threshold */
    if stab_weight < 0.1 then stab_weight = 0.1;
    
    keep SUBJID trt01an ps_prob stab_weight;
run;
```

---

## 🔄 Part 4: Balance Diagnostics

```sas
/******************************************************************************
* PART 4: BALANCE DIAGNOSTICS
* Purpose: Check covariate balance after weighting
*****************************************************************************/

* Method 1: Calculate Standardized Mean Difference (SMD);
proc means data=iptw_data noprint;
    class trt01an;
    var age sex bmi baseline_ecog prior_lines baseline_lab;
    output out=means_raw;
run;

* Weighted means (using weights);
proc means data=iptw_data noprint;
    class trt01an;
    var age bmi baseline_ecog prior_lines baseline_lab;
    weight stab_weight;
    output out=means_weighted;
run;

* Calculate SMD manually - Example for age;
proc sql;
    create table smd_calc as
    select 
        trt01an,
        mean(age) as mean_age,
        var(age) as var_age
    from iptw_data
    group by trt01an;
quit;

* Simplified SMD calculation using PROC PSMATCH;
proc psmatch data=iptw_data;
    class trt01an sex race;
    psvar = trt01an;
    psmodel trt01an(ref='0') = age sex race bmi baseline_ecog prior_lines baseline_lab;
    weight stab_weight;
    balance criteria=svd;
    output out=balance_out;
run;

* Method 2: Generate Love Plot (ASCII version);
proc sgplot data=balance_out;
    vbarparm category=covariate / response=smd_raw group=trt01an;
    yaxis label="Standardized Mean Difference";
run;

* Alternative: Output balance statistics to table;
proc psmatch data=iptw_data;
    class trt01an sex race;
    psvar = trt01an;
    psmodel trt01an(ref='0') = age sex race bmi baseline_ecog prior_lines baseline_lab;
    weight stab_weight;
    output out(psmatch_bal) 
        baltype=ksmd
        cov=SMD_before SMD_after;
run;

* Print balance table;
proc print data=psmatch_bal;
    var covariate sdm_before sdm_after;
    title "Covariate Balance: Before vs After IPTW";
run;
```

---

## 🔄 Part 5: Weighted Survival Analysis

```sas
/******************************************************************************
* PART 5: WEIGHTED SURVIVAL ANALYSIS
* Purpose: Run weighted Cox regression and Kaplan-Meier
*****************************************************************************/

* Method 1: Weighted Kaplan-Meier;
proc lifetest data=iptw_data;
    time os_time * os_censor(1='0');
    strata trt01an;
    weight stab_weight;
    plot(overlay)=survival;
    ods output ProductLimitEstimates=km_estimate;
run;

* Method 2: Weighted Cox Proportional Hazards;
proc phreg data=iptw_data;
    class trt01an(ref='0') sex(ref='F') race;
    model os_time * os_censor(1='0') = trt01an age sex race bmi baseline_ecog;
    weight stab_weight;
    robust; * Use robust SE for weighted analysis;
    title "Weighted Cox: Treatment Effect on Overall Survival";
    ods output ParameterEstimates=cox_results;
run;

* Method 3: Hazard Ratio with 95% CI;
proc phreg data=iptw_data;
    class trt01an(ref='0');
    model os_time * os_censor(1='0') = trt01an;
    weight stab_weight;
    robust;
    hazardratio 'Treatment Effect' trt01an / cl=both;
run;

* Method 4: Stratified analysis by key subgroup;
proc phreg data=iptw_data;
    class trt01an(ref='0') baseline_ecog;
    model os_time * os_censor(1='0') = trt01an baseline_ecog trt01an*baseline_ecog;
    weight stab_weight;
    robust;
    title "Interaction: Treatment * ECOG Status";
run;
```

---

## 🔄 Part 6: Sensitivity Analysis

```sas
/******************************************************************************
* PART 6: SENSITIVITY ANALYSIS
* Purpose: Additional robustness checks
*****************************************************************************/

* 1. Complete case analysis (no imputation);
proc phreg data=analysis_data;
    where missing(age) = 0 and missing(bmi) = 0;
    class trt01an(ref='0');
    model os_time * os_censor(1='0') = trt01an;
    weight stab_weight;
    robust;
run;

* 2. Different trimming thresholds;
data iptw_trim05;
    set iptw_data;
    if stab_weight < 0.5 then stab_weight = 0.5;
    if stab_weight > 5 then stab_weight = 5;
run;

proc phreg data=iptw_trim05;
    class trt01an(ref='0');
    model os_time * os_censor(1='0') = trt01an;
    weight stab_weight;
    robust;
run;

* 3. E-value for unmeasured confounding;
* Manual calculation: E-value = HR + sqrt(HR*(HR-1));
/*
   If HR = 1.5, then E-value = 1.5 + sqrt(1.5*0.5) = 1.5 + 0.866 = 2.37
   Interpretation: Unmeasured confounder would need to be associated with 
   both treatment and outcome by a risk ratio of at least 2.37 to explain away the observed effect
*/

* 4. Joiner analysis (dose-response);
proc sort data=iptw_data;
    by ps_prob;
run;

proc phreg data=iptw_data;
    model os_time * os_censor(1='0') = ps_prob;
    weight stab_weight;
    robust;
    title "Continuous PS as Dose-Response";
run;
```

---

## 📊 Complete Template Code

```sas
/******************************************************************************
* MASTER TEMPLATE: PS/IPTW ONCOLOGY SURVIVAL ANALYSIS
* Author: SAS Programmer Template
* Purpose: Real-world evidence analysis for oncology OS/PFS
* Last Updated: 2026-03-28
*****************************************************************************/

%let project = ONCOLOGY_RWE;
%let outcome = OS; /* OS or PFS */
%let treatment = trt01an;
%let covars = age sex race bmi baseline_ecog prior_lines baseline_lab;

*-------------------------------------------
* STEP 1: DATA PREPARATION
*-------------------------------------------
/* See Part 1 code above */

*-------------------------------------------
* STEP 2: PROPENSITY SCORE
*-------------------------------------------
proc psmatch data=analysis_data;
    class trt01an sex race;
    psvar = trt01an;
    psmodel trt01an(ref='0') = &covars;
    output out=ps_data;
run;

*-------------------------------------------
* STEP 3: STABILIZED IPTW
*-------------------------------------------
/* See Part 3 code - calculate stab_weight */

*-------------------------------------------
* STEP 4: BALANCE DIAGNOSTICS
*-------------------------------------------
/* See Part 4 code - check SMD < 0.1 */

*-------------------------------------------
* STEP 5: WEIGHTED SURVIVAL ANALYSIS
*-------------------------------------------
proc phreg data=iptw_data;
    class trt01an(ref='0');
    model os_time * os_censor(1='0') = trt01an;
    weight stab_weight;
    robust;
    hazardratio 'Treatment' trt01an / cl=both;
run;

*-------------------------------------------
* STEP 6: SENSITIVITY
*-------------------------------------------
/* See Part 6 code */
```

---

## 🎯 Key Output Interpretation

| Metric | Target | Interpretation |
|--------|--------|----------------|
| SMD | < 0.10 | Good balance |
| SMD | 0.10-0.20 | Acceptable |
| SMD | > 0.20 | Poor balance - need more covariates |
| Weight range | 0.1-10 | Reasonable |
| HR (Treatment) | - | Hazard ratio for treatment |
| 95% CI | - | Confidence interval |
| E-value | > 2.0 | Robust to unmeasured confounding |

---

## 🔗 Next Steps

This template can be adapted for:
1. **PFS outcome**: Change `os_censor`/`os_time` to `pfs_censor`/`pfs_time`
2. **Different covariates**: Modify `covars` macro variable
3. **Multiple treatments**: Use multinomial PS or stratification
4. **Time-varying treatment**: Use IPCW (inverse probability of censoring weights)

---

*Template completed: 2026-03-28*
*Ready for oncology RWE projects*