"""
Evidence Engine - Complete Clinical Decision Support System
10 Common Diseases Dashboard
MVP v2.0 - Full Version
"""

import streamlit as st
import sys
import os

# Add path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import all disease engines
from engine.diseases.chest_pain.chest_pain import ChestPainEngine, create_chestpain_from_dict
from engine.diseases.heart_failure.heart_failure import HeartFailureEngine, create_hf_from_dict
from engine.diseases.afib.afib import AFEngine, create_af_from_dict
from engine.diseases.hypertension.hypertension import HypertensionEngine, create_htn_from_dict
from engine.diseases.pe.pe import PEEngine, create_pe_from_dict
from engine.diseases.stroke.stroke import StrokeEngine, create_stroke_from_dict
from engine.diseases.diabetes.diabetes import DiabetesEngine, create_diabetes_from_dict
from engine.diseases.sepsis.sepsis import SepsisEngine, create_sepsis_from_dict
from engine.diseases.respiratory.respiratory import RespiratoryEngine, create_respiratory_from_dict
from engine.tachycardia.tachycardia_engine import TachycardiaEngine, Patient as TachyPatient


# Page config
st.set_page_config(
    page_title="Evidence Engine - 临床决策支持系统",
    page_icon="🏥",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .risk-high { background-color: #ffcccc; padding: 15px; border-radius: 10px; border-left: 5px solid red; }
    .risk-medium { background-color: #fff3cc; padding: 15px; border-radius: 10px; border-left: 5px solid orange; }
    .risk-low { background-color: #ccffcc; padding: 15px; border-radius: 10px; border-left: 5px solid green; }
    .disease-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 10px 0; }
    .evidence-box { background-color: #f5f5f5; padding: 10px; border-radius: 5px; font-size: 12px; margin: 5px 0; }
    h1 { color: #1f77b4; }
    .stButton>button { width: 100%; }
</style>
""", unsafe_allow_html=True)


def main():
    """Main function"""
    
    st.title("🏥 Evidence Engine - 临床决策支持系统")
    st.markdown("**10种常见疾病诊治辅助系统** | MVP v2.0")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 疾病选择")
        
        disease = st.selectbox(
            "选择疾病",
            [
                "心动过速 (Tachycardia)",
                "胸痛/ACS (Chest Pain)",
                "心力衰竭 (Heart Failure)",
                "房颤 (Atrial Fibrillation)",
                "高血压危象 (Hypertension)",
                "肺栓塞 (Pulmonary Embolism)",
                "脑卒中 (Stroke)",
                "糖尿病急症 (Diabetes)",
                "脓毒症 (Sepsis)",
                "呼吸衰竭 (Respiratory Failure)"
            ]
        )
        
        st.markdown("---")
        st.markdown("### ⚠️ 重要提示")
        st.error("本系统仅供临床辅助参考，不替代医生诊断和处方！")
        
        st.markdown("---")
        st.markdown("### 📚 疾病模块")
        st.info("""
        ✅ 心动过速 - 已完成
        ✅ 胸痛/ACS - 已完成
        ✅ 心力衰竭 - 已完成
        ✅ 房颤 - 已完成
        ✅ 高血压危象 - 已完成
        ✅ 肺栓塞 - 已完成
        ✅ 脑卒中 - 已完成
        ✅ 糖尿病急症 - 已完成
        ✅ 脓毒症 - 已完成
        ✅ 呼吸衰竭 - 已完成
        """)
    
    # Route to disease-specific pages
    if "心动过速" in disease:
        tachycardia_page()
    elif "胸痛" in disease:
        chest_pain_page()
    elif "心力" in disease:
        heart_failure_page()
    elif "房颤" in disease:
        afib_page()
    elif "高血压" in disease:
        hypertension_page()
    elif "肺栓塞" in disease:
        pe_page()
    elif "卒中" in disease:
        stroke_page()
    elif "糖尿病" in disease:
        diabetes_page()
    elif "脓毒症" in disease:
        sepsis_page()
    elif "呼吸" in disease:
        respiratory_page()


def tachycardia_page():
    """心动过速页面"""
    st.header("❤️ 心动过速诊治决策支持")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("患者信息输入")
        
        age = st.number_input("年龄", 0, 120, 65)
        gender = st.selectbox("性别", ["male", "female"], format_func=lambda x: "男" if x == "male" else "女")
        hr = st.number_input("心率 (bpm)", 0, 250, 168)
        sbp = st.number_input("收缩压 (mmHg)", 0, 250, 120)
        
        symptoms = st.multiselect("症状", ["心悸", "胸痛", "胸闷", "呼吸困难", "晕厥", "出汗"], default=["心悸", "胸闷"])
        
        qrs = st.radio("QRS", ["narrow", "wide"], format_func=lambda x: "窄QRS" if x == "narrow" else "宽QRS")
        rhythm = st.radio("节律", ["regular", "irregular"], format_func=lambda x: "规则" if x == "regular" else "不规则")
    
    with col2:
        if st.button("🔍 运行分析", type="primary"):
            # 创建患者
            patient = TachyPatient(
                age=age, gender=gender, hr=hr, sbp=sbp, dbp=80, spo2=95,
                symptoms=symptoms, ecg=f"{'规则' if rhythm == 'regular' else '不规则'}{qrs}心动过速",
                history=[]
            )
            
            engine = TachycardiaEngine()
            result = engine.analyze(patient)
            
            display_result(result)
    
    st.markdown("---")
    st.info("💡 使用说明：输入患者信息后点击「运行分析」查看诊治建议")


def chest_pain_page():
    """胸痛/ACS页面"""
    st.header("❤️ 胸痛/急性冠脉综合征")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("患者信息")
        
        age = st.number_input("年龄", 0, 120, 65)
        gender = st.selectbox("性别", ["male", "female"], format_func=lambda x: "男" if x == "male" else "女")
        
        st.subheader("症状")
        chest_pain = st.checkbox("胸痛/胸闷")
        dyspnea = st.checkbox("呼吸困难")
        nausea = st.checkbox("恶心/呕吐")
        diaphoresis = st.checkbox("出汗")
        
        st.subheader("生命体征")
        hr = st.number_input("心率", 0, 200, 80)
        sbp = st.number_input("收缩压", 0, 250, 120)
        
        st.subheader("心电图")
        st_elevation = st.checkbox("ST段抬高")
        st_depression = st.checkbox("ST段压低")
        
        st.subheader("病史")
        cad = st.checkbox("冠心病史")
        diabetes = st.checkbox("糖尿病")
        hypertension = st.checkbox("高血压")
        
        troponin = st.selectbox("肌钙蛋白", ["normal", "elevated", "pending"])
    
    with col2:
        if st.button("🔍 分析胸痛患者", type="primary"):
            data = {
                "age": age, "gender": gender, "chest_pain": chest_pain, "dyspnea": dyspnea,
                "nausea": nausea, "diaphoresis": diaphoresis, "hr": hr, "sbp": sbp,
                "st_elevation": st_elevation, "st_depression": st_depression,
                "cad_history": cad, "diabetes": diabetes, "hypertension": hypertension,
                "troponin": troponin
            }
            
            engine = ChestPainEngine()
            result = engine.analyze(create_chestpain_from_dict(data))
            
            display_result(result)


def heart_failure_page():
    """心衰页面"""
    st.header("💓 心力衰竭")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 70)
        dyspnea = st.checkbox("呼吸困难")
        orthopnea = st.checkbox("端坐呼吸")
        edema = st.checkbox("下肢水肿")
        
        hr = st.number_input("心率", 0, 200, 90)
        sbp = st.number_input("收缩压", 0, 250, 110)
        spo2 = st.number_input("SpO2 (%)", 0, 100, 95)
        
        rales = st.checkbox("肺部啰音")
        jugular_venous = st.checkbox("颈静脉怒张")
        
        echo_ef = st.slider("射血分数 (%)", 10, 70, 35)
    
    with col2:
        if st.button("🔍 分析心衰", type="primary"):
            data = {
                "age": age, "gender": "male", "dyspnea": dyspnea, "orthopnea": orthopnea,
                "edema": edema, "hr": hr, "sbp": sbp, "spo2": spo2,
                "rales": rales, "jugular_venous": jugular_venous, "echo_ef": echo_ef
            }
            
            engine = HeartFailureEngine()
            result = engine.analyze(create_hf_from_dict(data))
            
            display_result(result)


def afib_page():
    """房颤页面"""
    st.header("💓 心房颤动")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 70)
        gender = st.selectbox("性别", ["male", "female"], format_func=lambda x: "男" if x == "male" else "女")
        
        hr = st.number_input("心室率", 0, 200, 130)
        
        st.subheader("CHA2DS2-VASc因素")
        heart_failure = st.checkbox("心衰")
        hypertension = st.checkbox("高血压")
        age_75 = st.checkbox("≥75岁")
        diabetes = st.checkbox("糖尿病")
        stroke_tia = st.checkbox("卒中/TIA")
        
        duration = st.selectbox("房颤持续时间", ["<48h", ">48h", "unknown"])
    
    with col2:
        if st.button("🔍 分析房颤", type="primary"):
            data = {
                "age": age, "gender": gender, "heart_failure": heart_failure,
                "hypertension": hypertension, "age_75": age_75,
                "diabetes": diabetes, "stroke_tia": stroke_tia,
                "duration": duration, "female": gender == "female"
            }
            
            engine = AFEngine()
            result = engine.analyze(create_af_from_dict(data))
            
            display_result(result)


def hypertension_page():
    """高血压危象页面"""
    st.header("💉 高血压危象")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 60)
        sbp = st.number_input("收缩压 (mmHg)", 0, 300, 200)
        dbp = st.number_input("舒张压 (mmHg)", 0, 150, 120)
        
        st.subheader("症状")
        headache = st.checkbox("头痛")
        visual_changes = st.checkbox("视物模糊")
        chest_pain = st.checkbox("胸痛")
        dyspnea = st.checkbox("呼吸困难")
        neurological = st.checkbox("意识障碍")
        
        st.subheader("靶器官损害")
        acute_renal = st.checkbox("急性肾损伤")
        acute_pulmonary = st.checkbox("急性肺水肿")
        encephalopathy = st.checkbox("脑病")
    
    with col2:
        if st.button("🔍 分析高血压", type="primary"):
            data = {
                "age": age, "gender": "male", "sbp": sbp, "dbp": dbp,
                "headache": headache, "visual_changes": visual_changes,
                "chest_pain": chest_pain, "dyspnea": dyspnea,
                "neurological": neurological, "acute_renal": acute_renal,
                "acute_pulmonary": acute_pulmonary, "encephalopathy": encephalopathy
            }
            
            engine = HypertensionEngine()
            result = engine.analyze(create_htn_from_dict(data))
            
            display_result(result)


def pe_page():
    """肺栓塞页面"""
    st.header("🫁 肺栓塞")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 55)
        dyspnea = st.checkbox("呼吸困难")
        pleuritic = st.checkbox("胸膜性胸痛")
        syncope = st.checkbox("晕厥")
        leg_swelling = st.checkbox("下肢肿胀")
        
        hr = st.number_input("心率", 0, 200, 110)
        sbp = st.number_input("收缩压", 0, 250, 100)
        spo2 = st.number_input("SpO2", 0, 100, 92)
        
        d_dimer = st.selectbox("D-二聚体", ["not_done", "normal", "elevated"])
        
        prior_pe = st.checkbox("既往PE/DVT")
        recent_surgery = st.checkbox("近期手术")
        cancer = st.checkbox("肿瘤")
    
    with col2:
        if st.button("🔍 分析肺栓塞", type="primary"):
            data = {
                "age": age, "gender": "male", "dyspnea": dyspnea,
                "pleuritic_chest_pain": pleuritic, "syncope": syncope,
                "leg_swelling": leg_swelling, "hr": hr, "sbp": sbp,
                "spo2": spo2, "d_dimer": d_dimer, "prior_pe_dvt": prior_pe,
                "recent_surgery": recent_surgery, "cancer": cancer
            }
            
            engine = PEEngine()
            result = engine.analyze(create_pe_from_dict(data))
            
            display_result(result)


def stroke_page():
    """脑卒中页面"""
    st.header("🧠 脑卒中")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 65)
        
        st.subheader("症状")
        facial_droop = st.checkbox("面瘫")
        arm_weakness = st.checkbox("肢体无力")
        speech = st.checkbox("言语障碍")
        
        st.subheader("检查")
        ct_done = st.checkbox("CT已完成")
        ct_result = st.selectbox("CT结果", ["normal", "hemorrhage", "early_changes"])
        
        nihss = st.slider("NIHSS评分", 0, 42, 5)
        
        afib = st.checkbox("房颤史")
        hypertension = st.checkbox("高血压史")
    
    with col2:
        if st.button("🔍 分析卒中", type="primary"):
            data = {
                "age": age, "gender": "male", "facial_droop": facial_droop,
                "arm_weakness": arm_weakness, "speech_difficulty": speech,
                "ct_done": ct_done, "ct_result": ct_result,
                "nihss_score": nihss, "atrial_fibrillation": afib,
                "hypertension": hypertension, "sbp": 150, "glucose": 100
            }
            
            engine = StrokeEngine()
            result = engine.analyze(create_stroke_from_dict(data))
            
            display_result(result)


def diabetes_page():
    """糖尿病急症页面"""
    st.header("🩸 糖尿病急症")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 35)
        diabetes_type = st.selectbox("糖尿病类型", ["T1", "T2", "gestational"])
        
        st.subheader("症状")
        polyuria = st.checkbox("多尿")
        polydipsia = st.checkbox("多饮")
        nausea = st.checkbox("恶心/呕吐")
        confusion = st.checkbox("意识障碍")
        
        glucose = st.number_input("血糖 (mg/dL)", 0, 1000, 250)
        
        ketone = st.selectbox("血酮", ["negative", "positive"])
        
        ph = st.number_input("动脉血pH", 6.5, 7.6, 7.4, step=0.01)
        
        infection = st.checkbox("感染诱因")
    
    with col2:
        if st.button("🔍 分析糖尿病急症", type="primary"):
            data = {
                "age": age, "gender": "male", "diabetes_type": diabetes_type,
                "polyuria": polyuria, "polydipsia": polydipsia,
                "nausea": nausea, "confusion": confusion,
                "glucose": glucose, "ketone": ketone,
                "abg_ph": ph, "infection": infection
            }
            
            engine = DiabetesEngine()
            result = engine.analyze(create_diabetes_from_dict(data))
            
            display_result(result)


def sepsis_page():
    """脓毒症页面"""
    st.header("🦠 脓毒症")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 65)
        
        st.subheader("症状/体征")
        fever = st.checkbox("发热")
        hypothermia = st.checkbox("低热")
        altered_mental = st.checkbox("意识改变")
        
        hr = st.number_input("心率", 0, 200, 110)
        sbp = st.number_input("收缩压", 0, 250, 90)
        rr = st.number_input("呼吸频率", 0, 50, 24)
        
        st.subheader("感染源")
        source = st.selectbox("感染源", ["unknown", "respiratory", "urinary", "abdominal", "skin"])
        
        lactate = st.number_input("乳酸 (mmol/L)", 0.0, 20.0, 3.0, step=0.1)
    
    with col2:
        if st.button("🔍 分析脓毒症", type="primary"):
            data = {
                "age": age, "gender": "male", "fever": fever,
                "hypothermia": hypothermia, "altered_mental": altered_mental,
                "hr": hr, "sbp": sbp, "rr": rr, "rr_high": rr >= 22,
                "sbp_low": sbp <= 100, "source_type": source,
                "lactate": lactate
            }
            
            engine = SepsisEngine()
            result = engine.analyze(create_sepsis_from_dict(data))
            
            display_result(result)


def respiratory_page():
    """呼吸衰竭页面"""
    st.header("😮‍💨 呼吸衰竭")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        age = st.number_input("年龄", 0, 120, 70)
        
        dyspnea = st.checkbox("呼吸困难")
        cough = st.checkbox("咳嗽")
        
        hr = st.number_input("心率", 0, 200, 100)
        rr = st.number_input("呼吸频率", 0, 50, 28)
        spo2 = st.number_input("SpO2", 0, 100, 85)
        
        st.subheader("血气分析")
        pao2 = st.number_input("PaO2 (mmHg)", 0, 500, 50)
        paco2 = st.number_input("PaCO2 (mmHg)", 0, 200, 45)
        
        st.subheader("病因")
        copd = st.checkbox("慢阻肺")
        pneumonia = st.checkbox("肺炎")
        chf = st.checkbox("心衰")
    
    with col2:
        if st.button("🔍 分析呼吸衰竭", type="primary"):
            data = {
                "age": age, "gender": "male", "dyspnea": dyspnea, "cough": cough,
                "hr": hr, "rr": rr, "spo2": spo2, "pao2": pao2, "paco2": paco2,
                "copd": copd, "pneumonia": pneumonia, "chf": chf
            }
            
            engine = RespiratoryEngine()
            result = engine.analyze(create_respiratory_from_dict(data))
            
            display_result(result)


def display_result(result):
    """显示分析结果"""
    
    st.divider()
    st.header("📊 分析结果")
    
    # Clinical judgment
    if "clinical_judgment" in result:
        st.success(f"**临床判断**: {result['clinical_judgment']}")
    
    # Risk level / severity
    if "risk_level" in result:
        risk = result["risk_level"]
        color = "red" if "高" in risk else "orange" if "中" in risk else "green"
        st.markdown(f"**风险等级**: <span style='color:{color}'>{risk}</span>", unsafe_allow_html=True)
    elif "severity" in result:
        st.markdown(f"**严重程度**: {result['severity']}")
    
    st.markdown("---")
    
    # Recommendations
    if "treatments" in result:
        st.subheader("💊 治疗建议")
        for t in result["treatments"][:8]:
            priority_emoji = {1: "🔴", 2: "🟡", 3: "🟢"}.get(t.get("priority", 3), "⚪")
            content = t.get("content", str(t))
            category = t.get("category", "")
            st.write(f"{priority_emoji} **[{category}]** {content}")
    
    st.markdown("---")
    
    # Workup
    if "workup" in result:
        st.subheader("🔍 推荐检查")
        for w in result["workup"][:6]:
            p = w.get("priority", 3)
            emoji = {1: "🔴", 2: "🟡", 3: "🟢"}.get(p, "⚪")
            st.write(f"{emoji} **{w['name']}** - {w['reason']}")
    
    # Evidence
    if "evidence" in result:
        st.subheader("📚 证据依据")
        for e in result["evidence"]:
            st.markdown(f"""
            <div class="evidence-box">
                <strong>{e['title']}</strong><br>
                {e.get('key', '')}
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
