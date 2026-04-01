# Neuro-Oncology Platform Migration Plan
## 从实体瘤RWE平台 → 神经肿瘤适应症扩展

> 状态: 规划完成 | 日期: 2026-03-31

---

## 一、核心理念

> "不是重建平台，而是替换临床语义层，复用系统底座"

---

## 二、Neuro vs 普通肿瘤关键差异

| 维度 | 普通肿瘤 | 神经肿瘤 |
|------|----------|----------|
| 疗效指标 | OS/PFS | OS/PFS + 神经功能 |
| 影像评估 | RECIST | **RANO** (不同❗) |
| 症状 | 次要 | **核心** (认知/功能) |
| 治疗 | 系统治疗 | **手术 + 放疗 + 药物** |
| 数据复杂性 | 中 | **很高** (影像+神经评分) |

---

## 三、扩展后的Use Cases

### Use Case 1: GBM治疗疗效
- **对应原PD-1 effectiveness**
- OS / PFS分析
- 标准治疗 vs 新治疗
- RANO response评估

### Use Case 2: 神经毒性/Cognitive Decline
- **对应irAE safety**
- Treatment-related neurotoxicity
- Steroid use
- Cognitive function tracking

### Use Case 3: AI影像预测
- **对应AI prediction (更重要)**
- MRI + 临床
- Progression prediction
- Survival prediction
- 关键差异化点🔥

---

## 四、数据结构扩展

### 4.1 新增数据层

| 数据集 | 内容 | 原平台对应 |
|--------|------|------------|
| **ADNEURO** | 神经功能(KPS, 神经检查) | 新增❗ |
| **ADIMG** | 影像特征 | 新增❗ |
| **ADRANO** | RANO response | 新增❗ |
| **ADTREATSEQ** | 治疗序列 | 扩展 |

### 4.2 神经肿瘤特有字段

| 字段 | 说明 | 优先级 |
|------|------|--------|
| KPS | Karnofsky Performance Status | 高 |
| MGMT_METH | MGMT甲基化 | 高 |
| IDH_MUT | IDH突变 | 高 |
| EOR | 切除范围(GTR/STR/Biopsy) | 高 |
| RANO_RESPONSE | RANO评估结果 | 高 |
| SEIZURES | 癫痫发作 | 中 |
| EDEMA | 脑水肿 | 中 |
| NEURO_DEFICIT | 神经功能缺失 | 高 |

---

## 五、Bias-Control Engine升级

### 5.1 Neuro特有偏倚

| 偏倚类型 | 控制方法 | 重要级别 |
|----------|----------|----------|
| **Time bias** | Time-dependent Cox + Landmark | 🔴高 |
| **Measurement bias** | 影像标准化 + AI辅助 | 🔴高 |
| **Functional confounding** | KPS纳入PS模型 | 🔴高 |
| **Selection bias** | Target Trial Emulation | 🟡中 |
| **Competing risk** | Fine-Gray | 🟡中 |

### 5.2 生存分析升级

| 方法 | 用途 | 状态 |
|------|------|------|
| Time-dependent Cox | Progression timing | ✅ |
| Landmark Analysis | 固定时间点分析 | ✅ |
| Competing Risk (Fine-Gray) | Death vs Progression | ✅ |
| Multi-state Model | Diagnosis→Surgery→Progression→Death | 🔜 |

---

## 六、AI模块扩展

### 6.1 Neuro AI应用

| 应用 | 输入 | 输出 | 优先级 |
|------|------|------|--------|
| MRI Segmentation | MRI影像 | 肿瘤分割 | 🔴高 |
| Volume Tracking | 连续MRI | 体积变化 | 🔴高 |
| Progression Prediction | MRI + 临床 | 进展预测 | 🔴高 |
| Survival Prediction | 多模态 | 生存预测 | 🟡中 |

### 6.2 Multi-modal架构

```
Clinical Data (KPS, MGMT, Labs)
         ↓
    Concatenation
         ↓
┌───────────────────┐
│  MRI Features     │ → CNN (ResNet)
│  Clinical Features│ → MLP
└───────────────────┘
         ↓
    Fusion Layer
         ↓
   Prediction Output
```

---

## 七、Evidence Package扩展

### 7.1 必须新增输出

| 输出 | 说明 |
|------|------|
| RANO Response Table | 影像评估结果 |
| Neuro Function Score | KPS变化 |
| Imaging-based Evidence | MRI特征证据 |
| Treatment Sequence | 治疗路径图 |

### 7.2 Interpretation Discipline

**What CAN be concluded:**
- GBM治疗的OS/PFS趋势
- MGMT状态预后价值
- 切除范围对OS影响

**What CANNOT be concluded:**
- 影像解读的因果关系
- 单一中心结果的泛化

---

## 八、数据量要求

| 用途 | 最低要求 |
|------|----------|
| GBM survival | 300-800 |
| AI imaging | 500-1500 |
| Multi-modal | 1000+ |

> 注: 数据质量 > 数据量

---

## 九、迁移路线图

### Phase 1: MVP (已完成)
- ✅ GBM survival (1600 patients)
- ✅ KPS, MGMT, IDH, EOR
- ✅ ML prediction (AUC=0.776)

### Phase 2: 扩展 (规划)
- [ ] RANO response integration
- [ ] Multi-modal imaging AI
- [ ] Neurotoxicity tracking
- [ ] Competing risk model

### Phase 3: 完整 (规划)
- [ ] Multi-state model
- [ ] External validation
- [ ] Regulatory alignment

---

## 十、Director级别总结

> **"We don't rebuild the platform—we extend it by incorporating neuro-specific data structures, imaging-based endpoints, and more advanced time-dependent modeling to account for the unique biases in neuro-oncology."**

---

## 十一、致命风险与解决方案

| 风险 | 解决方案 |
|------|----------|
| MRI interpretation variability | Centralized reading + AI辅助 |
| Functional confounding | KPS纳入所有PS模型 |
| Small sample (rare disease) | 多中心合作 + 真实世界数据 |
| Time bias (progression detection) | Standardized RANO criteria |
| 临床实践不一致 | 建立统一数据字典 |

---

*迁移计划完成*
