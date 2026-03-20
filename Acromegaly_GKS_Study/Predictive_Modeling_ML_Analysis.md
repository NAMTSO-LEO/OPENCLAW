# Machine Learning and Deep Learning Analysis

## English Version

---

## 1. Overview

In addition to conventional regression-based analyses, this study will develop a **multimodal predictive modeling framework** to estimate:

1. **Durable endocrine remission**
2. **Time to endocrine remission**
3. **Biochemical recurrence**
4. **New hypopituitarism**
5. **Need for salvage treatment**

Candidate predictors will include demographic, endocrine, surgical, radiographic, and dosimetric variables.

---

## 2. Model Hierarchy

### Primary: Traditional Statistical Models

> **Conventional models, including penalized logistic regression and penalized Cox regression, will serve as the primary interpretable models.**

| Model | Application |
|-------|-------------|
| Cox proportional hazards | Time-to-event outcomes |
| Logistic regression | Binary outcomes |
| LASSO/Elastic Net | Variable selection & shrinkage |

### Secondary: Machine Learning

Machine learning approaches will be evaluated as **secondary predictive models** to capture nonlinear associations and higher-order interactions:

| Algorithm | Application |
|------------|-------------|
| Random Forest | Binary outcomes |
| Gradient Boosting | Binary/survival |
| XGBoost | Binary/survival |
| Support Vector Machines | Binary outcomes |
| Random Survival Forests | Survival outcomes |

### Exploratory: Deep Learning

> If sample size and event counts are sufficient, **deep learning–based survival models such as DeepSurv or DeepHit** may be explored for time-to-event outcomes.

---

## 3. Multimodal Exploratory Analysis

> For centers with sufficiently standardized imaging and radiosurgical planning data, exploratory multimodal models integrating clinical variables, MRI-derived features, and dosimetric parameters may also be developed.

> Radiomics- or convolutional neural network–based analyses may be considered in a subset of patients with high-quality imaging data.

---

## 4. Data Preprocessing

Model development will incorporate:

| Step | Method |
|------|--------|
| Missing data | Multiple imputation or model-specific imputation |
| Scaling | Standardization/normalization |
| Categorical encoding | One-hot or ordinal encoding |
| Center harmonization | Fixed effect, random effect, stratified |
| Skewed variables | Winsorization/transformation (GH, IGF-1) |

> **Model complexity will be constrained according to effective sample size and event number to reduce overfitting.**

---

## 5. Validation Strategy

> **Validation will prioritize repeated cross-validation, bootstrap optimism correction, and internal-external validation across contributing centers.**

| Method | Description |
|--------|-------------|
| Repeated K-fold CV | K=5 or 10 |
| Bootstrap | Optimism correction |
| Internal-external | Leave-one-center-out |
| Calibration | Calibration plots |
| Decision curve | Clinical utility |

---

## 6. Model Performance Metrics

### Binary Outcomes

| Metric | Description |
|--------|-------------|
| Discrimination | AUC / C-statistic |
| Calibration | Calibration slope, Brier score |
| Clinical utility | Decision curve analysis |
| Reclassification | NRI |

### Time-to-Event Outcomes

| Metric | Description |
|--------|-------------|
| Discrimination | Harrell's C-index, time-dependent AUC |
| Calibration | Integrated Brier, calibration at 3/5/10 years |
| Clinical utility | Decision curve analysis |

---

## 7. Model Interpretability

> **Model interpretability will be assessed using variable importance measures and SHAP-based explanation methods.**

SHAP is particularly suitable for:
- IGF-1 index
- Knosp grade
- Tumor volume
- Interval from surgery to GKS
- BED
- Medication hold

---

## 8. Dynamic Prediction Modeling

> **Dynamic prediction modeling using landmark analysis or joint modeling may be performed to update individualized remission probabilities over time as serial endocrine follow-up data become available.**

This approach is especially suitable for:
- Gradual remission over time
- Dynamic IGF-1 changes
- Long follow-up duration
- Nonlinear progression patterns

---

## 9. Model Translation

> **The final predictive model may be translated into a clinically usable nomogram, web-based calculator, or risk stratification tool, depending on model performance and external validity.**

---

## 10. Sample Size Constraint

> **Machine learning and deep learning analyses will be considered exploratory and will only be pursued if sample size, event number, and data completeness are sufficient to support robust model training and validation. To reduce overfitting, model complexity will be constrained according to the effective sample size and number of outcome events.**

---

## 11. Outcome Modeling Specification

| Outcome | Modeling Approach |
|---------|-------------------|
| Durable remission | Time-to-event (Cox) |
| Time to remission | Time-to-event (Cox) |
| Biochemical recurrence | Time-to-event (Cox) |
| New hypopituitarism | Binary / Time-to-event |
| Salvage treatment | Binary (Logistic) |

---

## 12. Candidate Predictor Variables

| Category | Variables |
|----------|-----------|
| Demographics | Age, sex |
| Endocrine | IGF-1 index, baseline GH, OGTT nadir GH |
| Tumor | Tumor volume, Knosp grade |
| Surgical | Interval from surgery to GKS, prior surgeries |
| Medication | Peri-radiosurgical medication hold |
| Radiosurgical | Margin dose, max dose, isodose, optic dose, BED, coverage |
| Strategy | Whole-sella vs targeted |

---

## 13. Summary

This study employs a **clinically interpretable statistical modeling framework as the primary analysis**, with machine learning models serving as predictive performance enhancers and deep learning reserved for exploratory analyses.

| Tier | Model Type | Purpose |
|------|------------|---------|
| **Primary** | Cox / Logistic / LASSO | Clinical inference, HR/OR, nomogram |
| **Secondary** | XGBoost, RF, Survival forests | Predictive enhancement |
| **Exploratory** | DeepSurv, Multimodal CNN | Hypothesis-generating |

This approach ensures:
- ✅ IRB compatibility
- ✅ Reviewer acceptance
- ✅ Clinical journal standards compliance
- ✅ Modern AI augmentation

---

*Updated: 2026-03-19*
