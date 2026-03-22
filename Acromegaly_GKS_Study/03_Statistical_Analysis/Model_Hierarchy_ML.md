# Statistical Model Hierarchy - Complete ML/Statistical Models for GKRS Study

---

## 一、模型分层结构 (Model Hierarchy)

### 🟢 Tier 1: Primary (主分析 - 必须)

**目的**: 临床解释 + 发表核心结果

| 模型 | 用途 | 输出 |
|------|------|------|
| Cox regression | 时间结局核心 | HR, KM曲线, Nomogram |
| Logistic regression | Binary结局 | OR |
| LASSO Cox | 变量筛选 | 筛选后变量 |
| Elastic Net | 可选,共线性处理 | 筛选后变量 |

**适用终点**:
- durable remission
- time to remission
- hypopituitarism
- recurrence

**验证方法**:
- Bootstrap
- Cross-validation

---

### 🔵 Tier 2: Secondary (增强分析 - 加分)

**目的**: 提高预测能力 + 发现非线性 + 提供新意

| 模型 | 优点 | 适用场景 |
|------|------|----------|
| **XGBoost** | 自动处理非线性,自动建interaction | remission prediction |
| Random Forest (RF) | 稳定,变量重要性 | risk stratification |
| **Random Survival Forest (RSF)** | 不需要PH假设 | time to remission/toxicity |
| Gradient Boosting Survival | survival版XGBoost | 复杂时间结局 |

**输出**:
- C-index
- AUC
- Brier score
- SHAP values

**验证方法**:
- k-fold CV
- repeated CV
- bootstrap

---

### 🟣 Tier 3: Advanced/Exploratory (顶刊加分项)

**目的**: 机制探索 / 创新

| 模型 | 用途 |
|------|------|
| DeepSurv | survival DL模型,学复杂非线性 |
| Neural network survival | 替代Cox |
| Multimodal (CNN + clinical) | 如有影像数据 |
| Bayesian model | 小样本,prior knowledge |

**注意**: 不作为主结论,用于hypothesis generating

---

## 二、最佳模型组合 (Recommended for This Study)

### 🔥 主分析 (必须)

```
Cox + LASSO Cox
```

**输出**:
- HR
- p值
- KM曲线
- Nomogram

### 🔥 增强分析 (强烈推荐)

```
RSF + XGBoost
```

**输出**:
- C-index比较
- SHAP解释

### 🔥 创新分析 (可选)

```
DeepSurv
```

**放入Supplement**

---

## 三、模型任务 (Model Tasks)

### Task 1: 预测谁会remission

| 模型 |
|------|
| Cox |
| RSF |
| XGBoost |

### Task 2: 预测谁会hypopituitarism

| 模型 |
|------|
| Cox |
| Logistic |
| RSF |

### Task 3: 时间动态预测 (高级)

| 模型 |
|------|
| landmark Cox |
| RSF |

### Task 4: 找关键变量 (机制)

| 模型 |
|------|
| LASSO |
| SHAP |

---

## 四、变量角色 (Variable Roles)

### 核心变量 (必须进模型)
- IGF-1i
- BED
- medication hold
- timing

### 次要变量
- tumor volume
- Knosp
- dose
- optic dose

### Interaction (建议)
- IGF-1i × BED
- BED × hold
- timing × IGF-1i

*注: ML会自动学,但Cox你也可以加*

---

## 五、Methods原文 (Publication-Ready)

### 中文版

除传统Cox比例风险模型外，本研究还采用机器学习方法，包括随机生存森林（Random Survival Forest）和梯度提升模型（Gradient Boosting），以捕捉变量间的非线性关系和交互效应。模型性能采用一致性指数（C-index）、时间依赖性AUC和Brier评分进行评估，并通过重复交叉验证和Bootstrap进行内部验证。模型可解释性采用SHAP值进行评估。

### English Version

In addition to traditional Cox proportional hazards models, machine learning approaches including random survival forests and gradient boosting models were applied to capture nonlinear relationships and interactions among variables. Model performance was evaluated using concordance index, time-dependent AUC, and Brier score, with internal validation via repeated cross-validation and bootstrapping. Model interpretability was assessed using SHAP values.

---

## 六、模型对比 (Model Comparison)

| 模型 | 角色 | 优点 | 缺点 |
|------|------|------|------|
| Cox | 主分析 | 可解释 | 线性假设 |
| LASSO | 变量筛选 | 稳定 | 需再建模 |
| XGBoost | 非线性 | 强预测 | 黑盒 |
| RSF | survival ML | 无PH假设 | 解释较弱 |
| DeepSurv | DL | 最强表达 | 数据要求高 |

---

## 七、核心结论

**你的文章核心是"解释",不是"预测"。**

因此:

- **主分析必须是**: Cox + LASSO
- **ML只是**: 增强 + 解释复杂关系

---

## 八、完整分析流程

```
1. LASSO Cox → 筛选变量
         ↓
2. Cox回归 → 主分析(HR, p值, KM)
         ↓
3. RSF/XGBoost → 增强分析(C-index, SHAP)
         ↓
4. Nomogram → 临床应用
```

---

*Document completed: 2026-03-21*
*Ready for SAP integration*