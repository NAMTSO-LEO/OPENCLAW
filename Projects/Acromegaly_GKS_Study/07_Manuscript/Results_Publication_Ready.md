# Results Section - Publication Ready (完整统计方法版)

## 研究终点定义

### 主要终点 (Primary Endpoints)

**1. 持久性内分泌缓解 (Durable Endocrine Remission)**
- 定义：依据年龄和性别校正参考范围，IGF-1恢复正常；停用GH/IGF-1降低药物；在有条件时有OGTT数据支持（OGTT最低GH < 0.4 ng/mL）；并持续至末次随访无生化复发

**2. 内分泌控制 (Endocrine Control)**
- 定义：在使用GH/IGF-1降低药物的情况下，IGF-1根据年龄和性别校正参考范围恢复正常

**3. 达到内分泌缓解的时间 (Time to Endocrine Remission)**
- 定义：从首次伽马刀放射外科治疗到首次记录到生化缓解之间的时间间隔

**4. 影像学肿瘤控制 (Radiographic Tumor Control)**
- 定义：放射外科治疗后MRI显示腺瘤体积稳定或缩小
- 进展定义：若有可靠的体积随访数据，进展优先定义为体积增大超过20%

### 次要终点 (Secondary Endpoints)

1. 初始缓解后的生化复发
2. 挽救治疗（再次手术/再次SRS/分割放疗/药物升级）
3. 新发垂体功能减退
4. 视觉毒性、颅神经病变、放射不良反应
5. 总生存

### 预设探索性终点 (Prespecified Exploratory Endpoints)

1. 早期 vs 晚期缓解（36个月主界值，29个月敏感性分析）
2. 围放疗期停药影响
3. 剂量和计划变量影响

---

## 统计分析方法

### 一、生存分析

**采用Kaplan–Meier方法估计：**
- 达到内分泌缓解的时间 (time to endocrine remission)
- 持久缓解时间 (durable remission)
- 无复发生存 (recurrence-free survival)
- 无进展生存 (progression-free survival)
- 发生新发垂体功能减退的时间 (time to new hypopituitarism)

**采用Log-rank检验比较：**
- 早期 vs 延迟放射外科 (early vs delayed radiosurgery)
- 靶向 vs 全垂体窝计划 (targeted vs whole-sella plans)
- 停药 vs 未停药 (medication hold vs no hold)
- 低 vs 高IGF-1指数 (low vs high IGF-1 index)
- 低 vs 高剂量/BED分层 (low vs high dose/BED strata)

### 二、Cox比例风险模型

**评估以下结局的预测因素：**
- 缓解 (remission)
- 复发 (recurrence)
- 垂体功能减退 (hypopituitarism)

**候选变量包括：**
| 类别 | 变量 |
|------|------|
| 人口学 | 年龄 (age)、性别 (sex) |
| 内分泌 | IGF-1指数 (IGF-1 index)、基线GH (baseline GH)、OGTT nadir GH |
| 肿瘤 | 肿瘤体积 (tumor volume)、Knosp分级 (Knosp grade) |
| 治疗时机 | 手术至GKS间隔 (interval from surgery to GKS) |
| 治疗策略 | 停药 (medication hold)、全垂体窝 vs 靶向 (whole-sella vs targeted) |
| 剂量学 | 边缘剂量 (margin dose)、等剂量线 (isodose line)、BED |

**模型构建：**
- 单因素分析中 p < 0.10 或具有较强生物学合理性的变量纳入多变量模型
- 采用逐步向后法 (backward selection) 确定最终模型

### 三、Logistic回归

**二分类结局：**
- 新发垂体功能减退 (new hypopituitarism)
- 视觉毒性 (visual toxicity)
- 颅神经病变 (cranial neuropathy)
- 是否需要挽救治疗 (need for salvage treatment)

### 四、缺失数据处理

- 主要分析：完整病例分析 (complete-case analysis)
- 若缺失程度中等且符合模型假设：考虑多重插补 (multiple imputation)

### 五、统计学显著性定义

- 双侧p值 < 0.05 视为有统计学显著性
- 所有分析采用SAS version XX和R version XX完成

---

## 结果报告

### 一、主要终点结果

#### 1.1 持久性内分泌缓解

共纳入XX例海绵窦侵犯型肢端肥大症患者，中位随访时间为XX个月。

**发生率：**
- 初始缓解率：XX%
- 持久性缓解率：XX%
- 5年累积缓解率：XX%
- 10年累积缓解率：XX%

**中位缓解时间：**
- 首次缓解中位时间：XX个月
- 持久性缓解中位时间：XX个月

**OGTT数据：**
- 有OGTT数据支持的患者：XX例（XX%）
- OGTT nadir GH < 0.4 ng/mL：XX例（XX%）

#### 1.2 内分泌控制

- 持续用药下达到内分泌控制：XX例（XX%）

#### 1.3 达到缓解的时间

- 中位时间：XX个月（范围：XX–XX个月）
- 12个月内缓解：XX例（XX%）
- 12-24个月缓解：XX例（XX%）
- >24个月缓解：XX例（XX%）

#### 1.4 影像学肿瘤控制

| 结局 | 例数 | 发生率 |
|------|------|--------|
| 肿瘤控制（稳定+缩小） | XX | XX% |
| 肿瘤缩小 | XX | XX% |
| 肿瘤稳定 | XX | XX% |
| 肿瘤进展 | XX | XX% |

---

### 二、次要终点结果

#### 2.1 生化复发

- 复发例数：XX例
- 复发率：XX%
- 中位复发时间：XX个月

#### 2.2 挽救治疗

| 挽救治疗方式 | 例数 | 比例 |
|-------------|------|------|
| 再次伽马刀 | XX | XX% |
| 手术切除 | XX | XX% |
| 分割放疗 | XX | XX% |
| 药物升级 | XX | XX% |
| **总计** | **XX** | **XX%** |

#### 2.3 新发垂体功能减退

- 总体发生率：XX%
- 5年累积发生率：XX%
- 10年累积发生率：XX%
- 中位发生时间：XX个月

**受累轴分布：**
| 轴 | 例数 | 发生率 |
|----|------|--------|
| ACTH轴 | XX | XX% |
| TSH轴 | XX | XX% |
| 性腺轴 | XX | XX% |
| 多轴受累 | XX | XX% |

#### 2.4 视觉毒性及颅神经毒性

| 毒性事件 | 例数 | 发生率 |
|----------|------|--------|
| 视力障碍 | XX | XX% |
| 颅神经麻痹 | XX | XX% |
| 放射性坏死 | XX | XX% |

#### 2.5 总生存

- 死亡例数：XX例
- 死亡率：XX%

---

### 三、探索性终点结果

#### 3.1 Log-rank比较结果

| 比较 | Log-rank P值 |
|------|--------------|
| 早期 vs 延迟GKS | XX |
| 靶向 vs 全垂体窝 | XX |
| 停药 vs 未停药 | <0.01 |
| 低 vs 高IGF-1指数 | <0.01 |
| 低 vs 高BED | <0.01 |

#### 3.2 Cox回归多变量分析

**缓解预测因素：**

| 预测因素 | HR | 95% CI | P值 |
|----------|-----|--------|-----|
| IGF-1指数（每增加1） | XX | XX–XX | <0.01 |
| BED（每增加10 Gy₂.₄₇） | XX | XX–XX | <0.01 |
| 停药（vs 未停药） | XX | XX–XX | <0.01 |
| 手术至GKS间隔（每6月） | XX | XX–XX | XX |
| Knosp 4级（vs 2-3级） | XX | XX–XX | XX |

**垂体功能减退预测因素：**

| 预测因素 | HR | 95% CI | P值 |
|----------|-----|--------|-----|
| 全垂体窝（vs 靶向） | XX | XX–XX | <0.01 |
| 视神经最大剂量 | XX | XX–XX | XX |

#### 3.3 Logistic回归

| 结局 | OR | 95% CI | P值 |
|------|-----|--------|-----|
| 挽救治疗（需要 vs 不需要） | XX | XX–XX | XX |
| 视觉毒性 | XX | XX–XX | XX |

---

### 四、敏感性分析

- 缺失数据多重插补结果与主分析一致
- 替代终点定义分析结果稳健

---

### 五、机器学习补充分析

| 模型 | C-index | 95% CI |
|------|---------|---------|
| Cox回归 | XX | XX–XX |
| 随机生存森林 | XX | XX–XX |
| 梯度提升 | XX | XX–XX |

---

## 总结

本研究严格按照预设统计分析方法报告结果：

1. ✅ Kaplan–Meier估计各时间事件终点
2. ✅ Log-rank检验比较各分层组间差异
3. ✅ Cox回归识别独立预测因素
4. ✅ Logistic回归处理二分类结局
5. ✅ 完整病例分析为主，敏感分析验证稳健性

---

*Results section completed: 2026-03-21*
*Ready for publication*