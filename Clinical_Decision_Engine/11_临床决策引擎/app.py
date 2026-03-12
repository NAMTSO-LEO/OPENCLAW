#!/usr/bin/env python3
"""
临床辅助决策系统 - Web界面
Clinical Decision Support System - Web Interface
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clinical_decision_engine import ClinicalDecisionEngine, PatientInfo

# 页面配置
st.set_page_config(
    page_title="临床辅助决策系统",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS样式
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .warning-box {
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .disclaimer {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
        padding: 10px;
        border-radius: 5px;
        font-size: 12px;
        color: #856404;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .high-risk {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
    }
    .medium-risk {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
    }
    .low-risk {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# 初始化引擎
@st.cache_resource
def get_engine():
    model_dir = '/Users/levi/.openclaw/workspace/EvidenceEngine_MVP/model_training'
    return ClinicalDecisionEngine(model_dir)

engine = get_engine()

# 标题
st.title("🏥 临床辅助决策系统")
st.markdown("### Clinical Decision Support System")

# 免责声明
st.markdown("""
<div class="disclaimer">
    ⚠️ <strong>免责声明：</strong>本系统仅供临床辅助参考，不替代医生判断。使用前请确认患者情况，必要时请咨询上级医师。
</div>
""", unsafe_allow_html=True)

# 侧边栏 - 功能选择
st.sidebar.title("功能菜单")
mode = st.sidebar.radio(
    "选择功能",
    ["🔬 疾病预测", "🚑 急诊分诊", "💊 治疗建议", "📋 病例管理"]
)

if mode == "🔬 疾病预测":
    st.header("疾病预测")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("患者信息")
        age = st.number_input("年龄", 1, 100, 50)
        gender = st.radio("性别", ["男", "女"])
        gender_val = 1 if gender == "女" else 0
        
        st.subheader("症状")
        fever = st.checkbox("发热")
        cough = st.checkbox("咳嗽")
        chest_pain = st.checkbox("胸痛")
        headache = st.checkbox("头痛")
        abdominal_pain = st.checkbox("腹痛")
        fatigue = st.checkbox("乏力")
        
    with col2:
        st.subheader("体征")
        hr = st.number_input("心率 (bpm)", 40, 200, 80)
        sbp = st.number_input("收缩压 (mmHg)", 70, 250, 120)
        dbp = st.number_input("舒张压 (mmHg)", 40, 150, 80)
        spo2 = st.number_input("血氧饱和度 (%)", 80, 100, 98)
        temp = st.number_input("体温 (°C)", 35.0, 42.0, 36.5)
        
        st.subheader("既往史")
        hypertension = st.checkbox("高血压")
        diabetes = st.checkbox("糖尿病")
        heart_disease = st.checkbox("心脏病")
        smoking = st.checkbox("吸烟")
    
    # 选择疾病
    st.subheader("选择预测疾病")
    disease_options = sorted(engine.models.keys())
    selected_disease = st.selectbox(
        "疾病类型",
        disease_options,
        index=disease_options.index("Heart Disease") if "Heart Disease" in disease_options else 0
    )
    
    if st.button("开始预测", type="primary"):
        # 创建患者对象
        patient = PatientInfo(
            age=age,
            gender=gender_val,
            fever=int(fever),
            cough=int(cough),
            chest_pain=int(chest_pain),
            headache=int(headache),
            abdominal_pain=int(abdominal_pain),
            fatigue=int(fatigue),
            hr=hr,
            sbp=sbp,
            dbp=dbp,
            spo2=spo2,
            temp=temp,
            hypertension=int(hypertension),
            diabetes=int(diabetes),
            heart_disease=int(heart_disease),
            smoking=int(smoking)
        )
        
        # 准备特征
        features = [
            age, gender_val, int(fever), int(cough), int(chest_pain),
            int(headache), int(abdominal_pain), int(fatigue), hr, sbp,
            int(hypertension), int(diabetes), int(heart_disease), int(smoking)
        ]
        
        # 预测
        result = engine.predict(selected_disease, features)
        
        # 显示结果
        st.divider()
        
        if 'error' in result:
            st.error(f"预测错误: {result['error']}")
        else:
            prob = result['probability']
            risk_level = "高" if prob > 0.7 else ("中" if prob > 0.4 else "低")
            risk_class = "high-risk" if prob > 0.7 else ("medium-risk" if prob > 0.4 else "low-risk")
            
            st.markdown(f"""
            <div class="result-box {risk_class}">
                <h3>🎯 预测结果</h3>
                <p><strong>疾病:</strong> {result['disease']}</p>
                <p><strong>风险等级:</strong> {risk_level}</p>
                <p><strong>预测概率:</strong> {prob*100:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 获取建议
            recommendations = engine.get_recommendations(selected_disease, risk_level)
            
            if recommendations['workup']:
                st.subheader("📋 建议检查")
                for item in recommendations['workup']:
                    st.write(f"- {item}")
            
            if recommendations['treatment']:
                st.subheader("💊 建议治疗")
                for item in recommendations['treatment']:
                    st.write(f"- {item}")
            
            if recommendations['referral']:
                st.subheader("🏥 转诊建议")
                for item in recommendations['referral']:
                    st.write(f"- {item}")

elif mode == "🚑 急诊分诊":
    st.header("急诊分诊")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("基本信息")
        age = st.number_input("年龄", 1, 100, 50, key="triage_age")
        gender = st.radio("性别", ["男", "女"], key="triage_gender")
        
        st.subheader("生命体征")
        hr_triage = st.number_input("心率 (bpm)", 40, 200, 80, key="triage_hr")
        sbp_triage = st.number_input("收缩压 (mmHg)", 70, 250, 120, key="triage_sbp")
        spo2_triage = st.number_input("血氧饱和度 (%)", 80, 100, 98, key="triage_spo2")
        temp_triage = st.number_input("体温 (°C)", 35.0, 42.0, 36.5, key="triage_temp")
    
    with col2:
        st.subheader("症状")
        chest_pain_triage = st.checkbox("胸痛", key="triage_chest")
        headache_triage = st.checkbox("剧烈头痛", key="triage_headache")
        abdominal_triage = st.checkbox("剧烈腹痛", key="triage_abdominal")
        dyspnea_triage = st.checkbox("呼吸困难", key="triage_dyspnea")
        
        st.subheader("既往史")
        hypertension_triage = st.checkbox("高血压", key="triage_hyper")
        diabetes_triage = st.checkbox("糖尿病", key="triage_diab")
    
    if st.button("开始分诊", type="primary"):
        patient = PatientInfo(
            age=age,
            gender=1 if gender == "女" else 0,
            hr=hr_triage,
            sbp=sbp_triage,
            spo2=spo2_triage,
            temp=temp_triage,
            chest_pain=int(chest_pain_triage),
            headache=int(headache_triage),
            abdominal_pain=int(abdominal_triage),
            hypertension=int(hypertension_triage),
            diabetes=int(diabetes_triage)
        )
        
        result = engine.triage(patient)
        
        st.divider()
        
        color_map = {
            "red": "🔴",
            "orange": "🟠",
            "yellow": "🟡",
            "green": "🟢"
        }
        
        st.markdown(f"""
        <div class="result-box">
            <h2>{color_map.get(result['color'], '⚪')} 分诊等级: {result['triage_level']}</h2>
            <p><strong>评分:</strong> {result['score']}</p>
            <p><strong>需要关注的症状:</strong></p>
            <ul>
            {"".join([f"<li>{r}</li>" for r in result['urgent_reasons']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 建议
        if result['score'] >= 3:
            st.warning("⚠️ 建议立即就医，可能需要急诊处理")

elif mode == "💊 治疗建议":
    st.header("治疗建议")
    
    disease = st.selectbox("选择疾病", sorted(engine.models.keys()))
    risk = st.select_slider("风险等级", ["低", "中", "高"])
    
    if st.button("获取建议"):
        recommendations = engine.get_recommendations(disease, risk)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 建议检查")
            if recommendations['workup']:
                for item in recommendations['workup']:
                    st.write(f"• {item}")
            else:
                st.write("暂无建议")
        
        with col2:
            st.subheader("💊 治疗方案")
            if recommendations['treatment']:
                for item in recommendations['treatment']:
                    st.write(f"• {item}")
            else:
                st.write("暂无建议")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("📊 监测建议")
            if recommendations['monitoring']:
                for item in recommendations['monitoring']:
                    st.write(f"• {item}")
            else:
                st.write("暂无建议")
        
        with col4:
            st.subheader("🏥 转诊建议")
            if recommendations['referral']:
                for item in recommendations['referral']:
                    st.write(f"• {item}")
            else:
                st.write("暂无建议")

elif mode == "📋 病例管理":
    st.header("病例管理")
    
    st.info("功能开发中... 敬请期待")
    
    # 预留
    st.markdown("""
    ### 计划功能
    - 病例记录与查询
    - 历史预测回顾
    - 病例分享与讨论
    - 数据导出
    """)

# 页脚
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>🏥 临床辅助决策系统 v1.0</p>
    <p>基于机器学习的临床决策支持工具</p>
    <p>⚠️ 本系统仅供辅助参考，不替代专业医疗判断</p>
</div>
""", unsafe_allow_html=True)
