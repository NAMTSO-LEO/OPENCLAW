# ADCE ISS 数据集规格说明书

## 1. 概述

### 1.1 目的
本文档描述了用于 **ISS（Integrated Summary of Safety，安全性综合汇总）** 的 ADCE（Analysis Dataset for Clinical Events）数据集的创建规格。

ADCE ISS 是将 **多个临床研究（STUDY_A、STUDY_B、STUDY_C1、STUDY_C2、STUDY_D、STUDY_E）** 中的临床事件数据整合成统一的分析数据集，供后续安全性分析使用。

### 1.2 数据来源
| 来源研究 | 数据来源 |
|----------|----------|
| STUDY_A | SDTM CE 域 |
| STUDY_B | 已有 ADCE |
| STUDY_C1 | SDTM CE 域 |
| STUDY_C2 | SDTM CE 域 |
| STUDY_D | SDTM CE 域 |
| STUDY_E | ADAE 反推构建 |

### 1.3 核心目标
把多个研究中的 Clinical Event 相关数据整合成一个统一的 ADCE 分析数据集，供后续 ISS 安全性分析使用。

---

## 2. 处理流程概述

### 2.1 六大处理步骤

```
┌─────────────────────────────────────────────────────────────────┐
│                    ADCE ISS 数据处理流程                          │
├─────────────────────────────────────────────────────────────────┤
│  Step 1: 按研究取数                                            │
│  从各研究分别提取 CE/ADCE/ADAE 相关记录                          │
├─────────────────────────────────────────────────────────────────┤
│  Step 2: 按研究内规则筛选事件                                   │
│  只保留目标事件类别（如 SIGNS AND SYMPTOMS、CRS/ICANS）         │
├─────────────────────────────────────────────────────────────────┤
│  Step 3: 标准化日期和分析时间变量                                │
│  统一日期格式、计算 Study Day、生成 datetime 变量                │
├─────────────────────────────────────────────────────────────────┤
│  Step 4: 关联 AE 信息                                          │
│  为每条事件补齐 AESPID、AESICAT 等 AE 相关变量                  │
├─────────────────────────────────────────────────────────────────┤
│  Step 5: 统一结构并合并                                         │
│  统一变量框架，纵向合并所有研究数据                              │
├─────────────────────────────────────────────────────────────────┤
│  Step 6: 去重、补充 ADSL、生成序号                               │
│  去重、与 ADSL 合并、生成 ASEQ                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. 详细处理步骤

### Step 1：按研究取数

#### 从各研究提取数据

| 研究 | 数据来源 | 说明 |
|------|----------|------|
| STUDY_A | SDTM CE 域 | 直接从 CE 提取 |
| STUDY_B | 已有 ADCE | 直接使用 |
| STUDY_C1 | SDTM CE 域 | 直接从 CE 提取 |
| STUDY_C2 | SDTM CE 域 | 直接从 CE 提取 |
| STUDY_D | SDTM CE 域 | 直接从 CE 提取 |
| STUDY_E | ADAE 反推 | 从 ADAE/ADAES 构建 CE 风格数据 |

#### 提取的关键变量
- STUDYID
- SUBJID / USUBJID
- SITEID
- CETERM / CEDECOD / CECAT / SCAT
- CESTDAT / CEEENDAT
- CEENRF / CESEQ

---

### Step 2：按研究内规则筛选事件

#### 各研究事件筛选规则

| 研究 | 保留的事件类别 |
|------|----------------|
| STUDY_A | SIGNS AND SYMPTOMS |
| STUDY_B | SIGNS AND SYMPTOMS |
| STUDY_C1 | CRS/ICANS 相关症状 |
| STUDY_C2 | CRS/ICANS 相关症状 |
| STUDY_D | SIGNS AND SYMPTOMS |
| STUDY_E | AE 相关事件（从 ADAE 反推） |

#### 筛选逻辑
```sas
/* 示例筛选逻辑 */
if CECAT = "SIGNS AND SYMPTOMS" then output;
if CECAT = "CRS/ICANS SYMPTOMS" then output;
```

---

### Step 3：标准化日期和分析时间变量

#### 需要生成的日期/时间变量

| 变量名 | 描述 | 来源/计算 |
|--------|------|-----------|
| CESTDAT | 事件开始日期 | 从原始日期转换 |
| CEEENDAT | 事件结束日期 | 从原始日期转换 |
| CESTDTC | 事件开始日期时间（ISO） | 原始值 |
| CEEENDTC | 事件结束日期时间（ISO） | 原始值 |
| CESTDY | 相对治疗开始日的分析日 | CESTDAT - TRTSDT + 1 |
| CEEENDY | 相对治疗结束日的分析日 | CEEENDAT - TRTSDT + 1 |
| CENDAT | 事件结束日期（分析用） | 同 CEEENDAT |
| CENDTC | 事件结束日期时间（分析用） | 同 CEEENDTC |

#### 日期转换规则
1. 将字符型 ISO 日期转换为标准 SAS date / datetime
2. 基于治疗开始日期（TRTSDT）计算相对天数
3. 对缺失时间的情况应用统一补齐规则

---

### Step 4：关联 AE 信息

#### 需要补齐的 AE 相关变量

| 变量名 | 描述 | 说明 |
|--------|------|------|
| AESPID | AE 序列号 | 用于关联 AE |
| AESICAT | AE 分类 | 如 CRS、ICANS、INFUSION RELATED REACTION 等 |

#### 关联方式

| 研究 | 关联方式 |
|------|----------|
| STUDY_A | 通过 link group 变量直接连接 |
| STUDY_B | 通过 link group 变量直接连接 |
| STUDY_C1 | 通过 RELREC 找到 CE 与 AE 的对应关系 |
| STUDY_C2 | 通过 RELREC 找到 CE 与 AE 的对应关系 |
| STUDY_D | 从 ADAE/ADAES 补回分类信息 |
| STUDY_E | 从 ADAE/ADAES 补回分类信息 |

#### 关联逻辑
```sas
/* 通过 RELREC 关联 */
proc sql;
    create table ce_ae_link as
    select a.*, b.aespid, b.aesicat
    from ce_all a
    left join relrec b
    on a.studyid = b.studyid 
    and a.subjid = b.subjid
    and a.ceterm = b.aeterm;
quit;
```

---

### Step 5：统一结构并合并

#### 统一保留的变量

| 变量名 | 描述 |
|--------|------|
| STUDYID | 研究编号 |
| SUBJID | 受试者编号 |
| USUBJID | 唯一受试者编号 |
| SITEID | 中心编号 |
| CETERM | 事件术语 |
| CEDECOD | 事件编码（PT） |
| CECAT | 事件类别 |
| SCAT | 亚类别 |
| ATOXGR | Toxicity Grade |
| ATOXGRN | Toxicity Grade（数值） |
| CESCAT | 事件分析分类 |
| CESEQ | 事件序列号 |
| CESTDAT | 事件开始日期 |
| CEEENDAT | 事件结束日期 |
| CENDAT | 事件结束日期（分析用） |
| CESTDY | 事件开始分析日 |
| CEEENDY | 事件结束分析日 |
| CENDY | 事件结束分析日（分析用） |
| CENDTC | 事件结束日期时间 |
| CETERM | 事件术语 |
| AESPID | AE 序列号 |
| AESICAT | AE 分类 |
| AESEQ | AE 序列号 |
| TRTSDT | 治疗开始日期 |
| TRTEDT | 治疗结束日期 |
| TRTP | 计划治疗 |
| TRTA | 实际治疗 |
| SAFFL | 安全性人群标志 |

#### 合并后全局标准化

| 标准化项 | 说明 |
|----------|------|
| AESICAT 文本统一 | 统一大小写、术语表达 |
| ATOXGR 格式统一 | 统一为字符型/数值型 |
| STUDYID 来源修正 | 确保各研究 ID 正确 |
| datetime 变量重新生成 | 统一格式 |

---

### Step 6：去重、补充 ADSL、生成序号

#### 去重规则
按以下关键变量去重：
- STUDYID
- USUBJID
- CETERM
- CESCAT
- CESTDAT
- CENDAT

```sas
proc sort data=adce_merged nodupkey;
    by studyid usubjid ceterm cescat cestdat cendat;
run;
```

#### 与 ADSL 合并
```sas
proc sql;
    create table adce_final as
    select a.*, b.AGE, b.SEX, b.RACE, b.TRTSDT, b.TRTEDT, b.TRTP, b.TRTA, b.SAFFL
    from adce_dedup a
    left join adsl b
    on a.studyid = b.studyid and a.usubjid = b.usubjid;
quit;
```

#### 生成分析序号 ASEQ
```sas
proc sort data=adce_final;
    by studyid usubjid cesq;
run;

data adce_final;
    set adce_final;
    by studyid usubjid;
    if first.usubjid then seq = 0;
    seq + 1;
    ASEQ = seq;
    drop seq;
run;
```

---

## 4. Key Variables 分类梳理

### 4.1 第一层：主键和记录标识变量

这些变量决定一条记录"是谁，是哪个研究、是哪条事件"。

| 变量 | 描述 | 核心程度 |
|------|------|----------|
| USUBJID | 受试者唯一标识，最核心的 subject-level key | ⭐⭐⭐ |
| STUDYID | 研究标识，决定记录来自哪个研究 | ⭐⭐⭐ |
| CESEQ | 原始 CE 记录序号，study 内事件记录标识 | ⭐⭐ |
| ASEQ | 最终 ADaM 中重新生成的分析序号 | ⭐⭐⭐ |
| SRCSEQ | 来源记录序号，保留原始来源定位 | ⭐ |
| SRCDOM | 来源域标识，说明记录来自哪个 source domain | ⭐ |

**最核心组合**：
- 原始定位：`USUBJID + CESEQ`
- 最终分析定位：`USUBJID + ASEQ`

---

### 4.2 第二层：事件描述变量

这些变量描述"发生了什么事件"。

| 变量 | 描述 | 核心程度 |
|------|------|----------|
| CETERM | Clinical Event 原始术语 | ⭐⭐⭐ |
| CEDECOD | 标准化后的事件解码词（Preferred Term） | ⭐⭐⭐ |
| CEPTCD | Preferred Term code | ⭐⭐ |
| CELLT | Lowest Level Term | ⭐ |
| CEHLGT | High Level Group Term | ⭐⭐ |
| CESOC | System Organ Class | ⭐⭐⭐ |
| CEBODSYS | Body System | ⭐⭐ |
| CEOCCUR | 事件是否发生 | ⭐⭐ |
| ACAT / CECAT | 事件分类 | ⭐⭐⭐ |

**最常用，最能代表事件本体**：
- `CETERM`
- `CEDECOD`
- `CESOC`
- `ACAT`

---

### 4.3 第三层：分析时间变量

这些变量描述事件何时发生，是 ADaM 中非常关键的一组。

| 变量 | 描述 | 核心程度 |
|------|------|----------|
| CESTDTC | 原始事件开始日期字符 | ⭐⭐ |
| CEEENDTC | 原始事件结束日期字符 | ⭐⭐ |
| ASTDT | 分析开始日期 | ⭐⭐⭐ |
| AENDT | 分析结束日期 | ⭐⭐⭐ |
| ASTDTM | 分析开始日期时间 | ⭐⭐⭐ |
| AENDTM | 分析结束日期时间 | ⭐⭐⭐ |
| ASTDY | 相对治疗开始日的开始 study day | ⭐⭐⭐ |
| AENDY | 相对治疗开始日的结束 study day | ⭐⭐⭐ |

**直接支持后续 analysis / listing / sorting / derivation**：
- `ASTDT / AENDT`
- `ASTDTM / AENDTM`
- `ASTDY / AENDY`

---

### 4.4 第四层：AE 关联变量

这是这段程序非常重要的一组，因为它不是单纯做 CE，而是在建立 **CE 与 AE 的映射关系**。

| 变量 | 描述 | 核心程度 |
|------|------|----------|
| AESPID | 与 AE 对应的标识 | ⭐⭐⭐ |
| AESICAT | AE category / 特定安全性分类 | ⭐⭐⭐ |
| AEREFID1–AEREFID4 | AE 相关 reference id | ⭐ |
| AELNKGRP / CELNKGRP | AE/CE link group，用于关系映射 | ⭐⭐ |
| AESEQ | 部分处理中间用于和 ADAE 连接的变量 | ⭐⭐ |

**业务上最关键**：
- `AESPID`
- `AESICAT`

因为这两个变量体现了 CE 记录如何挂接到 AE 安全性框架。

---

### 4.5 第五层：严重程度/分级变量

这些变量反映事件分级。

| 变量 | 描述 | 核心程度 |
|------|------|----------|
| CETOXGR | 原始 Toxicity Grade | ⭐⭐ |
| ATOXGR | 标准化后的 Analysis Toxicity Grade | ⭐⭐⭐ |
| ATOXGRN | 数值型 Toxicity Grade | ⭐⭐ |

**最终更重要的是**：`ATOXGR`

因为它是统一后保留到最终 ADCE 的 toxicity grade 变量。

---

### 4.6 压缩成"最核心变量"清单

若只保留最关键的一小组：

| 类别 | 变量 |
|------|------|
| 记录唯一性 | USUBJID, STUDYID, CESEQ, ASEQ |
| 事件内容 | CETERM / CEDECOD, ACAT |
| 分析时间 | ASTDT / AENDT, ASTDY / AENDY |
| AE 关联 | AESPID, AESICAT |
| 分级 | ATOXGR |

---

## 5. 最终数据集变量清单

### 4.1 识别变量

| 变量 | 标签 | 类型 |
|------|------|------|
| STUDYID | 研究编号 | Char |
| USUBJID | 唯一受试者编号 | Char |
| SUBJID | 受试者编号 | Char |
| SITEID | 中心编号 | Char |
| ASEQ | 分析序列号 | Num |

### 4.2 事件变量

| 变量 | 标签 | 类型 |
|------|------|------|
| CETERM | 事件术语 | Char |
| CEDECOD | 事件编码（Preferred Term） | Char |
| CECAT | 事件类别 | Char |
| SCAT | 事件亚类别 | Char |
| CESCAT | 事件分析分类 | Char |

### 4.3 严重性/分级变量

| 变量 | 标签 | 类型 |
|------|------|------|
| ATOXGR | Toxicity Grade | Char |
| ATOXGRN | Toxicity Grade（数值） | Num |
| AESER | 严重不良事件标志 | Char |
| AESEV | 严重性 | Char |

### 4.4 日期变量

| 变量 | 标签 | 类型 |
|------|------|------|
| CESTDTC | 事件开始日期时间（ISO） | Char |
| CEEENDTC | 事件结束日期时间（ISO） | Char |
| CESTDAT | 事件开始日期 | Num |
| CEEENDAT | 事件结束日期 | Num |
| CENDAT | 事件结束日期（分析用） | Num |
| CESTDY | 事件开始相对日 | Num |
| CEEENDY | 事件结束相对日 | Num |
| CENDY | 事件结束相对日（分析用） | Num |

### 4.5 AE 关联变量

| 变量 | 标签 | 类型 |
|------|------|------|
| AESPID | AE 序列号 | Char |
| AESICAT | AE 分类 | Char |
| AESEQ | AE 序列号 | Num |

### 4.6 治疗变量

| 变量 | 标签 | 类型 |
|------|------|------|
| TRTSDT | 治疗开始日期 | Num |
| TRTEDT | 治疗结束日期 | Num |
| TRTP | 计划治疗 | Char |
| TRTA | 实际治疗 | Char |
| TRTDUR | 治疗持续时间 | Num |

### 4.7 人群标志

| 变量 | 标签 | 类型 |
|------|------|------|
| SAFFL | 安全性人群标志 | Char |
| ITTFL | ITT 人群标志 | Char |

### 4.8 基线变量

| 变量 | 标签 | 类型 |
|------|------|------|
| AGE | 年龄 | Num |
| SEX | 性别 | Char |
| RACE | 种族 | Char |
| AGEGR1 | 年龄组 | Char |

---

## 6. 示例数据

### 5.1 单条记录示例

| STUDYID | USUBJID | CETERM | CEDECOD | CECAT | ATOXGR | CESTDAT | CENDY | AESICAT |
|---------|---------|--------|---------|-------|--------|---------|-------|---------|
| STUDY_A | STUDY_A-001 | Fever | PYREXIA | SIGNS AND SYMPTOMS | 2 | 2025-01-15 | 5 | INFLAMMATION |
| STUDY_A | STUDY_A-001 | Headache | HEADACHE | SIGNS AND SYMPTOMS | 1 | 2025-01-16 | 6 | |
| STUDY_C1 | STUDY_C1-001 | Cytokine release syndrome | CRS | CRS/ICANS | 3 | 2025-02-01 | 3 | CRS |

---

## 7. QC 检查清单

### 6.1 数据完整性
- [ ] 所有 6 个研究的数据均已合并
- [ ] 各研究的事件筛选规则已正确应用
- [ ] 日期变量已正确转换

### 6.2 数据一致性
- [ ] AE 关联信息已补齐
- [ ] 变量格式统一
- [ ] 去重后无重复记录

### 6.3 与 ADSL 一致性
- [ ] 所有 USUBJID 在 ADSL 中存在
- [ ] TRTSDT/TRTEDT 与 ADSL 一致

### 6.4 分析可用性
- [ ] ASEQ 已生成
- [ ] 分析日变量已计算
- [ ] 安全性人群标志正确

---

## 8. 核心逻辑一句话总结

> **先把各研究的临床事件数据分别提取并筛选，再统一日期格式并补齐 AE 关联信息，最后跨研究合并、去重后输出标准化的 ISS 用 ADCE 数据集。**

---

## 9. 参考文档

- CDISC ADaM IG v1.1
- ADaM Implementation Guide
- FDA Study Data Technical Conformance Guide
- Study-Specific SAP
