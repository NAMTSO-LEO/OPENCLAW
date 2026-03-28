# Landmark Analysis Code
# irAE无具体时间时的替代方案

import pandas as pd
import numpy as np
from lifelines import CoxPHFitter

# ============================================================
# Landmark Analysis - 3个月和6个月
# ============================================================

def landmark_analysis(df, landmark_months=3):
    """
    Landmark analysis: 只纳入在landmark时间点仍存活的患者
    """
    df_landmark = df.copy()
    
    # 只纳入landmark时间点仍存活的患者
    df_landmark = df_landmark[df_landmark['os_time'] > landmark_months]
    
    # 设置landmrk时间点后的新结局
    df_landmark['landmark_time'] = landmark_months
    df_landmark['landmark_event'] = df_landmark.apply(
        lambda x: x['os_event'] if x['os_time'] <= landmark_months * 2 else 0, 
        axis=1
    )
    
    # 或简化为：landmark时间点后6个月内的结局
    # df_landmark['landmark_event'] = ((df_landmark['os_time'] > landmark_months) & 
    #                               (df_landmark['os_time'] <= landmark_months * 2) &
    #                               (df_landmark['os_event'] == 1)).astype(int)
    
    # 同时处理irAE作为landmark时的固定暴露
    # 如果3个月时已发生irAE则为1，否则为0
    df_landmark['irae_landmark'] = (df_landmark['irae_time'] <= landmark_months).astype(int)
    df_landmark['irae_landmark'] = df_landmark['irae_landmark'].fillna(0)
    
    return df_landmark

# ============================================================
# 主分析
# ============================================================

if __name__ == "__main__":
    # 读取数据
    df = pd.read_csv("simulated_rr_dlbcl_pd1_irae.csv")
    
    print("=== Landmark Analysis (3个月) ===")
    df_3m = landmark_analysis(df, landmark_months=3)
    
    # Cox回归
    cph = CoxPHFitter()
    cph.fit(df_3m, duration_col='os_time', event_col='os_event', 
             formula='pd1_treatment + irae_landmark')
    
    print(f"样本量: {len(df_3m)}")
    print(cph.summary[['coef', 'se(coef)', 'exp(coef)']])
    
    print("\n=== Landmark Analysis (6个月) ===")
    df_6m = landmark_analysis(df, landmark_months=6)
    
    cph6 = CoxPHFitter()
    cph6.fit(df_6m, duration_col='os_time', event_col='os_event',
             formula='pd1_treatment + irae_landmark')
    
    print(f"样本量: {len(df_6m)}")
    print(cph6.summary[['coef', 'se(coef)']])

# ============================================================
# 结果解读
# ============================================================

"""
Landmark Analysis结果解读：
- 在3个月landmark时暴露vs未暴露的HR
- 在6个月landmark时暴露vs未暴露的HR
- 与主要time-dependent分析对比
- 在Discussion中说明这是敏感性分析之一
"""

print("✅ Landmark分析完成")