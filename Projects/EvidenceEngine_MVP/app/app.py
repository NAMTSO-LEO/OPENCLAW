"""
Evidence Engine MVP - Web界面
基于Streamlit的医疗证据分析应用
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# 添加core路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.analyzer import EvidenceAnalyzer

# 页面配置
st.set_page_config(
    page_title="Evidence Engine - 医疗证据分析",
    page_icon="🏥",
    layout="wide"
)

# 标题
st.title("🏥 Evidence Engine MVP")
st.markdown("**医疗证据操作系统** - 真实世界数据分析平台")

# 侧边栏
st.sidebar.title("功能导航")
page = st.sidebar.radio(
    "选择功能",
    ["数据上传", "描述性统计", "组间比较", "回归分析", "生存分析", "报告生成"]
)

# 初始化分析器
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = EvidenceAnalyzer()
    st.session_state.data_loaded = False

# ============ 数据上传 ============
if page == "数据上传":
    st.header("📁 数据上传")
    
    uploaded_file = st.file_uploader("上传CSV/Excel文件", type=['csv', 'xlsx'])
    
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.session_state.analyzer.load_data(df)
            st.session_state.data_loaded = True
            
            st.success(f"✅ 成功加载数据: {df.shape[0]} 行, {df.shape[1]} 列")
            
            st.subheader("数据预览")
            st.dataframe(df.head(10))
            
            st.subheader("数据类型")
            st.dataframe(df.dtypes)
            
        except Exception as e:
            st.error(f"加载失败: {e}")
    
    # 演示数据
    if st.checkbox("使用演示数据"):
        np.random.seed(42)
        n = 500
        df = pd.DataFrame({
            'patient_id': range(1, n + 1),
            'age': np.random.randint(18, 80, n),
            'sex': np.random.choice(['M', 'F'], n),
            'treatment': np.random.choice(['A', 'B'], n),
            'outcome': np.random.choice([0, 1], n, p=[0.6, 0.4]),
            'survival_days': np.random.exponential(100, n),
            'event': np.random.choice([0, 1], n, p=[0.7, 0.3]),
            'baseline_severity': np.random.randint(1, 5, n)
        })
        st.session_state.analyzer.load_data(df)
        st.session_state.data_loaded = True
        st.success("✅ 演示数据已加载")

# ============ 描述性统计 ============
elif page == "描述性统计":
    st.header("📊 描述性统计")
    
    if not st.session_state.data_loaded:
        st.warning("请先上传数据")
    else:
        df = st.session_state.analyzer.data
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        variables = st.multiselect("选择变量", numeric_cols, default=numeric_cols[:5])
        
        if st.button("计算统计量"):
            result = st.session_state.analyzer.descriptive_stats(variables)
            st.dataframe(result)
            
            # 可视化
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, len(variables), figsize=(4*len(variables), 4))
            if len(variables) == 1:
                axes = [axes]
            for ax, var in zip(axes, variables):
                ax.hist(df[var].dropna(), bins=20, edgecolor='black')
                ax.set_title(var)
            st.pyplot(fig)

# ============ 组间比较 ============
elif page == "组间比较":
    st.header("🔬 组间比较")
    
    if not st.session_state.data_loaded:
        st.warning("请先上传数据")
    else:
        df = st.session_state.analyzer.data
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        all_cols = df.columns.tolist()
        
        col1, col2 = st.columns(2)
        with col1:
            test_type = st.selectbox("检验类型", ["均值比较(t检验)", "卡方检验"])
        with col2:
            if test_type == "均值比较(t检验)":
                var = st.selectbox("数值变量", numeric_cols)
                group = st.selectbox("分组变量", all_cols)
            else:
                var = st.selectbox("分类变量", all_cols)
                group = st.selectbox("分组变量", all_cols)
        
        if st.button("执行检验"):
            try:
                if test_type == "均值比较(t检验)":
                    result = st.session_state.analyzer.compare_means(var, group)
                    st.success(f"p值: {result['p_value']:.4f}")
                    if result['significant']:
                        st.warning("✅ 组间差异显著")
                    else:
                        st.info("❌ 组间差异不显著")
                else:
                    result = st.session_state.analyzer.chi_square(var, group)
                    st.success(f"χ² = {result['chi2']:.2f}, p = {result['p_value']:.4f}")
                    st.dataframe(result['contingency_table'])
            except Exception as e:
                st.error(f"错误: {e}")

# ============ 回归分析 ============
elif page == "回归分析":
    st.header("📈 回归分析")
    
    if not st.session_state.data_loaded:
        st.warning("请先上传数据")
    else:
        df = st.session_state.analyzer.data
        all_cols = df.columns.tolist()
        
        method = st.selectbox("方法", ["Logistic回归", "线性回归", "Cox回归"])
        
        if method == "Logistic回归":
            y = st.selectbox("因变量(二分类)", all_cols)
            x_vars = st.multiselect("自变量", all_cols, default=all_cols[:2])
            
            if st.button("运行回归"):
                result = st.session_state.analyzer.logistic_regression(y, x_vars)
                st.success("回归完成")
                st.json(result)

# ============ 生存分析 ============
elif page == "生存分析":
    st.header("⏱️ 生存分析")
    
    if not st.session_state.data_loaded:
        st.warning("请先上传数据")
    else:
        df = st.session_state.analyzer.data
        all_cols = df.columns.tolist()
        
        time_var = st.selectbox("时间变量", all_cols)
        event_var = st.selectbox("事件变量", all_cols)
        group = st.selectbox("分组变量(可选)", ["无"] + all_cols)
        
        if st.button("执行生存分析"):
            try:
                result = st.session_state.analyzer.survival_analysis(
                    time_var, event_var, None if group == "无" else group
                )
                st.success(f"中位生存时间: {result['median_survival']:.1f} 天")
                st.json(result)
            except Exception as e:
                st.error(f"错误: {e}")

# ============ 报告生成 ============
elif page == "报告生成":
    st.header("📄 报告生成")
    
    if st.button("生成分析报告"):
        report = st.session_state.analyzer.generate_report()
        st.text_area("分析报告", report, height=400)
        
        # 下载
        st.download_button("下载报告", report, "evidence_engine_report.txt")

# 底部
st.markdown("---")
st.markdown("*Evidence Engine MVP v0.1 | 医疗证据分析平台*")
