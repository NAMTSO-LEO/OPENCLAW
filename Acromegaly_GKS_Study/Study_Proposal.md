# Study Proposal

---

## Title

**Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly: An International Multicenter Retrospective Study**

---

## Investigators

- Zhenye Li
- Bardia Hajikarimloo
- Salem M. Tos
- Yuki Shinya
- Jason P. Sheehan

---

## Background and Research Hypothesis

### Background

Acromegaly is caused by growth hormone–secreting pituitary adenomas and remains associated with substantial cardiovascular, metabolic, musculoskeletal, and neuroendocrine morbidity if not adequately controlled.

Although transsphenoidal surgery is the standard first-line treatment, biochemical remission declines markedly when the tumor invades the cavernous sinus. Cavernous sinus extension substantially increases surgical complexity and operative risk, thereby making gross-total resection significantly more difficult to achieve.

### Gamma Knife Radiosurgery (GKS)

GKS is widely used for persistent, residual, or recurrent acromegaly, particularly when adenomatous remnants are confined to the cavernous sinus.

Existing studies demonstrate:
- Excellent radiographic tumor control
- Slower and more heterogeneous endocrine remission (often over years)
- Various factors influencing outcomes: baseline hormonal burden, timing from surgery, peri-radiosurgical medication management, coverage strategy, and radiosurgical planning variables

### Research Gap

The current literature remains fragmented. Most studies include mixed acromegaly populations rather than a dedicated cohort of cavernous sinus–invading disease.

### Hypothesis

GKS provides high long-term tumor control and clinically meaningful endocrine remission in patients with cavernous sinus–invading acromegaly, but durable remission and toxicity are strongly influenced by:

- Baseline hormonal burden
- Residual cavernous sinus tumor volume and location
- Timing from surgery to radiosurgery
- Peri-radiosurgical medication status
- Radiosurgical planning variables

---

## Study Objectives

### Primary Objectives

1. **Determine rates and predictors of durable endocrine remission** after GKS for cavernous sinus–invading acromegaly

2. **Characterize the timing** of endocrine remission (early vs. late remission)

3. **Evaluate long-term radiographic control**, biochemical recurrence, and need for salvage therapy

4. **Define the incidence and predictors** of hypopituitarism and other radiation-related adverse effects

5. **Study treatment timing, medication hold, and advanced dosimetric variables** (e.g., BED) influence remission and toxicity

### Exploratory Objective

6. **Develop a dynamic prediction model** integrating surgical, radiosurgical, radiographic and biochemical factors for multimodal treatment outcomes in acromegaly

> **Note:** A detailed predictive modeling framework integrating traditional statistical models, machine learning, and deep learning approaches is provided in the supplementary document: `Predictive_Modeling_ML_Analysis.md`

---

## Patient Inclusion Criteria

1. Clinical and biochemical diagnosis of acromegaly before radiosurgery
   - Elevated IGF-1 and/or inadequate GH suppression on OGTT
   - According to local endocrine standards

2. Radiographic evidence of cavernous sinus–invading disease before or at the time of GKS
   - Knosp grade 1-4
   - Postoperative MRI evidence of residual adenoma within cavernous sinus
   - Treatment planning documentation showing targeted intracavernous remnant

3. Treatment with GKS as:
   - Postoperative adjuvant therapy for residual or recurrent acromegaly
   - Primary treatment only when surgery was contraindicated or declined

4. Minimum endocrine follow-up of ≥12 months after index GKS

5. Availability of:
   - At least one post-radiosurgical endocrine evaluation
   - At least one post-radiosurgical imaging evaluation

---

## Patient Exclusion Criteria

1. No convincing evidence of cavernous sinus involvement or targeted intracavernous disease

2. Non–growth hormone–secreting lesions or mixed sellar lesions without sufficient evidence that acromegaly was the primary treated condition

3. Prior fractionated pituitary radiotherapy before the index GKS

4. Prior stereotactic radiosurgery to the same lesion
   - Exception: repeat-radiosurgery subanalysis

5. Inadequate follow-up (<12 months) or absence of sufficient endocrine/imaging data

6. Absence of key baseline endocrine data necessary to classify biochemical outcome

7. Cases where radiosurgical target cannot be categorized as targeted cavernous sinus treatment or whole-sellar coverage strategy

---

## Definitions

| Term | Definition |
|------|------------|
| Cavernous sinus–invading acromegaly | Cases with ≥1 objective radiographic or treatment-based marker of cavernous sinus invasion or targeted intracavernous residual disease |
| IGF-1i | measured IGF-1 divided by age- and sex-adjusted ULN (IGF-1 / ULN) |

---

## Endpoints

### Primary Endpoints

| Endpoint | Definition |
|----------|------------|
| **Durable endocrine remission** | Normalization of IGF-1 (age/sex-adjusted), off GH/IGF-1–lowering medication, with supportive OGTT (GH <0.4 ng/mL), maintained without biochemical recurrence |
| **Endocrine control** | Normalization of IGF-1 (age/sex-adjusted), on GH/IGF-1–lowering medication |
| **Time to endocrine remission** | Interval from index GKS to first documented biochemical remission |
| **Radiographic tumor control** | Stable or decreased adenoma volume on MRI. Progression defined as >20% volumetric enlargement |

### Secondary Endpoints

- Biochemical recurrence after initial remission
- Need for additional intervention (repeat surgery, repeat SRS, fractionated radiotherapy, escalation of medical therapy)
- New hypopituitarism
- Visual toxicity, cranial neuropathy, adverse radiation effects
- Overall survival

### Prespecified Exploratory Endpoints

- Early vs. late remission (primary cutoff: 36 months; sensitivity: 29 months)
- Effect of peri-radiosurgical medication hold on remission
- Effect of dose and planning variables (margin dose, maximum dose, isodose line, optic maximum dose, BED)

---

## Statistical Analysis

### Methods

| Method | Application |
|--------|-------------|
| Kaplan–Meier | Time to endocrine remission, durable remission, recurrence-free survival, progression-free survival, time to new hypopituitarism |
| Log-rank testing | Compare early vs. delayed radiosurgery, targeted vs. whole-sella plans, medication hold vs. no hold, IGF-1 strata, dose/BED strata |
| Cox proportional hazards | Predictors of remission, recurrence, hypopituitarism |
| Logistic regression | Binary outcomes (new hypopituitarism, visual toxicity, cranial neuropathy, salvage treatment) |

### Candidate Variables

- Age, sex
- IGF-1 index, baseline GH, OGTT nadir GH
- Tumor volume, Knosp grade
- Interval from surgery to GKS
- Medication hold
- Whole-sella vs. targeted plan
- Margin dose, isodose line, BED

### Statistical Significance

Two-sided p-value < 0.05

### Sensitivity Analyses

1. Excluding primary GKS cases
2. Restricting to postoperative residual-only cases
3. Restricting to Knosp grade 3–4 disease
4. Comparing whole-sella vs. targeted cohorts (matching or IPW)
5. Applying stricter remission definitions (combined IGF-1 and GH/OGTT criteria)

---

## Expected Clinical Impact

This study is designed to answer:

> Among patients with cavernous sinus–invading acromegaly, **which endocrine, anatomical, timing, and dosimetric factors predict durable remission without excessive toxicity after Gamma Knife radiosurgery?**

### Potential Contributions

- Refine patient selection for adjuvant radiosurgery
- Guide timing of radiosurgery
- Optimize peri-radiosurgical medication management
- Provide guidance for surgical decision-making in acromegaly management

---

## Selected References

1. Kim EH, et al. Postoperative Gamma Knife radiosurgery for cavernous sinus–invading growth hormone–secreting pituitary adenomas. *World Neurosurg*. 2018.

2. Lee CC, et al. Stereotactic radiosurgery for acromegaly. *J Clin Endocrinol Metab*. 2014.

3. Ding D, et al. Stereotactic radiosurgery for acromegaly: an international multicenter retrospective cohort study. *Neurosurgery*. 2019.

4. Patibandla MR, et al. Factors affecting early versus late remission in acromegaly following stereotactic radiosurgery. *J Neurooncol*. 2018.

5. Shepard MJ, et al. Whole sella vs targeted stereotactic radiosurgery for acromegaly: a multicenter matched cohort study. 2020.

6. Xu Z, et al. Hypopituitarism after Gamma Knife radiosurgery for pituitary adenomas: a multicenter, international study. 2020.

7. Graffeo CS, et al. The impact of insulin-like growth factor index and biologic effective dose in acromegaly radiosurgery. 2020.

8. Qian ZR, et al. Role of biologically effective dose for prediction of endocrine remission in acromegaly patients treated with stereotactic radiosurgery. 2023.

9. Yarman S, et al. Endoscopic transsphenoidal approach for acromegaly with remission rates in 401 patients. 2017.

10. Consensus on acromegaly therapeutic outcomes and 2025 update.

---

*Document created: 2026-03-19*
