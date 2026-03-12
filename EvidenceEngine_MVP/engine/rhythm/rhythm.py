"""
节律分类引擎 - Rhythm Engine
Evidence Engine - Tachycardia Care Pathway Assistant
"""

from typing import Dict, List
from dataclasses import dataclass


class RhythmPathway:
    """心律路径"""
    REGULAR_NARROW = "规则窄QRS心动过速"
    IRREGULAR_NARROW = "不规则窄QRS心动过速"
    REGULAR_WIDE = "规则宽QRS心动过速"
    IRREGULAR_WIDE = "不规则宽QRS心动过速"


@dataclass
class Diagnosis:
    """诊断"""
    name: str
    probability: str  # high/medium/low
    notes: str = ""


class RhythmEngine:
    """节律分类引擎"""
    
    def __init__(self):
        self.pathway = ""
        self.diagnoses = []
        self.evidence = []
    
    def classify(self, qrs: str, rhythm: str, hr: int = 0) -> Dict:
        """分类心律"""
        
        # 确定路径
        if qrs == "narrow" and rhythm == "regular":
            self.pathway = RhythmPathway.REGULAR_NARROW
            self.diagnoses = self.get_regular_narrow_diagnoses()
        elif qrs == "narrow" and rhythm == "irregular":
            self.pathway = RhythmPathway.IRREGULAR_NARROW
            self.diagnoses = self.get_irregular_narrow_diagnoses()
        elif qrs == "wide" and rhythm == "regular":
            self.pathway = RhythmPathway.REGULAR_WIDE
            self.diagnoses = self.get_regular_wide_diagnoses()
        elif qrs == "wide" and rhythm == "irregular":
            self.pathway = RhythmPathway.IRREGULAR_WIDE
            self.diagnoses = self.get_irregular_wide_diagnoses()
        else:
            self.pathway = "未知"
            self.diagnoses = []
        
        self.evidence = ["ESC Supraventricular Tachycardia Guideline"]
        
        return self.get_result()
    
    def get_regular_narrow_diagnoses(self) -> List[Diagnosis]:
        """规则窄QRS - 可能的诊断"""
        return [
            Diagnosis("阵发性室上性心动过速 (PSVT/AVNRT/AVRT)", "高", "最常见"),
            Diagnosis("心房扑动伴2:1传导", "中", "ECG可见锯齿波"),
            Diagnosis("窦性心动过速", "低", "通常有诱因"),
            Diagnosis("房性心动过速", "中", "自律性或折返性"),
        ]
    
    def get_irregular_narrow_diagnoses(self) -> List[Diagnosis]:
        """不规则窄QRS - 可能的诊断"""
        return [
            Diagnosis("心房颤动 (AF)", "高", "最常见"),
            Diagnosis("多源性房性心动过速 (MAT)", "中", "多源性P波"),
            Diagnosis("房扑伴不规则传导", "中", "需仔细辨认"),
        ]
    
    def get_regular_wide_diagnoses(self) -> List[Diagnosis]:
        """规则宽QRS - 可能的诊断"""
        return [
            Diagnosis("室性心动过速 (VT)", "高", "首选考虑"),
            Diagnosis("室上性心动过速伴差异传导", "中", "原有束支阻滞"),
            Diagnosis("室上性心动过速伴药物影响", "低", "药物导致QRS增宽"),
        ]
    
    def get_irregular_wide_diagnoses(self) -> List[Diagnosis]:
        """不规则宽QRS - 可能的诊断"""
        return [
            Diagnosis("预激综合征伴房颤", "高", "高危！需紧急处理"),
            Diagnosis("多形性室性心动过速", "高", "可转为室颤"),
            Diagnosis("尖端扭转型室速", "中", "长QT综合征"),
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        return {
            "pathway": self.pathway,
            "diagnoses": [
                {"name": d.name, "probability": d.probability, "notes": d.notes}
                for d in self.diagnoses
            ],
            "evidence": self.evidence
        }
    
    def get_pathway_guidance(self) -> str:
        """获取路径指导"""
        guidance = {
            RhythmPathway.REGULAR_NARROW: "优先考虑室上速路径：迷走刺激→腺苷→专科评估",
            RhythmPathway.IRREGULAR_NARROW: "考虑房颤/房扑路径：评估血流动力学、卒中风险",
            RhythmPathway.REGULAR_WIDE: "按室速处理思路考虑：避免误判，及时专科会诊",
            RhythmPathway.IRREGULAR_WIDE: "高危警示：立即急诊处理，避免延误"
        }
        return guidance.get(self.pathway, "")
