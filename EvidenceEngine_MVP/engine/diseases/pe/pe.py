"""
肺栓塞诊治引擎
Pulmonary Embolism Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class PELikelihood(Enum):
    """肺栓塞可能性"""
    HIGH = "高度可能"
    INTERMEDIATE = "中度可能"
    LOW = "低度可能"


class PESeverity(Enum):
    """肺栓塞严重程度"""
    MASSIVE = "大面积肺栓塞"
    SUBMASSIVE = "次大面积肺栓塞"
    LOW_RISK = "低危"


@dataclass
class PEData:
    """肺栓塞患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 症状
    dyspnea: bool = False
    pleuritic_chest_pain: bool = False
    cough: bool = False
    hemoptysis: bool = False
    syncope: bool = False
    leg_pain: bool = False
    leg_swelling: bool = False
    
    # 生命体征
    hr: int = 0
    rr: int = 0
    sbp: int = 0
    spo2: int = 100
    temperature: float = 36.5
    
    # 体征
    leg_swelling_unilateral: bool = False
    hemoptysis_mild: bool = False
    
    # 病史
    prior_pe_dvt: bool = False
    recent_surgery: bool = False
    immobility: bool = False
    cancer: bool = False
    estrogen: bool = False  # 口服避孕药/激素
    pregnancy: bool = False
    thrombophilia: bool = False  # 血栓倾向
    
    # 检查
    d_dimer: str = "not_done"  # normal/elevated/not_done
    ctpa_done: bool = False
    ctpa_result: str = "not_done"  # positive/negative/not_done
    ultrasound_done: bool = False
    ultrasound_result: str = "not_done"
    alternate_diagnosis_less_likely: bool = False


class PEEngine:
    """肺栓塞诊治引擎"""
    
    def __init__(self):
        self.likelihood = PELikelihood.LOW
        self.severity = PESeverity.LOW_RISK
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: PEData) -> Dict:
        """分析肺栓塞患者"""
        
        # 1. 可能性评估 - Wells评分
        self.assess_likelihood(data)
        
        # 2. 严重程度
        self.assess_severity(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def assess_likelihood(self, data: PEData):
        """评估肺栓塞可能性 - Wells评分"""
        
        score = 0
        
        # Wells评分
        if data.prior_pe_dvt:
            score += 1.5
        if data.hr >= 100:
            score += 1.5
        if data.recent_surgery or data.immobility:
            score += 1.5
        if data.alternate_diagnosis_less_likely:
            score += 1.0
        if data.hemoptysis:
            score += 1.0
        if data.cancer:
            score += 1.0
        
        # D-二聚体
        if data.d_dimer == "elevated":
            score += 2.0
        
        if score >= 6:
            self.likelihood = PELikelihood.HIGH
        elif score >= 2:
            self.likelihood = PELikelihood.INTERMEDIATE
        else:
            self.likelihood = PELikelihood.LOW
    
    def assess_severity(self, data: PEData):
        """评估严重程度"""
        
        # 血压<90mmHg = 大面积
        if data.sbp < 90:
            self.severity = PESeverity.MASSIVE
        # 血压正常但右室功能不全 = 次大面积
        elif data.hr > 100 or data.spo2 < 95:
            self.severity = PESeverity.SUBMASSIVE
        else:
            self.severity = PESeverity.LOW_RISK
    
    def recommend_workup(self, data: PEData):
        """检查建议"""
        
        workups = [
            {"name": "心电图", "priority": 1, "reason": "排除其他原因"},
            {"name": "胸片", "priority": 1, "reason": "排除肺炎/气胸"},
        ]
        
        if self.likelihood == PELikelihood.HIGH:
            workups.extend([
                {"name": "CT肺动脉造影(CTPA)", "priority": 1, "reason": "确诊PE"},
                {"name": "下肢超声", "priority": 1, "reason": "寻找DVT证据"},
            ])
        elif self.likelihood == PELikelihood.INTERMEDIATE:
            workups.extend([
                {"name": "D-二聚体", "priority": 1, "reason": "筛查"},
                {"name": "CTPA", "priority": 1, "reason": "如果D-二聚体阳性"},
            ])
        else:
            workups.extend([
                {"name": "D-二聚体", "priority": 1, "reason": "排除PE"},
            ])
        
        if self.severity != PESeverity.LOW_RISK:
            workups.extend([
                {"name": "超声心动图", "priority": 1, "reason": "评估右室功能"},
                {"name": "血气分析", "priority": 1, "reason": "评估氧合"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: PEData):
        """治疗建议"""
        
        treatments = []
        
        if self.severity == PESeverity.MASSIVE:
            treatments.extend([
                {"category": "急救", "content": "立即生命支持", "priority": 1},
                {"category": "急救", "content": "溶栓治疗（rt-PA）", "priority": 1},
                {"category": "监测", "content": "ICU监护", "priority": 1},
                {"category": "抗凝", "content": "溶栓后抗凝", "priority": 1},
            ])
        elif self.severity == PESeverity.SUBMASSIVE:
            treatments.extend([
                {"category": "抗凝", "content": "立即抗凝", "priority": 1},
                {"category": "监测", "content": "密切监测，必要时溶栓", "priority": 1},
                {"category": "检查", "content": "评估右室功能", "priority": 1},
            ])
        else:
            treatments.extend([
                {"category": "抗凝", "content": "启动抗凝治疗", "priority": 1},
                {"category": "抗凝", "content": "DOAC（利伐沙班/阿哌沙班）或华法林", "priority": 1},
                {"category": "随访", "content": "门诊随访", "priority": 2},
            ])
        
        # 危险因素处理
        if data.recent_surgery or data.immobility:
            treatments.append({"category": "预防", "content": "考虑临时IVC滤器", "priority": 2})
        
        if data.estrogen or data.pregnancy:
            treatments.append({"category": "处理", "content": "停用雌激素", "priority": 1})
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ESC PE Guidelines 2022", "key": "Wells评分指导诊断，危险分层指导治疗"},
            {"title": "ACC Antithrombotic Therapy in VTE", "key": "DOAC作为一线抗凝"},
            {"title": "CTED Trial", "key": "早期溶栓对次大面积PE的价值"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "likelihood": self.likelihood.value,
            "severity": self.severity.value,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"PE可能性{self.likelihood.value}，{self.severity.value}"
        }


def create_pe_from_dict(d: dict) -> PEData:
    """从字典创建肺栓塞数据"""
    return PEData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        dyspnea=d.get("dyspnea", False),
        pleuritic_chest_pain=d.get("pleuritic_chest_pain", False),
        cough=d.get("cough", False),
        hemoptysis=d.get("hemoptysis", False),
        syncope=d.get("syncope", False),
        leg_pain=d.get("leg_pain", False),
        leg_swelling=d.get("leg_swelling", False),
        hr=d.get("hr", 0),
        rr=d.get("rr", 0),
        sbp=d.get("sbp", 0),
        spo2=d.get("spo2", 100),
        temperature=d.get("temperature", 36.5),
        leg_swelling_unilateral=d.get("leg_swelling_unilateral", False),
        hemoptysis_mild=d.get("hemoptysis_mild", False),
        prior_pe_dvt=d.get("prior_pe_dvt", False),
        recent_surgery=d.get("recent_surgery", False),
        immobility=d.get("immobility", False),
        cancer=d.get("cancer", False),
        estrogen=d.get("estrogen", False),
        pregnancy=d.get("pregnancy", False),
        thrombophilia=d.get("thrombophilia", False),
        d_dimer=d.get("d_dimer", "not_done"),
        ctpa_done=d.get("ctpa_done", False),
        ctpa_result=d.get("ctpa_result", "not_done"),
        ultrasound_done=d.get("ultrasound_done", False),
        ultrasound_result=d.get("ultrasound_result", "not_done")
    )
