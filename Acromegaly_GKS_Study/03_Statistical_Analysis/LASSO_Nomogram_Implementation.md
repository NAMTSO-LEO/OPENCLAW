# Complete LASSO + Nomogram Implementation Plan

## 一、建模范式总览

```
LASSO → 选变量 → Cox模型 → Nomogram → ML验证
```

---

## 二、变量输入

### 候选变量（全部放入）

| 变量 | 英文 | 类型 |
|------|------|------|
| IGF-1指数 | IGF-1 index | 连续 |
| 基线GH | Baseline GH | 连续 |
| 肿瘤体积 | Tumor volume | 连续 |
| Knosp分级 | Knosp grade | 有序 |
| 生物学有效剂量 | BED | 连续 |
| 边缘剂量 | Margin dose | 连续 |
| 等剂量线 | Isodose line | 连续 |
| 视神经剂量 | Optic dose | 连续 |
| 药物停用 | Medication hold | 二分类 |
| 手术-放疗间隔 | Surgery-GKRS interval | 连续 |
| 年龄 | Age | 连续 |
| 性别 | Sex | 二分类 |

---

## 三、Step 1: LASSO变量筛选

### 目的
- 防止过拟合
- 自动选变量
- 处理共线性

### 结果（示例）

LASSO选出：

| 变量 | 系数 |
|------|------|
| IGF-1i | -0.XX |
| BED | +0.XX |
| Medication hold | +0.XX |
| Timing | -0.XX |
| (Tumor volume) | (可选) |

### 输出
- 筛选后的变量列表
- 系数值

---

## 四、Step 2: 多变量Cox模型

### 模型

```
Time to remission ~ IGF-1i + BED + hold + timing + volume
```

### 输出

| 变量 | HR | 95% CI | P值 |
|------|-----|--------|-----|
| IGF-1i (每增1) | XX | XX-XX | <0.01 |
| BED (每增10) | XX | XX-XX | <0.01 |
| Hold (yes vs no) | XX | XX-XX | <0.01 |
| Timing (每6月) | XX | XX-XX | XX |

---

## 五、Step 3: 构建Nomogram

### 预测终点
- 1年remission概率
- 3年remission概率
- 5年remission概率

### Nomogram结构

```
Points:
  IGF-1i = 1.5 → 0分
  IGF-1i = 2.0 → 20分
  IGF-1i = 2.5 → 40分
  
  BED = 150 → 0分
  BED = 200 → 30分
  
  Hold = No → 0分
  Hold = Yes → 25分
  
  Timing = 12月 → 0分
  Timing = 36月 → 20分

Total Points → Remission Probability
```

### 临床意义
医生可以算："这个病人3年缓解概率是多少"

---

## 六、Step 4: 模型验证

### 内部验证
- Bootstrap（推荐，1000次）
- 或 5-fold CV

### 评估指标

| 指标 | 目标值 | 意义 |
|------|--------|------|
| C-index | >0.70 | 区分度 |
| AUC (1/3/5年) | >0.70 | 区分度 |
| Calibration | 无系统偏差 | 校准度 |
| Brier score | <0.25 | 预测误差 |

---

## 七、Step 5: ML增强分析

### 模型
- Random Survival Forest (RSF)
- XGBoost

### 目的
- 检查非线性
- 验证Cox结果
- 提高预测能力

---

## 八、Step 6: SHAP解释

### 输出

#### 变量重要度排名
1. IGF-1i
2. BED
3. Medication hold
4. Timing

#### 非线性关系
- IGF-1i: 负相关（非线性）
- BED: 正相关（平台效应）

---

## 九、Methods原文

### 中文版（投稿级）

为降低过拟合风险并提高变量筛选的稳定性，本研究采用LASSO惩罚回归对候选变量进行筛选。通过交叉验证确定最优惩罚参数（λ），并将筛选出的变量纳入多变量Cox比例风险模型。基于最终模型构建列线图（nomogram），用于预测个体化内分泌缓解概率。模型性能通过一致性指数（C-index）、校准曲线及Brier评分进行评估，并采用bootstrap方法进行内部验证。此外，采用随机生存森林及梯度提升模型进行补充分析，以探索变量间的非线性关系，并通过SHAP方法评估变量重要性。

### English Version

LASSO-penalized regression was applied for variable selection to reduce overfitting and improve model stability. The optimal penalty parameter (λ) was determined via cross-validation. Variables selected by LASSO were then included in a multivariable Cox proportional hazards model, and a nomogram was constructed to provide individualized remission probability predictions. Model performance was evaluated using concordance index, calibration curves, and Brier scores, with internal validation via bootstrapping. Additionally, random survival forests and gradient boosting models were applied for supplementary analysis to explore nonlinear relationships, with SHAP values used for variable importance assessment.

---

## 十、Results原文

### 中文版

LASSO惩罚回归筛选出IGF-1指数、生物学有效剂量（BED）、围放疗期药物停用及手术至放疗间隔为主要预测变量。多变量Cox分析显示，上述变量均与持久性内分泌缓解显著相关（均P<0.05）。基于该模型构建列线图用于预测1年、3年及5年缓解概率。模型表现良好，C-index为XX（95% CI: XX-XX），校准曲线显示预测结果与实际观察一致。机器学习模型进一步验证了上述结果，并显示IGF-1指数、BED及药物停用状态为最重要的预测因素。

### English Version

LASSO-penalized regression identified IGF-1 index, biologically effective dose (BED), peri-radiosurgical medication hold, and surgery-to-GKRS interval as the key predictors. Multivariable Cox analysis demonstrated that all selected variables were significantly associated with durable endocrine remission (all P<0.05). A nomogram was constructed based on the final model to predict 1-year, 3-year, and 5-year remission probabilities. The model demonstrated good performance with a C-index of XX (95% CI: XX-XX), and calibration curves showed agreement between predicted and observed outcomes. Machine learning models further validated these findings, with IGF-1 index, BED, and medication status identified as the most important predictors.

---

## 十一、Figure设计

### Figure 1: Nomogram（核心图）
- 预测1/3/5年remission概率

### Figure 2: Calibration Curve
- 1/3/5年校准曲线

### Figure 3: SHAP Plot
- 变量重要度
- 依赖图

### Figure 4: KM Curve
- 按关键变量分层

---

## 十二、完整分析流程

```
1. 数据准备
         ↓
2. LASSO变量筛选
         ↓
3. Cox模型建模
         ↓
4. Nomogram构建
         ↓
5. Bootstrap验证
         ↓
6. RSF/XGBoost增强
         ↓
7. SHAP解释
```

---

## 十三、代码工具

| 步骤 | R包 | SAS过程 |
|------|------|---------|
| LASSO | glmnet | PROC GLMSELECT |
| Cox | survival | PROC PHREG |
| Nomogram | rms | 无直接支持 |
| RSF | randomForestSRC | 无 |
| SHAP | shapviz | 无 |

---

## 十四、核心总结

**LASSO** = 让模型"更稳"
**Nomogram** = 让模型"可用"
**ML** = 让模型"更强"

---

*Implementation plan completed: 2026-03-21*
*Ready for analysis*