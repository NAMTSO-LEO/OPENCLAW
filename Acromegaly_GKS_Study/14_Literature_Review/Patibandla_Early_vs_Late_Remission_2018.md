# Literature Review: Early vs Late Remission Following SRS for Acromegaly

## Article 5: Patibandla et al. (Journal of Neuro-Oncology 2018)

---

### Publication Details

| Field | Value |
|-------|-------|
| **Title** | Factors affecting early versus late remission in acromegaly following stereotactic radiosurgery |
| **Journal** | Journal of Neuro-Oncology |
| **Volume/Issue** | Vol 138, 2018, Pages 209-216 |
| **Year** | 2018 (published online February) |
| **Authors** | Patibandla et al. |
| **Affiliations** | University of Virginia, Department of Neurosurgery |
| **DOI** | 10.1007/s11060-018-2792-x |

---

### Study Overview

This study specifically addresses **when** patients achieve remission after SRS, not just **if** they achieve remission. This is highly relevant to your time-to-event analysis approach.

---

### Key Results

#### Remission Timing Distribution

| Category | N | Percentage |
|----------|---|------------|
| **Total remission** | 102/157 | 64.9% |
| **Early remission (≤29 months)** | 62 | 60.7% |
| **Late remission (>29 months)** | 40 | 39.3% |

#### Actuarial Remission Rates

| Time after SRS | Remission Rate |
|----------------|----------------|
| 1 year | 10% |
| 2 years | 22% |
| 4 years | 61% |
| 6 years | 68% |
| 8 years | 77% |

---

### Key Predictors of Late Remission

| Factor | Early vs Late | P-value |
|--------|---------------|---------|
| **Time from last surgery to SRS** | 24.5 mo vs 41.5 mo | **0.040** |
| **Whole sella treated** | 27.4% vs 10.0% | **0.045** |
| **Cavernous sinus included** | 54.8% vs 32.5% | **0.041** |

---

### Competing Risk Analysis Results

| Variable | HR | 95% CI | P-value |
|----------|-----|--------|---------|
| **Time from resection to SRS** | 1.013 | 1.004-1.02 | **0.007** |
| Female gender | - | - | 0.054 (trend) |
| Pre-SRS IGF-1 | - | - | 0.08 (trend) |

**Interpretation:** Each month increase in interval from resection to SRS increases time to remission by 1.3%.

---

### Key Findings

#### 1. Early vs Late Remission
- Median time to remission: 16.3 months (early) vs 55.3 months (late)
- ~40% of patients achieve remission after 29 months

#### 2. Cavernous Sinus Involvement
- Patients with CS included in treatment had **earlier** remission (54.8% vs 32.5% in late group)
- This is counter-intuitive but suggests targeted treatment to CS may be more effective

#### 3. Timing from Surgery to SRS
- Longer interval = longer time to remission
- Suggests earlier SRS after surgery may be beneficial

#### 4. New Hypopituitarism
- 32.5% developed new endocrine deficiency
- Actuarial rates: 2.5% (2yr), 10.2% (4yr), 28.1% (6yr), 44% (8yr)
- No significant difference between early vs late groups (37% vs 35%)

---

### Comparison with Your Study

| Aspect | Patibandla et al. | Your Study |
|--------|------------------|------------|
| **Design** | Single-center (UVA) | Multicenter international |
| **N** | 157 | TBD |
| **Follow-up** | Median 66mo imaging, 104.8mo endocrine | TBD |
| **Primary outcome** | Early vs late remission | Time-to-remission |
| **Analysis** | Kaplan-Meier + competing risk | KM + Cox + weighted |
| **CS focus** | Included as variable | Primary focus |

---

### Key Insights for Your Paper

1. **Median time to remission**: 29 months - your data should be comparable
2. **Late remission is common**: 39.3% achieve remission after 29 months
3. **CS inclusion**: Associated with earlier remission (not delayed)
4. **Timing matters**: Earlier SRS after surgery → earlier remission

---

### Citations for Your Manuscript

**For remission timing:**
> "Patibandla et al. reported that 39.3% of patients achieve remission beyond 29 months following stereotactic radiosurgery, with actuarial rates of 61% at 4 years and 77% at 8 years."

**For CS treatment effect:**
> "In contrast to expectations, including the cavernous sinus in the radiosurgical target was associated with earlier remission (54.8% vs 32.5% in late remission group, p=0.041)."

**For timing from surgery:**
> "Patients with shorter intervals from last surgery to SRS achieved earlier remission (24.5 vs 41.5 months, p=0.040), suggesting earlier intervention may be beneficial."

**For hypopituitarism:**
> "New endocrine deficiency developed in 32.5% of patients, with actuarial rates increasing from 10.2% at 4 years to 44% at 8 years."

---

### Methodological Strengths

✓ Time-to-event analysis (Kaplan-Meier)
✓ Competing risk analysis
✓ Clear definition of early vs late (based on median)
✓ Long follow-up (104.8 months median)

---

### Limitations

✗ Single-center
✗ No multivariate adjustment for all predictors
✗ No weighting/propensity methods
✗ CS inclusion was physician preference (potential confounding)

---

### How Your Study Improves

| This Paper | Your Study |
|------------|------------|
| Single-center | Multicenter |
| No weighting | Overlap weighting |
| Early/late binary | Continuous time-to-event |
| CS as binary | CS by Knosp grade |
| No ML | XGBoost/RSF (exploratory) |

---

*Reviewed: 2026-03-21*