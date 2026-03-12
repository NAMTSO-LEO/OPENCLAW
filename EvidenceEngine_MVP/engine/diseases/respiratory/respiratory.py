"""
呼吸衰竭诊治引擎
Respiratory Failure Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class RFType(Enum):
    """呼吸衰竭类型"""
    TYPE_I = "I型呼吸衰竭 (低氧)"
    TYPE_II = "II型呼吸衰竭 (高碳酸血症)"


class RFSeverity(Enum):
    """呼吸衰竭严重程度"""
    MILD = "轻度"
    MODERATE = "中度"
    SEVERE = "重度"


@dataclass
class RespiratoryData:
    """呼吸衰竭患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 症状
    dyspnea: bool = False
    cough: bool = False
    sputum: bool = False
    chest_pain: bool = False
    fever: bool = False
    wheezing: bool = False
    
    # 生命体征
    hr: int = 0
    rr: int = 0  # 呼吸频率
    sbp: int = 0
    dbp: int = 0
    spo2: int = 100  # 吸空气
    temperature: float = 36.5
    
    # 血气分析
    ph: float = 7.4
    pao2: int = 0  # mmHg
    paco2: int = 0  # mmHg
    hco3: float = 24
    
    # 病因
    copd: bool = False
    asthma: bool = False
    chf: bool = False
    pneumonia: bool = False
    pulmonary_embolism: bool = False
    ards: bool = False
    
    # 既往史
    smoker: bool = False
    home_oxygen: bool = False


class RespiratoryEngine:
    """呼吸衰竭诊治引擎"""
    
    def __init__(self):
        self.rf_type = RFType.TYPE_I
        self.severity = RFSeverity.MILD
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: RespiratoryData) -> Dict:
        """分析呼吸衰竭患者"""
        
        # 1. 类型判断
        self.determine_type(data)
        
        # 2. 严重程度
        self.assess_severity(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def determine_type(self, data: RespiratoryData):
        """判断呼吸衰竭类型"""
        
        # I型: PaO2 < 60mmHg
        # II型: PaO2 < 60 + PaCO2 > 50mmHg
        
        if data.paco2 > 50:
            self.rf_type = RFType.TYPE_II
        else:
            self.rf_type = RFType.TYPE_I
    
    def assess_severity(self, data: RespiratoryData):
        """评估严重程度"""
        
        # 根据PaO2
        if data.pao2 < 40:
            self.severity = RFSeverity.SEVERE
        elif data.pao2 < 60:
            self.severity = RFSeverity.MODERATE
        else:
            self.severity = RFSeverity.MILD
        
        # 根据RR和SpO2调整
        if data.rr > 30 or data.spo2 < 90:
            self.severity = RFSeverity.SEVERE
    
    def recommend_workup(self, data: RespiratoryData):
        """检查建议"""
        
        workups = [
            {"name": "动脉血气分析", "priority": 1, "reason": "确诊和分型"},
            {"name": "胸部X线", "priority": 1, "reason": "寻找病因"},
            {"name": "心电图", "priority": 1, "reason": "排除心脏原因"},
        ]
        
        if self.rf_type == RFType.TYPE_II:
            workups.extend([
                {"name": "肺功能", "priority": 2, "reason": "评估通气功能"},
            ])
        
        if data.copd or data.asthma:
            workups.extend([
                {"name": "血常规", "priority": 1, "reason": "感染评估"},
                {"name": "痰培养", "priority": 2, "reason": "病原学"},
            ])
        
        if data.chf:
            workups.extend([
                {"name": "BNP/NT-proBNP", "priority": 1, "reason": "心衰评估"},
                {"name": "心脏超声", "priority": 2, "reason": "心功能"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: RespiratoryData):
        """治疗建议"""
        
        treatments = []
        
        # 氧疗
        if self.severity == RFSeverity.SEVERE:
            treatments.append(
                {"category": "氧疗", "content": "高流量鼻导管/面罩给氧", "priority": 1}
            )
            if data.spo2 < 80:
                treatments.append(
                    {"category": "呼吸支持", "content": "考虑无创通气或有创通气", "priority": 1}
                )
        else:
            treatments.append(
                {"category": "氧疗", "content": "鼻导管/面罩吸氧，目标SpO2>94%", "priority": 1}
            )
        
        # II型呼衰特别注意
        if self.rf_type == RFType.TYPE_II:
            treatments.extend([
                {"category": "通气", "content": "避免高浓度氧疗（II型呼衰）", "priority": 1},
                {"category": "通气", "content": "无创通气(NIV)考虑", "priority": 1},
                {"category": "诱因", "content": "治疗慢阻肺急性加重", "priority": 1},
            ])
        
        # 病因治疗
        if data.pneumonia:
            treatments.append(
                {"category": "病因", "content": "抗生素治疗", "priority": 1}
            )
        if data.chf:
            treatments.append(
                {"category": "病因", "content": "利尿剂/心衰治疗", "priority": 1}
            )
        if data.asthma or data.copd:
            treatments.extend([
                {"category": "支气管", "content": "支气管舒张剂", "priority": 1},
                {"category": "激素", "content": "全身激素", "priority": 1},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ATS/ERS Respiratory Failure Guidelines", "key": "呼吸衰竭分型和治疗"},
            {"title": "GOLD COPD Guidelines", "key": "慢阻肺急性加重管理"},
            {"title": "NIV in Acute Exacerbations", "key": "无创通气在II型呼衰中的应用"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "rf_type": self.rf_type.value,
            "severity": self.severity.value,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"PaO2={self.pao2}mmHg, PaCO2={self.paco2}mmHg, {self.rf_type.value}, {self.severity.value}"
        }


def create_respiratory_from_dict(d: dict) -> RespiratoryData:
    """从字典创建呼吸衰竭数据"""
    return RespiratoryData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        dyspnea=d.get("dyspnea", False),
        cough=d.get("cough", False),
        sputum=d.get("sputum", False),
        chest_pain=d.get("chest_pain", False),
        fever=d.get("fever", False),
        wheezing=d.get("wheezing", False),
        hr=d.get("hr", 0),
        rr=d.get("rr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        spo2=d.get("spo2", 100),
        temperature=d.get("temperature", 36.5),
        ph=d.get("ph", 7.4),
        pao2=d.get("pao2", 0),
        paco2=d.get("paco2", 0),
        hco3=d.get("hco3", 24),
        copd=d.get("copd", False),
        asthma=d.get("asthma", False),
        chf=d.get("chf", False),
        pneumonia=d.get("pneumonia", False),
        pulmonary_embolism=d.get("pulmonary_embolism", False),
        ards=d.get("ards", False),
        smoker=d.get("smoker", False),
        home_oxygen=d.get("home_oxygen", False)
    )
