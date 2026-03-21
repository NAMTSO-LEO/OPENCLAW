# Rebuttal Letter Template - Response to Reviewers
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

Dear Editor and Reviewers,

We sincerely thank the Editor and the Reviewers for your careful evaluation of our manuscript and for the constructive and insightful comments. We have revised the manuscript accordingly and believe that these changes have substantially improved the clarity, rigor, and clinical relevance of our study.

Below, we provide a point-by-point response to each comment. Reviewer comments are shown in *italics*, followed by our responses and corresponding revisions.

---

## Reviewer 1

### Comment 1: Selection Bias in Treatment Comparisons

*The comparison of treatment strategies (e.g., early vs delayed radiosurgery, medication hold vs no hold, targeted vs whole-sellar coverage) is potentially subject to significant selection bias. Although overlap weighting was applied, the authors should further clarify how treatment allocation decisions were made and whether unmeasured confounding may still influence the results.*

**Response:**

We thank the reviewer for this important comment. We agree that treatment allocation in this retrospective study was not randomized and may reflect underlying clinical decision-making, including tumor complexity and endocrine severity.

To address this concern, we applied overlap weighting based on propensity scores to reduce measured confounding and improve covariate balance across treatment groups (all SMDs <0.1). We have clarified this point in the Methods section.

We have also emphasized that treatment comparisons should be interpreted as hypothesis-generating rather than causal, as stated in the Discussion.

**Changes in manuscript:**
- Methods, Page XX: clarified propensity score model and covariate selection
- Discussion, Page XX: added statement on residual confounding and interpretative caution

---

### Comment 2: Remission Definition Consistency

*The definition of endocrine remission may vary across centers, particularly with respect to OGTT availability and assay variability. The authors should clarify how consistency was ensured and whether sensitivity analyses were performed.*

**Response:**

We appreciate this comment. Endocrine remission was defined primarily based on normalization of IGF-1 (IGF-1 index ≤1.0), with OGTT used as supportive evidence when available.

To address potential variability across centers, we performed sensitivity analyses using stricter remission definitions incorporating both IGF-1 and GH/OGTT criteria, which yielded consistent results.

We have clarified these definitions and added the sensitivity analyses in the revised manuscript.

**Changes:**
- Methods, Page XX: clarified remission definition and OGTT role
- Results, Page XX: added sensitivity analysis results
- Supplementary Table X: detailed criteria by center

---

### Comment 3: Multicenter Heterogeneity

*Given the multicenter nature of the study, variability in imaging protocols, endocrine assays, and treatment approaches may introduce heterogeneity that is not fully accounted for.*

**Response:**

We thank the reviewer for highlighting this important issue. We accounted for between-center heterogeneity using shared frailty models in Cox regression, as described in the Methods.

Furthermore, we performed internal–external cross-validation by iteratively leaving one center out, which demonstrated consistent model performance across centers, supporting the generalizability of our findings.

We have clarified these points in the revised manuscript.

**Changes:**
- Methods, Page XX: added frailty model description
- Results, Page XX: added IECV results

---

## Reviewer 2

### Comment 4: Machine Learning Value

*The added value of machine learning models over traditional regression models appears modest. The clinical implications of these models should be clarified.*

**Response:**

We fully agree with the reviewer's observation. In our study, machine learning models (random survival forests and gradient boosting) showed similar discrimination compared with penalized Cox models but did not substantially improve calibration.

We have revised the manuscript to emphasize that the primary value of the modeling framework lies in individualized risk estimation rather than algorithmic complexity. We have also highlighted the importance of model interpretability and robustness in clinical applications.

**Changes:**
- Discussion, Page XX: revised ML interpretation and clinical utility

---

### Comment 5: Follow-up Duration

*Given the delayed nature of endocrine remission after radiosurgery, longer follow-up may be required to fully capture outcomes.*

**Response:**

We agree that endocrine remission after radiosurgery is known to occur over several years. Although the median follow-up in our cohort was substantial, we acknowledge that longer follow-up may further refine remission estimates.

This limitation has been explicitly added to the Discussion.

**Changes:**
- Discussion, Page XX: added limitation statement

---

## Reviewer 3 (if applicable)

### Comment 6: Statistical Complexity

*The statistical approach is complex, and the rationale for using multiple advanced methods should be better explained.*

**Response:**

We thank the reviewer for this comment. Advanced statistical methods were applied to provide complementary perspectives on the data:

- **Cox regression with splines**: to model nonlinear relationships
- **Overlap weighting**: to reduce confounding in treatment comparisons
- **Multi-state modeling**: to characterize disease trajectories
- **Internal-external validation**: to assess generalizability

We have revised the manuscript to improve clarity and added brief explanations of the rationale for each method.

**Changes:**
- Methods, Page XX: simplified explanations
- Discussion, Page XX: added clarification on methodological rationale

---

## Additional Changes

We have also carefully reviewed the manuscript for clarity, consistency, and scientific accuracy and have revised the text throughout. All substantive changes have been highlighted in the revised version using track changes.

We believe that these revisions have substantially addressed all reviewer concerns and improved the overall quality of the manuscript.

Thank you for your consideration.

Sincerely,

[Your Name], MD/PhD
On behalf of all authors
[Institution]
[Email]

---

## Rebuttal Writing Tips

| Principle | Do | Don't |
|-----------|-----|-------|
| **Tone** | "We thank the reviewer..." | "We disagree..." |
| **Structure** | Thank → Acknowledge → Fix | Argue or defend |
| **Approach** | Turn weaknesses into strengths | Get defensive |
| **Language** | Professional and constructive | Combative |

---

## Key Phrases to Use

| Situation | Use This |
|-----------|----------|
| Agreeing | "We thank the reviewer for this important comment" |
| Partially agreeing | "We agree in part and have clarified..." |
| Explaining | "We have revised to clarify..." |
| Adding | "We have added..." |
| Emphasizing | "We have highlighted this point..." |

---

*Document created: 2026-03-21*
*Version: Rebuttal Letter Template*
