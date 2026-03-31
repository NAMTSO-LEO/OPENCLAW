#!/usr/bin/env python3
"""
临床辅助决策系统 v2.0 - 增强版
Enhanced Clinical Decision Support System
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

from enhanced_clinical_engine import EnhancedClinicalEngine, Patient

# 页面配置
st.set_page_config(
    page_title="临床辅助决策系统 v2.0",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .disclaimer {
        background: linear-gradient(90deg, #fff3cd, #ffeeba);
        border: 2px solid #ffc107;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .vital-box {
        background: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .diagnosis-box {
        background: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .treatment-box {
        background: #f3e5f5;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .warning-box {
        background: #ffebee;
        border-left: 4px solid #f44336;
        padding: 10px;
        margin: 10px 0;
    }
    .triage-red { background: #ffcdd2; border: 2px solid #f44336; padding: 20px; border-radius: 10px; }
    .triage-orange { background: #ffe0b2; border: 2px solid #ff9800; padding: 20px; border-radius: 10px; }
    .triage-yellow { background: #fff9c4; border: 2px solid #ffeb3b; padding: 20px; border-radius: 10px; }
    .triage-green { background: #c8e6c9; border: 2px solid #4caf50; padding: 20px; border-radius: 10px; }
    .stButton>button { width: 100%; }
    .report-box {
        background: #263238;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

# 初始化
@st.cache_resource
def get_engine():
    return EnhancedClinicalEngine()

engine = get_engine()

# 标题
st.title("🏥 临床辅助决策系统 v2.0")
st.markdown("### Enhanced Clinical Decision Support System")

# 免责声明
st.markdown("""
<div class="disclaimer">
    <h4>⚠️ 免责声明</h4>
    <p>本系统仅供临床辅助参考，不替代医生判断。使用前请确认患者情况，必要时请咨询上级医师。</p>
</div>
""", unsafe_allow_html=True)

# 侧边栏
st.sidebar.title("📋 功能菜单")
mode = st.sidebar.radio(
    "选择功能",
    [
        "🔬 智能诊断",
        "🚑 急诊分诊", 
        "💊 治疗方案",
        "💉 药物相互作用",
        "📊 ML疾病预测",
        "📋 临床报告"
    ]
)

# ========== 智能诊断 ==========
if mode == "🔬 智能诊断":
    st.header("🔬 智能诊断系统")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("👤 患者信息")
        name = st.text_input("姓名")
        age = st.number_input("年龄", 1, 100, 50)
        gender = st.radio("性别", ["男", "女"])
        chief_complaint = st.text_area("主诉", placeholder="如：胸痛伴发热2天")
        
    with col2:
        st.subheader("🌡️ 症状选择")
        col_a, col_b = st.columns(2)
        with col_a:
            fever = st.checkbox("发热")
            chills = st.checkbox("寒战")
            cough = st.checkbox("咳嗽")
            sputum = st.checkbox("咳痰")
            chest_pain = st.checkbox("胸痛")
            dyspnea = st.checkbox("呼吸困难")
        with col_b:
            headache = st.checkbox("头痛")
            dizziness = st.checkbox("头晕")
            nausea = st.checkbox("恶心")
            vomiting = st.checkbox("呕吐")
            abdominal_pain = st.checkbox("腹痛")
            diarrhea = st.checkbox("腹泻")
            fatigue = st.checkbox("乏力")
            weight_loss = st.checkbox("体重下降")
    
    st.subheader("📝 既往史")
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1:
        hypertension = st.checkbox("高血压")
        diabetes = st.checkbox("糖尿病")
    with col_h2:
        coronary_heart_disease = st.checkbox("冠心病")
        stroke = st.checkbox("脑卒中")
    with col_h3:
        copd = st.checkbox("慢阻肺")
        smoking = st.checkbox("吸烟")
    
    if st.button("🔍 开始诊断", type="primary"):
        patient = Patient(
            name=name,
            age=age,
            gender=1 if gender == "女" else 0,
            chief_complaint=chief_complaint,
            fever=int(fever),
            cough=int(cough),
            chest_pain=int(chest_pain),
            dyspnea=int(dyspnea),
            headache=int(headache),
            nausea=int(nausea),
            vomiting=int(vomiting),
            abdominal_pain=int(abdominal_pain),
            diarrhea=int(diarrhea),
            fatigue=int(fatigue),
            weight_loss=int(weight_loss),
            hypertension=int(hypertension),
            diabetes=int(diabetes),
            coronary_heart_disease=int(coronary_heart_disease),
            stroke=int(stroke),
            copd=int(copd),
            smoking=int(smoking)
        )
        
        result = engine.diagnose(patient)
        
        st.divider()
        
        # 显示结果
        st.markdown(f"""
        <div class="diagnosis-box">
            <h3>🎯 诊断结果</h3>
            <p><strong>症状:</strong> {', '.join(result['symptoms']) if result['symptoms'] else '无明显症状'}</p>
            <p><strong>可能疾病:</strong></p>
            <ul>
            {"".join([f"<li>{d}</li>" for d in result['possible_diseases']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if result['reasoning']:
            st.subheader("🧠 诊断推理")
            for r in result['reasoning']:
                st.info(f"• {r}")

# ========== 急诊分诊 ==========
elif mode == "🚑 急诊分诊":
    st.header("🚑 急诊分诊系统")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("👤 基本信息")
        age_t = st.number_input("年龄", 1, 100, 60, key="triage_age")
        gender_t = st.radio("性别", ["男", "女"], key="triage_gender")
        
        st.subheader("🌡️ 生命体征")
        hr_t = st.number_input("心率 (bpm)", 30, 220, 90, key="triage_hr")
        sbp_t = st.number_input("收缩压 (mmHg)", 60, 280, 130, key="triage_sbp")
        dbp_t = st.number_input("舒张压 (mmHg)", 30, 150, 80, key="triage_dbp")
        spo2_t = st.number_input("血氧 (%)", 70, 100, 96, key="triage_spo2")
        temp_t = st.number_input("体温 (°C)", 34.0, 42.0, 36.8, key="triage_temp")
    
    with col2:
        st.subheader("😰 主要症状")
        chest_pain_t = st.checkbox("胸痛", key="tp_chest")
        dyspnea_t = st.checkbox("呼吸困难", key="tp_dyspnea")
        abdominal_pain_t = st.checkbox("剧烈腹痛", key="tp_abdominal")
        headache_t = st.checkbox("剧烈头痛", key="tp_headache")
        vomiting_t = st.checkbox("反复呕吐", key="tp_vomit")
        
        st.subheader("📋 既往史")
        hypertension_t = st.checkbox("高血压", key="tp_hyper")
        diabetes_t = st.checkbox("糖尿病", key="tp_diab")
        copd_t = st.checkbox("慢阻肺", key="tp_copd")
        kidney_t = st.checkbox("肾病", key="tp_kidney")
    
    if st.button("🚨 开始分诊", type="primary"):
        patient = Patient(
            age=age_t,
            gender=1 if gender_t == "女" else 0,
            hr=hr_t,
            sbp=sbp_t,
            dbp=dbp_t,
            spo2=spo2_t,
            temp=temp_t,
            chest_pain=int(chest_pain_t),
            dyspnea=int(dyspnea_t),
            abdominal_pain=int(abdominal_pain_t),
            headache=int(headache_t),
            vomiting=int(vomiting_t),
            hypertension=int(hypertension_t),
            diabetes=int(diabetes_t),
            copd=int(copd_t),
            kidney_disease=int(kidney_t)
        )
        
        result = engine.triage(patient)
        
        st.divider()
        
        # 分级显示
        color_map = {"🔴": "triage-red", "🟠": "triage-orange", "🟡": "triage-yellow", "🟢": "triage-green"}
        
        st.markdown(f"""
        <div class="{color_map.get(result['color'], 'triage-green')}">
            <h2>{result['color']} {result['level']}</h2>
            <h3>{result['description']}</h3>
            <p><strong>评分:</strong> {result['score']} 分</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("⚠️ 需要关注的指标:")
        for r in result['reasons']:
            st.warning(f"• {r}")
        
        st.subheader("📊 生命体征:")
        col_v1, col_v2, col_v3, col_v4 = st.columns(4)
        with col_v1:
            st.metric("心率", f"{result['vital_signs']['hr']} bpm")
        with col_v2:
            st.metric("血压", f"{result['vital_signs']['sbp']}/{result['vital_signs']['dbp']}")
        with col_v3:
            st.metric("血氧", f"{result['vital_signs']['spo2']}%")
        with col_v4:
            st.metric("体温", f"{result['vital_signs']['temp']}°C")

# ========== 治疗方案 ==========
elif mode == "💊 治疗方案":
    st.header("💊 治疗方案")
    
    disease = st.selectbox(
        "选择疾病",
        ["冠心病", "高血压", "糖尿病", "肺炎", "脑卒中", "慢阻肺", "哮喘", 
         "胃炎/胃溃疡", "甲亢", "甲减", "冠心病", "心律失常"]
    )
    
    # 简单患者信息用于检查过敏
    with st.expander("患者过敏信息 (可选)"):
        allergies = st.text_input("过敏药物，用逗号分隔", placeholder="如：青霉素,磺胺类")
    
    patient = Patient()
    if allergies:
        patient.allergies = [a.strip() for a in allergies.split(',')]
    
    if st.button("📋 获取治疗方案", type="primary"):
        result = engine.get_treatment_plan(disease, patient)
        
        st.divider()
        
        st.subheader(f"💊 {result['disease']} 治疗方案")
        
        if result['protocol']:
            for phase, treatments in result['protocol'].items():
                st.markdown(f"**{phase}:**")
                for t in treatments:
                    st.write(f"  • {t}")
        
        if result.get('notes'):
            for note in result['notes']:
                st.warning(note)
        
        if not result['protocol']:
            st.info("暂无详细治疗方案，请咨询专科医生")

# ========== 药物相互作用 ==========
elif mode == "💉 药物相互作用":
    st.header("💉 药物相互作用检查")
    
    col1, col2 = st.columns(2)
    
    with col1:
        drug1 = st.selectbox(
            "药物1",
            ["阿司匹林", "华法林", "布洛芬", "地高辛", "胺碘酮", "他汀类", 
             "红霉素", "ACEI类", "螺内酯", "NSAID类", "β受体阻滞剂", "胰岛素"]
        )
    
    with col2:
        drug2 = st.selectbox(
            "药物2",
            ["华法林", "阿司匹林", "维生素K", "布洛芬", "胺碘酮", "红霉素",
             "螺内酯", "利尿剂", "氟喹诺酮", "对乙酰氨基酚", "酒精", "西柚"]
        )
    
    if st.button("🔍 检查相互作用", type="primary"):
        result = engine.check_drug_interaction(drug1, drug2)
        
        st.divider()
        
        if result:
            st.markdown(f"""
            <div class="warning-box">
                <h3>⚠️ 存在相互作用</h3>
                <p><strong>{drug1} + {drug2}</strong></p>
                <p>{result}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ 未发现明显相互作用")

# ========== ML疾病预测 ==========
elif mode == "📊 ML疾病预测":
    st.header("📊 ML疾病预测")
    
    st.info("使用已训练的机器学习模型进行疾病风险预测")
    
    # 选择模型
    model_names = sorted(engine.models.keys())
    selected_model = st.selectbox("选择疾病模型", model_names)
    
    st.subheader("输入特征")
    
    # 动态生成特征输入
    if selected_model in engine.models:
        features_info = engine.models[selected_model].get('features', [])
        
        if features_info:
            features = []
            cols = st.columns(3)
            
            for i, feat in enumerate(features_info[:12]):  # 最多12个
                with cols[i % 3]:
                    val = st.number_input(f"{feat}", value=0.0, step=1.0, key=f"feat_{i}")
                    features.append(val)
            
            if len(features) < len(features_info):
                features.extend([0.0] * (len(features_info) - len(features)))
            
            if st.button("🎯 开始预测", type="primary"):
                result = engine.predict_disease(selected_model, features)
                
                st.divider()
                
                if 'error' in result:
                    st.error(result['error'])
                else:
                    prob = result['probability']
                    
                    # 颜色
                    if prob > 0.7:
                        color = "🔴 高风险"
                        bg = "triage-red"
                    elif prob > 0.4:
                        color = "🟡 中风险"
                        bg = "triage-yellow"
                    else:
                        color = "🟢 低风险"
                        bg = "triage-green"
                    
                    st.markdown(f"""
                    <div class="{bg}" style="padding: 20px; border-radius: 10px;">
                        <h3>{color}</h3>
                        <p><strong>疾病:</strong> {result['disease']}</p>
                        <p><strong>预测概率:</strong> {prob*100:.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("该模型无特征信息")
    else:
        st.error("模型不可用")

# ========== 临床报告 ==========
elif mode == "📋 临床报告":
    st.header("📋 生成临床报告")
    
    # 简化版患者信息输入
    with st.form("report_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("姓名", "患者")
            age = st.number_input("年龄", 1, 100, 50)
            gender = st.radio("性别", ["男", "女"])
            chief_complaint = st.text_area("主诉", "胸痛伴发热")
        
        with col2:
            hr = st.number_input("心率", 40, 200, 80)
            sbp = st.number_input("收缩压", 70, 250, 120)
            dbp = st.number_input("舒张压", 40, 150, 80)
            spo2 = st.number_input("血氧", 80, 100, 98)
            temp = st.number_input("体温", 35.0, 42.0, 36.5)
        
        symptoms = st.multiselect(
            "症状",
            ["发热", "咳嗽", "胸痛", "呼吸困难", "头痛", "腹痛", "恶心", "呕吐", "乏力", "头晕"]
        )
        
        submit = st.form_submit_button("📋 生成报告", type="primary")
    
    if submit:
        patient = Patient(
            name=name,
            age=age,
            gender=1 if gender == "女" else 0,
            chief_complaint=chief_complaint,
            hr=hr,
            sbp=sbp,
            dbp=dbp,
            spo2=spo2,
            temp=temp,
            fever=1 if "发热" in symptoms else 0,
            cough=1 if "咳嗽" in symptoms else 0,
            chest_pain=1 if "胸痛" in symptoms else 0,
            dyspnea=1 if "呼吸困难" in symptoms else 0,
            headache=1 if "头痛" in symptoms else 0,
            abdominal_pain=1 if "腹痛" in symptoms else 0,
            nausea=1 if "恶心" in symptoms else 0,
            vomiting=1 if "呕吐" in symptoms else 0,
            fatigue=1 if "乏力" in symptoms else 0,
            dizziness=1 if "头晕" in symptoms else 0
        )
        
        report = engine.generate_report(patient)
        
        st.divider()
        
        st.markdown(f"""
        <div class="report-box">
            <pre>{report}</pre>
        </div>
        """, unsafe_allow_html=True)
        
        # 下载按钮
        st.download_button(
            "📥 下载报告",
            report,
            f"临床报告_{name}_{pd.Timestamp.now().strftime('%Y%m%d%H%M')}.txt",
            "text/plain"
        )

# 页脚
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>🏥 临床辅助决策系统 v2.0 | Enhanced Clinical Decision Support</p>
    <p>基于机器学习 + 临床知识库 | 56个疾病预测模型</p>
    <p>⚠️ 本系统仅供辅助参考，不替代专业医疗判断</p>
</div>
""", unsafe_allow_html=True)
