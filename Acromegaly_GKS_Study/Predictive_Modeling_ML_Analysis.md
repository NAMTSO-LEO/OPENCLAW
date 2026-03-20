# Predictive Modeling and Machine Learning Analysis

*(Enhanced Section for Study Proposal)*

---

## 1. Overall Modeling Strategy

A multimodal prediction framework will be developed to estimate:

1. **Durable endocrine remission**
2. **Time to endocrine remission**
3. **Risk of biochemical recurrence**
4. **Risk of new hypopituitarism**
5. **Need for salvage intervention**

The modeling framework will incorporate clinical, biochemical, surgical, radiographic, and radiosurgical dosimetric features. **Conventional regression-based models will serve as the primary clinically interpretable models**, while machine learning and deep learning approaches will be used as secondary or exploratory models to improve predictive performance and capture nonlinear interactions.

---

## 2. Traditional Statistical Models (Primary)

These will remain the primary inferential models:

| Model Type | Application |
|------------|-------------|
| Cox proportional hazards | Time-to-event endpoints (remission, recurrence, hypopituitarism) |
| Logistic regression | Binary endpoints (remission yes/no, toxicity) |
| Competing-risk models | If non-negligible death or alternative interventions |
| LASSO/Elastic Net | Variable selection and shrinkage |

### Why This Matters

Because the study aims not only to "predict" but also to answer **"which factors are associated?"**

Reviewers value:
- Interpretability
- HR / OR estimates
- Independent effects of clinical variables
- Ability to generate nomograms / risk scores

**Statistical models must be the primary models.**

---

## 3. Machine Learning and Deep Learning (Exploratory)

> **Machine learning and deep learning analyses will be considered exploratory and will only be pursued if sample size, event number, and data completeness are sufficient to support robust model training and validation. To reduce overfitting, model complexity will be constrained according to the effective sample size and number of outcome events.**

---

## 4. Data Preprocessing

The following preprocessing steps will be applied:

| Step | Method |
|------|--------|
| Missing data | Multiple imputation or model-specific imputation |
| Continuous variables | Standardization / normalization |
| Categorical variables | One-hot or ordinal encoding |
| Skewed biomarkers | Winsorization or transformation (GH, IGF-1) |
| Laboratory harmonization | IGF-1 index and standardized endocrine definitions |
| Center adjustment | Fixed effect, random effect, or stratified validation |

> **To account for between-center heterogeneity, center identifier will be incorporated into the modeling pipeline, and center-level internal-external cross-validation will be performed whenever feasible.**

---

## 5. Traditional Statistical Models (Primary)

These will remain the primary inferential models:

| Model Type | Application |
|------------|-------------|
| Cox proportional hazards | Time-to-event endpoints |
| Logistic regression | Binary endpoints |
| Competing-risk models | Competing risks |
| LASSO/Elastic Net | Variable selection |

---

## 6. Machine Learning Models (Secondary / Predictive Enhancement)

For predictive performance improvement:

### For Binary Outcomes

| Algorithm | Description |
|-----------|-------------|
| Random Forest | Ensemble tree-based |
| XGBoost | Gradient boosting |
| LightGBM / CatBoost | Advanced boosting |
| SVM | Support Vector Machine |
| Elastic Net Logistic | Regularized logistic |

### For Time-to-Event Outcomes

| Algorithm | Description |
|-----------|-------------|
| Random Survival Forest | Ensemble survival trees |
| Gradient Boosting Survival | Boosting for survival |
| Survival XGBoost | XGBoost for survival |
| Penalized Cox | Regularized Cox |
| DeepSurv | Deep learning survival (if n permits) |

---

## 7. Deep Learning (Exploratory)

### A. Survival Deep Learning

> Deep learning–based survival models such as DeepSurv or DeepHit may be explored to model nonlinear relationships between baseline characteristics and time-to-remission or time-to-toxicity outcomes.

**Suitable endpoints:** time to remission, recurrence, hypopituitarism

### B. Multimodal Fusion

> If imaging and radiosurgical planning data are available in standardized digital format, multimodal deep learning models integrating clinical variables, MRI-derived imaging features, and dosimetric parameters may be explored.

### C. MRI Radiomics / CNN (Exploratory)

> In centers with available high-quality pre-radiosurgical MRI data, radiomics- or CNN-based exploratory analyses may be performed to assess imaging signatures beyond conventional clinical models.

---

## 8. Model Development and Validation

### Split Strategy

> The dataset will be randomly split into training and test cohorts only if sample size is sufficiently large; otherwise, repeated k-fold cross-validation or bootstrap resampling will be used.

### Internal-External Validation (Priority)

> **Given the multicenter design, internal-external validation will be prioritized, whereby models are iteratively trained on all but one center and tested on the held-out center. This will assess transportability across institutions.**

### Validation Methods

| Method | Description |
|--------|-------------|
| Repeated 5-fold CV | Cross-validation |
| Bootstrap resampling | Optimism correction |
| Leave-one-center-out | Internal-external validation |
| Calibration assessment | Calibration plots |
| Decision curve analysis | Clinical utility |

---

## 9. Model Performance Metrics

### Binary Outcomes

| Metric | Description |
|--------|-------------|
| Discrimination | AUC / C-statistic |
| Calibration | Calibration slope, intercept, Brier score |
| Clinical utility | Decision curve analysis |
| Reclassification | NRI (when comparing models) |

### Time-to-Event Outcomes

| Metric | Description |
|--------|-------------|
| Discrimination | Harrell's C-index, time-dependent AUC |
| Calibration | Integrated Brier score, calibration at 3/5/10 years |
| Clinical utility | Decision curve analysis |

---

## 10. Model Interpretability

> **To improve clinical interpretability, variable importance measures, partial dependence plots, SHAP (Shapley additive explanations), and accumulated local effect plots may be used to characterize the contribution and directionality of key predictors across machine learning models.**

SHAP is particularly suitable for interpreting:
- IGF-1 index
- Knosp grade
- Tumor volume
- Interval from surgery to GKS
- BED
- Medication hold

---

## 11. Dynamic Prediction Models

> **Dynamic prediction models may be constructed using landmark analysis or joint modeling approaches to update individualized remission probabilities over time as serial endocrine measurements and interval imaging become available.**

This approach is especially suitable for:
- Gradual remission over time
- Dynamic IGF-1 changes
- Long follow-up duration
- Nonlinear progression patterns

---

## 12. Integration Summary

| Tier | Model Type | Role | Validation |
|------|------------|------|------------|
| **Primary** | Cox / Logistic | Clinical inference, HR/OR, nomogram | Bootstrap + CV |
| **Secondary** | XGBoost, RF, Survival forests | Predictive enhancement | CV + bootstrap |
| **Exploratory** | DeepSurv, Multimodal CNN | Novel methods | Limited by n |

---

## 13. Key Message

> This study employs a **clinically interpretable statistical modeling framework as the primary analysis**, with machine learning models serving as predictive performance enhancers and deep learning reserved for exploratory analyses. This approach ensures IRB compatibility, reviewer acceptance, and alignment with clinical journal standards while leveraging modern AI methods to augment predictive capability.

---

## 14. Reporting Guidelines

- **TRIPOD** for prediction models
- **ML-specific**: Algorithm, tuning, hyperparameters, feature importance
- **SHAP values** for tree-based model interpretation
- **Nomograms** for clinically interpretable models

---

*Section added: 2026-03-19*
