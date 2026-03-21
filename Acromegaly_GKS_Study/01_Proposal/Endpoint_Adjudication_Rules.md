# Endpoint Adjudication Rules

## Study: Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## 1. General Principles

### 1.1 Index Date
All time-to-event endpoints use:
- **Index GKS date** = First eligible Gamma Knife radiosurgery date

### 1.2 Baseline Window
- **Preferred:** Within 90 days before index GKS
- **Acceptable:** Within 180 days before index GKS
- **Flag variables:** BASE90_FL, BASE180_FL, BASEOUTWIN_FL

### 1.3 Assessment Hierarchy

| Endpoint | Priority |
|----------|----------|
| Endocrine | 1) Structured lab values → 2) Endo note → 3) Investigator-reported |
| Imaging | 1) Volumetric MRI → 2) Radiology report → 3) Investigator assessment |
| Hypopituitarism | 1) New hormone replacement → 2) Lab-confirmed → 3) Physician note |

### 1.4 Date Rules
- Complete date: Use as-is
- Year-month only: Use 15th of month
- Year only: Use for review, not precise TTE unless verified
- Multiple records: Use earliest date meeting criteria

---

## 2. Endocrine Endpoint Rules

### 2.1 Uncontrolled Disease
- IGF-1 index > 1.0
- OR physician documents active acromegaly without biochemical normalization

### 2.2 Endocrine Control
- IGF-1 index ≤ 1.0
- AND patient remains on GH/IGF-1 lowering medication

### 2.3 Biochemical Remission
**First meeting ALL of:**
1. IGF-1 index ≤ 1.0
2. Off GH/IGF-1 lowering medication
3. If OGTT available: OGTT nadir GH < 0.4 ng/mL

**If OGTT unavailable:**
- Use IGF-1 normal + off medication
- Flag: OGTT_SUPPORT_FL = N

### 2.4 Date of First Biochemical Remission
- Use assessment date meeting criteria
- If lab and medication status differ by ≤30 days: combine
- If >30 days apart: manual review

### 2.5 Durable Endocrine Remission
- Achieved biochemical remission
- No biochemical recurrence until last follow-up
- No restart/escalation of medication for relapse

### 2.6 Biochemical Recurrence
**Only for patients after remission:**

**Event:** First meeting any of:
1. IGF-1 index > 1.0
2. Physician documents recurrent biochemical acromegaly
3. Restart/escalation of medication due to biochemical relapse

**Exclude:** Non-disease medication restart (e.g., insurance, trial)

---

## 3. Imaging Endpoint Rules

### 3.1 Radiographic Tumor Control
- Last evaluable MRI: tumor stable or decreased
- TUMCTRL_FL = Y

### 3.2 Radiographic Progression
**Primary:** Volume increase >20% from nadir or baseline

**Alternative:** Radiology report explicitly states progression

### 3.3 Date of Progression
- First MRI meeting progression criteria
- "Possible minimal increase" = no progression unless confirmed

---

## 4. Salvage Therapy Endpoint Rules

### 4.1 Salvage Intervention
First after index GKS:
1. Repeat pituitary surgery
2. Repeat SRS
3. Fractionated radiotherapy
4. Medication escalation for persistent/recurrent disease

### 4.2 Salvage Reason
- Persistent biochemical disease
- Biochemical recurrence
- Radiographic progression
- Combined failure

---

## 5. Hypopituitarism Endpoint Rules

### 5.1 Baseline Axis Status
Each axis at baseline:
- Thyroid, Adrenal, Gonadal, GH, Posterior pituitary

### 5.2 New Hypopituitarism
First deficit in axis that was normal at baseline:

**Event:** Any of:
1. Documented new hormone replacement
2. Lab-confirmed new axis deficiency
3. Endocrinologist explicitly diagnoses new hypopituitarism

### 5.3 Subject-Level
- Any new axis deficit → HYPOPIT_FL = Y

---

## 6. Visual and Cranial Neuropathy Rules

### 6.1 Visual Toxicity
New or worsened after GKS:
- Visual acuity decline
- Visual field deficit
- Optic neuropathy

**Exclude:** Tumor progression causing visual changes without radiation evidence

### 6.2 Cranial Neuropathy
New or worsened CN III, IV, V, VI dysfunction after GKS, treatment-related

---

## 7. Censoring Rules by Endpoint

| Endpoint | Event Date | Censored Date |
|----------|-----------|----------------|
| TTRREM | FIRSTREMDT | Last endocrine assessment |
| TTDREM | FIRSTREMDT (durable) | Last endocrine assessment |
| TTRREC | RECURRDT | Last endocrine assessment |
| TTPROG | PROGDT | Last MRI date |
| TTHYPO | HYPODT | Last pituitary assessment |
| TTSALV | SALVDT | Last clinical follow-up |
| OS | DEATHDT | Last known alive |

---

## 8. Adjudication Flags

| Flag | Description |
|------|-------------|
| ADJ_FLAG | Manual adjudication needed |
| ADJ_REASON | Reason for adjudication |
| DATA_CONFLICT_FL | Conflicting data exists |
| DATE_IMPUTE_FL | Date imputed |
| OGTT_SUPPORT_FL | OGTT supports remission |
| OUTCOME_CERTAINTY | definite / probable / possible |

---

## 9. Special Scenarios

| Scenario | Rule |
|----------|------|
| IGF-1 normal, still on meds | → ENDO_CONTROL, not remission |
| IGF-1 normal, off meds, no physician note | Can still be remission if criteria met |
| OGTT missing | Don't block remission; flag OGTT_SUPPORT_FL=N |
| Medication status unclear | → Indeterminate, needs adjudication |
| "Minimal change" MRI | Not progression unless confirmed |
| Baseline hypopituitarism | Same axis cannot be "new" deficit |

---

*Created: 2026-03-21*
