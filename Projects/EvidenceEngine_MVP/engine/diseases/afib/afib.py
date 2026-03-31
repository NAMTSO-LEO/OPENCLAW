"""
房颤诊治引擎
Atrial Fibrillation Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class AFType(Enum):
    """房颤类型"""
    PAROXYSMAL = "阵发性房颤"
    PERSISTENT = "持续性房颤"
    LONG_STANDING = "长期持续性房颤"
    PERMANENT = "永久性房颤"


class StrokeRisk(Enum):
    """卒中风险"""
    HIGH = "高危"
    MODERATE = "中危"
    LOW = "低危"


@dataclass
class AFData:
    """房颤患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 症状
    palpitations: bool = False
    dyspnea: bool = False
    chest_discomfort: bool = False
    fatigue: bool = False
    dizziness: bool = False
    syncope: bool = False
    asymptomatic: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    spo2: int = 100
    
    # ECG
    irregular_rhythm: bool = True
    f_waves: bool = True
    
    # CHA2DS2-VASc评分因素
    heart_failure: bool = False
    hypertension: bool = False
    age_75: bool = False
    diabetes: bool = False
    stroke_tia: bool = False
    vascular_disease: bool = False
    age_65_74: bool = False
    female: bool = False
    
    # HAS-BLED评分因素
    hypertension_uncontrolled: bool = False
    abnormal_liver: bool = False
    abnormal_renal: bool = False
    bleeding_history: bool = False
    labile_inr: bool = False
    elderly: bool = False
    antiplatelet: bool = False
    alcohol: bool = False
    
    # 发作特点
    duration: str = "unknown"  # <48h, >48h, unknown
    previous_af: bool = False
    previous_cardioversion: bool = False
    
    # 合并症
    coronary_artery_disease: bool = False
    valvular_heart_disease: bool = False
    hyperthyroidism: bool = False
    sleep_apnea: bool = False


class AFEngine:
    """房颤诊治引擎"""
    
    def __init__(self):
        self.af_type = AFType.PAROXYSMAL
        self.stroke_risk = StrokeRisk.LOW
        self.bleeding_risk = 0
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: AFData) -> Dict:
        """分析房颤患者"""
        
        # 1. 房颤类型
        self.determine_type(data)
        
        # 2. 卒中风险
        self.assess_stroke_risk(data)
        
        # 3. 出血风险
        self.assess_bleeding_risk(data)
        
        # 4. 检查建议
        self.recommend_workup(data)
        
        # 5. 治疗建议
        self.recommend_treatment(data)
        
        # 6. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def determine_type(self, data: AFData):
        """判断房颤类型"""
        
        if data.previous_af:
            if data.duration == "<48h":
                self.af_type = AFType.PAROXYSMAL
            elif data.duration == ">48h":
                self.af_type = AFType.PERSISTENT
        else:
            # 初发性
            self.af_type = AFType.PAROXYSMAL
    
    def assess_stroke_risk(self, data: AFData):
        """评估卒中风险 - CHA2DS2-VASc"""
        
        score = 0
        
        # 心衰 +1
        if data.heart_failure:
            score += 1
        # 高血压 +1
        if data.hypertension:
            score += 1
        # 年龄>=75 +2
        if data.age_75:
            score += 2
        # 糖尿病 +1
        if data.diabetes:
            score += 1
        # 卒中/TIA +2
        if data.stroke_tia:
            score += 2
        # 血管病 +1
        if data.vascular_disease:
            score += 1
        # 65-74岁 +1
        if data.age_65_74:
            score += 1
        # 女性 +1
        if data.female:
            score += 1
        
        if score >= 2:
            self.stroke_risk = StrokeRisk.HIGH
        elif score == 1:
            self.stroke_risk = StrokeRisk.MODERATE
        else:
            self.stroke_risk = StrokeRisk.LOW
    
    def assess_bleeding_risk(self, data: AFData):
        """评估出血风险 - HAS-BLED"""
        
        score = 0
        
        if data.hypertension_uncontrolled: score += 1
        if data.abnormal_liver: score += 1
        if data.abnormal_renal: score += 1
        if data.bleeding_history: score += 1
        if data.labile_inr: score += 1
        if data.elderly: score += 1
        if data.antiplatelet: score += 1
        if data.alcohol: score += 1
        
        self.bleeding_risk = score
    
    def recommend_workup(self, data: AFData):
        """检查建议"""
        
        workups = [
            {"name": "心电图", "priority": 1, "reason": "确诊房颤"},
            {"name": "超声心动图", "priority": 1, "reason": "评估心脏结构和功能"},
            {"name": "甲状腺功能", "priority": 1, "reason": "排除甲亢"},
            {"name": "电解质", "priority": 1, "reason": "排除电解质紊乱"},
        ]
        
        if self.stroke_risk == StrokeRisk.HIGH:
            workups.extend([
                {"name": "CT/MRI脑", "priority": 2, "reason": "排除颅内病变"},
            ])
        
        workups.extend([
            {"name": "肝肾功能", "priority": 2, "reason": "评估抗凝可行性"},
            {"name": "血常规", "priority": 2, "reason": "排除贫血"},
        ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: AFData):
        """治疗建议"""
        
        treatments = []
        
        # 率控制
        treatments.extend([
            {"category": "率控制", "content": "β受体阻滞剂（美托洛尔）", "priority": 1},
            {"category": "率控制", "content": "钙通道阻滞剂（地尔硫卓）", "priority": 1},
            {"category": "率控制", "content": "地高辛（伴心衰时）", "priority": 2},
        ])
        
        # 抗凝
        if self.stroke_risk == StrokeRisk.HIGH:
            treatments.extend([
                {"category": "抗凝", "content": "DOAC优先（利伐沙班/达比加群/艾多沙班/阿哌沙班）", "priority": 1},
                {"category": "抗凝", "content": "如用华纳林需监测INR 2.0-3.0", "priority": 1},
            ])
        elif self.stroke_risk == StrokeRisk.MODERATE:
            treatments.append(
                {"category": "抗凝", "content": "考虑抗凝（DOAC）", "priority": 2}
            )
        
        # 节律控制
        if data.duration == "<48h":
            treatments.extend([
                {"category": "节律控制", "content": "可考虑药物复律", "priority": 2},
                {"category": "节律控制", "content": "如需急诊复律，可考虑电复律", "priority": 2},
            ])
        
        # 危险因素管理
        treatments.extend([
            {"category": "危险因素", "content": "控制血压", "priority": 1},
            {"category": "危险因素", "content": "治疗甲亢", "priority": 1},
            {"category": "危险因素", "content": "生活方式（戒烟酒、减重、运动）", "priority": 2},
        ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ESC AF Guidelines 2024", "key": "CHA2DS2-VASc指导抗凝，DOAC优先"},
            {"title": "ACC/AHA AF Guideline", "key": "节律控制和率控制同等重要"},
            {"title": "ATRIAL Trial", "key": "早期节律控制改善预后"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "af_type": self.af_type.value,
            "stroke_risk": f"{self.stroke_risk.value} (CHA2DS2-VASc)",
            "bleeding_risk": f"HAS-BLED {self.bleeding_risk}",
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"房颤（{self.af_type.value}），卒中风险{self.stroke_risk.value}"
        }


def create_af_from_dict(d: dict) -> AFData:
    """从字典创建房颤数据"""
    return AFData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        palpitations=d.get("palpitations", False),
        dyspnea=d.get("dyspnea", False),
        chest_discomfort=d.get("chest_discomfort", False),
        fatigue=d.get("fatigue", False),
        dizziness=d.get("dizziness", False),
        syncope=d.get("syncope", False),
        asymptomatic=d.get("asymptomatic", False),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        spo2=d.get("spo2", 100),
        irregular_rhythm=d.get("irregular_rhythm", True),
        f_waves=d.get("f_waves", True),
        heart_failure=d.get("heart_failure", False),
        hypertension=d.get("hypertension", False),
        age_75=d.get("age_75", False),
        diabetes=d.get("diabetes", False),
        stroke_tia=d.get("stroke_tia", False),
        vascular_disease=d.get("vascular_disease", False),
        age_65_74=d.get("age_65_74", False),
        female=d.get("female", False),
        hypertension_uncontrolled=d.get("hypertension_uncontrolled", False),
        abnormal_liver=d.get("abnormal_liver", False),
        abnormal_renal=d.get("abnormal_renal", False),
        bleeding_history=d.get("bleeding_history", False),
        labile_inr=d.get("labile_inr", False),
        elderly=d.get("elderly", False),
        antiplatelet=d.get("antiplatelet", False),
        alcohol=d.get("alcohol", False),
        duration=d.get("duration", "unknown"),
        previous_af=d.get("previous_af", False),
        previous_cardioversion=d.get("previous_cardioversion", False),
        coronary_artery_disease=d.get("coronary_artery_disease", False),
        valvular_heart_disease=d.get("valvular_heart_disease", False),
        hyperthyroidism=d.get("hyperthyroidism", False),
        sleep_apnea=d.get("sleep_apnea", False)
    )
