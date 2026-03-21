# Statistical Analysis Plan - Top-Tier Journal Version
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## 1. Study Objectives - Three-Tier Framework

### 1.1 Primary Objectives

**Tier 1: Clinical Inference**
- Identify factors associated with endocrine remission, recurrence, and hypopituitarism
- Compare treatment strategies: early vs delayed GKS, targeted vs whole-sella, medication hold vs no hold

**Tier 2: Individualized Prediction**
- Develop prediction models for 3-year and 5-year remission probability
- Develop prediction model for 5-year hypopituitarism risk

**Tier 3: Clinical Decision Support**
- Evaluate clinical utility of prediction models via decision curve analysis
- Assess whether models provide net benefit over clinical经验

---

## 2. Study Design

- International multicenter retrospective cohort
- Patients with cavernous sinus-invading acromegaly undergoing Gamma Knife radiosurgery
- Primary endpoint: Time to first endocrine remission
- Secondary endpoints: Recurrence, progression, hypopituitarism, salvage, OS

---

## 3. Analysis Populations

### 3.1 Full Analysis Set (FAS)
All eligible patients meeting inclusion/exclusion criteria

### 3.2 Endocrine Evaluable Set (EES)
Patients with baseline endocrine data and at least one post-GKS endocrine assessment

### 3.3 Imaging Evaluable Set (IES)
Patients with at least one post-GKS MRI assessment

### 3.4 Safety Analysis Set (SAS)
All patients who underwent eligible index GKS with post-treatment safety follow-up

---

## 4. Statistical Methods

### 4.1 Descriptive Analysis

#### 4.1.1 Baseline Characteristics
- Overall and by treatment strategy subgroup
- Continuous variables: median (Q1, Q3), mean (SD)
- Categorical variables: n (%)
- By center heterogeneity assessment

#### 4.1.2 Outcome Summary
- Remission rates at 1, 3, 5 years
- Recurrence rates among those achieving remission
- Tumor control rates
- Hypopituitarism incidence
- Salvage treatment rates

---

### 4.2 Primary Analysis: Time-to-Event

#### 4.2.1 Kaplan-Meier Analysis
- Kaplan-Meier curves for each endpoint
- Stratified by: plan type, medication hold, early/delayed GKS, Knosp grade
- Log-rank test for group comparisons

#### 4.2.2 Cox Proportional Hazards Model

**Model 1: Time to First Endocrine Remission**

Covariates:
- Age (continuous)
- Sex
- Baseline IGF-1 index (continuous)
- Baseline GH
- Tumor volume
- Knosp grade (1-2 vs 3-4)
- Surgery-to-GKS interval (continuous)
- Plan type (targeted vs whole-sella)
- Medication hold status
- Margin dose (continuous)
- BED (continuous)
- Center (frailty term)

**Non-linearity handling:**
- Restricted cubic splines for continuous variables (IGF-1i, tumor volume, interval, dose, BED)
- Minimum 3 knots, selection by AIC

**Center handling:**
- Frailty Cox model with random center effect
- Or: robust sandwich estimator clustered by center

#### 4.2.3 Penalized Cox Regression
- LASSO penalty for variable selection
- Elastic Net for correlated predictors
- Bootstrap-based shrinkage factor for optimism correction

#### 4.2.4 Competing Risks Analysis
- Fine-Gray subdistribution hazard model for:
  - Recurrence (competing: death without recurrence)
  - Salvage (competing: death, progression)

#### 4.2.5 Multi-State Model (Exploratory)
- States: uncontrolled → remission → recurrence → salvage
- Transition probabilities and hazards

---

### 4.3 Treatment Strategy Comparisons

#### 4.3.1 Causal Inference Framework

**Comparison 1: Medication Hold vs No Hold**
**Comparison 2: Targeted vs Whole-Sella**
**Comparison 3: Early vs Delayed GKS**

**Primary Method: Overlap Weighting**
- Stabilized weights based on propensity scores
- Balance assessment: standardized mean differences < 0.1
- Weighted Kaplan-Meier curves
- Weighted Cox regression

**Secondary Method: IPTW**
- Inverse probability of treatment weighting
- Weight trimming at 95th percentile

**Sensitivity: Matching**
- Nearest neighbor matching (1:1 or 1:2)
- Caliper = 0.1 SD of logit

**Propensity Score Variables:**
- Age, sex
- Baseline IGF-1i, GH
- Tumor volume, Knosp grade
- Prior surgery
- Center

---

### 4.4 Safety Analysis

#### 4.4.1 Hypopituitarism
- Time to new hypopituitarism by axis
- Competing risks: death
- Subgroup by dose, BED, location

#### 4.4.2 Visual/ Cranial Nerve Toxicity
- Cumulative incidence
- Time-to-event analysis

---

## 5. Prediction Model Development

### 5.1 Model Specifications

#### 5.1.1 Model 1: Baseline Clinical Model
- Age, sex
- Knosp grade
- Prior surgery
- Surgery-to-GKS interval

#### 5.1.2 Model 2: Clinical + Endocrine
- Model 1 + Baseline IGF-1i, GH, OGTT

#### 5.1.3 Model 3: Clinical + Endocrine + Imaging
- Model 2 + Tumor volume, residual location

#### 5.1.4 Model 4: Full Model
- Model 3 + Treatment variables (plan type, margin dose, BED, medication hold)

#### 5.1.5 Model 5: Penalized Cox
- LASSO-selected variables from full model

---

### 5.2 Algorithm Specifications

| Model | Type | Package |
|-------|------|---------|
| Logistic Regression | Baseline | stats::glm |
| Penalized Logistic | LASSO/Elastic Net | glmnet |
| Cox PH | Baseline | survival::coxph |
| Penalized Cox | LASSO | glmnet |
| Random Survival Forest | ML | randomForestSRC |
| Gradient Boosting | ML | xgboost |

---

### 5.3 Validation Strategy

#### 5.3.1 Internal Validation
- Bootstrap optimism correction (200 iterations)
- Repeated 5-fold CV (10 repeats)

#### 5.3.2 External Validation
- **Internal-External Cross-Validation (IECV)**
- Leave-one-center-out cross-validation
- Pooled performance metrics with heterogeneity assessment

---

### 5.4 Performance Metrics

#### 5.4.1 Discrimination
- C-index (time-to-event)
- Time-dependent AUC at 3y and 5y

#### 5.4.2 Calibration
- Calibration-in-the-large
- Calibration slope
- Observed vs expected plot at 3y and 5y
- Calibration curves with smooth fit

#### 5.4.3 Overall Accuracy
- Brier score
- Integrated Brier score

#### 5.4.4 Clinical Utility
- Decision curve analysis (DCA)
- Net benefit at threshold probabilities 10-50%

---

### 5.5 Interpretability

#### 5.5.1 Variable Importance
- Partial dependence plots
- Accumulated local effects (ALE)

#### 5.5.2 SHAP Analysis
- SHAP summary plots for tree-based models
- SHAP dependence plots for key variables

#### 5.5.3 Nomogram
- For clinically interpretable risk prediction

---

## 6. Missing Data Handling

### 6.1 Missingness Assessment
- Missing data patterns by variable
- Missing by center
- Outcome-related missingness assessment

### 6.2 Imputation Strategy
- Multiple imputation by chained equations (MICE)
- 20-50 imputed datasets
- Imputation model includes:
  - All baseline covariates
  - Treatment variables
  - Center
  - Nelson-Aalen cumulative hazard for survival outcomes

### 6.3 Sensitivity Analyses
- Complete-case analysis
- Worst-case imputation
- Pattern-mixture models

---

## 7. Sensitivity Analyses

### 7.1 Alternative Definitions
- Remission: stricter (IGF-1i < 0.8) vs standard
- Early GKS: 6 months vs 12 months vs 24 months cutoff
- Progression: >15% vs >20% volume change

### 7.2 Subgroup Analyses
- By Knosp grade (1-2 vs 3-4)
- By primary vs adjuvant GKS
- By center volume

### 7.3 Robustness Checks
- Excluding outliers
- Excluding centers with <10 patients
- Excluding missing BED

---

## 8. Sample Size Considerations

### 8.1 Power Analysis
- For Cox regression: minimum 10 events per predictor
- For ML: minimum 100 events for stable prediction
- Report effective sample size and event numbers

### 8.2 Reporting
- Total N
- Number of events per endpoint
- Events per variable (EPV)

---

## 9. Software

- SAS v9.4 or later
- R v4.3 or later
- Python 3.9+ (for ML models if needed)

---

## 10. Reporting Standards

### 10.1 TRIPOD+AI Alignment
- Transparent reporting of individual prognostic or diagnostic multivariable prediction models
- AI/ML supplement section for model development and validation

### 10.2 PROBAST+AI Alignment
- Risk of bias assessment using PROBAST
- Applicability assessment by domain

### 10.3 CONSORT Diagram
- Patient flow from eligibility to analysis

### 10.4 Tables and Figures

**Table 1:** Baseline characteristics by treatment group

**Table 2:** Outcome summary by treatment group

**Table 3:** Univariable and multivariable Cox models

**Table 4:** Weighted treatment comparisons

**Table 5:** Prediction model performance metrics

**Figure 1:** Kaplan-Meier curves by treatment strategy

**Figure 2:** Forest plot of hazard ratios

**Figure 3:** Calibration plots at 3y and 5y

**Figure 4:** Decision curve analysis

**Figure 5:** SHAP variable importance

---

## 11. Key Subgroup Analyses

- Knosp 1-2 vs 3-4
- Primary vs adjuvant GKS
- Targeted vs whole-sella
- Medication hold groups
- Low vs high IGF-1i
- Low vs high BED
- By center

---

## 12. Endpoint Definitions

### 12.1 Primary Endpoint
**Time to First Endocrine Remission (TTRREM)**
- Event: First date meeting all:
  - IGF-1 index ≤ 1.0
  - Off GH/IGF-1 lowering medication
  - OGTT nadir GH < 0.4 ng/mL if available
- Censoring: Last endocrine assessment date

### 12.2 Secondary Endpoints

**Biochemical Recurrence (TTRREC)**
- After prior remission: IGF-1i > 1.0 or medication restart for relapse

**Radiographic Progression (TTPROG)**
- Volume increase >20% from nadir/baseline or MRI progression

**New Hypopituitarism (TTHYPO)**
- New deficit in axis normal at baseline

**Salvage Intervention (TTSALV)**
- Repeat surgery, repeat SRS, RT, or medication escalation

**Overall Survival (OS)**
- Death from any cause

---

## 13. Statistical Analysis Plan Summary

| Analysis | Method | Primary/Secondary |
|----------|--------|-------------------|
| Descriptive | N (%), median (Q1,Q3) | Descriptive |
| KM Survival | Kaplan-Meier | Primary |
| Cox Regression | PH assumption + spline | Primary |
| Penalized Cox | LASSO/Elastic Net | Secondary |
| Frailty Cox | Random center effect | Secondary |
| Competing Risks | Fine-Gray | Secondary |
| Treatment Comparison | Overlap weighting | Primary |
| Treatment Comparison | IPTW | Secondary |
| Prediction: Logistic | Baseline + penalized | Secondary |
| Prediction: Survival | Penalized Cox, RSF | Secondary |
| Prediction: ML | XGBoost | Secondary |
| Validation | Bootstrap + IECV | Required |
| Calibration | Slope, plot, O/E | Required |
| DCA | Net benefit curves | Required |
| Interpretability | SHAP, PDP | Required |

---

## 14. Three-Paper Strategy

### Paper 1: Clinical Outcomes (Neurosurgery/JNS)
- Cohort description
- KM/Cox analyses
- Treatment comparisons
- Toxicity analysis

### Paper 2: Prediction Model Development (Lancet Digital Health/JCEM)
- Model development
- IECV validation
- Calibration + DCA
- Web calculator

### Paper 3: Methodology (Statistical journal)
- Comparison of methods
- IECV framework
- Generalizability assessment

---

## 15. Key Selling Points

1. **Rare disease subgroup**: Cavernous sinus-invading acromegaly
2. **Truly multimodal**: Surgery + GKS + Endocrinology + Imaging
3. **Dual objectives**: Efficacy + Safety
4. **Methodological completeness**:
   - Causal comparison (overlap weighting)
   - Survival modeling (spline + frailty)
   - Prediction (traditional + ML)
   - IECV validation
   - Calibration + DCA
5. **TRIPOD+AI / PROBAST+AI aligned**

---

*Document created: 2026-03-21*
*Version: Top-Tier Journal SAP*
