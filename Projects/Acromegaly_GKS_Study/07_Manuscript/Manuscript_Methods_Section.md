# Manuscript Methods Section - Top-Tier Journal Version
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Statistical Analysis

Baseline characteristics were summarized using medians with interquartile ranges for continuous variables and frequencies with percentages for categorical variables. Comparisons across subgroups were descriptive and not used for inferential purposes.

Time-to-event outcomes, including time to endocrine remission (TTRREM), time to biochemical recurrence (TTRREC), time to radiographic progression (TTPROG), time to new hypopituitarism (TTHYPO), time to salvage intervention (TTSALV), and overall survival (OS), were estimated using the Kaplan–Meier method. Differences between groups were assessed using log-rank tests.

Multivariable Cox proportional hazards models were used to identify predictors of each time-to-event outcome. Continuous variables, including IGF-1 index, tumor volume, time from surgery to radiosurgery, and dosimetric parameters, were modeled using restricted cubic splines to account for potential nonlinearity. Center-level heterogeneity was accounted for using frailty terms. Proportional hazards assumptions were evaluated using Schoenfeld residuals.

To evaluate treatment strategy effects (e.g., early vs delayed radiosurgery, targeted vs whole-sella plans, medication hold vs no hold), overlap weighting based on propensity scores was applied to reduce confounding due to nonrandom treatment allocation. Covariate balance after weighting was assessed using standardized mean differences.

Secondary analyses included competing risk models for outcomes subject to competing events and sensitivity analyses restricted to predefined subgroups.

---

## Prediction Modeling

Prediction models were developed to estimate individual probabilities of endocrine remission and hypopituitarism. Candidate predictors included demographic, endocrine, radiographic, surgical, and radiosurgical variables prespecified based on clinical relevance.

Penalized Cox regression models were used as the primary modeling approach. Machine learning models, including random survival forests and gradient boosting methods, were developed as complementary approaches to capture nonlinear and interaction effects.

Model performance was assessed in terms of discrimination and calibration. Discrimination was evaluated using the concordance index and time-dependent area under the curve. Calibration was assessed using calibration plots and calibration slope. Overall prediction error was quantified using the Brier score.

To evaluate generalizability across centers, internal-external cross-validation was performed by iteratively leaving one center out for validation while training the model on the remaining centers. Model performance was summarized across all iterations.

Clinical utility was assessed using decision curve analysis.

---

## Missing Data

Missing data were handled using multiple imputation under the missing at random assumption. Imputation models included all candidate predictors and outcomes. Imputation was performed within resampling procedures to avoid information leakage.

---

## Statistical Software

All analyses were performed using SAS (version 9.4) and R (version 4.3). A two-sided p-value < 0.05 was considered statistically significant.

---

## Key Reviewer Highlights

| Feature | Why It Matters |
|---------|----------------|
| Restricted cubic splines | Avoids information loss from arbitrary categorization |
| Frailty terms | Accounts for unmeasured center heterogeneity |
| Overlap weighting | Reduces confounding in treatment comparisons |
| Internal-external CV | Evaluates generalizability across centers |
| Calibration plots | Not just discrimination—shows prediction accuracy |
| Decision curve analysis | Evaluates clinical utility beyond statistics |
| Multiple imputation | Handles missing data under MAR assumption |

---

## Alternative Enhanced Version (For Higher-Impact Journals)

### Multi-State Modeling

As an exploratory analysis, we fitted a multi-state model to characterize disease progression through clinical states: uncontrolled disease → endocrine remission → biochemical recurrence → salvage intervention. Transition hazards were estimated using Cox models with shared frailty for center.

### Dynamic Prediction

We developed dynamic prediction models to update individual remission probabilities at landmark time points (6, 12, 24 months post-radiosurgery) using landmarking approaches. Predictions were validated using time-varying AUC.

### Model Comparison

We compared traditional Cox models, penalized Cox, random survival forests, and gradient boosting models using stratified cross-validation. Models were ranked by integrated Brier score and clinical utility metrics.

---

## Results Section Framework

### Suggested Figures

**Figure 1:** Study flow diagram (CONSORT-style)

**Figure 2:** Kaplan–Meier curves for:
- (A) Time to endocrine remission
- (B) Time to biochemical recurrence
- (C) Time to hypopituitarism

**Figure 3:** Forest plot of multivariable Cox model for remission

**Figure 4:** Calibration plots at 3-year and 5-year for:
- (A) Remission prediction model
- (B) Hypopituitarism prediction model

**Figure 5:** Decision curve analysis showing net benefit across threshold probabilities

**Figure 6:** SHAP variable importance plots for prediction models

### Suggested Tables

**Table 1:** Baseline characteristics by treatment strategy

**Table 2:** Outcome summary by treatment group

**Table 3:** Multivariable Cox regression results (remission)

**Table 4:** Multivariable Cox regression results (hypopituitarism)

**Table 5:** Prediction model performance metrics (discrimination, calibration, clinical utility)

**Table 6:** Internal-external cross-validation results by center

---

## Extended Methods for Results (Optional)

### Competing Risk Analysis

For outcomes with competing risks (e.g., recurrence with death as competing event), we fitted Fine-Gray subdistribution hazard models. Cumulative incidence functions were used to estimate event probabilities.

### Sensitivity Analyses

1. **Alternative remission definitions**: IGF-1i < 0.8 (stricter) vs ≤1.0
2. **Alternative time cutoffs**: Early GKS at 6 months vs 12 months vs 24 months
3. **Complete-case analysis**: Excluding patients with missing baseline covariates
4. **Excluding high-volume centers**: Sensitivity to influential centers

### Subgroup Analyses

Predefined subgroup analyses were conducted by:
- Knosp grade (1-2 vs 3-4)
- Primary vs adjuvant radiosurgery
- Baseline IGF-1i (above vs below median)

Heterogeneity across subgroups was assessed using interaction terms in Cox models.

---

## References Alignment

This methods section aligns with reporting guidelines:
- TRIPOD+AI for prediction model development and validation
- PROBAST+AI for risk of bias assessment
- STROBE for observational cohort study
- IMRaD structure for general medical journals

---

*Document created: 2026-03-21*
*Version: Manuscript-Ready*
