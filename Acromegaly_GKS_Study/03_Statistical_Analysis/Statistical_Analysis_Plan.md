# Statistical Analysis Plan (SAP)

## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## 1. Study Design

- **Type**: International Multicenter Retrospective Study
- **Population**: Patients with cavernous sinus–invading acromegaly treated with Gamma Knife radiosurgery
- **Primary Outcome**: Durable endocrine remission
- **Follow-up**: ≥12 months

---

## 2. Sample Size

- Expected: ~200-400 patients from multiple international centers
- Power: 80% to detect HR >1.5 for primary endpoint

---

## 3. Statistical Methods

### 3.1 Descriptive Statistics

| Variable | Presentation |
|----------|--------------|
| Continuous | Mean ± SD or median (IQR) |
| Categorical | n (%) |
| Missing data | Reported per variable |

### 3.2 Time-to-Event Analysis

- **Kaplan–Meier estimator** for:
  - Time to endocrine remission
  - Durable remission
  - Recurrence-free survival
  - Progression-free survival
  - Time to new hypopituitarism

- **Log-rank test** for comparisons:
  - Early vs. delayed radiosurgery
  - Targeted vs. whole-sella plans
  - Medication hold vs. no hold
  - Low vs. high IGF-1 index
  - Low vs. high dose/BED strata

### 3.3 Regression Models

#### Cox Proportional Hazards

- **Outcomes**: Remission, recurrence, hypopituitarism
- **Candidate predictors**:
  - Age, sex
  - IGF-1 index, baseline GH, OGTT nadir GH
  - Tumor volume, Knosp grade
  - Interval from surgery to GKS
  - Medication hold
  - Whole-sella vs. targeted plan
  - Margin dose, isodose line, BED

- **Model building**: Variables with p < 0.10 univariate or strong biological plausibility enter multivariable models

#### Logistic Regression

- Binary outcomes:
  - New hypopituitarism
  - Visual toxicity
  - Cranial neuropathy
  - Need for salvage treatment

### 3.4 Missing Data

- Primary: Complete-case analysis
- Sensitivity: Multiple imputation if missingness is moderate

---

## 4. Sensitivity Analyses

1. Exclude primary GKS cases
2. Restrict to postoperative residual-only cases
3. Restrict to Knosp grade 3–4 disease
4. Compare whole-sella vs. targeted (matching/IPW)
5. Stricter remission definitions (IGF-1 + GH/OGTT)

---

## 5. Statistical Software

- SAS 9.4 or R
- Two-sided α = 0.05

---

## 6. Reporting Guidelines

- STROBE for observational studies
- TRIPOD for prediction models

---

*SAP created: 2026-03-19*
