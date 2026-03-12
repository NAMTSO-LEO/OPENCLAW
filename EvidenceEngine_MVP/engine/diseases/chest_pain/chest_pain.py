"""
胸痛/急性冠脉综合征诊治引擎
Chest Pain / ACS Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class ACSRisk(Enum):
    """ACS风险分层"""
    HIGH = "高危"
    INTERMEDIATE = "中危"
    LOW = "低危"


class DiagnosisType(Enum):
    """诊断类型"""
    STEMI = "ST段抬高型心肌梗死"
    NSTEMI = "非ST段抬高型心肌梗死"
    UA = "不稳定型心绞痛"
    OTHER = "其他胸痛原因"


@dataclass
class ChestPainData:
    """胸痛患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 症状
    chest_pain: bool = False
    chest_pressure: bool = False
    chest_dispatch: bool = False
    radiation_arm: bool = False
    radiation_jaw: bool = False
    diaphoresis: bool = False
    dyspnea: bool = False
    nausea: bool = False
    syncope: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    rr: int = 0
    spo2: int = 100
    
    # ECG
    st_elevation: bool = False
    st_depression: bool = False
    t_inversion: bool = False
    new_lbbb: bool = False
    
    # 实验室
    troponin: str = "normal"  # normal/elevated/pending
    bnpp: str = "normal"
    
    # 病史
    cad_history: bool = False
    diabetes: bool = False
    hypertension: bool = False
    hyperlipidemia: bool = False
    smoking: bool = False
    family_history: bool = False


class ChestPainEngine:
    """胸痛/ACS诊治引擎"""
    
    def __init__(self):
        self.risk_level = ACSRisk.LOW
        self.diagnosis = []
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: ChestPainData) -> Dict:
        """分析胸痛患者"""
        
        # 1. 风险分层
        self.assess_risk(data)
        
        # 2. 诊断
        self.diagnose(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def assess_risk(self, data: ChestPainData):
        """风险分层 - HEART评分"""
        
        score = 0
        
        # History (0-2)
        if data.chest_pain or data.chest_pressure:
            score += 2
        elif data.chest_dispatch:
            score += 1
        
        # ECG (0-2)
        if data.st_elevation:
            score += 2
            self.risk_level = ACSRisk.HIGH
        elif data.st_depression or data.t_inversion:
            score += 1
            self.risk_level = ACSRisk.INTERMEDIATE
        
        # Age (0-2)
        if data.age >= 65:
            score += 2
        elif data.age >= 45:
            score += 1
        
        # Risk factors (0-2)
        rf_count = 0
        if data.cad_history: rf_count += 1
        if data.diabetes: rf_count += 1
        if data.hypertension: rf_count += 1
        if data.hyperlipidemia: rf_count += 1
        if data.smoking: rf_count += 1
        if data.family_history: rf_count += 1
        
        if rf_count >= 3:
            score += 2
        elif rf_count >= 1:
            score += 1
        
        # Troponin (0-2)
        if data.troponin == "elevated":
            score += 2
            self.risk_level = ACSRisk.HIGH
        elif data.troponin == "pending":
            score += 1
        
        # 风险分层
        if score >= 7:
            self.risk_level = ACSRisk.HIGH
        elif score >= 4:
            self.risk_level = ACSRisk.INTERMEDIATE
        else:
            self.risk_level = ACSRisk.LOW
    
    def diagnose(self, data: ChestPainData):
        """诊断"""
        
        self.diagnosis = []
        
        # STEMI
        if data.st_elevation:
            self.diagnosis.append({
                "type": "STEMI",
                "name": "ST段抬高型心肌梗死",
                "probability": "高",
                "action": "立即再灌注治疗"
            })
        # NSTEMI/UA
        elif data.troponin == "elevated":
            self.diagnosis.append({
                "type": "NSTEMI",
                "name": "非ST段抬高型心肌梗死",
                "probability": "高",
                "action": "危险分层后决定策略"
            })
        elif data.st_depression or data.t_inversion:
            self.diagnosis.append({
                "type": "UA",
                "name": "不稳定型心绞痛",
                "probability": "中",
                "action": "进一步评估"
            })
        # 其他原因
        else:
            self.diagnosis.append({
                "type": "OTHER",
                "name": "其他胸痛原因",
                "probability": "待定",
                "action": "排除ACS"
            })
            # 鉴别诊断
            self.diagnosis.extend([
                {"type": "Stable Angina", "name": "稳定型心绞痛", "probability": "低", "action": ""},
                {"type": "Pericarditis", "name": "心包炎", "probability": "低", "action": ""},
                {"type": "GERD", "name": "胃食管反流", "probability": "低", "action": ""},
                {"type": "Pneumothorax", "name": "气胸", "probability": "低", "action": ""},
            ])
    
    def recommend_workup(self, data: ChestPainData):
        """检查建议"""
        
        workups = [
            {"name": "12导联心电图", "priority": 1, "reason": "初步评估"},
            {"name": "心肌肌钙蛋白", "priority": 1, "reason": "心肌损伤标志物"},
            {"name": "血常规", "priority": 1, "reason": "排除贫血/感染"},
            {"name": "肾功能", "priority": 1, "reason": "评估肾功能和对比剂风险"},
            {"name": "电解质", "priority": 1, "reason": "电解质紊乱可导致心律失常"},
        ]
        
        if self.risk_level == ACSRisk.HIGH:
            workups.extend([
                {"name": "立即床旁超声", "priority": 1, "reason": "评估心脏功能和结构"},
                {"name": "D-二聚体", "priority": 2, "reason": "排除主动脉夹层/肺栓塞"},
            ])
        else:
            workups.extend([
                {"name": "运动负荷试验", "priority": 2, "reason": "评估缺血"},
                {"name": "冠脉CTA", "priority": 2, "reason": "解剖评估"},
            ])
        
        if data.dyspnea:
            workups.append({"name": "BNP/NT-proBNP", "priority": 1, "reason": "评估心衰"})
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: ChestPainData):
        """治疗建议"""
        
        treatments = []
        
        if self.risk_level == ACSRisk.HIGH:
            treatments.extend([
                {"category": "立即", "content": "吸氧（SpO2<94%）", "priority": 1},
                {"category": "立即", "content": "硝酸甘油舌下/静脉（血压允许）", "priority": 1},
                {"category": "抗血小板", "content": "阿司匹林300mg负荷", "priority": 1},
                {"category": "抗血小板", "content": "P2Y12抑制剂（替格瑞洛/氯吡格雷）", "priority": 1},
                {"category": "抗凝", "content": "普通肝素/低分子肝素", "priority": 1},
                {"category": "他汀", "content": "强化他汀治疗", "priority": 1},
                {"category": "再灌注", "content": "STEMI: 直接PCI或溶栓", "priority": 1},
                {"category": "NSTEMI/UA", "content": "早期介入策略（24-72h）", "priority": 1},
            ])
        elif self.risk_level == ACSRisk.INTERMEDIATE:
            treatments.extend([
                {"category": "监测", "content": "心电监护", "priority": 1},
                {"category": "药物", "content": "阿司匹林+P2Y12抑制剂", "priority": 1},
                {"category": "药物", "content": "低分子肝素", "priority": 1},
                {"category": "检查", "content": "冠脉造影评估", "priority": 2},
            ])
        else:
            treatments.extend([
                {"category": "评估", "content": "门诊进一步评估", "priority": 2},
                {"category": "预防", "content": "危险因素控制", "priority": 2},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ESC NSTEMI Guidelines 2023", "key": "危险分层使用GRACE评分，早期介入策略"},
            {"title": "ACC/AHA ACS Guidelines", "key": "双抗治疗，推荐早期介入"},
            {"title": "HEART Score", "key": "胸痛患者风险分层工具"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "risk_level": self.risk_level.value,
            "diagnosis": self.diagnosis,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"胸痛患者，ACS风险{self.risk_level.value}，需{'立即' if self.risk_level == ACSRisk.HIGH else '尽快' if self.risk_level == ACSRisk.INTERMEDIATE else '门诊'}评估"
        }


def create_chestpain_from_dict(d: dict) -> ChestPainData:
    """从字典创建胸痛数据"""
    return ChestPainData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        chest_pain=d.get("chest_pain", False),
        chest_pressure=d.get("chest_pressure", False),
        chest_dispatch=d.get("chest_dispatch", False),
        radiation_arm=d.get("radiation_arm", False),
        radiation_jaw=d.get("radiation_jaw", False),
        diaphoresis=d.get("diaphoresis", False),
        dyspnea=d.get("dyspnea", False),
        nausea=d.get("nausea", False),
        syncope=d.get("syncope", False),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        rr=d.get("rr", 0),
        spo2=d.get("spo2", 100),
        st_elevation=d.get("st_elevation", False),
        st_depression=d.get("st_depression", False),
        t_inversion=d.get("t_inversion", False),
        new_lbbb=d.get("new_lbbb", False),
        troponin=d.get("troponin", "normal"),
        bnpp=d.get("bnpp", "normal"),
        cad_history=d.get("cad_history", False),
        diabetes=d.get("diabetes", False),
        hypertension=d.get("hypertension", False),
        hyperlipidemia=d.get("hyperlipidemia", False),
        smoking=d.get("smoking", False),
        family_history=d.get("family_history", False)
    )
