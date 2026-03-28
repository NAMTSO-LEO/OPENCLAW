# Oncology RWE Project Flowchart
## From Cohort Definition to Target Trial Emulation

---

## 📊 Complete Project Workflow (Text/ASCII)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ONCOLOGY RWE PROJECT FLOWCHART                         │
│                    (From Data to Regulatory Decision)                     │
└─────────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════
PHASE 1: COHORT DEFINITION
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐
    │  1. Source Data  │
    │  (EHR/Claims/    │
    │   Registry)      │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     ┌──────────────────┐
    │ 2. Study Pop     │────▶│ 3. Eligibility   │
    │    Definition    │     │    Criteria      │
    │                  │     │                  │
    │ - Cancer type    │     │ - Age, histology │
    │ - Diagnosis     │     │ - Stage          │
    │ - Timeline       │     │ - Prior therapy  │
    └──────────────────┘     └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ 4. Exclusions    │
                              │                  │
                              │ - Death before   │
                              │   index          │
                              │ - Missing data   │
                              └────────┬─────────┘
                                         │
                                         ▼
                              ┌──────────────────┐
                              │ 5. Final Cohort  │
                              │                  │
                              │ N = XXX patients │
                              └────────┬─────────┘
                                         │
                                         ▼
                              ┌──────────────────┐
                              │ 6. Cohort Flow    │
                              │    (Table 1)     │
                              │                  │
                              │ CONSORT Diagram  │
                              └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 2: INDEX DATE & TREATMENT DEFINITION
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐
    │ 7. Index Date   │
    │    Definition   │
    │                 │
    │ First therapy   │
    │ date after      │
    │ diagnosis       │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     ┌──────────────────┐
    │ 8. Treatment    │────▶│ 9. Treatment   │
    │    Exposure     │     │    Groups       │
    │                 │     │                 │
    │ - Drug A        │     │ - Treated      │
    │ - Drug B        │     │ - Control      │
    │ - Combination   │     │ - Propensity   │
    └──────────────────┘     │    Score       │
                              │    Match       │
                              └────────┬─────────┘
                                         │
                                         ▼
                              ┌──────────────────┐
                              │ 10. Censoring   │
                              │    Rules        │
                              │                 │
                              │ - Lost to F/U   │
                              │ - End of study  │
                              └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 3: PROPENSITY SCORE / IPTW
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐
    │ 11. Covariate   │
    │    Selection    │
    │                 │
    │ - Demographics │
    │ - Baseline labs │
    │ - Comorbidities │
    │ - Prior therapy │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     ┌──────────────────┐
    │ 12. PS Model    │────▶│ 13. PS Score    │
    │                 │     │                 │
    │ PROC LOGISTIC  │     │ P(T|X)          │
    │ PROC PSMATCH   │     │                 │
    │ - Class        │     └────────┬─────────┘
    │ - Continuous   │              │
    └────────┬─────────┘              ▼
             │              ┌──────────────────┐
             │              │ 14. IPTW        │
             │              │    Calculation  │
             │              │                 │
             │              │ Stabilized:     │
             │              │ P(T)/P(T|X)    │
             └──────────────▶│                 │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ 15. Weight       │
                            │    Trimming     │
                            │                 │
                            │ 1st-99th %ile   │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ 16. Balance     │
                            │    Diagnostics  │
                            │                 │
                            │ SMD < 0.1       │
                            │ (Love Plot)     │
                            └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 4: OUTCOME & ANALYSIS
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐
    │ 17. Outcome    │
    │    Definition  │
    │                 │
    │ OS: Death       │
    │ PFS: Progression│
    │    or Death    │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     ┌──────────────────┐
    │ 18. Follow-up   │────▶│ 19. Time-to-    │
    │    Window       │     │    event Analysis│
    │                 │     │                 │
    │ - From index   │     │ - Weighted KM   │
    │   to event/    │     │ - Weighted Cox  │
    │   censor       │     │ - Stratified    │
    └──────────────────┘     └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ 20. Results      │
                              │                 │
                              │ HR, 95% CI      │
                              │ p-value          │
                              │ C-index          │
                              └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 5: SENSITIVITY & ROBUSTNESS
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐
    │ 21. Complete    │
    │    Case         │
    │    Analysis     │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     ┌──────────────────┐
    │ 22. Different  │────▶│ 23. E-value    │
    │    Trimming     │     │    Analysis     │
    │    Thresholds  │     │                 │
    │                 │     │ Unmeasured      │
    │ - 5th-95th    │     │ confounding     │
    │ - 1st-99th    │     │ sensitivity     │
    └──────────────────┘     └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ 24. Multiple   │
                              │    Imputation   │
                              │                 │
                              │ Missing data    │
                              │ robustness      │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ 25. Positive   │
                              │    Controls     │
                              │                 │
                              │ Known effect    │
                              │ validation      │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ 26. Negative    │
                              │    Controls     │
                              │                 │
                              │ Null effect     │
                              │ validation      │
                              └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 6: TARGET TRIAL EMULATION
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────────────────────────────────────────────────────────┐
    │                    TARGET TRIAL EMULATION FRAMEWORK                  │
    └──────────────────────────────────────────────────────────────────────┘

    ┌───────────────────────┐        ┌───────────────────────┐
    │   27. Trial Specs    │        │   28. Emulation      │
    │       (Real)         │        │      (RWE)           │
    │                       │        │                       │
    │ - Eligibility        │   ──▶  │ - Same eligibility  │
    │ - Treatment          │        │ - Treatment          │
    │ - Outcome            │        │ - Outcome            │
    │ - Follow-up          │        │ - Follow-up          │
    │ - Assignment          │        │ - Assignment:        │
    │                       │        │   IPTW               │
    └───────────────────────┘        └────────┬───────────────┘
                                              │
                                              ▼
    ┌─────────────────────────────────────────────────────────────────────┐
    │                    KEY EMULATION CRITERIA                           │
    │                                                                      │
    │  ✓ Same treatment strategy definitions                              │
    │  ✓ Same eligibility criteria (translated to codes)                  │
    │  ✓ Same outcome definitions (validated)                             │
    │  ✓ Same start/end of follow-up                                      │
    │  ✓ Address immortal time bias                                       │
    │  ✓ Address selection bias (PS/IPTW)                                │
    │                                                                      │
    │  FDA/EMA Guidance: "Real-world evidence should be based on          │
    │  well-defined trials that could have been conducted"               │
    └─────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────┐
    │                    TRANSLATION TO FDA/EMA SUBMISSION               │
    │                                                                      │
    │ 1. Protocol (SAP) - Pre-specify analysis plan                       │
    │ 2. Statistical Analysis - PS/IPTW methodology documented            │
    │ 3. Sensitivity - Multiple robustness checks                         │
    │ 4. Documentation - All decisions traceable                          │
    │ 5. Validation - Outcome codes validated vs medical records          │
    └─────────────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════════════
PHASE 7: OUTPUTS & DELIVERABLES
══════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
    │ Table 1:        │     │ Table 2:        │     │ Table 3:        │
    │ Cohort Flow     │     │ Baseline        │     │ PS Model        │
    │ (CONSORT)       │     │ Characteristics │     │ Specifications   │
    └──────────────────┘     └──────────────────┘     └──────────────────┘

    ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
    │ Figure 1:       │     │ Figure 2:       │     │ Table 4:        │
    │ Weighted KM     │     │ Love Plot       │     │ Cox Regression  │
    │ Curves           │     │ (Balance)       │     │ Results         │
    └──────────────────┘     └──────────────────┘     └──────────────────┘

    ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
    │ Sensitivity:    │     │ Subgroup:       │     │ Appendix:       │
    │ E-value         │     │ Forest Plot     │     │ Code & Logs     │
    └──────────────────┘     └──────────────────┘     └──────────────────┘


══════════════════════════════════════════════════════════════════════════════
                         DELIVERABLE CHECKLIST
══════════════════════════════════════════════════════════════════════════════

☑ Protocol/SAP with pre-specified analysis
☑ Covariate selection rationale documented
☑ PS model specifications (variables, interactions)
☑ IPTW calculation formula & code
☑ Balance diagnostics (SMD < 0.1 for all)
☑ Weighted analysis results (HR, 95% CI, p-value)
☑ Sensitivity analyses (trimming, complete case)
☑ E-value calculation
☑ Target Trial Emulation framework documented
☑ Validation: outcome codes vs source data
☑ CONSORT flow diagram
☑ All code reproducible

══════════════════════════════════════════════════════════════════════════════
```

---

## 📝 Detailed Phase Descriptions

### Phase 1: Cohort Definition
| Step | Description | Key Decision |
|------|-------------|--------------|
| 1 | Source data identification | EHR vs Claims vs Registry |
| 2 | Study population | Incident vs Prevalent |
| 3 | Eligibility criteria | Inclusions/Exclusions |
| 4 | Exclusion application | Sequential filtering |
| 5 | Final cohort | N and characteristics |
| 6 | Cohort flow diagram | CONSORT-style |

### Phase 2: Index Date & Treatment
| Step | Description | Key Decision |
|------|-------------|--------------|
| 7 | Index date definition | First therapy? Diagnosis? |
| 8 | Treatment exposure | Drug names, doses |
| 9 | Treatment groups | A vs B vs A+B |
| 10 | Censoring rules | Loss to follow-up |

### Phase 3: PS/IPTW
| Step | Description | Key Decision |
|------|-------------|--------------|
| 11 | Covariate selection | Literature + clinical |
| 12 | PS model | Logistic vs GBM |
| 13 | PS score | Distribution check |
| 14 | IPTW formula | Stabilized weights |
| 15 | Trimming | Percentile vs threshold |
| 16 | Balance diagnostics | SMD thresholds |

### Phase 4: Outcome & Analysis
| Step | Description | Key Decision |
|------|-------------|--------------|
| 17 | Outcome definition | OS/PFS criteria |
| 18 | Follow-up window | From-to dates |
| 19 | Analysis method | Cox vs others |
| 20 | Results reporting | HR, CI, p-value |

### Phase 5: Sensitivity
| Step | Description | Key Decision |
|------|-------------|--------------|
| 21 | Complete case | No imputation |
| 22 | Trimming thresholds | Different cutoffs |
| 23 | E-value | Unmeasured confounding |
| 24 | Multiple imputation | Missing handling |
| 25 | Positive control | Known effect |
| 26 | Negative control | Null effect |

### Phase 6: Target Trial Emulation
| Step | Description | Key Decision |
|------|-------------|--------------|
| 27 | Trial specifications | Real trial protocol |
| 28 | Emulation mapping | RWE equivalents |
| - | Key criteria | 5 essential elements |
| - | FDA/EMA alignment | Regulatory language |

### Phase 7: Deliverables
| Item | Description |
|------|-------------|
| Table 1 | Cohort flow |
| Table 2 | Baseline table |
| Table 3 | PS model specs |
| Table 4 | Regression results |
| Figure 1 | Weighted KM |
| Figure 2 | Love plot |
| Figure 3 | Forest plots |
| Appendix | Full code |

---

## 🎯 Quick Reference for Statistician/Medical Director

### Key Discussion Points:
1. **Why PS/IPTW?** - "To reduce selection bias in non-randomized data"
2. **Balance check** - "All covariates with SMD < 0.1 after weighting"
3. **Stabilization** - "Weights stabilized to prevent extreme values"
4. **Sensitivity** - "Multiple robustness checks performed"
5. **Target Trial** - "Analysis structured as if conducting an RCT"

### Timeline:
- Phase 1-2: 1-2 weeks
- Phase 3: 1 week
- Phase 4: 1 week
- Phase 5-6: 1 week
- Phase 7: 1 week
- **Total: ~6-7 weeks**

---

*Flowchart completed: 2026-03-28*
*Ready for oncology RWE projects*