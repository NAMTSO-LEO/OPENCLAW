# Tiered Data Framework

## 数据分级体系

| Tier | 数据类型 | 特征 | 可用于 | 例子 |
|------|----------|------|--------|------|
| **Tier 1** | 高质量临床数据库 | 前瞻/回顾、多中心、质控 | Confirmatory evidence | MIMIC, SEER, 内部高质量研究数据 |
| **Tier 1.5** | 监管型数据库 | 自报系统、信号检测 | Signal detection / validation | FAERS |
| **Tier 2** | 注册试验数据 | 结构化、验证过的 | Method validation | ClinicalTrials.gov |
| **Tier 3** | 公开数据集 | 探索性、模型原型 | Prototyping only | Kaggle数据集 |

---

## 使用规则

### Tier 3 → 仅用于
- 方法开发原型
- 概念验证
- 培训/教学

### Tier 2 → 可用于
- 方法学验证
- 敏感性分析参考
- 外部对标

### Tier 1 → 可用于
- 确认性证据生成
- 监管对话支持
- 注册研究

### Tier 1.5 (FAERS) → 仅用于
- 信号发现
- 假设生成
- 验证支持（不可直接因果结论）

---

## 本项目数据源

### 内部数据 (目标Tier 1)
| 数据源 | 用途 | 预期Tier |
|--------|------|----------|
| 医院EMR数据 | PD-1疗效分析 | Tier 1 |
| 临床数据库 | irAE分析 | Tier 1 |
| 随访数据 | 生存数据 | Tier 1 |

### 外部数据 (补充)
| 数据源 | 用途 | 预期Tier |
|--------|------|----------|
| Kaggle Chemotherapy | 模型验证 | Tier 3 |
| ClinicalTrials.gov | ECA构建参考 | Tier 2 |
| FAERS | irAE信号验证 | Tier 1.5 |

---

## Data Intake Sheet (模板)

每个数据源必须填写以下字段：

| 字段 | 说明 | 填写要求 |
|------|------|----------|
| source_name | 数据源名称 | 必填 |
| owner | 数据负责人 | 必填 |
| provenance | 数据来源 | 必填 |
| update_frequency | 更新频率 | 必填 |
| key_variables | 关键变量 | 至少5个 |
| missingness_risk | 缺失风险 | 高/中/低 |
| bias_risk | 偏倚风险 | 高/中/低 |
| intended_use | 预期用途 | 必填 |
| allowed_evidence_level | 允许的证据级别 | Tier 1-3 |

---

*MVP Step 3 - Data tiering framework defined*
