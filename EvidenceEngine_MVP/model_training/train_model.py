"""
临床决策支持系统 - 模型训练
Evidence Engine ML Training Pipeline
训练疾病预测模型
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score
from sklearn.pipeline import Pipeline
import pickle
import warnings
warnings.filterwarnings('ignore')

# ===================== 数据生成 =====================

def generate_clinical_data(n_samples=10000, seed=42):
    """生成模拟临床数据"""
    np.random.seed(seed)
    
    data = []
    
    for _ in range(n_samples):
        # 随机生成患者
        age = np.random.randint(18, 90)
        gender = np.random.choice(['M', 'F'])
        
        # 基础生命体征
        hr = np.random.randint(50, 180)
        sbp = np.random.randint(80, 220)
        dbp = np.random.randint(50, 130)
        spo2 = np.random.randint(85, 100)
        rr = np.random.randint(12, 30)
        temp = np.random.uniform(36.0, 38.5)
        
        # 症状
        chest_pain = np.random.choice([0, 1], p=[0.7, 0.3])
        dyspnea = np.random.choice([0, 1], p=[0.6, 0.4])
        fever = np.random.choice([0, 1], p=[0.7, 0.3])
        palpitations = np.random.choice([0, 1], p=[0.7, 0.3])
        syncope = np.random.choice([0, 1], p=[0.8, 0.2])
        
        # 实验室检查
        glucose = np.random.randint(70, 250)
        wbc = np.random.uniform(4, 15)
        hemoglobin = np.random.uniform(10, 16)
        platelet = np.random.uniform(100, 400)
        creatinine = np.random.uniform(0.6, 1.5)
        
        # 心电图
        st_change = np.random.choice([0, 1], p=[0.8, 0.2])
        
        # 病史
        hypertension = np.random.choice([0, 1], p=[0.5, 0.5])
        diabetes = np.random.choice([0, 1], p=[0.6, 0.4])
        cad = np.random.choice([0, 1], p=[0.7, 0.3])
        afib = np.random.choice([0, 1], p=[0.8, 0.2])
        
        # 生成诊断标签（基于规则）
        label = generate_diagnosis(
            age, hr, sbp, chest_pain, dyspnea, fever,
            st_change, glucose, hypertension, diabetes
        )
        
        data.append({
            'age': age,
            'gender': gender,
            'hr': hr,
            'sbp': sbp,
            'dbp': dbp,
            'spo2': spo2,
            'rr': rr,
            'temp': temp,
            'chest_pain': chest_pain,
            'dyspnea': dyspnea,
            'fever': fever,
            'palpitations': palpitations,
            'syncope': syncope,
            'glucose': glucose,
            'wbc': wbc,
            'hemoglobin': hemoglobin,
            'platelet': platelet,
            'creatinine': creatinine,
            'st_change': st_change,
            'hypertension': hypertension,
            'diabetes': diabetes,
            'cad': cad,
            'afib': afib,
            'diagnosis': label
        })
    
    return pd.DataFrame(data)


def generate_diagnosis(age, hr, sbp, chest_pain, dyspnea, fever, st_change, glucose, hypertension, diabetes):
    """基于临床规则生成诊断"""
    
    # 不稳定胸痛 → ACS
    if chest_pain == 1 and st_change == 1:
        return 'ACS'
    
    # 发热 + 呼吸系统症状 → 感染
    if fever == 1 and dyspnea == 1:
        return 'Infection'
    
    # 心率快 + 心脏病史 → 心律失常
    if hr > 120 and (hypertension == 1 or diabetes == 1):
        return 'Arrhythmia'
    
    # 高血糖 → 糖尿病相关
    if glucose > 180:
        return 'Diabetes'
    
    # 老年 + 高血压 → 心衰
    if age > 65 and hypertension == 1 and dyspnea == 1:
        return 'HeartFailure'
    
    # 胸痛无ECG改变 → 其他
    if chest_pain == 1:
        return 'Other'
    
    # 默认
    return 'Normal'


def generate_tachycardia_data(n_samples=5000):
    """生成心动过速专项数据"""
    np.random.seed(123)
    
    data = []
    
    for _ in range(n_samples):
        age = np.random.randint(20, 80)
        gender = np.random.choice(['M', 'F'])
        hr = np.random.randint(100, 200)
        sbp = np.random.randint(80, 180)
        spo2 = np.random.randint(90, 100)
        
        # 症状
        chest_pain = np.random.choice([0, 1], p=[0.6, 0.4])
        dyspnea = np.random.choice([0, 1], p=[0.5, 0.5])
        syncope = np.random.choice([0, 1], p=[0.8, 0.2])
        palpitations = np.random.choice([0, 1], p=[0.3, 0.7])
        
        # ECG特征
        qrs_narrow = np.random.choice([0, 1], p=[0.2, 0.8])
        rhythm_regular = np.random.choice([0, 1], p=[0.3, 0.7])
        
        # 生成风险标签
        unstable = 0
        if sbp < 90 or chest_pain == 1 or syncope == 1:
            unstable = 1
        
        data.append({
            'age': age,
            'gender': gender,
            'hr': hr,
            'sbp': sbp,
            'spo2': spo2,
            'chest_pain': chest_pain,
            'dyspnea': dyspnea,
            'syncope': syncope,
            'palpitations': palpitations,
            'qrs_narrow': qrs_narrow,
            'rhythm_regular': rhythm_regular,
            'unstable': unstable  # 目标变量: 0=稳定, 1=不稳定
        })
    
    return pd.DataFrame(data)


# ===================== 模型训练 =====================

def train_stability_model(df):
    """训练稳定性预测模型"""
    
    # 准备特征
    feature_cols = ['age', 'hr', 'sbp', 'spo2', 'chest_pain', 'dyspnea', 
                   'syncope', 'palpitations', 'qrs_narrow', 'rhythm_regular']
    
    X = df[feature_cols].values
    y = df['unstable'].values
    
    # 分割数据
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 训练多个模型
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100)
    }
    
    results = {}
    best_model = None
    best_score = 0
    
    print("\n" + "="*60)
    print("模型训练结果")
    print("="*60)
    
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_proba = model.predict_proba(X_test_scaled)[:, 1]
        
        acc = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_proba)
        
        results[name] = {
            'accuracy': acc,
            'auc': auc,
            'model': model
        }
        
        print(f"\n{name}:")
        print(f"  准确率: {acc:.4f}")
        print(f"  AUC: {auc:.4f}")
        
        if auc > best_score:
            best_score = auc
            best_model = model
            best_name = name
    
    print(f"\n最佳模型: {best_name} (AUC={best_score:.4f})")
    
    # 特征重要性
    if hasattr(best_model, 'feature_importances_'):
        print("\n特征重要性:")
        importance = best_model.feature_importances_
        for col, imp in sorted(zip(feature_cols, importance), key=lambda x: -x[1]):
            print(f"  {col}: {imp:.4f}")
    
    return best_model, scaler, feature_cols


def train_diagnosis_model(df):
    """训练疾病诊断模型"""
    
    # 准备特征
    feature_cols = ['age', 'hr', 'sbp', 'dbp', 'spo2', 'glucose', 
                   'chest_pain', 'dyspnea', 'fever', 'st_change',
                   'hypertension', 'diabetes', 'cad']
    
    X = df[feature_cols].values
    
    # 编码标签
    le = LabelEncoder()
    y = le.fit_transform(df['diagnosis'])
    
    # 分割
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 训练
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # 评估
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    
    print("\n" + "="*60)
    print("疾病诊断模型")
    print("="*60)
    print(f"准确率: {acc:.4f}")
    print(f"\n诊断类别: {list(le.classes_)}")
    
    return model, scaler, le, feature_cols


# ===================== 主程序 =====================

def main():
    print("="*60)
    print("Evidence Engine - 临床决策模型训练")
    print("="*60)
    
    # 1. 生成数据
    print("\n[1/4] 生成训练数据...")
    
    # 心动过速数据
    tachy_df = generate_tachycardia_data(5000)
    print(f"  - 心动过速数据: {len(tachy_df)} 样本")
    print(f"  - 不稳定比例: {tachy_df['unstable'].mean():.2%}")
    
    # 综合疾病数据
    disease_df = generate_clinical_data(10000)
    print(f"  - 疾病数据: {len(disease_df)} 样本")
    
    # 2. 训练稳定性预测模型
    print("\n[2/4] 训练稳定性预测模型...")
    stability_model, stability_scaler, stability_features = train_stability_model(tachy_df)
    
    # 3. 训练诊断模型
    print("\n[3/4] 训练疾病诊断模型...")
    diagnosis_model, diagnosis_scaler, diagnosis_encoder, diagnosis_features = train_diagnosis_model(disease_df)
    
    # 4. 保存模型
    print("\n[4/4] 保存模型...")
    
    models = {
        'stability_model': stability_model,
        'stability_scaler': stability_scaler,
        'stability_features': stability_features,
        'diagnosis_model': diagnosis_model,
        'diagnosis_scaler': diagnosis_scaler,
        'diagnosis_encoder': diagnosis_encoder,
        'diagnosis_features': diagnosis_features
    }
    
    with open('models.pkl', 'wb') as f:
        pickle.dump(models, f)
    
    print("  - 模型已保存到: models.pkl")
    
    print("\n" + "="*60)
    print("训练完成!")
    print("="*60)
    
    return models


def predict_new_patient(patient_data, models):
    """预测新患者"""
    
    # 稳定性预测
    stability_features = models['stability_features']
    X_stability = np.array([[patient_data.get(f, 0) for f in stability_features]])
    X_stability = models['stability_scaler'].transform(X_stability)
    stability_pred = models['stability_model'].predict(X_stability)[0]
    stability_proba = models['stability_model'].predict_proba(X_stability)[0]
    
    result = {
        'stability': '不稳定' if stability_pred == 1 else '稳定',
        'stability_probability': f"{stability_proba[1]:.2%}"
    }
    
    return result


if __name__ == "__main__":
    main()
