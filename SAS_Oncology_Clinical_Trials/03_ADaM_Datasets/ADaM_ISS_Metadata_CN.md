# ADaM ISS 元数据规范说明书

## 一、概述

### 1.1 什么是 ISS ADaM 数据集

本文档定义了 **ISS（Integrated Summary of Safety，综合安全性分析）** 所需的 ADaM 分析数据集规范。

ISS ADaM 数据集的核心作用是：
- 将多个临床研究的原始数据（SDTM）转换为分析-ready 的结构化数据
- 支持安全性分析、汇总和报告生成
- 为 TLG（Table、Listing、Figure）输出提供数据基础

### 1.2 ISS ADaM 数据集设计原则

| 原则 | 说明 |
|------|------|
| 追溯性 | 每条记录可追溯至原始 SDTM 数据 |
| 可重复性 | 基于规格说明可重新生成 |
| 分析可用性 | 变量设计支持常见安全性分析场景 |
| 标准合规性 | 符合 CDISC ADaM IG 规范 |

---

## 二、整体数据流程

```
┌─────────────────────────────────────────────────────────────┐
│                     ISS ADaM 数据流程                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   SDTM 数据源                                               │
│   (AE / CM / LB / CE / MH / PR / QS 等)                    │
│                                                             │
│          ↓                                                  │
│                                                             │
│   Study-level ADaM                                         │
│   (各研究独立的分析数据集)                                   │
│                                                             │
│          ↓                                                  │
│                                                             │
│   ISS 综合 ADaM                                            │
│   (多研究合并的安全性分析数据集)                             │
│                                                             │
│          ↓                                                  │
│                                                             │
│   TLG 输出                                                 │
│   (Table / Listing / Figure)                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 三、ADaM 数据集类型

ISS 分析数据集主要分为三大类：

### 3.1 受试者层数据集

| 数据集 | 说明 |
|--------|------|
| ADSL | Subject-Level Analysis Dataset，受试者层分析数据 |

**特点**：
- 每个受试者一条记录
- 是所有分析数据集的核心表
- 其他数据集通常会与 ADSL 进行 merge 以获取受试者层面信息

**关键变量**：
- STUDYID、USUBJID、SUBJID、SITEID
- AGE、SEX、RACE
- TRTSDT、TRTEDT、TRTP、TRTA
- SAFFL、ITTFL 等人群标志

---

### 3.2 事件类数据集（Occurrence）

表示某种事件的发生记录。

| 数据集 | 事件类型 |
|--------|----------|
| ADAE | 不良事件（Adverse Events） |
| ADAES | 不良事件汇总 |
| ADAESI | 特别关注不良事件 |
| ADCE | 临床事件（Clinical Events） |
| ADCM | 合并用药（Concomitant Medications） |
| ADCRS | 特定综合征事件（如 CRS） |
| ADEX | 用药暴露（Exposure） |
| ADMH | 既往史（Medical History） |
| ADNT | 神经毒性事件（Neurotoxicity） |
| ADPR | 医疗操作（Procedures） |

**通用结构**：
```
每个受试者 + 每个事件 = 一条记录
```

**常见关键变量**：
- STUDYID、USUBJID
- PARAMCD（参数代码）
- TERM（事件术语）
- START DATE（开始日期）
- END DATE（结束日期）
- ATOXGR（毒性分级）

---

### 3.3 参数型数据集（Basic）

用于保存分析参数值。

| 数据集 | 用途 |
|--------|------|
| ADBASE | 基线特征 |
| ADEXSUM | 暴露汇总 |
| ADLB | 实验室指标 |
| ADSAFTTE | 安全性 TTE（Time-to-Event） |

**通用结构**：
```
每个受试者 + 每个参数 + 每个时间点 = 一条记录
```

**示例**：
| USUBJID | PARAMCD | AVAL | AVISIT |
|----------|---------|------|---------|
| 001 | ALT | 32 | Baseline |
| 001 | ALT | 45 | Visit 2 |

---

## 四、数据集依赖关系

### 4.1 ISS 数据集层级结构

```
ADSL（核心受试者层）
│
├── ADAE（不良事件）
│   ├── ADAES（AE 汇总）
│   │   ├── ADAESI（特别关注 AE）
│   │   │   └── ADCRS（CRS 综合征）
│   │   │
│   │   └── ADNT（神经毒性）
│   │
├── ADCE（临床事件）
├── ADCM（合并用药）
├── ADEX（用药暴露）
│   └── ADEXSUM（暴露汇总）
│
├── ADLB（实验室指标）
│
├── ADMH（既往史）
│
├── ADPR（医疗操作）
│
└── ADSAFTTE（安全性 TTE）
    │
    └── ADBASE（基线特征）
```

### 4.2 典型派生关系

| 派生数据集 | 数据来源 | 说明 |
|------------|----------|------|
| ADAES | ADAE | 按受试者+AE term 汇总事件计数 |
| ADAESI | ADAES | 筛选特定关注的 AE |
| ADCRS | ADAESI | 筛选 CRSFL = 'Y' 的记录 |
| ADNT | ADAES | 基于 predefined event list 筛选神经毒性 |

---

## 五、核心数据集详解

### 5.1 ADAE 与 ADAES 的区别

这是 ISS 最常见的结构之一。

#### ADAE（原始不良事件）

- **定义**：原始不良事件记录
- **结构**：每个 AE 一条记录
- **用途**：用于生成详细的不良事件列表

**示例**：
| USUBJID | AEDECOD | AESTDTC |
|----------|---------|---------|
| 01 | Headache | 2025-01-05 |
| 01 | Headache | 2025-01-20 |

#### ADAES（AE 汇总）

- **定义**：按受试者和事件汇总
- **结构**：每个受试者每个 AE term 一条记录
- **用途**：用于 AE 发生率表（incidence tables）

**示例**：
| USUBJID | AEDECOD | COUNT |
|----------|---------|-------|
| 01 | Headache | 2 |

---

### 5.2 ADCRS 数据集逻辑

**来源**：ADAESI

**筛选规则**：CRSFL = 'Y'（细胞因子释放综合征标志）

```sas
data adcrs;
    set adaesi;
    if crsfl = "Y";
run;
```

**典型变量**：
- USUBJID、AECAT、AEPT、CRSFL
- CRSONSDT（CRS 开始日期）、CRSONEDT（CRS 结束日期）
- CRSMAXG（最大 CRS 分级）

---

### 5.3 实验室数据限制（ADLB）

ADLB 通常只保留预定义的指定指标。

**常用指标**：
| 参数代码 | 说明 |
|----------|------|
| ALT | 谷丙转氨酶 |
| AST | 谷草转氨酶 |
| BILI | 总胆红素 |
| CREAT | 肌酐 |
| GLUC | 葡萄糖 |
| PLAT | 血小板计数 |
| WBC | 白细胞计数 |

```sas
if paramcd in ("ALT", "AST", "BILI", "CREAT", "GLUC", "PLAT", "WBC");
```

---

### 5.4 ADCE 数据来源

ADCE（临床事件）的数据来源可能包括：

| 来源 | 说明 |
|------|------|
| SDTM CE | 直接从 CE 域提取 |
| SDTM AE | 从 AE 域反推构建 |

**筛选逻辑**：通常按特定症状或特定事件类别筛选

```sas
/* 示例筛选逻辑 */
if cecat = "SIGNS AND SYMPTOMS";
if scat like "%CRS%" or scat like "%ICANS%";
```

---

### 5.5 ADNT（神经毒性）

**来源**：ADAES

**筛选方式**：基于预定义的 event list

即：使用 **MedDRA term list** 来识别神经毒性相关事件。

**典型变量**：
- USUBJID、AEPT、AECAT
- ICANSFL（免疫效应细胞相关神经毒性综合征标志）
- ICANSDT、ICANSEDT
- ICANSMAXG（最大神经毒性分级）

---

## 六、推荐编程顺序

建立 ISS ADaM 数据集时，通常按照以下顺序：

| 顺序 | 数据集 | 说明 |
|------|--------|------|
| 1 | ADSL | 受试者层基础数据 |
| 2 | ADAE | 不良事件（最核心） |
| 3 | ADAES | AE 汇总 |
| 4 | ADAESI | 特别关注 AE |
| 5 | ADCRS | CRS 综合征事件 |
| 6 | ADCE | 临床事件 |
| 7 | ADCM | 合并用药 |
| 8 | ADEX | 用药暴露 |
| 9 | ADEXSUM | 暴露汇总 |
| 10 | ADLB | 实验室指标 |
| 11 | ADMH | 既往史 |
| 12 | ADPR | 医疗操作 |
| 13 | ADNT | 神经毒性事件 |
| 14 | ADSAFTTE | 安全性 TTE |
| 15 | ADBASE | 基线特征 |
| 16 | ADAESGPT | GPT 生成（若适用） |

---

## 七、变量分类总结

### 7.1 标识变量（Identifier Variables）

用于唯一识别记录。

| 变量 | 说明 |
|------|------|
| STUDYID | 研究编号 |
| USUBJID | 唯一受试者标识 |
| SUBJID | 受试者编号 |
| SITEID | 中心编号 |
| ASEQ | 分析序号 |

### 7.2 事件变量（Topic Variables）

描述事件内容。

| 变量 | 说明 |
|------|------|
| TERM / AETERM | 事件术语 |
| DECOD / AEDECOD | 解码术语 |
| SOC / AESOC | 系统器官分类 |
| CAT / AECAT | 事件类别 |

### 7.3 时间变量（Timing Variables）

描述事件时间。

| 变量 | 说明 |
|------|------|
| STDTC | 开始日期时间 |
| ENDTC | 结束日期时间 |
| STDY | 相对开始日 |
| ENDY | 相对结束日 |

### 7.4 关联变量（Linkage Variables）

建立事件间关联。

| 变量 | 说明 |
|------|------|
| LNKID / LNKGRP | 关联标识/组 |
| REFID | 参考 ID |

### 7.5 分析变量（Analysis Variables）

支持分析展示。

| 变量 | 说明 |
|------|------|
| AVAL | 分析值 |
| AVALU | 分析值单位 |
| ATOXGR | 分析毒性分级 |
| FL | 分析标志 |

---

## 八、核心逻辑总结

ISS ADaM 数据集设计的核心逻辑：

```
ADSL（核心受试者层）
    │
    └── ADAE（不良事件）
            │
            ├── ADAES（AE 汇总）
            │       │
            │       └── ADAESI（特别关注 AE）
            │               │
            │               └── ADCRS（CRS 综合征）
            │
            └── ADNT（神经毒性）
```

### 派生关系简述

| 从 | 到 | 派生方式 |
|----|----|----------|
| ADAE | ADAES | 按 USUBJID + AEDECOD 汇总 COUNT |
| ADAES | ADAESI | 筛选特定关注事件 |
| ADAESI | ADCRS | 筛选 CRSFL = 'Y' |
| ADAESI | ADNT | 基于 MedDRA 筛选神经毒性 |

---

## 九、最终用途

这些 ADaM 数据集最终用于生成：

| 输出类型 | 用途 |
|----------|------|
| Table | AE 发生率表、实验室汇总表、暴露汇总表 |
| Listing | 受试者详细事件列表 |
| Figure | Kaplan-Meier 曲线、森林图 |

---

## 十、参考标准

- CDISC ADaM Implementation Guide v1.1
- CDISC ADaM Terminology
- FDA Study Data Technical Conformance Guide
- Study-Specific SAP
