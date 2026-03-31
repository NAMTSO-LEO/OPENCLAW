# Statistical Methods - LASSO Justification

## LASSO在肿瘤研究中的应用 justification

---

## 中文版

### 一、LASSO在肿瘤研究中的地位

LASSO（Least Absolute Shrinkage and Selection Operator）已经是肿瘤学中"标准级变量筛选方法"之一，尤其在：

- 预后模型（prognostic models）
- 生存分析（survival analysis）
- 多组学研究（omics）
- 放疗/影像组学（radiomics）

### 二、肿瘤研究数据的特点

肿瘤数据有几个典型特点：

1. **变量多（high dimensional）**
   - 临床变量（年龄、分期等）
   - 生物标志物（IGF-1、基因）
   - 影像参数（radiomics）
   - 治疗参数（dose、BED）

2. **样本量有限**
   - 单中心：几十到几百
   - 多中心：几百但变量更多

3. **变量共线性强**
   - dose vs BED
   - tumor size vs volume
   - GH vs IGF-1

### 三、传统回归的问题

传统 stepwise 回归存在以下问题：
- 不稳定
- 选择随数据变化
- 容易假阳性

### 四、LASSO的优势

- 自动筛选变量
- 控制模型复杂度
- 处理共线性
- 提高稳定性
- 减少过拟合

### 五、本研究中的应用

**推荐结构：**

1. **LASSO筛选变量**
   - 输入：IGF-1i, GH, volume, Knosp, BED, dose, isodose, optic dose, medication hold, timing

2. **选出关键变量**
   - 如：IGF-1i + BED + medication hold + timing

3. **Cox模型**
   - 用筛选后的变量做HR、p值、KM分层

---

### 六、Methods原文

惩罚回归方法（如LASSO）在肿瘤研究中已被广泛应用于生存分析和预后模型构建，尤其适用于变量较多且存在多重共线性的研究场景。相较于传统逐步回归方法，LASSO能够通过引入惩罚项实现自动变量筛选，有效降低模型过拟合风险并提高结果稳定性。因此，本研究采用LASSO惩罚Cox回归对候选变量进行筛选，并结合多变量Cox模型进行最终分析。

---

## English Version

### 一、Role of LASSO in Oncology Research

LASSO (Least Absolute Shrinkage and Selection Operator) has become a standard variable selection method in oncology, particularly for:

- Prognostic models
- Survival analysis
- Multi-omics studies
- Radiomics

### 二、Characteristics of Oncology Data

1. **High-dimensional variables**
   - Clinical variables (age, stage)
   - Biomarkers (IGF-1, genes)
   - Imaging parameters (radiomics)
   - Treatment parameters (dose, BED)

2. **Limited sample sizes**
   - Single-center: dozens to hundreds
   - Multicenter: hundreds but more variables

3. **Strong multicollinearity**
   - dose vs BED
   - tumor size vs volume
   - GH vs IGF-1

### 三、Problems with Traditional Regression

Traditional stepwise regression has issues:
- Unstable
- Variable selection changes with data
- Prone to false positives

### 四、Advantages of LASSO

- Automated variable selection
- Controls model complexity
- Handles multicollinearity
- Improves stability
- Reduces overfitting

### 五、Application in This Study

**Recommended approach:**

1. **LASSO variable screening**
   - Inputs: IGF-1i, GH, volume, Knosp, BED, dose, isodose, optic dose, medication hold, timing

2. **Select key variables**
   - e.g., IGF-1i + BED + medication hold + timing

3. **Cox model**
   - Use selected variables for HR, p-values, KM stratification

---

### 六、Methods Text (Publication-Ready)

Penalized regression methods, particularly LASSO, have been widely applied in oncology research for survival modeling and prognostic factor selection, especially in settings with a relatively large number of candidate variables and potential multicollinearity. Compared with traditional stepwise approaches, LASSO enables automated variable selection while reducing overfitting and improving model stability. In this study, LASSO-penalized Cox regression was used to identify key predictors, followed by multivariable Cox modeling.

---

## 七、Limitations (for Discussion)

- Variable selection may not be unique
- Strongly correlated variables: only one may be retained
- p-values not directly available → requires subsequent Cox modeling

---

## 八、Summary

LASSO的核心价值不是"提高预测能力"，而是在复杂变量中找出真正稳定、可解释的关键因素。

In oncology research, the core value of LASSO is not to "improve predictive ability," but to identify truly stable and interpretable key factors among complex variables.

---

*Document created: 2026-03-21*
*Ready for manuscript integration*