"""
Expanded External Data + ML Training Pipeline
10 tumor types with comprehensive features
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

# ==============================
# Create 10 tumor types
# ==============================
print("=== Creating Expanded Dataset (10 Tumors) ===")

tumor_configs = {
    'DLBCL': {'n': 500, 'pd1_rate': 0.6, 'irae_rate': 0.30},
    'NSCLC': {'n': 800, 'pd1_rate': 0.70, 'irae_rate': 0.25},
    'Melanoma': {'n': 600, 'pd1_rate': 0.85, 'irae_rate': 0.40},
    'Breast': {'n': 700, 'pd1_rate': 0.25, 'irae_rate': 0.15},
    'CRC': {'n': 550, 'pd1_rate': 0.35, 'irae_rate': 0.12},
    'Gastric': {'n': 450, 'pd1_rate': 0.40, 'irae_rate': 0.18},
    'Renal': {'n': 400, 'pd1_rate': 0.75, 'irae_rate': 0.35},
    'Bladder': {'n': 350, 'pd1_rate': 0.55, 'irae_rate': 0.22},
    'HeadNeck': {'n': 400, 'pd1_rate': 0.60, 'irae_rate': 0.28},
    'HCC': {'n': 350, 'pd1_rate': 0.45, 'irae_rate': 0.20}
}

all_data = []

for tumor, cfg in tumor_configs.items():
    n = cfg['n']
    pd1_rate = cfg['pd1_rate']
    irae_rate = cfg['irae_rate']
    
    # Core features
    ages = np.random.randint(25, 85, n)
    sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
    ecog = np.random.choice([0, 1, 2, 3], n, p=[0.4, 0.35, 0.2, 0.05])
    stage = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.1, 0.2, 0.3, 0.4])
    
    # Labs
    ldh = np.random.lognormal(5.2, 0.6, n).clip(100, 2000).round(1)
    hgb = np.random.normal(12, 2, n).clip(6, 18).round(1)
    alb = np.random.normal(4, 0.5, n).clip(2, 5.5).round(1)
    wbc = np.random.normal(7, 2, n).clip(3, 15).round(1)
    plt = np.random.normal(250, 80, n).clip(100, 500).round(0)
    
    # Biomarker
    biomarker = np.random.choice([0, 1], n, p=[0.7, 0.3])
    prior_lines = np.random.choice([0, 1, 2, 3], n, p=[0.4, 0.35, 0.15, 0.1])
    
    # Treatment
    trt = np.random.choice(['PD-1', 'Chemo', 'Target'], n, p=[pd1_rate, 1-pd1_rate-0.1, 0.1])
    
    # Response (PD-1 only)
    response = []
    for t in trt:
        if t == 'PD-1':
            response.append(np.random.choice(['CR', 'PR', 'SD', 'PD'], p=[0.12, 0.25, 0.35, 0.28]))
        else:
            response.append(np.random.choice(['CR', 'PR', 'SD', 'PD'], p=[0.05, 0.15, 0.35, 0.45]))
    
    # irAE
    irae = [np.random.choice([0,1,2,3,4], p=[1-irae_rate, irae_rate*0.6, irae_rate*0.25, irae_rate*0.1, irae_rate*0.05]) if t=='PD-1' else 0 for t in trt]
    
    # OS
    stage_mult = {'I': 3.0, 'II': 2.2, 'III': 1.5, 'IV': 1.0}
    os_months = [min(round(np.random.exponential(15)*stage_mult.get(s,1)* (0.7 if tr=='PD-1' else 1.0)*np.random.uniform(0.7,1.3), 1), 60) 
                 for tr, s in zip(trt, stage)]
    event = [1 if o < 48 else 0 for o in os_months]
    
    df = pd.DataFrame({
        'SUBJID': [f"{tumor[:3].upper()}{i:05d}" for i in range(1, n+1)],
        'TUMOR': tumor, 'AGE': ages, 'SEX': sexes, 'ECOG': ecog, 'STAGE': stage,
        'LDH': ldh, 'HGB': hgb, 'ALB': alb, 'WBC': wbc, 'PLT': plt,
        'BIOMARKER': biomarker, 'PRIOR_LINES': prior_lines,
        'TRT': trt, 'RESP': response, 'IRAE': irae, 'OS': os_months, 'EVENT': event
    })
    all_data.append(df)

df = pd.concat(all_data, ignore_index=True)
df.to_csv('expanded_10_tumor.csv', index=False)

print(f"\nData: {len(df)} patients, {df['TUMOR'].nunique()} tumors")

# ==============================
# ML Training
# ==============================
print("\n=== ML Training ===")

# Filter PD-1
pd1 = df[df['TRT']=='PD-1'].copy()

# Encode
le = LabelEncoder()
pd1['STAGE_ENC'] = le.fit_transform(pd1['STAGE'])
pd1['RESP_BIN'] = pd1['RESP'].isin(['CR', 'PR']).astype(int)

# Features
feats = ['AGE', 'ECOG', 'LDH', 'HGB', 'ALB', 'WBC', 'PLT', 'BIOMARKER', 'PRIOR_LINES', 'IRAE', 'STAGE_ENC']
X = pd1[feats].fillna(pd1[feats].median())
y = pd1['RESP_BIN']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Models
print("\nTraining models...")
results = {}
for name, model in [
    ('LR', LogisticRegression(max_iter=1000)),
    ('RF', RandomForestClassifier(n_estimators=100, max_depth=10)),
    ('GB', GradientBoostingClassifier(n_estimators=100, max_depth=5))
]:
    model.fit(X_train_s, y_train)
    auc = roc_auc_score(y_test, model.predict_proba(X_test_s)[:,1])
    cv = cross_val_score(model, X_train_s, y_train, cv=5, scoring='roc_auc').mean()
    print(f"{name}: AUC={auc:.3f}, CV={cv:.3f}")
    results[name] = {'auc': auc, 'cv': cv}

# Feature importance (GB)
gb = GradientBoostingClassifier(n_estimators=100)
gb.fit(X_train_s, y_train)
imp = pd.DataFrame({'Feature': feats, 'Importance': gb.feature_importances_}).sort_values('Importance', ascending=False)
print("\nTop Features:")
print(imp.head(8).to_string(index=False))

imp.to_csv('feature_importance.csv', index=False)
print("\n✅ Training complete!")
