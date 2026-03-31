# Discussion Section - Final Version
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## Principal Findings

In this international multicenter study of patients with cavernous sinus–invading acromegaly, we demonstrate that Gamma Knife radiosurgery achieves high rates of long-term tumor control and clinically meaningful endocrine remission, albeit with delayed onset. Endocrine outcomes were strongly influenced by baseline hormonal burden, tumor characteristics, timing of radiosurgery, peri-radiosurgical medication management, and dosimetric parameters. Importantly, integrating these multimodal factors enabled accurate prediction of remission and treatment-related toxicity across centers.

---

## Interpretation and Clinical Implications

### Multimodal Determinants of Remission

Our findings highlight that endocrine remission after radiosurgery is not determined by a single factor but rather reflects the interplay between endocrine activity, tumor biology, and treatment strategy. Higher baseline IGF-1 index and larger tumor volume were associated with lower likelihood of remission, supporting the concept that hormonal burden and tumor load jointly define disease resistance. In contrast, shorter intervals from surgery to radiosurgery and higher biologically effective dose were associated with improved remission, suggesting that earlier and adequately dosed radiosurgical intervention may enhance treatment efficacy.

### Treatment Strategy Considerations

Using propensity-based overlap weighting, we observed that early radiosurgery and peri-radiosurgical medication hold were associated with improved endocrine outcomes, while targeted radiosurgery was associated with lower rates of hypopituitarism compared with whole-sellar coverage. These findings provide clinically actionable insights into treatment sequencing and planning, particularly in patients with residual cavernous sinus disease where complete surgical resection is not feasible.

### Dynamic Disease Trajectory

By applying a multi-state modeling framework, we demonstrate that acromegaly after radiosurgery follows a dynamic clinical trajectory characterized by transitions between uncontrolled disease, remission, recurrence, and treatment escalation. This approach captures the temporal complexity of endocrine outcomes and provides a more realistic representation of disease evolution than conventional single-endpoint analyses.

---

## Prediction and Individualized Care

We developed and validated prediction models incorporating clinical, endocrine, radiographic, and dosimetric variables, demonstrating good discrimination and calibration across centers. Notably, machine learning approaches did not substantially outperform penalized Cox models in terms of calibration, underscoring the importance of model interpretability and robustness in clinical applications.

Dynamic prediction using landmarking further enabled individualized risk estimation over time, reflecting changes in endocrine status and treatment exposure. Together, these findings support the feasibility of precision medicine approaches in acromegaly, with potential applications in treatment selection, patient counseling, and follow-up planning.

---

## Comparison With Prior Studies

Prior single-center and multicenter studies have consistently reported excellent tumor control but variable endocrine remission after radiosurgery for acromegaly. However, most studies included heterogeneous populations and did not specifically focus on cavernous sinus–invading disease. Furthermore, limited attention has been given to integrating surgical, endocrine, and radiosurgical factors within a unified analytical framework.

Our study extends the existing literature by focusing on a clinically distinct and surgically challenging subgroup, incorporating advanced statistical methods, and explicitly modeling treatment pathways and disease dynamics. The use of multi-state modeling and internal–external validation represents an important methodological advance over prior work.

---

## Strengths

This study has several strengths:

1. **Largest multicentric cohort** focusing specifically on cavernous sinus–invading acromegaly
2. **Unified analytical framework** integrating surgical, radiosurgical, endocrine, and radiographic data
3. **Advanced analytical methods** including propensity-based weighting, spline modeling, multi-state analysis, and internal–external cross-validation
4. **Clinically interpretable prediction models** with demonstrated utility for individualized risk stratification

---

## Limitations

Several limitations should be acknowledged:

1. **Retrospective design** introduces potential selection bias and residual confounding despite propensity-based adjustment
2. **Variability across centers** in endocrine assessment, imaging protocols, and treatment strategies may have introduced heterogeneity, although this also reflects real-world practice
3. **Missing data** and incomplete availability of OGTT and detailed dosimetric parameters in some cases may have affected endpoint classification
4. **External validation** in independent prospective cohorts is warranted to confirm generalizability
5. **Machine learning models** showed modest improvement over traditional models, highlighting the need for careful model selection in datasets of this size

---

## Conclusions

In patients with cavernous sinus–invading acromegaly, endocrine outcomes after Gamma Knife radiosurgery are driven by a complex interaction of hormonal, anatomical, and treatment-related factors. Early intervention, optimized radiosurgical dosing, and careful treatment planning may improve remission while minimizing toxicity. Integrating multimodal data enables accurate prediction of clinical outcomes and supports a shift toward individualized, data-driven management strategies in this challenging population.

---

## Key Reviewer Talking Points

| Point | What to Emphasize |
|-------|-------------------|
| Clinical relevance | Cavernous sinus invasion = surgically challenging subgroup |
| Methodological rigor | Overlap weighting + spline + multi-state + IECV |
| ML nuance | "Did not substantially improve calibration" |
| Generalizability | "Consistent performance across centers" |
| Future direction | External validation warranted |

---

## Suggested Closing Sentence

These findings provide a framework for personalized treatment planning and risk stratification in patients with cavernous sinus–invading acromegaly undergoing Gamma Knife radiosurgery.

---

*Document created: 2026-03-21*
*Version: Final - Submission Ready*
