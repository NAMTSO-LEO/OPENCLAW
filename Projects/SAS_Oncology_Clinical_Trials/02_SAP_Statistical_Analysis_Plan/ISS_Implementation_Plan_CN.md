# ISS 综合安全性分析实施方案

## 一、项目目标

建立一套可审计、可追溯、可复用的 ISS（Integrated Summary of Safety，综合安全性分析）流程，完成以下交付物：

- ISS ADSL 及各专题 ADaM 数据集
- ISS 安全性 TLF（Tables, Listings, Figures）
- Define.xml / Analysis Metadata
- ADRG（Analysis Data Reviewer's Guide）
- 编程说明、QC 记录、运行日志、版本归档

核心目标：把多个研究的安全性数据统一整合到同一个分析框架中，支持汇总性安全分析与注册申报。

---

## 二、适用范围

适用于以下场景：

- 多研究安全性整合
- 同一药物 / 同一适应症 / 同一剂量或可比剂量人群整合
- 以安全性为主的 ISS 项目
- 输出以 AE、实验室、暴露、合并用药、临床事件、特殊关注事件、生存 / 时间到事件分析为核心

---

## 三、总体工作流

### 阶段 A：启动与需求确认

**输入文件**：
- Protocol / Integrated Protocol
- SAP（Statistical Analysis Plan）
- TFL Shell
- 各研究 SDTM / ADaM Spec
- Dictionary Version 信息
- Mapping Rule / Sponsor Convention
- 已有 Study-level ADaM

**输出**：
- ISS Programming Plan
- 数据范围确认表
- 数据来源映射表
- 风险清单

**关键动作**：
- 明确纳入哪些研究
- 明确 ISS Population 定义
- 明确是否直接复用 Study-level ADaM，还是从 SDTM 重建
- 明确 MedDRA / WHODrug / CTCAE 版本统一策略
- 明确 Cut-off Date 和 Data Freeze 规则

---

### 阶段 B：数据盘点与整合策略

**需要先回答 5 个问题**：

1. 受试者怎么纳入
2. 不同研究 Treatment Arm 怎么统一
3. 不同研究变量名 / 编码差异怎么对齐
4. 同一事件在不同研究中的 Derivation 是否一致
5. 哪些分析必须用 ISS 重新派生，哪些可以复用 Study ADaM

**建议产出**：Integration Mapping Sheet，至少包含：

| Source Study | Source Dataset | Source Variable | ISS Target Variable | Derivation Rule | Controlled Terminology | Comments |
|--------------|----------------|-----------------|---------------------|-----------------|------------------------|----------|

---

### 阶段 C：ISS ADSL 构建

**ADSL 是 ISS 核心**。

**必做内容**：
- 统一受试者唯一标识
- 统一 Treatment 变量
- 统一 Analysis Flags
- 统一人口学和基线变量
- 统一研究层变量（Study、Cohort、Dose Group、Region 等）

**常见变量**：
- STUDYID、USUBJID
- TRTxxP / TRTxxA
- SAFFL、ITTFL（如需要）
- Demographic Baseline Variables
- First Dose Date / Last Dose Date
- Analysis Cut-off Related Variables

**风险点**：
- 同一个药多研究 Arm 命名不一致
- Cohort 逻辑不一致
- Baseline 定义不一致
- 既往治疗线数或疾病分层变量来源不一致

---

### 阶段 D：专题 ADaM 构建

**推荐顺序**：

1. ADSL
2. ADAE
3. ADAES
4. ADAESI
5. ADCRS / 其他特殊事件集
6. ADCE
7. ADCM
8. ADEX / ADEXSUM
9. ADLB
10. ADMH
11. ADPR
12. ADNT
13. ADSAFTTE
14. 其他专题数据集

---

## 四、各核心数据集实施思路

### 4.1 ISS ADSL

**作用**：定义 ISS Population 和所有后续 Merge 锚点。

**重点**：
- 明确纳入标准
- 统一 Treatment Mapping
- 统一 Safety Population Flag
- 确保每个受试者一条记录
- 做好跨研究变量标准化

**QC 要点**：
- Subject Count by Study
- Subject Count by Treatment
- SAFFL Consistency
- First Dose / Treatment Assignment Consistency

---

### 4.2 ADAE

**作用**：原始 AE 分析主表。

**重点**：
- 跨研究统一 AE Term、SOC、严重性、因果关系、严重不良事件标志
- 统一 Treatment-emergent 规则
- 统一 Onset Relative Day
- 统一 Partial Date Imputations
- 明确是否保留 Symptoms/Signs 类型 AE

**QC 要点**：
- Record Count by Study
- TEAE Flag Consistency
- AE Term / SOC Completeness
- Date Derivation Review
- 去重检查

---

### 4.3 ADAES

**作用**：面向 Incidence Summary 的 AE 汇总表。

**重点**：
- 一般为"每受试者每事件术语一条记录"
- 定义 Event Collapsing 规则
- 明确 Worst Grade / Max Relatedness / First Onset / Closest Causality
- 作为大部分 AE Summary Table 的基础

**QC 要点**：
- ADAES 与 ADAE 一对多 / 多对一逻辑核对
- 每个 Subject-Term 是否唯一
- Worst Severity 是否正确继承

---

### 4.4 ADAESI

**作用**：特殊关注不良事件（AESI）分析。

**重点**：
- 明确 AESI 判定来源
- 可能来自 AE Category
- 可能来自 Sponsor Predefined List
- 可能来自 Study-level Derived Flag
- 固定算法，避免不同研究定义漂移

**QC 要点**：
- AESI Flag 来源可追溯
- Sponsor List 与实际命中 Term 核对
- Study-level 与 ISS-level 定义差异检查

---

### 4.5 ADCRS / ADNT / 其他专题安全表

**作用**：为 CRS、神经毒性、感染、输注反应等专题分析准备。

**重点**：
- 优先基于 ADAESI / ADAAE 派生
- 必须锁定术语清单与 Broad / Narrow 定义
- 明确是否支持 Subject Incidence、Event Incidence、Worst Grade 分析

**QC 要点**：
- Term List Version 固定
- Flag Derivation 可追溯
- 与 Summary Table Denominator 对齐

---

### 4.6 ADLB

**作用**：实验室安全分析主表。

**重点**：
- 统一检验项目代码
- 统一单位转换
- 统一 Baseline 和 Worst Post-baseline 逻辑
- 统一 CTCAE Grading
- 输出 Shift Table 所需变量

**QC 要点**：
- 单位标准化检查
- Baseline 唯一性
- Grade Shift 准确性
- Normal Range / Toxicity Grading Consistency

---

### 4.7 ADEX / ADEXSUM

**作用**：暴露与暴露汇总。

**重点**：
- 统一 Cycle / Visit / Dose Amount / Actual Exposure
- 计算 Dose Intensity、Relative Dose Intensity、Cumulative Dose、Dose Modification
- 明确 Interruption / Reduction / Discontinuation 逻辑

**QC 要点**：
- Total Dose Consistency
- Exposure Duration 合理性
- First / Last Exposure Date 一致性

---

### 4.8 ADCM / ADMH / ADPR / ADCE

**作用**：支持合并用药、既往史、程序操作、临床事件分析。

**重点**：
- 变量标准化
- 时序归类（Prior / Concomitant / Post）
- 与安全事件的辅助关联

---

### 4.9 ADSAFTTE

**作用**：用于 Time-to-Event Safety 分析。

**常见 Endpoint**：
- Time to First TEAE
- Time to First Grade ≥3 AE
- Time to First Serious AE
- Time to First AESI
- Time to Discontinuation due to AE

**QC 要点**：
- Censoring Rule
- Event Date Selection
- Competing Event 处理
- Parameter-level Uniqueness

---

## 五、TLF 方案

ISS 的 TFL 建议分 6 大包：

### 包 1：总体概览
- Disposition
- Exposure Summary
- Treatment Duration
- Deaths / Discontinuations

### 包 2：总体 AE
- TEAE Incidence
- Grade 3+ TEAE
- Serious AE
- Related AE
- AE Leading to Discontinuation / Interruption / Reduction

### 包 3：分层 AE
- SOC/PT Summary
- Worst Grade Summary
- By Treatment / Subgroup / Study Summary

### 包 4：专题安全
- AESI
- CRS
- Neurotoxicity
- Infections
- Infusion Reactions
- Cytopenia 等

### 包 5：实验室与临床指标
- Shift Table
- Worst Post-baseline Table
- Marked Abnormality
- Selected Lab Trend

### 包 6：时间到事件与图形
- Kaplan-Meier
- Cumulative Incidence
- Swimmer / Timeline（如 Shell 要求）

---

## 六、QC 与验证方案

### 6.1 数据集级 QC
- PROC COMPARE
- Key Variable Uniqueness
- Missingness Review
- Subject/Record Reconciliation by Study
- Cross-dataset Consistency Review

### 6.2 逻辑级 QC
- Population Flag Consistency
- Treatment Mapping Consistency
- Worst Grade / First Occurrence / Summary Logic Review
- Date Imputation Review
- CTCAE Grading Review

### 6.3 输出级 QC
- Shell 对比
- Denominator 核对
- 数字一致性
- Footnote / Title / Population Definition Review

### 6.4 审计级 QC
- Program Log
- Version Trace
- Metadata Traceability
- Reviewer Note Resolution

---

## 七、文档交付包

最少建议包含：

- ISS Programming Plan
- Dataset Specification
- Dataset Mapping Sheet
- Derivation Conventions
- TLF Tracking Sheet
- Validation Plan
- Define.xml
- ADRG
- Run Log
- Issue Log / Decision Log
- Transfer / Archive Checklist

---

## 八、时间规划模板

### 中等复杂度 ISS（6 周）

| 周次 | 内容 |
|------|------|
| 第 1 周 | 收集资料、明确纳入研究与 Population、统一字典和变量映射、锁定 ADaM Spec 草稿 |
| 第 2–3 周 | 构建 ADSL / ADAE / ADAES / ADAESI、完成核心专题集初版、第一轮 Reconciliation |
| 第 4 周 | 完成 ADLB / ADEX / ADCM / 其他专题集、跑主要 AE / Lab TFL 初版、修正规则差异 |
| 第 5 周 | Validation Programming、TFL QC、Define Metadata 准备、ADRG 草稿 |
| 第 6 周 | Final Run、Issue Closure、Delivery Package、Archive |

### 大型 ISS（并行线）

- **Population / Exposure 线**
- **AE / Special Interest 线**
- **Lab / TTE / Outputs 线**

---

## 九、角色分工建议

| 角色 | 职责 |
|------|------|
| Lead Programmer | 方案与标准确认、Risk Control、Spec Review、复杂 Derivation 决策、Timeline 跟踪 |
| Primary Programmer | 数据集主程序、TFL 主程序、自检与说明 |
| Validation Programmer | 独立 QC、Compare / Listing Review、Discrepancy Resolution |
| Statistician | Population / Endpoint / Censoring Rule 最终确认、Shell / SAP 解释、Output Signoff |

---

## 十、风险清单

ISS 最容易翻车的地方：

1. 不同研究 Treatment 映射不一致
2. TEAE 定义不一致
3. Baseline 定义不一致
4. Partial Date 规则不一致
5. MedDRA / WHODrug 版本不一致
6. AESI 术语表版本漂移
7. Lab 单位转换不一致
8. Subject 在 Study-level ADaM 已被筛过，ISS 再筛一次导致偏差
9. ADAES 汇总逻辑与 Shell 不一致
10. Denominator 与 Population Flag 不一致

---

## 十一、推荐目录结构

```
/iss
 /spec          # 规格说明
 /raw_specs     # 原始规格
 /mapping       # 映射表
 /adam          # ADaM 程序
 /qc            # QC 程序
 /tlf           # TFL 程序
 /define        # Define.xml
 /adrg          # ADRG
 /logs          # 运行日志
 /transfer      # 交付文件
 /archive       # 归档
```

**程序分层建议**：

```
01_setup
02_adsl
03_adae
04_adaes
05_adaesi
06_topic
07_tlf
08_qc
09_define
10_delivery
```

---

## 十二、立即可用的执行清单

### 第 1 步：ISS Study Inventory
内容包括：研究编号、纳入/排除、治疗组、样本量、字典版本、已有 ADaM 情况

### 第 2 步：锁定核心数据集
先锁定 **ADSL + ADAE + ADAES + ADAESI**，因为 70% 的安全分析都依赖这 4 个

### 第 3 步：TLF Mapping Sheet
每个表对应：Source Dataset、Denominator、Grouping Variable、Shell Note、Program Name、QC Status

### 第 4 步：补专题集
如 ADLB、ADCRS、ADNT、ADSAFTTE

### 第 5 步：最终交付
Define、ADRG、Log 清理、Archive

---

## 十三、核心结论

做 ISS，不要一开始就陷进每个细节变量里。最稳的路径是：

1. **先统一 Population**
2. **再统一 AE 主链**
3. **再做专题安全**
4. **最后做 TLF / Define / ADRG**

**任务拆分建议**：
- Spec
- Spec QC
- Primary Programming
- Validation Programming
- Define
- ADRG
- Unique TFL
- Replicated TFL
