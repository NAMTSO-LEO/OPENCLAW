"""
危险分层引擎 - Triage Engine
Evidence Engine - Tachycardia Care Pathway Assistant
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class RiskLevel(Enum):
    """危险分层"""
    HIGH = "高危"
    MEDIUM = "中危"
    LOW = "低危"


class Stability(Enum):
    """稳定性"""
    UNSTABLE = "不稳定"
    STABLE = "稳定"


@dataclass
class PatientData:
    """患者数据"""
    # 基本信息
    age: int
    gender: str  # male/female
    
    # 症状
    chest_pain: bool = False
    dyspnea: bool = False
    syncope: bool = False
    palpitations: bool = False
    dizziness: bool = False
    sweating: bool = False
    fever: bool = False
    altered_mental: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    spo2: int = 100
    rr: int = 0
    temperature: float = 36.5
    
    # ECG特征
    qrs: str = "narrow"  # narrow/wide
    rhythm: str = "regular"  # regular/irregular
    p_wave: str = "not_seen"  # seen/not_seen/unclear
    st_change: bool = False
    
    # 病史
    cad: bool = False  # 冠心病
    hf: bool = False  # 心衰
    hypertension: bool = False  # 高血压
    af_history: bool = False  # 房颤史
    thyroid: bool = False  # 甲状腺疾病
    drug_use: bool = False  # 药物使用
    caffeine: bool = False  # 咖啡因
    alcohol: bool = False  # 酒精
    
    # 已有检查
    electrolytes_done: bool = False
    troponin_done: bool = False
    glucose_done: bool = False
    cbc_done: bool = False
    tsh_done: bool = False


class TriageEngine:
    """危险分层引擎"""
    
    def __init__(self):
        self.risk_level = RiskLevel.LOW
        self.stability = Stability.STABLE
        self.unstable_signs = []
        self.recommendations = []
    
    def assess(self, patient: PatientData) -> Dict:
        """评估危险分层"""
        self.unstable_signs = []
        
        # 检查不稳定征象
        # AHA: 低血压、休克体征、缺血性胸痛、急性心衰、意识改变
        
        # 低血压
        if patient.sbp < 90:
            self.unstable_signs.append(f"低血压 (SBP={patient.sbp}mmHg)")
        
        # 胸痛/胸闷
        if patient.chest_pain:
            self.unstable_signs.append("胸痛/胸闷")
        
        # 意识改变
        if patient.altered_mental:
            self.unstable_signs.append("意识改变")
        
        # 呼吸困难/急性心衰
        if patient.dyspnea:
            self.unstable_signs.append("呼吸困难")
        
        # 晕厥
        if patient.syncope:
            self.unstable_signs.append("晕厥")
        
        # 心率极快
        if patient.hr >= 180:
            self.unstable_signs.append(f"极快心率 ({patient.hr}bpm)")
        
        # 严重低氧
        if patient.spo2 < 90:
            self.unstable_signs.append(f"低氧 (SpO2={patient.spo2}%)")
        
        # 判断稳定性
        if self.unstable_signs:
            self.stability = Stability.UNSTABLE
            self.risk_level = RiskLevel.HIGH
        elif patient.hr >= 150 or patient.sbp < 100:
            self.stability = Stability.STABLE
            self.risk_level = RiskLevel.MEDIUM
        else:
            self.stability = Stability.STABLE
            self.risk_level = RiskLevel.LOW
        
        return self.get_result()
    
    def get_result(self) -> Dict:
        """获取结果"""
        return {
            "risk_level": self.risk_level.value,
            "stability": self.stability.value,
            "unstable_signs": self.unstable_signs,
            "color": self.get_color(),
            "message": self.get_message()
        }
    
    def get_color(self) -> str:
        """获取颜色"""
        if self.risk_level == RiskLevel.HIGH:
            return "red"
        elif self.risk_level == RiskLevel.MEDIUM:
            return "yellow"
        else:
            return "green"
    
    def get_message(self) -> str:
        """获取消息"""
        if self.stability == Stability.UNSTABLE:
            return "不稳定性心动过速，需立即处理"
        elif self.risk_level == RiskLevel.MEDIUM:
            return "中危，需密切关注"
        else:
            return "相对稳定，建议完善检查"


def create_patient_from_dict(data: Dict) -> PatientData:
    """从字典创建患者数据"""
    return PatientData(
        age=data.get("age", 0),
        gender=data.get("gender", "male"),
        chest_pain=data.get("chest_pain", False),
        dyspnea=data.get("dyspnea", False),
        syncope=data.get("syncope", False),
        palpitations=data.get("palpitations", False),
        dizziness=data.get("dizziness", False),
        sweating=data.get("sweating", False),
        fever=data.get("fever", False),
        altered_mental=data.get("altered_mental", False),
        hr=data.get("hr", 0),
        sbp=data.get("sbp", 0),
        dbp=data.get("dbp", 0),
        spo2=data.get("spo2", 100),
        rr=data.get("rr", 0),
        temperature=data.get("temperature", 36.5),
        qrs=data.get("qrs", "narrow"),
        rhythm=data.get("rhythm", "regular"),
        p_wave=data.get("p_wave", "not_seen"),
        st_change=data.get("st_change", False),
        cad=data.get("cad", False),
        hf=data.get("hf", False),
        hypertension=data.get("hypertension", False),
        af_history=data.get("af_history", False),
        thyroid=data.get("thyroid", False),
        drug_use=data.get("drug_use", False),
        caffeine=data.get("caffeine", False),
        alcohol=data.get("alcohol", False),
        electrolytes_done=data.get("electrolytes_done", False),
        troponin_done=data.get("troponin_done", False),
        glucose_done=data.get("glucose_done", False),
        cbc_done=data.get("cbc_done", False),
        tsh_done=data.get("tsh_done", False)
    )
