# 提案PPT大纲 - 对接珠海先进院
## Causal-RWE-AI 解决方案

---

## 📊 PPT结构 (10页)

---

### 第1页: 封面

**标题**: Causal-RWE-AI Engine for Drug & Device Evaluation

**副标题**: 真实世界因果证据 + AI自动化 - 助力珠海先进院生物医药/医疗器械决策

**汇报人**: [你的名字]
**日期**: 2026年3月

---

### 第2页: 问题与机遇

**核心痛点**:
- 真实世界数据(RWD)如何转化为监管认可的因果证据？
- 如何将AI能力与因果推断结合？

**市场机遇**:
- NMPA/FDA对RWE需求激增
- 医疗器械上市后研究缺口大
- AI辅助申报成为趋势

---

### 第3页: 解决方案概览

**CRAE Engine = 5大引擎**

1. Data Harmonization Engine - 数据标准化
2. Causal Engine - 因果推断
3. Validation Engine - 可信度验证
4. AI Copilot - AI辅助
5. Decision Engine - 决策输出

---

### 第4页: 技术架构

```
┌─────────────────────────────────────────────┐
│              AI Copilot                     │
│  (自动DAG生成 → SAP生成 → 注册材料)         │
├─────────────────────────────────────────────┤
│  Causal Engine                              │
│  PS/IPTW | Target Trial | MSM | IV         │
├─────────────────────────────────────────────┤
│  Validation Engine                          │
│  SMD | E-value | Sensitivity               │
├─────────────────────────────────────────────┤
│  Data Harmonization                         │
│  RCT → ADaM | RWD → Pseudo-ADaM            │
└─────────────────────────────────────────────┘
```

---

### 第5页: 核心能力 - 因果推断

| 方法 | 适用场景 | 价值 |
|------|----------|------|
| PS/IPTW | 基础因果 | 标准方法 |
| Target Trial Emulation | RWE→RCT | 监管认可 |
| MSM | 时间依赖暴露 | 器械专用 |
| IV (医生偏好) | 器械推广 | 独特优势 |
| Doubly Robust | 双重保护 | 稳健性 |

---

### 第6页: 医疗器械场景 (重点)

**为什么特别适合先进院**:

1. **Time-varying exposure**
   - 器械使用 ≠ 一次用药
   - 使用次数、时长、switching

2. **医生偏好作为IV**
   - 医院/医生倾向 → 天然IV
   - 适合推广效果评估

3. **Learning Curve**
   - 初期效果差 ≠ 器械差
   - 医生熟练度建模

---

### 第7页: AI增强价值

**不是替代统计，而是增强**:
- 自动生成DAG初稿
- 自动识别潜在confounders
- 自动生成SAP/CSR草稿
- 自动解释结果 (NLP)

**对接先进院AI平台**:
- 医疗器械注册申报AI大模型
- AI+医疗器械大数据解决方案

---

### 第8页: 案例展示

**项目案例**: AI-assisted causal evaluation of oncology device

| 步骤 | 内容 |
|------|------|
| 1 | Target Trial Emulation设计 |
| 2 | 多源数据整合 (RCT+EHR+Claims) |
| 3 | PS-IPTW + MSM + IV分析 |
| 4 | AI自动生成CSR |
| 5 | 监管申报证据输出 |

**一句话**: "把真实世界器械数据转化为监管级因果证据"

---

### 第9页: 团队与价值主张

**我能带来的**:
- ✅ 因果推断方法论 (PS/IPTW/TTE)
- ✅ SAS/CDISC专业能力
- ✅ Oncology RWE经验
- ✅ AI对接能力

**先进院需要的**:
- ✅ 因果RWE核心人才
- ✅ 平台数据→证据的桥梁

---

### 第10页: 下一步与联系方式

**立即可执行**:
1. 医疗器械RWE试点项目
2. 因果方法培训 + 工具包
3. AI平台对接方案

**联系方式**: [你的联系信息]

---

## 🎯 Key Talking Points

1. **不是程序员，是因果证据工程师**
2. **不是偏药，是药械双场景**
3. **不是空谈，已有完整SAS模板**
4. **直接对接先进院AI平台**

---

## 💼 一页纸总结 (Elevator Pitch)

> 珠海先进院有数据+AI，但缺把RWE变成监管级因果证据的人。我可以提供完整的Causal-RWE-AI解决方案，包括SAS/IPTW模板、Target Trial Emulation框架、以及与你们AI平台的对接能力。专注于医疗器械场景，用医生偏好IV、时间依赖暴露模型等独特方法，产生可申报的证据。

---

*PPT Outline created: 2026-03-28*
*Ready for presentation*