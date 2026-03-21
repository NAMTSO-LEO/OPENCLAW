# CDISC Implementation Strategy
## From Oncology TAUG (Pancreatic Cancer) to Endocrine Tumors (Acromegaly)

---

## 1. Core Strategy

### What We're Doing
Using CDISC Oncology TAUG (Pancreatic Cancer) as structural template → extending to Pituitary/Acromegaly

This is **disease-specific implementation on top of foundational CDISC standards**

---

## 2. Domain Mapping: Oncology → Endocrine

| Dimension | Pancreatic Cancer (Oncology TAUG) | Pituitary/Acromegaly | Mapping |
|-----------|-----------------------------------|---------------------|---------|
| Disease | Solid tumor | Endocrine-secreting tumor | Adapt |
| Primary efficacy | ORR / PFS / OS | Endocrine remission / tumor control | **Replace** |
| Imaging | RECIST | MRI + volumetric | Modify |
| Biomarkers | CA19-9 | IGF-1 / GH / IGF-1i | **Replace** |
| Treatment | Chemo / RT | Surgery + GKS + meds | Extend |
| Key risk | Progression | Hypopituitarism | **Replace** |

---

## 3. SDTM Domains: Direct Reuse

These CDISC domains are **unchanged** (structure preserved):

| Domain | Description | Status |
|--------|-------------|--------|
| DM | Demographics | ✅ No change |
| AE | Adverse Events | ✅ No change |
| CM | Concomitant Medications | ✅ No change |
| EX | Exposure | ✅ No change |
| DS | Disposition | ✅ No change |
| SV | Visits | ✅ No change |
| MH | Medical History | ✅ No change |

---

## 4. SDTM Domains: Key Modification

### 4.1 TU (Tumor Identification) → Modified for Pituitary

**Oncology (Pancreatic):**
- TULOC = pancreatic lesion location

**Pituitary Adaptation:**

| Variable | SDTM | Value | Notes |
|----------|------|-------|-------|
| TULOC | TU | Cavernous sinus / Sellar / Parasellar | Tumor location |
| TUTYPE | TU | Residual tumor / Recurrent tumor / Primary | Tumor type |
| TUMETHOD | TU | MRI | Imaging modality |
| TUEVAL | TU | Investigator / Radiologist | Reader |

---

### 4.2 TR (Tumor Results) → Modified

**Oncology:**
- TRTESTCD = "TUMORLEN" (longest diameter)
- TRORRES = length in mm
- TRMETHOD = CT/MRI

**Pituitary Adaptation:**

| Variable | SDTM | Value | Notes |
|----------|------|-------|-------|
| TRTESTCD | TR | TUMVOL / MAXDIM | Volume or max diameter |
| TRORRES | TR | Numeric (cc or mm) | Measurement |
| TRSTRESC | TR | N/A (continuous) | Not RECIST |
| TRMETHOD | TR | MRI volumetric / estimated | Method |
| TRACPT79 | TR | N | Not using RECIST |
| TRLnkID | TR | Link to TU | Links to identification |

---

### 4.3 RS (Response Assessment) → **REPLACED**

This is the **key transformation**:

**Oncology (Pancreatic):**
```
RSSTRESC = CR / PR / SD / PD
```

**Pituitary Adaptation:**

```
RSSTRESC = 
  "Endocrine remission"
  "Endocrine control"
  "Biochemical uncontrolled"
  "Radiographic progression"
```

| Variable | SDTM | Value | Notes |
|----------|------|-------|-------|
| RSTESTCD | RS | BIOCHEM / RADIOGRAF | Assessment type |
| RSSTRESC | RS | As above | Response term |
| RSDTC | RS | Assessment date | |
| RSEVAL | RS | Investigator / Endocrinologist | |
| RSORRES | RS | Same as RSSTRESC | |

---

### 4.4 LB (Laboratory) → **KEY INNOVATION**

In oncology: CA19-9, CA125, etc.

In pituitary: **IGF-1, GH, OGTT**

**New LB for this study:**

| Variable | SDTM | Value | Notes |
|----------|------|-------|-------|
| LBTESTCD | LB | IGF1 / IGF1I / GH / OGTTGH | Test codes |
| LBSTRESN | LB | Numeric | Result |
| LBSTRESC | LB | Character | If needed |
| LBORRESU | LB | ng/mL / unitless | Unit |
| LBNRIND | LB | LOW / NORMAL / HIGH | Reference range |
| LBNRLO / LBNRHI | LB | Reference range | Normal limits |
| LBBLFL | LB | Y / N | Baseline flag |

**IGF-1 Index (IGF1I) as SDTM variable:**
- LBTESTCD = "IGF1I"
- LBSTRESN = IGF-1 / ULN
- LBORRESU = "ratio" or "unitless"

---

### 4.5 PR (Procedures) → **NEW FOR SRS**

In oncology: surgical procedures rarely primary

In pituitary: **Gamma Knife radiosurgery is PRIMARY treatment**

| Variable | SDTM | Value | Notes |
|----------|------|-------|-------|
| PRTRT | PR | Gamma Knife radiosurgery | Treatment name |
| PRSTDTC | PR | GKS date | Start date |
| PRENDTC | PR | (single procedure) | End date |
| PRLOC | PR | Cavernous sinus | Location |
| PRDOSU | PR | Gy | Dose unit |
| PRDOSE | PR | Margin dose | Numeric |
| PRMETHOD | PR | SRS / GKRS | Method |
| PRSEEN | PR | Y | Seen |

---

## 5. ADaM Implementation

### 5.1 ADSL - Subject-Level Analysis Dataset

**Oncology structure retained, with study-specific variables added:**

| Variable | ADaM | Type | Description | Source |
|----------|------|------|-------------|--------|
| BASE_IGF1I | ADSL | Num | Baseline IGF-1 Index | LB |
| BASE_GH | ADSL | Num | Baseline GH | LB |
| BASE_OGTTGH | ADSL | Num | Baseline OGTT nadir | LB |
| KNOSP | ADSL | Num | Knosp grade | TU/TR |
| PLAN_TYPE | ADSL | Char | Radiosurgery plan type | PR |
| MEDHOLD_CAT | ADSL | Char | Medication hold category | CM→EX |
| SURG2GKS_MOS | ADSL | Num | Surgery to GKS interval | DS/PR |
| BED | ADSL | Num | Biologically effective dose | PR |
| OPTICMAX | ADSL | Num | Optic apparatus max dose | PR |

---

### 5.2 ADTTE - Time-to-Event

**Completely reusable oncology structure with new endpoints:**

| PARAMCD | PARAM | Definition | CNSR |
|---------|-------|------------|------|
| TTRREM | Time to First Endocrine Remission | Days to first biochemical remission | 0=event, 1=censored |
| TTRREC | Time to Biochemical Recurrence | Days from remission to recurrence | 0=event, 1=censored |
| TTPROG | Time to Radiographic Progression | Days to tumor progression | 0=event, 1=censored |
| TTHYPO | Time to New Hypopituitarism | Days to new pituitary deficit | 0=event, 1=censored |
| TTSALV | Time to Salvage Treatment | Days to salvage intervention | 0=event, 1=censored |
| OS | Overall Survival | Days to death | 0=event, 1=censored |

---

### 5.3 ADLB - Laboratory Results (BDS)

**Longitudinal hormone data:**

| Variable | ADaM | Type | Description |
|----------|------|------|-------------|
| USUBJID | BDS | Char | Subject ID |
| PARAMCD | BDS | Char | IGF1 / IGF1I / GH / OGTTGH |
| PARAM | BDS | Char | Parameter description |
| AVAL | BDS | Num | Numeric result |
| BASE | BDS | Num | Baseline value |
| CHG | BDS | Num | Change from baseline |
| PCHG | BDS | Num | Percent change from baseline |
| ANL01FL | BDS | Char | Analysis flag |

---

### 5.4 ADENDO - **NEW DATASET**

**Endocrine-specific analysis dataset (not in standard CDISC):**

This is a **study-specific innovation**:

| Variable | ADaM | Type | Description |
|----------|------|------|-------------|
| USUBJID | ADENDO | Char | Subject ID |
| ADT | ADENDO | Num | Assessment date |
| DAYSFROMGKS | ADENDO | Num | Days from GKS |
| IGF1I | ADENDO | Num | IGF-1 Index |
| GH | ADENDO | Num | GH value |
| OGTTGH | ADENDO | Num | OGTT nadir |
| ON_MED | ADENDO | Char | On medication Y/N |
| ENDO_STATUS | ADENDO | Char | UNCONTROLLED / CONTROLLED / REMISSION / RECURR |
| FIRSTREM_FL | ADENDO | Char | First remission flag |
| RECURR_FL | ADENDO | Char | Recurrence flag |

---

## 6. SDTM Mapping Table

### 6.1 Raw to SDTM: DEMO → DM

| Raw Variable | SDTM | Notes |
|--------------|------|-------|
| SITEID | DOMAIN = "DM", SITEID | |
| STUDY_SUBJID | USUBJID | |
| SEX | SEX | M/F/UN |
| AGE_GKS | AGE | |
| AGEU | AGEU | "YEARS" |
| COUNTRY | COUNTRY | |
| RACE / ETHNIC | RACE / ETHNIC | If collected |

---

### 6.2 Raw to SDTM: ENDO → LB

| Raw Variable | SDTM | Notes |
|--------------|------|-------|
| ENDO_DT | LBSTDTC | Collection date |
| IGF1 | LBTESTCD = "IGF1", LBSTRESN = value | |
| IGF1_ULN | LBNRHI | Upper normal limit |
| IGF1I | LBTESTCD = "IGF1I", LBSTRESN = value | IGF-1 / IGF-1_ULN |
| GH | LBTESTCD = "GH", LBSTRESN = value | |
| OGTT_NADIR_GH | LBTESTCD = "OGTTGH", LBSTRESN = value | |
| ENDO_BASE_FL | LBBLFL | Y for baseline |
| ON_MED | LBENDY | Medication status |

---

### 6.3 Raw to SDTM: IMG → TR

| Raw Variable | SDTM | Notes |
|--------------|------|-------|
| MRI_DT | TRDTC | Assessment date |
| TUMOR_VOL | TRTESTCD = "TUMVOL", TRORRES = value | Volume in cc |
| TUMOR_MAXDIM | TRTESTCD = "MAXDIM", TRORRES = value | |
| KNOSP_GRADE | TUTESTCD = "KNOSP", TUORRES = value | |
| MRI_RESPONSE | RSTESTCD = "BIOCHEM", RSSTRESC | |

---

### 6.4 Raw to SDTM: GKS → PR

| Raw Variable | SDTM | Notes |
|--------------|------|-------|
| GKS_DT | PRSTDTC | Procedure date |
| PLAN_TYPE | PRTRT = "Gamma Knife radiosurgery", PRLOC | Target location |
| MARGINDOSE | PRDOSE | |
| MAXDOSE | PRDOSU = "Gy" | |
| TARGET_VOL_CC | PRENOTOT | Target volume |

---

## 7. Key Implementation Decisions

### 7.1 Non-RECIST Response Assessment
- Do NOT use RECIST-based CR/PR/SD/PD
- Use endocrine-based response: remission/control/uncontrolled/progression
- Document in TAUG supplement

### 7.2 IGF-1 Index in SDTM
- LBTESTCD = "IGF1I" 
- LBSTRESN = numeric ratio
- LBORRESU = "ratio" or "unitless"
- Include ULN in LBNRHI

### 7.3 Radiosurgery as Procedure
- Use PR domain (not EX)
- Include dosimetry parameters in PR
- Document in study-specific SDTM IG

### 7.4 Endocrine Response in RS
- RS domain repurposed for biochemical response
- New response criteria: endocrine remission/control/uncontrolled

---

## 8. Academic Value

### What This Achieves

1. **Extends CDISC to endocrine tumors**
   - CDISC currently lacks pituitary/endocrine tumor standards
   - This fills a gap

2. **Defines non-RECIST response system**
   - Traditional: CR/PR/SD/PD
   - New: remission/control/recurrence
   - Methodological innovation

3. **Standardizes SRS data representation**
   - Gamma Knife not in standard CDISC
   - New procedure mapping established

---

## 9. Publication Framework

### Suggested Title

**Extending CDISC Oncology Data Standards to Endocrine Tumors: A Case Study in Cavernous Sinus–Invading Acromegaly**

### Key Sections
1. Pancreatic Cancer TAUG as structural template
2. RECIST → endocrine response adaptation
3. IGF-1 / GH longitudinal modeling
4. New endpoint system (remission/recurrence)
5. ADaM dataset construction

---

## 10. Next Steps

If you want to continue, I can create:
1. **Complete SDTM mapping table** (variable-level)
2. **ADSL + ADTTE + ADENDO complete specs** (directly program-able)

---

*Created: 2026-03-21*
