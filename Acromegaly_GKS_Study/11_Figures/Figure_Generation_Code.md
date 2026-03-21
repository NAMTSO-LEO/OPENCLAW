# Figure Generation Code - R and SAS
## Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly

---

## R Code Package

### Required Libraries

```r
# Install if needed
install.packages(c("survival", "survminer", "rms", "ggplot2", "ggDCA", 
                 "riskRegression", "prodlim", "tidyverse", "openxlsx"))

# Load libraries
library(survival)
library(survminer)
library(rms)
library(ggplot2)
library(ggDCA)
library(riskRegression)
library(prodlim)
library(tidyverse)
library(openxlsx)
```

---

## Figure 1: Study Flow Diagram

### R Code

```r
# Study flow diagram data
flow_data <- data.frame(
  stage = c("Initial cohort", 
            "Excluded (n=X)",
            "  - No cavernous sinus invasion",
            "  - Follow-up <12 months", 
            "  - Missing baseline data",
            "Final analysis set"),
  n = c(N, 
        N - final_n,
        NA, NA, NA,
        final_n)
)

# Create flow diagram using ggplot2
ggplot(flow_data, aes(x = 1, y = n, fill = stage)) +
  geom_bar(stat = "identity", width = 0.5) +
  geom_text(aes(label = paste0(stage, "\n(n=", n, ")")), 
            position = position_stack(vjust = 0.5)) +
  coord_flip() +
  theme_minimal() +
  theme(axis.text = element_blank(),
        axis.title = element_blank(),
        legend.position = "bottom") +
  scale_fill_brewer(palette = "Set2")
```

---

## Figure 2: Kaplan–Meier Curves (Endocrine Remission)

### R Code

```r
# Fit Kaplan–Meier
fit_remission <- survfit(Surv(time, event_remission) ~ strat_variable, 
                          data = adtte)

# Basic KM plot
ggsurvplot(fit_remission,
           data = adtte,
           conf.int = TRUE,
           risk.table = TRUE,
           risk.table.col = "strata",
           surv.median.line = "hv",
           pval = TRUE,
           ggtheme = theme_minimal(),
           palette = c("#2E86AB", "#A23B72", "#F18F01"),
           xlab = "Months after Gamma Knife",
           ylab = "Probability of Endocrine Remission",
           title = "Time to Endocrine Remission")
```

### With Custom Stratification (e.g., IGF-1 Index)

```r
# Create IGF-1 category
adtte$igf1_cat <- cut(adtte$IGF1I, 
                       breaks = quantile(adtte$IGF1I, c(0, 0.33, 0.67, 1), na.rm = TRUE),
                       labels = c("Low", "Medium", "High"))

# KM by IGF-1 category
fit_igf1 <- survfit(Surv(TTRREM, event = REN REMISS) ~ igf1_cat, data = adtte)

ggsurvplot(fit_igf1,
           data = adtte,
           conf.int = TRUE,
           risk.table = TRUE,
           pval = TRUE,
           log.rank.weights = "Fleming-Harrington",
           palette = c("#28A745", "#FFC107", "#DC3545"),
           xlab = "Months",
           ylab = "Cumulative Probability of Remission",
           legend.title = "IGF-1 Index")
```

---

## Figure 3: Kaplan–Meier Curves (Hypopituitarism)

### R Code

```r
# Fit for hypopituitarism
fit_hypo <- survfit(Surv(TTHYPO, event = HYPOEVENT) ~ PLAN_TYPE, 
                     data = adtte)

ggsurvplot(fit_hypo,
           data = adtte,
           conf.int = TRUE,
           risk.table = TRUE,
           pval = TRUE,
           palette = c("#17A2B8", "#6C757D"),
           xlab = "Months after Gamma Knife",
           ylab = "Probability of New Hypopituitarism",
           title = "Time to New Hypopituitarism by Planning Strategy")
```

---

## Figure 4: Restricted Cubic Spline Plots

### R Code

```r
# Fit Cox model with spline
library(rms)

# For IGF-1 Index
dd <- datadist(adtte)
options(datadist = "dd")

fit_spline_igf1 <- cph(Surv(TTRREM, event = REMISS) ~ rcs(IGF1I, 4), 
                         data = adtte, x = TRUE, y = TRUE)

# Plot spline
ggplot(Predict(fit_spline_igf1, IGF1I, fun = exp), 
       conf = 0.95) +
  geom_hline(yintercept = 1, linetype = "dashed", color = "gray") +
  geom_smooth() +
  theme_minimal() +
  labs(x = "Baseline IGF-1 Index",
       y = "Hazard Ratio for Remission",
       title = "Nonlinear Association between IGF-1 Index and Remission")

# For BED (biologically effective dose)
fit_spline_bed <- cph(Surv(TTRREM, event = REMISS) ~ rcs(BED, 4), 
                       data = adtte, x = TRUE, y = TRUE)

ggplot(Predict(fit_spline_bed, BED, fun = exp), 
       conf = 0.95) +
  geom_hline(yintercept = 1, linetype = "dashed", color = "gray") +
  geom_smooth() +
  theme_minimal() +
  labs(x = "Biologically Effective Dose (Gy)",
       y = "Hazard Ratio for Remission",
       title = "Nonlinear Association between BED and Remission")
```

### Combined Spline Plot (2 panels)

```r
# Combine using patchwork or gridExtra
library(patchwork)

p1 <- ggplot(Predict(fit_spline_igf1, IGF1I, fun = exp), conf = 0.95) +
  geom_hline(yintercept = 1, linetype = "dashed") +
  geom_smooth() + theme_minimal() +
  labs(x = "IGF-1 Index", y = "HR for Remission") +
  ggtitle("A) IGF-1 Index")

p2 <- ggplot(Predict(fit_spline_bed, BED, fun = exp), conf = 0.95) +
  geom_hline(yintercept = 1, linetype = "dashed") +
  geom_smooth() + theme_minimal() +
  labs(x = "BED (Gy)", y = "HR for Remission") +
  ggtitle("B) Biologically Effective Dose")

p1 + p2
```

---

## Figure 5: Multi-State Model Diagram

### R Code

```r
library(mstate)

# Create transition matrix
tmat <- trans.illnessdeath(from = c("Uncontrolled", "Remission", "Remission"),
                           to = c("Remission", "Recurrence", "Hypopituitarism"),
                           names = c("Uncontrolled", "Remission", "Recurrence", 
                                   "Hypopituitarism", "Death"))

# Fit competing risk model
library(cmprsk)
crr_model <- crr(ftime, fstatus, cov1, failcode = 1, cencode = 0)

# Create state probability plot
# (simplified visualization)
states <- c("Uncontrolled", "Remission", "Recurrence", "Hypopituitarism", "Death")
transitions <- data.frame(
  from = c("Uncontrolled", "Remission", "Remission", "Remission", "Uncontrolled"),
  to = c("Remission", "Recurrence", "Hypopituitarism", "Death", "Hypopituitarism"),
  prob = c(0.45, 0.15, 0.12, 0.03, 0.08)  # Example probabilities
)

# Manual diagram using ggplot2
ggplot() +
  # State boxes
  annotate("rect", xmin = 0, xmax = 1, ymin = 4, ymax = 5, 
           fill = "#FF6B6B", alpha = 0.3) +
  annotate("rect", xmin = 2, xmax = 3, ymin = 4, ymax = 5, 
           fill = "#4ECDC4", alpha = 0.3) +
  annotate("rect", xmin = 2, xmax = 3, ymin = 2, ymax = 3, 
           fill = "#FFE66D", alpha = 0.3) +
  annotate("rect", xmin = 4, xmax = 5, ymin = 4, ymax = 5, 
           fill = "#95E1D3", alpha = 0.3) +
  annotate("rect", xmin = 4, xmax = 5, ymin = 2, ymax = 3, 
           fill = "#636E72", alpha = 0.3) +
  # State labels
  annotate("text", x = 0.5, y = 4.5, label = "Uncontrolled", size = 4) +
  annotate("text", x = 2.5, y = 4.5, label = "Remission", size = 4) +
  annotate("text", x = 2.5, y = 2.5, label = "Recurrence", size = 4) +
  annotate("text", x = 4.5, y = 4.5, label = "Hypopituitarism", size = 4) +
  annotate("text", x = 4.5, y = 2.5, label = "Death", size = 4) +
  theme_void() +
  xlim(-0.5, 5.5) + ylim(1, 5.5)
```

---

## Supplement Figure: Calibration Plot

### R Code

```r
library(rms)

# Calibration at 3 years
cal_3y <- calibrate(fit_cox, 
                    cmethod = "hare", 
                    method = "boot", 
                    u = 36, # 36 months = 3 years
                    m = 50, # bucket size
                    B = 200)

plot(cal_3y, 
     xlab = "Predicted Probability",
     ylab = "Observed Probability",
     main = "Calibration at 3 Years")

# Calibration at 5 years
cal_5y <- calibrate(fit_cox, 
                    cmethod = "hare", 
                    method = "boot", 
                    u = 60,
                    m = 50,
                    B = 200)

plot(cal_5y,
     xlab = "Predicted Probability",
     ylab = "Observed Probability",
     main = "Calibration at 5 Years")
```

---

## Supplement Figure: Decision Curve Analysis

### R Code

```r
library(ggDCA)

# Fit models
fit_basic <- cph(Surv(TTRREM, REMISS) ~ IGF1I + VOLUME, data = adtte)
fit_full <- cph(Surv(TTRREM, REMISS) ~ IGF1I + VOLUME + BED + KNOSP + AGE, 
                data = adtte)

# Decision curve
dca(fit_full, 
    new.data = adtte,
    model.names = c("Full Model"),
    x.start = 0.05,
    x.stop = 0.5) +
  ggplot(aes(x = threshold, y = net.benefit)) +
  geom_line() +
  theme_minimal() +
  labs(x = "Threshold Probability",
       y = "Net Benefit",
       title = "Decision Curve Analysis")
```

---

## Supplement Figure: Love Plot (Covariate Balance)

### R Code

```r
library(ggplot2)

# SMD data
smd_data <- data.frame(
  variable = c("Age", "Sex", "IGF-1 Index", "Tumor Volume", 
               "Knosp Grade", "Prior Surgery", "Margin Dose", "BED"),
  SMD_before = c(0.45, 0.32, 0.58, 0.62, 0.38, 0.28, 0.51, 0.48),
  SMD_after = c(0.05, 0.03, 0.08, 0.07, 0.04, 0.06, 0.09, 0.08)
)

# Plot
ggplot(smd_data, aes(x = variable)) +
  geom_point(aes(y = SMD_before, color = "Before Weighting"), 
             size = 3, shape = 16) +
  geom_point(aes(y = SMD_after, color = "After Weighting"), 
             size = 3, shape = 17) +
  geom_hline(yintercept = 0.1, linetype = "dashed", color = "red") +
  geom_hline(yintercept = 0, linetype = "solid", color = "gray") +
  coord_flip() +
  theme_minimal() +
  labs(x = "Covariate",
       y = "Standardized Mean Difference",
       title = "Covariate Balance: Before vs After Overlap Weighting",
       color = "Weighting") +
  scale_color_manual(values = c("Before Weighting" = "#E74C3C", 
                               "After Weighting" = "#27AE60"))
```

---

## Export Figures to TIFF/EPS

```r
# Save as high-resolution TIFF
ggsave("Figure2_KM_Remission.tiff", 
       width = 8, height = 6, units = "in", dpi = 300, compression = "lzw")

ggsave("Figure4_Spline.tiff",
       width = 10, height = 5, units = "in", dpi = 300, compression = "lzw")
```

---

## SAS Code (Alternative)

### Kaplan–Meier Curves (SAS)

```sas
/* Kaplan-Meier for Remission */
proc lifetest data=adtte plots=survival(cl);
  time TTRREM * REMISS(0);
  strata &strata;
  run;

/* Add atrisk table */
proc lifetest data=adtte plots=survival(cb);
  time TTRREM * REMISS(0);
  strata &strata;
  run;
```

### Cox with Spline (SAS)

```sas
/* Restricted cubic spline */
proc phreg data=adtte;
  model TTRREM*REMISS(0) = rcs(IGF1I, 4) / risklimits;
  output out=spline_out xbeta=loghr lower=lower upper=upper / recast=cl;
run;

proc sgplot data=spline_out;
  band x=IGF1I lower=lower upper=upper / fillattrs=(color=gray transparency=0.7);
  series x=IGF1I y=loghr / lineattrs=(color=blue thickness=2);
  refline 0 / axis=y lineattrs=(pattern=dash);
run;
```

### Calibration Plot (SAS)

```sas
/* Using %calibration macro or %包子 */
%calibration(data=adtte, response=REMISS, predicted=pred, time=TTRREM, 
             nevent=50, nrefit=200)
```

---

## Figure Checklist Before Export

- [ ] All figures meet 300 DPI minimum
- [ ] Fonts are readable (8-10 pt minimum)
- [ ] Axes labeled clearly
- [ ] Legends complete
- [ ] Number at risk included for KM curves
- [ ] P-values formatted correctly
- [ ] Confidence intervals shown where appropriate
- [ ] TIFF/EPS format preferred

---

*Document created: 2026-03-21*
*Version: Figure Generation Code*
