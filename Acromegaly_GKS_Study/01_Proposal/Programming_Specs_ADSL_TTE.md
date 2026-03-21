# Programming Specifications

## Study: GKS for Cavernous Sinus–Invading Acromegaly

---

## Part 1: ADSL Specification

### 1.1 Dataset Name
**ADSL** - Subject-Level Analysis Dataset

### 1.2 Purpose
Subject-level analysis dataset for:
- Population flags
- Baseline characteristics
- Prior treatment summary
- Index GKS treatment summary
- Follow-up summary
- Subject-level outcome flags

### 1.3 Grain
One record per subject

### 1.4 Primary Sources
- STG_DEMO
- STG_ELIG
- STG_SURG
- STG_MEDHX
- STG_ENDO
- STG_IMG
- STG_GKS
- STG_FU
- Endpoint summary datasets

### 1.5 Build Steps

**Step A:** Start from eligible subject frame
- Inner join STG_DEMO + STG_ELIG (ELIGIBLE_FL='Y') + STG_GKS

**Step B:** Merge surgery summary

**Step C:** Merge medication summary

**Step D:** Merge baseline endocrine

**Step E:** Merge baseline imaging

**Step F:** Merge GKS details

**Step G:** Merge follow-up summary

**Step H:** Merge endpoint flags/dates

---

### 1.6 Key Variable Specification

| Variable | Type | Label | Source | Derivation |
|----------|------|-------|--------|------------|
| STUDYID | Char | Study Identifier | constant | fixed |
| USUBJID | Char | Unique Subject ID | STG_DEMO | STUDY_SUBJID |
| SITEID | Char | Site ID | STG_DEMO | direct |
| SUBJECT_ID | Char | Local Subject ID | STG_DEMO | direct |
| COUNTRY | Char | Country | STG_DEMO | direct |
| AGE | Num | Age at Index GKS | STG_DEMO | direct |
| SEX | Char | Sex | STG_DEMO | mapped |
| INDEXDT | Num | Index GKS Date | STG_GKS | GKS_DT |
| FASFL | Char | Full Analysis Set Flag | STG_ELIG | Y if eligible |
| EFFL | Char | Endocrine Evaluable Flag | STG_ELIG/ENDO | Y if baseline + post-GKS |
| IMGEVLFL | Char | Imaging Evaluable Flag | STG_ELIG/IMG | Y if post-GKS MRI |
| SAFFL | Char | Safety Analysis Flag | STG_GKS/FU | Y if GKS + follow-up |

---

### 1.7 Surgery Summary Variables

**Source:** STG_SURG

**Preprocessing:** Keep surgeries with valid date < INDEXDT

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| PRIOR_SURG_N | Num | Number of Prior Surgeries | count before INDEXDT |
| LASTSURGDT | Num | Last Surgery Date | max date < INDEXDT |
| SURG2GKS_DAYS | Num | Days from Surgery to GKS | INDEXDT - LASTSURGDT |
| SURG2GKS_MOS | Num | Months from Surgery to GKS | SURG2GKS_DAYS / 30.4375 |
| EARLYGKS_FL | Char | Early GKS Flag | Y if <=12 months |

---

### 1.8 Medication Summary Variables

**Source:** STG_MEDHX

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| PRIOR_MEDS_FL | Char | Prior Medical Therapy | Y if any med before/on GKS |
| MEDSTAT_GKS | Char | Medication Status at GKS | ON/OFF/NONE/UNKNOWN |
| MEDHOLD_FL | Char | Peri-GKS Hold Flag | Y if held around GKS |
| MEDHOLD_CAT | Char | Hold Category | NO_MED/ON_MED_NO_HOLD/ON_MED_HOLD |

---

### 1.9 Baseline Endocrine Variables

**Source:** STG_ENDO

**Selection Rule:**
1. ENDO_REL='PRE'
2. Prefer ENDO_BASE_FL='Y' if unique
3. Else closest to INDEXDT
4. Prefer non-missing IGF1/ULN

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| BASE_ENDODT | Num | Baseline Date | selected pre-GKS date |
| BASE_IGF1 | Num | Baseline IGF-1 | direct |
| BASE_IGF1_ULN | Num | Baseline ULN | direct |
| BASE_IGF1I | Num | Baseline IGF-1 Index | BASE_IGF1 / BASE_IGF1_ULN |
| BASE_GH | Num | Baseline GH | direct |
| BASE_OGTTGH | Num | Baseline OGTT Nadir | direct |
| BASE_ONMED | Char | On Med at Baseline | direct |
| BASE90_FL | Char | Within 90 Days | Y if INDEXDT-BASE ≤90 |
| BASE180_FL | Char | Within 180 Days | Y if INDEXDT-BASE ≤180 |

---

### 1.10 Baseline Imaging Variables

**Source:** STG_IMG

**Selection Rule:** Similar to endocrine - closest pre-GKS MRI

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| BASE_IMGDT | Num | Baseline MRI Date | selected |
| KNOSP | Num | Knosp Grade | direct |
| KNOSPGR | Char | Knosp Group | 1-2 vs 3-4 |
| CSI_DEF_TYPE | Char | CSI Definition | mapped |
| BASE_TUMVOL | Num | Baseline Volume | direct |
| BASE_LOC | Char | Residual Location | from flags |
| RESIDUAL_CS_FL | Char | CS Residual Flag | direct |

---

### 1.11 GKS Variables

**Source:** STG_GKS

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| GKS_ROLE | Char | Role of GKS | mapped |
| PLAN_TYPE | Char | Plan Type | mapped |
| TARGETED_FL | Char | Targeted Flag | Y if Targeted |
| WHOLESELLA_FL | Char | Whole-Sella Flag | Y if Whole-sella |
| MARGINDOSE | Num | Margin Dose (Gy) | direct |
| MAXDOSE | Num | Maximum Dose (Gy) | direct |
| ISODOSE | Num | Isodose Line (%) | direct |
| OPTICMAX | Num | Optic Max Dose | direct |
| BED | Num | BED | direct |
| BEDGR1 | Char | BED Group | median split |

---

### 1.12 Follow-up Variables

| Variable | Type | Label | Derivation |
|----------|------|-------|------------|
| FUPDT | Num | Last Follow-up Date | direct |
| FUP_DAYS | Num | Follow-up Days | FUPDT - INDEXDT |
| FUP_MOS | Num | Follow-up Months | FUP_DAYS / 30.4375 |
| ALIVE_FL | Char | Alive Flag | direct |
| DEATHDT | Num | Death Date | direct |

---

### 1.13 Outcome Summary Variables (Backfilled)

| Variable | Type | Label |
|----------|------|-------|
| REMISS_FL | Char | Ever Remission |
| DURREMISS_FL | Char | Durable Remission |
| RECURR_FL | Char | Recurrence |
| PROG_FL | Char | Progression |
| TUMCTRL_FL | Char | Tumor Control |
| HYPOPIT_FL | Char | New Hypopituitarism |
| SALVAGE_FL | Char | Salvage Treatment |
| DEATH_FL | Char | Death |
| FIRSTREMDT | Num | First Remission Date |
| RECURRDT | Num | Recurrence Date |
| PROGDT | Num | Progression Date |
| HYPODT | Num | Hypopituitarism Date |
| SALVDT | Num | Salvage Date |

---

### 1.14 QC Checks

**Record-level:**
- One row per USUBJID
- INDEXDT not missing
- Eligible subjects only

**Logic:**
- BASE_ENDODT ≤ INDEXDT
- BASE_IMGDT ≤ INDEXDT
- LASTSURGDT < INDEXDT
- FUPDT ≥ INDEXDT
- FUP_DAYS ≥ 0

---

## Part 2: TTRREM Derivation Specification

### 2.1 Parameter
**TTRREM** - Time to First Endocrine Remission

### 2.2 Purpose
Create subject-level and TTE derivation for first biochemical remission after index GKS

### 2.3 Output Datasets
- REMISSION_SUMM
- ADTTE_TTRREM

### 2.4 Input
- ADSL
- ADENDO

### 2.5 Population
Subjects with EFFL='Y', valid INDEXDT, ≥1 post-GKS endocrine

### 2.6 Remission Definition

**Required:**
1. IGF1I ≤ 1.0
2. ON_MED = 'N'

**Conditional:**
3. If OGTT available: OGTT_NADIR_GH < 0.4

**Window:** ±30 days for combining lab + med + OGTT

---

### 2.7 ADENDO Preprocessing

```sas
* Keep post-GKS records;
data post_endo;
 set adendo;
 where adt > indexdt;
 
 rem_igf_fl = (not missing(igf1i) and igf1i <= 1);
 rem_med_fl = (on_med = 'N');
 
 if missing(ogtt_nadir_gh) then rem_ogtt_fl = 1;
 else rem_ogtt_fl = (ogtt_nadir_gh < 0.4);
 
 rem_cand_fl = (rem_igf_fl and rem_med_fl and rem_ogtt_fl);
run;
```

---

### 2.8 First Remission Date

```sas
data remission_summ;
 set post_endo;
 by usubjid adt;
 retain firstremdt lastendodt remiss_fl;
 
 if first.usubjid then do;
  firstremdt = .;
  lastendodt = .;
  remiss_fl = 'N';
 end;
 
 lastendodt = adt;
 
 if rem_cand_fl = 1 and missing(firstremdt) then do;
  firstremdt = adt;
  remiss_fl = 'Y';
 end;
 
 if last.usubjid then output;
run;
```

---

### 2.9 Censoring Rule

| Status | ADT | CNSR |
|--------|-----|------|
| Event | FIRSTREMDT | 0 |
| Censored | LASTENDODT | 1 |

**AVAL** = ADT - INDEXDT + 1

---

### 2.10 ADTTE Structure

| Variable | Value |
|----------|-------|
| PARAMCD | TTRREM |
| PARAM | Time to First Endocrine Remission |
| STARTDT | INDEXDT |
| CNSR | 0=event, 1=censored |
| EVNTDESC | Description |

---

### 2.11 Special Cases

| Case | Handling |
|------|----------|
| IGF-1 normal, off meds, OGTT missing | Allow remission, flag OGTT_SUPPORT=N |
| ON_MED unknown | Do not auto-derive; adjudicate |
| Multiple remission records | Use earliest |
| Site says remission, data inconsistent | Objective criteria prevail |

---

### 2.12 QC Listings

**Listing A:** All remission events with dates, IGF1I, ON_MED, OGTT

**Listing B:** All censored subjects with last endocrine date

**Listing C:** Issue cases - conflicts, missing data, adjudicated

---

## Part 3: TTHYPO Derivation Specification

### 3.1 Parameter
**TTHYPO** - Time to New Hypopituitarism

### 3.2 Purpose
Derive time to first new pituitary axis deficiency after index GKS

### 3.3 Output
- HYPOPIT_SUMM
- ADTTE_TTHYPO

### 3.4 Input
- ADSL
- ADPIT
- ADAE (if needed for hormone replacement evidence)

### 3.5 Definition

**New Hypopituitarism =** First deficit in axis that was normal at baseline

**Required:**
1. BASE_DEFICIT = 'N' for that axis
2. NEW_DEFICIT = 'Y' for that axis

### 3.6 Axes
- Thyroid
- Adrenal
- Gonadal
- GH
- Posterior pituitary

---

### 3.7 Derivation Logic

```sas
* Step 1: Get baseline axis status;
proc sort data=adpit; by usubjid axis adt; run;

data baseline_axis;
 set adpit;
 where adt <= indexdt;
 by usubjid axis adt;
 if last.axis; * keep closest to GKS;
 retain base_def_&axis;
 if first.axis then base_def_&axis = base_deficit;
run;

* Step 2: Identify new deficits;
data new_deficits;
 merge adpit(in=a keep=usubjid axis adt base_deficit new_deficit)
       baseline_axis(keep=usubjid axis base_def_&axis rename=(base_def_&axis=baseline_status));
 by usubjid axis;
 if a and adt > indexdt and baseline_status='N' and new_deficit='Y';
run;

* Step 3: Get first new deficit per subject;
proc sort data=new_deficits; by usubjid adt; run;

data hypopit_summ;
 set new_deficits;
 by usubjid;
 retain firsthypodt hypopit_fl;
 if first.usubjid then do;
  firsthypodt = .;
  hypopit_fl = 'N';
 end;
 
 firsthypodt = adt;
 hypopit_fl = 'Y';
 
 if last.usubjid then output;
run;
```

---

### 3.8 Censoring

| Status | ADT | CNSR |
|--------|-----|------|
| Event | First new deficit date | 0 |
| Censored | Last pituitary assessment | 1 |

---

### 3.9 ADTTE Structure

| Variable | Value |
|----------|-------|
| PARAMCD | TTHYPO |
| PARAM | Time to New Hypopituitarism |
| STARTDT | INDEXDT |

---

### 3.10 QC Checks

- Verify baseline deficit status correctly excluded
- Check axis-specific vs subject-level consistency
- Verify date logic (post-GKS only)

---

## Part 4: TTPROG Derivation Specification

### 4.1 Parameter
**TTPROG** - Time to Radiographic Progression

### 4.2 Purpose
Derive time to first radiographic tumor progression after index GKS

### 4.3 Output
- PROGRESSION_SUMM
- ADTTE_TTPROG

### 4.4 Input
- ADSL
- ADIMG

### 4.5 Definition

**Primary:** Volume increase >20% from nadir or baseline

**Alternative:** MRI_RESPONSE = 'Progressed' or MRI_PROG = 'Y'

### 4.6 Derivation Logic

```sas
* Step 1: Get baseline and nadir volume;
proc sort data=adimg; by usubjid mri_dt; run;

data baseline_nadir;
 set adimg(where=(mri_dt <= indexdt));
 by usubjid mri_dt;
 if last.usubjid then output; * closest to GKS = baseline
run;

data nadir_vol;
 set adimg(where=(mri_dt > indexdt));
 by usubjid tumor_vol;
 if first.usubjid; * smallest volume = nadir
run;

* Step 2: Calculate progression;
data progression_candidates;
 merge adimg(in=a keep=usubjid mri_dt tumor_vol mri_response mri_prog)
       baseline_nadir(keep=usubjid tumor_vol rename=(tumor_vol=base_vol))
       nadir_vol(keep=usubjid tumor_vol rename=(tumor_vol=nadir_vol));
 by usubjid;
 if a and mri_dt > indexdt;
 
 * Method 1: Volume change >20%;
 if not missing(tumor_vol) and not missing(base_vol) then 
  volchg_pct = (tumor_vol - base_vol) / base_vol * 100;
 else if not missing(tumor_vol) and not missing(nadir_vol) then
  volchg_pct = (tumor_vol - nadir_vol) / nadir_vol * 100;
 
 prog_vol_fl = (volchg_pct > 20);
 
 * Method 2: Response/flag;
 prog_resp_fl = (mri_response = 'Progressed' or mri_prog = 'Y');
 
 * Combined;
 prog_fl = (prog_vol_fl or prog_resp_fl);
run;
```

---

### 4.7 First Progression Date

```sas
proc sort data=progression_candidates; by usubjid mri_dt; run;

data prog_summ;
 set progression_candidates;
 by usubjid;
 retain progdt tumctrl_fl;
 if first.usubjid then do;
  progdt = .;
  tumctrl_fl = 'Y'; * assume controlled until proven
 end;
 
 if prog_fl = 1 and missing(progdt) then do;
  progdt = mri_dt;
  tumctrl_fl = 'N';
 end;
 
 if last.usubjid then output;
run;
```

---

### 4.8 Censoring

| Status | ADT | CNSR |
|--------|-----|------|
| Event | First progression date | 0 |
| Censored | Last MRI date | 1 |

---

### 4.9 ADTTE Structure

| Variable | Value |
|----------|-------|
| PARAMCD | TTPROG |
| PARAM | Time to Radiographic Progression |
| STARTDT | INDEXDT |

---

### 4.10 QC Checks

- Verify volume change calculation
- Check response/flag consistency
- Review "possible progression" cases

---

## Part 5: Summary Table

| Endpoint | PARAMCD | Key Derivation | censoring |
|----------|---------|----------------|-----------|
| Remission | TTRREM | IGF1I≤1, off med, OGTT<0.4 | Last endo date |
| Recurrence | TTRREC | After remission, IGF1I>1 | Last endo date |
| Progression | TTPROG | Volume>20% or response=progressed | Last MRI |
| Hypopituitarism | TTHYPO | New deficit in baseline-normal axis | Last pit date |
| Salvage | TTSALV | First intervention post-GKS | Last follow-up |
| OS | OS | Death | Last known alive |

---

*Created: 2026-03-21*
