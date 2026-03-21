# 多学科决策视角分析

## Multidisciplinary Decision-Making Framework

---

## 一句话总框架

**这项研究本质是在优化一个"三阶段治疗链"：**

```
药物 ↔ 手术 ↔ 伽玛刀
```

并用数据科学去找最优组合。

---

## ① 内分泌/用药视角 (Endocrinologist)

### 核心目标

- 控制GH / IGF-1，减少并发症

### 实际临床困境

#### 问题1：药物要不要一直用？

| 常见药 | 说明 |
|--------|------|
| Somatostatin analogs (SSA) | 生长抑素类似物 |
| Pegvisomant | 生长激素受体拮抗剂 |
| Dopamine agonists | 多巴胺激动剂 |

| 情况 | 结果 |
|------|------|
| 一直用药 | 激素控制好，但可能掩盖放疗效果 |
| 停药 | 激素升高，但可能增强放疗效果 |

#### 问题2：什么时候停药？

**关键变量：medication hold（围放疗停药）**

### 这篇研究在回答

- 停药 vs 不停药，谁更容易达到长期缓解？
- 同时看：remission rate、durability（是否复发）

### 总结

> 内分泌医生关心："我是在帮患者过渡，还是在干扰最终治愈？"

---

## ② 外科医生视角 (Neurosurgeon)

### 核心目标

- 最大程度安全切除肿瘤

### 最大冲突点

**海绵窦 = 禁区**

| 内含结构 | 风险 |
|----------|------|
| ICA（颈内动脉） | 出血 |
| CN III, IV, VI | 神经损伤 |

| 选择 | 后果 |
|------|------|
| aggressive resection | 神经损伤风险↑ |
| 保守 | 残留肿瘤 |

### 这篇研究在帮外科回答

**"我该不该拼命去全切？"**

### 对应变量

- Knosp grade
- residual tumor volume
- location

### 外科策略可能改变

| 从 | 转向 |
|------|------|
| 追求GTR | planned subtotal + GKS |

### 总结

> 这篇研究在推动一个理念转变：**从"尽量切干净" → "合理分阶段治疗"**

---

## ③ 伽玛刀/放射外科视角 (Radiosurgeon)

### 核心目标

- 控制肿瘤 + 降激素 + 不伤正常结构

### 三个最关键问题

#### 1. 打哪里（Targeting strategy）

| 策略 | 说明 |
|------|------|
| targeted | 只打残余 |
| whole sella | 全覆盖 |

**研究要比较：精确 vs 全覆盖，谁更优**

#### 2. 打多少（Dosimetry）

| 变量 | 说明 |
|------|------|
| margin dose | 边缘剂量 |
| max dose | 最大剂量 |
| isodose line | 等剂量线 |
| **BED** | 生物有效剂量 ⭐ |

**本质：剂量够不够触发"内分泌缓解"**

#### 3. 什么时候打（Timing）

- 术后早期 vs 延迟治疗

**研究里：early vs delayed radiosurgery**

### 放疗医生最大困境

| 效果 | 风险 |
|------|------|
| 剂量高 → remission↑ | hypopituitarism↑ |
| 剂量低 → 安全 | remission↓ |

### 总结

> 这篇研究在解决：**"怎么打伽玛刀，才能刚好够有效但不过量"**

---

## ④ 数据科学家/生统视角

### 核心目标

- 从复杂变量中找规律 + 建预测模型

### 研究本质结构

```
输入（features） → 输出（outcomes）
```

### 输入变量（多模态）

| 类别 | 变量 |
|------|------|
| 临床 | age, sex |
| 内分泌 | IGF-1 index, GH, OGTT |
| 影像 | tumor volume, Knosp |
| 治疗 | surgery→GKS interval, medication hold, plan type |
| 放疗参数 | dose / BED |

### 输出（endpoints）

#### 时间事件
- time to remission
- PFS
- recurrence

#### 二分类
- hypopituitarism
- toxicity

### 分析方法

| 方法 | 用途 |
|------|------|
| KM | 时间分布 |
| Cox | hazard ratio |
| Logistic | 风险预测 |

### 真正高级的点

> **Dynamic prediction model**
> - individualized prediction
> - risk score
> - nomogram
> - ML

### 数据科学核心问题

> **"在什么组合条件下，患者最可能："**
> - 达到remission
> - 不复发
> - 不出现毒性

---

## 四个学科的"冲突点"

| 决策点 | 内分泌 | 外科 | 放疗 | 数据 |
|--------|--------|------|------|------|
| 是否停药 | 倾向用药 | 不关心 | 可能影响效果 | 要验证 |
| 手术范围 | 不参与 | 想切多 | 希望留点可打 | 看残余影响 |
| 放疗剂量 | 无 | 无 | 想提高效果 | 看toxicity trade-off |
| 治疗时机 | 想稳定 | 术后决定 | 早 vs 晚 | KM分析 |

---

## 最终整合

### 这项研究其实在建立一个

> **"多学科协同决策模型"**

---

## 临床路径

### Step 1: 手术
- **问题**：留多少？

### Step 2: 药物
- **问题**：用不用？停不停？

### Step 3: 伽玛刀
- **问题**：什么时候打？怎么打？

---

## 最终目标

> **找到一个最优组合：**
> - **最大化 remission + 最小化 toxicity**

---

## 行业级总结

> 这项研究不是单一治疗评估，而是在构建一个
> 
> **"肢端肥大症多模态精准治疗决策系统"**

---

*Document created: 2026-03-21*
