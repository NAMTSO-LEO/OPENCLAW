# Python PS + Stabilized IPTW + Balance + Weighted Cox (Corrected Version)
## For ZIAT Oncology / Medical Device RWE - Production Ready

---

## Complete Python Code (Corrected)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from lifelines import CoxPHFitter

# =========================================================
# 1. 数据读取
# =========================================================
# 必需列：
# treatment: 1=treated, 0=control
# time: 随访时间
# event: 1=事件, 0=删失

df = pd.read_csv("your_oncology_data.csv").copy()

# 示例变量
continuous_vars = ["age", "comorbidity_score", "ecog"]
categorical_vars = ["sex", "stage"]
covariates = continuous_vars + categorical_vars

# 去掉关键变量缺失
df = df.dropna(subset=["treatment", "time", "event"] + covariates).copy()

# treatment 转 int
df["treatment"] = df["treatment"].astype(int)
df["event"] = df["event"].astype(int)

print(f"样本量: {len(df)}")
print(f"治疗组: {df['treatment'].sum()}, 对照组: {(df['treatment']==0).sum()}")

# =========================================================
# 2. 预处理 + Propensity Score (正确方式)
# =========================================================

# 连续变量标准化，分类变量做dummy encoding
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), continuous_vars),
        ("cat", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"), categorical_vars)
    ]
)

ps_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("logit", LogisticRegression(max_iter=2000, solver="lbfgs", random_state=42))
])

X = df[covariates]
y = df["treatment"]

ps_model.fit(X, y)
df["ps"] = ps_model.predict_proba(X)[:, 1]

# PS 截断，防止极端值导致爆炸权重
eps = 0.01
df["ps"] = df["ps"].clip(eps, 1 - eps)

print("\nPS summary:")
print(df["ps"].describe())

# =========================================================
# 3. Stabilized IPTW (正确方式)
# =========================================================

p_treated = df["treatment"].mean()  # 整体治疗概率

# Stabilized weight formula: P(T) / P(T|X)
df["iptw"] = np.where(
    df["treatment"] == 1,
    p_treated / df["ps"],          # treated: P(T)/P(T|X)
    (1 - p_treated) / (1 - df["ps"])  # control: (1-P(T))/(1-P(T|X))
)

# 进一步 trimming：1% ~ 99%
lower, upper = df["iptw"].quantile([0.01, 0.99])
df["iptw_trim"] = df["iptw"].clip(lower=lower, upper=upper)

print("\nIPTW summary (before trimming):")
print(df["iptw"].describe())

print("\nIPTW summary (after trimming):")
print(df["iptw_trim"].describe())

# =========================================================
# 4. SMD 计算函数 (加权前/后对比)
# =========================================================

def weighted_mean(x, w):
    return np.sum(w * x) / np.sum(w)

def weighted_var(x, w):
    mu = weighted_mean(x, w)
    return np.sum(w * (x - mu) ** 2) / np.sum(w)

def smd_continuous(x_t, x_c, w_t=None, w_c=None):
    if w_t is None:
        w_t = np.ones(len(x_t))
    if w_c is None:
        w_c = np.ones(len(x_c))
    
    mt = weighted_mean(x_t, w_t)
    mc = weighted_mean(x_c, w_c)
    vt = weighted_var(x_t, w_t)
    vc = weighted_var(x_c, w_c)
    return abs((mt - mc) / np.sqrt((vt + vc) / 2))

def smd_binary(x_t, x_c, w_t=None, w_c=None):
    if w_t is None:
        w_t = np.ones(len(x_t))
    if w_c is None:
        w_c = np.ones(len(x_c))
    
    pt = weighted_mean(x_t, w_t)
    pc = weighted_mean(x_c, w_c)
    p = (pt + pc) / 2
    denom = np.sqrt(p * (1 - p))
    if denom == 0:
        return 0.0
    return abs((pt - pc) / denom)

def calculate_smd_table(df, continuous_vars, categorical_vars, treatment_col="treatment", weight_col=None):
    treated = df[df[treatment_col] == 1]
    control = df[df[treatment_col] == 0]
    
    wt_t = treated[weight_col].values if weight_col else None
    wt_c = control[weight_col].values if weight_col else None
    
    rows = []
    
    # 连续变量
    for var in continuous_vars:
        smd_unweighted = smd_continuous(treated[var].values, control[var].values)
        
        if weight_col:
            smd_weighted = smd_continuous(treated[var].values, control[var].values, wt_t, wt_c)
        else:
            smd_weighted = smd_unweighted
        
        rows.append({
            'Variable': var,
            'Type': 'Continuous',
            'SMD_Before': smd_unweighted,
            'SMD_After': smd_weighted,
            'Balanced': '✅' if smd_weighted < 0.1 else '❌'
        })
    
    # 分类变量
    for var in categorical_vars:
        # 获取dummy后的列名
        var_cols = [c for c in df.columns if c.startswith(f"{var}_")]
        for var_col in var_cols:
            smd_unweighted = smd_binary(treated[var_col].values, control[var_col].values)
            
            if weight_col:
                smd_weighted = smd_binary(treated[var_col].values, control[var_col].values, wt_t, wt_c)
            else:
                smd_weighted = smd_unweighted
            
            rows.append({
                'Variable': var_col,
                'Type': 'Binary',
                'SMD_Before': smd_unweighted,
                'SMD_After': smd_weighted,
                'Balanced': '✅' if smd_weighted < 0.1 else '❌'
            })
    
    smd_df = pd.DataFrame(rows)
    return smd_df

# 计算加权前后的SMD对比
balance_table = calculate_smd_table(
    df, 
    continuous_vars, 
    categorical_vars, 
    treatment_col="treatment",
    weight_col="iptw_trim"
)

print("\n" + "="*60)
print("平衡性诊断 (SMD < 0.10 为良好)")
print("="*60)
print(balance_table.to_string(index=False))

# 可视化 SMD 对比
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(balance_table))
width = 0.35
ax.bar([i - width/2 for i in x], balance_table['SMD_Before'], width, label='Before IPTW', color='red', alpha=0.7)
ax.bar([i + width/2 for i in x], balance_table['SMD_After'], width, label='After IPTW', color='green', alpha=0.7)
ax.axhline(y=0.1, color='black', linestyle='--', label='Threshold (0.1)')
ax.set_xticks(x)
ax.set_xticklabels(balance_table['Variable'], rotation=45, ha='right')
ax.set_ylabel('|SMD|')
ax.set_title('Covariate Balance: Before vs After IPTW')
ax.legend()
plt.tight_layout()
plt.show()

# =========================================================
# 5. 加权 Cox 回归 (正确方式)
# =========================================================

# 正确方式：先把权重作为新列，然后指定 weights_col
# lifelines 的 weights_col 参数
cph = CoxPHFitter(penalizer=0.1, l1_ratio=0.0)

cph.fit(
    df,
    duration_col='time',
    event_col='event',
    formula='treatment',
    weights_col='iptw_trim',  # 正确：指定权重列名
    robust=True  # 使用稳健标准误
)

print("\n" + "="*60)
print("加权 Cox 模型结果 (因果 HR)")
print("="*60)
cph.print_summary()

# =========================================================
# 6. 生存曲线可视化
# =========================================================

cph.plot_partial_effects_on_outcome('treatment', values=[0, 1], plot_baseline=False)
plt.title('Weighted Survival Curves (IPTW-adjusted)')
plt.xlabel('Time')
plt.ylabel('Survival Probability')
plt.show()

# =========================================================
# 7. 输出供 AI 大模型的结构化结果
# =========================================================

results = {
    'ATE_HR': cph.hazard_ratios_.iloc[0],
    'HR_95CI_lower': cph.confidence_intervals_.loc['treatment', '95% lower-bound'],
    'HR_95CI_upper': cph.confidence_intervals_.loc['treatment', '95% upper-bound'],
    'p_value': cph.summary.loc['treatment', 'p'],
    'sample_size_original': len(df),
    'sample_size_after_trim': len(df),
    'mean_iptw': df['iptw_trim'].mean(),
    'max_smd_after': balance_table['SMD_After'].max(),
    'balanced_all': (balance_table['SMD_After'] < 0.1).all()
}

print("\n" + "="*60)
print("基础模型输出摘要（可直接喂给注册申报AI大模型）")
print("="*60)
for k, v in results.items():
    print(f"{k}: {v}")

# 保存结果
pd.DataFrame([results]).to_csv('causal_rwe_base_results.csv', index=False)
print("\n结果已保存至: causal_rwe_base_results.csv")
```

---

## 关键修正点

| 问题 | 修正 |
|------|------|
| `weights=df['iptw']` | 改为 `weights_col='iptw_trim'` |
| 分类变量直接StandardScaler | 改用 `OneHotEncoder` |
| 只看加权后SMD | 同时显示加权前/后对比 |
| PS无截断 | 改为 `df["ps"].clip(eps, 1-eps)` |

---

## 使用说明

1. 准备CSV数据 (treatment/time/event/covariates)
2. 运行完整代码
3. 检查SMD表 (After列 < 0.1)
4. 解读HR, 95% CI, p-value
5. 导出结果喂给AI大模型

---

*Corrected version created: 2026-03-28*
*Production ready for ZIAT projects*