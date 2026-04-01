"""
Neuro-Oncology: Efficient Training with 10K sample
Optimized for speed
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

print("=== Generating 10K Neuro Data (Efficient) ===")

# Generate 10K efficiently
n = 10000

# Distribution
tumors = ['Glioblastoma', 'Diffuse Glioma', 'Meningioma', 'Pituitary', 'Medulloblastoma']
probs = [0.20, 0.25, 0.30, 0.15, 0.10]

tumor = np.random.choice(tumors, n, p=probs)

# Demographics
ages = np.random.randint(18, 75, n)
sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
kps = np.random.choice([60, 70, 80, 90, 100], n, p=[0.15, 0.25, 0.35, 0.2, 0.05])

# Molecular
mgmt = np.random.choice([0, 1], n, p=[0.4, 0.6])
idh = np.random.choice([0, 1], n, p=[0.5, 0.5])

# Treatment
trt = np.random.choice(['Surgery+RT+TMZ', 'Surgery+RT', 'Surgery', 'RT'], n, p=[0.3, 0.35, 0.25, 0.1])
eor = np.random.choice(['GTR', 'STR', 'Biopsy'], n, p=[0.35, 0.4, 0.25])

# Labs
ldh = np.random.lognormal(4.8, 0.5, n).clip(100, 800).round(1)
alb = np.random.normal(4, 0.5, n).clip(2.5, 5.5).round(1)

# Imaging
tumor_vol = np.random.lognormal(3, 1, n).clip(1, 100).round(1)
edema_vol = np.random.lognormal(2.5, 0.8, n).clip(0, 50).round(1)

# Survival
os_months = []
for t, e in zip(trt, eor):
    base = np.random.exponential(18)
    if 'TMZ' in t: base *= 0.75
    if e == 'GTR': base *= 0.6
    elif e == 'STR': base *= 0.8
    os_months.append(round(min(base * np.random.uniform(0.7, 1.3), 60), 1))

event = [1 if o < 36 else 0 for o in os_months]
surv_12m = (np.array(os_months) >= 12).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'TUMOR': tumor, 'AGE': ages, 'SEX': sexes, 'KPS': kps,
    'MGMT': mgmt, 'IDH': idh, 'TRT': trt, 'EOR': eor,
    'LDH': ldh, 'ALBUMIN': alb, 'TUMOR_VOL': tumor_vol, 'EDEMA_VOL': edema_vol,
    'OS_MONTHS': os_months, 'EVENT': event, 'SURV_12M': surv_12m
})

# Save
df.to_csv('neuro_10k_data.csv', index=False)
print(f"Saved: {len(df)} patients")

# ==============================
# Training
# ==============================
print("\n=== Training Models ===")

# Encode
df_enc = pd.get_dummies(df, columns=['TUMOR', 'TRT', 'EOR'], drop_first=True)
feats = [c for c in df_enc.columns if c not in ['OS_MONTHS', 'EVENT', 'SURV_12M', 'SEX']]

X = df_enc[feats].fillna(0)
y = df_enc['SURV_12M']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Models
results = {}
for name, model in [
    ('LR', LogisticRegression(max_iter=500)),
    ('RF', RandomForestClassifier(n_estimators=100, max_depth=10)),
    ('GB', GradientBoostingClassifier(n_estimators=100, max_depth=6))
]:
    model.fit(X_train_s, y_train)
    auc = roc_auc_score(y_test, model.predict_proba(X_test_s)[:,1])
    results[name] = (model, auc)
    print(f"{name}: AUC = {auc:.4f}")

# Best model analysis
best_model, best_auc = max(results.items(), key=lambda x: x[1][1])
print(f"\nBest: {best_model} with AUC = {best_auc:.4f}")

# Feature importance
if hasattr(results['GB'][0], 'feature_importances_'):
    imp = pd.DataFrame({'Feature': feats, 'Importance': results['GB'][0].feature_importances_})
    imp = imp.sort_values('Importance', ascending=False).head(12)
    print("\nTop Features:")
    print(imp.to_string(index=False))
    imp.to_csv('neuro_10k_importance.csv', index=False)

# Summary report
print("\n=== Report ===")
print(f"Dataset: {len(df)}")
print(f"12-month survival rate: {y.mean()*100:.1f}%")
print(f"Best model AUC: {best_auc:.4f}")
print(f"Training features: {len(feats)}")

# Save report
report = f"""
# Neuro-Oncology Model Training Report
## Dataset
- Total patients: {len(df)}
- Features: {len(feats)}
- 12-month survival: {y.mean()*100:.1f}%

## Model Results
- Logistic Regression: AUC = {results['LR'][1]:.4f}
- Random Forest: AUC = {results['RF'][1]:.4f}
- Gradient Boosting: AUC = {results['GB'][1]:.4f}

## Best Model: {best_model} (AUC = {best_auc:.4f})

## Top Predictive Features
{imp.to_string(index=False)}

---
Generated: 2026-03-31
"""
with open('training_report.md', 'w') as f:
    f.write(report)

print("\n✅ Complete!")
