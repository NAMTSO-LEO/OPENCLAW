"""
糖尿病急症诊治引擎
Diabetes Emergency Decision Engine (DKA & Hypoglycemia)
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class DiabetesEmergencyType(Enum):
    """糖尿病急症类型"""
    DKA = "糖尿病酮症酸中毒"
    HHS = "高血糖高渗状态"
    HYPOGLYCEMIA = "低血糖"
    NONE = "非糖尿病急症"


class DKASeverity(Enum):
    """DKA严重程度"""
    MILD = "轻度"
    MODERATE = "中度"
    SEVERE = "重度"


@dataclass
class DiabetesData:
    """糖尿病急症患者数据"""
    # 基本信息
    age: int
    gender: str
    diabetes_type: str = "T1"  # T1/T2/gestational
    
    # 症状
    polyuria: bool = False  # 多尿
    polydipsia: bool = False  # 多饮
    polyphagia: bool = False  # 多食
    weight_loss: bool = False
    nausea: bool = False
    vomiting: bool = False
    abdominal_pain: bool = False
    confusion: bool = False
    altered_consciousness: bool = False
    weakness: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    rr: int = 0
    temperature: float = 36.5
    
    # 实验室
    glucose: int = 0  # mg/dL
    ketone: str = "negative"  # negative/positive
    abg_ph: float = 7.4
    bicarb: float = 24  # mEq/L
    anion_gap: float = 12
    bun: int = 0
    creatinine: float = 1.0
    
    # 诱因
    infection: bool = False
    missed_insulin: bool = False
    new_diagnosis: bool = False
    medication: bool = False  # 新用药物


class DiabetesEngine:
    """糖尿病急症诊治引擎"""
    
    def __init__(self):
        self.emergency_type = DiabetesEmergencyType.NONE
        self.severity = DKASeverity.MILD
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: DiabetesData) -> Dict:
        """分析糖尿病患者"""
        
        # 1. 类型判断
        self.determine_type(data)
        
        # 2. 严重程度
        if self.emergency_type == DiabetesEmergencyType.DKA:
            self.assess_dka_severity(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def determine_type(self, data: DiabetesData):
        """判断急症类型"""
        
        # 低血糖
        if data.glucose < 70:
            self.emergency_type = DiabetesEmergencyType.HYPOGLYCEMIA
        # DKA
        elif (data.glucose > 250 and 
              data.ketone == "positive" and 
              data.abg_ph < 7.3):
            self.emergency_type = DiabetesEmergencyType.DKA
        # HHS
        elif data.glucose > 600 and data.abg_ph > 7.3:
            self.emergency_type = DiabetesEmergencyType.HHS
        else:
            self.emergency_type = DiabetesEmergencyType.NONE
    
    def assess_dka_severity(self, data: DiabetesData):
        """评估DKA严重程度"""
        
        if data.abg_ph < 7.0 or data.bicarb < 10:
            self.severity = DKASeverity.SEVERE
        elif data.abg_ph < 7.3 or data.bicarb < 15:
            self.severity = DKASeverity.MODERATE
        else:
            self.severity = DKASeverity.MILD
    
    def recommend_workup(self, data: DiabetesData):
        """检查建议"""
        
        workups = [
            {"name": "指尖血糖", "priority": 1, "reason": "即时血糖"},
            {"name": "血酮", "priority": 1, "reason": "筛查酮症"},
            {"name": "动脉血气", "priority": 1, "reason": "评估酸碱状态"},
        ]
        
        if self.emergency_type == DiabetesEmergencyType.DKA:
            workups.extend([
                {"name": "静脉血糖", "priority": 1, "reason": "确诊"},
                {"name": "电解质", "priority": 1, "reason": "评估电解质紊乱"},
                {"name": "肾功能", "priority": 1, "reason": "评估肾功能和BG/CR比"},
                {"name": "血常规", "priority": 1, "reason": "排除感染"},
                {"name": "尿常规", "priority": 1, "reason": "评估脱水和感染"},
                {"name": "培养", "priority": 2, "reason": "排查感染源"},
            ])
        
        elif self.emergency_type == DiabetesEmergencyType.HYPOGLYCEMIA:
            workups.extend([
                {"name": "指尖血糖", "priority": 1, "reason": "确认低血糖"},
                {"name": "胰岛素/C肽", "priority": 2, "reason": "评估内源性胰岛素"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: DiabetesData):
        """治疗建议"""
        
        treatments = []
        
        if self.emergency_type == DiabetesEmergencyType.HYPOGLYCEMIA:
            treatments.extend([
                {"category": "紧急", "content": "50%葡萄糖20-50ml静脉推注", "priority": 1},
                {"category": "后续", "content": "10%葡萄糖持续输注", "priority": 1},
                {"category": "监测", "content": "每15分钟监测血糖", "priority": 1},
                {"category": "查找", "content": "查找低血糖原因", "priority": 2},
            ])
        
        elif self.emergency_type == DiabetesEmergencyType.DKA:
            treatments.extend([
                {"category": "液体", "content": "0.9%盐水1-2L/小时（最初）", "priority": 1},
                {"category": "胰岛素", "content": "小剂量胰岛素静滴（0.1U/kg/h）", "priority": 1},
                {"category": "补钾", "content": "根据血钾补钾", "priority": 1},
                {"category": "碳酸氢钠", "content": "pH<7.0时考虑", "priority": 2},
                {"category": "诱因", "content": "治疗诱因（感染等）", "priority": 1},
                {"category": "监测", "content": "每1-2小时监测血糖/电解质", "priority": 1},
            ])
        
        elif self.emergency_type == DiabetesEmergencyType.HHS:
            treatments.extend([
                {"category": "液体", "content": "0.9%盐水缓慢补液", "priority": 1},
                {"category": "胰岛素", "content": "小剂量胰岛素（血糖<400后开始）", "priority": 1},
                {"category": "监测", "content": "避免渗透压下降过快", "priority": 1},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ADA Standards of Care 2024", "key": "DKA和HHS诊疗流程"},
            {"title": "ISPAD Clinical Practice Guidelines", "key": "儿童和青少年DKA"},
            {"title": "Endocrine Society Hypoglycemia Guidelines", "key": "低血糖诊疗"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "emergency_type": self.emergency_type.value,
            "severity": self.severity.value if self.emergency_type == DiabetesEmergencyType.DKA else "N/A",
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"血糖{data.glucose}mg/dL，{self.emergency_type.value}"
        }


def create_diabetes_from_dict(d: dict) -> DiabetesData:
    """从字典创建糖尿病数据"""
    return DiabetesData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        diabetes_type=d.get("diabetes_type", "T1"),
        polyuria=d.get("polyuria", False),
        polydipsia=d.get("polydipsia", False),
        polyphagia=d.get("polyphagia", False),
        weight_loss=d.get("weight_loss", False),
        nausea=d.get("nausea", False),
        vomiting=d.get("vomiting", False),
        abdominal_pain=d.get("abdominal_pain", False),
        confusion=d.get("confusion", False),
        altered_consciousness=d.get("altered_consciousness", False),
        weakness=d.get("weakness", False),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        rr=d.get("rr", 0),
        temperature=d.get("temperature", 36.5),
        glucose=d.get("glucose", 0),
        ketone=d.get("ketone", "negative"),
        abg_ph=d.get("abg_ph", 7.4),
        bicarb=d.get("bicarb", 24),
        anion_gap=d.get("anion_gap", 12),
        bun=d.get("bun", 0),
        creatinine=d.get("creatinine", 1.0),
        infection=d.get("infection", False),
        missed_insulin=d.get("missed_insulin", False),
        new_diagnosis=d.get("new_diagnosis", False),
        medication=d.get("medication", False)
    )
