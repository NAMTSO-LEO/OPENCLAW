# Bias-Control Framework

## 偏倚控制框架 (Bias-First Organization)

### 核心原则
> Organize methods around bias control, not software tools

---

## 偏倚类型与控制方法映射

| 偏倚类型 | 控制层级 | 方法 | 工具 |
|----------|----------|------|------|
| **Confounding** | Design + Estimation | IPTW / AIPW | causallib |
| **Selection Bias** | Design | Target Trial Emulation | 自定义 |
| **Immortal Time Bias** | Estimation | Time-dependent Cox | lifelines |
| **Competing Risk** | Estimation | Fine-Gray | lifelines |
| **Unmeasured Confounding** | Sensitivity | E-value | 自定义公式 |

---

## 1. Confounding Control

### 设计层面
- **Target Trial Emulation**: 模拟RCT设计，用治疗意图而非实际治疗作为暴露

### 估计层面
- **IPTW** (逆概率加权): 标准化处理概率权重
- **AIPW** (增强逆概率加权): 双重稳健估计

### 诊断层面
- **SMD** (标准化均值差): < 0.1 为好
- **ESS** (有效样本量): > 50% 为可接受
- **Love Plot**: 可视化加权前后平衡

---

## 2. Selection Bias Control

### 设计层面
- **Target Trial Emulation Protocol**
  - 定义目标人群
  - 定义治疗策略
  - 定义time zero
  - 定义结局

### 实现
- 只纳入符合入组标准的患者
- 明确排除标准

---

## 3. Immortal Time Bias Control

### 识别
- 暴露定义涉及未来事件
- 时间依赖暴露

### 方法
- **Time-dependent Cox**: 将暴露作为时变协变量
- **Landmark Analysis**: 固定时间点后开始随访
- **Start-stop data structure**: 专门的时间依赖数据格式

### 诊断
- 对比普通Cox vs Time-dependent Cox结果差异

---

## 4. Competing Risk Control

### 场景
- 多种死因
- 竞争事件影响感兴趣事件

### 方法
- **Fine-Gray模型**: 子分布风险比
- **Aalen-Johansen**: 累计竞争事件函数

### 场景
- 非癌症死亡 vs 癌症死亡

---

## 5. Unmeasured Confounding Control

### 方法
- **E-value**: 评估未测混杂需要多强才能解释效应
- **敏感性分析**: 不同假设下的结果范围

### 公式
```
E-value = HR + sqrt(HR*(HR-1))
```

---

## Bias Assessment Checklist (每个分析必填)

- [ ] 主要混杂是什么？
- [ ] 设计层面如何处理？
- [ ] 估计层面如何处理？
- [ ] 诊断指标达标了吗？(SMD < 0.1)
- [ ] 敏感性分析做了吗？
- [ ] 结论是否对偏倚敏感？

---

## MVP实现优先级

### 第一阶段 (MVP)
1. IPTW for confounding
2. Standard diagnostics (SMD, ESS)
3. Time-dependent Cox for irAE

### 第二阶段 (扩展)
4. Target Trial Emulation
5. AIPW (doubly robust)
6. Fine-Gray (competing risk)

### 第三阶段 (完整)
7. E-value
8. 完整敏感性分析框架

---

*MVP Step 5 - Bias control framework defined*
