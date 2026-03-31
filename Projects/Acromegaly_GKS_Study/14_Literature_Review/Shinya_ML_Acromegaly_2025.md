# Literature Review: ML in Pituitary Adenoma Surgery
## Article 1: Supervised Machine Learning for Acromegaly

---

### Publication Details

| Field | Value |
|-------|-------|
| **Title** | A supervised machine learning approach for predicting the need for post-surgical intervention in acromegaly |
| **Journal** | Neurosurgical Focus |
| **Volume/Issue** | Vol 59, Issue 1 |
| **Year** | 2025 |
| **Authors** | Shinya et al. |
| **Affiliations** | Mayo Clinic, University of Tokyo |
| **DOI** | 10.3171/2025.4.FOCUS2597 |
| **Submitted** | January 21, 2025 |
| **Accepted** | April 22, 2025 |

---

### Study Overview

This study developed supervised machine learning models to predict the need for additional interventions (surgery, radiation, or medical therapy) in patients with growth hormone-secreting pituitary adenomas (acromegaly) after initial transsphenoidal surgery.

---

### Key Methods

- **Study Design**: Retrospective cohort
- **Patients**: ~100 patients with GH-secreting adenomas
- **Period**: 2013-2023
- **ML Algorithms**: Tree-based supervised learning models
- **Outcomes**: Prediction of additional interventions (re-operation, radiation, medical therapy)
- **Validation**: Not specified in detail

---

### Key Findings

| Outcome | Result |
|---------|--------|
| **Model Accuracy** | 81% |
| **Key Predictors** | Tumor size <9mm, Complete tumor removal, Age <65 years, Lower Knosp-Steiner grade |

---

### Comparison with Your GKS Study

| Aspect | Shinya et al. | Your Study |
|--------|---------------|-------------|
| **Population** | Post-surgical acromegaly | Cavernous sinus-invading acromegaly undergoing GKS |
| **Intervention** | Surgery → Additional intervention | GKS as primary/adjuvant treatment |
| **Outcome** | Need for additional intervention | Endocrine remission, recurrence, hypopituitarism |
| **ML Approach** | Tree-based models | Cox + RSF + XGBoost (planned) |
| **Sample Size** | ~100 | TBD |
| **Multi-center** | Mayo + Tokyo | Your multicenter design |

---

### Relevance to Your Study

1. **Similar ML framework**: Their 81% accuracy with tree-based models provides a benchmark
2. **Key predictors overlap**: Tumor size, Knosp grade are common predictors
3. **Validation approach**: Their model used single-institution data; your multicenter IECV is stronger
4. **Clinical utility**: Both aim to predict treatment outcomes to guide decision-making

---

### Citations for Your Manuscript

**Can cite as:**
> "Recent studies have applied machine learning to predict outcomes in acromegaly. Shinya et al. developed a supervised learning model achieving 81% accuracy in predicting need for additional intervention, identifying tumor size, extent of resection, and Knosp grade as key predictors."

---

### Related Publications by Same Group

| Publication | Journal | Year |
|-------------|---------|------|
| ML-based model for Cushing's disease outcomes | J Neurosurgery | 2025 |
| ML for long-term tumor control in acromegaly | J Neurol Surg B: Skull Base | 2025 |

---

### Notes

- This paper is highly relevant as it provides ML benchmark in same disease area
- Your study adds value by focusing on **radiosurgery (GKS)** rather than surgery
- Your multicenter design and internal-external validation are methodological strengths
- Consider citing this paper in Discussion as comparison

---

*Reviewed: 2026-03-21*
