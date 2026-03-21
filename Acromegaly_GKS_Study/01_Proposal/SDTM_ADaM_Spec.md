# SDTM & ADaM Specification
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Document Purpose
This specification defines the SDTM and ADaM datasets for a multicenter retrospective study of Gamma Knife radiosurgery for cavernous sinus-invading acromegaly. The approach extends CDISC oncology standards to endocrine tumors while maintaining compliance with CDISC Foundational Standards.

---

## Part 1: SDTM Domains

### 1.1 DM — Demographics

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "DM" |
| USUBJID | Yes | Char | Unique subject identifier |
| SUBJID | No | Char | Subject ID |
| SITEID | Yes | Char | Site identifier |
| AGE | No | Num | Age |
| AGEU | No | Char | Age units (YEARS) |
| SEX | Yes | Char | Sex (M/F/UN) |
| RACE | No | Char | Race |
| ETHNIC | No | Char | Ethnicity |
| COUNTRY | No | Char | Country |

---

### 1.2 DS — Disposition

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "DS" |
| USUBJID | Yes | Char | Unique subject identifier |
| DSSEQ | Yes | Num | Sequence number |
| DSTERM | Yes | Char | Disposition term |
| DSDECOD | Yes | Char | Standardized disposition term |
| DSCAT | Yes | Char | Category |
| DSSTDTC | No | Char | Start date |
| DSENDTC | No | Char | End date |

**Controlled Terms:**

| DSCAT | DSDECOD |
|-------|---------|
| DISPOSITION EVENT | ENROLLED |
| DISPOSITION EVENT | COMPLETED |
| DISPOSITION EVENT | LOST TO FOLLOW-UP |
| DISPOSITION EVENT | DEATH |

---

### 1.3 MH — Medical History

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "MH" |
| USUBJID | Yes | Char | Unique subject identifier |
| MHSEQ | Yes | Num | Sequence number |
| MHTERM | Yes | Char | Medical history term |
| MHDECOD | No | Char | Standardized med history term |
| MHCAT | No | Char | Category |
| MHSTDTC | No | Char | Start date |
| MHENDTC | No | Char | End date |
| MHENRTPT | No | Char | Ongoing (ONGOING) |

**Suggested Categories:**

| MHCAT | MHTERM Examples |
|-------|----------------|
| ENDOCRINE DISORDER | Acromegaly |
| ENDOCRINE DISORDER | Pituitary adenoma |
| ENDOCRINE DISORDER | Hypopituitarism |
| METABOLIC DISORDER | Diabetes mellitus |
| CARDIOVASCULAR | Hypertension |
| CARDIOVASCULAR | Cardiovascular disease |
| RESPIRATORY | Obstructive sleep apnea |

---

### 1.4 CM — Concomitant Medications

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "CM" |
| USUBJID | Yes | Char | Unique subject identifier |
| CMSEQ | Yes | Num | Sequence number |
| CMTRT | Yes | Char | Medication name |
| CMDECOD | No | Char | Standardized medication |
| CMCAT | No | Char | Category |
| CMSTDTC | No | Char | Start date |
| CMENDTC | No | Char | End date |
| CMENDY | No | Num | End relative to reference |
| CMDOSE | No | Num | Dose |
| CMDOSU | No | Char | Dose units |
| CMROUTE | No | Char | Route |
| CMINDC | No | Char | Indication |

**Suggested Categories:**

| CMCAT | CMTRT Examples |
|-------|----------------|
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

---

### 1.5 PR — Procedures

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "PR" |
| USUBJID | Yes | Char | Unique subject identifier |
| PRSEQ | Yes | Num | Sequence number |
| PRTRT | Yes | Char | Procedure treatment |
| PRDECOD | No | Char | Standardized procedure |
| PRCAT | Yes | Char | Category |
| PRSCAT | No | Char | Subcategory |
| PRSTDTC | Yes | Char | Start date |
| PRENDTC | No | Char | End date |
| PRLOC | No | Char | Location |
| PRDOSE | No | Num | Dose (Gy for radiation) |
| PRDOSU | No | Char | Dose units |
| PRDUR | No | Num | Duration |
| PRDURU | No | Char | Duration units |
| PRMETH | No | Char | Method |

**Suggested Records:**

| PRCAT | PRTRT | PRLOC |
|-------|-------|-------|
| SURGICAL PROCEDURE | Transsphenoidal surgery | Sella region |
| RADIOSURGERY | Gamma Knife radiosurgery | Cavernous sinus |
| RADIOSURGERY | Gamma Knife radiosurgery | Sellar region |
| SURGICAL PROCEDURE | Repeat transsphenoidal surgery | Sella region |
| RADIOTHERAPY | Fractionated radiotherapy | Sella region |

---

### 1.6 LB — Laboratory Test Results

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "LB" |
| USUBJID | Yes | Char | Unique subject identifier |
| LBSEQ | Yes | Num | Sequence number |
| LBTESTCD | Yes | Char | Test code |
| LBTEST | Yes | Char | Test name |
| LBCAT | No | Char | Category |
| LBSCAT | No | Char | Subcategory |
| LBORRES | No | Char | Original result |
| LBORRESU | No | Char | Original units |
| LBSTRESN | No | Num | Numeric result |
| LBSTRESC | No | Char | Character result |
| LBSTRESU | No | Char | Standard units |
| LBNRIND | No | Char | Reference range indicator |
| LBSTNRLO | No | Num | Reference range low |
| LBSTNRHI | No | Num | Reference range high |
| LBDTC | Yes | Char | Collection date |
| LBDY | No | Num | Day relative to reference |
| VISITNUM | No | Num | Visit number |
| VISIT | No | Char | Visit name |
| LBBLFL | No | Char | Baseline flag (Y/N) |

**Core Tests:**

| LBTESTCD | LBTEST | LBSTRESU | LBCAT |
|-----------|--------|----------|-------|
| IGF1 | Insulin-Like Growth Factor 1 | ng/mL | ENDOCRINE |
| IGF1I | IGF-1 Index | ratio | ENDOCRINE |
| GH | Growth Hormone | ng/mL | ENDOCRINE |
| OGTTGH | OGTT Nadir GH | ng/mL | ENDOCRINE |
| TSH | Thyroid Stimulating Hormone | mIU/L | PITUITARY |
| FT4 | Free Thyroxine | ng/dL | PITUITARY |
| CORTISOL | Serum Cortisol | mcg/dL | PITUITARY |
| ACTH | ACTH | pg/mL | PITUITARY |
| FSH | FSH | mIU/mL | PITUITARY |
| LH | LH | mIU/mL | PITUITARY |
| TESTOST | Testosterone | ng/dL | PITUITARY |
| ESTRAD | Estradiol | pg/mL | PITUITARY |
| PROLACTIN | Prolactin | ng/mL | PITUITARY |

---

### 1.7 TU — Tumor Identification

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "TU" |
| USUBJID | Yes | Char | Unique subject identifier |
| TULNKID | Yes | Char | Link identifier |
| TUSEQ | Yes | Num | Sequence number |
| TUTESTCD | Yes | Char | Test code |
| TUTEST | Yes | Char | Test name |
| TUORRES | No | Char | Original result |
| TULOC | No | Char | Location |
| TUTYPE | No | Char | Type |
| TUDTC | No | Char | Date |

**Suggested Values:**

| TUTESTCD | TUTEST | TUORRES | TULOC | TUTYPE |
|-----------|--------|---------|-------|--------|
| TUMIDENT | Tumor Identification | Residual adenoma | Cavernous sinus | TARGET LESION |
| TUMIDENT | Tumor Identification | Residual adenoma | Sellar | TARGET LESION |
| TUMIDENT | Tumor Identification | Recurrent disease | Cavernous sinus | TARGET LESION |

---

### 1.8 TR — Tumor Results

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "TR" |
| USUBJID | Yes | Char | Unique subject identifier |
| TRLNKID | Yes | Char | Link to TU |
| TRSEQ | Yes | Num | Sequence number |
| TRTESTCD | Yes | Char | Test code |
| TRTEST | Yes | Char | Test name |
| TRORRES | No | Char | Original result |
| TRSTRESN | No | Num | Numeric result |
| TRSTRESC | No | Char | Character result |
| TRSTRESU | No | Char | Units |
| TRMETHOD | No | Char | Method |
| TRDTC | Yes | Char | Assessment date |
| TRDY | No | Num | Day relative to reference |
| VISITNUM | No | Num | Visit number |
| VISIT | No | Char | Visit name |

**Core Tests:**

| TRTESTCD | TRTEST | TRSTRESU | TRMETHOD |
|-----------|--------|----------|----------|
| TUMVOL | Tumor Volume | cc | MRI volumetric |
| TUMVOL | Tumor Volume | cc | MRI estimated |
| MAXDIM | Maximum Diameter | mm | MRI |

---

### 1.9 RS — Disease Response

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "RS" |
| USUBJID | Yes | Char | Unique subject identifier |
| RSLINKID | No | Char | Link identifier |
| RSSEQ | Yes | Num | Sequence number |
| RSTESTCD | Yes | Char | Test code |
| RSTEST | Yes | Char | Test name |
| RSORRES | No | Char | Original result |
| RSSTRESC | No | Char | Standardized result |
| RSDTC | Yes | Char | Assessment date |
| RDY | No | Num | Day relative to reference |
| RSEVAL | No | Char | Evaluator |
| VISITNUM | No | Num | Visit number |
| VISIT | No | Char | Visit name |

**Response Systems:**

**A. Endocrine Response (RSTESTCD = ENDORESP)**

| RSSTRESC | Definition |
|----------|------------|
| REMISSION | IGF-1 normal, off medication |
| CONTROL_ON_MED | IGF-1 normal, on medication |
| UNCONTROLLED | IGF-1 elevated |
| RECURRENCE | Biochemical recurrence after prior remission |

**B. Imaging Response (RSTESTCD = IMGRESP)**

| RSSTRESC | Definition |
|----------|------------|
| DECREASED | Tumor volume decreased |
| STABLE | Tumor volume stable |
| PROGRESSED | Tumor volume increased |
| INEVALUABLE | Cannot be assessed |

---

### 1.10 AE — Adverse Events

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "AE" |
| USUBJID | Yes | Char | Unique subject identifier |
| AESEQ | Yes | Num | Sequence number |
| AETERM | Yes | Char | Adverse event term |
| AEDECOD | No | Char | Standardized term |
| AEBODSYS | No | Char | Body system |
| AESEV | No | Char | Severity |
| AESER | No | Char | Serious (Y/N) |
| AEREL | No | Char | Relationship |
| AEPT | No | Char | Preferred term |
| AESTDTC | Yes | Char | Start date |
| AEENDTC | No | Char | End date |
| AEENDY | No | Num | End day |
| AEOUT | No | Char | Outcome |
| AECAT | No | Char | Category |

**Key Events:**

| AECAT | AEDECOD Examples |
|-------|-------------------|
| VISUAL TOXICITY | Visual acuity decreased |
| VISUAL TOXICITY | Visual field defect |
| VISUAL TOXICITY | Optic neuropathy |
| CRANIAL NERVE | Cranial nerve palsy |
| RADIATION | Adverse radiation effect |
| RADIATION | Radionecrosis |
| ENDOCRINE | Hypopituitarism |

---

### 1.11 FA — Findings About

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "FA" |
| USUBJID | Yes | Char | Unique subject identifier |
| FASEQ | Yes | Num | Sequence number |
| FATESTCD | Yes | Char | Test code |
| FATEST | Yes | Char | Test name |
| FAORRES | No | Char | Original result |
| FASTRESC | No | Char | Standardized result |
| FANRIND | No | Char | Reference range indicator |
| FADTC | Yes | Char | Date |
| FADY | No | Num | Day relative to reference |
| FAEVAL | No | Char | Evaluator |

**Disease-Specific Findings:**

| FATESTCD | FATEST | FASTRESC Examples |
|-----------|--------|-------------------|
| KNOSP | Knosp Grade | 0, 1, 2, 3, 4 |
| PLANTYPE | Radiosurgery Plan Type | TARGETED / WHOLE_SELLA / MIXED |
| MEDHOLD | Medication Hold Around GKS | YES / NO |
| CSI | Cavernous Sinus Invasion | CONFIRMED / NOT_CONFIRMED |

---

### 1.12 SV — Subject Visits

| Variable | Core | Type | Description |
|----------|------|------|-------------|
| STUDYID | Yes | Char | Study identifier |
| DOMAIN | Yes | Char | "SV" |
| USUBJID | Yes | Char | Unique subject identifier |
| VISITNUM | Yes | Num | Visit number |
| VISIT | Yes | Char | Visit name |
| SVSTDTC | No | Char | Visit start date |
| SVENDTC | No | Char | Visit end date |
| SVSTDY | No | Num | Start day |
| SVENDY | No | Num | End day |

**Suggested Visits:**

| VISITNUM | VISIT | Expected Timing |
|----------|-------|-----------------|
| 1 | BASELINE | Index GKS |
| 2 | POSTGKS_3M | 3 months post-GKS |
| 3 | POSTGKS_6M | 6 months post-GKS |
| 4 | POSTGKS_12M | 12 months post-GKS |
| 5 | POSTGKS_24M | 24 months post-GKS |
| 6 | POSTGKS_36M | 36 months post-GKS |
| 7 | POSTGKS_48M | 48 months post-GKS |
| 8 | POSTGKS_60M | 60 months post-GKS |

---

## Part 2: ADaM Datasets

### 2.1 ADSL — Subject-Level Analysis Dataset

| Variable | Type | Description | Source |
|----------|------|-------------|--------|
| STUDYID | Char | Study identifier | DM |
| USUBJID | Char | Unique subject ID | DM |
| SITEID | Char | Site identifier | DM |
| AGE | Num | Age at index GKS | DM → derived |
| SEX | Char | Sex | DM |
| INDEXDT | Num | Index GKS date | PR |
| FASFL | Char | Full analysis set flag | DS → derived |
| EFFL | Char | Endocrine evaluable flag | Derived |
| IMGEVLFL | Char | Imaging evaluable flag | Derived |
| SAFFL | Char | Safety analysis flag | Derived |
| KNOSP | Num | Knosp grade | FA or TU |
| KNOSPGR | Char | Knosp grade group | Derived |
| CSI_DEF_TYPE | Char | CSI definition type | FA |
| BASE_TUMVOL | Num | Baseline tumor volume | TR |
| BASE_LOC | Char | Baseline location | TU |
| PRIOR_SURG_N | Num | Number of prior surgeries | PR → derived |
| LASTSURGDT | Num | Last surgery date | PR → derived |
| SURG2GKS_DAYS | Num | Days from surgery to GKS | Derived |
| SURG2GKS_MOS | Num | Months from surgery to GKS | Derived |
| EARLYGKS_FL | Char | Early GKS flag | Derived |
| PRIOR_MEDS_FL | Char | Prior medical therapy flag | CM → derived |
| BASE_IGF1 | Num | Baseline IGF-1 | LB |
| BASE_IGF1_ULN | Num | Baseline IGF-1 ULN | LB |
| BASE_IGF1I | Num | Baseline IGF-1 index | LB → derived |
| BASE_GH | Num | Baseline GH | LB |
| BASE_OGTTGH | Num | Baseline OGTT nadir GH | LB |
| PLAN_TYPE | Char | Radiosurgery plan type | FA |
| TARGETED_FL | Char | Targeted plan flag | Derived |
| WHOLESELLA_FL | Char | Whole-sella plan flag | Derived |
| MARGINDOSE | Num | Margin dose (Gy) | PR |
| MAXDOSE | Num | Maximum dose (Gy) | PR |
| ISODOSE | Num | Isodose line (%) | PR |
| OPTICMAX | Num | Optic apparatus max dose (Gy) | PR |
| BED | Num | Biologically effective dose | PR → derived |
| BEDGR1 | Char | BED group | Derived |
| MEDHOLD_CAT | Char | Medication hold category | FA → derived |
| FUPDT | Num | Last follow-up date | DS |
| FUP_DAYS | Num | Follow-up days | Derived |
| FUP_MOS | Num | Follow-up months | Derived |
| REMISS_FL | Char | Ever remission flag | Derived |
| DURREMISS_FL | Char | Durable remission flag | Derived |
| RECURR_FL | Char | Recurrence flag | Derived |
| PROG_FL | Char | Progression flag | Derived |
| TUMCTRL_FL | Char | Tumor control flag | Derived |
| HYPOPIT_FL | Char | New hypopituitarism flag | Derived |
| SALVAGE_FL | Char | Salvage treatment flag | Derived |
| DEATH_FL | Char | Death flag | Derived |
| FIRSTREMDT | Num | First remission date | Derived |
| RECURRDT | Num | Recurrence date | Derived |
| PROGDT | Num | Progression date | Derived |
| HYPODT | Num | New hypopituitarism date | Derived |
| SALVDT | Num | Salvage date | Derived |
| DEATHDT | Num | Death date | Derived |

---

### 2.2 ADLB — Laboratory Analysis Dataset (BDS)

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| PARAMCD | Char | Parameter code |
| PARAM | Char | Parameter description |
| AVISIT | Char | Analysis visit |
| AVISITN | Num | Analysis visit number |
| ADT | Num | Analysis date |
| ADY | Num | Analysis day |
| AVAL | Num | Analysis value |
| BASE | Num | Baseline value |
| CHG | Num | Change from baseline |
| PCHG | Num | Percent change from baseline |
| ANRIND | Char | Reference range indicator |
| ONMED | Char | On medication (Y/N) |

**Parameters:**

| PARAMCD | PARAM |
|---------|-------|
| IGF1 | Insulin-Like Growth Factor 1 |
| IGF1I | IGF-1 Index |
| GH | Growth Hormone |
| OGTTGH | OGTT Nadir GH |

---

### 2.3 ADENDO — Endocrine Analysis Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| ADT | Num | Assessment date |
| ADY | Num | Assessment day |
| AVISIT | Char | Visit |
| AVISITN | Num | Visit number |
| IGF1I | Num | IGF-1 Index |
| GH | Num | Growth Hormone |
| OGTTGH | Num | OGTT nadir GH |
| ON_MED | Char | On medication (Y/N) |
| ENDO_STATUS | Char | Endocrine status |
| FIRSTREM_FL | Char | First remission flag |
| POSTREM_FL | Char | Post-remission flag |
| RECURR_EVENT_FL | Char | Recurrence event flag |

**ENDO_STATUS Values:**

| Value | Definition |
|-------|------------|
| UNCONTROLLED | IGF-1i > 1 |
| ENDO_CONTROL | IGF-1i ≤ 1, on medication |
| BIOCHEM_REM | IGF-1i ≤ 1, off medication |
| RECURR | Biochemical recurrence |
| INDETERMINATE | Cannot be determined |

---

### 2.4 ADIMG — Imaging Analysis Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| ADT | Num | MRI date |
| ADY | Num | Days from index |
| AVISIT | Char | Visit |
| AVISITN | Num | Visit number |
| TUMVOL | Num | Tumor volume (cc) |
| VOLCHG | Num | Change from baseline |
| VOLCHGPCT | Num | Percent change |
| MRIRESP | Char | MRI response |
| PROG_EVENT_FL | Char | Progression event flag |
| TUMCTRL_FL | Char | Tumor control flag |

**MRIRESP Values:**

| Value | Definition |
|-------|------------|
| DECREASED | Volume decreased |
| STABLE | Volume stable |
| PROGRESSED | Volume increased >20% |
| INEVALUABLE | Cannot be assessed |

---

### 2.5 ADRAD — Radiosurgery Analysis Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| GKSDT | Num | GKS date |
| PLAN_TYPE | Char | Plan type |
| TARGETVOL_CC | Num | Target volume |
| MARGINDOSE | Num | Margin dose (Gy) |
| MAXDOSE | Num | Maximum dose (Gy) |
| ISODOSE | Num | Isodose line (%) |
| OPTICMAX | Num | Optic max dose (Gy) |
| BED | Num | Biologically effective dose |
| NISOCENTER | Num | Number of isocenters |

---

### 2.6 ADPIT — Pituitary Function Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| ADT | Num | Assessment date |
| ADY | Num | Days from index |
| AXIS | Char | Pituitary axis |
| BASE_DEF_FL | Char | Baseline deficit flag |
| NEW_DEF_FL | Char | New deficit flag |
| DEF_STATUS | Char | Deficit status |

**AXIS Values:**

| Value | Definition |
|-------|------------|
| THYROID | Thyroid axis |
| ADRENAL | Adrenal axis |
| GONADAL | Gonadal axis |
| GH | Growth hormone axis |
| POSTPIT | Posterior pituitary |

---

### 2.7 ADAE — Adverse Event Analysis Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| AEDECOD | Char | Standardized term |
| AESTDT | Num | Start date |
| AEENDT | Num | End date |
| TRTEMFL | Char | Treatment-related flag |
| AEREL | Char | Relationship |
| AESEV | Char | Severity |
| AECAT | Char | Category |
| VISUAL_AE_FL | Char | Visual toxicity flag |
| CN_AE_FL | Char | Cranial nerve flag |
| ARE_AE_FL | Char | Radiation effect flag |

---

### 2.8 ADINT — Intervention Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| INTDT | Num | Intervention date |
| INTDY | Num | Days from index |
| INTTYPE | Char | Intervention type |
| INTREAS | Char | Intervention reason |

**INTTYPE Values:**

| Value | Definition |
|-------|------------|
| REPEAT_SURGERY | Repeat transsphenoidal surgery |
| REPEAT_SRS | Repeat stereotactic radiosurgery |
| FRACTIONATED_RT | Fractionated radiotherapy |
| MED_ESCALATION | Medication escalation |

---

### 2.9 ADTTE — Time-to-Event Dataset

| Variable | Type | Description |
|----------|------|-------------|
| STUDYID | Char | Study identifier |
| USUBJID | Char | Unique subject ID |
| PARAMCD | Char | Parameter code |
| PARAM | Char | Parameter description |
| STARTDT | Num | Start date |
| ADT | Num | Event/censoring date |
| CNSR | Num | Censoring indicator (0=event, 1=censored) |
| AVAL | Num | Time to event (days) |
| EVNTDESC | Char | Event description |
| SRCDOM | Char | Source domain |
| SRCVAR | Char | Source variable |

**Endpoints:**

| PARAMCD | PARAM | Definition |
|---------|-------|------------|
| TTRREM | Time to First Endocrine Remission | Days to first biochemical remission |
| TTDREM | Time to Durable Remission | Days to confirmed durable remission |
| TTRREC | Time to Biochemical Recurrence | Days from remission to recurrence |
| TTPROG | Time to Radiographic Progression | Days to tumor progression |
| TTHYPO | Time to New Hypopituitarism | Days to new pituitary deficit |
| TTSALV | Time to Salvage Intervention | Days to salvage treatment |
| OS | Overall Survival | Days to death |

---

## Part 3: Key Derivation Rules

### 3.1 Baseline Selection

**Rule:** Select closest assessment before index GKS within:
- Primary window: 90 days
- Secondary window: 180 days

**Variables:**
- BASE90_FL = Y if within 90 days
- BASE180_FL = Y if within 180 days

---

### 3.2 IGF-1 Index

```
IGF1I = IGF1 / IGF1_ULN
```

---

### 3.3 Endocrine Remission

**Required (all must be true):**
1. IGF1I ≤ 1.0
2. ON_MED = N

**Conditional:**
3. If OGTT available: OGTTGH < 0.4 ng/mL

---

### 3.4 Endocrine Control

**Required:**
1. IGF1I ≤ 1.0
2. ON_MED = Y

---

### 3.5 Biochemical Recurrence

**Required (after prior remission):**
1. IGF1I > 1.0
OR
2. Medication restarted/escalated for disease relapse

---

### 3.6 Radiographic Progression

**Primary:**
- Volume increase >20% from nadir or baseline

**Alternative:**
- MRI response = "PROGRESSED"

---

### 3.7 New Hypopituitarism

**Required:**
1. Baseline deficit for axis = N
2. Post-GKS new deficit for same axis = Y

---

### 3.8 Early vs Delayed GKS

```
EARLYGKS_FL = Y if SURG2GKS_MOS ≤ 12
EARLYGKS_FL = N if SURG2GKS_MOS > 12
```

---

### 3.9 Medication Hold Category

```
if no prior medication → MEDHOLD_CAT = "NO_MED"
else if medication held peri-GKS → MEDHOLD_CAT = "ON_MED_HOLD"
else → MEDHOLD_CAT = "ON_MED_NO_HOLD"
```

---

## Part 4: Data Flow

```
Raw Data → SDTM → ADaM → Analysis
   ↓           ↓
  DM         ADSL
  DS         ADLB
  MH         ADENDO
  CM         ADIMG
  PR         ADRAD
  LB         ADPIT
  TU         ADAE
  TR         ADINT
  RS         ADTTE
  AE
  FA
  SV
```

---

## Part 5: Dataset Relationships

```
ADSL (one row per subject)
├── ADLB (many rows per subject)
├── ADENDO (many rows per subject)
├── ADIMG (many rows per subject)
├── ADRAD (one row per GKS)
├── ADPIT (many rows per subject)
├── ADAE (many rows per subject)
├── ADINT (many rows per subject)
└── ADTTE (many rows per subject per endpoint)
```

---

## Part 6: Implementation Notes

### 6.1 Non-RECIST Approach
This study does NOT use RECIST criteria. Instead:
- Imaging uses volumetric measurements (cc)
- Response is categorized as DECREASED/STABLE/PROGRESSED
- Endocrine response is primary efficacy measure

### 6.2 IGF-1 Index
- Stored in SDTM LB as LBTESTCD = "IGF1I"
- ULN stored in LBSTNRHI for reference
- IGF1I can also be derived in ADaM

### 6.3 Gamma Knife as Procedure
- GKS is captured in PR domain (not EX)
- Dosimetry parameters stored in PR
- This is the primary treatment for this study

### 6.4 Disease-Specific Response
- RS domain adapted for endocrine response
- New response categories: REMISSION, CONTROL, UNCONTROLLED, RECURRENCE

---

*Document created: 2026-03-21*
