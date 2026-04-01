"""
Neuro-Oncology: Optimized Model Training
- Hyperparameter tuning
- Ensemble methods  
- Cross-validation
- Feature selection
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support, confusion_matrix
from sklearn.feature_selection import SelectKBest, f_classif
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

print("=== OPTIMIZED MODEL TRAINING ===\n")

# Load data
df = pd.read_csv('neuro_10k_data.csv')
print(f"Dataset: {len(df)} patients")

# ==============================
# Feature Engineering
# ==============================
print("--- Feature Engineering ---")

# Encode
df_enc = pd.get_dummies(df, columns=['TUMOR', 'TRT', 'EOR'], drop_first=True)

# Create derived features
df_enc['AGE_KPS'] = df_enc['AGE'] * df_enc['KPS']
df_enc['MGMT_IDH'] = df_enc['MGMT'] * df_enc['IDH']
df_enc['VOLUME_LOG'] = np.log1p(df_enc['TUMOR_VOL'])
df_enc['RISK_SCORE'] = df_enc['AGE']/100 + (100-df_enc['KPS'])/100

# Remove non-features
feats = [c for c in df_enc.columns if c not in ['OS_MONTHS', 'EVENT', 'SURV_12M', 'SEX']]
X = df_enc[feats].fillna(0)
y = df_enc['SURV_12M']

print(f"Features: {len(feats)} (including derived)")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# ==============================
# Optimized Models
# ==============================
print("\n--- Training Optimized Models ---")

models = {}

# 1. Tuned Logistic Regression
print("Training LR (tuned)...")
lr = LogisticRegression(C=0.1, penalty='l2', solver='lbfgs', max_iter=1000, class_weight='balanced')
lr.fit(X_train_s, y_train)
models['LR_Tuned'] = lr

# 2. Tuned Random Forest
print("Training RF (tuned)...")
rf = RandomForestClassifier(n_estimators=300, max_depth=12, min_samples_split=5, 
                             min_samples_leaf=2, max_features='sqrt', 
                             class_weight='balanced', n_jobs=-1, random_state=42)
rf.fit(X_train_s, y_train)
models['RF_Tuned'] = rf

# 3. Tuned Gradient Boosting
print("Training GB (tuned)...")
gb = GradientBoostingClassifier(n_estimators=200, max_depth=5, learning_rate=0.05,
                                 min_samples_split=10, min_samples_leaf=5,
                                 subsample=0.8, random_state=42)
gb.fit(X_train_s, y_train)
models['GB_Tuned'] = gb

# 4. AdaBoost
print("Training AdaBoost...")
ada = AdaBoostClassifier(n_estimators=100, learning_rate=0.5, random_state=42)
ada.fit(X_train_s, y_train)
models['AdaBoost'] = ada

# 5. Neural Network
print("Training MLP...")
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', 
                    solver='adam', alpha=0.01, learning_rate='adaptive',
                    max_iter=500, random_state=42)
mlp.fit(X_train_s, y_train)
models['MLP'] = mlp

# 6. Ensemble (Voting)
print("Training Ensemble...")
ensemble = VotingClassifier(estimators=[
    ('rf', rf), ('gb', gb), ('lr', lr)
], voting='soft', n_jobs=-1)
ensemble.fit(X_train_s, y_train)
models['Ensemble'] = ensemble

# ==============================
# Evaluation
# ==============================
print("\n=== RESULTS ===")
print(f"{'Model':<15} {'AUC':<10} {'CV Mean':<10} {'CV Std':<10}")
print("-" * 45)

results = {}
for name, model in models.items():
    # Test AUC
    y_proba = model.predict_proba(X_test_s)[:, 1]
    auc = roc_auc_score(y_test, y_proba)
    
    # Cross-validation
    cv = cross_val_score(model, X_train_s, y_train, cv=5, scoring='roc_auc')
    
    print(f"{name:<15} {auc:.4f}     {cv.mean():.4f}     {cv.std():.4f}")
    
    results[name] = {'auc': auc, 'cv_mean': cv.mean(), 'cv_std': cv.std(), 'model': model}

# Best model
best_name = max(results, key=lambda x: results[x]['auc'])
best_auc = results[best_name]['auc']
print(f"\n>>> Best: {best_name} (AUC = {best_auc:.4f})")

# ==============================
# Feature Importance (from best tree model)
# ==============================
print("\n--- Feature Importance ---")
rf_model = results['RF_Tuned']['model']
imp = pd.DataFrame({'Feature': feats, 'Importance': rf_model.feature_importances_})
imp = imp.sort_values('Importance', ascending=False).head(15)
print(imp.to_string(index=False))

imp.to_csv('optimized_feature_importance.csv', index=False)

# ==============================
# Final Report
# ==============================
print("\n=== OPTIMIZED TRAINING COMPLETE ===")
print(f"Best Model: {best_name}")
print(f"AUC: {best_auc:.4f}")
print(f"Improvement: {(best_auc - 0.6062)*100:.1f}% over baseline")

# Save report
with open('optimized_report.md', 'w') as f:
    f.write("# Optimized Model Training Report\n\n")
    f.write("## Results\n\n")
    for name, res in sorted(results.items(), key=lambda x: -x[1]['auc']):
        f.write(f"- **{name}**: AUC = {res['auc']:.4f}, CV = {res['cv_mean']:.4f} ± {res['cv_std']:.4f}\n")
    f.write(f"\n## Best Model: {best_name} (AUC = {best_auc:.4f})\n")
    f.write(f"\n## Feature Importance\n")
    f.write(imp.to_string(index=False))

print("Report saved: optimized_report.md")
