# Holter动态心电监测项目 - 研究方案模板
## AI-assisted Causal RWE Evaluation of Holter Monitor–guided Arrhythmia Detection

---

## 项目名称

### 中文
基于Holter动态心电监测的隐匿性房颤筛查与AI辅助识别项目

### English
AI-assisted Causal RWE Evaluation of Holter Monitor–guided Detection of Occult Atrial Fibrillation after Stroke/TIA

---

## 一、项目定位

| 层次 | 内容 |
|------|------|
| 检测层 | Holter识别房颤、室早、室速、传导阻滞 |
| 因果层 | 评估Holter+AI是否改善临床结局 |
| 决策层 | 为转诊、复查、抗凝、起搏器评估提供支持 |

**匹配场景**：
- ✅ 医疗器械真实世界研究
- ✅ AI辅助医疗器械
- ✅ 注册申报/临床验证
- ✅ HEOR/临床决策支持

---

## 二、研究问题

### Primary Question
使用AI增强的Holter monitor，是否能提高 clinically significant arrhythmia 的检出率？

### Secondary Questions
Holter + AI 是否能：
- 缩短确诊时间
- 提高房颤检出率
- 降低漏诊率
- 促进后续干预决策
- 改善短期临床结局

---

## 三、Target Trial Emulation 设计

### Population (纳入标准)
- 年龄 ≥ 50岁
- 最近3个月内缺血性卒中或TIA
- 既往无明确房颤诊断
- 出院后进入随访系统

### Intervention
Holter monitor + AI-assisted interpretation

### Comparator
常规随访 / 常规短时心电 / 非AI判读

### Index Date
出院后首次监测日期 或 纳入管理路径日期

### Follow-up
30天 / 90天 / 180天

### Outcomes

| 类别 | 变量 |
|------|------|
| Primary | 90天内新发房颤检出率 |
| Secondary | 首次房颤确诊时间 |
| Secondary | 抗凝治疗启动率 |
| Secondary | 再发卒中/TIA |
| Secondary | 心血管相关急诊/住院 |

---

## 四、数据来源

| 数据源 | 变量 |
|--------|------|
| **医院EHR** | 年龄、性别、卒中/TIA诊断、既往病史、药物信息 |
| **Holter设备数据** | 监测时长、AF episode数量、最长AF持续时间、PAC/PVC burden、HRV指标、pause/VT events |
| **随访数据** | 抗凝启动、再入院、再卒中、门诊心内科转诊 |
| **AI判读输出** | 事件候选片段、风险评分、报警等级、自动报告草稿 |

---

## 五、变量设计

### 暴露变量

| 版本 | 定义 |
|------|------|
| **版本1 (二元)** | treatment=1: Holter+AI, treatment=0: 常规路径 |
| **版本2 (剂量)** | Holter监测时长、AI标记阳性负荷、有效分析片段比例 |

### 协变量 (DAG)

```
age
sex
stroke severity (NIHSS)
hypertension
diabetes
heart failure
prior CAD
prior PAC/PVC burden
baseline ECG abnormality
anticoagulant contraindication
hospital / physician (cluster)
monitoring indication severity
```

### 结局变量

| 类型 | 变量 |
|------|------|
| 检测结局 | AF detected within 90 days (binary) |
| 时间结局 | time to AF diagnosis |
| 临床结局 | recurrent stroke/TIA, hospitalization, anticoagulation initiation |

---

## 六、分析框架

### 1. 描述性分析
- 基线特征
- Holter使用比例
- AF检出率
- 不同年龄/卒中严重度分层

### 2. 因果主分析 (PS/IPTW Pipeline)

```python
# 可直接使用现有pipeline
pipeline = CausalRWEPipelineZIAT_TimeVarying(
    continuous_vars=['age', 'stroke_severity', 'prior_pac_burden'],
    categorical_vars=['sex', 'hypertension', 'diabetes'],
    cluster_col='hospital_id'
)

pipeline.fit_ps_iptw(df, treatment_col='holter_ai_use')
pipeline.balance_check()
pipeline.run_time_dependent_cox()
pipeline.export_for_ai_model()
```

### 3. 分析方法

| 分析 | 方法 |
|------|------|
| 主效应 | PS + Stabilized IPTW + Weighted Cox |
| 中心效应 | cluster robust SE |
| 敏感性 | trimming阈值、AF定义阈值、分层分析 |

---

## 七、AI模块嵌入

| AI功能 | 应用 |
|--------|------|
| **事件预筛** | AF, frequent PAC, PVC runs, pauses, AV block, non-sustained VT |
| **风险分层** | occult AF high-risk, urgent cardiology review, anticoagulation evaluation |
| **自动报告** | Holter summary + 临床建议草稿 + 注册申报性能摘要 |

---

## 八、项目流程图

```
卒中/TIA患者进入随访
       ↓
收集EHR + Holter数据
       ↓
AI识别节律异常事件
       ↓
构建Holter+AI vs 常规路径队列
       ↓
DAG定义混杂因素
       ↓
PS + Stabilized IPTW
       ↓
平衡性诊断 (SMD < 0.1)
       ↓
加权Cox / Logistic分析
       ↓
输出：AF检出率、确诊时间、抗凝启动率
       ↓
形成临床与注册证据
```

---

## 九、预期结果示例

> Compared with usual care, Holter monitor with AI-assisted interpretation was associated with a higher probability of atrial fibrillation detection and earlier initiation of stroke-preventive management.

| 指标 | 对照组 | 干预组 | HR/OR |
|------|--------|--------|-------|
| 90天AF检出率 | 12% | 28% | OR=2.8 |
| 确诊时间(中位数) | 45天 | 18天 | HR=2.1 |
| 抗凝启动率 | 35% | 62% | OR=3.0 |
| 90天再入院率 | 18% | 12% | HR=0.6 |

---

## 十、可交付成果

| # | 交付件 | 内容 |
|---|--------|------|
| 1 | 统计分析模块 | PS/IPTW, Cox/Logistic, Balance |
| 2 | AI模块 | 异常节律识别、风险评分、自动报告 |
| 3 | 注册支持材料 | 性能验证摘要、临床评价支持、RWE报告 |
| 4 | 可视化Dashboard | AF detection rate, time to diagnosis, subgroup |

---

## 十一、项目标题选项

| 风格 | 标题 |
|------|------|
| 偏科研 | 基于Holter动态心电与因果真实世界研究的隐匿性房颤筛查及临床决策支持 |
| 偏平台 | Holter动态心电AI辅助判读与真实世界临床价值评估平台 |
| 偏注册 | 面向医疗器械注册申报的Holter monitor AI辅助识别与真实世界证据生成项目 |

---

## 十二、下一步

如需完整Python分析代码模板，请告诉我！

---

*Research proposal template completed: 2026-03-28*
*Ready for ZIAT project initiation*