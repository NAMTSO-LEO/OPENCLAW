"""
Clinical Decision Engine - 心动过速模块 Web界面
Tachycardia Decision Support System
"""

import streamlit as st
import sys
import os

# 添加路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from 心动过速模块.tachycardia_engine import TachycardiaEngine, Patient

# 页面配置
st.set_page_config(
    page_title="心动过速决策支持系统",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ 心动过速诊治决策支持系统")
st.markdown("**Tachycardia Clinical Decision Support** - MVP v1.0")

# 侧边栏
st.sidebar.title("功能导航")
page = st.sidebar.radio("选择", ["诊治决策", "病例演示", "知识库"])

# ============ 诊治决策页面 ============
if page == "诊治决策":
    st.header("📋 患者信息输入")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("年龄", 0, 120, 65)
        gender = st.selectbox("性别", ["male", "female"], format_func=lambda x: "男" if x == "male" else "女")
        hr = st.number_input("心率 (次/分)", 0, 250, 168)
    
    with col2:
        sbp = st.number_input("收缩压 (mmHg)", 0, 250, 120)
        dbp = st.number_input("舒张压 (mmHg)", 0, 150, 80)
        spo2 = st.number_input("血氧 (%)", 0, 100, 95)
    
    with col3:
        symptoms = st.multiselect(
            "症状",
            ["心悸", "胸痛", "胸闷", "出汗", "呼吸困难", "晕厥", "意识改变", "烦躁", "头晕"],
            default=["心悸", "胸闷"]
        )
    
    # 病史
    st.subheader("既往史")
    history = st.multiselect(
        "既往病史",
        ["高血压", "糖尿病", "冠心病", "心律失常", "甲亢", "结构性心脏病", "无"],
        default=["高血压", "糖尿病"]
    )
    
    # ECG
    st.subheader("心电图")
    ecg_options = [
        "规则性心动过速，QRS窄",
        "不规则性心动过速，QRS窄",
        "规则性心动过速，QRS宽",
        "不规则性心动过速，QRS宽"
    ]
    ecg = st.selectbox("ECG结果", ecg_options)
    
    # 运行分析
    if st.button("🔍 运行分析", type="primary"):
        # 创建患者对象
        patient = Patient(
            age=age,
            gender=gender,
            hr=hr,
            sbp=sbp,
            dbp=dbp,
            spo2=spo2,
            symptoms=symptoms,
            ecg=ecg,
            history=history
        )
        
        # 运行引擎
        engine = TachycardiaEngine()
        result = engine.analyze(patient)
        
        # 显示结果
        st.divider()
        st.header("📊 分析结果")
        
        # 危险分层
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("心率", f"{hr} bpm")
        with col2:
            st.metric("血压", f"{sbp}/{dbp} mmHg")
        with col3:
            risk_color = "🔴" if "高危" in result["risk_level"] else "🟢"
            st.metric("危险分层", f"{risk_color} {result['risk_level']}")
        
        st.divider()
        
        # 诊断
        st.subheader("🔬 鉴别诊断")
        for i, d in enumerate(result["diagnosis"], 1):
            st.write(f"{i}. **{d['diagnosis']}** (概率: {d['probability']})")
        
        st.divider()
        
        # 治疗建议
        st.subheader("💊 治疗建议")
        treatments = sorted(result["treatments"], key=lambda x: x.priority)
        for t in treatments:
            if t.priority == 1:
                emoji = "🔴"
            elif t.priority == 2:
                emoji = "🟡"
            else:
                emoji = "🟢"
            st.write(f"{emoji} **[{t.category}]** {t.content}")
        
        st.divider()
        
        # 推荐检查
        st.subheader("🔍 推荐检查")
        workups = sorted(result["workups"], key=lambda x: x.priority)
        for w in workups:
            if w.priority == 1:
                emoji = "🔴"
            elif w.priority == 2:
                emoji = "🟡"
            else:
                emoji = "🟢"
            st.write(f"{emoji} **{w.category}**: {w.content}")
        
        st.divider()
        
        # 证据来源
        st.subheader("📚 证据来源")
        for e in result["evidence"]:
            st.write(f"- {e}")
        
        # 警告
        if "高危" in result["risk_level"]:
            st.error("⚠️ 警告：此患者为不稳定性心动过速，请立即按ACLS流程处理！")

# ============ 病例演示页面 ============
elif page == "病例演示":
    st.header("📖 典型病例演示")
    
    case = st.selectbox("选择病例", ["不稳定病例 (62岁男性)", "稳定病例 (35岁女性)"])
    
    if "不稳定" in case:
        st.info("""
        **病例**: 62岁男性
        
        **主诉**: 心悸3小时，胸闷，出汗
        
        **生命体征**: 
        - HR: 168次/分
        - BP: 86/58 mmHg
        - SpO2: 95%
        
        **病史**: 高血压、2型糖尿病
        
        **查体**: 轻度烦躁，四肢偏凉
        
        **ECG**: 规则性心动过速，QRS窄
        """)
        
        if st.button("运行分析"):
            patient = Patient(
                age=62,
                gender="male",
                hr=168,
                sbp=86,
                dbp=58,
                spo2=95,
                symptoms=["心悸", "胸闷", "出汗", "烦躁"],
                ecg="规则性心动过速，QRS窄",
                history=["高血压", "糖尿病"]
            )
            
            engine = TachycardiaEngine()
            result = engine.analyze(patient)
            
            st.warning("⚠️ 结果: **不稳定性有脉性心动过速**")
            st.error("需要立即同步电复律!")
            
            st.write("### 鉴别诊断")
            for d in result["diagnosis"]:
                st.write(f"- {d['diagnosis']} ({d['probability']})")
            
            st.write("### 首要处理")
            for t in sorted(result["treatments"], key=lambda x: x.priority)[:3]:
                st.write(f"- {t.content}")
    
    else:
        st.info("""
        **病例**: 35岁女性
        
        **主诉**: 突发心悸20分钟，无胸痛，无晕厥
        
        **生命体征**: 
        - HR: 178次/分
        - BP: 122/76 mmHg
        - SpO2: 98%
        
        **既往史**: 无器质性心脏病史
        
        **ECG**: 规则窄QRS心动过速
        """)
        
        if st.button("运行分析"):
            patient = Patient(
                age=35,
                gender="female",
                hr=178,
                sbp=122,
                dbp=76,
                spo2=98,
                symptoms=["心悸"],
                ecg="规则窄QRS心动过速",
                history=[]
            )
            
            engine = TachycardiaEngine()
            result = engine.analyze(patient)
            
            st.success("✅ 结果: **稳定性室上性心动过速**")
            
            st.write("### 鉴别诊断")
            for d in result["diagnosis"]:
                st.write(f"- {d['diagnosis']} ({d['probability']})")
            
            st.write("### 推荐处理")
            for t in sorted(result["treatments"], key=lambda x: x.priority):
                st.write(f"- {t.content}")

# ============ 知识库页面 ============
elif page == "知识库":
    st.header("📚 心动过速知识库")
    
    st.subheader("AHA 成人心动过速算法要点")
    st.markdown("""
    ### 不稳定表现（需要立即电复律）
    - 持续性低血压 (SBP < 90 mmHg)
    - 休克体征
    - 缺血性胸痛
    - 急性心衰
    - 意识状态改变
    
    ### 稳定患者处理流程
    1. 评估QRS宽度
    2. 评估节律规则性
    3. 窄QRS + 规则 → PSVT/房扑
    4. 窄QRS + 不规则 → 房颤
    5. 宽QRS → 室速可能
    """)
    
    st.subheader("ESC 室上速指南要点")
    st.markdown("""
    ### 规则窄QRS心动过速处理
    1. 迷走神经刺激
    2. 腺苷（诊断+治疗）
    3. β受体阻滞剂/钙通道阻滞剂
    4. 反复发作 → 导管消融评估
    
    ### 证据等级
    - 证据A: 多中心RCT
    - 证据B: 单中心RCT/大型注册研究
    - 证据C: 专家共识
    """)
    
    st.subheader("危险信号")
    st.error("""
    ⚠️ 以下情况应立即急诊处理：
    - 胸痛
    - 晕厥或接近晕厥
    - 呼吸困难
    - 收缩压低
    - 意识改变
    - 持续心率很快且不缓解
    """)

# 底部
st.markdown("---")
st.caption("*此系统仅供辅助决策参考，不替代临床判断*")
