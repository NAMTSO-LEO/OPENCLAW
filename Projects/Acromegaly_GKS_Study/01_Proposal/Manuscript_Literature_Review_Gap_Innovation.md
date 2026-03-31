# Literature Review, Gap, and Innovation - Formal Manuscript Section

---

## Literature Review

Stereotactic radiosurgery (SRS), particularly Gamma Knife radiosurgery (GKRS), has emerged as an effective adjuvant treatment for acromegaly, with reported endocrine remission rates ranging from 40% to 60% at 5 years and approaching 60% to 70% at 10 years. Tumor control rates consistently exceed 90% across series. However, the existing literature reveals substantial heterogeneity in patient populations, outcome definitions, and analytical approaches.

Key predictors of endocrine remission have been investigated across multiple studies. Baseline IGF-1 level (or IGF-1 index normalized to age- and sex-adjusted reference ranges) represents the most stable biological predictor, with lower pre-treatment values consistently associated with higher remission rates. The International Gamma Knife Research Foundation (IGKRF) multicenter study of 371 patients identified temporary cessation of IGF-1-lowering medications prior to SRS as an independent predictor of durable remission (HR=2.49, p=0.01), suggesting that treatment state critically modulates radiosensitivity. Radiologically, cavernous sinus invasion has been associated with inferior outcomes in several series, though dedicated analyses of this surgically challenging subgroup are lacking.

Recent studies have advanced our understanding of dosimetric predictors. The Mayo Clinic series demonstrated that biologically effective dose (BED), which accounts for treatment time and DNA repair during irradiation, predicts biochemical remission more reliably than physical margin dose alone (HR=2.27 for BED >200 Gy₂.₄₇, p=0.002). Comparative strategy studies, including matched analyses of whole-sella versus targeted SRS planning, have shown similar efficacy but potentially higher toxicity with whole-sella approaches, indicating that anatomical factors primarily modulate safety rather than effectiveness.

The temporal dynamics of SRS outcomes have been characterized across series. Mean time to endocrine remission ranges from 24 to 40 months, with actuarial rates continuing to increase through 10 years of follow-up. Biochemical recurrence after initial remission occurs in approximately 9% of patients, typically within the first 1 to 3 years. New-onset hypopituitarism represents the most common adverse event, affecting 25% to 30% of patients with a median onset of 29 to 50 months—demonstrating distinct temporal trajectories for efficacy and toxicity endpoints.

---

## Gap Analysis

Despite the growing body of literature on GKRS for acromegaly, several critical knowledge gaps remain:

1. **Subgroup-specific data**: No dedicated multicenter study has focused specifically on patients with cavernous sinus-invading pituitary adenomas—the most surgically challenging subgroup with the highest likelihood of requiring adjuvant radiotherapy.

2. **Unified predictive framework**: Previous studies have examined biological factors (IGF-1), dosimetric factors (BED), and treatment state factors (medication hold) in isolation. No single study has integrated all three domains within a coherent analytical framework.

3. **Dynamic outcome modeling**: Existing analyses predominantly employ traditional Kaplan-Meier and Cox proportional hazards methods. The application of multi-state modeling, dynamic prediction, and continuous variable smoothing (e.g., spline regression) remains limited.

4. **Benefit-risk balance**: Most studies report efficacy and toxicity as separate endpoints without explicit joint modeling of time-to-remission versus time-to-hypopituitarism.

---

## Innovation

The present study addresses these gaps through several innovations:

1. **Focused subgroup**: We specifically enroll patients with cavernous sinus-invading or intracavernous residual growth hormone-secreting pituitary adenomas, a clinically distinct population with consistently higher surgical failure rates and greater reliance on adjuvant GKRS.

2. **Unified framework**: We analyze the independent and interactive effects of:
   - **Biology**: Pre-treatment IGF-1 index
   - **Radiation**: Margin dose and calculated BED
   - **Treatment state**: Medication status at time of SRS

3. **Advanced methodology**:
   - Overlap weighting for covariate balance
   - Spline regression for continuous predictors
   - Landmark analysis for early biochemical response
   - Sensitivity analyses for unmeasured confounding

4. **Comprehensive endpoints**: We evaluate the full disease trajectory including durable endocrine remission, endocrine control, biochemical recurrence, radiographic tumor control, salvage therapy, hypopituitarism, and visual/cranial nerve toxicity.

By integrating cavernous sinus invasion as the defining anatomical subgroup, IGF-1/IGF-1i as the defining biological variable, BED as the defining dosimetric variable, and medication hold as the defining treatment state variable—while characterizing the complete disease trajectory through remission, recurrence, and hypopituitarism—this study provides the first unified, subgroup-specific, multi-dimensional analysis of GKRS outcomes in acromegaly.