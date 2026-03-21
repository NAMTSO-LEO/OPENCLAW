# Literature Review: Primary vs Postoperative GKS for Acromegaly

## Article 2: Wu et al. (Clinical Neurology and Neurosurgery 2021)

---

### Publication Details

| Field | Value |
|-------|-------|
| **Title** | Comparing primary gamma knife radiosurgery and postoperative gamma knife radiosurgery for acromegaly: A monocenter retrospective study |
| **Journal** | Clinical Neurology and Neurosurgery |
| **Volume/Issue** | Vol 200, 2021 |
| **Year** | 2020 (published online) |
| **Authors** | Wu et al. |
| **Affiliations** | West China Hospital, Sichuan University |
| **DOI** | 10.1016/j.clineuro.2020.106385 |

---

### Study Overview

This study directly compared primary GKS (without prior surgery) vs postoperative GKS (adjuvant after surgery) for acromegaly - the **exact comparison** your study is making.

---

### Methods

| Aspect | Details |
|--------|---------|
| **Design** | Monocenter retrospective cohort |
| **Patients** | 75 patients (38 primary GKS, 37 postoperative GKS) |
| **Period** | March 2010 - December 2018 |
| **Follow-up** | ≥ 6 months |
| **Definition** | Age-sex matched IGF-1 normalization + GH nadir <1 ng/mL after OGTT or random GH <2.0 ng/mL, OFF medication ≥4 weeks |

---

### Key Results

#### Comparison: Primary vs Postoperative GKS

| Outcome | Primary GKS (n=38) | Postoperative GKS (n=37) | P-value |
|---------|-------------------|--------------------------|---------|
| **Initial remission rate** | 23.68% | 27.03% | 0.944 |
| **Durable remission rate** | 21.05% | 21.62% | 0.831 |
| **Biochemical recurrence** | 2.63% | 5.41% | 0.981 |
| **Imaging regression** | 66.67% | 74.07% | 0.563 |
| **New visual disturbance** | 7.89% | 5.41% | 1.000 |
| **New hypopituitarism** | 10.53% | 21.62% | 0.190 |

#### Actuarial Remission (Kaplan-Meier)

| Time | Primary GKS | Postoperative GKS | P-value |
|------|-------------|-------------------|---------|
| 3-year | 10.60% | 6.70% | 0.800 |
| 5-year | 33.80% | 43.40% | (log-rank) |
| 8-year | 70.60% | 78.80% | |

#### Predictors (Cox Regression)

| Variable | HR | 95% CI | P-value |
|----------|-----|--------|---------|
| **Base nadir GH after OGTT** | 0.637 | 0.416-0.977 | **0.039** |
| Margin dose | - | - | NS |
| Tumor volume | - | - | NS |

---

### Baseline Characteristics (Key Differences)

| Factor | Primary GKS | Postoperative GKS | P-value |
|--------|-------------|-------------------|---------|
| Mean age | 46.47 years | 40.95 years | 0.028 |
| Female % | 50.00% | 78.38% | 0.010 |
| Pre-GKS tumor volume | 1.01 cm³ | 1.57 cm³ | 0.042 |
| **Knosp ≥3** | 26.32% | **75.68%** | <0.001 |
| Pre-GKS visual disturbance | 5.26% | 27.03% | 0.010 |
| Margin dose | 28 Gy | 25 Gy | 0.008 |

---

### Key Insights

#### 1. No Significant Difference
> "We didn't find significant differences in endocrine remission, biochemical recurrence, imaging regression, imaging progression, radiation-induced complications between the primary GKS group and the postoperative GKS group."

#### 2. Key Predictor
Only **base nadir GH after OGTT** predicted durable remission (HR=0.637, p=0.039)

#### 3. Clinical Implications
- GKS effective for both primary and adjuvant settings
- Cavernous sinus invasion (Knosp ≥3) much higher in postoperative group (75.68% vs 26.32%)
- Despite more invasive tumors, postoperative GKS achieved similar remission rates
- GKS should be considered for residual/recurrent tumor including cavernous sinus invasion

---

### Comparison with Your Study

| Aspect | Wu et al. (2021) | Your Study |
|--------|------------------|------------|
| **Design** | Single-center | Multicenter international |
| **Sample** | 75 patients | TBD (likely larger) |
| **Primary comparison** | Primary vs Postoperative GKS | Primary vs Postoperative GKS |
| **Key predictor** | Nadir GH after OGTT | TBD |
| **Follow-up** | Median 25-27 months | TBD |
| **Validation** | None | Internal-external CV |

---

### Relevance to Your Study

1. **Directly relevant**: Same comparison (primary vs postoperative GKS)
2. **Similar endpoints**: Uses same remission definition
3. **Baseline imbalance**: They found significant differences in age, tumor volume, Knosp grade - your study should address this with overlap weighting
4. **Sample size**: Their N=75 is small; your multicenter may have larger sample
5. **Generalizability**: Single-center limits external validity; your multicenter design is stronger

---

### Citations for Your Manuscript

**Method comparison:**
> "Wu et al. compared primary GKS (n=38) with postoperative GKS (n=37) in a monocenter cohort and found comparable endocrine remission rates (21.05% vs 21.62%, p=0.831)."

**Endpoint alignment:**
> "Our remission definition is consistent with prior studies, including IGF-1 normalization (IGF-1 index ≤1) and GH criteria (nadir GH <1 ng/mL after OGTT or random GH <2.0 ng/mL), off medication for ≥4 weeks."

**Addressing confounding:**
> "In contrast to prior studies that reported baseline imbalances between treatment groups, we applied overlap weighting to achieve covariate balance and reduce confounding."

---

### What They Did Well

✓ Direct comparison of primary vs adjuvant GKS
✓ Standard remission criteria
✓ Kaplan-Meier time-to-event analysis
✓ Cox regression for predictors
✓ Long follow-up (up to 8 years)

---

### Limitations

✗ Single-center (limited generalizability)
✗ Baseline imbalance between groups (age, tumor size, Knosp grade)
✗ Small sample (N=75)
✗ No causal inference methods to address confounding
✗ No external validation

---

### How Your Study Improves Upon This

| Weakness in Wu et al. | Your Study Improvement |
|----------------------|------------------------|
| Single-center | Multicenter international |
| N=75 | Larger sample expected |
| Baseline imbalance not addressed | Overlap weighting applied |
| No external validation | IECV across centers |
| No ML/exploratory analysis | XGBoost + RSF (secondary) |

---

### Key Quote for Discussion

> "Wu et al. found comparable efficacy between primary and postoperative GKS, with 8-year actuarial remission rates of 70.6% and 78.8% respectively. However, their postoperative cohort had significantly higher rates of cavernous sinus invasion (75.68% vs 26.32%), suggesting GKS remains effective even in surgically challenging cases."

---

*Reviewed: 2026-03-21*