# Method Modules

## 核心模块清单

### 1. Cohort Definition Module
```python
def define_cohort(adsl, inclusion_criteria, exclusion_criteria):
    """Define analysis cohort"""
    # Apply criteria
    pass
```

### 2. Baseline Covariate Module
```python
def get_baseline_covariates(adsl, vars):
    """Extract baseline covariates"""
    pass
```

### 3. Propensity Score Module
```python
def estimate_ps(data, treatment_var, covars, model='logistic'):
    """Estimate propensity score"""
    # Logistic / XGBoost / Neural Network
    pass
```

### 4. Weighting Module
```python
def compute_weights(ps, method='iptw', trim_percentile=[1, 99]):
    """Compute IPTW weights"""
    pass
```

### 5. Balance Diagnostics Module
```python
def check_balance(data, weights, covars):
    """Check covariate balance"""
    # SMD, ESS, Love Plot
    pass
```

### 6. Survival Analysis Module
```python
def survival_analysis(data, weights, time_var, event_var, method='cox'):
    """Run survival analysis"""
    # KM, Cox, Time-dependent Cox
    pass
```

### 7. Sensitivity Analysis Module
```python
def sensitivity_analysis(hr, ci_lower, ci_upper):
    """Compute E-value and sensitivity"""
    pass
```

### 8. Explainability Module
```python
def explain_model(model, X, method='shap'):
    """Explain model predictions"""
    pass
```

---

## 模块依赖关系

```
Cohort Definition
       ↓
Baseline Covariates
       ↓
Propensity Score → Weighting → Balance Diagnostics
       ↓                           ↓
    Survival Analysis ←←←←←←←←←
       ↓
Sensitivity Analysis
       ↓
  Explainability (if ML)
```

---

## MVP脚本结构

```
src/
├── preprocessing/
│   └── data_prep.py
├── causal/
│   ├── propensity_score.py
│   ├── weighting.py
│   └── diagnostics.py
├── survival/
│   ├── km_curve.py
│   ├── cox_model.py
│   └── time_dependent.py
├── ml/
│   └── prediction.py
└── reporting/
    └── evidence_package.py
```

---

## 使用示例: PD-1 Efficacy Analysis

```python
# 1. Define cohort
cohort = define_cohort(adsl, inclusion=['Stage III-IV'], exclusion=[])

# 2. Get baseline
baseline = get_baseline_covariates(cohort, ['AGE', 'SEX', 'STAGE', 'LDH'])

# 3. Estimate PS
ps = estimate_ps(cohort, 'TRTP', baseline, model='logistic')

# 4. Compute weights
weights = compute_weights(ps, method='iptw')

# 5. Check balance
balance = check_balance(cohort, weights, baseline)
print(f"SMD max: {balance['max_smd']}")

# 6. Run survival analysis
surv_result = survival_analysis(cohort, weights, 'AVAL', 'CNSR', method='cox')
print(f"HR: {surv_result['hr']}, 95% CI: {surv_result['ci']}")

# 7. Sensitivity
evalue = sensitivity_analysis(surv_result['hr'], surv_result['ci_lower'], surv_result['ci_upper'])
print(f"E-value: {evalue}")
```

---

*MVP Step 6 - Method modules defined*
