# SDTM & ADaM Variable Specification (Excel Style)
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Part 1: SDTM Variable Specification

### 1.1 DM — Demographics

| # | Variable | Type | Core | Label | Comment/Derivation |
|---|---------|------|------|-------|---------------------|
| 1 | STUDYID | Char | Y | Study Identifier | Fixed study ID |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | DM |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | SITEID-SUBJECT_ID |
| 4 | SUBJID | Char | N | Subject Identifier | Local subject ID |
| 5 | SITEID | Char | Y | Study Site Identifier | Center code |
| 6 | AGE | Num | Y | Age | Age at GKS |
| 7 | AGEU | Char | Y | Age Units | YEARS |
| 8 | SEX | Char | Y | Sex | M/F/U |
| 9 | RACE | Char | N | Race | If collected |
| 10 | ETHNIC | Char | N | Ethnicity | If collected |
| 11 | COUNTRY | Char | N | Country | Country code |

---

### 1.2 DS — Disposition

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | DS |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | DSSEQ | Num | Y | Sequence Number | |
| 5 | DSCAT | Char | Y | Category | DISPOSITION EVENT |
| 6 | DSTERM | Char | Y | Reported Term | |
| 7 | DSDECOD | Char | N | Standardized Term | ENROLLED/COMPLETED/DEATH/LOST |
| 8 | DSSTDTC | Char | N | Start Date | YYYY-MM-DD |

**Controlled Terms:** ENROLLED, COMPLETED, DEATH, LOST TO FOLLOW-UP

---

### 1.3 MH — Medical History

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | MH |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | MHSEQ | Num | Y | Sequence Number | |
| 5 | MHTERM | Char | Y | Reported Term | |
| 6 | MHDECOD | Char | N | Standardized Term | |
| 7 | MHCAT | Char | N | Category | ENDOCRINE DISORDER/METABOLIC/CV |
| 8 | MHSTDTC | Char | N | Start Date | |
| 9 | MHENRTPT | Char | N | End Relative to Reference | ONGOING |

**Recommended Terms:** Acromegaly, Pituitary adenoma, Hypopituitarism, Diabetes mellitus, Hypertension, Cardiovascular disease, Obstructive sleep apnea

---

### 1.4 CM — Concomitant Medications

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | CM |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | CMSEQ | Num | Y | Sequence Number | |
| 5 | CMTRT | Char | Y | Reported Name | |
| 6 | CMDECOD | Char | N | Standardized Name | |
| 7 | CMCAT | Char | N | Category | ACROMEGALY TREATMENT/HORMONE REPLACEMENT |
| 8 | CMSTDTC | Char | N | Start Date | |
| 9 | CMENDTC | Char | N | End Date | |
| 10 | CMDOSE | Num | N | Dose | |
| 11 | CMDOSU | Char | N | Dose Units | |
| 12 | CMROUTE | Char | N | Route | |
| 13 | CMINDC | Char | N | Indication | |

**Drug Classes:**
- Acromegaly: Octreotide, Lanreotide, Pegvisomant, Bromocriptine, Cabergoline
- Replacement: Levothyroxine, Hydrocortisone, Testosterone, Estrogen, Desmopressin

---

### 1.5 PR — Procedures

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | PR |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | PRSEQ | Num | Y | Sequence Number | |
| 5 | PRTRT | Char | Y | Procedure Name | |
| 6 | PRDECOD | Char | N | Standardized Term | |
| 7 | PRCAT | Char | Y | Category | SURGICAL PROCEDURE/RADIOSURGERY |
| 8 | PRSCAT | Char | N | Subcategory | PRIMARY/REPEAT/SALVAGE |
| 9 | PRSTDTC | Char | Y | Start Date | |
| 10 | PRENDTC | Char | N | End Date | |
| 11 | PRLOC | Char | N | Location | Sellar region/Cavernous sinus |
| 12 | PRDOSE | Num | N | Dose (Gy) | For radiation |
| 13 | PRDOSU | Char | N | Dose Units | Gy |
| 14 | PRMETH | Char | N | Method | |

---

### 1.6 LB — Laboratory Test Results

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | LB |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | LBSEQ | Num | Y | Sequence Number | |
| 5 | LBTESTCD | Char | Y | Test Code | IGF1/GH/OGTTGH/TSH/FT4 |
| 6 | LBTEST | Char | Y | Test Name | |
| 7 | LBCAT | Char | N | Category | ENDOCRINE/PITUITARY |
| 8 | LBSCAT | Char | N | Subcategory | ORAL GLUCOSE TOLERANCE TEST |
| 9 | LBORRES | Char | N | Original Result | |
| 10 | LBORRESU | Char | N | Original Units | |
| 11 | LBSTRESN | Num | N | Numeric Result | |
| 12 | LBSTRESC | Char | N | Character Result | |
| 13 | LBSTRESU | Char | N | Standard Units | |
| 14 | LBNRIND | Char | N | Reference Range Indicator | LOW/NORMAL/HIGH |
| 15 | LBSTNRLO | Num | N | Reference Range Low | |
| 16 | LBSTNRHI | Num | N | Reference Range High | |
| 17 | LBDTC | Char | Y | Collection Date | |
| 18 | LBDY | Num | N | Day Relative to Reference | |
| 19 | VISITNUM | Num | N | Visit Number | |
| 20 | VISIT | Char | N | Visit Name | |
| 21 | LBBLFL | Char | N | Baseline Flag | Y/N |

---

### 1.7 FA — Findings About

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | FA |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | FASEQ | Num | Y | Sequence Number | |
| 5 | FATESTCD | Char | Y | Test Code | KNOSP/PLANTYPE/MEDHOLD/CSI |
| 6 | FATEST | Char | Y | Test Name | |
| 7 | FAORRES | Char | N | Original Result | |
| 8 | FASTRESC | Char | N | Standardized Result | |
| 9 | FAOBJ | Char | N | Object | |
| 10 | FANRIND | Char | N | Reference Range Indicator | |
| 11 | FADTC | Char | Y | Date | |
| 12 | FADY | Num | N | Day | |
| 13 | FAEVAL | Char | N | Evaluator | |

**Test Codes:**
- KNOSP: 0/1/2/3/4
- PLANTYPE: TARGETED/WHOLE_SELLA/MIXED
- MEDHOLD: YES/NO
- CSI: CONFIRMED/NOT_CONFIRMED

---

### 1.8 AE — Adverse Events

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | AE |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | AESEQ | Num | Y | Sequence Number | |
| 5 | AETERM | Char | Y | Adverse Event Term | |
| 6 | AEDECOD | Char | N | Standardized Term | |
| 7 | AEBODSYS | Char | N | Body System | |
| 8 | AESEV | Char | N | Severity | MILD/MODERATE/SEVERE |
| 9 | AESER | Char | N | Serious | Y/N |
| 10 | AEREL | Char | N | Relationship | RELATED/NOT RELATED |
| 11 | AESTDTC | Char | Y | Start Date | |
| 12 | AEENDTC | Char | N | End Date | |
| 13 | AEOUT | Char | N | Outcome | |

**Categories:** VISUAL, CRANIAL NERVE, RADIATION, ENDOCRINE

---

### 1.9 TU — Tumor Identification

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | TU |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | TULNKID | Char | Y | Link Identifier | |
| 5 | TUSEQ | Num | Y | Sequence Number | |
| 6 | TUTESTCD | Char | Y | Test Code | TUMIDENT |
| 7 | TUTEST | Char | Y | Test Name | |
| 8 | TUORRES | Char | N | Original Result | |
| 9 | TULOC | Char | N | Location | CAVERNOUS SINUS/SELLAR |
| 10 | TUTYPE | Char | N | Type | TARGET LESION |
| 11 | TUDTC | Char | N | Date | |

---

### 1.10 TR — Tumor Results

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | TR |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | TRLNKID | Char | Y | Link to TU | |
| 5 | TRSEQ | Num | Y | Sequence Number | |
| 6 | TRTESTCD | Char | Y | Test Code | TUMVOL/MAXDIM |
| 7 | TRTEST | Char | Y | Test Name | |
| 8 | TRORRES | Char | N | Original Result | |
| 9 | TRSTRESN | Num | N | Numeric Result | |
| 10 | TRSTRESC | Char | N | Character Result | |
| 11 | TRSTRESU | Char | N | Units | cc/mm |
| 12 | TRMETHOD | Char | N | Method | MRI |
| 13 | TRDTC | Char | Y | Date | |

---

### 1.11 RS — Response Assessment

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | RS |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | RSLNKID | Char | N | Link Identifier | |
| 5 | RSSEQ | Num | Y | Sequence Number | |
| 6 | RSTESTCD | Char | Y | Test Code | ENDORESP/IMGRESP |
| 7 | RSTEST | Char | Y | Test Name | |
| 8 | RSORRES | Char | N | Original Result | |
| 9 | RSSTRESC | Char | N | Standardized Result | |
| 10 | RSDTC | Char | Y | Date | |
| 11 | RSEVAL | Char | N | Evaluator | |
| 12 | VISITNUM | Num | N | Visit Number | |

**Response Values:**
- ENDORESP: REMISSION, CONTROL_ON_MED, UNCONTROLLED, RECURRENCE
- IMGRESP: DECREASED, STABLE, PROGRESSED, INEVALUABLE

---

### 1.12 SV — Subject Visits

| # | Variable | Type | Core | Label | Comment |
|---|---------|------|------|-------|---------|
| 1 | STUDYID | Char | Y | Study Identifier | |
| 2 | DOMAIN | Char | Y | Domain Abbreviation | SV |
| 3 | USUBJID | Char | Y | Unique Subject Identifier | |
| 4 | VISITNUM | Num | Y | Visit Number | |
| 5 | VISIT | Char | Y | Visit Name | |
| 6 | SVSTDTC | Char | N | Visit Start Date | |
| 7 | SVENDTC | Char | N | Visit End Date | |
| 8 | SVSTDY | Num | N | Start Day | |
| 9 | SVENDY | Num | N | End Day | |

---

## Part 2: ADaM Variable Specification

### 2.1 ADSL — Subject-Level Analysis Dataset

| # | Variable | Type | Label | Derivation/Source |
|---|---------|------|-------|-------------------|
| 1 | STUDYID | Char | Study Identifier | DM |
| 2 | USUBJID | Char | Unique Subject ID | DM |
| 3 | SITEID | Char | Site Identifier | DM |
| 4 | AGE | Num | Age | DM → derived |
| 5 | SEX | Char | Sex | DM |
| 6 | INDEXDT | Num | Index GKS Date | PR → derived |
| 7 | FASFL | Char | Full Analysis Set Flag | DS → derived |
| 8 | EFFL | Char | Endocrine Evaluable Flag | Derived |
| 9 | IMGEVLFL | Char | Imaging Evaluable Flag | Derived |
| 10 | SAFFL | Char | Safety Analysis Flag | Derived |
| 11 | KNOSP | Num | Knosp Grade | FA → derived |
| 12 | KNOSPGR | Char | Knosp Group | Derived |
| 13 | CSI_DEF_TYPE | Char | CSI Definition Type | FA |
| 14 | BASE_TUMVOL | Num | Baseline Tumor Volume | TR |
| 15 | PRIOR_SURG_N | Num | Number of Prior Surgeries | PR → derived |
| 16 | LASTSURGDT | Num | Last Surgery Date | PR → derived |
| 17 | SURG2GKS_DAYS | Num | Days from Surgery to GKS | Derived |
| 18 | SURG2GKS_MOS | Num | Months from Surgery to GKS | Derived |
| 19 | EARLYGKS_FL | Char | Early GKS Flag | Derived |
| 20 | PRIOR_MEDS_FL | Char | Prior Medical Therapy Flag | CM → derived |
| 21 | BASE_IGF1 | Num | Baseline IGF-1 | LB |
| 22 | BASE_IGF1_ULN | Num | Baseline IGF-1 ULN | LB |
| 23 | BASE_IGF1I | Num | Baseline IGF-1 Index | LB → derived |
| 24 | BASE_GH | Num | Baseline GH | LB |
| 25 | BASE_OGTTGH | Num | Baseline OGTT Nadir GH | LB |
| 26 | PLAN_TYPE | Char | Plan Type | FA |
| 27 | TARGETED_FL | Char | Targeted Plan Flag | Derived |
| 28 | WHOLESELLA_FL | Char | Whole-Sella Flag | Derived |
| 29 | MARGINDOSE | Num | Margin Dose (Gy) | PR |
| 30 | MAXDOSE | Num | Maximum Dose (Gy) | PR |
| 31 | ISODOSE | Num | Isodose Line (%) | PR |
| 32 | OPTICMAX | Num | Optic Max Dose (Gy) | PR |
| 33 | BED | Num | BED | Derived |
| 34 | MEDHOLD_CAT | Char | Medication Hold Category | FA → derived |
| 35 | FUPDT | Num | Last Follow-up Date | DS |
| 36 | FUP_DAYS | Num | Follow-up Days | Derived |
| 37 | FUP_MOS | Num | Follow-up Months | Derived |
| 38 | REMISS_FL | Char | Ever Remission Flag | Derived |
| 39 | DURREMISS_FL | Char | Durable Remission Flag | Derived |
| 40 | RECURR_FL | Char | Recurrence Flag | Derived |
| 41 | PROG_FL | Char | Progression Flag | Derived |
| 42 | HYPOPIT_FL | Char | New Hypopituitarism Flag | Derived |
| 43 | SALVAGE_FL | Char | Salvage Flag | Derived |
| 44 | DEATH_FL | Char | Death Flag | Derived |
| 45 | FIRSTREMDT | Num | First Remission Date | Derived |
| 46 | RECURRDT | Num | Recurrence Date | Derived |
| 47 | PROGDT | Num | Progression Date | Derived |
| 48 | HYPODT | Num | Hypopituitarism Date | Derived |
| 49 | SALVDT | Num | Salvage Date | Derived |
| 50 | DEATHDT | Num | Death Date | Derived |

---

### 2.2 ADLB — Laboratory Analysis Dataset

| # | Variable | Type | Label | Derivation |
|---|---------|------|-------|------------|
| 1 | STUDYID | Char | Study Identifier | |
| 2 | USUBJID | Char | Unique Subject ID | |
| 3 | PARAMCD | Char | Parameter Code | IGF1/GH/OGTTGH/IGF1I |
| 4 | PARAM | Char | Parameter Description | |
| 5 | AVISIT | Char | Analysis Visit | |
| 6 | AVISITN | Num | Analysis Visit Number | |
| 7 | ADT | Num | Analysis Date | |
| 8 | ADY | Num | Analysis Day | |
| 9 | AVAL | Num | Analysis Value | |
| 10 | BASE | Num | Baseline Value | |
| 11 | CHG | Num | Change from Baseline | |
| 12 | PCHG | Num | Percent Change | |
| 13 | ANRIND | Char | Reference Range Indicator | |

---

### 2.3 ADENDO — Endocrine Analysis Dataset

| # | Variable | Type | Label | Notes |
|---|---------|------|-------|-------|
| 1 | STUDYID | Char | Study Identifier | |
| 2 | USUBJID | Char | Unique Subject ID | |
| 3 | ADT | Num | Assessment Date | |
| 4 | ADY | Num | Assessment Day | |
| 5 | IGF1I | Num | IGF-1 Index | |
| 6 | GH | Num | Growth Hormone | |
| 7 | OGTTGH | Num | OGTT Nadir GH | |
| 8 | ON_MED | Char | On Medication | Y/N |
| 9 | ENDO_STATUS | Char | Endocrine Status | UNCONTROLLED/ENDO_CONTROL/BIOCHEM_REM/RECURR |
| 10 | FIRSTREM_FL | Char | First Remission Flag | |
| 11 | POSTREM_FL | Char | Post-Remission Flag | |
| 12 | RECURR_EVENT_FL | Char | Recurrence Event Flag | |

---

### 2.4 ADTTE — Time-to-Event Dataset

| # | Variable | Type | Label | Notes |
|---|---------|------|-------|-------|
| 1 | STUDYID | Char | Study Identifier | |
| 2 | USUBJID | Char | Unique Subject ID | |
| 3 | PARAMCD | Char | Parameter Code | TTRREM/TTDREC/TTPROG/TTHYPO/TTSALV/OS |
| 4 | PARAM | Char | Parameter Description | |
| 5 | STARTDT | Num | Start Date | INDEXDT |
| 6 | ADT | Num | Event/Censor Date | |
| 7 | CNSR | Num | Censoring Indicator | 0=event, 1=censored |
| 8 | AVAL | Num | Time Value (days) | |
| 9 | EVNTDESC | Char | Event Description | |
| 10 | SRCDOM | Char | Source Domain | |
| 11 | SRCVAR | Char | Source Variable | |

---

## Part 3: Minimum Deliverable Version

### 3.1 SDTM Minimum Files (Required)

| File | Description | Priority |
|------|-------------|----------|
| dm.sas7bdat | Demographics | Required |
| ds.sas7bdat | Disposition | Required |
| cm.sas7bdat | Medications | Required |
| pr.sas7bdat | Procedures (GKS) | Required |
| lb.sas7bdat | Labs (IGF-1, GH) | Required |
| ae.sas7bdat | Adverse Events | Required |
| fa.sas7bdat | Findings (Knosp, plan type) | Strongly Recommended |

### 3.2 ADaM Minimum Files (Required)

| File | Description | Priority |
|------|-------------|----------|
| adsl.sas7bdat | Subject-level analysis | Required |
| adlb.sas7bdat | Lab analysis | Required |
| adtte.sas7bdat | Time-to-event | Required |

---

## Part 4: Programming Next Steps

### Step 1: Create import programs for each SDTM domain
### Step 2: Build SDTM datasets following variable specs
### Step 3: Create derivation programs for ADaM
### Step 4: Build ADSL, ADLB, ADTTE
### Step 5: Run QC and validation
### Step 6: Generate analysis outputs

---

*Document created: 2026-03-21*
*Version: Excel Style - Production Ready*
