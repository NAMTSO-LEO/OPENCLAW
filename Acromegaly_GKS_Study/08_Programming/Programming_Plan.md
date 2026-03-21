# Programming Plan

## Study: GKS for Cavernous Sinus–Invading Acromegaly

---

## 1. Overall Flow

### 6 Layers

| Layer | Output | Purpose |
|-------|--------|---------|
| 1. Raw Data Intake | RAW_* | Receive and preserve original data |
| 2. Standardization | STG_* | Harmonize formats |
| 3. Subject Master | ADSL | One row per subject |
| 4. Longitudinal | ADENDO/ADIMG/ADRAD/ADAE/ADINT | Event-level datasets |
| 5. Endpoints | ADTTE | Time-to-event datasets |
| 6. TLF | Tables/Figures | Analysis outputs |

---

## 2. Directory Structure

```
/programs
├── 00_setup/
│   ├── setup.sas
│   └── libnames.sas
├── 01_raw_import/
│   ├── import_demo.sas
│   ├── import_elig.sas
│   ├── import_surg.sas
│   ├── import_medhx.sas
│   ├── import_endo.sas
│   ├── import_img.sas
│   ├── import_gks.sas
│   ├── import_tox.sas
│   ├── import_pitfunc.sas
│   └── import_salvfu.sas
├── 02_staging/
│   ├── stg_demo.sas
│   ├── stg_elig.sas
│   ├── stg_surg.sas
│   ├── stg_medhx.sas
│   ├── stg_endo.sas
│   ├── stg_img.sas
│   ├── stg_gks.sas
│   ├── stg_tox.sas
│   ├── stg_pitfunc.sas
│   └── stg_salvfu.sas
├── 03_qc_staging/
│   ├── qc_subject_recon.sas
│   ├── qc_date_logic.sas
│   └── qc_baseline_uniqueness.sas
├── 04_adsl/
│   ├── build_adsl.sas
│   └── qc_adsl.sas
├── 05_adendo/
│   ├── build_adendo.sas
│   └── qc_adendo.sas
├── 06_adimg/
│   ├── build_adimg.sas
│   └── qc_adimg.sas
├── 07_adrad/
│   ├── build_adrad.sas
│   └── qc_adrad.sas
├── 08_adpit/
│   ├── build_adpit.sas
│   └── qc_adpit.sas
├── 09_adae/
│   ├── build_adae.sas
│   └── qc_adae.sas
├── 10_adint/
│   ├── build_adint.sas
│   └── qc_adint.sas
├── 11_derive_endpoints/
│   ├── 11a_derive_remission.sas
│   ├── 11b_derive_recurrence.sas
│   ├── 11c_derive_progression.sas
│   ├── 11d_derive_hypopit.sas
│   ├── 11e_derive_salvage.sas
│   ├── 11f_derive_os.sas
│   └── stack_adtte.sas
├── 12_adtte/
│   └── qc_adtte.sas
├── 13_analysis/
│   ├── desc/
│   │   ├── t1_baseline.sas
│   │   ├── t2_outcome_summary.sas
│   │   └── t3_missingness.sas
│   ├── survival/
│   │   ├── f_km_remission.sas
│   │   ├── f_km_progression.sas
│   │   ├── f_km_hypopit.sas
│   │   └── f_km_salvage.sas
│   ├── regression/
│   │   ├── t_cox_remission.sas
│   │   ├── t_cox_hypopit.sas
│   │   ├── t_cox_progression.sas
│   │   └── t_logistic_fixedhorizon.sas
│   ├── weighted/
│   │   ├── t_weighted_hold.sas
│   │   ├── t_weighted_plan.sas
│   │   └── t_weighted_early.sas
│   └── prediction/
│       ├── t_model_performance.sas
│       ├── f_calibration.sas
│       └── f_shap_importance.sas
├── 14_tlf/
│   ├── combine_outputs.sas
│   └── export_rtf.sas
└── 15_qc_reports/
    ├── generate_qc_reports.sas
    └── qc_summary.sas
```

---

## 3. Raw Layer

### Input Files
- RAW_DEMO
- RAW_ELIG
- RAW_SURG
- RAW_MEDHX
- RAW_ENDO
- RAW_IMG
- RAW_GKS
- RAW_TOX
- RAW_PITFUNC
- RAW_SALVFU

### Actions
- Import files
- Preserve original variable names
- Log import date
- Flag duplicate records

### Output
- Raw datasets
- raw_inventory_listing
- raw_missing_summary

---

## 4. Standardization Layer (STG_*)

### Common Standardizations

#### A. Primary Keys
- STUDYID
- SITEID
- SUBJECT_ID
- STUDY_SUBJID

#### B. Date Standardization
- Keep raw character version
- Create numeric SAS date variable

#### C. Controlled Terminology
- sex
- plan_type
- endo_status
- mri_response
- tox_type
- salvage_type

#### D. Unit Conversion
- IGF1, ULN, GH
- Tumor volume (cc)
- Dose (Gy)

---

## 5. QC Before Derivation

### 5.1 Subject Reconciliation
- DEMO, ELIG, GKS subjects match
- Eligible subjects have GKS
- Eligible subjects have post-ENDO and post-IMG

### 5.2 Chronology Checks
- surgery < GKS
- baseline assessments <= GKS
- post assessments > GKS
- salvage > GKS

### 5.3 Uniqueness Checks
- Baseline endocrine unique
- Baseline imaging unique
- GKS main record unique

---

## 6. ADSL Build

### Source Mapping

| Variable Group | Source |
|----------------|--------|
| Subject ID/demographics | STG_DEMO |
| Eligibility flags | STG_ELIG |
| Prior surgery summary | STG_SURG |
| Baseline endocrine | STG_ENDO |
| Baseline imaging | STG_IMG |
| GKS treatment | STG_GKS |
| Medication history | STG_MEDHX |
| Follow-up summary | STG_FU |

### Derivation Order

**Step 1:** Build subject frame from DEMO + ELIG + GKS

**Step 2:** Surgery summary
- PRIOR_SURG_N
- LASTSURGDT
- SURG2GKS_DAYS
- SURG2GKS_MOS
- EARLYGKS_FL

**Step 3:** Medication summary
- PRIOR_MEDS_FL
- MEDSTAT_GKS
- MEDHOLD_FL
- MEDHOLD_CAT

**Step 4:** Baseline endocrine
- BASE_IGF1, BASE_IGF1_ULN, BASE_IGF1I
- BASE_GH, BASE_OGTTGH
- BASE90_FL, BASE180_FL

**Step 5:** Baseline imaging
- KNOSP, KNOSPGR
- CSI_DEF_TYPE
- BASE_TUMVOL, BASE_LOC

**Step 6:** GKS details
- PLAN_TYPE, TARGETED_FL, WHOLESELLA_FL
- MARGINDOSE, MAXDOSE, ISODOSE
- OPTICMAX, BED

**Step 7:** Follow-up summary
- FUPDT, FUP_DAYS, FUP_MOS

---

## 7. Longitudinal Datasets

### 7.1 ADENDO
- Source: STG_ENDO + ADSL
- Derive: DAYSFROMGKS, MOSFROMGKS
- Derive: IGF1I, ENDO_STATUS_DER
- Flags: FIRSTREM_FL, POSTREM_FL, RECURR_EVENT_FL

### 7.2 ADIMG
- Source: STG_IMG + ADSL
- Derive: DAYSFROMGKS, MOSFROMGKS
- Derive: MRIRESP_DER, PROG_EVENT_FL, TUMCTRL_FL

### 7.3 ADRAD
- Source: STG_GKS
- Usually one row per patient

### 7.4 ADPIT
- Source: STG_PITFUNC + ADSL
- Derive: DAYSFROMGKS
- Derive: NEWDEF_SUBJ_FL

### 7.5 ADAE
- Source: STG_TOX + ADSL
- Derive: TRTEMFL, toxicity flags

### 7.6 ADINT
- Source: STG_SALV + ADSL
- Derive: INTTYPE, INTDT, INTDY

---

## 8. Endpoint Derivation

### 8.1 Remission (11a)
- Input: ADSL, ADENDO
- Logic: Find first post-GKS IGF1I <=1, off med, OGTT<0.4 if available
- Output: FIRSTREMDT, REMISS_FL, DURREMISS_FL

### 8.2 Recurrence (11b)
- Input: remission summary, ADENDO, ADINT
- Logic: After remission, IGF1I>1 OR restart meds for relapse
- Output: RECURR_FL, RECURRDT

### 8.3 Progression (11c)
- Input: ADIMG
- Logic: MRI_PROG=Y OR response=Progressed OR volume>20%
- Output: PROG_FL, PROGDT, TUMCTRL_FL

### 8.4 Hypopituitarism (11d)
- Input: ADPIT
- Logic: New deficit in axis normal at baseline
- Output: HYPOPIT_FL, HYPODT

### 8.5 Salvage (11e)
- Input: ADINT
- Logic: First intervention after index GKS
- Output: SALVAGE_FL, SALVDT

### 8.6 OS (11f)
- Input: DEMO/FU summary
- Output: DEATH_FL, DEATHDT

---

## 9. ADTTE Stack

### Fields
- STUDYID, USUBJID
- PARAMCD, PARAM
- STARTDT, ADT
- CNSR, AVAL
- EVNTDESC
- SRCDOM, SRCVAR

### Process
1. Create one dataset per endpoint
2. Standardize columns
3. Concatenate
4. Sort by subject + paramcd

---

## 10. Table/Figure Production

### 10.1 Descriptive
- t1_baseline.sas
- t2_outcome_summary.sas
- t3_missingness.sas

### 10.2 Survival
- f_km_remission.sas
- f_km_progression.sas
- f_km_hypopit.sas
- f_km_salvage.sas

### 10.3 Regression
- t_cox_remission.sas
- t_cox_hypopit.sas
- t_cox_progression.sas
- t_logistic_fixedhorizon.sas

### 10.4 Weighted Analyses
- t_weighted_hold.sas
- t_weighted_plan.sas
- t_weighted_early.sas

### 10.5 Prediction
- t_model_performance.sas
- f_calibration.sas
- f_shap_importance.sas

---

## 11. QC Strategy by Layer

| Layer | QC Focus |
|-------|----------|
| Raw→Staging | Record counts, missing, date conversion failures |
| Staging→ADSL | Subject count, one row per subject, merge match rates |
| Longitudinal | Relative day calculations, duplicate records |
| Endpoints | Patient-level endpoint listings |

---

## 12. Lock Points

| Lock | Milestone |
|------|-----------|
| Lock 1 | Raw imported and reconciled |
| Lock 2 | Staging standardized, QC passed |
| Lock 3 | ADSL signed off |
| Lock 4 | Endpoint derivations signed off |
| Lock 5 | TLFs finalized |

---

## 13. Common Errors to Check

1. Wrong baseline endocrine record selected
2. Wrong baseline MRI selected
3. Pre/post GKS direction wrong
4. "On medication normal" misclassified as remission
5. Recurrence not limited to post-remission patients
6. Hypopit not excluding baseline deficient axes
7. Routine medication adjustment counted as salvage
8. Wrong last follow-up censoring date

---

## 14. Execution Waves

### Wave 1
- Raw import → Staging → Staging QC → ADSL

### Wave 2
- ADENDO, ADIMG, ADINT, ADPIT

### Wave 3
- Remission/progression/hypopit/salvage/OS derivation → ADTTE

### Wave 4
- Table 1, outcome summary, KM plots

### Wave 5
- Multivariable models, weighted analyses, prediction models

---

## 15. Key Message

> Programming is NOT one big program. Break into modules: baseline selection → endpoint definition → TTE construction → QC at each layer.

---

*Created: 2026-03-21*
