# t5-crs2.sas 程序总结

## 1. 程序目的

t5-crs2.sas 用于 ISS（Integrated Summary of Safety）分析，生成表 t_5.2.3，汇总 EPCO 相关研究中**细胞因子释放综合征（CRS）特征**的统计结果。

该程序整合了两类联合治疗/单药治疗数据，主要覆盖：
- M20-621
- GCT3013-02
- 另外程序中还纳入了 GCT3013-01、M23-362、GCT3013-05 的单药相关数据用于第 7 组分析

最终输出为 RTF 格式表格，按预设分页生成 CRS 特征汇总表。

---

## 2. 程序头信息

| 项目 | 内容 |
|------|------|
| Program name | t5-crs2.sas |
| Compound | EPCO |
| Study | M20-621 and GCT3013-02 |
| Milestone | ISS |
| Description | Create TFL t__5.2.3 |

**版本历史**：
- zhangyx86 于 20Jan2025 创建原始版本
- HONGLX1 于 13NOV2025 更新

---

## 3. 程序依赖与运行前准备

### 宏
| 宏 | 用途 |
|----|------|
| %init | 初始化环境 |
| %user | 设定输出类型、是否打印等参数 |
| %create_rtf_style_template | 定义 RTF 样式模板 |
| %l_get_htf | 生成输出文件名 |
| %l_add_htf | 插入页眉页脚/HTF信息 |

### 必要输入数据集
- adam.adsl
- adam.adaesi
- adam.adce
- adam.adaes
- adam.adsaftte

### 输出相关
- &tpath 指向有效 RTF 输出路径
- vtlfdata 库已定义
- &_output_ds、&_rtffile 可正常生成

---

## 4. 关键全局设置

| 宏变量 | 值 | 说明 |
|--------|-----|------|
| dtft | date9. | 日期格式 |
| rtyp | TABLE | 输出类型 |
| groupn | trtn | 分组变量名 |
| grpno | 7 | 分析组数量 |
| ptkey | usubjid | 受试者标识 |

---

## 5. 分析组定义

程序通过 %grp 宏定义 **7 个分析组**，基于：
- STUDYID
- TR01AG1N
- IPIGR1

### 7个分析组逻辑

| 组号 | 研究 | TR01AG1N | IPI |
|------|------|----------|-----|
| 1 | M20-621 | 1 | 2–5 |
| 2 | M20-621 | 2 | 2–5 |
| 3 | GCT3013-02 + M20-621 | 1 | 2–5 |
| 4 | M20-621 | 1 | 3–5 |
| 5 | M20-621 | 2 | 3–5 |
| 6 | GCT3013-02 + M20-621 | 1 | 3–5 |
| 7 | GCT3013-01 / M23-362 / GCT3013-05 | 3 | - |

### 对应表头

- M20-621 (IPI 2-5): Epco + R-CHOP / R-CHOP
- Pooled Epco + R-CHOP (IPI 2-5)
- M20-621 (IPI 3-5): Epco + R-CHOP / R-CHOP
- Pooled Epco + R-CHOP (IPI 3-5)
- Pooled Epco Monotherapy

---

## 6. 数据处理主线

### 第一步：确定安全分析集
- 从 ADSL 中筛选 SAFFL='Y'
- 应用 %grp 宏分配到 7 个分析组

### 第二步：识别 CRS 事件
从 ADAESI 中提取 CRS 事件：
- CRSFL='Y'
- TRTEMFL='Y'
- AESICAT in ('CYTOKINE RELEASE SYNDROME','CRS')
- AEPTCD in (10052015, 10050685)

ATOXGR 转换为数值型 ATOXGRN：
- Grade 1 → 1
- Grade 2 → 2
- Grade 3 → 3
- Grade 4 → 4
- Grade 5 → 5

### 第三步：构建 CRS 症状信息
症状来源：ADCE
- Fever / Pyrexia
- Hypotension
- Hypoxia
- Other

**关联键**：
- M20-621 / M23-362：AEREFID1-AEREFID4
- GCT研究：AESPID

### 第四步：构建 CRS 汇总分析集
主要统计：
1. 至少 1 次 CRS 事件的受试者数
2. 每受试者 CRS 发作次数分布
3. CRS 分级（Grade 1–5）
4. Cycle 1 CRS 事件数
5. CRS 症状发生情况
6. CRS 相关处理措施

### 第五步：时间统计
时间参数来自 ADSAFTTE：
- CRSDURH：CRS 起始时间（小时）
- CRSDURD：CRS 起始时间（天）
- CRSRSD：CRS 缓解时间

---

## 7. 统计分母逻辑

### 受试者层面
用于：Subjects with at least one CRS event、Number of episodes per subject
- 分母：有 CRS 事件的受试者总数 total_s

### 事件层面
用于：Grade 1–5、症状、治疗措施、Resolved CRS
- 分母：CRS 总事件数 total_e

---

## 8. 最终表格结构

### 第1页
- CRS受试者数
- 发作次数
- CRS Grade

### 第2页
- CRS signs and symptoms
- Other 明细项

### 第3页
- CRS event management
- 起始时间（小时/天）
- 缓解时间

---

## 9. 运行时重点检查项

1. **样本量宏变量**：&numd1 ~ &numd7
2. **CRS 事件筛选**：CRSFL、TRTEMFL、AESICAT、AEPTCD
3. **症状关联**：adce 与 aesa 的合并键匹配
4. **时间参数**：ADSAFTTE 中 PARAMCD
5. **输出检查**：final 数据集、&_rtffile、&tpath

---

## 10. 常见风险点

| 风险 | 说明 |
|------|------|
| 分组条件写死 | 研究号、治疗组和 IPI 条件硬编码，数据编码改变会出错 |
| ATOXGR 值异常 | 不在 Grade 1–5 内会丢失分级统计 |
| CRS 症状关联复杂 | M20-621/M23-362 与 GCT 系列采用不同关联键 |
| 时间参数依赖 PARAMCD | ADSAFTTE 的 PARAMCD 不一致会导致时间统计为空 |

---

## 11. 交接说明

本程序 t5-crs2.sas 用于 ISS 中生成表 t_5.2.3，汇总 EPCO 相关研究中 CRS 特征。程序基于 ADSL、ADAESI、ADCE、ADAES 和 ADSAFTTE，按照研究、治疗组及 IPI 分层定义 7 个分析组，统计至少一次 CRS 事件的受试者数、每受试者发作次数、CRS 分级、CRS 症状、CRS 相关治疗措施，以及 CRS 起始与缓解时间，最终通过 PROC REPORT 输出 3 页 RTF 表格。运行时需重点确认分组逻辑、CRS 筛选条件、症状关联键、时间参数及样本量宏变量是否正确。

---

*文档创建：2025-11-13*  
*最后更新：2025-11-13*  
*维护人：HONGLX1*
