# AI/ML 预后模型设计

## 一、模型目标

### 1.1 预测任务
- **二分类**：伽玛刀治疗后 IGF-1 是否正常化
- **二分类**：肿瘤是否得到控制
- **时间到事件**：无进展生存期

### 1.2 预测时间点
- 治疗后 6 个月
- 治疗后 12 个月
- 治疗后 24 个月

---

## 二、特征变量

### 2.1 临床特征

| 特征 | 说明 | 类型 |
|------|------|------|
| AGE | 年龄 | 连续 |
| SEX | 性别 | 分类 |
| DURATION | 病程 | 连续 |
| PRE_SURG | 既往手术 | 二分类 |
| PRE_MED | 术前药物 | 二分类 |

### 2.2 肿瘤特征

| 特征 | 说明 | 类型 |
|------|------|------|
| TUMOR_SIZE | 肿瘤最大径 | 连续 |
| TUMOR_VOL | 肿瘤体积 | 连续 |
| KNOPSP | Knosp分级 | 有序分类 |
| CAVERNOUS | 海绵窦侵袭 | 二分类 |
| SUPRASELLAR | 鞍上扩展 | 二分类 |

### 2.3 激素特征

| 特征 | 说明 | 类型 |
|------|------|------|
| GH_BASE | 基线GH | 连续 |
| IGF1_BASE | 基线IGF-1 | 连续 |
| IGF1_RATIO | IGF-1/ULN比值 | 连续 |

### 2.4 放疗特征

| 特征 | 说明 | 类型 |
|------|------|------|
| DOSE_EDGE | 边缘剂量 | 连续 |
| DOSE_MAX | 最大剂量 | 连续 |
| TARGET_VOL | 靶区体积 | 连续 |
| TARGET_NUM | 靶区数量 | 连续 |

---

## 三、建模方法

### 3.1 基线模型
- Logistic Regression
- 优点：可解释性强

### 3.2 机器学习模型
- Random Forest
- XGBoost / LightGBM
- Support Vector Machine

### 3.3 生存分析
- Cox Proportional Hazards
- Random Survival Forest

---

## 四、模型构建流程

### Step 1: 数据预处理
```
- 缺失值处理（多重插补/删除）
- 连续变量标准化
- 分类变量编码
```

### Step 2: 特征选择
```
- LASSO 回归
- Random Forest 重要性
- XGBoost 重要性
- SHAP 贡献度
```

### Step 3: 模型训练
```
- 训练集/验证集划分（70/30）
- 交叉验证
- 超参数调优
```

### Step 4: 模型评估
```
- AUC / C-index
- 灵敏度 / 特异度
- 校准曲线
- DCA 决策曲线
```

### Step 5: 可解释性
```
- SHAP 值
- 特征重要性图
- 局部解释
```

---

## 五、评估指标

| 指标 | 说明 |
|------|------|
| AUC | 区分度 |
| C-index | 生存分析区分度 |
| 灵敏度 | 敏感度 |
| 特异度 | 特异性 |
| PPV | 阳性预测值 |
| NPV | 阴性预测值 |
| Brier Score | 校准度 |

---

## 六、验证策略

### 6.1 内部验证
- 简单划分（70%训练/30%验证）
- K折交叉验证（K=5或10）
- 时间分割验证

### 6.2 外部验证（如有条件）
- 多中心数据
- 外部公开数据集

---

## 七、代码框架（Python/PyCaret）

### 7.1 数据准备
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_excel('clinical_data.xlsx')

# 定义特征和目标
X = df[feature_cols]
y = df['IGF1_NORMAL']

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 7.2 模型训练（以XGBoost为例）
```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train_scaled, y_train)
```

### 7.3 评估
```python
from sklearn.metrics import roc_auc_score, classification_report

y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

print(classification_report(y_test, y_pred))
print('AUC:', roc_auc_score(y_test, y_pred_proba))
```

### 7.4 SHAP解释
```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test_scaled)

shap.summary_plot(shap_values, X_test)
```

---

## 八、预期产出

1. **预测模型**：可预测伽玛刀后 IGF-1 正常化概率
2. **特征重要性排名**：识别关键预后因素
3. **可解释性分析**：SHAP可视化
4. **Nomogram**：临床决策支持工具

---

## 九、注意事项

1. 样本量有限，避免过拟合
2. 优先使用临床可获得特征
3. 强调可解释性，不只是"黑箱"
4. 结果需临床验证后再应用
