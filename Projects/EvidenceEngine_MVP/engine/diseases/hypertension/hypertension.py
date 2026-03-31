"""
高血压危象诊治引擎
Hypertension Crisis Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class HypertensiveEmergency(Enum):
    """高血压急症vs亚急症"""
    EMERGENCY = "高血压急症"
    URGENCY = "高血压亚急症"


class HypertensiveType(Enum):
    """高血压类型"""
    MALIGNANT = "恶性高血压"
    HYPERTENSIVE_EMERGENCY = "高血压急症"
    HYPERTENSIVE_URGENCY = "高血压亚急症"
    SEVERE_ESSENTIAL = "重度原发性高血压"


@dataclass
class HypertensionData:
    """高血压患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 血压
    sbp: int = 0
    dbp: int = 0
    
    # 症状
    headache: bool = False
    visual_changes: bool = False
    chest_pain: bool = False
    dyspnea: bool = False
    neurological: bool = False  # 意识改变、抽搐
    epistaxis: bool = False  # 鼻出血
    
    # 靶器官损害
    acute_renal: bool = False  # 急性肾损伤
    acute_pulmonary: bool = False  # 急性肺水肿
    acute_cardiac: bool = False  # 急性心衰
    aortic_dissection: bool = False  # 主动脉夹层
    encephalopathy: bool = False  # 高血压脑病
    eclampsia: bool = False  # 子痫
    
    # 病史
    known_hypertension: bool = False
    medication_compliance: bool = True  # 依从性
    renal_disease: bool = False
    diabetes: bool = False


class HypertensionEngine:
    """高血压危象诊治引擎"""
    
    def __init__(self):
        self.type = HypertensiveType.SEVERE_ESSENTIAL
        self.is_emergency = False
        self.sbp = 0
        self.dbp = 0
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: HypertensionData) -> Dict:
        """分析高血压患者"""
        
        self.sbp = data.sbp
        self.dbp = data.dbp
        
        # 1. 类型判断
        self.determine_type(data)
        
        # 2. 检查建议
        self.recommend_workup(data)
        
        # 3. 治疗建议
        self.recommend_treatment(data)
        
        # 4. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def determine_type(self, data: HypertensionData):
        """判断高血压类型"""
        
        # 靶器官损害 = 高血压急症
        if (data.acute_renal or data.acute_pulmonary or data.acute_cardiac or 
            data.aortic_dissection or data.encephalopathy or data.eclampsia or
            data.neurological or data.dbp > 130):
            self.is_emergency = True
            self.type = HypertensiveType.HYPERTENSIVE_EMERGENCY
        elif data.sbp >= 180 or data.dbp >= 120:
            if data.headache or data.visual_changes:
                self.type = HypertensiveType.MALIGNANT
            else:
                self.type = HypertensiveType.HYPERTENSIVE_URGENCY
        else:
            self.type = HypertensiveType.SEVERE_ESSENTIAL
    
    def recommend_workup(self, data: HypertensionData):
        """检查建议"""
        
        workups = [
            {"name": "复查血压", "priority": 1, "reason": "确认血压水平"},
            {"name": "心电图", "priority": 1, "reason": "评估心脏"},
        ]
        
        if self.is_emergency:
            workups.extend([
                {"name": "胸片", "priority": 1, "reason": "评估肺水肿"},
                {"name": "急诊超声", "priority": 1, "reason": "评估心脏功能和主动脉"},
                {"name": "头部CT", "priority": 1, "reason": "排除脑病/出血"},
                {"name": "肾功能", "priority": 1, "reason": "评估肾损害"},
                {"name": "电解质", "priority": 1, "reason": "排除低钾/高钾"},
                {"name": "尿常规", "priority": 1, "reason": "蛋白尿/血尿"},
            ])
        
        workups.extend([
            {"name": "血糖、血脂", "priority": 2, "reason": "代谢评估"},
            {"name": "眼科检查", "priority": 2, "reason": "评估视网膜病变"},
        ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: HypertensionData):
        """治疗建议"""
        
        treatments = []
        
        if self.is_emergency:
            # 高血压急症
            treatments.extend([
                {"category": "监测", "content": "ICU/CCU监护", "priority": 1},
                {"category": "监测", "content": "持续血压监测", "priority": 1},
                {"category": "降压", "content": "静脉降压药（硝普钠/硝酸甘油/拉贝洛尔）", "priority": 1},
                {"category": "目标", "content": "第1小时降压不超过25%", "priority": 1},
                {"category": "目标", "content": "2-6小时降至160/100mmHg", "priority": 1},
            ])
            
            if data.encephalopathy:
                treatments.append({"category": "特殊", "content": "高血压脑病：首选拉贝洛尔/尼卡地平", "priority": 1})
            if data.aortic_dissection:
                treatments.append({"category": "特殊", "content": "主动脉夹层：将SBP降至<120mmHg", "priority": 1})
            if data.acute_pulmonary:
                treatments.append({"category": "特殊", "content": "急性肺水肿：硝酸甘油+利尿剂", "priority": 1})
        else:
            # 高血压亚急症
            treatments.extend([
                {"category": "评估", "content": "口服降压药调整", "priority": 1},
                {"category": "监测", "content": "门诊观察4-6小时", "priority": 1},
                {"category": "生活方式", "content": "低盐饮食、休息", "priority": 2},
                {"category": "随访", "content": "24-48小时门诊随访", "priority": 2},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ACC/AHA 2017 Hypertension Guidelines", "key": "高血压急症需静脉降压，监测靶器官"},
            {"title": "ESC HTN Guidelines 2023", "key": "第1小时降压不超过25%"},
            {"title": "ISH Global Guidelines 2020", "key": "高血压急症分层管理"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "type": self.type.value,
            "is_emergency": self.is_emergency,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"血压{self.sbp}/{self.dbp}mmHg，{self.type.value}"
        }


def create_htn_from_dict(d: dict) -> HypertensionData:
    """从字典创建高血压数据"""
    return HypertensionData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        headache=d.get("headache", False),
        visual_changes=d.get("visual_changes", False),
        chest_pain=d.get("chest_pain", False),
        dyspnea=d.get("dyspnea", False),
        neurological=d.get("neurological", False),
        epistaxis=d.get("epistaxis", False),
        acute_renal=d.get("acute_renal", False),
        acute_pulmonary=d.get("acute_pulmonary", False),
        acute_cardiac=d.get("acute_cardiac", False),
        aortic_dissection=d.get("aortic_dissection", False),
        encephalopathy=d.get("encephalopathy", False),
        eclampsia=d.get("eclampsia", False),
        known_hypertension=d.get("known_hypertension", False),
        medication_compliance=d.get("medication_compliance", True),
        renal_disease=d.get("renal_disease", False),
        diabetes=d.get("diabetes", False)
    )
