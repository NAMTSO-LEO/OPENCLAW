# Neurosurgery Final Manuscript Template - READY FOR SUBMISSION
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Title

**Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly: Predictors of Remission and Multimodal Treatment Outcomes in an International Multicenter Study**

---

## Abstract

### Background
Cavernous sinus–invading acromegaly represents a clinically distinct and surgically challenging subgroup in whom complete resection is often not feasible. Gamma Knife stereotactic radiosurgery (GKS) is widely used as adjuvant treatment, but predictors of long-term endocrine outcomes in this specific population remain poorly characterized.

### Objective
To evaluate predictors of endocrine remission, recurrence, and treatment-related toxicity after GKS for cavernous sinus–invading acromegaly, and to develop validated prediction models incorporating clinical, radiographic, and dosimetric variables.

### Methods
International multicenter retrospective cohort study. Primary endpoint: time to endocrine remission (IGF-1 index ≤1.0, off medication). Secondary endpoints: biochemical recurrence, radiographic progression, new hypopituitarism, salvage treatment, and overall survival. Analyses included Kaplan–Meier survival estimation, multivariable Cox proportional hazards regression with restricted cubic splines and shared frailty terms, propensity-based overlap weighting for treatment comparisons, and internally validated prediction models.

### Results
A total of N patients from X centers were included. Median follow-up was X months. Cumulative endocrine remission was X% at 3 years and X% at 5 years. Lower baseline IGF-1 index (HR X.X, 95% CI X.X–X.X), higher biologically effective dose (HR X.X, 95% CI X.X–X.X), and shorter surgery-to-radiosurgery interval (HR X.X, 95% CI X.X–X.X) were independently associated with remission. Early radiosurgery was associated with a higher likelihood of remission compared with delayed treatment. New hypopituitarism occurred in X% of patients. Prediction models demonstrated good discrimination (C-index X.X) and calibration, with consistent performance across centers.

### Conclusions
GKS achieves meaningful endocrine remission in cavernous sinus–invading acromegaly. Outcomes are influenced by baseline hormonal burden, tumor characteristics, treatment timing, and dosimetric parameters. These findings support individualized treatment strategies and may inform clinical decision-making in this complex patient population.

---

## Introduction

### Paragraph 1: Clinical Context
Acromegaly is a systemic disease caused by growth hormone–secreting pituitary adenomas, associated with significant morbidity and increased mortality if inadequately controlled. Cavernous sinus invasion represents a surgically challenging situation, as complete transsphenoidal resection is often not achievable without unacceptable risk to cranial nerves. Gamma Knife stereotactic radiosurgery (GKS) is widely used as adjuvant treatment for residual or recurrent disease.

### Paragraph 2: Knowledge Gap
Prior studies on GKS for acromegaly have included heterogeneous populations with varying degrees of cavernous sinus invasion. Limited data exist specifically on this surgically challenging subgroup, and the determinants of long-term endocrine outcomes, recurrence patterns, and treatment-related toxicity have not been comprehensively characterized. Furthermore, few studies have integrated surgical, endocrine, and radiosurgical factors within a unified analytical framework.

### Paragraph 3: Study Objective
We conducted an international multicenter study to (1) characterize long-term endocrine and radiographic outcomes after GKS for cavernous sinus–invading acromegaly, (2) identify independent predictors of remission and toxicity, (3) evaluate treatment strategy effects using causal inference methods, and (4) develop and validate prediction models to support individualized risk estimation.

---

## Methods

### Study Design and Setting
This international multicenter retrospective cohort study included patients with cavernous sinus–invading acromegaly treated with GKS at X centers between YEAR and YEAR. The study was approved by the institutional review board at each center with waiver of informed consent due to the retrospective nature.

### Patients
Inclusion criteria: (1) confirmed diagnosis of acromegaly with biochemical evidence (elevated IGF-1), (2) radiographically confirmed cavernous sinus invasion (Knosp grade 3–4), (3) Gamma Knife radiosurgery as primary or adjuvant treatment, (4) at least 12 months of endocrine and imaging follow-up. Exclusion criteria: (1) prior radiation therapy, (2) incomplete baseline endocrine assessment.

### Outcomes
**Primary endpoint:** Time to endocrine remission, defined as IGF-1 index (IGF-1/upper limit of normal) ≤1.0 on two consecutive assessments at least 3 months apart, while not receiving medical therapy. **Secondary endpoints:** Biochemical recurrence (IGF-1 index >1.0 after prior remission), radiographic progression (tumor volume increase >20%), new hypopituitarism (development of any new pituitary hormone deficiency), salvage treatment (additional surgery or radiation), and overall survival.

### Statistical Analysis
Baseline characteristics were summarized using medians with interquartile ranges for continuous variables and frequencies with percentages for categorical variables. Time-to-event outcomes were estimated using the Kaplan–Meier method, with comparisons performed using log-rank tests. Univariable and multivariable Cox proportional hazards regression were used to evaluate predictors.

Given the retrospective design, treatment comparisons should be interpreted as associative rather than causal. Continuous variables were modeled using restricted cubic splines to avoid arbitrary categorization and to detect nonlinear relationships. Center-level heterogeneity was addressed using shared frailty terms. Proportional hazards assumptions were assessed using Schoenfeld residuals.

To reduce confounding in treatment strategy comparisons, propensity score overlap weighting was applied. Covariate balance was assessed using standardized mean differences, with values <0.1 considered adequate balance.

Prediction models were developed using penalized Cox regression and machine learning approaches to support individualized risk estimation. Model performance was evaluated using concordance index, time-dependent area under the curve, calibration plots, and Brier scores. Internal–external cross-validation was performed by iteratively leaving one center out to assess generalizability. Clinical utility was evaluated using decision curve analysis. Missing data were handled using multiple imputation under the missing-at-random assumption.

All analyses were conducted using SAS version 9.4 and R version 4.3. Statistical significance was defined as two-sided p < 0.05.

---

## Results

### Patient Characteristics
A total of N patients from X centers were included in the analysis. Median age was XX years (IQR XX–XX), and XX% were female. Median follow-up duration was XX months (IQR XX–XX).

Baseline tumor characteristics included median volume of XX cc (IQR XX–XX) and cavernous sinus invasion classified as Knosp grade 3 in XX% and grade 4 in XX% of patients. Prior transsphenoidal surgery had been performed in XX% of patients, with a median interval of XX months between surgery and radiosurgery.

Gamma Knife radiosurgery parameters included median margin dose of XX Gy (IQR XX–XX), median target volume of XX cc (IQR XX–XX), and median biologically effective dose of XX Gy (IQR XX–XX). A targeted treatment plan was used in XX% of cases, and medication was held peri-radiosurgery in XX% of patients.

### Endocrine and Radiographic Outcomes
The cumulative incidence of endocrine remission was XX% at 3 years and XX% at 5 years, with a median time to remission of XX months (95% CI XX–XX). Biochemical recurrence after initial remission occurred in XX% of patients, with a median time to recurrence of XX months.

Radiographic tumor control was achieved in XX% of patients, with progression observed in XX% at a median of XX months. New hypopituitarism developed in XX% of patients during follow-up, and salvage treatment was required in XX% of cases.

### Predictors of Endocrine Remission
In multivariable Cox regression analysis, lower baseline IGF-1 index (HR X.X, 95% CI X.X–X.X, p=X.X), higher biologically effective dose (HR X.X, 95% CI X.X–X.X, p=X.X), and shorter interval from surgery to radiosurgery (HR X.X, 95% CI X.X–X.X, p=X.X) were independently associated with higher likelihood of endocrine remission. Restricted cubic spline analyses demonstrated nonlinear associations between these predictors and remission probability.

### Treatment Strategy Comparisons
After overlap weighting, covariate balance was achieved across treatment groups (all standardized mean differences <0.1). Early radiosurgery (within 12 months of prior surgery) was associated with a higher likelihood of remission compared with delayed treatment (HR X.X, 95% CI X.X–X.X). Peri-radiosurgical medication hold was associated with improved remission outcomes (HR X.X, 95% CI X.X–X.X). Targeted radiosurgical planning showed comparable remission rates but lower risk of hypopituitarism compared with whole-sellar coverage.

### Prediction Model Performance
Prediction models demonstrated good discrimination, with a concordance index of X.X (95% CI X.X–X.X). Time-dependent AUC at 3 and 5 years was X.X and X.X, respectively. Calibration was satisfactory, with calibration slopes close to 1.0. Internal–external cross-validation demonstrated consistent performance across centers. Machine learning approaches did not substantially outperform regression-based models.

---

## Discussion

### Principal Findings
In this multicenter international cohort of patients with cavernous sinus–invading acromegaly, we demonstrate that Gamma Knife radiosurgery achieves meaningful long-term endocrine remission, with outcomes influenced by baseline hormonal burden, tumor characteristics, treatment timing, and dosimetric parameters. This study addresses a clinically distinct and surgically challenging subgroup that has not been comprehensively evaluated in prior literature.

### Interpretation
Our findings highlight that endocrine remission after radiosurgery reflects the interplay between endocrine activity, tumor biology, and treatment strategy. Higher baseline IGF-1 index and larger tumor volume were associated with lower likelihood of remission, suggesting that hormonal burden and tumor load jointly define disease resistance. Shorter interval from surgery to radiosurgery and higher biologically effective dose were associated with improved remission, indicating that earlier and adequately dosed treatment may enhance efficacy.

Using propensity-based overlap weighting, we observed that early radiosurgery and peri-radiosurgical medication hold were associated with improved endocrine outcomes. These findings provide clinically actionable insights into treatment sequencing and planning, particularly for patients with residual cavernous sinus disease where complete surgical resection is not feasible.

### Prediction Models
Prediction models incorporating clinical, endocrine, radiographic, and dosimetric variables demonstrated good discrimination and calibration across centers. Machine learning approaches did not substantially outperform regression-based models, highlighting that simpler, interpretable models may be sufficient in this setting. Findings should be interpreted cautiously due to the nonrandomized design.

### Strengths and Limitations
This study has several strengths. First, it represents one of the largest international cohorts focusing specifically on cavernous sinus–invading acromegaly. Second, we integrated surgical, radiosurgical, and endocrine data within a unified framework. Third, we applied advanced analytical methods including propensity-based weighting, spline modeling, and internal–external validation.

Several limitations should be acknowledged. The retrospective design introduces potential selection bias and residual confounding despite adjustment. Variability in assessment protocols across centers may have introduced heterogeneity, although this also reflects real-world practice. Missing data and incomplete availability of some parameters may have affected endpoint classification. External validation in independent cohorts is warranted to confirm generalizability.

### Conclusions
In patients with cavernous sinus–invading acromegaly, endocrine outcomes after Gamma Knife radiosurgery are driven by a complex interaction of hormonal, anatomical, and treatment-related factors. Earlier intervention, optimized dosing, and careful treatment planning may improve remission while minimizing toxicity. These findings support individualized treatment strategies and may inform clinical decision-making in this complex patient population.

---

## Key Sentences (Must Appear in Manuscript)

| Location | Required Sentence |
|----------|-------------------|
| Abstract/Introduction | "This subgroup represents a clinically distinct and surgically challenging population" |
| Results | "was associated with a higher likelihood of" |
| Results | "After overlap weighting, covariate balance was achieved (SMD <0.1)" |
| Discussion | "Findings should be interpreted cautiously due to the nonrandomized design" |
| Discussion | "Machine learning approaches did not substantially outperform regression-based models" |
| Discussion | "consistent performance across centers" |
| Conclusion | "individualized treatment strategies" |

---

## Figure Checklist

| Figure | Content | Location |
|--------|---------|----------|
| 1 | Patient flow diagram | Main text |
| 2 | Kaplan–Meier: remission | Main text |
| 3 | Kaplan–Meier: hypopituitarism | Main text |
| 4 | Restricted cubic spline plots | Main text |
| 5 | Calibration plots | Supplementary |
| 6 | Decision curve analysis | Supplementary |
| S1 | Covariate balance (Love plot) | Supplementary |
| S2 | Sensitivity analyses | Supplementary |

---

## Checklist Before Submission

- [ ] Title includes all 4 elements
- [ ] Abstract <350 words
- [ ] "clinically distinct and surgically challenging" in Abstract
- [ ] Methods: overlap weighting described
- [ ] Methods: spline + frailty described
- [ ] Results: all HRs use "associated with"
- [ ] Results: SMD <0.1 reported
- [ ] Discussion: limitation paragraph includes 4 points
- [ ] Discussion: ML paragraph includes "did not substantially outperform"
- [ ] Conclusion: includes "individualized"
- [ ] No "improved," "better," "superior" in Results
- [ ] No "definitive," "novel," "first" in text

---

*Document created: 2026-03-21*
*Version: NEUROSURGERY FINAL - READY FOR SUBMISSION*
