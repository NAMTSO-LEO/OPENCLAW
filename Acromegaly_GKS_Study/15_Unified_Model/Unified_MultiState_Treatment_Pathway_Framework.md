# Unified Multi-State Model for Acromegaly Treatment Pathway

## A Framework for Top-Tier Publication (JCO/Lancet Oncology Level)

---

## Executive Summary

This document outlines a unified analytical framework that synthesizes three treatment modalities (surgery, Gamma Knife SRS, and fractionated radiotherapy) into a comprehensive multi-state disease model. This approach addresses the major limitations of existing literature and positions the research for top-tier journal publication.

---

## 1. Study Rationale

### 1.1 Literature Gaps

Current literature treats each treatment modality in isolation:
- **Surgery papers** (e.g., Cardinal 2020): Focus on immediate remission, ignore subsequent treatments
- **GKRS papers** (e.g., Patibandla 2018, Knappe 2020): Analyze single modality, ignore surgical history
- **IMRT papers** (e.g., Lian 2020): Fractionated approach, limited comparison with SRS

### 1.2 The Problem

1. **Selection bias**: Patients receiving RT are fundamentally different from surgical cures
2. **Time scale mismatch**: Surgery works in weeks, radiation in years
3. **Treatment switching**: Patients move between modalities but are analyzed in silos
4. **Competing risks**: Remission, relapse, toxicity occur simultaneously

### 1.3 Our Solution

A unified multi-state model that tracks patients across all treatment pathways with time-dependent transitions.

---

## 2. Proposed State Definitions

### 2.1 Core Disease States

```
State 0: Active Disease (IGF-1 elevated, untreated)
State 1: Post-Surgery Remission (IGF-1 normal, no meds)
State 2: Post-Surgery Residual (IGF-1 elevated, no further treatment)
State 3: Medical Control (IGF-1 normal on medication)
State 4: Post-Radiation Remission (IGF-1 normal, no meds, >12 months)
State 5: Radiation Partial Response (IGF-1 improved but not normal)
State 6: New Hypopituitarism (any new hormone deficiency)
State 7: Visual/S neurological deficit
State 8: Death (all causes)
```

### 2.2 State Transitions

```
Active Disease → Surgery → Post-Surgery Remission
                            → Post-Surgery Residual
                  → Medical Control

Post-Surgery Residual → GKRS/IMRT → Post-Radiation Remission
                                    → Radiation Partial Response
                        → Medical Control

Post-Surgery Remission → Relapse → Active Disease
                              → Medical Control

New Hypopituitarism can occur at any state after treatment
```

### 2.3 Time-Dependent Features

- **Clock**: Time since diagnosis
- **Treatment history**: Which treatments received and when
- **IGF-1 trajectory**: Continuous value over time
- **Tumor characteristics**: Static (Knosp, volume) and dynamic (response)

---

## 3. Statistical Framework

### 3.1 Primary Analysis: Multi-State Model

**Software**: R package `msm` or `mstate`

**Model Specification**:
```r
# Example state definitions
states <- c("Active", "SurgeryRem", "SurgeryResid", "Medical",
            "RTRem", "RTPartial", "Hypopit", "Death")

# Transition intensity matrix Q
# Transitions allowed:
# Active → SurgeryRem, SurgeryResid, Medical
# SurgeryRem → Relapse → Active
# SurgeryResid → RTRem, RTPartial, Medical
# RTRem → Relapse → Active
# All states → Hypopit
# All states → Death (competing)
```

### 3.2 Covariate Effects

| Covariate | Expected Effect |
|-----------|-----------------|
| Knosp grade (higher) | Slower transition to remission |
| Pre-treatment IGF-1 | Slower transition to remission |
| Age | Faster remission, higher toxicity |
| Margin dose (higher) | Faster remission |
| Whole-sellar treatment | Faster remission, higher toxicity |
| Prior surgeries (multiple) | Slower remission |

### 3.3 Competing Risk Framework

For each transition to absorbing state (Death, Hypopituitarism):
- Use Fine-Gray subdistribution hazard model
- Treat other clinical events as competing risks

### 3.4 Joint Model (Advanced)

**For IGF-1 trajectory + event hazard:**
- Use R package `JMbayes` or `lcmm`
- Model: IGF-1(t) = mixed-effects + event hazard

---

## 4. Data Structure Requirements

### 4.1 Variables Needed

| Variable | Type | Source |
|----------|------|--------|
| Patient ID | Identifier | All |
| Diagnosis date | Date | All |
| Surgery date(s) | Date | Surgical series |
| Extent of resection | Categorical | Surgical series |
| GKRS/IMRT date | Date | Radiation series |
| Margin dose | Continuous | Radiation series |
| Isodose line | Continuous | Radiation series |
| Knosp grade | Ordinal (0-4) | Imaging |
| Tumor volume | Continuous | Imaging |
| IGF-1 (serial) | Continuous | Labs |
| GH (serial) | Continuous | Labs |
| Pituitary function (serial) | Categorical | Labs |
| Visual fields (serial) | Categorical | Clinical |
| Death | Binary + date | Registry |
| Last follow-up | Date | All |

### 4.2 CDISC Alignment

This framework aligns with CDISC standards:
- **ADSL**: Patient-level demographics
- **ADVS**: Vital signs / tumor measurements
- **ADLB**: Laboratory results (IGF-1, GH, hormones)
- **ADTTE**: Time-to-event endpoints

---

## 5. Key Research Questions

### 5.1 Primary Question
**What are the time-dependent probabilities of achieving durable remission across different treatment sequences?**

### 5.2 Secondary Questions

1. **Treatment Effect**: Does early vs delayed radiation affect time to remission?
2. **Dose-Response**: What is the relationship between margin dose and remission time?
3. **Toxicity Trade-off**: What is the competing risk of hypopituitarism vs remission?
4. **Prediction**: Can we build a dynamic prediction model for individual patients?

### 5.3 Sensitivity Analyses

1. Different remission definitions (strict vs lenient)
2. Different follow-up truncation
3. Multiple imputation for missing data

---

## 6. Visualization Plan

### 6.1 Figure 1: Treatment Pathway Sankey Diagram
- Show patient flow from diagnosis through all treatments
- Width of arrows = number of patients

### 6.2 Figure 2: State Occupancy Probabilities
- Stacked area plot showing proportion in each state over time
- Faceted by treatment strategy

### 6.3 Figure 3: Cumulative Incidence Curves
- Competing risk plot for hypopituitarism and death
- Stratified by treatment modality

### 6.4 Figure 4: Forest Plot of Transition Hazards
- HRs for each covariate effect on each transition

### 6.5 Figure 5: Dynamic Prediction Nomogram
- Predict probability of remission at 1, 3, 5 years given patient characteristics

---

## 7. Expected Contributions

### 7.1 Methodological
- First unified multi-state model across treatment modalities
- Novel competing risk analysis for pituitary radiotherapy
- Dynamic prediction framework for clinical decision-making

### 7.2 Clinical
- Evidence for optimal treatment sequencing
- Quantification of benefit-risk trade-off
- Personalized prediction of treatment outcomes

### 7.3 Policy
- Framework for treatment guidelines
- Resource allocation for pituitary tumor centers

---

## 8. Timeline and Resources

| Phase | Duration | Activities |
|-------|-----------|------------|
| Data collection | 2 months | Retrospective chart review |
| Data cleaning | 1 month | Quality checks, imputation |
| Primary analysis | 2 months | Multi-state modeling |
| Secondary analyses | 1 month | Sensitivity, subgroup |
| Visualization | 1 month | Figures, tables |
| Writing | 2 months | Manuscript preparation |

**Total**: ~9 months to first draft

---

## 9. Target Journals

| Journal | Impact | Fit |
|---------|--------|-----|
| **Lancet Oncology** | 50+ | Perfect for clinical pathway analysis |
| **JCO** | 25+ | Strong for retrospective cohort studies |
| **JCEM** | 6+ | Good for endocrine focus |
| **Neurosurgery** | 4+ | Good for neurosurgical audience |

---

## 10. Key References for Methods

1. **Multi-state models**: van Houwelingen & Putter (2012) "Dynamic Modeling and Long-Term Predictions"
2. **Competing risks**: Fine & Gray (1999) "A Proportional Hazards Model for Subdistribution"
3. **Joint models**: Rizopoulos (2010) "Joint Models for Longitudinal and Time-to-Event Data"

---

## 11. Next Steps

1. **Confirm data availability** from your multicenter cohort
2. **Define exact state structure** based on your data elements
3. **Begin SAS/R programming** for the multi-state framework
4. **Draft Introduction** focusing on the literature gap

---

*Document created: 2026-03-21*
*This framework is designed for top-tier journal publication (JCO/Lancet Oncology level)*