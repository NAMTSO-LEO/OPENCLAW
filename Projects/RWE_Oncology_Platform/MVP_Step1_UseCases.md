# Use Case Selection

## 选择标准
- 临床价值高
- 监管相关性高
- 方法可复用
- 数据可获得
- 能代表不同证据需求

## 选定的3个Use Case

### Use Case 1: PD-1 Real-World Effectiveness Evaluation

| 字段 | 内容 |
|------|------|
| **Business question** | PD-1治疗在真实世界中是否比标准挽救治疗更有效？ |
| **Clinical question** | 在R/R DLBCL中，PD-1能否延长OS？ |
| **Evidence question** | 在校正混杂后，PD-1 vs non-PD-1的HR是多少？ |
| **Decision owner** | 临床开发团队 / 医学事务 |
| **Development phase** | 注册后证据 / Label extension |
| **Priority rationale** | 高价值、高监管相关性、方法可复用至其他免疫治疗 |
| **Expected deliverable** | IPTW校正后的OS HR + 95%CI + KM曲线 + SMD诊断图 |

---

### Use Case 2: irAE Safety Monitoring (Time-Dependent)

| 字段 | 内容 |
|------|------|
| **Business question** | irAE是否与疗效相关？传统分析是否高估了这种相关性？ |
| **Clinical question** | 出现irAE的患者是否生存期更长？（需控制时间依赖偏倚） |
| **Evidence question** | Time-dependent Cox vs 普通Cox的HR差异有多大？ |
| **Decision owner** | 安全团队 / 医学事务 |
| **Development phase** | 上市后监测 |
| **Priority rationale** | 方法学亮点强、解决immortal time bias、行业关注度高 |
| **Expected deliverable** | Time-dependent HR + 普通Cox对比图 + 敏感性分析 |

---

### Use Case 3: AI-Driven Patient Response Prediction

| 字段 | 内容 |
|------|------|
| **Business question** | 哪些患者更可能从PD-1治疗中获益？ |
| **Clinical question** | 基于多模态数据能否预测ORR/PFS？ |
| **Evidence question** | ML模型的预测性能是否显著优于临床变量 alone？ |
| **Decision owner** | 临床开发 / 精准医疗团队 |
| **Development phase** | 探索性 / 精准患者筛选 |
| **Priority rationale** | AI能力展示、多模态融合、精准医疗导向 |
| **Expected deliverable** | 预测模型 + SHAP解释 + 特征重要性排序 |

---

## 优先级理由

1. **PD-1疗效** - 最直接的业务价值，最高的监管相关性
2. **irAE安全** - 方法学创新最强，可发表高水平论文
3. **AI预测** - 平台AI能力展示，未来扩展性强

---

*MVP Step 1 - Use Cases selected*

---

## Extended Use Cases (Multi-Tumor)

### Use Case 4: NSCLC Immunotherapy Effectiveness

| 字段 | 内容 |
|------|------|
| Business question | PD-1在非小细胞肺癌中是否比化疗更有效？ |
| Clinical question | IV期NSCLC中，PD-1 vs化疗的OS HR是多少？ |
| Evidence question | 在校正PD-L1表达和其他混杂后，HR是多少？ |
| Priority rationale | 最高！NSCLC是PD-1最大适应症 |

### Use Case 5: Melanoma irAE-Response Association

| 字段 | 内容 |
|------|------|
| Business question | irAE是否与黑色素瘤疗效相关？ |
| Clinical question | 出现irAE的患者是否OS更长？ |
| Priority rationale | 经典irAE-疗效假设，高关注度 |

### Use Case 6: Breast Cancer TNBC Response Prediction

| 字段 | 内容 |
|------|------|
| Business question | 哪些TNBC患者可能从PD-1获益？ |
| Clinical question | 多模态数据能否预测ORR？ |
| Priority rationale | 精准医疗，高价值 |

---

### Data Summary (Multi-Tumor)

| Tumor | N | PD-1 | Chemo | irAE Rate |
|-------|---|------|-------|-----------|
| DLBCL | 500 | 305 | 148 | 20% |
| NSCLC | 600 | 424 | 115 | 19% |
| Melanoma | 400 | 341 | 20 | 34% |
| Breast | 500 | 140 | 309 | 6% |
| GI | 450 | 178 | 220 | 6% |
| **Total** | **2450** | **1388** | **812** | **16%** |
