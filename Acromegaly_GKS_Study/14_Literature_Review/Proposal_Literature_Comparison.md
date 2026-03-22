# Study Proposal: Literature Gap Analysis

## Your Proposal Strengths

### 1. Focused Subgroup
- CS-invading acromegaly = hardest surgical subgroup
- Most likely to require GKRS
- No dedicated GKRS study exists

### 2. Unified Framework
- Biology (IGF-1i) + Radiation (BED) + Treatment State (medication hold)
- First to combine all three in one CS-focused study

### 3. Multimodal Endpoints
- 10+ endpoints covering full disease course
- Durable remission, control, recurrence, salvage, toxicity

### 4. Advanced Methods
- KM + Cox + logistic
- IPW/overlap weighting
- Dynamic prediction model
- Spline for continuous variables

---

## Weaknesses to Address

### 1. Multi-State Model Not Explicit
**Current:** Traditional KM/Cox
**Suggested:** Explicit multi-state model for remission → recurrence → salvage

### 2. Continuous Variable Handling
**Current:** Low/high strata
**Suggested:** Continuous + spline (following Mayo BED paper)

### 3. Benefit-Risk Joint Framework
**Current:** Efficacy and toxicity analyzed separately
**Suggested:** Time to remission + time to hypopituitarism as co-primary

### 4. Early Biochemical Response
**Current:** Baseline factors only
**Suggested:** 6-month landmark analysis for early response prediction

---

## Literature Summary

### What Existing Papers Say

| Category | Conclusion |
|----------|------------|
| **Efficacy** | LC >90%, ER 40-60% @ 10yr |
| **Predictors** | IGF-1i stable, BED > dose, medication hold important |
| **Safety** | Hypopituitarism 17-30%, visual <5% |
| **Methodology** | Retrospective, inconsistent definitions, fragmented variables |

### Your Gap
> "In CS-invading acromegaly - the most surgically challenging subgroup - what determines durable remission vs toxicity balance?"

---

## Upgrade Path

| Current Level | Target Level |
|--------------|--------------|
| Predictor paper | Clinically distinct subgroup study |
| Multicenter cohort | Multimodal strategy paper |
| Traditional Cox | Dynamic outcome / multi-state |
| Fragmented variables | Unified framework (biology + radiation + treatment state) |

---

*Analysis date: 2026-03-21*