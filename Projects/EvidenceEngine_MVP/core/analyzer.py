"""
Evidence Engine MVP - 医疗证据分析引擎
核心统计分析模块
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


class EvidenceAnalyzer:
    """医疗证据分析引擎核心类"""
    
    def __init__(self):
        self.data = None
        self.results = {}
    
    def load_data(self, df: pd.DataFrame):
        """加载数据"""
        self.data = df
        self.results = {}
        return self
    
    def descriptive_stats(self, variables: List[str]) -> pd.DataFrame:
        """描述性统计"""
        if self.data is None:
            raise ValueError("请先加载数据")
        
        desc = self.data[variables].describe().T
        desc['missing'] = self.data[variables].isnull().sum()
        desc['missing_pct'] = (desc['missing'] / len(self.data) * 100).round(2)
        
        self.results['descriptive'] = desc
        return desc
    
    def compare_means(self, var: str, group: str) -> Dict:
        """两组均值比较（t检验）"""
        groups = self.data[group].unique()
        if len(groups) != 2:
            raise ValueError("仅支持两组比较")
        
        g1 = self.data[self.data[group] == groups[0]][var].dropna()
        g2 = self.data[self.data[group] == groups[1]][var].dropna()
        
        t_stat, p_value = stats.ttest_ind(g1, g2)
        
        result = {
            'group1': groups[0],
            'group2': groups[1],
            'n1': len(g1), 'n2': len(g2),
            'mean1': g1.mean(), 'mean2': g2.mean(),
            'std1': g1.std(), 'std2': g2.std(),
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < 0.05
        }
        
        self.results['compare_means'] = result
        return result
    
    def chi_square(self, var: str, group: str) -> Dict:
        """卡方检验"""
        contingency = pd.crosstab(self.data[var], self.data[group])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
        
        result = {
            'chi2': chi2,
            'p_value': p_value,
            'dof': dof,
            'significant': p_value < 0.05,
            'contingency_table': contingency
        }
        
        self.results['chi_square'] = result
        return result
    
    def logistic_regression(self, y: str, x_vars: List[str]) -> Dict:
        """ logistic回归分析 """
        from sklearn.linear_model import LogisticRegression
        from sklearn.preprocessing import StandardScaler
        
        df = self.data[[y] + x_vars].dropna()
        X = df[x_vars]
        y_var = df[y]
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = LogisticRegression(max_iter=1000)
        model.fit(X_scaled, y_var)
        
        result = {
            'coefficients': dict(zip(x_vars, model.coef_[0])),
            'intercept': model.intercept_[0],
            'n': len(df),
            'variables': x_vars
        }
        
        self.results['logistic'] = result
        return result
    
    def survival_analysis(self, time_var: str, event_var: str, group: str = None) -> Dict:
        """生存分析（Kaplan-Meier + Cox回归）"""
        from lifelines import KaplanMeierFitter, CoxPHFitter
        
        df = self.data[[time_var, event_var]].dropna()
        if group:
            df = df.join(self.data[group])
        
        kmf = KaplanMeierFitter()
        kmf.fit(df[time_var], df[event_var])
        
        result = {
            'median_survival': kmf.median_survival_time_,
            'survival_curve': kmf.survival_function_,
            'n_events': df[event_var].sum(),
            'n_at_risk': len(df)
        }
        
        self.results['survival'] = result
        return result
    
    def propensity_score_matching(self, treatment: str, confounders: List[str]) -> pd.DataFrame:
        """倾向评分匹配"""
        from sklearn.neighbors import NearestNeighbors
        from sklearn.linear_model import LogisticRegression
        
        df = self.data[[treatment] + confounders].dropna()
        X = df[confounders]
        treatment = df[treatment]
        
        model = LogisticRegression(max_iter=1000)
        model.fit(X, treatment)
        ps = model.predict_proba(X)[:, 1]
        
        matched = []
        treated = ps[treatment == 1]
        control = ps[treatment == 0]
        
        nn = NearestNeighbors(n_neighbors=1)
        nn.fit(control.reshape(-1, 1))
        
        for i, ps_val in enumerate(treated):
            idx = nn.kneighbors([[ps_val]])[1][0][0]
            matched.append(df.index[idx])
        
        result_df = df.loc[list(matched) + list(df[treatment == 1].index)]
        self.results['psm'] = result_df
        return result_df
    
    def generate_report(self) -> str:
        """生成分析报告"""
        if not self.results:
            return "暂无分析结果"
        
        report = "=" * 50 + "\n"
        report += "Evidence Engine 分析报告\n"
        report += "=" * 50 + "\n\n"
        
        for key, value in self.results.items():
            report += f"【{key}】\n"
            report += f"{value}\n\n"
        
        return report


def demo():
    """演示"""
    # 创建模拟数据
    np.random.seed(42)
    n = 500
    
    data = pd.DataFrame({
        'patient_id': range(1, n + 1),
        'age': np.random.randint(18, 80, n),
        'sex': np.random.choice(['M', 'F'], n),
        'treatment': np.random.choice(['A', 'B'], n),
        'outcome': np.random.choice([0, 1], n, p=[0.6, 0.4]),
        'survival_days': np.random.exponential(100, n),
        'event': np.random.choice([0, 1], n, p=[0.7, 0.3]),
        'baseline_severity': np.random.randint(1, 5, n)
    })
    
    # 分析
    analyzer = EvidenceAnalyzer()
    analyzer.load_data(data)
    
    print("1. 描述性统计:")
    print(analyzer.descriptive_stats(['age', 'survival_days']))
    print("\n2. 均值比较:")
    print(analyzer.compare_means('age', 'treatment'))
    print("\n3. 卡方检验:")
    print(analyzer.chi_square('outcome', 'treatment'))
    print("\n4. 回归分析:")
    print(analyzer.logistic_regression('outcome', ['age', 'baseline_severity']))
    
    return analyzer


if __name__ == "__main__":
    demo()
