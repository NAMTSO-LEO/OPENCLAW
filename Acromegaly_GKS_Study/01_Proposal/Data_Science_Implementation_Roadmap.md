# 数据科学实施路线图

## Data Science Implementation Roadmap

---

## 1. 项目目标

把这项 study 落成一个可分析的数据科学 pipeline，回答三类问题：

### 三类问题

| 类别 | 内容 |
|------|------|
| **描述/推断** | GKS 后 durable remission 率、tumor control 率、recurrence/hypopituitarism/toxicity 多少、哪些因素相关 |
| **策略比较** | early vs delayed GKS, medication hold vs no hold, targeted vs whole-sella, low vs high dose/BED |
| **个体化预测** | 谁更可能 remission、recurrence、hypopituitarism |

---

## 2. 分析单位

### 推荐主分析单位

- **Patient-level**
- **Index date = first eligible Gamma Knife radiosurgery date**

### 原因

- 终点大多围绕"首次纳入研究的 GKS 后"发生
- 避免 repeat SRS 把单位搞乱

### Repeat SRS 处理

- 主分析：作为 salvage treatment outcome
- 亚组分析：单独做 repeat-radiosurgery subanalysis

---

## 3. 数据库结构

### 3.1 ADSL：主体表

一人一行，放最核心 baseline 信息

| 变量 | 说明 |
|------|------|
| STUDYID | 研究编号 |
| USUBJID | 受试者ID |
| CENTER | 中心 |
| INDEXDT | 首次GKS日期 |
| AGE | 年龄 |
| SEX | 性别 |
| PRIMARY_GKS_FL | 是否初始GKS |
| PRIOR_SURGERY_N | 既往手术次数 |
| PRIOR_MED_TX_FL | 既往药物治疗 |
| FU_MONTHS | 随访月数 |
| KNOSP | Knosp分级 |
| CSI_DEF_TYPE | 海绵窦侵犯定义类型 |
| TARGET_PLAN_TYPE | 靶区类型 |
| MED_HOLD_FL | 停药标志 |
| EARLY_GKS_FL | 早期GKS标志 |
| WHOLESELLA_FL | 全鞍区标志 |

### 3.2 ADENDO：内分泌表

每次 endocrine assessment 一行

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| ASSESSDT | 评估日期 |
| AVISIT | 访视 |
| DAYS_FROM_GKS | 距GKS天数 |
| IGF1 | IGF-1值 |
| IGF1_ULN | IGF-1正常上限 |
| IGF1I | IGF-1指数 |
| GH | 生长激素 |
| OGTT_NADIR_GH | OGTT谷值GH |
| ON_MED_FL | 用药标志 |
| BIOCHEM_STATUS | 生化状态 |

### 3.3 ADRAD：放疗参数表

一人一行，或一次 GKS 一行

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| GKS_DATE | GKS日期 |
| MARGIN_DOSE | 边缘剂量 |
| MAX_DOSE | 最大剂量 |
| ISODOSE_LINE | 等剂量线 |
| OPTIC_MAX_DOSE | 视神经最大剂量 |
| TARGET_VOLUME_CC | 靶区体积 |
| BED | 生物有效剂量 |
| N_ISOCENTERS | 等中心数 |
| PLAN_TYPE | 计划类型 |

### 3.4 ADIMG：影像表

每次 MRI 一行

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| MRI_DATE | MRI日期 |
| DAYS_FROM_GKS | 距GKS天数 |
| TUMOR_VOL_CC | 肿瘤体积 |
| MRI_RESPONSE | MRI反应 |
| PROGRESSION_FL | 进展标志 |
| CAVERNOUS_RESIDUAL_FL | 海绵窦残留标志 |
| OPTIC_APPARATUS_DISTANCE | 视神经距离 |

### 3.5 ADAE：不良事件表

放所有相关 toxicity

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| AESTDTC | 事件日期 |
| AEDECOD | 标准术语 |
| AECAT | 事件分类 |
| AESER | 严重事件标志 |
| AEGRADE | 级别 |
| AE_REL_RAD | 放射相关 |
| AE_VISUAL_FL | 视觉毒性 |
| AE_CN_FL | 颅神经毒性 |
| AE_RN_FL | 放射性坏死 |

### 3.6 ADPIT：垂体轴功能表

因为 hypopituitarism 很关键，建议单独建

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| ASSESSDT | 评估日期 |
| AXIS | 垂体轴 |
| BASELINE_DEFICIT_FL | 基线缺陷标志 |
| NEW_DEFICIT_FL | 新发缺陷标志 |

### 3.7 ADINT：后续干预表

记录 salvage

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| INTDT | 干预日期 |
| INTTYPE | 干预类型 |

### 3.8 ADTTE：时间到事件分析表

最重要的分析表，每个 endpoint 一行

| 变量 | 说明 |
|------|------|
| USUBJID | 受试者ID |
| PARAMCD | 参数编码 |
| PARAM | 参数 |
| STARTDT | 起始日期 |
| ADT | 事件日期 |
| CNSR | 截尾标志 |
| AVAL | 数值 |
| EVNTDESC | 事件描述 |

---

## 4. Endpoint 定义

### 主终点 1：Durable Endocrine Remission

**推荐规则**（满足所有条件）：

1. IGF-1i <= 1.0
2. off medication
3. 若有 OGTT，则 nadir GH < 0.4
4. 后续随访未出现 recurrence

**实现上分两层：**

| 层 | 说明 |
|------|------|
| 层1 | 首次 remission - 第一次满足 remission 条件的日期 |
| 层2 | durable remission - 到末次随访都没 recurrence，才记为 durable |

> **注意**：durable 是"回顾确认型终点"，适合做 fixed follow-up status + time-to-first-remission 双轨分析

### 主终点 2：Endocrine Control

- IGF-1i <= 1.0
- on medication

> 最好作为状态，不一定做主 TTE 终点

### 主终点 3：Time to Endocrine Remission

- start = GKS date
- event = first biochemical remission date

### 主终点 4：Radiographic Control

- stable/decreased = control
- progressed = failure

如果有体积：
- progression = >20% increase

> 建议：binary at last follow-up，另做 TTPROG

### 次要终点

- recurrence after remission
- salvage treatment
- new hypopituitarism
- visual toxicity
- cranial neuropathy
- overall survival

---

## 5. 关键派生变量

### 激素负荷

- **IGF1I = IGF1 / ULN**
- baseline 取 GKS 前最近一次，建议窗口 90 天内优先，最多 180 天

### Baseline GH

- 同理取 GKS 前最近值

### Surgery to GKS Interval

- GKS date - last surgery date

### Early vs Delayed GKS

需要 protocol 先定 cutoff：
- 主分析建议 **12 months**
- 敏感性分析可试 6 months / median split

### Dose/BED Strata

- 优先按临床 cutoff
- 若无共识，可按 median 或 restricted cubic spline 后找合理节点

### Medication Hold

建议分类：
- no medication
- on medication, no hold
- on medication, held peri-GKS

> 而不是简单二分类，因为"不用药"和"用了没停"不是一回事

---

## 6. 缺失值处理

### Missingness Audit

- 每个核心变量缺失比例
- 按中心看缺失模式
- 看 outcome-related missingness

### 建议

**Complete-case 只做敏感性分析**

主分析不能太依赖 complete-case，尤其如果：
- OGTT
- BED
- tumor volume
缺失较多

**Multiple Imputation**

适合：
- baseline covariates
- non-monotone missing

不适合直接插补：
- event status
- event time

**建议：MICE + 分中心或含 center 变量插补**

---

## 7. 传统统计主分析

### A. 描述性统计

**输出 Table 1：总体 + 分组**

分组：
- targeted vs whole-sella
- hold vs no hold
- early vs delayed GKS

变量：
- age, sex
- baseline IGF1I, GH
- tumor volume
- Knosp
- prior surgery
- interval
- dose/BED
- follow-up

### B. Kaplan-Meier

**做这些曲线：**

- time to remission
- time to durable remission
- recurrence-free survival
- progression-free survival
- hypopituitarism-free survival

**分层：**
- early vs delayed
- targeted vs whole-sella
- hold vs no hold
- low vs high IGF1I
- low vs high BED

### C. Cox 回归

**建议做 3 个主模型：**

| 模型 | Outcome |
|------|---------|
| Model 1 | remission |
| Model 2 | recurrence |
| Model 3 | hypopituitarism |

**候选变量**
- age, sex
- IGF1I, baseline GH
- tumor volume, Knosp
- surgery_to_GKS_interval
- medication status
- plan type
- margin dose, optic max dose, BED
- center

**注意**
- 优先：penalized Cox 或限制每模型变量数量
- 中心处理：robust sandwich SE by center 或 frailty Cox

### D. Logistic 回归

**可做这些 fixed-horizon 终点：**
- 3-year remission
- 5-year durable remission
- any new hypopituitarism by 5 years
- any salvage treatment by 5 years

**前提：只纳入该 landmark 有充分随访的人**

### E. 策略比较：因果推断

**最值得做 3 个比较：**

| 比较 | 方法 |
|------|------|
| medication hold vs no hold | overlap weighting / IPTW / matching |
| targeted vs whole-sella | overlap weighting / IPTW / matching |
| early vs delayed GKS | overlap weighting / IPTW / matching |

**方法优先级：**
1. overlap weighting
2. IPTW
3. matching

**PS 模型变量**

必须纳入治疗选择相关的基线因素：
- age, sex
- IGF1I, GH
- tumor volume, Knosp
- prior surgery, interval
- center
- optic proximity if available
- baseline medication use

---

## 8. ML 部分

ML 不作为主论文唯一证据，而是做预测增强

### A. 预测任务定义

| Task | 说明 |
|------|------|
| Task 1 | 预测 5-year durable remission |
| Task 2 | 预测 time to remission |
| Task 3 | 预测 5-year hypopituitarism |

### B. 特征集分层

| 特征集 | 变量 |
|--------|------|
| Feature Set 1 | Clinical: age, sex, center |
| Feature Set 2 | + Endocrine: IGF1I, GH, OGTT |
| Feature Set 3 | + Imaging: tumor volume, Knosp, location |
| Feature Set 4 | + Treatment: interval, med hold, plan type |
| Feature Set 5 | Full: + dose/BED, optic dose |

### C. 模型候选

| 优先级 | 模型 |
|--------|------|
| 1 | penalized Cox / penalized logistic |
| 2 | RSF (Random Survival Forest) |
| 3 | XGBoost |

> 不建议一上来 deep learning

### D. 验证方式

不建议简单 train/test split（样本不大）

建议：
- bootstrap internal validation
- repeated k-fold CV
- optimism-corrected C-index

### E. 评估指标

**二分类**
- AUROC, AUPRC
- calibration slope, calibration-in-the-large
- Brier score

**生存模型**
- C-index
- time-dependent AUC
- integrated Brier score
- calibration at 3y / 5y

> **必须看 calibration，不能只看 AUC**

### F. 可解释性

- SHAP for XGBoost
- variable importance for RSF
- partial dependence / ALE

**重点看：**
- IGF1I 是否存在阈值效应
- BED 是否存在平台效应
- volume 是否与 toxicity 非线性相关
- med hold 是否与 baseline burden 交互

---

## 9. 分析顺序

### Phase 1：Data Lock 前

- 定义 CRF dictionary
- 统一中心变量字典
- endpoint charter
- missingness plan
- SAP draft

### Phase 2：Cleaning

- 单位统一
- 日期核查
- 重复记录核查
- logical consistency checks
- outcome adjudication

### Phase 3：Core Analysis

1. cohort flowchart
2. Table 1
3. KM
4. Cox/logistic
5. weighted sensitivity analyses

### Phase 4：Prediction Analysis

1. feature engineering
2. imputation inside resampling
3. model training
4. internal validation
5. calibration

### Phase 5：Deliverables

- 主论文图表
- supplement
- risk score / nomogram / calculator prototype

---

## 10. 最强图表组合

### Main Figures

1. Study flow diagram
2. KM for remission
3. KM for hypopituitarism
4. Forest plot of multivariable Cox
5. Weighted comparison plot: targeted vs whole-sella / hold vs no hold
6. Calibration plot of prediction model

### Main Tables

1. Baseline characteristics
2. Outcome summary
3. Multivariable remission model
4. Multivariable toxicity model
5. Prediction model performance

---

## 11. 最容易卡住的点

| 点 | 说明 |
|------|------|
| 1 | remission 定义不统一 - on/off medication, OGTT availability, lab range differences |
| 2 | BED 质量不一致 - 提前决定能算多少例，是否作为 exploratory only |
| 3 | 随访不规则 - 影响 fixed-horizon outcome |
| 4 | center heterogeneity 太强 - 提前计划 center adjustment |
| 5 | 事件数不够 - 最后可能做不了太复杂模型 |

---

## 12. 最终实用分析蓝图

### Primary Inferential Package

- KM + Cox for remission
- KM + Cox for hypopituitarism
- logistic/Cox for salvage
- weighted comparison for hold / plan / timing

### Primary Predictive Package

- penalized Cox for remission
- penalized logistic for 5-year durable remission
- penalized logistic or Cox for hypopituitarism

### Exploratory ML Package

- RSF / XGBoost
- SHAP
- nonlinearity exploration

---

## 13. 一句话项目语言

> 这个 study 的数据科学任务不是"跑几个模型"，而是：
> 
> **把一个多中心、非随机、时间到事件、数据不完全统一的临床问题，转成一个既能支持临床推断、又能支持个体化预测的分析系统**

---

*Document created: 2026-03-21*
