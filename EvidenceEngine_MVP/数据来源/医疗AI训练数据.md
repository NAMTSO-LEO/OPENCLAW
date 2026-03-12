# 医疗AI模型训练 - 公共数据来源

## 一、国际公共数据集

### 1. ICU/急诊数据

| 数据集 | 描述 | 申请方式 |
|--------|------|----------|
| **MIMIC-IV** | 美国ICU数据，4万+患者 | physionet.org 申请（需审核） |
| **eICU-CRD** | 多中心ICU数据 | MIT申请 |
| **CIBMTR** | 造血干细胞移植 | 需要合作 |

### 2. 专科数据

| 数据集 | 描述 | 访问 |
|--------|------|------|
| **ChestX-ray14** | 胸片14种疾病 | 公开下载 |
| **NIH Clinical Center** | 各类临床数据 | 申请 |
| **SEER** | 癌症登记数据 | 申请 |

### 3. 心血管数据

| 数据集 | 描述 |
|--------|------|
| **Framingham Heart Study** | 心血管队列研究 |
| **MIMIC-ECG** | 心电图数据 |

---

## 二、中国数据来源

### 1. 公开平台

| 平台 | 描述 |
|------|------|
| **丁香园** | 临床病例讨论 |
| **医脉通** | 医学知识库 |
| **万方/知网** | 医学文献 |

### 2. 官方数据

| 来源 | 描述 |
|------|------|
| **国家医保局** | 医保数据 |
| **CDC** | 传染病数据 |
| **裁判文书网** | 医疗纠纷案例 |

### 3. 医院合作

- 与医院建立科研合作
- 申请伦理审查后获取脱敏数据

---

## 三、快速获取数据方案

### 方案1：使用模拟数据（推荐先试）
```python
# 生成模拟患者数据
import numpy as np
import pandas as pd

n = 1000
data = pd.DataFrame({
    'age': np.random.randint(18, 90, n),
    'hr': np.random.randint(60, 150, n),
    'sbp': np.random.randint(90, 200, n),
    'troponin': np.random.choice([0, 1], n, p=[0.7, 0.3])
})
```

### 方案2：申请MIMIC-IV
1. 访问 physionet.org
2. 注册账号
3. 申请MIMIC-IV访问
4. 完成CITI培训（免费）
5. 审核1-2周

### 方案3：找医院合作
- 联系主任/科室
- 谈科研合作
- 申请伦理批件

---

## 四、数据预处理

### 常用库
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

### 标准流程
1. 数据清洗
2. 缺失值处理
3. 特征工程
4. 数据分割
5. 模型训练

---

## 五、下一步建议

1. **先用模拟数据** 把模型跑通
2. **申请MIMIC-IV** 作为正式训练数据
3. **找医院合作** 获取真实数据

---

*更新: 2026-03-12*
