# AI-Driven RWE Oncology Platform 构建 Instructions
## 从0到1构建Director级平台

> 这是一套可执行的完整实施指令

---

## 🎯 先定义平台使命

**第一条指令**：定义平台要服务的决策，而不是先定义技术。

> **Platform Mission**: Build a reusable oncology RWE evidence-generation platform that converts heterogeneous real-world data into decision-ready, regulatory-aligned evidence.

### 服务的决策类型
- Go/No-Go
- Safety signal escalation
- Label expansion
- Post-marketing evidence support
- Patient stratification

---

## 1. 确定平台边界

### 平台做什么 (Do)
- 数据分级与数据准入
- CDISC/ADaM-like 分析数据构建
- 因果推断与生存分析框架
- 可解释 AI 预测模块
- 决策级证据输出

### 平台不做什么 (Don't)
- 所有 exploratory 分析
- 无治理的 ad hoc 报表
- 脱离临床问题的模型实验
- 无法 trace 的黑箱输出

---

## 2. 先定Use Case，不先定模型

### 选择标准 (3个)
1. 临床价值高
2. 监管相关性高
3. 方法可复用
4. 数据可获得
5. 能代表不同证据需求

### 推荐起始Use Case
1. **PD-1 effectiveness evaluation** - 疗效评估
2. **irAE safety monitoring** - 安全性监测
3. **AI-driven response prediction** - 患者分层

### 原则
> 不要一开始做10个Use Case。先用3个Use Case验证平台框架。

---

## 3. 建立Strategy Layer

### 每个Use Case的Strategy Brief (1页)

| 字段 | 内容 |
|------|------|
| Business question | 业务问题 |
| Clinical question | 临床问题 |
| Evidence question | 证据问题 |
| Decision owner | 决策者 |
| Priority rationale | 优先级理由 |
| Expected deliverable | 预期产出 |

---

## 4. 建立Data Governance

### Tiered Data Framework

| Tier | 数据类型 | 可用于 |
|------|----------|--------|
| **Tier 1** | 高质量临床数据库 / 内部高质量研究数据 | Confirmatory evidence |
| **Tier 1.5** | 监管型数据库 (FAERS) | Signal detection / validation |
| **Tier 2** | 注册试验 / 高结构化外部数据 | Method validation |
| **Tier 3** | Kaggle / 公开探索性数据 | Prototyping only |

### 规则
- Tier 3 只能用于 prototyping
- Tier 1/2 才能进入 confirmatory evidence
- FAERS 只能用于 signal detection，不可直接做强因果结论

### Data Intake Sheet (每个数据源必填)
- Source name
- Owner
- Provenance
- Update frequency
- Key variables
- Missingness risk
- Bias risk
- Intended use
- Allowed evidence level

---

## 5. 建立标准化数据流

### 统一数据流

```
Raw → Curated → SDTM-like → ADaM-like → Analysis-ready
```

### 核心分析数据集 (最低要求)

| 数据集 | 用途 |
|--------|------|
| **ADSL** | Subject-level 主数据 |
| **ADAE** | Adverse events 不良事件 |
| **ADTTE** | Time-to-event 事件时间 |
| **ADRS** | Response/tumor outcome 肿瘤疗效 |

### 原则

> Reusable analytical input, not project-specific data chaos

---

## 6. 设计Bias-Control Engine

### 偏倚控制框架 (Bias-First)

| 偏倚类型 | 控制方法 |
|----------|----------|
| Confounding | IPTW / AIPW |
| Immortal time bias | Time-dependent Cox |
| Selection bias | Target trial emulation |
| Competing risk | Fine-Gray |
| Unmeasured confounding | E-value / sensitivity analysis |

### 每个Analysis Template必须回答
1. 主要偏倚是什么？
2. 设计层面如何处理？
3. 估计层面如何处理？
4. 诊断层面如何验证？

---

## 7. 建立Method Modules

### 核心模块

| 模块 | 功能 |
|------|------|
| cohort definition module | 队列定义 |
| baseline covariate module | 基线协变量 |
| propensity score module | 倾向评分 |
| weighting module | 加权模块 |
| balance diagnostics module | 平衡诊断 |
| time-dependent data builder | 时间依赖数据构建 |
| survival modeling module | 生存分析 |
| sensitivity analysis module | 敏感性分析 |
| explainability module | 可解释性 |

### 结果
每个Use Case只需要：
- 选择模块
- 配置参数
- 运行标准流程
- 做科学解释

---

## 8. 设计AI Layer (但不要让AI先行)

### AI模块前置条件
- 数据治理完成
- 临床问题明确
- 标签定义清楚
- 偏倚问题被识别

### AI层内容
- Response prediction
- Risk stratification
- Multimodal fusion
- Explainability (SHAP, feature attribution)

### 规则
AI输出必须：
- 可解释
- 可审查
- 不替代因果设计
- 不直接越过 evidence qualification

---

## 9. 定义Evidence Package

### 标准Evidence Package内容

| 字段 | 内容 |
|------|------|
| Study question | 研究问题 |
| Cohort definition | 队列定义 |
| Data source qualification | 数据源资质 |
| Bias assessment | 偏倚评估 |
| Primary analysis | 主分析 |
| Diagnostics | 诊断 |
| Sensitivity analyses | 敏感性分析 |
| Interpretation | 解释 |
| Limitations | 局限性 |
| Decision implications | 决策影响 |

### 典型输出
- HR with 95% CI
- KM curves
- Forest plot
- Balance diagnostics
- Overlap plot
- SHAP summary
- Sensitivity analysis summary

---

## 10. 建立Decision Support Layer

### 决策适配

| 决策类型 | Evidence Level |
|----------|----------------|
| Exploratory signal | 低置信 |
| Internal prioritization | 中置信 |
| Development support | 中-高置信 |
| Regulatory discussion support | 高置信 |
| Post-marketing monitoring | 视情况 |

### 规则
不是所有 evidence 都能直接进监管沟通。必须给 evidence level 打标签。

---

## 11. 建立Governance Model

### 三层Governance

| 层级 | 负责内容 |
|------|----------|
| **Data Governance** | 数据准入/分级/更新/provenance/traceability |
| **Method Governance** | 分析模板/偏倚控制标准/诊断标准/方法变更审批 |
| **Evidence Governance** | 输出格式/解释一致性/决策适配性/审计追踪 |

---

## 12. 明确团队角色

### 最小团队配置

| 角色 | 功能 |
|------|------|
| Platform lead | 定义框架与优先级 |
| Clinical / medical lead | 临床问题与意义 |
| Statistical methods lead | 方法学标准 |
| Data engineering lead | 数据标准与工程 |
| AI/ML lead | AI模块 |
| Regulatory interface lead | 监管对接 |
| Program manager | 项目管理 |

---

## 13. 先建MVP (不要一开始全做)

### MVP只包含
- 3个高价值Use Case
- 1套数据分级规则
- 1条标准数据流
- 1个bias-control framework
- 1套evidence package模板
- 1个governance review process

### MVP成功标准
- 至少一个Use Case端到端跑通
- 输出可复用模板
- 第二个Use Case能复用 >50% 流程
- Stakeholder能理解和接受输出

---

## 14. 定义平台KPI

### 技术KPI
- Time-to-evidence
- Cross-study reuse rate
- % analyses using standard templates
- Rework reduction
- Diagnostic compliance rate
- Traceability completeness
- Stakeholder adoption rate

### 业务KPI
- Decision cycle time reduction
- Number of reusable evidence packages
- Number of programs supported
- Readiness for regulatory discussion

---

## 15. 建立Adoption机制

### 必做动作
- 方法模板培训
- Use case playbook
- Office hours / review forum
- Platform champions in each team
- Quarterly governance review

### 交付内容
- 使用规则
- 培训体系
- 评审机制
- 持续改进闭环

---

## 16. 建立Roadmap

### Phase 1: Foundation (Month 1-3)
- Define use cases
- Establish tiering
- Build ADaM-like structures
- Standardize bias-control engine

### Phase 2: Validation (Month 4-6)
- Run 3 priority use cases
- Finalize evidence package templates
- Validate reuse across studies
- Establish review board

### Phase 3: Scale (Month 7-12)
- Expand to more indications
- Add multimodal AI
- Integrate with regulatory evidence workflows
- Institutionalize metrics and governance

---

## 17. Director级实施原则

### 5条核心原则

1. **Start with decisions, not data.**
   > 从决策出发，不要从数据出发

2. **Standardize the foundation, not the science.**
   > 标准化基础，不是标准化科学

3. **Organize methods around bias control, not software tools.**
   > 按偏倚控制组织方法，不是按软件工具

4. **Produce evidence packages, not isolated analyses.**
   > 产出evidence package，不是孤立分析

5. **Build organizational capability, not hero-based execution.**
   > 建立组织能力，不是英雄式执行

---

## 📅 Step-by-Step Checklist

### Week 1-2
- [ ] 定义平台使命
- [ ] 选3个Use Case
- [ ] 写Strategy brief

### Week 3-4
- [ ] 建Tiered Data Framework
- [ ] 建data intake sheet
- [ ] 定义标准数据流

### Week 5-6
- [ ] 建ADSL/ADAE/ADTTE/ADRS
- [ ] 定义bias-control framework
- [ ] 确立标准diagnostics

### Week 7-8
- [ ] 搭建reusable method modules
- [ ] 跑第一个MVP Use Case
- [ ] 形成第一版evidence package

### Week 9-10
- [ ] 跑第二、第三个Use Case
- [ ] 检验复用率
- [ ] 建governance review

### Week 11-12
- [ ] 建KPI dashboard
- [ ] 启动培训与adoption
- [ ] 输出Roadmap v2

---

## 🎯 最后一句总指令

> **Do not build a collection of analyses. Build a governed, reusable, decision-oriented evidence platform.**

---

*实施指令完成 - 可直接执行*
