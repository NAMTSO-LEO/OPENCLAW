# PD-1 + irAE 联合研究方案
## 完整Protocol - 可投稿/可申请基金/可药企合作

---

## 研究标题

### English
Impact of Immune-Related Adverse Events on Survival Outcomes of PD-1-Based Immunotherapy in Relapsed/Refractory Diffuse Large B-Cell Lymphoma: A Causal Real-World Evidence Study Using Time-Dependent Analysis

### 中文
免疫相关不良事件对复发/难治性弥漫大B细胞淋巴瘤PD-1治疗生存获益的影响：一项基于时间依赖模型的真实世界因果研究

---

## 项目编号
ZIAT-RWE-PD1-IRAE-2026

---

## 核心科学问题 (三层递进)

### Q1 (基础因果)
在R/R DLBCL患者中，PD-1相关免疫治疗是否因果改善OS和PFS？（调整选择偏倚后）

### Q2 (时间依赖安全性)
发生irAE后，患者的OS风险是否发生改变？（使用time-dependent Cox，避免immortal time bias）

### Q3 (交互/调节作用) ⭐ 亮点
PD-1治疗的生存获益是否被irAE发生"调节"？irAE能否作为PD-1治疗反应的临床生物标志物？

---

## 研究设计

### 类型
回顾性队列研究，采用 **Target Trial Emulation** 框架模拟前瞻性RCT

### 人群

**纳入标准**：
- 成人（≥18岁）R/R DLBCL患者
- 既往至少1-2线治疗失败
- 有明确基线评估（ECOG、IPI、LDH等）
- 有可追踪用药、irAE和生存随访记录

**排除标准**：
- 既往PD-1/PD-L1治疗史
- 合并其他活动性恶性肿瘤
- 关键数据缺失严重
- 预期生存<30天

### 指数日期
当前治疗方案启动日期

### 暴露定义

| 暴露 | 定义 |
|------|------|
| **主要暴露** | PD-1相关治疗 vs 非PD-1标准挽救治疗 |
| **时间依赖暴露** | irAE_td (0=irAE发生前; 1=irAE发生后) |

---

## 结局指标

### 主要结局
- 总生存（OS）

### 次要结局
- 无进展生存（PFS）
- 客观缓解率（ORR）
- 完全缓解率（CR）
- 下一次治疗时间（TTNT）

### 安全性结局
- irAE发生率
- 严重程度（grade ≥3）
- 特定器官irAE

---

## 统计分析计划 (SAP)

### Layer 1: PD-1疗效因果估计

| 步骤 | 方法 |
|------|------|
| 混杂因素 | DAG定义 (age, sex, ECOG, stage, LDH, IPI, prior_lines, refractory_status, prior_CART/ASCT) |
| 因果估计 | Propensity Score + Stabilized IPTW |
| 诊断 | PS overlap图、Love Plot、SMD、ESS |
| 主模型 | 加权Cox + 加权Logistic + 加权KM |
| 稳健性 | Cluster robust SE |

### Layer 2: irAE时间依赖影响

| 步骤 | 方法 |
|------|------|
| 数据结构 | start-stop长格式 |
| 主模型 | Time-dependent Cox |
| 关键 | 避免immortal time bias |

### Layer 3: 交互/调节分析 ⭐

| 步骤 | 方法 |
|------|------|
| 交互项 | PD-1 × irAE |
| 分层分析 | with irAE vs without irAE |
| 探索 | irAE作为生物标志物 |

---

## 敏感性分析

| 分析 | 说明 |
|------|------|
| 不同trimming | 1%-99% vs 5%-95% |
| Landmark | 3个月/6个月landmark |
| E-value | 未测混杂评估 |
| Grade ≥3 | 严重irAE亚组 |
| Competing risk | 淋巴瘤vs其他死亡 |

---

## 亚组分析

- primary refractory vs relapsed
- prior CAR-T vs no
- 年龄≥65岁
- 高IPI
- 高LDH
- 不同ECOG

---

## AI辅助模块 (先进院特色)

| 功能 | 方法 |
|------|------|
| irAE自动抽取 | NLP从病历文本提取时间、类型、严重程度 |
| irAE风险预测 | XGBoost + SHAP解释 |
| 获益预测 | ML模型预测治疗反应 |

---

## 亮点与创新点

1. ✅ Target Trial Emulation + 严格因果方法
2. ✅ Time-dependent Cox处理irAE
3. ✅ irAE作为治疗反应生物标志物
4. ✅ AI融合：NLP + 风险预测
5. ✅ 注册潜力：External Control Arm

---

## 预期结果模板

- PD-1组经IPTW调整后OS/PFS显著优于对照组
- irAE发生后，time-dependent HR显示保护/风险改变
- 存在PD-1 × irAE交互
- AI抽取准确率 > 85%
- irAE风险预测AUC > 0.75

---

## 投稿方向

| 优先级 | 期刊 |
|--------|------|
| 首选 | JITC, Frontiers in Oncology, Cancer Medicine |
| 冲刺 | Clinical Cancer Research, Blood Advances |

---

## 下一步

如需完整SAP或Python代码整合版，请告诉我！

---

*Protocol completed: 2026-03-28*
*Ready for submission/funding application*