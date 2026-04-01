"""
Neuro-Oncology Large-Scale Data Generation & Training
Target: 100,000 patients
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support, confusion_matrix
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

print("=== Generating 100K Neuro-Oncology Data ===")

# ==============================
# Generate 100K patients
# ==============================
n_total = 100000

# Distribution (approx real-world)
tumor_dist = {
    'Glioblastoma': 0.20,      # 20,000
    'Diffuse Glioma': 0.25,    # 25,000
    'Meningioma': 0.30,         # 30,000
    'Pituitary Adenoma': 0.15, # 15,000
    'Medulloblastoma': 0.05,    # 5,000
    'Other CNS': 0.05           # 5,000
}

data = []
for tumor, prop in tumor_dist.items():
    n = int(n_total * prop)
    
    # Demographics
    if tumor == 'Medulloblastoma':
        ages = np.random.randint(3, 25, n)
    elif tumor == 'Pituitary Adenoma':
        ages = np.random.randint(20, 65, n)
    else:
        ages = np.random.randint(18, 80, n)
    
    sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
    
    # Clinical
    kps = np.random.choice([50, 60, 70, 80, 90, 100], n, 
                           p=[0.08, 0.15, 0.25, 0.3, 0.17, 0.05])
    
    # Molecular (tumor-specific)
    if tumor in ['Glioblastoma', 'Diffuse Glioma']:
        mgmt = np.random.choice([0, 1], n, p=[0.4, 0.6])
        idh = np.random.choice([0, 1], n, p=[0.45, 0.55])
    else:
        mgmt = np.random.choice([0, 1], n, p=[0.9, 0.1])
        idh = np.random.choice([0, 1], n, p=[0.9, 0.1])
    
    # Treatment
    if tumor == 'Glioblastoma':
        trt = np.random.choice(['Surgery+RT+TMZ', 'Surgery+RT', 'RT+TMZ'], n, p=[0.5, 0.3, 0.2])
    elif tumor == 'Meningioma':
        trt = np.random.choice(['Surgery', 'Surgery+RT', 'RT', 'Observation'], n, p=[0.65, 0.2, 0.1, 0.05])
    else:
        trt = np.random.choice(['Surgery+RT', 'Surgery', 'RT'], n, p=[0.5, 0.35, 0.15])
    
    # EOR
    eor = np.random.choice(['GTR', 'STR', 'Biopsy'], n, p=[0.35, 0.4, 0.25])
    
    # Labs
    ldh = np.random.lognormal(4.8, 0.5, n).clip(100, 1000).round(1)
    alb = np.random.normal(4, 0.5, n).clip(2.5, 5.5).round(1)
    
    # Complications
    seizures = np.random.choice([0, 1], n, p=[0.7, 0.3])
    edema = np.random.choice([0, 1], n, p=[0.6, 0.4])
    
    # Imaging features
    tumor_vol = np.random.lognormal(3, 1.2, n).clip(0.1, 150).round(1)
    edema_vol = np.random.lognormal(2.5, 1, n).clip(0, 80).round(1)
    enhancement = np.random.choice(['None', 'Mild', 'Moderate', 'Strong'], n, p=[0.2, 0.3, 0.35, 0.15])
    
    # Response
    if tumor == 'Glioblastoma':
        resp = np.random.choice(['CR', 'PR', 'SD', 'PD'], n, p=[0.05, 0.15, 0.35, 0.45])
    else:
        resp = np.random.choice(['CR', 'PR', 'SD', 'PD'], n, p=[0.15, 0.3, 0.35, 0.2])
    
    # Survival (months) - tumor specific
    os_base = {'Glioblastoma': 12, 'Diffuse Glioma': 36, 'Meningioma': 120, 
               'Pituitary Adenoma': 180, 'Medulloblastoma': 60, 'Other CNS': 48}
    
    os = []
    for t, e in zip(trt, eor):
        base = np.random.exponential(os_base.get(tumor, 24))
        
        # Treatment effect
        if 'TMZ' in t: base *= 0.75
        if 'RT' in t: base *= 0.85
        
        # EOR effect  
        if e == 'GTR': base *= 0.6
        elif e == 'STR': base *= 0.8
        
        base = min(base * np.random.uniform(0.6, 1.4), 120)
        os.append(round(base, 1))
    
    event = [1 if o < 60 else 0 for o in os]
    
    # 12-month survival (target)
    surv_12m = (np.array(os) >= 12).astype(int)
    
    df = pd.DataFrame({
        'SUBJID': [f"NEURO{i:06d}" for i in range(1, n+1)],
        'TUMOR': tumor, 'AGE': ages, 'SEX': sexes, 'KPS': kps,
        'MGMT': mgmt, 'IDH': idh, 'TREATMENT': trt, 'EOR': eor,
        'LDH': ldh, 'ALBUMIN': alb, 'SEIZURES': seizures, 'EDEMA': edema,
        'TUMOR_VOL': tumor_vol, 'EDEMA_VOL': edema_vol, 'ENHANCEMENT': enhancement,
        'RESPONSE': resp, 'OS_MONTHS': os, 'EVENT': event, 'SURV_12M': surv_12m
    })
    data.append(df)

df = pd.concat(data, ignore_index=True)
print(f"Generated: {len(df)} patients")

# Save
df.to_csv('neuro_100k_data.csv', index=False)
print("Saved to: neuro_100k_data.csv")

# ==============================
# ML Training
# ==============================
print("\n=== Training Models on 100K Data ===")

# Prepare features
le = LabelEncoder()
df['TUMOR_ENC'] = le.fit_transform(df['TUMOR'])
df['TRT_ENC'] = le.fit_transform(df['TREATMENT'])
df['EOR_ENC'] = le.fit_transform(df['EOR'])
df['ENH_ENC'] = le.fit_transform(df['ENHANCEMENT'])

feats = ['AGE', 'KPS', 'MGMT', 'IDH', 'LDH', 'ALBUMIN', 'SEIZURES', 'EDEMA',
         'TUMOR_VOL', 'EDEMA_VOL', 'TUMOR_ENC', 'TRT_ENC', 'EOR_ENC', 'ENH_ENC']

X = df[feats].fillna(df[feats].median())
y = df['SURV_12M']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Train models
print("\n--- Model Training ---")
results = {}

for name, model in [
    ('Logistic Regression', LogisticRegression(max_iter=1000)),
    ('Random Forest', RandomForestClassifier(n_estimators=200, max_depth=15, n_jobs=-1)),
    ('Gradient Boosting', GradientBoostingClassifier(n_estimators=200, max_depth=8))
]:
    print(f"Training {name}...")
    model.fit(X_train_s, y_train)
    
    y_pred = model.predict(X_test_s)
    y_proba = model.predict_proba(X_test_s)[:, 1]
    
    auc = roc_auc_score(y_test, y_proba)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
    
    cv = cross_val_score(model, X_train_s, y_train, cv=5, scoring='roc_auc').mean()
    
    print(f"  AUC: {auc:.4f} | CV: {cv:.4f} | F1: {f1:.4f}")
    
    results[name] = {'auc': auc, 'cv': cv, 'f1': f1, 'model': model}

# ==============================
# Feature Importance
# ==============================
print("\n--- Feature Importance (GB) ---")
gb = results['Gradient Boosting']['model']
imp = pd.DataFrame({'Feature': feats, 'Importance': gb.feature_importances_}).sort_values('Importance', ascending=False)
print(imp.head(10).to_string(index=False))

imp.to_csv('neuro_100k_feature_importance.csv', index=False)

# ==============================
# Summary
# ==============================
print("\n=== Results Summary ===")
print(f"Dataset: {len(df):,} patients")
print(f"Events: {y.sum():,} ({y.mean()*100:.1f}%)")

print("\nModel Performance:")
for name, res in results.items():
    print(f"  {name}: AUC={res['auc']:.4f}, CV={res['cv']:.4f}")

print("\n✅ Training Complete!")
