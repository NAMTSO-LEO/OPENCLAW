# Manuscript Results Section - High-Impact Template
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Patient Characteristics

A total of N patients from X centers were included in the analysis. The median age was [XX] years (IQR [XX–XX]), and [XX]% were female. The median follow-up duration was [XX] months (IQR [XX–XX]).

At baseline, the median IGF-1 index was [XX] (IQR [XX–XX]), and the median tumor volume was [XX] cc (IQR [XX–XX]). Cavernous sinus invasion was classified as Knosp grade 3–4 in [XX]% of patients.

Prior transsphenoidal surgery was performed in [XX]% of patients, with a median interval of [XX] months between surgery and radiosurgery. Gamma Knife radiosurgery was delivered with a median margin dose of [XX] Gy and median target volume of [XX] cc. A targeted treatment plan was used in [XX]%, and medication was held peri-radiosurgery in [XX]% of cases.

---

## Endocrine and Radiographic Outcomes

### Remission

The cumulative incidence of endocrine remission was [XX]% at 3 years and [XX]% at 5 years. The median time to remission was [XX] months (95% CI [XX–XX]).

### Recurrence

Biochemical recurrence occurred in [XX]% of patients after initial remission, with a median time to recurrence of [XX] months.

### Tumor Control

Radiographic tumor control was achieved in [XX]% of patients, with progression observed in [XX]% at a median of [XX] months.

### Hypopituitarism

New hypopituitarism developed in [XX]% of patients during follow-up.

### Salvage Treatment

Salvage treatment was required in [XX]% of cases.

---

## Predictors of Endocrine Remission

In multivariable Cox regression analysis, lower baseline IGF-1 index (HR [XX], 95% CI [XX–XX], p=[XX]), smaller tumor volume (HR [XX], 95% CI [XX–XX], p=[XX]), shorter interval from surgery to radiosurgery (HR [XX], 95% CI [XX–XX], p=[XX]), and higher biologically effective dose (HR [XX], 95% CI [XX–XX], p=[XX]) were independently associated with higher likelihood of endocrine remission.

Restricted cubic spline analyses demonstrated nonlinear associations between IGF-1 index, tumor volume, and remission probability (Figure 2).

---

## Treatment Strategy Comparisons

After overlap weighting, covariate balance was achieved across treatment groups (all standardized mean differences <0.1).

### Early vs Delayed Radiosurgery

Early radiosurgery was associated with a higher probability of endocrine remission compared with delayed treatment (HR [XX], 95% CI [XX–XX], p=[XX]).

### Targeted vs Whole-Sella

Targeted radiosurgery showed comparable remission rates but lower risk of hypopituitarism compared with whole-sellar coverage (HR [XX], 95% CI [XX–XX], p=[XX]).

### Medication Hold

Medication hold during radiosurgery was associated with improved remission rates (HR [XX], 95% CI [XX–XX], p=[XX]).

---

## Multi-State Analysis

Multi-state modeling demonstrated dynamic transitions between disease states following radiosurgery (Figure 3). The probability of transitioning from uncontrolled disease to endocrine remission increased steadily over time, with the highest transition rates observed within the first [XX] months.

Among patients achieving remission, the cumulative probability of subsequent recurrence was [XX]% at 5 years, while the probability of requiring salvage intervention was [XX]%. Transition to hypopituitarism occurred progressively over time, particularly in patients receiving higher radiation doses.

---

## Prediction Model Performance

### Discrimination

Prediction models for endocrine remission and hypopituitarism demonstrated good discrimination, with a concordance index of [XX] (95% CI [XX–XX]). Time-dependent AUC at 3 and 5 years ranged from [XX] to [XX].

### Calibration

Calibration was satisfactory, with calibration slopes close to 1.0 and good agreement between observed and predicted risks (Figure 4). The integrated Brier score was [XX].

### Validation

Internal-external cross-validation demonstrated consistent performance across centers, with minimal heterogeneity in model discrimination and calibration.

### Machine Learning Comparison

Machine learning models (random survival forests and gradient boosting) showed similar or modestly improved discrimination compared with penalized Cox models but did not substantially improve calibration.

---

## Clinical Utility

Decision curve analysis demonstrated that the prediction models provided net clinical benefit across a range of threshold probabilities compared with treat-all or treat-none strategies (Figure 5), supporting their potential utility in guiding individualized treatment decisions.

---

## Suggested Figures

| Figure | Content |
|--------|---------|
| **Figure 1** | Study flow diagram (CONSORT-style) |
| **Figure 2** | Kaplan–Meier curves for remission and hypopituitarism |
| **Figure 3** | Restricted cubic spline plots showing nonlinear effects |
| **Figure 4** | Multi-state model diagram with transition probabilities |
| **Figure 5** | Calibration plots at 3-year and 5-year |
| **Figure 6** | Decision curve analysis |

---

## Suggested Tables

| Table | Content |
|-------|---------|
| **Table 1** | Baseline characteristics by treatment group |
| **Table 2** | Outcome summary by treatment group |
| **Table 3** | Multivariable Cox regression for remission |
| **Table 4** | Multivariable Cox regression for hypopituitarism |
| **Table 5** | Prediction model performance metrics |
| **Table 6** | Internal-external CV results by center |

---

## Key Sentences for Reviewers

Include these critical statements:

1. **Confounding control**: "After overlap weighting, covariate balance was achieved across treatment groups (all SMDs <0.1)."

2. **Nonlinear effects**: "Restricted cubic spline analyses demonstrated nonlinear associations..."

3. **Generalizability**: "Internal-external cross-validation demonstrated consistent performance across centers..."

4. **ML vs Traditional**: "Machine learning models showed similar discrimination but did not substantially improve calibration."

5. **Clinical utility**: "Decision curve analysis demonstrated net clinical benefit..."

---

*Document created: 2026-03-21*
*Version: Manuscript-Ready Results*
