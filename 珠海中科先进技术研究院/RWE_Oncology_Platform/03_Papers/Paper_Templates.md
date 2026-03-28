# 论文模板 - Abstract + Results + Figure/Table Captions

---

## 1. Abstract模板 (Structured Abstract, 250-300字)

### Background
Patients with relapsed/refractory diffuse large B-cell lymphoma (R/R DLBCL) have limited treatment options. While PD-1-based immunotherapy has shown promise, real-world evidence is needed to evaluate its effectiveness after accounting for treatment selection bias. Additionally, the prognostic impact of immune-related adverse events (irAEs) remains unclear due to potential immortal time bias in conventional analyses.

### Methods
This retrospective cohort study emulated a target trial using real-world data from R/R DLBCL patients. PD-1-based therapy versus non-PD-1 salvage regimens was compared using stabilized inverse probability of treatment weighting (IPTW) after propensity score estimation. Covariate balance was assessed with standardized mean differences (SMD) and Love plots. The association between irAE occurrence and overall survival (OS) was evaluated using a time-dependent Cox proportional hazards model to avoid immortal time bias. Interaction between PD-1 therapy and irAE was explored. Sensitivity analyses included different trimming thresholds and landmark approaches.

### Results
A total of [N] patients were included ([n] in PD-1 group). After IPTW adjustment, baseline covariates were well balanced (all SMD < 0.10). PD-1-based therapy was associated with improved OS (HR [value], 95% CI [lower–upper]; p = [value]). Occurrence of irAE was associated with [better/worse/no significant difference in] survival in the time-dependent model (HR [value], 95% CI [lower–upper]; p = [value]). A significant interaction was observed between PD-1 therapy and irAE ([p for interaction = value]), suggesting that patients who developed irAE derived greater survival benefit from PD-1 therapy. Weighted Kaplan-Meier curves and sensitivity analyses supported the main findings.

### Conclusions
In this causal real-world study, PD-1-based immunotherapy was associated with improved survival in R/R DLBCL after rigorous adjustment for confounding. irAE occurrence, when properly modeled as a time-dependent exposure, was linked to survival outcomes and may serve as a clinical biomarker of treatment benefit. These findings provide actionable real-world evidence to support clinical decision-making and regulatory submissions.

**Keywords**: relapsed/refractory DLBCL, PD-1 immunotherapy, immune-related adverse events, time-dependent Cox model, real-world evidence, causal inference

---

## 2. Results段落模板

### Patient Characteristics
A total of [N] patients with R/R DLBCL were included in the analysis, of whom [n (%)] received PD-1-based immunotherapy. Before weighting, several imbalances were observed between groups (e.g., higher ECOG and LDH in the non-PD-1 group). After stabilized IPTW with trimming, all measured covariates were well balanced (maximum SMD < 0.10). The effective sample size (ESS) after weighting was [ESS value], representing [XX%] of the original cohort.

### Effectiveness of PD-1-Based Therapy
In the IPTW-weighted analysis, PD-1-based therapy was associated with significantly improved overall survival compared with non-PD-1 salvage regimens (HR [value], 95% CI [lower–upper]; p = [value]). The weighted Kaplan-Meier curves demonstrated separation favoring the PD-1 group. Similar trends were observed for progression-free survival (HR [value], 95% CI [lower–upper]). Objective response rate was also higher in the PD-1 group in the weighted logistic regression (OR [value], 95% CI [lower–upper]).

### Impact of irAE on Survival
When irAE was analyzed as a time-dependent exposure using the start-stop dataset, [n (%)] patients experienced irAE. In the time-dependent Cox model, irAE occurrence was associated with [HR value] (95% CI [lower–upper]; p = [value]). The landmark analysis at [3/6] months yielded consistent results. Importantly, a significant PD-1 × irAE interaction was observed (p = [value]), indicating that patients who developed irAE had [greater/less] survival benefit from PD-1 therapy compared with those without irAE.

### Sensitivity Analyses
The results were robust across multiple sensitivity analyses. Using different trimming thresholds (1%-99% vs 5%-95%) and alternative covariate specifications did not materially change the effect estimates. The E-value for the OS analysis was [value], suggesting that an unmeasured confounder would need to be associated with both treatment selection and survival by a risk factor of at least [value] to explain away the observed association.

---

## 3. Figure/Table标题模板

### Figures
- **Figure 1**: Patient flow diagram showing selection of the study cohort
- **Figure 2**: Love plot showing covariate balance before and after IPTW
- **Figure 3**: Weighted Kaplan-Meier curves for overall survival by treatment group
- **Figure 4**: Propensity score overlap (density plot) between PD-1 and non-PD-1 groups
- **Figure 5**: Patient timeline examples for time-dependent irAE analysis (start-stop format)
- **Figure 6**: Forest plot showing subgroup analyses

### Tables
- **Table 1**: Patient baseline characteristics before and after IPTW
- **Table 2**: Unweighted and weighted effect estimates (OS, PFS, ORR)
- **Table 3**: Time-dependent Cox model results for irAE and survival
- **Table 4**: Sensitivity analyses with different trimming thresholds
- **Table 5**: irAE characteristics (type, grade, timing)

---

## 4. 方法学亮点 (供Discussion)

1. **Target Trial Emulation**: We emulated a target trial using causal inference methods
2. **Time-dependent Cox**: Properly handled irAE as time-varying to avoid immortal time bias
3. **Stabilized IPTW**: Used stabilized weights to preserve precision
4. **ESS reporting**: Reported effective sample size for transparency
5. **Multiple sensitivities**: Confirmed robustness across analytic choices

---

*Template created: 2026-03-28*
*Ready for manuscript preparation*