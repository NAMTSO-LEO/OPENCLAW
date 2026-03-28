# 淋巴瘤PD-1研究方案模板
## 复发/难治性弥漫大B细胞淋巴瘤PD-1免疫治疗RWE研究

---

## 项目标题

### 中文
复发/难治性弥漫大B细胞淋巴瘤中PD-1相关免疫治疗的真实世界疗效、安全性及获益人群识别研究

### English
AI-assisted Causal Real-World Evidence Evaluation of PD-1-based Immunotherapy in Relapsed/Refractory Diffuse Large B-cell Lymphoma (R/R DLBCL)

---

## 项目编号
ZIAT-RWE-LYMPHOMA-PD1-2026

---

## 一、研究背景与意义

| 背景 | 内容 |
|------|------|
| 疾病 | R/R DLBCL是淋巴瘤治疗难点 |
| 治疗 | PD-1抑制剂在真实世界应用日益广泛 |
| 问题 | RCT证据覆盖有限，治疗选择偏倚严重 |

**创新点**:
- Target Trial Emulation + 因果推断(PS/IPTW)
- 先进院AI大模型支持
- 直接支持NMPA/FDA补充申报

---

## 二、研究目的

### 主要目的
评价PD-1相关免疫治疗是否显著改善OS和PFS

### 次要目的
1. ORR/CR影响
2. TTNT和缓解持续时间
3. ≥3级AE和irAEs风险
4. 获益亚组识别
5. 外部对照臂生成

---

## 三、研究设计

### 人群
- 成人(≥18岁)R/R DLBCL
- 既往1-2线治疗失败
- 有基线评估记录

### 干预组
PD-1相关免疫治疗(单药或联合)

### 对照组
非PD-1标准挽救治疗

### 随访
主要窗口: 24个月
主要分析: OS/PFS

---

## 四、结局指标

| 类型 | 指标 |
|------|------|
| 主要 | OS, PFS |
| 次要 | ORR/CR, TTNT, 缓解持续时间, ≥3级AE, irAEs |

---

## 五、统计分析方法 (对接Pipeline)

```python
# 使用现有pipeline
pipeline = CausalRWEPipelineZIAT_TimeVarying(
    continuous_vars=['age', 'ldh', 'prior_lines'],
    categorical_vars=['sex', 'ecog', 'stage', 'refractory_status'],
    cluster_col='hospital_id'
)

pipeline.fit_ps_iptw(df, treatment_col='pd1_treatment')
pipeline.balance_check()

# OS/PFS分析
pipeline.run_time_d ependent_cox()

# 输出给AI
pipeline.export_for_ai_model()
```

---

## 六、AI模块

| 功能 | 描述 |
|------|------|
| 文本抽取 | ECOG、IPI、irAEs自动结构化 |
| 获益预测 | CR概率、早期进展风险 |
| 报告生成 | RWE报告、CSR片段 |

---

## 七、预期结果

| 指标 | 预期 |
|------|------|
| OS/PFS | PD-1组显著优于对照组 (HR<1) |
| ORR | 提高 |
| irAEs | 可控 |
| 亚组 | 特定人群获益更明显 |

---

## 八、可交付成果

1. RWE分析报告 + SAP
2. AI辅助变量抽取与预测模型
3. NMPA/FDA注册申报材料
4. Dashboard(生存曲线、Love Plot、森林图)
5. SCI论文 (*JCO* 或 *Blood Advances*)

---

## 九、下一步

如需完整Python代码，请告诉我！

---

*Template completed: 2026-03-28*