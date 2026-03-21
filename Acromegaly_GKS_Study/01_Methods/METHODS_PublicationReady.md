# METHODS

## Publication-Ready Version

---

## Study Design and Patient Population

This was an **international, multicenter retrospective cohort study** evaluating outcomes of Gamma Knife radiosurgery (GKS) in patients with **cavernous sinus–invading acromegaly**. Participating centers contributed de-identified data according to local institutional review board approval or exemption.

Eligible patients had a clinical and biochemical diagnosis of acromegaly and radiographic or treatment-based evidence of cavernous sinus invasion, including Knosp grade ≥1, postoperative residual tumor within the cavernous sinus, or radiosurgical targeting of an intracavernous component. Patients were required to have at least 12 months of endocrine follow-up and available post-radiosurgical endocrine and imaging assessments.

Patients without clear cavernous sinus involvement, those with non–growth hormone–secreting lesions, prior fractionated radiotherapy, or inadequate follow-up were excluded.

---

## Data Collection and Variable Definitions

Data collected included **demographic characteristics, endocrine parameters, surgical history, radiographic features, and radiosurgical treatment variables**.

Baseline endocrine variables included insulin-like growth factor 1 (IGF-1), IGF-1 index (IGF-1 normalized to age- and sex-adjusted upper limit of normal), growth hormone (GH), and oral glucose tolerance test (OGTT) nadir GH where available. Hormonal values were log-transformed where appropriate due to skewed distributions.

Tumor-related variables included tumor volume, Knosp grade, cavernous sinus involvement characteristics, and residual tumor location. Radiosurgical parameters included margin dose, maximum dose, isodose line, target coverage, optic apparatus dose, and biologically effective dose (BED) when calculable. Treatment strategy was categorized as targeted cavernous sinus treatment or whole-sellar coverage.

To address inter-center variability, endocrine measures were harmonized using IGF-1 index, and center identifiers were incorporated into downstream analyses.

---

## Outcome Measures

### Primary Outcome

**Durable endocrine remission**, defined as normalization of IGF-1 according to age- and sex-adjusted reference ranges, off medical therapy, with supportive OGTT data where available, and without biochemical recurrence through last follow-up.

### Secondary Outcomes

- Endocrine control on medication
- Time to endocrine remission
- Radiographic tumor control
- Biochemical recurrence
- New hypopituitarism
- Visual toxicity
- Cranial neuropathy
- Need for salvage intervention
- Overall survival

Time-to-event outcomes were measured from the date of index GKS to the occurrence of the event or last follow-up.

---

## Statistical Analysis

**Kaplan–Meier methods** were used to estimate time-to-event outcomes, including time to endocrine remission, recurrence-free survival, progression-free survival, and time to new hypopituitarism. Differences between groups were assessed using **log-rank tests**.

**Cox proportional hazards regression models** were used to evaluate predictors of time-to-event outcomes. **Logistic regression models** were used for binary outcomes. Candidate variables included demographic factors, endocrine markers (IGF-1 index, GH), tumor characteristics (volume, Knosp grade), treatment timing, medication status, and radiosurgical parameters.

**Penalized regression methods**, including least absolute shrinkage and selection operator (LASSO) and elastic net, were applied to improve model stability and perform variable selection. Variables with p < 0.10 in univariable analyses or strong clinical relevance were considered for multivariable models.

Missing data were handled primarily using **complete-case analysis**, with multiple imputation considered when appropriate. Statistical significance was defined as a two-sided p-value < 0.05.

---

## Machine Learning and Deep Learning–Augmented Modeling

To complement conventional regression analyses, **supervised machine learning models** were developed to enhance predictive performance and capture nonlinear relationships. Algorithms evaluated included:

- Random forest
- Gradient boosting machines
- Extreme gradient boosting (XGBoost)
- Support vector machines
- Random survival forests (for time-to-event outcomes)

If sample size and event counts were sufficient, **deep learning–based survival models** (e.g., DeepSurv or DeepHit) were explored to model complex nonlinear associations between predictors and time-dependent outcomes.

Data preprocessing included:
- Imputation of missing values
- Normalization or transformation of continuous variables
- Encoding of categorical variables
- Harmonization of endocrine measurements across centers

---

## Model Development and Validation

Model development employed **resampling-based approaches**. When feasible, the dataset was partitioned into training and testing cohorts; otherwise, **repeated k-fold cross-validation** and **bootstrap resampling** were used.

Given the multicenter design, **internal-external validation** was performed by iteratively training models on all but one center and testing performance on the held-out center to evaluate generalizability.

Model complexity was constrained according to the number of outcome events to reduce overfitting.

---

## Model Performance and Interpretation

Model performance was evaluated in terms of **discrimination**, **calibration**, and **clinical utility**:

| Aspect | Metrics |
|--------|---------|
| Discrimination | AUC, time-dependent AUC, Harrell's C-index |
| Calibration | Calibration plots, Brier scores |
| Clinical utility | Decision curve analysis |

To enhance interpretability, **model-agnostic methods** including variable importance measures and **Shapley additive explanations (SHAP)** were used to quantify the contribution of individual predictors.

---

## Dynamic Prediction Modeling

For patients with longitudinal endocrine follow-up data, **dynamic prediction models** were constructed using **landmark analysis** or **joint modeling approaches**. These models enabled updating of individualized probabilities of remission or recurrence over time based on evolving endocrine status.

---

## Exploratory Multimodal Analysis

In a subset of patients with high-quality imaging and radiosurgical planning data, **exploratory analyses** integrating clinical, radiographic, and dosimetric features were performed. **Radiomics-based** or **convolutional neural network–based** approaches were considered to evaluate whether imaging-derived features improved predictive performance.

---

## Clinical Translation

Where appropriate, predictive models were translated into **clinically interpretable tools** such as **nomograms** or **risk stratification systems** to facilitate individualized decision-making.

---

*Methods section finalized: 2026-03-19*
