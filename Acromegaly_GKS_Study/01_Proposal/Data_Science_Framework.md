# 数据科学框架完整分析

## Data Science Framework Analysis

---

## 1. 这个Study在数据科学上到底是什么问题

### 本质：四类问题混合

| 类别 | 内容 |
|------|------|
| **第一类：描述性与预后研究** | remission rate, tumor control rate, hypopituitarism incidence, recurrence rate |
| **第二类：时间到事件预测** | time to endocrine remission, time to recurrence, PFS, time to hypopituitarism |
| **第三类：治疗策略比较** | early vs delayed GKS, targeted vs whole-sella, medication hold vs no hold, high vs low BED |
| **第四类：个体化预测** | dynamic prediction model, individualized prediction |

---

## 2. 核心挑战

### 挑战1：样本量大概率不大

- 海绵窦侵犯型 + Gamma Knife 多中心回顾性
- 总样本数有限
- 事件数更少
- 真正 durable remission 事件可能不多
- toxicity 更少

> 首先不是"模型多复杂"，而是**事件数够不够支撑建模**

---

### 挑战2：多中心异质性

| 异质性来源 | 具体表现 |
|------------|----------|
| 内分泌标准 | 不同参考范围 |
| 手术哲学 | 切除程度不同 |
| 影像判读 | Knosp分级主观性 |
| 放疗计划 | 剂量策略不同 |
| 随访频率 | 数据完整度差异 |
| 药物策略 | medication hold 不一致 |

> 数据不是 i.i.d.，需考虑 **center effect, clustering**

---

### 挑战3：治疗不是随机分配

| 偏倚来源 | 例子 |
|----------|------|
| 选择偏倚 | 高危病人更可能早做 GKS |
| 剂量偏倚 | 大残余更可能 whole-sella |
| 药物偏倚 | 激素高的人更可能停药 |
| 解剖偏倚 | 靠近 optic apparatus 剂量更保守 |

> 直接比较 "hold vs no hold" 或 "whole-sella vs targeted" 容易把"医生选择偏好"误当成治疗效果

---

### 挑战4：终点有竞争与依赖关系

| 关系 | 说明 |
|------|------|
| remission → recurrence | 有顺序关系 |
| pituitary insufficiency | 可能在 remission 前后发生 |
| salvage therapy | 改变后续风险 |
| death | 虽少，但属于 competing risk |

> 终点之间**不是独立的**

---

### 挑战5：变量缺失与测量不一致

| 变量 | 问题 |
|------|------|
| OGTT | 不是所有病人都有 |
| IGF-1 | reference range 中心不同 |
| BED | 有的能算，有的不能 |
| tumor volume | 有的精确，有的只有径线 |
| Knosp grading | 主观性差异 |

> **数据预处理和 harmonization 非常关键**

---

## 3. 传统统计分析框架

### A. 数据标准化和队列定义

#### 需要统一的定义

| 项目 | 定义 |
|------|------|
| index date | 首次 GKS 日期 |
| baseline hormone window | 离 GKS 最近的 pre-GKS hormone |
| follow-up windows | 随访时间窗 |
| remission definition | 缓解定义 |
| recurrence definition | 复发定义 |
| hypopituitarism definition | 垂体功能减退定义 |
| progression definition | 进展定义 |

> **IGF-1 不应直接用原值，应优先用 IGF-1 index = IGF-1 / ULN**

---

### B. 描述性分析

#### 需要呈现的变量

- age, sex
- prior surgery count
- primary vs adjuvant GKS
- Knosp grade
- tumor volume
- baseline GH, IGF-1i
- medication use / hold
- margin dose, max dose, BED
- targeted vs whole-sella
- follow-up duration

#### 注意事项

- 非正态连续变量用 **median/IQR**
- 小样本下少用花哨检验
- center-by-center baseline distribution 也要看

---

### C. 生存分析

#### 主要模型

| 模型 | 应用 |
|------|------|
| Kaplan–Meier | time to remission, PFS, recurrence-free survival, time to hypopituitarism |
| Log-rank | 比较 early vs delayed GKS, hold vs no hold, targeted vs whole-sella |

> **注意**：KM 和 log-rank 是粗比较，受 confounding 影响很大

---

### D. Cox Proportional Hazards Model

#### 适合分析

- remission
- recurrence
- hypopituitarism

#### 候选协变量

- age
- sex
- baseline IGF-1i
- GH
- OGTT nadir GH
- tumor volume
- Knosp grade
- surgery-to-GKS interval
- medication hold
- targeted vs whole-sella
- margin dose
- isodose line
- **BED**

#### 建议注意点

1. **先检查事件数**，不要塞太多变量
2. 不要迷信单因素 p<0.10 才入模，更合理的是：临床先验 + 文献依据 + 事件数控制
3. ** penalized Cox 更稳**
4. 检查 PH assumption，某些变量可能不满足（如 medication hold, targeted vs whole-sella）
5. 考虑 **center frailty / mixed-effects Cox**

---

### E. Logistic Regression

#### 适用于

- new hypopituitarism
- visual toxicity
- cranial neuropathy
- salvage treatment need
- durable remission by fixed timepoint

#### 问题

随访时间长短差异明显时，直接 logistic 会偏

#### 解决

- 固定 **landmark time**
- 或优先用 **time-to-event model**

---

### F. 倾向评分 / 因果推断

#### 适合比较的暴露

- hold vs no hold
- targeted vs whole-sella
- early vs delayed GKS

#### 可用方法

- propensity score matching
- **IPTW** (逆概率加权)
- overlap weighting
- doubly robust model

#### 为什么重要

医生不会随机决定谁停药、谁 whole-sella

> 不做 adjustment，比较结果很可能是假象

#### 实操建议

样本如果不大，优先：**overlap weighting** 或 **stabilized IPTW**，比 PSM 更省样本

---

### G. Competing Risks / Multi-state

#### 如果数据足够好

这是更高级也更贴切的框架

#### Competing Risks

| 场景 | 方法 |
|------|------|
| recurrence 前可能先 salvage treatment | Fine-Gray |
| hypopituitarism 可能和其他事件竞争 | cause-specific hazard model |

#### Multi-state Model

最贴近临床路径：

| 状态 | 说明 |
|------|------|
| post-GKS, not in remission | 未缓解 |
| endocrine remission | 缓解 |
| recurrence | 复发 |
| salvage therapy | 补救治疗 |
| hypopituitarism | 垂体功能减退 |
| death | 死亡 |

> 比单一 endpoint 更真实，但要求数据质量高

---

## 4. 机器学习方法

### A. ML 最合适做什么

| 任务 | 说明 |
|------|------|
| **个体化风险预测** | 给定基线特征，预测未来概率 |
| **非线性与交互发现** | dose-volume 可能非线性，BED 效应可能受 hold 修饰 |
| **分层** | 发现不同 phenotype |

---

### B. 适合的ML方法

#### 1. Regularized Regression (第一梯队)

| 方法 | 优点 |
|------|------|
| LASSO | 变量选择 |
| Elastic Net | 稳 |
| Ridge | 抗过拟合 |
| penalized Cox | 小样本医学数据最合适 |

#### 2. Tree-based Models

| 方法 | 应用 |
|------|------|
| Random Forest | fixed time binary prediction |
| XGBoost | risk stratification |
| LightGBM | - |

> 前提：样本量别太小，否则容易过拟合

#### 3. Survival ML

| 方法 | 应用 |
|------|------|
| Random Survival Forest | time to remission/recurrence/hypopituitarism |
| Survival XGBoost | - |
| DeepSurv | 样本规模有限时未必合适 |

> 如果样本规模有限，优先：**RSF** 或 **penalized Cox**

#### 4. Unsupervised Learning

| 方法 | 应用 |
|------|------|
| hierarchical clustering | patient phenotypes |
| latent class analysis | treatment-response subgroups |
| UMAP + clustering | 探索性分析 |

> 只能作为**探索性分析**，不能当主结果

---

## 5. 传统统计 vs ML

### 传统统计更适合回答

- 哪些变量与 remission 相关
- 哪种 treatment strategy 看起来更优
- Hazard ratio 是多少
- 结果是否可解释、可发表、可审稿

### ML 更适合回答

- 给某个具体病人，风险多大
- 是否存在复杂非线性
- 变量交互是否重要
- 能否做临床决策支持工具

---

## 6. 最靠谱的分析路线

### 第一层：临床发表主分析

用传统统计完成：
- cohort description
- KM
- Cox
- logistic
- **IPTW / matching sensitivity analyses**

> 这是 paper 的主体，最容易被临床接受

---

### 第二层：预测建模

#### 模型候选

| 模型 | 变量 |
|------|------|
| baseline clinical model | 基础临床变量 |
| clinical + endocrine model | +内分泌 |
| clinical + endocrine + imaging model | +影像 |
| full multimodal model | +放疗参数 |

#### 比较指标

- C-index
- time-dependent AUC
- Brier score
- calibration slope
- calibration plot

> 看增加 BED、plan type、hold 等变量后，预测是否提高

---

### 第三层：解释性ML

用：
- **SHAP**
- partial dependence
- variable importance

解释：
- IGF-1i 在什么区间风险陡增
- BED 到哪个点后收益平台化
- volume 和 toxicity 的关系是否非线性

---

## 7. 最值得做的三个ML模型

### 模型1：Durable Remission Prediction

| 项目 | 内容 |
|------|------|
| 目标 | 预测病人最终是否达到 durable remission |
| 输入 | baseline endocrine + imaging + treatment + dosimetry |
| 意义 | 临床最关心 |

---

### 模型2：Time-to-Remission Model

| 项目 | 内容 |
|------|------|
| 目标 | 预测多快能缓解 |
| 方法 | penalized Cox / RSF |
| 意义 | 帮助患者咨询和随访计划 |

---

### 模型3：Toxicity Risk Model

| 项目 | 内容 |
|------|------|
| 目标 | 预测 hypopituitarism / cranial toxicity |
| 意义 | 权衡疗效与安全性，最接近临床决策 |

---

## 8. 最容易犯的数据科学错误

| 错误 | 说明 |
|------|------|
| ❌ 小样本做成"大模型" | 变量一堆，事件很少，全是假阳性 |
| ❌ 忽视时间信息 | 所有结局二分类化，丢掉 time-to-event 结构 |
| ❌ 把治疗比较当预测问题 | 用 XGBoost 发现 hold 重要就说有因果作用 |
| ❌ 忽视中心差异 | 多中心资料直接合并，不处理 center effect |
| ❌ 只看 discrimination 不看 calibration | AUC 高不代表临床可用 |
| ❌ 缺失值随便删 | OGTT、BED、体积缺失不随机，complete-case 严重偏 |

---

## 9. 完整数据科学框架

### Step 1: Data Harmonization

- 统一变量定义
- 统一 endpoint
- 统一单位
- 统一时间锚点

### Step 2: Missingness Audit

- 缺失比例
- 缺失机制
- 是否多重插补

### Step 3: Descriptive + Center Heterogeneity

- baseline summary
- by-center variation
- outcome variation

### Step 4: Main Inferential Models

- KM / log-rank
- Cox
- logistic
- **IPTW / overlap weighting** sensitivity analyses

### Step 5: Predictive Modeling

- penalized Cox
- RSF
- XGBoost at fixed horizon

### Step 6: Internal Validation

- bootstrap
- repeated cross-validation
- optimism correction

### Step 7: Model Explanation

- SHAP / variable importance
- calibration plots
- clinical risk groups

### Step 8: Deliverable

- nomogram or web calculator
- low / medium / high risk schema

---

## 10. 一句话总结

> 从数据科学角度，这个 study 不是一个简单的回顾性分析，而是一个：
> 
> **多中心，小样本，带治疗选择偏倚的生存预测与策略评估问题**
> 
> 最好的技术路线不是只用传统统计，也不是盲目上 ML，而是：
> 
> **用传统统计做可解释的临床推断，用 ML 做个体化风险预测和非线性关系挖掘**

---

*Document created: 2026-03-21*
