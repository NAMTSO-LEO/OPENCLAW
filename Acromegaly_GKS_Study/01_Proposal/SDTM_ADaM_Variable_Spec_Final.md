# SDTM & ADaM Variable-Level Specification
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly
### Final Production-Ready Version

---

## Part 1: SDTM Variable Specification

### 1.1 DM — Demographics

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | DM |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | SUBJID | No | Char | 20 | Subject ID | - |
| 5 | SITEID | Yes | Char | 10 | Site identifier | - |
| 6 | AGE | No | Num | 8 | Age | - |
| 7 | AGEU | No | Char | 10 | Age units | YEARS |
| 8 | SEX | Yes | Char | 1 | Sex | M/F/UN |
| 9 | RACE | No | Char | 40 | Race | - |
| 10 | ETHNIC | No | Char | 40 | Ethnicity | - |
| 11 | COUNTRY | No | Char | 3 | Country | - |

---

### 1.2 DS — Disposition

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | DS |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | DSSEQ | Yes | Num | 8 | Sequence number | - |
| 5 | DSTERM | Yes | Char | 100 | Disposition term | - |
| 6 | DSDECOD | No | Char | 100 | Standardized term | ENROLLED/COMPLETED/LOST TO FOLLOW-UP/DEATH |
| 7 | DSCAT | Yes | Char | 50 | Category | DISPOSITION EVENT |
| 8 | DSSTDTC | No | Char | 10 | Start date (YYYY-MM-DD) | - |
| 9 | DSENDTC | No | Char | 10 | End date | - |

---

### 1.3 MH — Medical History

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | MH |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | MHSEQ | Yes | Num | 8 | Sequence number | - |
| 5 | MHTERM | Yes | Char | 200 | Medical history term | - |
| 6 | MHDECOD | No | Char | 100 | Standardized term | - |
| 7 | MHCAT | No | Char | 50 | Category | ENDOCRINE DISORDER/METABOLIC DISORDER/CARDIOVASCULAR/RESPIRATORY |
| 8 | MHSTDTC | No | Char | 10 | Start date | - |
| 9 | MHENDTC | No | Char | 10 | End date | - |
| 10 | MHENRTPT | No | Char | 10 | End relative to reference | ONGOING |

---

### 1.4 CM — Concomitant Medications

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | CM |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | CMSEQ | Yes | Num | 8 | Sequence number | - |
| 5 | CMTRT | Yes | Char | 100 | Medication name | - |
| 6 | CMDECOD | No | Char | 100 | Standardized medication | - |
| 7 | CMCAT | No | Char | 50 | Category | ACROMEGALY TREATMENT/HORMONE REPLACEMENT |
| 8 | CMSTDTC | No | Char | 10 | Start date | - |
| 9 | CMENDTC | No | Char | 10 | End date | - |
| 10 | CMENDY | No | Num | 8 | End day relative to reference | - |
| 11 | CMDOSE | No | Num | 8 | Dose | - |
| 12 | CMDOSU | No | Char | 20 | Dose units | - |
| 13 | CMROUTE | No | Char | 20 | Route | - |
| 14 | CMINDC | No | Char | 100 | Indication | - |

---

### 1.5 PR — Procedures

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | PR |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | PRSEQ | Yes | Num | 8 | Sequence number | - |
| 5 | PRTRT | Yes | Char | 100 | Procedure treatment | - |
| 6 | PRDECOD | No | Char | 100 | Standardized procedure | - |
| 7 | PRCAT | Yes | Char | 50 | Category | SURGICAL PROCEDURE/RADIOSURGERY |
| 8 | PRSCAT | No | Char | 50 | Subcategory | PRIMARY/REPEAT/SALVAGE |
| 9 | PRSTDTC | Yes | Char | 10 | Start date | - |
| 10 | PRENDTC | No | Char | 10 | End date | - |
| 11 | PRLOC | No | Char | 50 | Location | CAVERNOUS SINUS/SELLA REGION |
| 12 | PRDOSE | No | Num | 8 | Dose (Gy) | - |
| 13 | PRDOSU | No | Char | 10 | Dose units | Gy |
| 14 | PRMETH | No | Char | 30 | Method | - |

---

### 1.6 LB — Laboratory Test Results

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | LB |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | LBSEQ | Yes | Num | 8 | Sequence number | - |
| 5 | LBTESTCD | Yes | Char | 10 | Test code | IGF1/GH/OGTTGH/TSH/FT4/CORTISOL |
| 6 | LBTEST | Yes | Char | 50 | Test name | - |
| 7 | LBCAT | No | Char | 30 | Category | ENDOCRINE/PITUITARY |
| 8 | LBSCAT | No | Char | 30 | Subcategory | ORAL GLUCOSE TOLERANCE TEST |
| 9 | LBORRES | No | Char | 30 | Original result | - |
| 10 | LBORRESU | No | Char | 20 | Original units | ng/mL/mIU/mL/mcg/dL |
| 11 | LBSTRESN | No | Num | 8 | Numeric result | - |
| 12 | LBSTRESC | No | Char | 30 | Character result | - |
| 13 | LBSTRESU | No | Char | 20 | Standard units | - |
| 14 | LBNRIND | No | Char | 10 | Reference range indicator | LOW/NORMAL/HIGH |
| 15 | LBSTNRLO | No | Num | 8 | Reference range low | - |
| 16 | LBSTNRHI | No | Num | 8 | Reference range high | - |
| 17 | LBDTC | Yes | Char | 10 | Collection date | - |
| 18 | LBDY | No | Num | 8 | Day relative to reference | - |
| 19 | VISITNUM | No | Num | 8 | Visit number | - |
| 20 | VISIT | No | Char | 30 | Visit name | - |
| 21 | LBBLFL | No | Char | 1 | Baseline flag | Y/N |

---

### 1.7 FA — Findings About

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | FA |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | FASEQ | Yes | Num | 8 | Sequence number | - |
| 5 | FATESTCD | Yes | Char | 10 | Test code | KNOSP/PLANTYPE/MEDHOLD/CSI/NEWPITDEF |
| 6 | FATEST | Yes | Char | 50 | Test name | - |
| 7 | FAORRES | No | Char | 30 | Original result | - |
| 8 | FASTRESC | No | Char | 30 | Standardized result | - |
| 9 | FANRIND | No | Char | 10 | Reference range indicator | - |
| 10 | FAOBJ | No | Char | 50 | Object | PITUITARY ADENOMA/ACROMEGALY MEDICATION |
| 11 | FADTC | Yes | Char | 10 | Date | - |
| 12 | FADY | No | Num | 8 | Day | - |
| 13 | FAEVAL | No | Char | 30 | Evaluator | INVESTIGATOR/RADIOLOGIST |

---

### 1.8 AE — Adverse Events

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | AE |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | AESEQ | Yes | Num | 8 | Sequence number | - |
| 5 | AETERM | Yes | Char | 200 | Adverse event term | - |
| 6 | AEDECOD | No | Char | 100 | Standardized term | - |
| 7 | AEBODSYS | No | Char | 50 | Body system | - |
| 8 | AESEV | No | Char | 20 | Severity | MILD/MODERATE/SEVERE |
| 9 | AESER | No | Char | 1 | Serious | Y/N |
| 10 | AEREL | No | Char | 20 | Relationship | RELATED/NOT RELATED |
| 11 | AESTDTC | Yes | Char | 10 | Start date | - |
| 12 | AEENDTC | No | Char | 10 | End date | - |
| 13 | AEENDY | No | Num | 8 | End day | - |
| 14 | AEOUT | No | Char | 20 | Outcome | RECOVERED/NOT RECOVERED/FATAL |
| 15 | AECAT | No | Char | 50 | Category | VISUAL/CRANIAL NERVE/RADIATION/ENDOCRINE |

---

### 1.9 TU — Tumor Identification

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | TU |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | TULNKID | Yes | Char | 20 | Link identifier | - |
| 5 | TUSEQ | Yes | Num | 8 | Sequence number | - |
| 6 | TUTESTCD | Yes | Char | 10 | Test code | TUMIDENT |
| 7 | TUTEST | Yes | Char | 30 | Test name | - |
| 8 | TUORRES | No | Char | 30 | Original result | - |
| 9 | TULOC | No | Char | 30 | Location | CAVERNOUS SINUS/SELLAR |
| 10 | TUTYPE | No | Char | 20 | Type | TARGET LESION |
| 11 | TUDTC | No | Char | 10 | Date | - |

---

### 1.10 TR — Tumor Results

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | TR |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | TRLNKID | Yes | Char | 20 | Link to TU | - |
| 5 | TRSEQ | Yes | Num | 8 | Sequence number | - |
| 6 | TRTESTCD | Yes | Char | 10 | Test code | TUMVOL/MAXDIM |
| 7 | TRTEST | Yes | Char | 30 | Test name | - |
| 8 | TRORRES | No | Char | 30 | Original result | - |
| 9 | TRSTRESN | No | Num | 8 | Numeric result | - |
| 10 | TRSTRESC | No | Char | 30 | Character result | - |
| 11 | TRSTRESU | No | Char | 10 | Units | cc/mm |
| 12 | TRMETHOD | No | Char | 30 | Method | MRI VOLUMETRIC/MRI ESTIMATED |
| 13 | TRDTC | Yes | Char | 10 | Assessment date | - |
| 14 | TRDY | No | Num | 8 | Day | - |
| 15 | VISITNUM | No | Num | 8 | Visit number | - |

---

### 1.11 RS — Response Assessment

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | RS |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | RSLNKID | No | Char | 20 | Link identifier | - |
| 5 | RSSEQ | Yes | Num | 8 | Sequence number | - |
| 6 | RSTESTCD | Yes | Char | 10 | Test code | ENDORESP/IMGRESP |
| 7 | RSTEST | Yes | Char | 30 | Test name | - |
| 8 | RSORRES | No | Char | 30 | Original result | - |
| 9 | RSSTRESC | No | Char | 30 | Standardized result | REMISSION/CONTROL_ON_MED/UNCONTROLLED/RECURRENCE/DECREASED/STABLE/PROGRESSED |
| 10 | RSDTC | Yes | Char | 10 | Assessment date | - |
| 11 | RDY | No | Num | 8 | Day | - |
| 12 | RSEVAL | No | Char | 30 | Evaluator | - |
| 13 | VISITNUM | No | Num | 8 | Visit number | - |

---

### 1.12 SV — Subject Visits

| # | Variable | Core | Type | Length | Description | Controlled Terms |
|---|---------|------|------|--------|-------------|-----------------|
| 1 | STUDYID | Yes | Char | 20 | Study identifier | - |
| 2 | DOMAIN | Yes | Char | 2 | Domain name | SV |
| 3 | USUBJID | Yes | Char | 40 | Unique subject identifier | - |
| 4 | VISITNUM | Yes | Num | 8 | Visit number | - |
| 5 | VISIT | Yes | Char | 30 | Visit name | BASELINE/POSTGKS_3M/POSTGKS_6M/POSTGKS_12M etc |
| 6 | SVSTDTC | No | Char | 10 | Visit start date | - |
| 7 | SVENDTC | No | Char | 10 | Visit end date | - |
| 8 | SVSTDY | No | Num | 8 | Start day | - |
| 9 | SVENDY | No | Num | 8 | End day | - |

---

## Part 2: ADaM Variable Specification

### 2.1 ADSL — Subject-Level Analysis Dataset

| # | Variable | Type | Length | Description | Derivation/Source |
|---|---------|------|--------|-------------|-------------------|
| 1 | STUDYID | Char | 20 | Study identifier | DM |
| 2 | USUBJID | Char | 40 | Unique subject ID | DM |
| 3 | SITEID | Char | 10 | Site identifier | DM |
| 4 | AGE | Num | 8 | Age at index GKS | DM → derived |
| 5 | SEX | Char | 1 | Sex | DM |
| 6 | INDEXDT | Num | 8 | Index GKS date | PR → derived |
| 7 | FASFL | Char | 1 | Full analysis set flag | DS → derived |
| 8 | EFFL | Char | 1 | Endocrine evaluable flag | Derived |
| 9 | IMGEVLFL | Char | 1 | Imaging evaluable flag | Derived |
| 10 | SAFFL | Char | 1 | Safety analysis flag | Derived |
| 11 | KNOSP | Num | 8 | Knosp grade | FA → derived |
| 12 | KNOSPGR | Char | 10 | Knosp group | Derived |
| 13 | CSI_DEF_TYPE | Char | 20 | CSI definition type | FA |
| 14 | BASE_TUMVOL | Num | 8 | Baseline tumor volume | TR |
| 15 | BASE_LOC | Char | 30 | Baseline location | TU |
| 16 | PRIOR_SURG_N | Num | 8 | Number of prior surgeries | PR → derived |
| 17 | LASTSURGDT | Num | 8 | Last surgery date | PR → derived |
| 18 | SURG2GKS_DAYS | Num | 8 | Days from surgery to GKS | Derived |
| 19 | SURG2GKS_MOS | Num | 8 | Months from surgery to GKS | Derived |
| 20 | EARLYGKS_FL | Char | 1 | Early GKS flag | Derived |
| 21 | PRIOR_MEDS_FL | Char | 1 | Prior medical therapy flag | CM → derived |
| 22 | BASE_IGF1 | Num | 8 | Baseline IGF-1 | LB |
| 23 | BASE_IGF1_ULN | Num | 8 | Baseline IGF-1 ULN | LB |
| 24 | BASE_IGF1I | Num | 8 | Baseline IGF-1 index | LB → derived |
| 25 | BASE_GH | Num | 8 | Baseline GH | LB |
| 26 | BASE_OGTTGH | Num | 8 | Baseline OGTT nadir GH | LB |
| 27 | PLAN_TYPE | Char | 20 | Radiosurgery plan type | FA |
| 28 | TARGETED_FL | Char | 1 | Targeted plan flag | Derived |
| 29 | WHOLESELLA_FL | Char | 1 | Whole-sella plan flag | Derived |
| 30 | MARGINDOSE | Num | 8 | Margin dose (Gy) | PR |
| 31 | MAXDOSE | Num | 8 | Maximum dose (Gy) | PR |
| 32 | ISODOSE | Num | 8 | Isodose line (%) | PR |
| 33 | OPTICMAX | Num | 8 | Optic max dose (Gy) | PR |
| 34 | BED | Num | 8 | Biologically effective dose | Derived |
| 35 | BEDGR1 | Char | 10 | BED group | Derived |
| 36 | MEDHOLD_CAT | Char | 20 | Medication hold category | FA → derived |
| 37 | FUPDT | Num | 8 | Last follow-up date | DS |
| 38 | FUP_DAYS | Num | 8 | Follow-up days | Derived |
| 39 | FUP_MOS | Num | 8 | Follow-up months | Derived |
| 40 | REMISS_FL | Char | 1 | Ever remission flag | ADTTE → derived |
| 41 | DURREMISS_FL | Char | 1 | Durable remission flag | Derived |
| 42 | RECURR_FL | Char | 1 | Recurrence flag | Derived |
| 43 | PROG_FL | Char | 1 | Progression flag | Derived |
| 44 | TUMCTRL_FL | Char | 1 | Tumor control flag | Derived |
| 45 | HYPOPIT_FL | Char | 1 | New hypopituitarism flag | Derived |
| 46 | SALVAGE_FL | Char | 1 | Salvage treatment flag | Derived |
| 47 | DEATH_FL | Char | 1 | Death flag | Derived |
| 48 | FIRSTREMDT | Num | 8 | First remission date | Derived |
| 49 | RECURRDT | Num | 8 | Recurrence date | Derived |
| 50 | PROGDT | Num | 8 | Progression date | Derived |
| 51 | HYPODT | Num | 8 | Hypopituitarism date | Derived |
| 52 | SALVDT | Num | 8 | Salvage date | Derived |
| 53 | DEATHDT | Num | 8 | Death date | Derived |

---

### 2.2 ADLB — Laboratory Analysis Dataset (BDS)

| # | Variable | Type | Length | Description | Derivation |
|---|---------|------|--------|-------------|------------|
| 1 | STUDYID | Char | 20 | Study identifier | - |
| 2 | USUBJID | Char | 40 | Unique subject ID | - |
| 3 | PARAMCD | Char | 10 | Parameter code | IGF1/GH/OGTTGH/IGF1I |
| 4 | PARAM | Char | 30 | Parameter description | - |
| 5 | AVISIT | Char | 30 | Analysis visit | - |
| 6 | AVISITN | Num | 8 | Analysis visit number | - |
| 7 | ADT | Num | 8 | Analysis date | - |
| 8 | ADY | Num | 8 | Analysis day | - |
| 9 | AVAL | Num | 8 | Analysis value | - |
| 10 | BASE | Num | 8 | Baseline value | - |
| 11 | CHG | Num | 8 | Change from baseline | - |
| 12 | PCHG | Num | 8 | Percent change | - |
| 13 | ANRIND | Char | 10 | Reference range indicator | - |

---

### 2.3 ADENDO — Endocrine Analysis Dataset

| # | Variable | Type | Length | Description | Notes |
|---|---------|------|--------|-------------|-------|
| 1 | STUDYID | Char | 20 | Study identifier | - |
| 2 | USUBJID | Char | 40 | Unique subject ID | - |
| 3 | ADT | Num | 8 | Assessment date | - |
| 4 | ADY | Num | 8 | Assessment day | - |
| 5 | AVISIT | Char | 30 | Visit | - |
| 6 | AVISITN | Num | 8 | Visit number | - |
| 7 | IGF1I | Num | 8 | IGF-1 Index | Derived |
| 8 | GH | Num | 8 | Growth Hormone | - |
| 9 | OGTTGH | Num | 8 | OGTT nadir GH | - |
| 10 | ON_MED | Char | 1 | On medication | Y/N |
| 11 | ENDO_STATUS | Char | 20 | Endocrine status | UNCONTROLLED/ENDO_CONTROL/BIOCHEM_REM/RECURR |
| 12 | FIRSTREM_FL | Char | 1 | First remission flag | Derived |
| 13 | POSTREM_FL | Char | 1 | Post-remission flag | Derived |
| 14 | RECURR_EVENT_FL | Char | 1 | Recurrence event flag | Derived |

---

### 2.4 ADTTE — Time-to-Event Dataset

| # | Variable | Type | Length | Description | Notes |
|---|---------|------|--------|-------------|-------|
| 1 | STUDYID | Char | 20 | Study identifier | - |
| 2 | USUBJID | Char | 40 | Unique subject ID | - |
| 3 | PARAMCD | Char | 10 | Parameter code | TTRREM/TTDREC/TTPROG/TTHYPO/TTSALV/OS |
| 4 | PARAM | Char | 40 | Parameter description | - |
| 5 | STARTDT | Num | 8 | Start date | INDEXDT |
| 6 | ADT | Num | 8 | Event/censoring date | - |
| 7 | CNSR | Num | 8 | Censoring indicator | 0=event, 1=censored |
| 8 | AVAL | Num | 8 | Time value (days) | - |
| 9 | EVNTDESC | Char | 100 | Event description | - |
| 10 | SRCDOM | Char | 10 | Source domain | ADENDO/ADIMG/ADPIT/ADINT |
| 11 | SRCVAR | Char | 20 | Source variable | - |

---

### 2.5 ADTTE Endpoint Summary

| PARAMCD | PARAM | STARTDT | Event Definition | CNSR=0 | CNSR=1 |
|---------|-------|---------|-------------------|--------|--------|
| TTRREM | Time to First Endocrine Remission | INDEXDT | First IGF1I≤1, off med | Event date | Last endocrine date |
| TTDREM | Time to Durable Remission | INDEXDT | Confirmed durable | First remission date | Last endocrine date |
| TTRREC | Time to Biochemical Recurrence | INDEXDT | Recurrence after remission | Recurrence date | Last endocrine date |
| TTPROG | Time to Radiographic Progression | INDEXDT | Volume>20% or progressed | Progression date | Last MRI date |
| TTHYPO | Time to New Hypopituitarism | INDEXDT | New axis deficit | Deficit date | Last pituitary date |
| TTSALV | Time to Salvage Intervention | INDEXDT | First salvage treatment | Salvage date | Last follow-up |
| OS | Overall Survival | INDEXDT | Death | Death date | Last known alive |

---

## Part 3: Controlled Terminology Summary

### 3.1 Procedure Categories (PR)

| PRCAT | PRTRT | PRLOC |
|-------|-------|-------|
| SURGICAL PROCEDURE | Transsphenoidal surgery | Sella region |
| RADIOSURGERY | Gamma Knife radiosurgery | Cavernous sinus |
| SURGICAL PROCEDURE | Repeat transsphenoidal surgery | Sella region |
| RADIOTHERAPY | Fractionated radiotherapy | Sella region |

### 3.2 Medication Categories (CM)

| CMCAT | CMTRT |
|-------|-------|
| ACROMEGALY TREATMENT | Octreotide |
| ACROMEGALY TREATMENT | Lanreotide |
| ACROMEGALY TREATMENT | Pegvisomant |
| ACROMEGALY TREATMENT | Bromocriptine |
| ACROMEGALY TREATMENT | Cabergoline |
| HORMONE REPLACEMENT | Levothyroxine |
| HORMONE REPLACEMENT | Hydrocortisone |
| HORMONE REPLACEMENT | Testosterone |
| HORMONE REPLACEMENT | Estrogen |
| HORMONE REPLACEMENT | Desmopressin |

### 3.3 Findings (FA)

| FATESTCD | FASTRESC |
|-----------|----------|
| KNOSP | 0, 1, 2, 3, 4 |
| PLANTYPE | TARGETED / WHOLE_SELLA / MIXED |
| MEDHOLD | YES / NO |
| CSI | CONFIRMED / NOT_CONFIRMED |

### 3.4 Endocrine Status (ADENDO)

| ENDO_STATUS | Definition |
|--------------|------------|
| UNCONTROLLED | IGF1I > 1 |
| ENDO_CONTROL | IGF1I ≤1, on medication |
| BIOCHEM_REM | IGF1I ≤1, off medication |
| RECURR | Biochemical recurrence |

### 3.5 Response Assessment (RS)

| RSTESTCD | RSSTRESC |
|----------|----------|
| ENDORESP | REMISSION / CONTROL_ON_MED / UNCONTROLLED / RECURRENCE |
| IMGRESP | DECREASED / STABLE / PROGRESSED / INEVALUABLE |

---

## Part 4: Key Derivation Formulas

### 4.1 IGF-1 Index
```
BASE_IGF1I = BASE_IGF1 / BASE_IGF1_ULN
```

### 4.2 Early GKS
```
if SURG2GKS_MOS <= 12 then EARLYGKS_FL = 'Y'
else EARLYGKS_FL = 'N'
```

### 4.3 Follow-up Duration
```
FUP_DAYS = FUPDT - INDEXDT
FUP_MOS = FUP_DAYS / 30.4375
```

### 4.4 Remission Candidate
```
REM_CAND = (IGF1I <= 1) AND (ON_MED = 'N') AND (OGTTGH < 0.4 or OGTT not done)
```

---

## Part 5: File Delivery Specification

### 5.1 SDTM File List
1. dm.sas7bdat
2. ds.sas7bdat
3. mh.sas7bdat
4. cm.sas7bdat
5. pr.sas7bdat
6. lb.sas7bdat
7. fa.sas7bdat
8. ae.sas7bdat
9. tu.sas7bdat
10. tr.sas7bdat
11. rs.sas7bdat
12. sv.sas7bdat

### 5.2 ADaM File List
1. adsl.sas7bdat
2. adlb.sas7bdat
3. adendo.sas7bdat
4. adimg.sas7bdat
5. adpit.sas7bdat
6. adrad.sas7bdat
7. adint.sas7bdat
8. adae.sas7bdat
9. adtte.sas7bdat

---

*Document created: 2026-03-21*
*Version: Final Production-Ready*
