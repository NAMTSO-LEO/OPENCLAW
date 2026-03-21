# Complete SDTM & ADaM Variable Specification
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly
### Production-Ready Version with Controlled Terminology

---

## Part 1: SDTM Domain Specifications

### 1.1 DM — Demographics

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | Fixed study ID |
| DOMAIN | Char | Y | Domain Abbreviation | DM |
| USUBJID | Char | Y | Unique Subject Identifier | SITEID-SUBJECT_ID |
| SUBJID | Char | N | Subject Identifier | Local subject ID |
| SITEID | Char | Y | Study Site Identifier | Center code |
| AGE | Num | Y | Age | Age at GKS |
| AGEU | Char | Y | Age Units | YEARS |
| SEX | Char | Y | Sex | M/F/U |
| RACE | Char | N | Race | If collected |
| ETHNIC | Char | N | Ethnicity | If collected |
| COUNTRY | Char | N | Country | Country code |

---

### 1.2 DS — Disposition

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | DS |
| USUBJID | Char | Y | Unique Subject Identifier | |
| DSSEQ | Num | Y | Sequence Number | |
| DSCAT | Char | Y | Category | DISPOSITION EVENT |
| DSTERM | Char | Y | Reported Term | |
| DSDECOD | Char | N | Standardized Term | ENROLLED/COMPLETED/DEATH/LOST TO FOLLOW-UP |
| DSSTDTC | Char | N | Start Date | YYYY-MM-DD |

**Controlled Terms:** ENROLLED, COMPLETED, DEATH, LOST TO FOLLOW-UP

---

### 1.3 MH — Medical History

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | MH |
| USUBJID | Char | Y | Unique Subject Identifier | |
| MHSEQ | Num | Y | Sequence Number | |
| MHTERM | Char | Y | Reported Term | |
| MHDECOD | Char | N | Standardized Term | |
| MHCAT | Char | N | Category | ENDOCRINE DISORDER/METABOLIC/CARDIOVASCULAR/RESPIRATORY |
| MHSTDTC | Char | N | Start Date | |
| MHENRTPT | Char | N | End Relative to Reference | ONGOING |

**Recommended Terms:** Acromegaly, Pituitary adenoma, Hypopituitarism, Diabetes mellitus, Hypertension, Cardiovascular disease, Obstructive sleep apnea

---

### 1.4 CM — Concomitant Medications

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | CM |
| USUBJID | Char | Y | Unique Subject Identifier | |
| CMSEQ | Num | Y | Sequence Number | |
| CMTRT | Char | Y | Reported Name | |
| CMDECOD | Char | N | Standardized Name | |
| CMCAT | Char | N | Category | ACROMEGALY TREATMENT/HORMONE REPLACEMENT |
| CMSTDTC | Char | N | Start Date | |
| CMENDTC | Char | N | End Date | |
| CMDOSE | Num | N | Dose | |
| CMDOSU | Char | N | Dose Units | |
| CMROUTE | Char | N | Route | |
| CMINDC | Char | N | Indication | |

**Drug Classes:**
- Acromegaly: Octreotide, Lanreotide, Pegvisomant, Bromocriptine, Cabergoline
- Replacement: Levothyroxine, Hydrocortisone, Testosterone, Estrogen, Desmopressin

---

### 1.5 PR — Procedures

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | PR |
| USUBJID | Char | Y | Unique Subject Identifier | |
| PRSEQ | Num | Y | Sequence Number | |
| PRTRT | Char | Y | Procedure Name | |
| PRDECOD | Char | N | Standardized Term | |
| PRCAT | Char | Y | Category | SURGICAL PROCEDURE/RADIOSURGERY/RADIOTHERAPY |
| PRSCAT | Char | N | Subcategory | PRIMARY/REPEAT/SALVAGE |
| PRSTDTC | Char | Y | Start Date | |
| PRENDTC | Char | N | End Date | |
| PRLOC | Char | N | Location | Sellar region/Cavernous sinus |
| PRDOSE | Num | N | Dose (Gy) | For radiation |
| PRDOSU | Char | N | Dose Units | Gy |
| PRMETH | Char | N | Method | |

**Key Records:** Transsphenoidal surgery, Gamma Knife radiosurgery, Repeat surgery, Repeat SRS, Fractionated RT

---

### 1.6 LB — Laboratory Test Results

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | LB |
| USUBJID | Char | Y | Unique Subject Identifier | |
| LBSEQ | Num | Y | Sequence Number | |
| LBTESTCD | Char | Y | Test Code | IGF1/GH/OGTTGH/TSH/FT4 |
| LBTEST | Char | Y | Test Name | |
| LBCAT | Char | N | Category | ENDOCRINE/PITUITARY |
| LBSCAT | Char | N | Subcategory | ORAL GLUCOSE TOLERANCE TEST |
| LBORRES | Char | Y | Result as Collected | |
| LBORRESU | Char | N | Original Units | |
| LBSTRESC | Char | N | Standardized Result (Char) | |
| LBSTRESN | Num | N | Standardized Result (Num) | |
| LBSTRESU | Char | N | Standardized Units | |
| LBSTNRLO | Num | N | Reference Range Low | |
| LBSTNRHI | Num | N | Reference Range High | ULN is critical |
| LBNRIND | Char | N | Reference Range Indicator | LOW/NORMAL/HIGH |
| LBDTC | Char | Y | Collection Date | |
| VISIT | Char | N | Visit Name | |
| VISITNUM | Num | N | Visit Number | |

**Recommended LBTESTCD:** IGF1, GH, OGTTGH

**Note:** IGF1I is recommended for ADaM derivation, not SDTM.

---

### 1.7 AE — Adverse Events

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | AE |
| USUBJID | Char | Y | Unique Subject Identifier | |
| AESEQ | Num | Y | Sequence Number | |
| AETERM | Char | Y | Reported Term | |
| AEDECOD | Char | N | Standardized Term | |
| AECAT | Char | N | Category | NEUROLOGIC/ENDOCRINE/VISUAL/RADIATION |
| AESTDTC | Char | Y | Start Date | |
| AEENDTC | Char | N | End Date | |
| AESEV | Char | N | Severity | MILD/MODERATE/SEVERE |
| AESER | Char | N | Serious | Y/N |
| AEREL | Char | N | Causality | RELATED/NOT RELATED |

**Important Events:** Visual decline, Visual field defect, Optic neuropathy, Cranial neuropathy, Adverse radiation effect, Radionecrosis, Hypopituitarism

---

### 1.8 FA — Findings About

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | FA |
| USUBJID | Char | Y | Unique Subject Identifier | |
| FASEQ | Num | Y | Sequence Number | |
| FAGRPID | Char | N | Group ID | |
| FATESTCD | Char | Y | Test Code | KNOSP/CSI/PLANTYPE/MEDHOLD/NEWPITDEF |
| FATEST | Char | Y | Test Name | |
| FACAT | Char | Y | Category | DISEASE CHARACTERISTIC/TREATMENT CHARACTERISTIC |
| FAOBJ | Char | Y | Object | Pituitary adenoma/GKS plan/medication |
| FASTRESC | Char | Y | Result (Char) | |
| FASTRESN | Num | N | Result (Num) | |
| FASTRESU | Char | N | Result Units | |
| FADTC | Char | Y | Date | |

**Controlled Terms:**
- KNOSP: 0, 1, 2, 3, 4
- CSI: CONFIRMED/NOT_CONFIRMED
- PLANTYPE: TARGETED/WHOLE_SELLA/MIXED
- MEDHOLD: YES/NO/UNKNOWN

---

### 1.9 TU — Tumor Identification

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | TU |
| USUBJID | Char | Y | Unique Subject Identifier | |
| TUSEQ | Num | Y | Sequence Number | |
| TULNKID | Char | Y | Link Identifier | Links to TR/RS |
| TUTESTCD | Char | Y | Test Code | TUMIDENT |
| TUTEST | Char | Y | Test Name | |
| TUORRES | Char | N | Result | Residual adenoma/Recurrent |
| TULOC | Char | N | Location | CAVERNOUS SINUS/SELLAR |
| TUTYPE | Char | N | Type | RESIDUAL/RECURRENT |
| TUDTC | Char | N | Date | |

---

### 1.10 TR — Tumor Results

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | TR |
| USUBJID | Char | Y | Unique Subject Identifier | |
| TRSEQ | Num | Y | Sequence Number | |
| TRLNKID | Char | Y | Link to TU | |
| TRTESTCD | Char | Y | Test Code | TUMVOL/MAXDIM |
| TRTEST | Char | Y | Test Name | |
| TRORRES | Char | N | Result as Collected | |
| TRSTRESN | Num | N | Numeric Result | Core volume value |
| TRSTRESU | Char | N | Units | cc/mm |
| TRMETHOD | Char | N | Method | MRI volumetric |
| TRDTC | Char | Y | Assessment Date | |
| VISIT | Char | N | Visit Name | |

---

### 1.11 RS — Response Assessment

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | RS |
| USUBJID | Char | Y | Unique Subject Identifier | |
| RSSEQ | Num | Y | Sequence Number | |
| RSTESTCD | Char | Y | Test Code | ENDORESP/IMGRESP |
| RSTEST | Char | Y | Test Name | |
| RSORRES | Char | N | Result as Collected | |
| RSSTRESC | Char | Y | Standardized Result | |
| RSEVAL | Char | N | Evaluator | Investigator/Central |
| RSDTC | Char | Y | Assessment Date | |
| VISIT | Char | N | Visit Name | |

**Controlled Terms:**
- ENDORESP: REMISSION, CONTROL_ON_MED, UNCONTROLLED, RECURRENCE
- IMGRESP: DECREASED, STABLE, PROGRESSED, INEVALUABLE

---

### 1.12 SV — Subject Visits

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| DOMAIN | Char | Y | Domain Abbreviation | SV |
| USUBJID | Char | Y | Unique Subject Identifier | |
| SVSEQ | Num | Y | Sequence Number | |
| VISITNUM | Num | Y | Visit Number | |
| VISIT | Char | Y | Visit Name | Baseline/3m/6m/12m/annual |
| SVSTDTC | Char | N | Visit Start Date | |
| SVENDTC | Char | N | Visit End Date | |

---

## Part 2: ADaM Dataset Specifications

### 2.1 ADSL — Subject-Level Analysis Dataset

| # | Variable | Type | Core | Label | Derivation/Source |
|---|---------|------|------|-------|------------------|
| 1 | STUDYID | Char | Y | Study Identifier | DM |
| 2 | USUBJID | Char | Y | Unique Subject ID | DM |
| 3 | SITEID | Char | Y | Site ID | DM |
| 4 | AGE | Num | Y | Age | DM → derived |
| 5 | SEX | Char | Y | Sex | DM |
| 6 | INDEXDT | Num | Y | Index GKS Date | PR → derived |
| 7 | FASFL | Char | Y | Full Analysis Set Flag | DS → derived |
| 8 | EFFL | Char | Y | Endocrine Evaluable Flag | Derived |
| 9 | IMGEVLFL | Char | Y | Imaging Evaluable Flag | Derived |
| 10 | SAFFL | Char | Y | Safety Analysis Flag | Derived |
| 11 | BASE_IGF1 | Num | Y | Baseline IGF-1 | LB |
| 12 | BASE_IGF1_ULN | Num | Y | Baseline IGF-1 ULN | LB |
| 13 | BASE_IGF1I | Num | Y | Baseline IGF-1 Index | LB → derived |
| 14 | BASE_GH | Num | N | Baseline GH | LB |
| 15 | BASE_OGTTGH | Num | N | Baseline OGTT Nadir GH | LB |
| 16 | KNOSP | Num | Y | Baseline Knosp Grade | FA |
| 17 | KNOSPGR | Char | Y | Knosp Grade Group | Derived |
| 18 | CSI_DEF_TYPE | Char | Y | CSI Definition Type | FA |
| 19 | BASE_TUMVOL | Num | N | Baseline Tumor Volume | TR |
| 20 | PRIOR_SURG_N | Num | Y | Number of Prior Surgeries | PR → derived |
| 21 | LASTSURGDT | Num | N | Last Surgery Date | PR → derived |
| 22 | SURG2GKS_DAYS | Num | N | Days from Surgery to GKS | Derived |
| 23 | SURG2GKS_MOS | Num | N | Months from Surgery to GKS | Derived |
| 24 | EARLYGKS_FL | Char | N | Early GKS Flag | Derived |
| 25 | PRIOR_MEDS_FL | Char | Y | Prior Medical Therapy Flag | CM → derived |
| 26 | PLAN_TYPE | Char | Y | Plan Type | FA |
| 27 | TARGETED_FL | Char | Y | Targeted Plan Flag | Derived |
| 28 | WHOLESELLA_FL | Char | Y | Whole-Sella Plan Flag | Derived |
| 29 | MARGINDOSE | Num | N | Margin Dose (Gy) | PR |
| 30 | MAXDOSE | Num | N | Maximum Dose (Gy) | PR |
| 31 | ISODOSE | Num | N | Isodose Line (%) | PR |
| 32 | OPTICMAX | Num | N | Optic Maximum Dose (Gy) | PR |
| 33 | BED | Num | N | Biologically Effective Dose | Derived |
| 34 | MEDHOLD_CAT | Char | Y | Medication Hold Category | FA → derived |
| 35 | FUPDT | Num | Y | Last Follow-up Date | DS → derived |
| 36 | FUP_DAYS | Num | Y | Follow-up Duration (Days) | Derived |
| 37 | FUP_MOS | Num | Y | Follow-up Duration (Months) | Derived |
| 38 | REMISS_FL | Char | Y | Ever Remission Flag | Derived |
| 39 | DURREMISS_FL | Char | Y | Durable Remission Flag | Derived |
| 40 | RECURR_FL | Char | Y | Recurrence Flag | Derived |
| 41 | PROG_FL | Char | Y | Progression Flag | Derived |
| 42 | TUMCTRL_FL | Char | Y | Tumor Control Flag | Derived |
| 43 | HYPOPIT_FL | Char | Y | New Hypopituitarism Flag | Derived |
| 44 | SALVAGE_FL | Char | Y | Salvage Treatment Flag | Derived |
| 45 | DEATH_FL | Char | Y | Death Flag | DS → derived |
| 46 | FIRSTREMDT | Num | N | First Remission Date | Derived |
| 47 | RECURRDT | Num | N | Recurrence Date | Derived |
| 48 | PROGDT | Num | N | Progression Date | Derived |
| 49 | HYPODT | Num | N | Hypopituitarism Date | Derived |
| 50 | SALVDT | Num | N | Salvage Date | Derived |
| 51 | DEATHDT | Num | N | Death Date | DS → derived |

---

### 2.2 ADLB — Laboratory Analysis Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| PARAMCD | Char | Y | Parameter Code | IGF1/GH/OGTTGH/IGF1I |
| PARAM | Char | Y | Parameter Description | |
| ADT | Num | Y | Analysis Date | |
| ADY | Num | Y | Analysis Relative Day | ADT - INDEXDT + 1 |
| AVISIT | Char | N | Analysis Visit | |
| AVISITN | Num | N | Analysis Visit Number | |
| AVAL | Num | Y | Analysis Value | |
| AVALU | Char | N | Analysis Value Unit | |
| BASE | Num | N | Baseline Value | |
| CHG | Num | N | Change from Baseline | |
| PCHG | Num | N | Percent Change | |
| ANRIND | Char | N | Reference Range Indicator | |
| ONMED | Char | N | On Medication | |

---

### 2.3 ADENDO — Endocrine Analysis Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| ADT | Num | Y | Assessment Date | |
| ADY | Num | Y | Relative Day | |
| AVISIT | Char | N | Analysis Visit | |
| IGF1I | Num | Y | IGF-1 Index | Derived |
| GH | Num | N | Growth Hormone | |
| OGTTGH | Num | N | OGTT Nadir GH | |
| ON_MED | Char | Y | On Medication | Y/N |
| ENDO_STATUS | Char | Y | Endocrine Status | UNCONTROLLED/ENDO_CONTROL/BIOCHEM_REM/RECURR/INDETERMINATE |
| FIRSTREM_FL | Char | N | First Remission Flag | |
| POSTREM_FL | Char | N | Post-Remission Flag | |
| RECURR_EVENT_FL | Char | N | Recurrence Event Flag | |

---

### 2.4 ADIMG — Imaging Analysis Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| ADT | Num | Y | MRI Assessment Date | |
| ADY | Num | Y | Relative Day | |
| TUMVOL | Num | N | Tumor Volume | cc |
| VOLCHG | Num | N | Change in Volume | |
| VOLCHGPCT | Num | N | Percent Change in Volume | |
| MRIRESP | Char | Y | MRI Response | DECREASED/STABLE/PROGRESSED/UNEVALUABLE |
| PROG_EVENT_FL | Char | Y | Progression Event Flag | |
| TUMCTRL_FL | Char | Y | Tumor Control Flag | |

---

### 2.5 ADRAD — Radiosurgery Analysis Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| GKSDT | Num | Y | Gamma Knife Date | |
| PLAN_TYPE | Char | Y | Plan Type | TARGETED/WHOLE_SELLA/MIXED |
| TARGETVOL_CC | Num | N | Target Volume | |
| MARGINDOSE | Num | N | Margin Dose | Gy |
| MAXDOSE | Num | N | Maximum Dose | Gy |
| ISODOSE | Num | N | Isodose Line | % |
| OPTICMAX | Num | N | Optic Maximum Dose | Gy |
| BED | Num | N | BED | |

---

### 2.6 ADPIT — Pituitary Function Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| ADT | Num | Y | Assessment Date | |
| AXIS | Char | Y | Pituitary Axis | THYROID/ADRENAL/GONADAL/GH/POSTPIT |
| BASE_DEF_FL | Char | Y | Baseline Deficit Flag | |
| NEW_DEF_FL | Char | Y | New Deficit Flag | |
| DEF_STATUS | Char | Y | Deficit Status | |

---

### 2.7 ADINT — Intervention Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| INTDT | Num | Y | Intervention Date | |
| INTTYPE | Char | Y | Intervention Type | REPEAT_SURGERY/REPEAT_SRS/FRACTIONATED_RT/MED_ESCALATION |
| INTREAS | Char | N | Intervention Reason | |

---

### 2.8 ADAE — Adverse Event Analysis Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| AEDECOD | Char | Y | Standardized Term | |
| AESTDT | Num | Y | Start Date | |
| TRTEMFL | Char | Y | Treatment Emergent Flag | |
| AEREL | Char | N | Relationship | |
| AESEV | Char | N | Severity | |
| AECAT | Char | N | Category | |
| VISUAL_AE_FL | Char | N | Visual Toxicity Flag | |
| CN_AE_FL | Char | N | Cranial Neuropathy Flag | |
| ARE_AE_FL | Char | N | Radiation Effect Flag | |
| HYPOPIT_AE_FL | Char | N | Hypopituitarism Flag | |

---

### 2.9 ADTTE — Time-to-Event Dataset

| Variable | Type | Core | Label | Comment |
|----------|------|------|-------|---------|
| STUDYID | Char | Y | Study Identifier | |
| USUBJID | Char | Y | Unique Subject ID | |
| PARAMCD | Char | Y | Parameter Code | TTRREM/TTDREM/TTRREC/TTPROG/TTHYPO/TTSALV/OS |
| PARAM | Char | Y | Parameter | |
| STARTDT | Num | Y | Start Date | INDEXDT |
| ADT | Num | Y | Event/Censor Date | |
| CNSR | Num | Y | Censoring Indicator | 0=event, 1=censored |
| AVAL | Num | Y | Time Value (days) | |
| EVNTDESC | Char | N | Event Description | |

---

## Part 3: Minimum Deliverable Version

### SDTM Files (Minimum)
1. dm.sas7bdat
2. ds.sas7bdat
3. cm.sas7bdat
4. pr.sas7bdat
5. lb.sas7bdat
6. ae.sas7bdat
7. fa.sas7bdat
8. tr.sas7bdat
9. rs.sas7bdat

### ADaM Files (Minimum)
1. adsl.sas7bdat
2. adlb.sas7bdat
3. adendo.sas7bdat
4. adtte.sas7bdat

---

## Part 4: Critical Derivation Rules

### 4.1 Index Date
- INDEXDT = first eligible GKS date

### 4.2 Baseline Window
- Primary: within 90 days before INDEXDT
- Secondary: within 180 days before INDEXDT

### 4.3 IGF-1 Index
```
BASE_IGF1I = BASE_IGF1 / BASE_IGF1_ULN
```

### 4.4 Early GKS
```
if SURG2GKS_MOS <= 12 then EARLYGKS_FL = 'Y'
```

### 4.5 Remission
- IGF1I ≤ 1.0
- ON_MED = N
- OGTTGH < 0.4 if available

### 4.6 Progression
- Volume increase >20% from baseline/nadir
- OR MRI response = PROGRESSED

### 4.7 New Hypopituitarism
- Baseline: no deficit in that axis
- Post-GKS: new deficit in that axis

---

*Document created: 2026-03-21*
*Version: Complete Production-Ready*
