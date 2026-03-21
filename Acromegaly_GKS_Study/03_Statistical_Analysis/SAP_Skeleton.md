# SAP Skeleton and ADaM Dataset Design

---

## 1. SAP Table of Contents

1. Title Page
2. Introduction
3. Objectives (Primary, Secondary, Exploratory)
4. Study Design
5. Analysis Populations
6. Study Definitions
7. Endpoints
8. General Statistical Considerations
9. Handling of Missing Data
10. Derivation Rules
11. Statistical Methods
12. Subgroup Analyses
13. Tables, Listings, Figures
14. Quality Control
15. References

---

## 2. ADaM Dataset Design

### 2.1 ADSL - Subject-Level Analysis Dataset
One record per subject.

### 2.2 ADENDO - Endocrine Longitudinal Dataset
One record per endocrine assessment per subject.

### 2.3 ADIMG - Imaging Analysis Dataset
One record per MRI per subject.

### 2.4 ADRAD - Radiosurgery Parameter Dataset
One record per GKS per subject.

### 2.5 ADPIT - Pituitary Function Dataset
One record per axis per assessment per subject.

### 2.6 ADAE - Safety Dataset
One record per adverse event per subject.

### 2.7 ADINT - Subsequent Intervention Dataset
One record per intervention per subject.

### 2.8 ADTTE - Time-to-Event Dataset
One record per endpoint per subject.

---

## 3. Key Derivation Rules

### 3.1 Baseline
- Closest value before index GKS within 90 days (prefer) or 180 days (max)

### 3.2 IGF-1 Index
- IGF1I = IGF1 / ULN

### 3.3 Early vs Delayed GKS
- EARLYGKS_FL = Y if SURG2GKS_MOS <= 12

### 3.4 Durable Remission
- First: IGF1I <= 1, off meds, OGTT < 0.4
- Durable: No recurrence until last follow-up

---

## 4. Must-Lock 10 Fields

1. GKS date
2. Last surgery date
3. Baseline IGF-1
4. Baseline ULN
5. Baseline GH
6. Knosp grade
7. Residual tumor volume
8. Plan type
9. Medication hold status
10. Post-GKS remission/recurrence/hypopituitarism dates

---

## 5. Key Message

Lock these 6 things first:
- index date
- baseline window
- remission definition
- progression definition
- medication hold definition
- plan type definition

Once locked, traditional stats and ML can run smoothly.

---

*Created: 2026-03-21*
