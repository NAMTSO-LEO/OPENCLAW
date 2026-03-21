# Data Transfer Specification

## Study: GKS for Cavernous Sinus–Invading Acromegaly

---

## 1. Delivery Requirements

### 1.1 File Format
- Format: .xlsx or .csv
- Encoding: UTF-8
- One sheet or file per domain

### 1.2 Naming Convention
```
<SiteID>_<Domain>_<YYYYMMDD>.xlsx
```

Example:
```
JHU_DEMO_20260321.xlsx
JHU_ENDO_20260321.xlsx
JHU_IMG_20260321.xlsx
```

### 1.3 Primary Keys
All domains must include:
- SITEID
- SUBJECT_ID
- STUDY_SUBJID = SITEID + "-" + SUBJECT_ID

### 1.4 Date Format
- Preferred: YYYY-MM-DD
- Acceptable: YYYY-MM
- Minimum: YYYY

### 1.5 Missing Values
- Leave blank
- Do NOT use: NA, N/A, -, unknown, 999

---

## 2. Required Domains

| Domain | Description |
|--------|-------------|
| DEMO | Demographics |
| ELIG | Eligibility |
| SURG | Surgery history |
| MEDHX | Medical therapy history |
| ENDO | Endocrine assessments |
| IMG | Imaging/MRI |
| GKS | Gamma Knife treatment |
| TOX | Toxicity/adverse events |
| PITFUNC | Pituitary function |
| SALVFU | Salvage + follow-up |

---

## 3. DEMO Domain

**Filename:** `<SiteID>_DEMO_<date>.xlsx`

**One row per subject**

| Column | Type | Required | Format/Notes |
|--------|------|----------|--------------|
| SITEID | Text | Yes | Site code |
| SUBJECT_ID | Text | Yes | Local unique ID |
| STUDY_SUBJID | Text | Yes | SITEID-SUBJECT_ID |
| COUNTRY | Text | Yes | Free text |
| SEX | Text | Yes | Male/Female/Other/Unknown |
| AGE_GKS | Numeric | Yes | Years |
| ACRO_DIAG_DT | Text | Preferred | YYYY-MM-DD |
| LASTFU_DT | Text | Yes | YYYY-MM-DD |
| ALIVE_FL | Text | Yes | Y/N |
| DEATH_DT | Text | No | YYYY-MM-DD |

---

## 4. ELIG Domain

**One row per subject**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| INC_ACRO_DIAG | Text | Yes | Y/N |
| INC_CSI | Text | Yes | Y/N |
| INC_GKS | Text | Yes | Y/N |
| INC_FU12M | Text | Yes | Y/N |
| INC_POSTENDO | Text | Yes | Y/N |
| INC_POSTMRI | Text | Yes | Y/N |
| EXC_NO_CSI | Text | Yes | Y/N |
| EXC_NON_GH | Text | Yes | Y/N |
| EXC_PRIOR_FXRT | Text | Yes | Y/N |
| EXC_PRIOR_SRS | Text | Yes | Y/N |
| EXC_INADEQ_FU | Text | Yes | Y/N |
| EXC_MISS_BASE_ENDO | Text | Yes | Y/N |
| EXC_UNCLASS_PLAN | Text | Yes | Y/N |
| ELIGIBLE_FL | Text | Yes | Y/N |

---

## 5. SURG Domain

**One row per surgery**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| SURG_SEQ | Numeric | Yes | 1,2,3... |
| SURG_DT | Text | Yes | YYYY-MM-DD |
| SURG_APPROACH | Text | Preferred | Endoscopic/Microscopic/Transcranial/Other |
| SURG_INTENT | Text | Preferred | Primary/Repeat/Debulking/Salvage |
| SURG_RESULT | Text | No | GTR/STR/PR/Unknown |
| SURG_COMPL | Text | No | Y/N |
| SURG_NOTES | Text | No | Free text |

---

## 6. MEDHX Domain

**One row per medication**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| MED_SEQ | Numeric | Yes | 1,2,3... |
| MED_NAME | Text | Yes | SSA/Pegvisomant/Dopamine_agonist/Other |
| MED_NAME_OTHER | Text | No | If Other |
| MED_STARTDT | Text | No | YYYY-MM-DD |
| MED_STOPDT | Text | No | YYYY-MM-DD |
| MED_ONGOING_GKS | Text | Yes | Y/N |
| MED_HOLD_PERIGKS | Text | No | Y/N/Unknown |
| MED_HOLD_DAYS_BEFORE | Numeric | No | Integer |
| MED_RESUME_DAYS_AFTER | Numeric | No | Integer |

---

## 7. ENDO Domain

**One row per assessment (pre and post together)**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| ENDO_SEQ | Numeric | Yes | 1,2,3... |
| ENDO_DT | Text | Yes | YYYY-MM-DD |
| ENDO_REL | Text | Yes | PRE/POST |
| ENDO_BASE_FL | Text | Yes | Y/N (only one PRE=Y) |
| IGF1 | Numeric | Preferred | Decimal |
| IGF1_UNIT | Text | Preferred | Free text |
| IGF1_ULN | Numeric | Preferred | Decimal |
| IGF1_LLN | Numeric | No | Decimal |
| GH | Numeric | No | Decimal |
| GH_UNIT | Text | No | Free text |
| OGTT_DONE | Text | Yes | Y/N |
| OGTT_NADIR_GH | Numeric | No | If OGTT_DONE=Y |
| ON_MED | Text | Yes | Y/N/Unknown |
| ACTIVE_MEDS | Text | No | Free text |
| ENDO_STATUS_SITE | Text | No | Uncontrolled/Controlled/Remission/Recurrence/Unknown |
| NEW_HORM_TX | Text | No | Y/N |

---

## 8. IMG Domain

**One row per MRI (pre and post together)**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| IMG_SEQ | Numeric | Yes | 1,2,3... |
| MRI_DT | Text | Yes | YYYY-MM-DD |
| IMG_REL | Text | Yes | PRE/POST |
| IMG_BASE_FL | Text | Yes | Y/N (only one PRE=Y) |
| KNOSP_GRADE | Text | Preferred | 0/1/2/3/4 |
| CSI_EVIDENCE | Text | Yes | Knosp/MRI_residual/Planning/Other |
| TUMOR_VOL | Numeric | No | Decimal (cc) |
| TUMOR_MAXDIM | Numeric | No | Decimal (mm) |
| RESIDUAL_CS | Text | Preferred | Y/N |
| RESIDUAL_SELLA | Text | No | Y/N |
| OPTIC_PROX | Text | No | Y/N/Unknown |
| VOL_METHOD | Text | No | Manual/Software/Estimated/Unknown |
| VOLCHG_PCT | Numeric | No | Decimal |
| MRI_RESPONSE | Text | No | Decreased/Stable/Progressed/Unevaluable |
| MRI_PROG | Text | No | Y/N |
| IMG_INTERP | Text | No | Free text |

---

## 9. GKS Domain

**One row per index GKS**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| GKS_DT | Text | Yes | YYYY-MM-DD |
| GKS_ROLE | Text | Yes | Adjuvant/Recurrent/Primary |
| PLAN_TYPE | Text | Yes | Targeted_CS/Whole_sella/Mixed/Unknown |
| TARGET_DESC | Text | No | Free text |
| TARGET_VOL_CC | Numeric | No | Decimal |
| MARGINDOSE | Numeric | Preferred | Decimal (Gy) |
| MAXDOSE | Numeric | Preferred | Decimal (Gy) |
| ISODOSE_LINE | Numeric | No | Decimal (%) |
| OPTIC_MAX_DOSE | Numeric | No | Decimal (Gy) |
| CN_MAX_DOSE | Numeric | No | Decimal (Gy) |
| N_ISOCENTERS | Numeric | No | Integer |
| BED | Numeric | No | Decimal |
| BED_METHOD | Text | No | Free text |

---

## 10. TOX Domain

**One row per toxicity event**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| TOX_SEQ | Numeric | Yes | 1,2,3... |
| TOX_DT | Text | Yes | YYYY-MM-DD |
| TOX_TYPE | Text | Yes | Visual/Field/Optic/CN/ARE/Radionecrosis/Other |
| TOX_TYPE_OTHER | Text | No | If Other |
| TOX_GRADE | Text | No | Free text |
| TOX_NEW | Text | Yes | New/Worsened/Preexisting_unchanged |
| TOX_RELATED | Text | Yes | Y/N/Unknown |
| TOX_RESOLVED | Text | No | Y/N/Unknown |
| TOX_NOTES | Text | No | Free text |

---

## 11. PITFUNC Domain

**One row per axis per assessment**

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| PIT_SEQ | Numeric | Yes | 1,2,3... |
| PIT_DT | Text | Yes | YYYY-MM-DD |
| AXIS | Text | Yes | Thyroid/Adrenal/Gonadal/GH/Posterior |
| BASE_DEFICIT | Text | Yes | Y/N |
| NEW_DEFICIT | Text | Yes | Y/N |
| REPLACEMENT_STARTED | Text | No | Y/N |
| REPLACEMENT_TYPE | Text | No | Free text |
| PIT_NOTES | Text | No | Free text |

---

## 12. SALVFU Domain

### 12A. Salvage Records

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| SALV_SEQ | Numeric | Yes | 1,2,3... |
| SALV_DT | Text | Yes | YYYY-MM-DD |
| SALV_TYPE | Text | Yes | Repeat_surgery/Repeat_SRS/Fractionated_RT/Med_escalation |
| SALV_REASON | Text | Yes | Persistent/Recurrence/Progression/Combined/Other |
| SALV_REASON_OTHER | Text | No | If Other |
| SALV_NOTES | Text | No | Free text |

### 12B. Subject Summary

| Column | Type | Required | Format |
|--------|------|----------|--------|
| SITEID | Text | Yes | |
| SUBJECT_ID | Text | Yes | |
| STUDY_SUBJID | Text | Yes | |
| LASTFU_DT | Text | Yes | YYYY-MM-DD |
| LASTFU_TYPE | Text | No | Endo/Imaging/Clinical/Telephone/Chart |
| ALIVE_FL | Text | Yes | Y/N |
| DEATH_DT | Text | No | YYYY-MM-DD |
| DEATH_CAUSE | Text | No | Free text |

---

## 13. Critical Mapping Requirements

### 13.1 Cross-Table Consistency
These fields must match exactly across all domains:
- SITEID
- SUBJECT_ID
- STUDY_SUBJID

### 13.2 Baseline Flag Uniqueness
- ENDO: Only one ENDO_BASE_FL = Y (PRE)
- IMG: Only one IMG_BASE_FL = Y (PRE)

### 13.3 GKS Index Treatment
- Submit only first eligible GKS
- Repeat SRS → SALVFU as salvage event

---

## 14. Center Self-Check Before Delivery

### Patient Count
- [ ] DEMO count = ELIG count
- [ ] All ELIGIBLE_FL=Y appear in GKS
- [ ] All eligible patients have ≥1 post-ENDO and ≥1 post-IMG

### Date Logic
- [ ] SURG_DT < GKS_DT
- [ ] ENDO_BASE_FL=Y date ≤ GKS_DT
- [ ] IMG_BASE_FL=Y date ≤ GKS_DT
- [ ] All POST dates > GKS_DT
- [ ] SALV_DT > GKS_DT
- [ ] LASTFU_DT ≥ all post-assessment dates

### Variable Logic
- [ ] OGTT_DONE=Y → OGTT_NADIR_GH not empty
- [ ] MRI_PROG=Y → MRI_RESPONSE=Progressed
- [ ] NEW_DEFICIT=Y → BASE_DEFICIT=N (same axis)
- [ ] ALIVE_FL=N → DEATH_DT required

---

## 15. Central QC Listings (Post-Import)

### Listing 1: Subject Roster
- SITEID, STUDY_SUBJID, ELIGIBLE_FL, GKS_DT, LASTFU_DT

### Listing 2: Baseline Endocrine
- Baseline date, IGF1, ULN, GH, OGTT, ON_MED

### Listing 3: Baseline Imaging
- Baseline MRI date, Knosp, CSI evidence, tumor volume

### Listing 4: Outcome Chronology
- GKS → first remission → recurrence → progression → hypopituitarism → salvage → death

---

## 16. Recommended Delivery Package

1. **Domain files:**
   - DEMO, ELIG, SURG, MEDHX, ENDO, IMG, GKS, TOX, PITFUNC, SALVFU

2. **Data dictionary:** If local variable names differ, provide mapping table

3. **Readme:**
   - Units used
   - Missing value rules
   - Date imputation notes
   - Local summarization if any

---

## 17. Controlled Terminology Summary

| Variable | Values |
|----------|---------|
| SEX | Male/Female/Other/Unknown |
| ENDO_REL | PRE/POST |
| ON_MED | Y/N/Unknown |
| OGTT_DONE | Y/N |
| MRI_PROG | Y/N |
| ALIVE_FL | Y/N |
| ELIGIBLE_FL | Y/N |
| MED_NAME | SSA/Pegvisomant/Dopamine_agonist/Other |
| PLAN_TYPE | Targeted_CS/Whole_sella/Mixed/Unknown |
| TOX_TYPE | Visual/Field/Optic/CN/ARE/Radionecrosis/Other |
| AXIS | Thyroid/Adrenal/Gonadal/GH/Posterior |
| SALV_TYPE | Repeat_surgery/Repeat_SRS/Fractionated_RT/Med_escalation |

---

*Created: 2026-03-21*
