"""
脓毒症诊治引擎
Sepsis Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class SepsisSeverity(Enum):
    """脓毒症严重程度"""
    SEPSIS = "脓毒症"
    SEPTIC_SHOCK = "脓毒性休克"
    NO_SEPSIS = "非脓毒症"


class QSOFALevel(Enum):
    """qSOFA评分"""
    HIGH = "≥2分（高危）"
    LOW = "<2分（低危）"


@dataclass
class SepsisData:
    """脓毒症患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 感染表现
    fever: bool = False
    hypothermia: bool = False
    chills: bool = False
    cough: bool = False
    dysuria: bool = False
    abdominal_pain: bool = False
    wound: bool = False
    source_known: bool = False
    source_type: str = "unknown"  # respiratory/urinary/abdominal/skin/other
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    rr: int = 0
    spo2: int = 100
    temperature: float = 36.5
    
    # qSOFA
    altered_mental: bool = False
    rr_high: bool = False  # RR >= 22
    sbp_low: bool = False  # SBP <= 100
    
    # 实验室
    wbc: int = 0  # x10^9/L
    lactate: float = 0  # mmol/L
    creatinine: float = 1.0
    bilirubin: float = 1.0
    inr: float = 1.0
    platelets: int = 0  # x10^9/L
    
    # 合并症
    immunocompromised: bool = False
    diabetes: bool = False
    renal_disease: bool = False
    liver_disease: bool = False
    
    # 液体反应性
    fluid_responsive: bool = False


class SepsisEngine:
    """脓毒症诊治引擎"""
    
    def __init__(self):
        self.severity = SepsisSeverity.NO_SEPSIS
        self.qsofa = QSOFALevel.LOW
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: SepsisData) -> Dict:
        """分析脓毒症患者"""
        
        # 1. qSOFA评估
        self.assess_qsofa(data)
        
        # 2. 严重程度
        self.assess_severity(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def assess_qsofa(self, data: SepsisData):
        """评估qSOFA"""
        
        score = 0
        
        if data.altered_mental:
            score += 1
        if data.rr >= 22:
            score += 1
        if data.sbp <= 100:
            score += 1
        
        if score >= 2:
            self.qsofa = QSOFALevel.HIGH
        else:
            self.qsofa = QSOFALevel.LOW
    
    def assess_severity(self, data: SepsisData):
        """评估严重程度"""
        
        # 脓毒性休克：需要血管活性药物 + 乳酸 > 2
        if (data.sbp < 90 or data.sbp < 100) and data.lactate > 2:
            self.severity = SepsisSeverity.SEPTIC_SHOCK
        # 脓毒症：感染 + qSOFA >= 2 或 SOFA >= 2
        elif self.qsofa == QSOFALevel.HIGH:
            self.severity = SepsisSeverity.SEPSIS
        else:
            self.severity = SepsisSeverity.NO_SEPSIS
    
    def recommend_workup(self, data: SepsisData):
        """检查建议"""
        
        workups = [
            {"name": "血常规", "priority": 1, "reason": "WBC评估感染"},
            {"name": "血培养", "priority": 1, "reason": "病原学诊断"},
            {"name": "乳酸", "priority": 1, "reason": "组织灌注评估"},
            {"name": "肾功能", "priority": 1, "reason": "器官功能"},
            {"name": "肝功能", "priority": 1, "reason": "器官功能"},
        ]
        
        if self.severity == SepsisSeverity.SEPTIC_SHOCK:
            workups.extend([
                {"name": "中心静脉压", "priority": 1, "reason": "液体管理"},
                {"name": "混合静脉血氧", "priority": 2, "reason": "氧代谢评估"},
            ])
        
        # 根据感染源
        if data.source_type == "respiratory":
            workups.extend([
                {"name": "痰培养", "priority": 1, "reason": "呼吸道病原"},
                {"name": "胸片", "priority": 1, "reason": "肺部评估"},
            ])
        elif data.source_type == "urinary":
            workups.extend([
                {"name": "尿培养", "priority": 1, "reason": "泌尿系病原"},
                {"name": "尿常规", "priority": 1, "reason": "评估感染"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: SepsisData):
        """治疗建议"""
        
        treatments = []
        
        if self.severity == SepsisSeverity.SEPTIC_SHOCK:
            treatments.extend([
                {"category": "液体", "content": "30ml/kg晶体液快速补液", "priority": 1},
                {"category": "血管活性", "content": "去甲肾上腺素首选", "priority": 1},
                {"category": "抗生素", "content": "1小时内广谱抗生素", "priority": 1},
                {"category": "监测", "content": "MAP目标≥65mmHg", "priority": 1},
                {"category": "血糖", "content": "控制血糖<180mg/dL", "priority": 1},
            ])
        
        elif self.severity == SepsisSeverity.SEPSIS:
            treatments.extend([
                {"category": "液体", "content": "晶体液补液", "priority": 1},
                {"category": "抗生素", "content": "1小时内抗生素", "priority": 1},
                {"category": "源头", "content": "控制感染源", "priority": 1},
                {"category": "监测", "content": "密切监测", "priority": 1},
            ])
        
        # 感染源控制
        if data.source_type == "urinary":
            treatments.append({"category": "处理", "content": "考虑导尿", "priority": 2})
        elif data.source_type == "abdominal":
            treatments.append({"category": "处理", "content": "外科引流/手术", "priority": 2})
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "Surviving Sepsis Campaign 2021", "key": "1小时bundle：抗生素、液体、血管活性药"},
            {"title": "SOFA Score", "key": "器官功能评估"},
            {"title": "qSOFA", "key": "快速筛查"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "severity": self.severity.value,
            "qsofa": self.qsofa.value,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"qSOFA {self.qsofa.value}，{self.severity.value}"
        }


def create_sepsis_from_dict(d: dict) -> SepsisData:
    """从字典创建脓毒症数据"""
    return SepsisData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        fever=d.get("fever", False),
        hypothermia=d.get("hypothermia", False),
        chills=d.get("chills", False),
        cough=d.get("cough", False),
        dysuria=d.get("dysuria", False),
        abdominal_pain=d.get("abdominal_pain", False),
        wound=d.get("wound", False),
        source_known=d.get("source_known", False),
        source_type=d.get("source_type", "unknown"),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        rr=d.get("rr", 0),
        spo2=d.get("spo2", 100),
        temperature=d.get("temperature", 36.5),
        altered_mental=d.get("altered_mental", False),
        rr_high=d.get("rr_high", False),
        sbp_low=d.get("sbp_low", False),
        wbc=d.get("wbc", 0),
        lactate=d.get("lactate", 0),
        creatinine=d.get("creatinine", 1.0),
        bilirubin=d.get("bilirubin", 1.0),
        inr=d.get("inr", 1.0),
        platelets=d.get("platelets", 0),
        immunocompromised=d.get("immunocompromised", False),
        diabetes=d.get("diabetes", False),
        renal_disease=d.get("renal_disease", False),
        liver_disease=d.get("liver_disease", False),
        fluid_responsive=d.get("fluid_responsive", False)
    )
