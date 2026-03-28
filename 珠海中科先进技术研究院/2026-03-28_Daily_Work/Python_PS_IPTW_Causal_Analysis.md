# Python PS/IPTW Causal Analysis Template
## For ZIAT Oncology / Medical Device RWE

---

## Environment Setup

```bash
pip install pandas numpy scikit-learn lifelines matplotlib seaborn causalml dowhy
```

---

## Complete Python Code

```python
"""
Python PS/IPTW Causal Analysis Template
For: 珠海中科先进技术研究院 (ZIAT)
Author: [Your Name]
Date: 2026-03-28
Purpose: Oncology / Medical Device Real-World Evidence Analysis
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import lifelines
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# =====================================================
# 1. DATA PREPARATION
# =====================================================

def load_and_prepare_data(filepath, covariates, treatment_col='treatment', 
                          time_col='time', event_col='event'):
    """
    加载并准备数据
    
    Parameters:
    -----------
    filepath : str - 数据文件路径
    covariates : list - 协变量列表（根据DAG选择）
    treatment_col : str - 治疗列名
    time_col : str - 时间列名
    event_col : str - 事件列名
    
    Returns:
    --------
    df : DataFrame - 准备好的数据
    """
    df = pd.read_csv(filepath)
    
    # 标准化连续变量
    scaler = StandardScaler()
    X = df[covariates]
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X), 
        columns=X.columns, 
        index=X.index
    )
    
    # 合并
    df_processed = df.copy()
    for col in covariates:
        df_processed[col + '_scaled'] = X_scaled[col]
    
    print(f"数据加载完成: {len(df_processed)} 行")
    print(f"治疗组: {df_processed[treatment_col].sum()}, 对照组: {(df_processed[treatment_col] == 0).sum()}")
    
    return df_processed, covariates


# =====================================================
# 2. PROPENSITY SCORE ESTIMATION
# =====================================================

def estimate_ps(df, covariates, treatment_col='treatment'):
    """
    估计Propensity Score
    
    Parameters:
    -----------
    df : DataFrame
    covariates : list - 协变量列表（已标准化）
    treatment_col : str - 治疗列名
    
    Returns:
    --------
    df : DataFrame - 添加ps列
    ps_model : LogisticRegression - 训练好的模型
    """
    scaled_covariates = [c + '_scaled' for c in covariates]
    X = df[scaled_covariates]
    y = df[treatment_col]
    
    ps_model = LogisticRegression(
        max_iter=1000, 
        solver='lbfgs', 
        random_state=42
    )
    ps_model.fit(X, y)
    
    # 预测PS
    df['ps'] = ps_model.predict_proba(X)[:, 1]
    
    print("\nPropensity Score 分布统计：")
    print(df['ps'].describe())
    
    return df, ps_model


# =====================================================
# 3. STABILIZED IPTW CALCULATION
# =====================================================

def calculate_stabilized_iptw(df, treatment_col='treatment', ps_col='ps',
                               lower_pct=1, upper_pct=99):
    """
    计算Stabilized IPTW（推荐版本）
    
    Formula: SW = P(T) / P(T|X)
    
    Parameters:
    -----------
    df : DataFrame
    treatment_col : str - 治疗列名
    ps_col : str - PS列名
    lower_pct : float - 下限修剪百分位
    upper_pct : float - 上限修剪百分位
    
    Returns:
    --------
    df : DataFrame - 添加iptw列并修剪
    """
    # 整体治疗概率 (Numerator)
    p_treatment = df[treatment_col].mean()
    
    # Stabilized Weight 计算
    df['iptw'] = np.where(
        df[treatment_col] == 1,
        p_treatment / df[ps_col],  # Treated: P(T)/P(T|X)
        (1 - p_treatment) / (1 - df[ps_col])  # Control: (1-P(T))/(1-P(T|X))
    )
    
    # Trimming (权重修剪)
    lower = np.percentile(df['iptw'], lower_pct)
    upper = np.percentile(df['iptw'], upper_pct)
    
    df_trimmed = df[(df['iptw'] >= lower) & (df['iptw'] <= upper)].copy()
    
    print(f"\n修剪前样本量: {len(df)}")
    print(f"修剪后样本量: {len(df_trimmed)} (移除 {len(df) - len(df_trimmed)} 行)")
    print(f"修剪阈值: [{lower:.3f}, {upper:.3f}]")
    
    print("\nStabilized IPTW 统计：")
    print(df_trimmed['iptw'].describe())
    
    return df_trimmed


# =====================================================
# 4. BALANCE DIAGNOSTICS (SMD)
# =====================================================

def calculate_smd(df, covariates, treatment_col='treatment', weight_col='iptw'):
    """
    计算加权 Standardized Mean Difference
    
    Target: SMD < 0.1 表示良好平衡
    
    Parameters:
    -----------
    df : DataFrame
    covariates : list - 原始协变量（未标准化）
    treatment_col : str - 治疗列名
    weight_col : str - 权重列名
    
    Returns:
    --------
    smd_df : DataFrame - SMD结果
    """
    smd_results = {}
    
    for cov in covariates:
        treated = df[df[treatment_col] == 1]
        control = df[df[treatment_col] == 0]
        
        # 加权均值
        mean_t = np.average(treated[cov], weights=treated[weight_col])
        mean_c = np.average(control[cov], weights=control[weight_col])
        
        # 加权方差
        var_t = np.average((treated[cov] - mean_t)**2, weights=treated[weight_col])
        var_c = np.average((control[cov] - mean_c)**2, weights=control[weight_col])
        
        # SMD
        smd = (mean_t - mean_c) / np.sqrt((var_t + var_c) / 2)
        smd_results[cov] = abs(smd)
    
    smd_df = pd.DataFrame.from_dict(
        smd_results, 
        orient='index', 
        columns=['SMD']
    )
    smd_df['Balance'] = smd_df['SMD'].apply(lambda x: '✅ Good' if x < 0.1 else '⚠️ Check')
    
    print("\n" + "="*50)
    print("平衡性检查 (SMD < 0.1 为良好)")
    print("="*50)
    print(smd_df)
    
    return smd_df


# =====================================================
# 5. WEIGHTED COX SURVIVAL ANALYSIS
# =====================================================

def weighted_cox_analysis(df, treatment_col='treatment', time_col='time', 
                         event_col='event', weight_col='iptw'):
    """
    加权Cox生存分析
    
    Parameters:
    -----------
    df : DataFrame
    treatment_col : str - 治疗列名
    time_col : str - 时间列名
    event_col : str - 事件列名
    weight_col : str - 权重列名
    
    Returns:
    --------
    cph : CoxPHFitter - 训练好的模型
    """
    cph = CoxPHFitter(penalizer=0.1)  # 轻微惩罚防止过拟合
    
    cph.fit(
        df,
        duration_col=time_col,
        event_col=event_col,
        formula=treatment_col,
        weights=df[weight_col],
        robust=True  # 使用稳健标准误
    )
    
    print("\n" + "="*50)
    print("加权 Cox 模型结果 (因果效应估计)")
    print("="*50)
    cph.print_summary()
    
    return cph


# =====================================================
# 6. VISUALIZATION
# =====================================================

def plot_survival_curves(cph, df, treatment_col='treatment', time_col='time', 
                        event_col='event'):
    """
    绘制加权生存曲线
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    cph.plot_partial_effects_on_outcome(
        treatment_col, 
        values=[0, 1],
        ax=ax,
        color=['blue', 'red']
    )
    
    ax.set_title('Weighted Survival Curves: Treatment vs Control', fontsize=14)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Survival Probability', fontsize=12)
    ax.legend(['Control', 'Treatment'], fontsize=10)
    
    plt.tight_layout()
    plt.show()


def plot_smd_comparison(smd_df, save_path=None):
    """
    绘制SMD对比图 (Love Plot思路)
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['green' if x < 0.1 else 'red' for x in smd_df['SMD']]
    
    bars = ax.barh(smd_df.index, smd_df['SMD'], color=colors, alpha=0.7)
    ax.axvline(x=0.1, color='red', linestyle='--', label='Threshold (0.1)')
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    
    ax.set_xlabel('|SMD|', fontsize=12)
    ax.set_ylabel('Covariates', fontsize=12)
    ax.set_title('Covariate Balance After IPTW Weighting', fontsize=14)
    ax.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


# =====================================================
# 7. MAIN PIPELINE (一键运行)
# =====================================================

def run_causal_analysis(filepath, covariates, output_dir=None):
    """
    一键运行完整因果分析流程
    """
    print("="*60)
    print("开始因果推断分析流程")
    print("="*60)
    
    # Step 1: 数据准备
    print("\n[Step 1] 数据准备...")
    df, covariates = load_and_prepare_data(
        filepath, covariates,
        treatment_col='treatment',
        time_col='time', 
        event_col='event'
    )
    
    # Step 2: PS估计
    print("\n[Step 2] Propensity Score估计...")
    df, ps_model = estimate_ps(df, covariates)
    
    # Step 3: IPTW计算
    print("\n[Step 3] Stabilized IPTW计算...")
    df = calculate_stabilized_iptw(df)
    
    # Step 4: 平衡性诊断
    print("\n[Step 4] 平衡性诊断...")
    smd_df = calculate_smd(df, covariates)
    
    # Step 5: 加权Cox分析
    print("\n[Step 5] 加权Cox生存分析...")
    cph = weighted_cox_analysis(df)
    
    # Step 6: 可视化
    print("\n[Step 6] 生成可视化...")
    plot_survival_curves(cph, df)
    if output_dir:
        plot_smd_comparison(smd_df, f"{output_dir}/smd_plot.png")
    
    print("\n" + "="*60)
    print("分析完成!")
    print("="*60)
    
    return df, smd_df, cph


# =====================================================
# 8. EXAMPLE USAGE
# =====================================================

if __name__ == "__main__":
    # 示例调用
    # 替换为你的数据路径和协变量
    covariates = ['age', 'sex', 'stage', 'comorbidity_score', 'ecog']
    
    # 运行完整流程
    # df, smd_df, cph = run_causal_analysis(
    #     filepath='your_data.csv',
    #     covariates=covariates,
    #     output_dir='./output'
    # )
    
    print("请取消注释上方代码并运行")
```

---

## 额外增强功能

### Sensitivity Analysis (敏感性分析)

```python
def sensitivity_analyses(df, covariates):
    """敏感性分析：不同trimming阈值"""
    
    thresholds = [(1, 99), (5, 95), (2.5, 97.5)]
    results = []
    
    for lower, upper in thresholds:
        df_temp = calculate_stabilized_iptw(df, lower_pct=lower, upper_pct=upper)
        cph = weighted_cox_analysis(df_temp)
        results.append({
            'trim': f'{lower}-{upper}',
            'hr': cph.summary.loc['treatment', 'exp(coef)'],
            'p': cph.summary.loc['treatment', 'p']
        })
    
    return pd.DataFrame(results)
```

### E-value (未测量混杂)

```python
def calculate_e_value(hr, p_value):
    """计算E-value评估未测量混杂"""
    if p_value > 0.05:
        return "Not significant"
    
    hr = float(hr)
    e_value = hr + np.sqrt(hr * (hr - 1))
    return f"E-value = {e_value:.2f}"
```

---

## 🎯 使用说明

1. **准备数据**: CSV格式，包含treatment/time/event/covariates
2. **运行Pipeline**: `run_causal_analysis()`
3. **检查SMD**: 确保所有 < 0.1
4. **解读结果**: HR, 95% CI, p-value

---

## 📊 输出示例

| 输出 | 描述 |
|------|------|
| PS分布 | 0.1-0.9之间 |
| IPTW统计 | 中位数~1, 无极端值 |
| SMD表 | 所有<0.1 |
| Cox结果 | HR, 95% CI, p-value |
| 生存曲线 | Treatment vs Control |

---

*Python template created: 2026-03-28*
*Ready for ZIAT oncology/medical device RWE projects*