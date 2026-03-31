"""
脑卒中诊治引擎
Stroke / TIA Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class StrokeType(Enum):
    """卒中类型"""
    ISCHEMIC = "缺血性卒中"
    HEMORRHAGIC = "出血性卒中"
    TIA = "短暂性脑缺血发作"
    UNKNOWN = "待定"


class StrokeSeverity(Enum):
    """卒中严重程度 - NIHSS"""
    MILD = "轻度 (0-5)"
    MODERATE = "中度 (6-15)"
    SEVERE = "重度 (>15)"


@dataclass
class StrokeData:
    """卒中患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 发病时间
    onset_time: str = "unknown"  # 精确时间/范围/unknown
    last_normal: str = "unknown"
    wake_up: bool = False
    
    # 症状
    facial_droop: bool = False
    arm_weakness: bool = False
    leg_weakness: bool = False
    speech_difficulty: bool = False
    facial_numbness: bool = False
    visual_loss: bool = False
    vertigo: bool = False
    ataxia: bool = False
    altered_consciousness: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    glucose: int = 0  # mg/dL
    temperature: float = 36.5
    
    # NIHSS评分
    nihss_score: int = 0
    
    # CT发现
    ct_done: bool = False
    ct_result: str = "normal"  # normal/hemorrhage/early_changes
    
    # 病史
    atrial_fibrillation: bool = False
    hypertension: bool = False
    diabetes: bool = False
    prior_stroke: bool = False
    coronary_artery_disease: bool = False
    smoking: bool = False
    
    # 治疗相关
    candidate_tpa: bool = False
    candidate_mechanical: bool = False


class StrokeEngine:
    """脑卒中诊治引擎"""
    
    def __init__(self):
        self.stroke_type = StrokeType.UNKNOWN
        self.severity = StrokeSeverity.MILD
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: StrokeData) -> Dict:
        """分析卒中患者"""
        
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
    
    def determine_type(self, data: StrokeData):
        """判断卒中类型"""
        
        if data.ct_done:
            if data.ct_result == "hemorrhage":
                self.stroke_type = StrokeType.HEMORRHAGIC
            elif data.ct_result == "early_changes":
                self.stroke_type = StrokeType.ISCHEMIC
            else:
                # CT正常，可能是缺血性或TIA
                if data.nihss_score > 0:
                    self.stroke_type = StrokeType.ISCHEMIC
                else:
                    self.stroke_type = StrokeType.TIA
        else:
            self.stroke_type = StrokeType.UNKNOWN
    
    def assess_severity(self, data: StrokeData):
        """评估严重程度"""
        
        score = data.nihss_score
        
        if score <= 5:
            self.severity = StrokeSeverity.MILD
        elif score <= 15:
            self.severity = StrokeSeverity.MODERATE
        else:
            self.severity = StrokeSeverity.SEVERE
    
    def recommend_workup(self, data: StrokeData):
        """检查建议"""
        
        workups = [
            {"name": "头颅CT/MRI", "priority": 1, "reason": "鉴别缺血/出血"},
            {"name": "心电图", "priority": 1, "reason": "排查房颤"},
            {"name": "血糖", "priority": 1, "reason": "排除低血糖"},
        ]
        
        if self.stroke_type == StrokeType.ISCHEMIC:
            workups.extend([
                {"name": "CTA/MRA", "priority": 1, "reason": "评估大血管"},
                {"name": "颈动脉超声", "priority": 1, "reason": "评估颈内动脉"},
                {"name": "凝血功能", "priority": 1, "reason": "tPA准备"},
                {"name": "血常规", "priority": 1, "reason": "血细胞计数"},
            ])
        
        if self.stroke_type == StrokeType.HEMORRHAGIC:
            workups.extend([
                {"name": "CTA/数字减影", "priority": 1, "reason": "查找病因"},
                {"name": "凝血功能", "priority": 1, "reason": "评估抗凝"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: StrokeData):
        """治疗建议"""
        
        treatments = []
        
        if self.stroke_type == StrokeType.ISCHEMIC:
            # 缺血性卒中
            treatments.extend([
                {"category": "一般", "content": "保持气道通畅", "priority": 1},
                {"category": "一般", "content": "控制血压（除非>220/120）", "priority": 1},
                {"category": "一般", "content": "血糖控制", "priority": 1},
            ])
            
            # tPA
            if data.candidate_tpa:
                treatments.append(
                    {"category": "再灌注", "content": "rt-PA静脉溶栓（4.5小时内）", "priority": 1}
                )
            
            # 机械取栓
            if data.candidate_mechanical:
                treatments.append(
                    {"category": "再灌注", "content": "机械取栓（24小时内大血管闭塞）", "priority": 1}
                )
            
            # 抗血小板
            treatments.extend([
                {"category": "抗血小板", "content": "阿司匹林（24-48小时后）", "priority": 1},
                {"category": "二级预防", "content": "抗凝（房颤）", "priority": 1},
                {"category": "二级预防", "content": "他汀强化治疗", "priority": 1},
            ])
        
        elif self.stroke_type == StrokeType.HEMORRHAGIC:
            treatments.extend([
                {"category": "一般", "content": "控制血压", "priority": 1},
                {"category": "一般", "content": "止血（如果有凝血病）", "priority": 1},
                {"category": "手术", "content": "神经外科评估（脑积水/脑疝）", "priority": 1},
            ])
        
        elif self.stroke_type == StrokeType.TIA:
            treatments.extend([
                {"category": "评估", "content": "ABCD2评分", "priority": 1},
                {"category": "治疗", "content": "抗血小板治疗", "priority": 1},
                {"category": "评估", "content": "查找病因（房颤、颈动脉）", "priority": 1},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "AHA/ASA Stroke Guidelines 2021", "key": "tPA和机械取栓时间窗"},
            {"title": "EXTEND-IA TNK Trial", "key": "TNK vs rt-PA"},
            {"title": "DEFUSE 3 Trial", "key": "大血管闭塞机械取栓时间窗延长"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "stroke_type": self.stroke_type.value,
            "severity": self.severity.value,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"{self.stroke_type.value}，{self.severity.value}"
        }


def create_stroke_from_dict(d: dict) -> StrokeData:
    """从字典创建卒中数据"""
    return StrokeData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        onset_time=d.get("onset_time", "unknown"),
        last_normal=d.get("last_normal", "unknown"),
        wake_up=d.get("wake_up", False),
        facial_droop=d.get("facial_droop", False),
        arm_weakness=d.get("arm_weakness", False),
        leg_weakness=d.get("leg_weakness", False),
        speech_difficulty=d.get("speech_difficulty", False),
        facial_numbness=d.get("facial_numbness", False),
        visual_loss=d.get("visual_loss", False),
        vertigo=d.get("vertigo", False),
        ataxia=d.get("ataxia", False),
        altered_consciousness=d.get("altered_consciousness", False),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        glucose=d.get("glucose", 0),
        temperature=d.get("temperature", 36.5),
        nihss_score=d.get("nihss_score", 0),
        ct_done=d.get("ct_done", False),
        ct_result=d.get("ct_result", "normal"),
        atrial_fibrillation=d.get("atrial_fibrillation", False),
        hypertension=d.get("hypertension", False),
        diabetes=d.get("diabetes", False),
        prior_stroke=d.get("prior_stroke", False),
        coronary_artery_disease=d.get("coronary_artery_disease", False),
        smoking=d.get("smoking", False),
        candidate_tpa=d.get("candidate_tpa", False),
        candidate_mechanical=d.get("candidate_mechanical", False)
    )
