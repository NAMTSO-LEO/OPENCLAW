# CRF / Data Collection Dictionary

## Study: Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## 1. CRF Module Structure

### 10 Modules

1. **Site/Subject Identification**
2. **Eligibility/Enrollment**
3. **Baseline Clinical Presentation**
4. **Prior Treatment History**
5. **Pre-GKS Endocrine Data**
6. **Pre-GKS Imaging Data**
7. **Gamma Knife Treatment Data**
8. **Post-GKS Endocrine Follow-up**
9. **Post-GKS Imaging/Safety/Salvage**
10. **Vital Status/Last Follow-up**

---

## 2. Module 1: Site/Subject ID

### Site Information
| Field | Type | Required |
|-------|------|----------|
| SITEID | Text | Yes |
| COUNTRY | Text | Yes |
| PI_NAME | Text | No |

### Subject Information
| Field | Type | Required |
|-------|------|----------|
| SUBJECT_ID | Text | Yes |
| STUDY_SUBJID | Text | Yes |
| SEX | Male/Female/Other/Unknown | Yes |
| DOB_YR | YYYY | Preferred |
| AGE_GKS | Numeric | Yes |

---

## 3. Module 2: Eligibility

### Inclusion Criteria
| Field | Required |
|-------|----------|
| INC_ACRO_DIAG - Clinical diagnosis of acromegaly | Yes |
| INC_CSI - Cavernous sinus invasion evidence | Yes |
| INC_GKS - Eligible GKS performed | Yes |
| INC_FU12M - ≥12 months endocrine follow-up | Yes |
| INC_POSTENDO - Post-GKS endocrine eval | Yes |
| INC_POSTMRI - Post-GKS MRI eval | Yes |

### Exclusion Criteria
| Field |
|-------|
| EXC_NO_CSI |
| EXC_NON_GH |
| EXC_PRIOR_FXRT |
| EXC_PRIOR_SRS |
| EXC_INADEQ_FU |
| EXC_MISS_BASE_ENDO |
| EXC_UNCLASS_PLAN |

---

## 4. Module 3: Baseline Clinical

| Field | Type |
|-------|------|
| ACRO_DIAG_DT | Date |
| PRESENT_HEADACHE | Y/N |
| PRESENT_VISUAL | Y/N |
| PRESENT_DIPLOPIA | Y/N |
| PRESENT_ACROFEAT | Y/N |
| PRESENT_HYPOPIT | Y/N |
| COMORB_DM | Y/N |
| COMORB_HTN | Y/N |
| COMORB_CV | Y/N |
| COMORB_OSA | Y/N |

---

## 5. Module 4: Prior Treatment

### Surgery (Repeating)
| Field | Type |
|-------|------|
| SURG_SEQ | Numeric |
| SURG_DT | Date |
| SURG_APPROACH | Endoscopic/Microscopic/Transcranial/Other |
| SURG_INTENT | Primary/Repeat/Debulking/Salvage |
| SURG_RESULT | GTR/STR/PR/Unknown |
| SURG_COMPL | Y/N |

### Medical Therapy (Repeating)
| Field | Type |
|-------|------|
| MED_SEQ | Numeric |
| MED_NAME | SSA/Pegvisomant/Dopamine agonist/Other |
| MED_STARTDT | Date |
| MED_STOPDT | Date |
| MED_ONGOING | Y/N |
| MED_HOLD_PERIGKS | Y/N |
| MED_HOLD_DAYS_BEFORE | Numeric |
| MED_RESUME_DAYS_AFTER | Numeric |

---

## 6. Module 5: Pre-GKS Endocrine (Repeating)

| Field | Type |
|-------|------|
| ENDO_SEQ | Numeric |
| ENDO_DT | Date |
| ENDO_BASE_FL | Y/N |
| IGF1 | Numeric |
| IGF1_UNIT | Text |
| IGF1_ULN | Numeric |
| IGF1_LLN | Numeric |
| GH | Numeric |
| GH_UNIT | Text |
| OGTT_DONE | Y/N |
| OGTT_NADIR_GH | Numeric |
| ENDO_ONMED | Y/N |
| ENDO_INTERP | Uncontrolled/Controlled/Remission/Recurrence/Unknown |

---

## 7. Module 6: Pre-GKS Imaging (Repeating)

| Field | Type |
|-------|------|
| IMG_SEQ | Numeric |
| MRI_DT | Date |
| IMG_BASE_FL | Y/N |
| KNOSP_GRADE | 0/1/2/3/4 |
| CSI_EVIDENCE | Knosp/MRI residual/Plan-based/Other |
| TUMOR_VOL | Numeric (cc) |
| TUMOR_MAXDIM | Numeric (mm) |
| RESIDUAL_CS | Y/N |
| RESIDUAL_SELLA | Y/N |
| OPTIC_PROX | Y/N |
| IMG_INTERP | Residual/Recurrent/Stable/Progression/Unknown |

---

## 8. Module 7: GKS Treatment

| Field | Type | Required |
|-------|------|----------|
| GKS_DT | Date | Yes |
| GKS_ROLE | Adjuvant/Recurrent/Primary | Yes |
| PLAN_TYPE | Targeted/Whole-sella/Mixed/Unknown | Yes |
| TARGET_DESC | Text | No |
| TARGET_VOL_CC | Numeric | Preferred |
| MARGINDOSE | Numeric (Gy) | Yes |
| MAXDOSE | Numeric (Gy) | Yes |
| ISODOSE_LINE | Numeric (%) | Yes |
| OPTICMAX | Numeric (Gy) | Preferred |
| CN_MAX_DOSE | Numeric (Gy) | No |
| N_ISOCENTERS | Numeric | No |
| BED | Numeric | No |
| BED_METHOD | Text | No |

---

## 9. Module 8: Post-GKS Endocrine (Repeating)

| Field | Type |
|-------|------|
| POST_ENDO_SEQ | Numeric |
| POST_ENDO_DT | Date |
| IGF1 | Numeric |
| IGF1_UNIT | Text |
| IGF1_ULN | Numeric |
| GH | Numeric |
| OGTT_DONE | Y/N |
| OGTT_NADIR_GH | Numeric |
| ON_MED | Y/N |
| MED_NAMES | Text |
| ENDO_STATUS_SITE | Uncontrolled/Controlled/Remission/Recurrence/Unknown |
| NEW_HORM_TX | Y/N |

---

## 10. Module 9: Post-GKS Imaging (Repeating)

| Field | Type |
|-------|------|
| POST_IMG_SEQ | Numeric |
| POST_MRI_DT | Date |
| TUMOR_VOL | Numeric |
| VOL_METHOD | Manual/Software/Estimated/Unknown |
| VOLCHG_PCT | Numeric |
| MRI_RESPONSE | Decreased/Stable/Progressed/Unevaluable |
| MRI_PROG | Y/N |
| MRI_NOTES | Text |

---

## 11. Module 10: Pituitary Function (Repeating)

| Field | Type |
|-------|------|
| PIT_SEQ | Numeric |
| PIT_DT | Date |
| AXIS | Thyroid/Adrenal/Gonadal/GH/Posterior |
| BASE_DEFICIT | Y/N |
| NEW_DEFICIT | Y/N |
| REPLACEMENT_STARTED | Y/N |
| REPLACEMENT_TYPE | Text |
| PIT_NOTES | Text |

---

## 12. Module 11: Toxicity (Repeating)

| Field | Type |
|-------|------|
| TOX_SEQ | Numeric |
| TOX_DT | Date |
| TOX_TYPE | Visual/Field/Optic/CN/ARE/Radionecrosis/Other |
| TOX_GRADE | Numeric/Text |
| TOX_NEW | New/Worsened/Pre-existing unchanged |
| TOX_RELATED | Y/N/Unknown |
| TOX_RESOLVED | Y/N |
| TOX_NOTES | Text |

---

## 13. Module 12: Salvage Treatment (Repeating)

| Field | Type |
|-------|------|
| SALV_SEQ | Numeric |
| SALV_DT | Date |
| SALV_TYPE | Repeat surgery/Repeat SRS/Fractionated RT/Med escalation |
| SALV_REASON | Persistent/Recurrence/Progression/Combined/Other |
| SALV_NOTES | Text |

---

## 14. Module 13: Vital Status

| Field | Type |
|-------|------|
| LASTFU_DT | Date |
| LASTFU_TYPE | Endocrine/Imaging/Clinical/Telephone/Chart |
| ALIVE_FL | Y/N |
| DEATH_DT | Date |
| DEATH_CAUSE | Text |

---

## 15. Controlled Terminology

### PLAN_TYPE
- Targeted cavernous sinus
- Whole sella
- Mixed
- Unknown

### GKS_ROLE
- Adjuvant for residual disease
- Treatment for recurrent disease
- Primary treatment

### ENDO_STATUS_SITE
- Uncontrolled
- Controlled on medication
- Remission
- Recurrence
- Unknown

### MRI_RESPONSE
- Decreased
- Stable
- Progressed
- Unevaluable

### TOX_TYPE
- Visual decline
- Visual field defect
- Optic neuropathy
- Cranial neuropathy
- Adverse radiation effect
- Radionecrosis
- Other

### SALV_TYPE
- Repeat surgery
- Repeat SRS
- Fractionated radiotherapy
- Medication escalation

---

## 16. Minimum Required Fields

1. Subject ID
2. Age/Sex
3. Index GKS date
4. CSI evidence
5. Knosp grade
6. Baseline IGF-1 + ULN
7. Baseline GH (if available)
8. Baseline tumor volume
9. Prior surgery history
10. Medication status at GKS
11. Medication hold
12. Plan type
13. Margin dose
14. Follow-up duration
15. ≥1 post-GKS endocrine value
16. ≥1 post-GKS MRI
17. Remission status/date
18. Recurrence status/date
19. New hypopituitarism status/date
20. Salvage status/date
21. Vital status

---

*Created: 2026-03-21*
