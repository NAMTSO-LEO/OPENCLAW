# SDTM & ADaM Specification (Acromegaly-Optimized)
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

### Design Philosophy
- **Primary Template:** Diabetes TAUG (endocrine disease focus)
- **Foundation:** CDISC SDTMIG v3.4 / ADaMIG v1.3
- **Selective Borrow:** Oncology TU/TR/RS for MRI tumor information only

---

## 1. SDTM Domain Architecture

### 1.1 Core Domains (Required)

| Domain | Purpose | Priority |
|--------|---------|----------|
| DM | Demographics | Required |
| DS | Disposition | Required |
| MH | Medical History | Required |
| CM | Concomitant Medications | Required |
| PR | Procedures (Surgery, GKS) | Required |
| LB | Laboratory (IGF-1, GH, OGTT) | Required |
| AE | Adverse Events | Required |
| SV | Subject Visits | Required |

### 1.2 Disease-Specific Domains (Recommended)

| Domain | Purpose | Priority |
|--------|---------|----------|
| FA | Findings About (Knosp, plan type, med hold) | Strongly Recommended |
| TU | Tumor Identification (residual tumor location) | Selective |
| TR | Tumor Results (MRI volume) | Selective |
| RS | Disease Response (endocrine + imaging) | Selective |

### 1.3 Rationale

**Why Diabetes TAUG approach:**
- Primary endpoints are IGF-1, GH, OGTT (endocrine labs)
- On/off medication status is critical
- Endocrine remission/control/recurrence are key outcomes
- Not classic solid tumor with RECIST response

**Why selective Oncology borrow:**
- Tumor information is important but secondary
- MRI volumetric assessment ≠ RECIST
- Response categories are different (remission vs CR/PR)

---

## 2. SDTM Domains: Complete Specification

### 2.1 DM — Demographics

Standard CDISC implementation.

### 2.2 DS — Disposition

| DSCAT | DSDECOD |
|-------|---------|
| DISPOSITION EVENT | ENROLLED |
| DISPOSITION EVENT | COMPLETED |
| DISPOSITION EVENT | LOST TO FOLLOW-UP |
| DISPOSITION EVENT | DEATH |

### 2.3 MH — Medical History

| MHCAT | MHTERM Examples |
|-------|----------------|
| ENDOCRINE DISORDER | Acromegaly |
| ENDOCRINE DISORDER | Pituitary adenoma |
| ENDOCRINE DISORDER | Hypopituitarism |
| METABOLIC | Diabetes mellitus |
| CARDIOVASCULAR | Hypertension |
| RESPIRATORY | Obstructive sleep apnea |

### 2.4 CM — Concomitant Medications

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

### 2.5 PR — Procedures

| PRCAT | PRTRT | PRLOC |
|-------|-------|-------|
| SURGICAL PROCEDURE | Transsphenoidal surgery | Sella region |
| RADIOSURGERY | Gamma Knife radiosurgery | Cavernous sinus |
| SURGICAL PROCEDURE | Repeat transsphenoidal surgery | Sella region |
| RADIOTHERAPY | Fractionated radiotherapy | Sella region |

### 2.6 LB — Laboratory (Core Domain)

This is the **primary efficacy domain** for acromegaly.

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

### 2.7 AE — Adverse Events

| AECAT | AEDECOD Examples |
|-------|-----------------|
| VISUAL | Visual acuity decreased |
| VISUAL | Visual field defect |
| VISUAL | Optic neuropathy |
| CRANIAL NERVE | Cranial nerve palsy |
| RADIATION | Adverse radiation effect |
| RADIATION | Radionecrosis |
| ENDOCRINE | Hypopituitarism |

### 2.8 FA — Findings About (Disease-Specific)

| FATESTCD | FATEST | FASTRESC |
|-----------|--------|----------|
| KNOSP | Knosp Grade | 0, 1, 2, 3, 4 |
| PLANTYPE | Radiosurgery Plan Type | TARGETED / WHOLE_SELLA / MIXED |
| MEDHOLD | Medication Hold Around GKS | YES / NO |
| CSI | Cavernous Sinus Invasion | CONFIRMED / NOT_CONFIRMED |
| AXISDEF | Pituitary Axis Deficit | THYROID / ADRENAL / GONADAL / GH / POSTPIT |

### 2.9 TU — Tumor Identification (Selective Borrow)

| TUTESTCD | TUORRES | TULOC | TUTYPE |
|-----------|---------|-------|--------|
| TUMIDENT | Residual adenoma | Cavernous sinus | TARGET |
| TUMIDENT | Residual adenoma | Sellar | TARGET |
| TUMIDENT | Recurrent disease | Cavernous sinus | TARGET |

### 2.10 TR — Tumor Results (Selective Borrow)

| TRTESTCD | TRTEST | TRSTRESU | TRMETHOD |
|-----------|--------|----------|----------|
| TUMVOL | Tumor Volume | cc | MRI volumetric |
| TUMVOL | Tumor Volume | cc | MRI estimated |
| MAXDIM | Maximum Diameter | mm | MRI |

### 2.11 RS — Disease Response (Selective Borrow)

**A. Endocrine Response (Primary)**

| RSTESTCD | RSTEST | RSSTRESC |
|-----------|--------|----------|
| ENDORESP | Endocrine Response | REMISSION |
| ENDORESP | Endocrine Response | CONTROL_ON_MED |
| ENDORESP | Endocrine Response | UNCONTROLLED |
| ENDORESP | Endocrine Response | RECURRENCE |

**B. Imaging Response (Secondary)**

| RSTESTCD | RSTEST | RSSTRESC |
|-----------|--------|----------|
| IMGRESP | Imaging Response | DECREASED |
| IMGRESP | Imaging Response | STABLE |
| IMGRESP | Imaging Response | PROGRESSED |
| IMGRESP | Imaging Response | INEVALUABLE |

---

## 3. ADaM Dataset Specification

### 3.1 Required Datasets

| Dataset | Purpose | Priority |
|---------|---------|----------|
| ADSL | Subject-level analysis | Required |
| ADLB | Lab results (IGF-1, GH, OGTT) | Required |
| ADTTE | Time-to-event endpoints | Required |

### 3.2 Recommended Disease-Specific Datasets

| Dataset | Purpose | Priority |
|---------|---------|----------|
| ADENDO | Endocrine status over time | Strongly Recommended |
| ADIMG | MRI tumor results | Recommended |
| ADPIT | Pituitary axis function | Strongly Recommended |
| ADRAD | Radiosurgery parameters | Recommended |
| ADAE | Adverse events | Required |
| ADINT | Salvage interventions | Recommended |

---

## 4. Key Differences: Diabetes TAUG vs Oncology TAUG

| Aspect | Diabetes TAUG | Oncology TAUG | This Study |
|--------|---------------|---------------|-------------|
| Primary Endpoint | HbA1c, glucose | ORR, PFS | IGF-1i, remission |
| Lab Focus | Metabolic markers | Tumor markers | IGF-1, GH |
| Response | Not applicable | CR/PR/SD/PD | Remission/Control |
| Treatment | Medications | Chemo/RT | Surgery + GKS + meds |
| Time-to-Event | Not primary | OS, PFS | TTRREM, TTRREC |

**This study follows Diabetes TAUG pattern for:**
- Laboratory-centric endpoints
- Medication status importance
- Long-term disease control concept

---

## 5. ADTTE Endpoints (Final)

| PARAMCD | PARAM | Definition |
|---------|-------|------------|
| TTRREM | Time to First Endocrine Remission | Days to first IGF-1i ≤1, off meds |
| TTDREM | Time to Durable Remission | Days to confirmed durable remission |
| TTRREC | Time to Biochemical Recurrence | Days from remission to recurrence |
| TTPROG | Time to Radiographic Progression | Days to MRI progression |
| TTHYPO | Time to New Hypopituitarism | Days to new pituitary deficit |
| TTSALV | Time to Salvage Intervention | Days to salvage treatment |
| OS | Overall Survival | Days to death |

---

## 6. Derivation Rules Summary

### 6.1 Endocrine Remission
- IGF-1i ≤ 1.0
- Off GH/IGF-1 lowering medication
- OGTT nadir GH < 0.4 if available

### 6.2 Endocrine Control
- IGF-1i ≤ 1.0
- On medication

### 6.3 Biochemical Recurrence
- After prior remission: IGF-1i > 1.0 OR medication restart for relapse

### 6.4 Radiographic Progression
- MRI volume increase >20% from nadir/baseline
- OR MRI response = "PROGRESSED"

### 6.5 New Hypopituitarism
- Baseline: no deficit in that axis
- Post-GKS: new deficit in that axis

---

## 7. Document Position

This specification represents:
- **Foundation:** CDISC SDTMIG v3.4 / ADaMIG v1.3
- **Primary Reference:** Diabetes TAUG (endocrine disease pattern)
- **Secondary Reference:** Oncology TU/TR/RS (selective MRI borrow)
- **No Public TAUG Exists:** For Acromegaly / Pituitary Adenoma

This is a **disease-specific implementation** following CDISC methodology, not an official CDISC-published TAUG.

---

## 8. Key Publications Support

- CDISC public pages show Diabetes TAUG availability
- CDISC public pages show Pancreatic Cancer TAUG availability
- **No Acromegaly TAUG in CDISC public directory**

This validates the "Diabetes TAUG as primary, selective Oncology borrow" approach.

---

*Document created: 2026-03-21*
