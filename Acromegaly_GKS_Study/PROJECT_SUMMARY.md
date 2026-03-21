# Acromegaly GKS Study - Project Summary

## 项目总览

| 项目 | 内容 |
|------|------|
| **研究标题** | Gamma Knife Radiosurgery for Cavernous Sinus–Invading Acromegaly |
| **研究设计** | 国际多中心回顾性队列研究 |
| **研究编号** | Acromegaly_GKS_Study |
| **创建日期** | 2026-03-19 |

---

## 文件清单

| 文件名 | 描述 | 状态 |
|--------|------|------|
| Study_Proposal.md | 研究提案 | ✅ |
| Statistical_Analysis_Plan.md | 统计分析计划 | ✅ |
| Predictive_Modeling_ML_Analysis.md | ML/DL预测建模（英文） | ✅ |
| ML_Analysis_Chinese.md | ML/DL预测建模（中文） | ✅ |
| Variable_Coding_ADaM.md | 变量编码与ADaM结构 | ✅ |
| METHODS_PublicationReady.md | 投稿版Methods（英文） | ✅ |
| METHODS_Chinese.md | 投稿版Methods（中文） | ✅ |
| ABSTRACT_PublicationReady.md | 投稿版摘要（英文） | ✅ |
| ABSTRACT_Chinese.md | 投稿版摘要（中文） | ✅ |

---

## 研究概要

### 研究背景

肢端肥大症是由生长激素分泌型垂体腺瘤引起，若未充分控制可导致显著的心血管、代谢、肌肉骨骼和神经内分泌疾病。经鼻蝶手术是一线治疗，但当肿瘤侵犯海绵窦时，手术缓解率显著下降。

### 研究目的

1. 确定GKS后持久性内分泌缓解的概率和预测因素
2. 明确缓解时间特征（早期 vs 晚期）
3. 评估长期影像学控制、生化复发和补救治疗需求
4. 定义垂体功能减退和其他放射副反应的发生率和预测因素
5. 研究治疗时机、药物暂停和先进剂量学变量对缓解和毒性的影响
6. 开发动态预测模型

### 研究假设

GKS在海绵窦侵犯型肢端肥大症中提供高长期肿瘤控制和临床有意义的内分泌缓解，但持久缓解和毒性受到以下因素强烈影响：
- 基线激素负荷
- 残留肿瘤体积和位置
- 手术到放疗的间隔
- 围放疗药物状态
- 放疗计划变量

---

## 主要和次要终点

### 主要终点

| 终点 | 定义 |
|------|------|
| 持久性内分泌缓解 | IGF-1正常，停药，无复发 |
| 内分泌控制 | IGF-1正常，用药中 |
| 缓解时间 | GKS到首次缓解的间隔 |
| 影像学肿瘤控制 | MRI显示肿瘤稳定或缩小 |

### 次要终点

- 初始缓解后的生化复发
- 补救治疗需求
- 新发垂体功能减退
- 视觉毒性、颅神经损伤
- 总生存

---

## 统计方法

### 传统统计（主要）

| 方法 | 应用 |
|------|------|
| Kaplan-Meier | 生存分析 |
| Log-rank检验 | 组间比较 |
| Cox回归 | 时间-事件分析 |
| Logistic回归 | 二分类结局 |
| LASSO/Elastic Net | 变量筛选 |

### 机器学习（次级）

| 算法 | 应用 |
|------|------|
| Random Forest | 二分类 |
| XGBoost | 二分类/生存 |
| Random Survival Forest | 生存分析 |

### 深度学习（探索）

- DeepSurv
- 多模态融合模型

---

## 验证策略

- 重复K折交叉验证
- Bootstrap乐观校正
- **Internal-external validation**（中心留一验证）

---

## 性能评价指标

| 指标类型 | 指标 |
|----------|------|
| 区分度 | AUC, C-index, time-dependent AUC |
| 校准度 | Calibration plots, Brier score |
| 临床效用 | Decision curve analysis |

---

## 建模变量

### 核心变量

| 类别 | 关键变量 |
|------|----------|
| 内分泌 | IGF-1指数 ⭐ |
| 肿瘤 | 肿瘤体积, Knosp分级 ⭐ |
| 手术 | 手术到GKS间隔 ⭐ |
| 放疗 | BED, Margin dose, Plan type ⭐ |
| 药物 | 围放疗药物暂停 ⭐ |

---

## ADaM数据结构

| 数据集 | 用途 |
|--------|------|
| ADSL | 受试者水平数据 |
| ADTTE | 时间-事件数据 |
| ADLB | 纵向内分泌数据 |
| ADOUT | 二分类结局 |

---

## 预期发表亮点

⭐ **1. 海绵窦特异性队列**（别人没有）
⭐ **2. BED + 剂量学**（放疗领域加分）
⭐ **3. 动态预测模型**（少有人做）
⭐ **4. Internal-external validation**（顶刊喜欢）

---

## Figure设计

| 图表 | 内容 |
|------|------|
| Figure 1 | 流程图（纳入排除） |
| Figure 2 | Kaplan-Meier曲线 |
| Figure 3 | Nomogram |
| Figure 4 | SHAP图 |
| Figure 5 | 校准曲线 + DCA |

---

## 目标期刊

- Neurosurgery
- JNS
- JCEM

---

## 关键日期

| 日期 | 事件 |
|------|------|
| 2026-03-19 | 项目创建 |

---

## 研究团队

- Zhenye Li
- Bardia Hajikarimloo
- Salem M. Tos
- Yuki Shinya
- Jason P. Sheehan

---

*Summary created: 2026-03-21*
