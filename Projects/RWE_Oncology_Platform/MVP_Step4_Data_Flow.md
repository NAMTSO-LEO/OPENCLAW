# 标准化数据流

## 统一数据流架构

```
Raw Data → Curated → SDTM-like → ADaM-like → Analysis-ready
```

---

## Stage 1: Raw Data
- 原始来源数据
- 最小化处理
- 保留所有原始字段

---

## Stage 2: Curated
- 数据清洗
- 重复去除
- 基础标准化
- 缺失值标记

---

## Stage 3: SDTM-like
- 按主题组织 (DM, EX, AE, LB, etc.)
- 标准变量命名
- 时间格式统一

---

## Stage 4: ADaM-like (核心分析数据集)

### 核心数据集

| 数据集 | 用途 | 关键变量 |
|--------|------|----------|
| **ADSL** | 受试者主数据 | SUBJID, AGE, SEX, RACE, ARM, SUBJDS, SUBJDSU |
| **ADAE** | 不良事件 | USUBJID, AETERM, AESTDY, AESELEV, AEOUT |
| **ADTTE** | 时间到事件 | USUBJID, CNSR, AVALC, AVAL, AVALU, ADT, TRTP |
| **ADRS** | 肿瘤疗效 | USUBJID, AVAL, AVALU, ANL01FL, ANL02FL, TRTP |

---

## Stage 5: Analysis-Ready
- 添加分析所需衍生变量
- 绑定暴露组/对照组建模
- 创建时间相关变量

---

## 数据流检查清单

- [ ] Raw → Curated: 数据清洗完成
- [ ] Curated → SDTM-like: 变量映射完成
- [ ] SDTM-like → ADaM-like: 分析数据集就绪
- [ ] ADaM-like → Analysis-ready: 建模数据可用

---

*MVP Step 4 - Data flow defined*
