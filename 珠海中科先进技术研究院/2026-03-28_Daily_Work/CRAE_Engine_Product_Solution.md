# Causal-RWE-AI Engine (CRAE) - Product-Level Solution
## For 珠海中科先进技术研究院 (ZIAT)

---

## ⭐ Product Name

**Causal-RWE-AI Engine for Drug & Device Evaluation (CRAE Engine)**

---

## 🔷 Core Modules (Product-Level)

### 1️⃣ Data Harmonization Engine
**数据标准化引擎**

| Capability | Value Proposition |
|------------|-------------------|
| RCT → ADaM | CDISC标准，直接用于监管 |
| RWD → Pseudo-ADaM | 解决多源数据不可分析痛点 |
| Medical Device Data | exposure-event结构化 |

**Target**: 先进院最大痛点 - 多源数据整合

---

### 2️⃣ Causal Engine
**因果推断引擎** (护城河)

| Method | Use Case |
|--------|-----------|
| PS/IPTW | 主分析 |
| Target Trial Emulation | RWE模拟RCT |
| Doubly Robust (AIPW) | 双重保护 |
| IV (医生偏好) | 器械场景专用 |

**Delivery**: SAS Macro + Python API 双版本

---

### 3️⃣ Validation Engine
**可信度验证引擎**

| Validation | Description |
|------------|-------------|
| Covariate Balance | SMD < 0.1 |
| Negative Control | 验证无偏 |
| Sensitivity | E-value分析 |
| Weight Diagnostics | 权重分布检查 |

---

### 4️⃣ AI Copilot
**AI助手** (差异化核心)

| AI Function | Description |
|-------------|-------------|
| 自动生成DAG | 文献+数据驱动 |
| 识别Confounders | 基于知识图谱 |
| 自动生成SAP/CSR | 注册材料草稿 |
| 自然语言解释 | regulator-friendly输出 |

---

### 5️⃣ Decision Engine
**决策输出引擎**

| Output | Use Case |
|--------|----------|
| Regulatory-ready evidence | NMPA/FDA申报 |
| 器械注册报告 | 注册支持 |
| HTA/HEOR分析 | 成本效果 |
| Label extension建议 | 适应症拓展 |

---

## 🔶 Medical Device vs Drug (Key Differences)

| Dimension | Drug | Device |
|-----------|------|--------|
| Exposure | 固定用药 | 使用行为（时间依赖） |
| Bias | Confounding | + Learning curve |
| IV Opportunity | 少 | 多（医院/医生偏好） |
| RWE Value | 补充 | 核心证据 |

---

## 🔥 Device-Specific Causal Models

### 1. Time-varying Exposure
```sas
/* Marginal Structural Model */
proc phreg data=device_data;
    model time*event(0) = device_use / ties=efron;
    weight ipw_device;
    /* Time-varying covariate adjustment */
run;
```

### 2. Instrumental Variable (医生偏好)
- IV = 医院/医生倾向使用某器械
- 适合先进院场景

### 3. Learning Curve Adjustment
```sas
/* Operator experience as covariate */
proc phreg data=device_data;
    model time*event(0) = device use_days operator_exp time_since_adoption;
run;
```

---

## 🎯 Project Case Study

**项目名称**: AI-assisted causal evaluation of a novel oncology device using real-world data

### Study Design

**Step 1: Target Trial Emulation**
- Population: stage III/IV cancer
- Treatment: device vs standard care
- Index date: first device use
- Follow-up: 12 months

**Step 2: 数据来源**
- RCT (if available)
- EHR + claims
- 先进院器械数据库

**Step 3: 因果方法**
- PS-IPTW (主分析)
- MSM (时间依赖)
- IV (医生偏好)

**Step 4: 结果**
- OS / PFS
- AE rate
- cost-effectiveness

**Step 5: AI增强**
- 自动生成CSR
- 自动可视化
- 自动写注册摘要

---

## 💼 一句话总结

> "We convert real-world device data into regulatory-grade causal evidence with AI-assisted automation."

---

## 👤 Personal Positioning

### Current → Target

| Current | Target |
|---------|--------|
| SAS Programmer | Causal RWE Scientist (AI-enabled) |
| Statistical Analyst | Real-World Evidence & Causal Modeling Lead |

### Your True Value

✅ 把真实世界数据变成"因果证据"的人
✅ 能对接AI的人（但不被AI替代）
✅ 懂CDISC → 直接可用于监管

---

## 🚀 Next Steps Available

1. **完整SAS Macro系统** - 自动输出SMD表、Love Plot、Cox结果、PDF报告
2. **AI融合方案** - Python + LLM自动生成DAG、SAP
3. **提案PPT** - "对接珠海先进院的10页PPT结构"

---

*Product solution created: 2026-03-28*
*Ready for project proposal / interview*