# ADaM Dataset General Template

## Overview
This template provides a framework for creating analysis-ready datasets following CDISC ADaM standards for oncology clinical trials.

## Dataset Types

### 1. ADSL (Subject-Level Analysis Dataset)
```sas
/* ADSL Variable Template */
data adsl;
    set raw.raw_subject;
    
    /* Required Variables */
    STUDYID = strip(study_id);
    SUBJID = strip(subject_id);
    USUBJID = catx("-", STUDYID, SUBJID);
    SITEID = strip(site_id);
    ARMCD = strip(arm_code);
    ARM = strip(arm_description);
    
    /* Demographics */
    AGE = age;
    AGEGR1 = ifc(age < 65, "<65", ">=65");
    SEX = strip(sex);
    RACE = strip(race);
    RACEGN = ifc(race in ("WHITE"), "White", "Non-White");
    
    /* Country */
    COUNTRY = strip(country);
    
    /* Informed Consent */
    RFICDTC = strip(rfic_date);
    
    /* Randomization */
    RANDDT = rand_date;
    ARM = strip(assigned_arm);
    
    /* Disposition */
    DSCAT = strip(disposition_category);
    DSSTDTC = strip(disposition_date);
    DSDECOD = strip(disposition_reason);
    
    /* Treatment Exposure */
    TRTSDT = strip(treatment_start_date);
    TRTEDT = strip(treatment_end_date);
    TRTDUR = duration_days;
    TRTP = strip(treatment);
    TRTPN = input(treatment, 3.);
    
    /* Safety Population Flag */
    SAFFL = ifc(safety_pop="Y", "Y", "N");
    
    /* ITT Population Flag */
    ITTFL = ifc(itt_pop="Y", "Y", "N");
    
    /* Derived Variables */
    if TRTSDT ne "" and TRTEDT ne "" then do;
        TRTDUR = input(TRTEDT, yymmdd10.) - input(TRTSDT, yymmdd10.) + 1;
    end;
    
    format _all_;
    keep STUDYID SUBJID USUBJID SITEID ARMCD ARM AGE AGEGR1 SEX RACE 
         RACEGN COUNTRY RFICDTC RANDDT DSCAT DSSTDTC DSDECOD 
         TRTSDT TRTEDT TRTDUR TRTP TRTPN SAFFL ITTFL;
run;
```

### 2. ADAE (Adverse Events Dataset)
```sas
/* ADAE Variable Template */
data adae;
    set raw.ae_data;
    
    /* Identification */
    STUDYID = strip(study_id);
    SUBJID = strip(subject_id);
    USUBJID = catx("-", STUDYID, SUBJID);
    SITEID = strip(site_id);
    
    /* Event Details */
    AETERM = strip(ae_term);
    AEDECOD = strip(pt_term);
    AESOC = strip(soc_term);
    AEBODSYS = strip(body_system);
    
    /* Event Classification */
    AETOXGR = strip(toxicity_grade);
    AESER = ifc(serious="Y", "Y", "N");
    AESEV = strip(severity);
    
    /* Date Variables */
    AESTDTC = strip(ae_start_date);
    AEENDTC = strip(ae_end_date);
    AEDUR = ae_duration;
    AESTDY = input(AESTDTC, yymmdd10.) - input(RFICDTC, yymmdd10.) + 1;
    
    /* Relationship */
    AEREL = strip(relatedness);
    AECONTRT = ifc(concomitant_med="Y", "Y", "N");
    
    /* Outcome */
    AEOUT = strip(outcome);
    
    /* Action Taken */
    AEACN = strip(action_taken);
    
    /* Safety Flag */
    SAFFL = ifc(safety_pop="Y", "Y", "N");
    
    /* Treatment Variables */
    TRTP = strip(treatment);
    TRTA = strip(actual_treatment);
    
    format _all_;
    keep STUDYID SUBJID USUBJID SITEID AETERM AEDECOD AESOC AEBODSYS
         AETOXGR AESER AESEV AESTDTC AEENDTC AEDUR AESTDY 
         AEREL AECONTRT AEOUT AEACN SAFFL TRTP TRTA;
run;
```

### 3. ADTTE (Time-to-Event Dataset)
```sas
/* ADTTE Variable Template */
data adtte;
    set raw.tt_data;
    
    /* Identification */
    STUDYID = strip(study_id);
    SUBJID = strip(subject_id);
    USUBJID = catx("-", STUDYID, SUBJID);
    SITEID = strip(site_id);
    
    /* Event Parameters */
    PARAM = strip(endpoint);
    PARAMCD = endpoint_code;
    PARAMN = input(endpoint_code, 3.);
    
    /* Time to Event */
    CNSR = ifc(event_observed="N", 1, 0);
    CENSOR = CNSR;
    EVNTDESC = strip(event_description);
    SRVDESC = strip(censor_reason);
    
    /* Time Variables */
    ADT = analysis_date;
    STARTDT = baseline_date;
    
    /* Calculate Time */
    if ADT ne "" and STARTDT ne "" then do;
        AVAL = input(ADT, yymmdd10.) - input(STARTDT, yymmdd10.);
    end;
    
    /* Time Unit */
    AVALU = "DAYS";
    
    /* Treatment */
    TRTP = strip(treatment);
    TRTA = strip(actual_treatment);
    TRTAN = input(TRTA, 3.);
    
    /* Analysis Flags */
    ANAL1FL = "Y";
    SRSCAT = strip(subgroup);
    
    format ADT STARTDT yymmdd10.;
    keep STUDYID SUBJID USUBJID SITEID PARAM PARAMCD PARAMN 
         CNSR CENSOR EVNTDESC SRVDESC ADT STARTDT AVAL AVALU 
         TRTP TRTA TRTAN ANAL1FL SRSCAT;
run;
```

### 4. ADLB (Laboratory Dataset)
```sas
/* ADLB Variable Template */
data adlb;
    set raw.lab_data;
    
    /* Identification */
    STUDYID = strip(study_id);
    SUBJID = strip(subject_id);
    USUBJID = catx("-", STUDYID, SUBJID);
    SITEID = strip(site_id);
    
    /* Lab Parameters */
    LBTEST = strip(lab_test);
    LBTESTCD = lab_test_code;
    LBORRES = strip(original_result);
    LBORRESU = strip(result_unit);
    
    /* Standardized Results */
    LBSTRES = strip(standardized_result);
    LBSTRESN = standardized_result_num;
    LBSTRESC = strip(character_result);
    LBSTRESU = strip(standardized_unit);
    
    /* Reference Range */
    LBORNRLO = strip(low_normal_range);
    LBORNRHI = strip(high_normal_range);
    LBNRIND = strip(reference_range_indicator);
    
    /* Baseline */
    BASE = baseline_value;
    CHG = input(LBSTRESN, best12.) - BASE;
    PCHG = (CHG / BASE) * 100;
    
    /* Flags */
    ABLFL = ifc(baseline_flag="Y", "Y", "N");
    ANL01FL = ifc(analysis_flag="Y", "Y", "N");
    
    /* Visit */
    VISITNUM = visit_number;
    VISIT = strip(visit_name);
    
    /* Treatment */
    TRTP = strip(treatment);
    TRTA = strip(actual_treatment);
    
    /* Safety Population */
    SAFFL = ifc(safety_pop="Y", "Y", "N");
    
    format _all_;
    keep STUDYID SUBJID USUBJID SITEID LBTEST LBTESTCD LBORRES 
         LBORRESU LBSTRES LBSTRESN LBSTRESC LBSTRESU LBORNRLO 
         LBORNRHI LBNRIND BASE CHG PCHG ABLFL ANL01FL VISITNUM 
         VISIT TRTP TRTA SAFFL;
run;
```

## Common Derivation Rules

### Date Handling
```sas
/* Convert ISO date to SAS date */
ADT = input(strip(ADTC), yymmdd10.);
format ADT yymmdd10.;
```

### Baseline Derivation
```sas
/* Derive baseline from screening visit */
proc sort data=adlb;
    by usubjid lbtest visitnum;
run;

data adlb_base;
    set adlb;
    by usubjid lbtest visitnum;
    if first.lbtest and ablfl="Y" then base_val = lbstresn;
    retain base_val;
run;
```

### Treatment Emergent Flag
```sas
/* Flag treatment-emergent adverse events */
if input(aestdtc, yymmdd10.) >= input(trtsdtc, yymmdd10.) and 
   input(aestdtc, yymmdd10.) <= (input(trtsdtc, yymmdd10.) + 30) 
then TEAFL = "Y";
else TEAFL = "N";
```

## Standard Format Codes

### Sex
```sas
format $SEX. 'M'='Male' 'F'='Female' 'UNK'='Unknown';
```

### Race
```sas
format $RACE. 'WHITE'='White' 'BLACK'='Black or African American' 
                 'ASIAN'='Asian' 'AMERIND'='American Indian or Alaska Native'
                 'MULTIPLE'='Multiple' 'UNKNOWN'='Unknown';
```

### Toxicity Grade
```sas
format $GRADE. '1'='Grade 1' '2'='Grade 2' '3'='Grade 3' 
               '4'='Grade 4' '5'='Grade 5';
```

## QC Checklist
- [ ] Verify all required variables present
- [ ] Check variable formats and lengths
- [ ] Validate derivations against specifications
- [ ] Confirm population flags consistency
- [ ] Cross-check with source data
- [ ] Review for duplicate records
- [ ] Verify treatment dates alignment
- [ ] Check baseline derivations
- [ ] Validate censoring flags for time-to-event
- [ ] Document all derivation logic
