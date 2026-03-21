# SAS Derivation Framework
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly
### Three-Treatment-Line Model: Surgery + GKS + Endocrinology

---

## 1. Program Structure

```
/sdtm_to_adam
├── 01_build_dm.sas
├── 02_build_pr_cm_lb_fa_rs_tr_ae.sas
├── 03_build_adsl.sas
├── 04_build_adendo.sas
├── 05_build_adimg.sas
├── 06_build_adrad.sas
├── 07_build_adpit.sas
├── 08_build_adint.sas
├── 09_build_adtte_ttrrem.sas
├── 10_build_adtte_ttrrec.sas
├── 11_build_adtte_ttprog.sas
├── 12_build_adtte_tthypo.sas
├── 13_build_adtte_ttsalv.sas
├── 14_build_adtte_os.sas
└── 15_stack_adtte.sas
```

---

## 2. ADSL Derivation

### 2.1 Step 1: Get Index GKS Date

```sas
/* Get first eligible Gamma Knife radiosurgery date */
proc sort data=pr out=pr_gks;
    where upcase(prcat)='RADIOSURGERY' 
          and upcase(prtrt) contains 'GAMMA';
    by usubjid prstdtc;
run;

data gks_index;
    set pr_gks;
    by usubjid prstdtc;
    if first.usubjid;
    indexdt = input(prstdtc, yymmdd10.);
    format indexdt yymmdd10.;
    keep usubjid indexdt;
run;
```

### 2.2 Step 2: Surgery Summary

```sas
/* Get prior surgeries before index GKS */
proc sort data=pr out=pr_surg;
    where upcase(prcat)='SURGICAL PROCEDURE';
    by usubjid prstdtc;
run;

proc sql;
    create table surg_sum as
    select a.usubjid,
           a.indexdt,
           count(b.prstdtc) as prior_surg_n,
           max(input(b.prstdtc,yymmdd10.)) as lastsurgdt format=yymmdd10.
    from gks_index as a
    left join pr_surg as b
        on a.usubjid = b.usubjid
        and input(b.prstdtc,yymmdd10.) < a.indexdt
    group by a.usubjid, a.indexdt;
quit;

data surg_sum;
    set surg_sum;
    surg2gks_days = indexdt - lastsurgdt;
    surg2gks_mos = surg2gks_days / 30.4375;
    if not missing(surg2gks_mos) then 
        earlygks_fl = ifc(surg2gks_mos <= 12, 'Y', 'N');
    else earlygks_fl = '';
    drop indexdt;
run;
```

### 2.3 Step 3: Baseline Endocrine

```sas
/* Get baseline endocrine values - closest to index GKS */
proc sort data=lb out=lb_endo;
    where lbtestcd in ('IGF1','GH','OGTTGH');
    by usubjid lbdtc;
run;

data lb_pre;
    merge lb_endo(in=a) gks_index(keep=usubjid indexdt);
    by usubjid;
    lbdt = input(lbdtc, yymmdd10.);
    if a and lbdt <= indexdt;
    diff = indexdt - lbdt;
run;

proc sort data=lb_pre;
    by usubjid lbtestcd diff lbdt;
run;

data lb_base;
    set lb_pre;
    by usubjid lbtestcd;
    if first.lbtestcd;
run;

/* Transpose to wide format */
proc transpose data=lb_base out=lb_base_wide prefix=BASE_;
    by usubjid;
    id lbtestcd;
    var lbstresn;
run;

/* Get ULN values */
data lb_uln;
    set lb_endo;
    where upcase(lbtestcd) = 'IGF1';
    keep usubjid lbdtc lbstnrhi;
run;

proc sort data=lb_uln;
    by usubjid lbdtc;
run;

data lb_uln_base;
    set lb_uln;
    by usubjid;
    if first.usubjid;
    rename lbstnrhi = base_igf1_uln;
run;

/* Merge and calculate IGF1I */
data lb_base_final;
    merge lb_base_wide lb_uln_base(keep=usubjid base_igf1_uln);
    by usubjid;
    if not missing(BASE_IGF1) and not missing(base_igf1_uln) and base_igf1_uln > 0 then
        BASE_IGF1I = BASE_IGF1 / base_igf1_uln;
run;
```

### 2.4 Step 4: GKS Parameters from FA

```sas
/* Get GKS parameters from FA */
proc sort data=fa out=fa_gks;
    where upcase(fatestcd) in ('PLANTYPE','BED','TARGETVOL','MARGDOSE','MAXDOSE','ISODOSE','OPTICDOSE');
    by usubjid fadtc;
run;

proc transpose data=fa_gks out=fa_gks_wide prefix=FA_;
    by usubjid;
    id fatestcd;
    var fastresc fastresn;
run;
```

### 2.5 Step 5: Medication Status

```sas
/* Get medication status at GKS */
proc sort data=cm out=cm_gks;
    where upcase(cmcat) = 'ACROMEGALY TREATMENT';
    by usubjid cmstdtc;
run;

/* Determine if on medication at GKS */
proc sql;
    create table med_at_gks as
    select a.usubjid,
           a.indexdt,
           b.cmstdtc,
           b.cmendtc,
           case when missing(b.cmendtc) then 'Y'
                when input(b.cmendtc,yymmdd10.) >= a.indexdt then 'Y'
                else 'N'
           end as on_med_at_gks
    from gks_index as a
    left join cm_gks as b
        on a.usubjid = b.usubjid
        and input(b.cmstdtc,yymmdd10.) <= a.indexdt
    group by a.usubjid
    having min(on_med_at_gks) = 'Y';
quit;

/* Medication hold status from FA */
proc sort data=fa out=fa_medhold;
    where upcase(fatestcd) = 'MEDHOLD';
    by usubjid fadtc;
run;

data fa_medhold_latest;
    set fa_medhold;
    by usubjid fadtc;
    if last.usubjid;
run;
```

### 2.6 Step 6: Build Final ADSL

```sas
data adsl;
    merge 
        dm(keep=usubjid siteid age sex)
        gks_index
        surg_sum
        lb_base_final(keep=usubjid base_igf1 base_gh base_ogttgh base_igf1i)
        fa_gks_wide
        med_at_gks(keep=usubjid on_med_at_gks)
        fa_medhold_latest(keep=usubjid fastresc rename=(fastresc=medhold_fl))
        ds(keep=usubjid dsstdtc dsdcod rename=(dsstdtc=fupdt))
        ;
    by usubjid;
    
    /* Derived variables */
    if not missing(surg2gks_mos) and surg2gks_mos <= 12 then earlygks_fl = 'Y';
    else if not missing(surg2gks_mos) then earlygks_fl = 'N';
    
    if on_med_at_gks = 'Y' and medhold_fl = 'Y' then medhold_cat = 'ON_MED_HOLD';
    else if on_med_at_gks = 'Y' then medhold_cat = 'ON_MED_NO_HOLD';
    else if on_med_at_gks = 'N' then medhold_cat = 'NO_MED';
    else medhold_cat = 'UNKNOWN';
    
    /* Follow-up */
    fup_days = fupdt - indexdt;
    fup_mos = fup_days / 30.4375;
    
    /* Flags */
    fasfl = 'Y';
    effl = 'Y';
    imgevifl = 'Y';
    saffl = 'Y';
    
    label 
        usubjid = "Unique Subject Identifier"
        indexdt = "Index GKS Date"
        surg2gks_mos = "Months from Surgery to GKS"
        earlygks_fl = "Early GKS Flag"
        base_igf1i = "Baseline IGF-1 Index"
        medhold_cat = "Medication Hold Category"
        fup_days = "Follow-up Days"
        fup_mos = "Follow-up Months";
    
    format indexdt fupdt yymmdd10.;
run;
```

---

## 3. ADENDO Derivation

### 3.1 Get Post-GKS Endocrine Records

```sas
/* Get all post-GKS endocrine assessments */
proc sort data=lb out=lb_post;
    where lbtestcd in ('IGF1','GH','OGTTGH');
    by usubjid lbdtc;
run;

data lb_post_adt;
    merge lb_post(in=a) adsl(keep=usubjid indexdt);
    by usubjid;
    if a and input(lbdtc,yymmdd10.) > indexdt;
    adt = input(lbdtc, yymmdd10.);
    ady = adt - indexdt + 1;
    format adt yymmdd10.;
run;

proc sort data=lb_post_adt;
    by usubjid adt lbtestcd;
run;

/* Transpose to wide format per date */
proc transpose data=lb_post_adt out=endo_wide prefix=LAB_;
    by usubjid adt ady;
    id lbtestcd;
    var lbstresn;
run;
```

### 3.2 Add Medication Status

```sas
/* Add on-med status at each assessment */
proc sql;
    create table adendo_pre as
    select a.*,
           b.cmstdtc as med_start,
           b.cmendtc as med_end
    from endo_wide as a
    left join cm_gks as b
        on a.usubjid = b.usubjid
        and input(b.cmstdtc,yymmdd10.) <= a.adt
        and (missing(b.cmendtc) or input(b.cmendtc,yymmdd10.) >= a.adt);
quit;

data adendo;
    set adendo_pre;
    
    /* Determine on medication at assessment */
    if not missing(med_start) then on_med = 'Y';
    else on_med = 'N';
    
    /* Calculate IGF1I */
    if not missing(LAB_IGF1) and not missing(IGF1_ULN) and IGF1_ULN > 0 then
        IGF1I = LAB_IGF1 / IGF1_ULN;
    
    /* Determine endocrine status */
    length endo_status $20;
    if not missing(IGF1I) then do;
        if IGF1I <= 1 and on_med = 'N' then do;
            if missing(LAB_OGTTGH) or LAB_OGTTGH < 0.4 then 
                endo_status = 'BIOCHEM_REM';
            else endo_status = 'INDETERMINATE';
        end;
        else if IGF1I <= 1 and on_med = 'Y' then 
            endo_status = 'ENDO_CONTROL';
        else if IGF1I > 1 then 
            endo_status = 'UNCONTROLLED';
    end;
    
    label 
        adt = "Assessment Date"
        ady = "Analysis Day"
        IGF1I = "IGF-1 Index"
        LAB_GH = "Growth Hormone"
        LAB_OGTTGH = "OGTT Nadir GH"
        on_med = "On Medication"
        endo_status = "Endocrine Status";
run;
```

### 3.3 Identify First Remission

```sas
proc sort data=adendo;
    by usubjid adt;
run;

data adendo_flag;
    set adendo;
    by usubjid adt;
    retain firstrem_fl postrem_fl;
    
    if first.usubjid then do;
        firstrem_fl = 'N';
        postrem_fl = 'N';
    end;
    
    if endo_status = 'BIOCHEM_REM' and firstrem_fl = 'N' then do;
        firstrem_fl = 'Y';
    end;
    
    if firstrem_fl = 'Y' then postrem_fl = 'Y';
    
    label 
        firstrem_fl = "First Remission Flag"
        postrem_fl = "Post-Remission Flag";
run;
```

---

## 4. ADTTE Derivation

### 4.1 TTRREM - Time to First Endocrine Remission

```sas
proc sort data=adendo_flag;
    by usubjid adt;
run;

data rem_summ;
    set adendo_flag;
    by usubjid adt;
    retain firstremdt lastendodt remiss_fl;
    
    if first.usubjid then do;
        firstremdt = .;
        lastendodt = .;
        remiss_fl = 'N';
    end;
    
    lastendodt = adt;
    
    if endo_status = 'BIOCHEM_REM' and missing(firstremdt) then do;
        firstremdt = adt;
        remiss_fl = 'Y';
    end;
    
    if last.usubjid then output;
run;

data adtte_ttrrem;
    merge adsl(keep=usubjid indexdt) rem_summ(keep=usubjid firstremdt lastendodt remiss_fl);
    by usubjid;
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'TTRREM';
    param = 'Time to First Endocrine Remission';
    startdt = indexdt;
    
    if remiss_fl = 'Y' then do;
        adt = firstremdt;
        cnsr = 0;
        evntdesc = 'First biochemical remission';
    end;
    else do;
        adt = lastendodt;
        cnsr = 1;
        evntdesc = 'Censored at last endocrine assessment';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.2 TTRREC - Time to Biochemical Recurrence

```sas
/* Get post-remission records only */
data adendo_postrem;
    merge adendo_flag(in=a) rem_summ(keep=usubjid firstremdt remiss_fl);
    by usubjid;
    if a and remiss_fl = 'Y' and adt > firstremdt;
run;

proc sort data=adendo_postrem;
    by usubjid adt;
run;

data rec_summ;
    set adendo_postrem;
    by usubjid adt;
    retain recurrdt recurr_fl lastpostremdt;
    
    if first.usubjid then do;
        recurrdt = .;
        recurr_fl = 'N';
        lastpostremdt = .;
    end;
    
    lastpostremdt = adt;
    
    /* Recurrence: IGF1I > 1 after prior remission */
    if IGF1I > 1 and missing(recurrdt) then do;
        recurrdt = adt;
        recurr_fl = 'Y';
    end;
    
    if last.usubjid then output;
run;

data adtte_ttrrec;
    merge rem_summ(keep=usubjid firstremdt remiss_fl) 
          rec_summ(keep=usubjid recurrdt recurr_fl lastpostremdt);
    by usubjid;
    if remiss_fl = 'Y';
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'TTRREC';
    param = 'Time to Biochemical Recurrence';
    startdt = firstremdt;
    
    if recurr_fl = 'Y' then do;
        adt = recurrdt;
        cnsr = 0;
        evntdesc = 'Biochemical recurrence';
    end;
    else do;
        adt = lastpostremdt;
        cnsr = 1;
        evntdesc = 'Censored after remission';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.3 TTPROG - Time to Radiographic Progression

```sas
/* Get post-GKS MRI assessments */
data adimg_post;
    merge tr(in=a where=(upcase(trtestcd)='TUMVOL')) 
          adsl(keep=usubjid indexdt);
    by usubjid;
    if a and input(trdtc,yymmdd10.) > indexdt;
    adt = input(trdtc, yymmdd10.);
    ady = adt - indexdt + 1;
    format adt yymmdd10.;
run;

/* Calculate volume change */
proc sort data=adimg_post;
    by usubjid trdtc;
run;

data adimg_calc;
    set adimg_post;
    by usubjid trdtc;
    retain base_vol nadir_vol;
    
    if first.usubjid then do;
        base_vol = .;
        nadir_vol = .;
    end;
    
    /* First record as baseline */
    if base_vol = . and not missing(trstresn) then base_vol = trstresn;
    
    /* Track nadir */
    if not missing(trstresn) and (nadir_vol = . or trstresn < nadir_vol) then 
        nadir_vol = trstresn;
    
    /* Calculate percent change from baseline */
    if not missing(base_vol) and base_vol > 0 and not missing(trstresn) then 
        volchg_pct = (trstresn - base_vol) / base_vol * 100;
    
    /* Determine progression */
    if volchg_pct > 20 or upcase(mriresp) = 'PROGRESSED' then prog_fl = 'Y';
    else prog_fl = 'N';
run;

proc sort data=adimg_calc;
    by usubjid adt;
run;

data prog_summ;
    set adimg_calc;
    by usubjid adt;
    retain progdt lastmridt;
    
    if first.usubjid then do;
        progdt = .;
        lastmridt = .;
    end;
    
    lastmridt = adt;
    
    if prog_fl = 'Y' and missing(progdt) then do;
        progdt = adt;
    end;
    
    if last.usubjid then output;
run;

data adtte_ttprog;
    merge adsl(keep=usubjid indexdt) prog_summ(keep=usubjid progdt prog_fl lastmridt);
    by usubjid;
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'TTPROG';
    param = 'Time to Radiographic Progression';
    startdt = indexdt;
    
    if prog_fl = 'Y' then do;
        adt = progdt;
        cnsr = 0;
        evntdesc = 'Radiographic progression';
    end;
    else do;
        adt = lastmridt;
        cnsr = 1;
        evntdesc = 'Censored at last MRI';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.4 TTHYPO - Time to New Hypopituitarism

```sas
/* Get pituitary function assessments */
proc sort data=adpit;
    by usubjid adt;
run;

data hypo_summ;
    set adpit;
    by usubjid adt;
    retain hypodt hypopit_fl lastpitdt;
    
    if first.usubjid then do;
        hypodt = .;
        hypopit_fl = 'N';
        lastpitdt = .;
    end;
    
    lastpitdt = adt;
    
    if new_def_fl = 'Y' and missing(hypodt) then do;
        hypodt = adt;
        hypopit_fl = 'Y';
    end;
    
    if last.usubjid then output;
run;

data adtte_tthypo;
    merge adsl(keep=usubjid indexdt) hypo_summ(keep=usubjid hypodt hypopit_fl lastpitdt);
    by usubjid;
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'TTHYPO';
    param = 'Time to New Hypopituitarism';
    startdt = indexdt;
    
    if hypopit_fl = 'Y' then do;
        adt = hypodt;
        cnsr = 0;
        evntdesc = 'New hypopituitarism';
    end;
    else do;
        adt = lastpitdt;
        cnsr = 1;
        evntdesc = 'Censored at last pituitary assessment';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.5 TTSALV - Time to Salvage Intervention

```sas
/* Get salvage interventions */
proc sort data=adint;
    by usubjid intdt;
run;

data salv_summ;
    set adint;
    by usubjid intdt;
    retain salvdt salvage_fl lastfupt;
    
    if first.usubjid then do;
        salvdt = .;
        salvage_fl = 'N';
    end;
    
    /* First intervention after index GKS */
    if missing(salvdt) and input(intdt,yymmdd10.) > indexdt then do;
        salvdt = input(intdt,yymmdd10.);
        salvage_fl = 'Y';
    end;
    
    /* Get last follow-up from ADSL */
    /* Merge in next step */
    if last.usubjid then output;
run;

data adtte_ttsalv;
    merge adsl(keep=usubjid indexdt fupdt) 
          salv_summ(keep=usubjid salvdt salvage_fl);
    by usubjid;
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'TTSALV';
    param = 'Time to Salvage Intervention';
    startdt = indexdt;
    
    if salvage_fl = 'Y' then do;
        adt = salvdt;
        cnsr = 0;
        evntdesc = 'Salvage intervention';
    end;
    else do;
        adt = fupdt;
        cnsr = 1;
        evntdesc = 'Censored at last follow-up';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.6 OS - Overall Survival

```sas
data adtte_os;
    set adsl(keep=usubjid indexdt fupdt deathdt death_fl);
    
    length paramcd $8 param $40 evntdesc $60;
    paramcd = 'OS';
    param = 'Overall Survival';
    startdt = indexdt;
    
    if death_fl = 'Y' then do;
        adt = deathdt;
        cnsr = 0;
        evntdesc = 'Death';
    end;
    else do;
        adt = fupdt;
        cnsr = 1;
        evntdesc = 'Censored alive';
    end;
    
    aval = adt - startdt + 1;
    
    format startdt adt yymmdd10.;
    
    keep studyid usubjid paramcd param startdt adt cnsr aval evntdesc;
run;
```

### 4.7 Stack All ADTTE

```sas
data adtte;
    set adtte_ttrrem
        adtte_ttrrec
        adtte_ttprog
        adtte_tthypo
        adtte_ttsalv
        adtte_os;
    by usubjid paramcd;
    
    label 
        paramcd = "Parameter Code"
        param = "Parameter"
        startdt = "Start Date"
        adt = "Event/Censor Date"
        cnsr = "Censoring Indicator"
        aval = "Analysis Value"
        evntdesc = "Event Description";
run;

proc sort data=adtte;
    by usubjid paramcd;
run;
```

---

## 5. Three-Treatment-Line Integration

### 5.1 Surgery Variables in ADSL

| Variable | Source | Description |
|----------|--------|-------------|
| PRIOR_SURG_N | PR | Number of prior surgeries |
| LASTSURGDT | PR | Last surgery date |
| SURG2GKS_MOS | Derived | Months from surgery to GKS |
| EARLYGKS_FL | Derived | Early GKS flag |
| RESECT_TYPE | FA | Resection extent |

### 5.2 GKS Variables in ADRAD

| Variable | Source | Description |
|----------|--------|-------------|
| GKSDT | PR | GKS date |
| PLAN_TYPE | FA | Plan type |
| TARGETVOL_CC | FA/PR | Target volume |
| MARGINDOSE | FA | Margin dose |
| MAXDOSE | FA | Maximum dose |
| ISODOSE | FA | Isodose line |
| OPTICMAX | FA | Optic max dose |
| BED | FA | Biologically effective dose |

### 5.3 Endocrinology Variables in ADENDO

| Variable | Source | Description |
|----------|--------|-------------|
| IGF1I | LB Derived | IGF-1 Index |
| GH | LB | Growth Hormone |
| OGTTGH | LB | OGTT nadir GH |
| ON_MED | CM/FA | On medication |
| ENDO_STATUS | Derived | Endocrine status |

---

## 6. Key QC Checks

### 6.1 ADSL QC

- One row per USUBJID
- INDEXDT not missing
- No negative FUP_DAYS
- BASELINE values <= INDEXDT
- SURGERY dates < INDEXDT

### 6.2 ADENDO QC

- ADT > INDEXDT for all records
- IGF1I calculation verified
- ENDO_STATUS assigned correctly
- FIRSTREM_FL appears only once per subject

### 6.3 ADTTE QC

- STARTDT = INDEXDT (except TTRREC = first remission date)
- No negative AVAL
- CNSR = 0 for events, 1 for censored
- No duplicate PARAMCD per subject

---

## 7. Summary

This framework integrates:

1. **Surgery Line** - PRIOR_SURG_N, SURG2GKS_MOS, EARLYGKS_FL
2. **Gamma Knife Line** - PLAN_TYPE, MARGINDOSE, BED, OPTICMAX
3. **Endocrinology Line** - IGF1I, ON_MED, ENDO_STATUS, TTRREM/TTRREC

The ADTTE dataset contains 6 key endpoints:
- TTRREM (Time to First Remission)
- TTRREC (Time to Recurrence)
- TTPROG (Time to Progression)
- TTHYPO (Time to Hypopituitarism)
- TTSALV (Time to Salvage)
- OS (Overall Survival)

---

*Document created: 2026-03-21*
*Version: Production Ready*
