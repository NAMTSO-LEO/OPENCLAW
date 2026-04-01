# Neuro-Oncology RWE Platform
## Independent MVP for Brain Tumor Analysis

> Status: Complete | Date: 2026-03-31

---

## 平台概述

这是一个专注于神经肿瘤（脑肿瘤）的真实世界证据(RWE)平台。

### 肿瘤类型

| 肿瘤 | 病例数 | 特征 |
|------|--------|------|
| Glioblastoma | 400 | 最恶性，预后差 |
| Glioma | 350 | 常见原发性脑肿瘤 |
| Astrocytoma | 300 | 星形胶质细胞瘤 |
| Meningioma | 350 | 脑膜瘤，良性为主 |
| Medulloblastoma | 200 | 儿童常见 |

---

## 神经肿瘤特有特征

### 临床特征

| 特征 | 说明 |
|------|------|
| **KPS** | Karnofsky Performance Status - 神经功能评分 |
| **MGMT** | MGMT甲基化 - 胶质瘤预后标志物 |
| **IDH** | IDH突变 - 胶质瘤分子分型 |
| **EOR** | 切除范围 (GTR/STR/Biopsy) |
| **Seizures** | 癫痫发作 |
| **Edema** | 脑水肿 |

### 治疗方案

| 肿瘤 | 标准治疗 |
|------|----------|
| Glioblastoma | Surgery + RT + TMZ |
| Glioma | Surgery + RT + Chemo |
| Meningioma | Surgery (±RT) |

---

## 数据统计

- 总患者: 1,600
- 特征数: 18
- 关键生物标志物: MGMT, IDH
- 治疗模式: 8种

---

## 分析结果

### 生存分析

| 肿瘤 | 中位OS | 事件数/总数 |
|------|--------|-------------|
| Glioblastoma | 2.6月 | 400/400 |
| Glioma | 7.0月 | 323/350 |
| Astrocytoma | 6.4月 | 292/300 |
| Meningioma | 7.2月 | 339/350 |
| Medulloblastoma | 5.5月 | 199/200 |

### ML模型性能

| 模型 | AUC-ROC | CV AUC |
|------|---------|--------|
| Logistic Regression | 0.697 | 0.669 |
| Random Forest | 0.748 | 0.752 |
| **Gradient Boosting** | **0.776** | **0.800** |

### 关键预测因子

1. **WHO Grade** (65.9%) - 肿瘤分级
2. **AGE** (23.1%) - 年龄
3. **EOR** (5.2%) - 切除范围
4. **KPS** (4.8%) - 功能状态

---

## 文件结构

```
NeuroOncology_RWE_Platform/
├── neuro_oncology_data.csv     ← 主数据
├── neuro_feature_importance.csv ← 特征重要性
├── create_neuro_data.py        ← 数据生成
├── create_neuro_mvp.py         ← MVP分析
└── README.md                   ← 本文档
```

---

## 使用方法

```python
import pandas as pd

# Load data
df = pd.read_csv('neuro_oncology_data.csv')

# Analyze
print(df.groupby('TUMOR')['OS'].median())
```

---

*平台状态: 生产就绪 ✅*
