"""
Evidence Engine - Tachycardia Care Pathway Assistant
主应用入口 - Streamlit Web界面
MVP v1.0
"""

import streamlit as st
import sys
import os
from datetime import datetime

# 添加路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.triage.triage import TriageEngine, create_patient_from_dict
from engine.rhythm.rhythm import RhythmEngine
from engine.causes.causes import CausesEngine
from engine.treatment.treatment import TreatmentEngine
from engine.evidence.evidence import EvidenceEngine


# 页面配置
st.set_page_config(
    page_title="Evidence Engine - 心动过速诊治助手",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS样式
st.markdown("""
<style>
    .risk-high { background-color: #ffcccc; padding: 15px; border-radius: 10px; border-left: 5px solid red; }
    .risk-medium { background-color: #fff3cc; padding: 15px; border-radius: 10px; border-left: 5px solid orange; }
    .risk-low { background-color: #ccffcc; padding: 15px; border-radius: 10px; border-left: 5px solid green; }
    .evidence-box { background-color: #f0f0f0; padding: 10px; border-radius: 5px; font-size: 12px; }
    .warning-box { background-color: #ffe6e6; padding: 15px; border-radius: 10px; border: 2px solid red; }
    .success-box { background-color: #e6ffe6; padding: 15px; border-radius: 10px; border: 2px solid green; }
    .info-box { background-color: #e6f3ff; padding: 15px; border-radius: 10px; }
    .card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 10px 0; }
    h1 { color: #1f77b4; }
    h2 { color: #2ca02c; }
    h3 { color: #ff7f0e; }
    .stButton>button { width: 100%; }
</style>
""", unsafe_allow_html=True)


def main():
    """主函数"""
    
    # 标题
    st.title("❤️ Evidence Engine - Tachycardia")
    st.markdown("**心动过速临床决策支持系统** | MVP v1.0")
    st.markdown("---")
    
    # 侧边栏
    with st.sidebar:
        st.header("📋 功能导航")
        page = st.radio("选择页面", ["🔬 诊治决策", "📖 病例演示", "📚 知识库", "ℹ️ 关于"])
        
        st.markdown("---")
        st.markdown("### ⚠️ 重要提示")
        st.error("本系统仅供临床辅助参考，不替代医生诊断和处方。危重患者请立即按急救流程处理！")
    
    # 页面路由
    if page == "🔬 诊治决策":
        assessment_page()
    elif page == "📖 病例演示":
        demo_cases_page()
    elif page == "📚 知识库":
        knowledge_page()
    else:
        about_page()


def assessment_page():
    """诊治决策页面"""
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 患者信息输入")
        
        # 基本信息
        st.subheader("基本信息")
        col_a, col_b = st.columns(2)
        with col_a:
            age = st.number_input("年龄 (岁)", 0, 120, 65)
        with col_b:
            gender = st.selectbox("性别", ["male", "female"], format_func=lambda x: "男" if x == "male" else "女")
        
        # 症状
        st.subheader("症状")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            chest_pain = st.checkbox("胸痛/胸闷")
            dyspnea = st.checkbox("呼吸困难")
            syncope = st.checkbox("晕厥/接近晕厥")
        with col_s2:
            palpitations = st.checkbox("心悸")
            dizziness = st.checkbox("头晕")
            sweating = st.checkbox("出汗/发热")
        
        # 生命体征
        st.subheader("生命体征")
        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            hr = st.number_input("心率 (bpm)", 0, 250, 168)
        with col_v2:
            sbp = st.number_input("收缩压 (mmHg)", 0, 250, 120)
        with col_v3:
            spo2 = st.number_input("SpO2 (%)", 0, 100, 95)
        
        dbp = st.number_input("舒张压 (mmHg)", 0, 150, 80)
        
        # ECG特征
        st.subheader("心电图特征")
        qrs = st.radio("QRS形态", ["narrow", "wide"], format_func=lambda x: "窄QRS" if x == "narrow" else "宽QRS")
        rhythm = st.radio("节律", ["regular", "irregular"], format_func=lambda x: "规则" if x == "regular" else "不规则")
        st_change = st.checkbox("ST段改变")
        
        # 病史
        st.subheader("既往史")
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            cad = st.checkbox("冠心病")
            hf = st.checkbox("心衰")
        with col_h2:
            hypertension = st.checkbox("高血压")
            af_history = st.checkbox("房颤史")
        
        thyroid = st.checkbox("甲状腺疾病")
        
        # 已有检查
        st.subheader("已有检查")
        col_lab1, col_lab2 = st.columns(2)
        with col_lab1:
            electrolytes_done = st.checkbox("电解质已查")
            troponin_done = st.checkbox("肌钙蛋白已查")
        with col_lab2:
            glucose_done = st.checkbox("血糖已查")
            cbc_done = st.checkbox("血常规已查")
    
    with col2:
        st.header("📊 分析结果")
        
        # 构建患者数据
        patient_data = {
            "age": age,
            "gender": gender,
            "chest_pain": chest_pain,
            "dyspnea": dyspnea,
            "syncope": syncope,
            "palpitations": palpitations,
            "dizziness": dizziness,
            "sweating": sweating,
            "hr": hr,
            "sbp": sbp,
            "dbp": dbp,
            "spo2": spo2,
            "qrs": qrs,
            "rhythm": rhythm,
            "st_change": st_change,
            "cad": cad,
            "hf": hf,
            "hypertension": hypertension,
            "af_history": af_history,
            "thyroid": thyroid,
            "electrolytes_done": electrolytes_done,
            "troponin_done": troponin_done,
            "glucose_done": glucose_done,
            "cbc_done": cbc_done
        }
        
        # 运行分析
        if st.button("🔍 运行分析", type="primary", use_container_width=True):
            with st.spinner("分析中..."):
                # 1. 危险分层
                patient = create_patient_from_dict(patient_data)
                triage = TriageEngine()
                triage_result = triage.assess(patient)
                
                # 2. 节律分类
                rhythm_engine = RhythmEngine()
                rhythm_result = rhythm_engine.classify(qrs, rhythm, hr)
                
                # 3. 病因分析
                causes_engine = CausesEngine()
                causes_result = causes_engine.analyze(patient_data)
                
                # 4. 治疗建议
                treatment_engine = TreatmentEngine()
                treatment_result = treatment_engine.recommend(
                    triage_result["stability"],
                    rhythm_result["pathway"],
                    patient_data
                )
                
                # 5. 证据
                evidence_engine = EvidenceEngine()
                evidence_result = evidence_engine.get_all_evidence(
                    triage_result["stability"],
                    rhythm_result["pathway"]
                )
                
                # 显示结果
                display_results(triage_result, rhythm_result, causes_result, 
                             treatment_result, evidence_result, patient_data)
        
        else:
            st.info("👈 请在左侧输入患者信息，然后点击「运行分析」")
    
    # 底部警告
    st.markdown("---")
    st.error("⚠️ **免责声明**：本系统仅供临床辅助决策参考，不替代医生诊断和治疗。遇到危重患者请立即按标准急救流程处理！")


def display_results(triage, rhythm, causes, treatment, evidence, patient_data):
    """显示分析结果"""
    
    # Card 1: 风险等级
    st.markdown("### 🎯 风险分层")
    
    risk_colors = {
        "高危": "risk-high",
        "中危": "risk-medium", 
        "低危": "risk-low"
    }
    
    risk_class = risk_colors.get(triage["risk_level"], "risk-low")
    
    st.markdown(f"""
    <div class="{risk_class}">
        <h2 style="margin:0;">{triage['risk_level']} - {triage['stability']}</h2>
        <p style="margin:5px 0;">{triage['message']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if triage.get("unstable_signs"):
        st.write("**不稳定征象**: " + ", ".join(triage["unstable_signs"]))
    
    st.markdown("---")
    
    # Card 2: 诊断
    st.markdown("### 🔬 可能诊断")
    
    for i, d in enumerate(rhythm["diagnoses"], 1):
        prob_emoji = {"高": "🔴", "中": "🟡", "低": "🟢"}.get(d["probability"], "⚪")
        st.write(f"{prob_emoji} **{i}. {d['name']}** ({d['probability']}概率)")
        if d.get("notes"):
            st.caption(f"   {d['notes']}")
    
    st.markdown("---")
    
    # Card 3: 检查建议
    st.markdown("### 🔍 推荐检查")
    
    for w in causes["workup"][:8]:
        priority_emoji = {1: "🔴", 2: "🟡", 3: "🟢"}.get(w["priority"], "⚪")
        st.write(f"{priority_emoji} **{w['name']}** - {w['reason']}")
    
    st.markdown("---")
    
    # Card 4: 处理建议
    st.markdown("### 💊 初始处理建议")
    
    for t in treatment["treatments"]:
        priority_emoji = {1: "🔴", 2: "🟡", 3: "🟢"}.get(t["priority"], "⚪")
        st.write(f"{priority_emoji} **[{t['category']}]** {t['content']}")
    
    st.markdown("---")
    
    # Card 5: 升级提醒
    st.markdown("### ⚠️ 升级处理条件")
    
    for e in treatment["escalation"]:
        st.write(f"• {e}")
    
    st.markdown("---")
    
    # Card 6: 证据来源
    st.markdown("### 📚 证据依据")
    
    for e in evidence["evidence"]:
        st.markdown(f"""
        <div class="evidence-box">
            <strong>{e['title']}</strong><br>
            {e['key_point']}<br>
            <em>证据等级: {e['level']} | 来源: {e['source']}</em>
        </div>
        """, unsafe_allow_html=True)
    
    # 临床判断
    st.markdown("---")
    if triage["stability"] == "不稳定":
        st.error(f"**临床判断**: {treatment['clinical_judgment']}")
    else:
        st.success(f"**临床判断**: {treatment['clinical_judgment']}")


def demo_cases_page():
    """病例演示页面"""
    
    st.header("📖 典型病例演示")
    
    case = st.selectbox("选择病例", [
        "不稳定病例 - 62岁男性胸闷低血压",
        "稳定病例 - 35岁女性心悸",
        "宽QRS - 55岁男性规则宽QRS心动过速",
        "不规则窄QRS - 70岁男性房颤心室率快"
    ])
    
    if "不稳定" in case:
        st.info("""
        **病例**: 62岁男性
        
        **主诉**: 心悸3小时，胸闷，出汗
        
        **生命体征**: 
        - HR: 168 bpm
        - BP: 86/58 mmHg
        - SpO2: 95%
        
        **症状**: 胸闷、出汗
        
        **ECG**: 规则窄QRS心动过速
        
        **既往史**: 高血压、冠心病
        """)
        
        patient_data = {
            "age": 62, "gender": "male",
            "chest_pain": True, "dyspnea": False, "syncope": False,
            "palpitations": True, "dizziness": False, "sweating": True,
            "hr": 168, "sbp": 86, "dbp": 58, "spo2": 95,
            "qrs": "narrow", "rhythm": "regular", "st_change": False,
            "cad": True, "hf": False, "hypertension": True, "af_history": False,
            "thyroid": False, "electrolytes_done": False, "troponin_done": False,
            "glucose_done": False, "cbc_done": False
        }
        
    elif "稳定" in case:
        st.info("""
        **病例**: 35岁女性
        
        **主诉**: 突发心悸20分钟
        
        **生命体征**: 
        - HR: 178 bpm
        - BP: 122/76 mmHg
        - SpO2: 98%
        
        **症状**: 心悸，无胸痛
        
        **ECG**: 规则窄QRS心动过速
        
        **既往史**: 无特殊
        """)
        
        patient_data = {
            "age": 35, "gender": "female",
            "chest_pain": False, "dyspnea": False, "syncope": False,
            "palpitations": True, "dizziness": False, "sweating": False,
            "hr": 178, "sbp": 122, "dbp": 76, "spo2": 98,
            "qrs": "narrow", "rhythm": "regular", "st_change": False,
            "cad": False, "hf": False, "hypertension": False, "af_history": False,
            "thyroid": False, "electrolytes_done": False, "troponin_done": False,
            "glucose_done": False, "cbc_done": False
        }
    
    elif "宽QRS" in case:
        st.info("""
        **病例**: 55岁男性
        
        **主诉**: 心悸、胸闷1小时
        
        **生命体征**: 
        - HR: 160 bpm
        - BP: 110/70 mmHg
        - SpO2: 96%
        
        **症状**: 心悸、胸闷
        
        **ECG**: 规则宽QRS心动过速
        
        **既往史**: 高血压
        """)
        
        patient_data = {
            "age": 55, "gender": "male",
            "chest_pain": True, "dyspnea": False, "syncope": False,
            "palpitations": True, "dizziness": False, "sweating": False,
            "hr": 160, "sbp": 110, "dbp": 70, "spo2": 96,
            "qrs": "wide", "rhythm": "regular", "st_change": True,
            "cad": False, "hf": False, "hypertension": True, "af_history": False,
            "thyroid": False, "electrolytes_done": False, "troponin_done": False,
            "glucose_done": False, "cbc_done": False
        }
    
    else:  # 不规则窄QRS
        st.info("""
        **病例**: 70岁男性
        
        **主诉**: 心悸、气促3天
        
        **生命体征**: 
        - HR: 142 bpm
        - BP: 130/80 mmHg
        - SpO2: 94%
        
        **症状**: 心悸、气促
        
        **ECG**: 不规则窄QRS心动过速
        
        **既往史**: 高血压、房颤史
        """)
        
        patient_data = {
            "age": 70, "gender": "male",
            "chest_pain": False, "dyspnea": True, "syncope": False,
            "palpitations": True, "dizziness": False, "sweating": False,
            "hr": 142, "sbp": 130, "dbp": 80, "spo2": 94,
            "qrs": "narrow", "rhythm": "irregular", "st_change": False,
            "cad": False, "hf": False, "hypertension": True, "af_history": True,
            "thyroid": False, "electrolytes_done": False, "troponin_done": False,
            "glucose_done": False, "cbc_done": False
        }
    
    if st.button("运行分析", type="primary"):
        with st.spinner("分析中..."):
            patient = create_patient_from_dict(patient_data)
            
            triage = TriageEngine()
            triage_result = triage.assess(patient)
            
            rhythm_engine = RhythmEngine()
            rhythm_result = rhythm_engine.classify(patient_data["qrs"], patient_data["rhythm"], patient_data["hr"])
            
            causes_engine = CausesEngine()
            causes_result = causes_engine.analyze(patient_data)
            
            treatment_engine = TreatmentEngine()
            treatment_result = treatment_engine.recommend(triage_result["stability"], rhythm_result["pathway"], patient_data)
            
            evidence_engine = EvidenceEngine()
            evidence_result = evidence_engine.get_all_evidence(triage_result["stability"], rhythm_result["pathway"])
            
            display_results(triage_result, rhythm_result, causes_result, treatment_result, evidence_result, patient_data)


def knowledge_page():
    """知识库页面"""
    
    st.header("📚 心动过速知识库")
    
    st.markdown("""
    ### AHA 成人心动过速算法要点
    
    #### 不稳定表现（需要立即电复律）
    - 持续性低血压 (SBP < 90 mmHg)
    - 休克体征
    - 缺血性胸痛
    - 急性心衰
    - 意识状态改变
    
    #### 稳定患者处理流程
    1. 评估QRS宽度
    2. 评估节律规则性
    3. 窄QRS + 规则 → PSVT/房扑
    4. 窄QRS + 不规则 → 房颤
    5. 宽QRS → 室速可能
    """)
    
    st.markdown("""
    ### ESC 室上速指南要点
    
    #### 规则窄QRS心动过速处理
    1. 迷走神经刺激 (Valsalva动作)
    2. 腺苷静脉注射（诊断+治疗）
    3. β受体阻滞剂/钙通道阻滞剂
    4. 反复发作 → 导管消融评估
    """)
    
    st.markdown("### ⚠️ 危险信号")
    st.error("""
    以下情况应立即急诊处理：
    - 胸痛
    - 晕厥或接近晕厥
    - 呼吸困难
    - 收缩压低
    - 意识改变
    - 持续心率很快且不缓解
    """)


def about_page():
    """关于页面"""
    
    st.header("ℹ️ 关于本系统")
    
    st.markdown("""
    ### Evidence Engine - Tachycardia Care Pathway Assistant
    
    **版本**: MVP v1.0
    
    **定位**: 临床辅助决策系统，不替代医生诊断
    
    **功能**:
    - 危险分层
    - 节律分类
    - 病因搜索
    - 治疗建议
    - 证据展示
    
    **开发计划**: 12周
    
    ### 核心原则
    1. 先评估稳定性
    2. 再分析节律
    3. 最后寻找病因
    4. 每项建议有据可循
    """)


if __name__ == "__main__":
    main()
