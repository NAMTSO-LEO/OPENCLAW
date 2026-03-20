# 建模变量体系与ADaM数据结构设计

---

## 一、核心建模变量体系

### 1. Baseline Demographics（人口学）

| Variable | Type | Notes |
|----------|------|-------|
| Age at GKS | Continuous | 可考虑非线性 (restricted cubic spline) |
| Sex | Binary | Male/Female |
| Center | Categorical | 用于 internal-external validation |

---

### 2. Endocrine Variables（核心变量 ⭐）

| Variable | Type | Notes |
|----------|------|-------|
| IGF-1 (absolute) | Continuous | log transform |
| **IGF-1 index (IGF-1i)** | Continuous | ⭐ 核心变量 |
| Baseline GH | Continuous | log transform |
| OGTT nadir GH | Continuous | 若缺失较多 → indicator |
| On medication at GKS | Binary | yes/no |
| Medication type | Categorical | SSA / Pegvisomant / Dopamine agonist |
| **Medication hold** | Binary | ⭐ 重点研究变量 |

---

### 3. Surgical Variables

| Variable | Type | Notes |
|----------|------|-------|
| Prior surgery | Binary | yes/no |
| Number of surgeries | Integer | optional |
| Extent of resection | Categorical | GTR / STR / unknown |
| **Interval surgery → GKS** | Continuous | ⭐ 关键预测因子 |

---

### 4. Tumor / Imaging Variables

| Variable | Type | Notes |
|----------|------|-------|
| **Tumor volume** | Continuous | log transform |
| **Knosp grade** | Ordinal | ⭐ 强预测因子 |
| Cavernous sinus laterality | Categorical | unilateral / bilateral |
| ICA encasement | Binary | optional |
| Residual location | Categorical | intracavernous vs mixed |
| Pre-GKS progression | Binary | optional |

---

### 5. Radiosurgical Variables（重点创新点）

| Variable | Type | Notes |
|----------|------|-------|
| **Margin dose** | Continuous | ⭐ |
| Maximum dose | Continuous | |
| Isodose line | Continuous | |
| Target coverage | Continuous | |
| Optic max dose | Continuous | toxicity |
| **BED** | Continuous | ⭐ 高级变量 |
| **Plan type** | Binary | targeted vs whole sella ⭐ |

---

### 6. Outcome Variables（统一编码）

#### Time-to-event

| Variable | Definition |
|----------|------------|
| Time to remission | GKS → remission |
| Time to recurrence | remission → recurrence |
| Time to hypopituitarism | GKS → event |
| Time to progression | imaging |

#### Binary

| Variable | Definition |
|----------|------------|
| Durable remission | yes/no |
| Endocrine control | yes/no |
| Hypopituitarism | yes/no |
| Visual toxicity | yes/no |
| Salvage therapy | yes/no |

---

## 二、Feature Engineering（特征工程）

### 1. 非线性处理（必须做）

| 原变量 | 转换 |
|--------|------|
| IGF-1 | log(IGF-1) |
| GH | log(GH) |
| Tumor volume | log(tumor volume) |

### 2. 分层变量（用于 KM + ML）

- IGF-1i high vs low (median / clinical cutoff)
- BED high vs low
- Early vs delayed GKS

### 3. 交互项（论文亮点）

| 交互项 | 说明 |
|--------|------|
| IGF-1i × BED | ⭐ |
| Tumor volume × margin dose | |
| Medication hold × IGF-1i | |
| Knosp × plan type | |

---

## 三、ADaM 数据结构（SAS-ready）

### 1. ADSL（Subject-Level Dataset）

每个患者一行

```
USUBJID
AGE
SEX
CENTER
IGF1
IGF1I
GH
OGTT_GH
MEDICATION
MED_HOLD
SURGERY
SURG_NUM
SURG_GKS_INT
TUMOR_VOL
KNOSP
PLAN_TYPE
MARGIN_DOSE
MAX_DOSE
ISODOSE
OPTIC_DOSE
BED
```

---

### 2. ADTTE（Time-to-event dataset）

```
USUBJID
PARAMCD     (REMISSION / RECURRENCE / HYPOPIT)
AVAL        (time)
CNSR        (0=event, 1=censored)
```

| PARAMCD | Meaning |
|---------|---------|
| TTR | time to remission |
| TTRC | time to recurrence |
| TTH | time to hypopituitarism |

---

### 3. ADLB（Longitudinal endocrine）

用于 dynamic model / joint model

```
USUBJID
AVISIT
ADT
IGF1
IGF1I
GH
```

---

### 4. ADOUT（Binary outcomes）

```
USUBJID
DURABLE_REMISSION
ENDO_CONTROL
HYPOPIT
VISUAL_TOX
SALVAGE
```

---

## 四、ML/DL 建模 Pipeline

```
Raw Data
    ↓
Preprocessing (missing, encoding)
    ↓
Feature Engineering (log, interactions)
    ↓
Train / Validation Split (or CV)
    ↓
Model Training
    - Cox / LASSO Cox (Primary)
    - XGBoost / RSF (ML)
    - DeepSurv (DL)
    ↓
Cross-validation (repeated k-fold / bootstrap)
    ↓
Performance Evaluation (C-index, AUC, Brier, DCA)
    ↓
Interpretation (SHAP, Variable Importance)
```

---

## 五、推荐模型组合（最优解）

### Primary（必须做）

| Model | Purpose |
|-------|---------|
| Cox multivariable | 临床推断, HR/OR |
| LASSO Cox | 变量筛选 |

### ML（强烈推荐）

| Model | Purpose |
|-------|---------|
| XGBoost | 预测增强 |
| Random Survival Forest | 非线性捕捉 |

### DL（探索）

| Model | Purpose |
|-------|---------|
| DeepSurv | 时间结局 |

---

## 六、发文亮点

⭐ **1. Cavernous sinus–specific cohort**（别人没有）
⭐ **2. BED + dosimetry**（放疗领域加分）
⭐ **3. Dynamic prediction model**（少有人做）
⭐ **4. Internal-external validation**（顶刊喜欢）

---

## 七、Figure 设计

| Figure | 内容 |
|--------|------|
| Figure 1 | Flowchart（纳入排除） |
| Figure 2 | Kaplan–Meier curves (remission, hypopituitarism) |
| Figure 3 | Nomogram（如果用 Cox） |
| Figure 4 | SHAP plot（ML解释） |
| Figure 5 | Calibration curve + DCA |

---

*设计日期: 2026-03-19*
