# Submission Package - Complete Manuscript
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Complete Manuscript Structure

### Front Matter
- [ ] Title Page (with author affiliations)
- [ ] Abstract (structured, 250-350 words)
- [ ] Keywords (5-7)
- [ ] Running title (<50 characters)

---

### Main Manuscript

#### Abstract
**Background:** Cavernous sinus–invading acromegaly represents a surgically challenging subgroup. We evaluated outcomes, predictors, and prediction models after Gamma Knife radiosurgery.

**Methods:** Multicenter retrospective cohort. Primary endpoint: time to endocrine remission. Secondary: recurrence, progression, hypopituitarism. Analyses: Kaplan–Meier, Cox with splines, overlap weighting, multi-state modeling, IECV.

**Results:** N patients, median follow-up X months. Cumulative remission X% at 3 years, X% at 5 years. Predictors: lower IGF-1 index, higher BED, shorter surgery-to-GKS interval. Prediction model C-index X.

**Conclusions:** GKS achieves durable remission. Earlier intervention and optimized planning improve outcomes. Validated models support individualized decision-making.

---

#### Introduction (2-3 paragraphs)

**Paragraph 1:** Clinical context
- Acromegaly burden
- Cavernous sinus invasion = surgical challenge
- GKS as adjuvant treatment

**Paragraph 2:** Knowledge gap
- Limited data on cavernous sinus subgroup
- Need for outcome predictors
- Role of multimodal integration

**Paragraph 3:** Study objective
- Characterize outcomes
- Identify predictors
- Develop validated prediction models

---

#### Methods (Structured)

##### Study Design & Setting
- International multicenter retrospective
- X centers, YEAR–YEAR
- IRB approval (waiver of consent)

##### Patients
- Inclusion: cavernous sinus invasion, GKS, ≥12 months follow-up
- Exclusion: prior radiation, missing baseline

##### Outcomes
- **Primary:** Time to endocrine remission (IGF-1 index ≤1.0, off medication)
- **Secondary:** Biochemical recurrence, radiographic progression, new hypopituitarism, salvage treatment, OS

##### Statistical Analysis
- Descriptive: median (IQR), n (%)
- Survival: Kaplan–Meier, log-rank
- Regression: Cox with restricted cubic splines, frailty terms
- Confounding: propensity score overlap weighting
- Competing risk: Fine-Gray sensitivity analysis
- Prediction: penalized Cox, RSF, XGBoost
- Validation: internal-external CV by center
- Evaluation: C-index, time-dependent AUC, calibration, DCA
- Missing data: multiple imputation under MAR

##### Software
- SAS 9.4, R 4.3+

---

#### Results

##### Patient Characteristics (Table 1, Figure 1)
- N = 
- Demographics: age, sex
- Tumor: volume, Knosp grade
- Prior surgery: n (%), interval to GKS
- GKS parameters: margin dose, BED, target volume, plan type

##### Outcomes (Figure 2, Table 2)
- Remission: X% at 3y, X% at 5y
- Recurrence: X% after remission
- Progression: X%
- Hypopituitarism: X%
- Salvage: X%

##### Predictors (Table 3, Figure 3)
- Univariable and multivariable HRs with 95% CI
- Spline plots for continuous predictors

##### Treatment Comparisons (Table 4)
- Early vs delayed GKS
- Targeted vs whole-sella
- Medication hold vs no hold
- Balance assessment (SMDs)

##### Multi-State Analysis (Figure 4)
- Transition probabilities over time

##### Prediction Models (Table 5, Figure 5-6)
- Model performance: C-index, AUC, calibration
- IECV results by center
- ML vs regression comparison

---

#### Discussion

##### Principal Findings
- Summarize key results

##### Interpretation
- Comparison with prior literature
- Treatment strategy implications
- Disease trajectory modeling

##### Prediction Models
- Clinical utility
- ML vs traditional

##### Strengths & Limitations
- Be honest but turn limitations into strengths

##### Conclusions
- Clinical take-home message

---

### References
- Vancouver style
- Key prior studies on GKS + acromegaly
- Recent methodology references (TRIPOD, PROBAST)

---

### Supplementary Materials
- Variable definitions (Supplemental Table S1)
- Missing data summary (Supplemental Table S2)
- Additional sensitivity analyses
- Love plot for covariate balance
- Full model coefficients

---

## Figure Plan

| Figure | Content | Type |
|--------|---------|------|
| **1** | Study flow diagram | Flowchart |
| **2** | Kaplan–Meier curves (remission, hypopituitarism) | Survival |
| **3** | Restricted cubic spline plots | Regression |
| **4** | Multi-state model diagram + probabilities | State diagram |
| **5** | Calibration plots (3y, 5y) | Validation |
| **6** | Decision curve analysis | Clinical utility |

---

## Table Plan

| Table | Content |
|-------|---------|
| **1** | Baseline characteristics |
| **2** | Outcome summary |
| **3** | Multivariable Cox regression |
| **4** | Treatment comparisons (weighted) |
| **5** | Prediction model performance |

---

## Submission Versions

### Version A: Neurosurgery
**Title:** Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly: Predictors of Remission and Treatment Outcomes in an International Multicenter Study

**Focus:** Clinical decision-making, treatment strategies, complication rates

**Emphasize:** Surgical challenge, radiosurgery outcomes, hypopituitarism risk

**De-emphasize:** ML complexity (keep one paragraph)

---

### Version B: JCEM
**Title:** Endocrine Outcomes After Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly: A Multicenter Study

**Focus:** IGF-1, biochemical remission, medication effects

**Emphasize:** Endocrine endpoints, hormonal control

**De-emphasize:** Surgical details

---

### Version C: Lancet Digital Health
**Title:** Multimodal Prediction of Endocrine Remission After Radiosurgery for Acromegaly: An International Multicenter Study

**Focus:** Prediction modeling, generalizability, clinical decision support

**Emphasize:** IECV, calibration, DCA, dynamic prediction

---

## Timeline

| Task | Timeline |
|------|----------|
| Finalize data | Week 1 |
| Run final analyses | Week 2 |
| Draft manuscript | Week 3 |
| Internal review | Week 4 |
| Submit to journal | Week 5 |
| First decision | Week 9-13 |
| Revision | Week 14-18 |
| Acceptance | Week 20-24 |

---

## Checklist Before Clicking "Submit"

- [ ] All authors approved
- [ ] Conflicts disclosed
- [ ] Funding declared
- [ ] Ethics statement included
- [ ] Data availability statement
- [ ] Cover letter ready
- [ ] Figures meet resolution requirements
- [ ] References formatted correctly
- [ ] Supplementary complete

---

## Quick Reference: Key Sentences

### Methods
"We used restricted cubic splines to model continuous variables without arbitrary categorization."

"We applied overlap weighting based on propensity scores to reduce confounding in treatment comparisons."

"We performed internal-external cross-validation by iteratively leaving one center out."

### Results
"All standardized mean differences were <0.1 after overlap weighting."

"Machine learning models showed similar discrimination but did not substantially improve calibration."

### Discussion
"Findings should be interpreted as hypothesis-generating rather than causal."

"Treatment allocation was not randomized; residual confounding cannot be excluded."

"Longer follow-up may further refine outcome estimates."

---

*Document created: 2026-03-21*
*Version: Complete Submission Package*
