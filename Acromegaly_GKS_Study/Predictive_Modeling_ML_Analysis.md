# Statistical Analysis and Predictive Modeling

---

## 1. Conventional Statistical Analysis

Kaplan–Meier methods will be used to estimate time to endocrine remission, durable remission, recurrence-free survival, progression-free survival, and time to new hypopituitarism. Log-rank tests will be used for group comparisons, including early versus delayed radiosurgery, targeted versus whole-sella planning strategies, medication hold versus no hold, low versus high IGF-1 index, and dose/BED strata.

Cox proportional hazards regression models will be used to identify predictors of time-to-event outcomes, including endocrine remission, recurrence, and hypopituitarism. Logistic regression models will be used for binary outcomes such as new hypopituitarism, visual toxicity, cranial neuropathy, and need for salvage treatment. Variables with p < 0.10 in univariable analysis or strong biological plausibility will be included in multivariable models.

To improve model stability and reduce overfitting, penalized regression techniques (LASSO and elastic net) will be applied for variable selection and shrinkage. Complete-case analysis will be primary, with multiple imputation considered if missingness is moderate and compatible with model assumptions. Statistical significance will be defined as a two-sided p-value < 0.05.

---

## 2. Machine Learning and Deep Learning–Augmented Predictive Modeling

In addition to conventional regression-based analyses, a multimodal predictive modeling framework will be developed to estimate clinically relevant outcomes following Gamma Knife radiosurgery (GKS), including durable endocrine remission, time to remission, biochemical recurrence, new hypopituitarism, and need for salvage intervention.

### 2.1 Modeling Strategy

> **Conventional regression models will serve as the primary, clinically interpretable models.** Machine learning algorithms will be implemented as secondary models to enhance predictive performance and capture nonlinear relationships and higher-order interactions. These may include random forest, gradient boosting machines, extreme gradient boosting (XGBoost), support vector machines, and random survival forests for time-to-event outcomes.

If sample size, number of events, and data completeness are sufficient, deep learning–based survival models such as DeepSurv or DeepHit will be explored to model complex nonlinear relationships between predictors and time-dependent outcomes.

### 2.2 Data Processing and Feature Engineering

Data preprocessing will include:

- Handling missing data using multiple imputation or model-specific techniques
- Normalization or standardization of continuous variables
- Transformation of skewed endocrine biomarkers (e.g., GH, IGF-1)
- Encoding of categorical variables
- Harmonization of endocrine measurements across centers using IGF-1 index

> **To account for inter-center variability, center identifiers will be incorporated into the modeling framework, and center-level heterogeneity will be addressed through adjustment or validation strategies.**

### 2.3 Model Development and Validation

Model development will use resampling-based strategies. If sample size permits, data will be divided into training and testing sets; otherwise, repeated k-fold cross-validation and bootstrap resampling will be applied.

> **Given the multicenter design, internal-external validation will be prioritized, whereby models are iteratively trained on all but one center and tested on the held-out center to evaluate generalizability.**

Model complexity will be constrained according to effective sample size and number of outcome events to minimize overfitting.

### 2.4 Model Performance Evaluation

Model performance will be assessed using:

| Aspect | Metrics |
|--------|---------|
| Discrimination | AUC, time-dependent AUC, Harrell's C-index |
| Calibration | Calibration plots, calibration slope, calibration-in-the-large, Brier score |
| Clinical utility | Decision curve analysis |

For survival models, integrated Brier score and time-dependent calibration at clinically relevant time points will also be evaluated.

### 2.5 Model Interpretability

> **To enhance interpretability, model-agnostic explanation methods will be used, including variable importance measures, Shapley additive explanations (SHAP), and partial dependence plots, to quantify the contribution and direction of key predictors.**

Key predictors for SHAP analysis include:
- IGF-1 index
- Knosp grade
- Tumor volume
- Interval from surgery to GKS
- BED
- Medication hold status

### 2.6 Dynamic Prediction Modeling

> If longitudinal endocrine follow-up data are available, **dynamic prediction models will be constructed using landmark analysis or joint modeling approaches to update individualized risk estimates over time.**

### 2.7 Exploratory Multimodal Modeling

In centers with high-quality imaging and radiosurgical planning data, exploratory multimodal models integrating clinical, radiographic, and dosimetric features may be developed. Radiomics- or convolutional neural network–based analyses will be considered in selected subsets with sufficient data consistency.

### 2.8 Clinical Translation

> If model performance and generalizability are adequate, **the final model may be translated into a clinically applicable tool, such as a nomogram, web-based calculator, or risk stratification system.**

---

## 3. Sample Size Constraint

> **Machine learning and deep learning analyses will be considered exploratory and will only be pursued if sample size, event number, and data completeness are sufficient to support robust model training and validation. To reduce overfitting, model complexity will be constrained according to the effective sample size and number of outcome events.**

---

## 4. Reporting Guidelines

This analysis will follow:

- **TRIPOD** for prediction model reporting
- **STROBE** for observational study elements
- **ML-specific**: Algorithm, tuning, hyperparameters, feature importance

---

## 5. Summary: Model Hierarchy

| Tier | Model Type | Role | Validation |
|------|------------|------|------------|
| **Primary** | Cox / Logistic / LASSO | Clinical inference, HR/OR, nomogram | Bootstrap + CV |
| **Secondary** | XGBoost, RF, Survival forests | Predictive enhancement | CV + bootstrap |
| **Exploratory** | DeepSurv, Multimodal CNN | Hypothesis-generating | Limited by n |

---

*Section finalized: 2026-03-19*
