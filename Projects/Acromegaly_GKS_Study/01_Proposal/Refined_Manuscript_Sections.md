# Refined Manuscript Sections
## Enhanced Methods, Results, Figures, Discussion

---

## METHODS (Enhanced Version)

### Study Design

This was an international multicenter retrospective cohort study of patients with acromegaly treated with GKRS.

### Patient Population

Patients were included if they met all of the following criteria:
- Clinical and biochemical diagnosis of acromegaly
- Radiographic evidence of cavernous sinus invasion or targeted intracavernous residual disease
- Treatment with GKRS
- Minimum endocrine follow-up of 12 months
- Availability of post-treatment endocrine and imaging data

Patients without confirmed cavernous sinus involvement or with insufficient data were excluded.

### Variables (Key: Organized by Domain)

**Biology:**
- IGF-1 index (IGF-1 / ULN)
- Baseline GH
- OGTT nadir GH (if available)

**Anatomy:**
- Knosp grade
- Tumor volume
- Cavernous sinus location

**Treatment State:**
- Interval from surgery to GKRS
- Medication hold vs no hold
- Residual vs recurrent disease

**Radiation:**
- Margin dose
- Maximum dose
- Isodose line
- Optic maximum dose
- Whole-sella vs targeted plan
- Biologically effective dose (BED)

### Outcomes

**Primary Outcome:**
- **Durable endocrine remission:**
  - Normal IGF-1
  - Off medication
  - No recurrence

**Secondary Outcomes:**
- Endocrine control
- Time to remission
- Recurrence
- Salvage therapy
- Radiographic control
- Hypopituitarism
- Visual/CN toxicity

### Statistical Analysis
- Kaplan–Meier for time-to-event outcomes
- Cox models for predictors
- Logistic regression for binary toxicity outcomes
- Restricted cubic splines for IGF-1i, BED, tumor volume, and timing
- Propensity weighting for:
  - medication hold vs no hold
  - whole-sella vs targeted
- **Exploratory dynamic analysis:**
  - landmark models at 6 and 12 months
  - optional multi-state modeling

---

## RESULTS (Structure Template)

### 1. Cohort
- N
- baseline IGF-1i
- Knosp distribution
- dose/BED

### 2. Endocrine Outcomes
- remission rate
- durable remission
- time to remission

### 3. Recurrence & Salvage
- recurrence rate
- salvage therapy types

### 4. Predictors
- IGF-1i
- medication hold
- BED
- timing
- CS extent

### 5. Toxicity
- hypopituitarism
- visual/CN events

### 6. Comparative analyses
- hold vs no hold
- whole-sella vs targeted

### 7. Dynamic modeling
- early vs late remission
- time-dependent effects

---

## FIGURES (Publication-Ready)

### Figure 1
**Flow diagram**
- Patient selection and cohort derivation

### Figure 2
**Kaplan-Meier: durable remission**
- Stratified by: medication hold vs no hold

### Figure 3
**Spline plots**
- Panel A: IGF-1i vs remission hazard
- Panel B: BED vs remission hazard

### Figure 4
**Kaplan-Meier: hypopituitarism**
- Stratified by: whole-sella vs targeted

### Figure 5
**Forest plot**
- Predictors of remission AND predictors of hypopituitarism side-by-side

---

## DISCUSSION (5-Paragraph Structure)

### Paragraph 1 — Main Findings
GKRS provides substantial long-term endocrine control in cavernous sinus–invading acromegaly, with durable remission achieved in a significant proportion of patients. However, outcomes evolve over time rather than occurring immediately.

### Paragraph 2 — Comparison with Literature
- Consistent with IGKRF (medication hold)
- Consistent with Mayo (IGF-1i, BED)
- Consistent with whole-sella study (toxicity tradeoff)

### Paragraph 3 — Your Innovations
- CS-invading subgroup focus
- Integrated biology + anatomy + dose + timing
- Dynamic outcome framework

### Paragraph 4 — Clinical Implications
- Earlier GKRS may be beneficial
- Medication hold should be considered
- Targeted planning may reduce toxicity

### Paragraph 5 — Limitations
- Retrospective design
- Heterogeneity across centers
- Missing data

---

## Master Conclusion

> Gamma Knife radiosurgery in cavernous sinus–invading acromegaly should be understood as a dynamic, time-dependent treatment in which durable remission and delayed toxicity reflect the interplay between tumor biology, treatment state, and radiosurgical strategy.

---

## Next Steps (Critical)

1. **Figure 2–4** (KM + spline) design specifications
2. **Statistical analysis** SAS/R code templates
3. **Results section** - fill-in template ready for submission

---

*Refined sections completed: 2026-03-21*
*Ready for data filling*