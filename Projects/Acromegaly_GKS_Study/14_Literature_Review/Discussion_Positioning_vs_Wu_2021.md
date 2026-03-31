# Discussion Template: Positioning Against Wu et al. (2021)

## Comparative Analysis: Your GKS Study vs. Wu et al.

---

## How Your Study Exceeds Wu et al. (2021)

### 1. Selection Bias Correction

| Aspect | Wu et al. (2021) | Your Study |
|--------|------------------|------------|
| **Baseline imbalance** | Significant (age, tumor volume, Knosp grade) | Addressed with overlap weighting |
| **Adjustment** | Univariate/multivariate Cox only | Propensity score + overlap weighting |
| **Comparability** | Groups not comparable at baseline | Covariate balance achieved post-weighting |

**Positioning:**
> "Wu et al. reported comparable outcomes between primary and postoperative GKS but did not adjust for substantial baseline imbalances, with 75.7% of postoperative patients having Knosp grade ≥3 versus only 26.3% in the primary group."

---

### 2. Multicenter Design

| Aspect | Wu et al. (2021) | Your Study |
|--------|------------------|------------|
| **Design** | Single-center (West China Hospital) | Multicenter international |
| **Sample size** | N=75 | Larger expected |
| **External validity** | Limited | Generalizable across centers |

**Positioning:**
> "In contrast to their single-center cohort, our multicenter international design provides broader generalizability."

---

### 3. Methodological Advancement

| Aspect | Wu et al. (2021) | Your Study |
|--------|------------------|------------|
| **Primary analysis** | Kaplan-Meier + Cox | KM + Cox + spline + weighted |
| **ML component** | None | XGBoost + RSF (exploratory) |
| **Validation** | None | Internal-external CV |

**Positioning:**
> "While Wu et al. applied standard survival analysis, we employed more comprehensive approaches including time-to-event modeling with flexible hazard functions and internal-external cross-validation."

---

## Suggested Discussion Paragraph

### Comparison with Prior GKS Studies

Wu et al. conducted a landmark comparison of primary versus postoperative Gamma Knife radiosurgery for acromegaly, finding comparable endocrine remission rates (21.1% vs 21.6%, p=0.831) and 8-year actuarial remission of 70.6% and 78.8% respectively. Their work established that GKS can serve as either a primary or adjuvant treatment modality.

However, important methodological differences exist between their cohort and ours. First, Wu et al. did not address substantial baseline imbalances between groups—the postoperative cohort had significantly higher rates of cavernous sinus invasion (75.7% vs 26.3%), larger tumor volumes (1.57 vs 1.01 cm³), and different age distributions. We applied overlap weighting to achieve covariate balance and reduce confounding. Second, their single-center design limits generalizability, whereas our multicenter international cohort provides broader external validity. Third, we incorporated internal-external cross-validation across centers to assess model robustness.

These differences are particularly relevant for cavernous sinus–invading disease, where treatment selection is most challenging. Our findings extend prior work by demonstrating comparable efficacy in this difficult-to-treat subgroup after appropriate adjustment for baseline differences.

---

## Key Points for Your Discussion

### What to Emphasize

1. **Baseline imbalance addressed** (they didn't adjust)
2. **Multicenter > Single-center** (better generalizability)
3. **Larger sample** (more statistical power)
4. **Cavernous sinus focus** (specific subpopulation)
5. **Advanced methods** (weighted analysis + validation)

### What to Acknowledge

- Their clinical question is valid and important
- Results are consistent with their findings (no difference)
- They established GKS as both primary and adjuvant treatment

### What to Avoid

- Don't dismiss their paper—acknowledge the contribution
- Focus on methodological improvement, not result dismissal

---

## Template Language

### To cite their work:

> "Wu et al. (2021) demonstrated comparable outcomes between primary and postoperative GKS in a single-center cohort of 75 patients."

### To differentiate:

> "Unlike Wu et al., who did not adjust for baseline imbalances between treatment groups, we applied overlap weighting to achieve covariate balance, addressing substantial differences in tumor burden and cavernous sinus invasion."

### To show advancement:

> "While Wu et al. focused on overall GKS outcomes in a single-center cohort, we specifically examined cavernous sinus–invading disease using multicenter data with internal-external validation."

---

## Summary Table

| Your Study Advantage | Wu et al. | Implication |
|---------------------|-----------|-------------|
| Baseline adjustment | Not performed | More credible comparison |
| Multicenter design | Single-center | Better generalizability |
| Cavernous sinus focus | All comers | More specific population |
| IECV | Not performed | More robust validation |
| Weighted analysis | Not performed | Reduced confounding |

---

## Key Quote for Your Paper

> "Wu et al. established that GKS achieves comparable efficacy whether used as primary treatment or adjuvant therapy after surgery. However, their postoperative cohort had markedly higher rates of cavernous sinus invasion (75.7% vs 26.3%), suggesting that even in surgically challenging cases, GKS provides meaningful disease control."

---

*Document created: 2026-03-21*
*For use in Discussion section positioning against Wu et al. (2021)*