"""
心动过速诊治决策引擎
Tachycardia Decision Engine
Clinical Decision Support System MVP
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class Stability(Enum):
    """血流动力学稳定性"""
    STABLE = "稳定"
    UNSTABLE = "不稳定"


class RhythmPattern(Enum):
    """心律类型"""
    REGULAR_NARROW = "规则窄QRS"
    IRREGULAR_NARROW = "不规则窄QRS"
    REGULAR_WIDE = "规则宽QRS"
    IRREGULAR_WIDE = "不规则宽QRS"


@dataclass
class Patient:
    """患者数据"""
    age: int
    gender: str  # male/female
    hr: int  # 心率
    sbp: int  # 收缩压
    dbp: int  # 舒张压
    spo2: int  # 血氧
    symptoms: List[str]  # 症状列表
    ecg: str  # ECG结果
    history: List[str]  # 既往史


@dataclass
class Recommendation:
    """建议"""
    priority: int  # 优先级 1=最高
    category: str  # 分类
    content: str  # 内容
    evidence: str  # 证据来源


class TachycardiaEngine:
    """心动过速决策引擎"""
    
    def __init__(self):
        self.recommendations: List[Recommendation] = []
        self.diagnosis: List[Dict] = []
        self.risk_level: str = ""
        self.evidence_sources: List[str] = []
    
    def assess_stability(self, patient: Patient) -> Stability:
        """评估血流动力学稳定性"""
        # AHA: 不稳定征象
        unstable_signs = []
        
        # 低血压
        if patient.sbp < 90:
            unstable_signs.append("低血压(SBP<90)")
        
        # 胸痛
        if "胸痛" in patient.symptoms or "胸闷" in patient.symptoms:
            unstable_signs.append("胸痛/胸闷")
        
        # 意识改变
        if "意识改变" in patient.symptoms or "晕厥" in patient.symptoms:
            unstable_signs.append("意识改变/晕厥")
        
        # 呼吸困难
        if "呼吸困难" in patient.symptoms:
            unstable_signs.append("呼吸困难")
        
        # 急性心衰
        if "急性心衰" in patient.symptoms:
            unstable_signs.append("急性心衰")
        
        if unstable_signs:
            self.risk_level = f"高危 - 不稳定性心动过速"
            self.recommendations.append(Recommendation(
                priority=1,
                category="危险分层",
                content=f"存在不稳定表现: {', '.join(unstable_signs)}",
                evidence="AHA 2025 Adult Tachyarrhythmia With a Pulse Algorithm"
            ))
            return Stability.UNSTABLE
        else:
            self.risk_level = "稳定"
            return Stability.STABLE
    
    def identify_rhythm(self, patient: Patient) -> RhythmPattern:
        """识别心律类型"""
        # 基于ECG描述判断
        ecg = patient.ecg.lower()
        
        if "窄qrs" in ecg or "narrow" in ecg:
            if "规则" in ecg or "regular" in ecg:
                return RhythmPattern.REGULAR_NARROW
            else:
                return RhythmPattern.IRREGULAR_NARROW
        elif "宽qrs" in ecg or "wide" in ecg:
            if "规则" in ecg or "regular" in ecg:
                return RhythmPattern.REGULAR_WIDE
            else:
                return RhythmPattern.IRREGULAR_WIDE
        
        # 默认窄QRS规则
        return RhythmPattern.REGULAR_NARROW
    
    def get_differential_diagnosis(self, patient: Patient, rhythm: RhythmPattern) -> List[Dict]:
        """鉴别诊断"""
        diagnoses = []
        
        if rhythm == RhythmPattern.REGULAR_NARROW:
            diagnoses = [
                {"diagnosis": "阵发性室上性心动过速(PSVT/AVNRT/AVRT)", "probability": "高"},
                {"diagnosis": "心房扑动伴2:1传导", "probability": "中"},
                {"diagnosis": "窦性心动过速", "probability": "低"},
                {"diagnosis": "房性心动过速", "probability": "低-中"},
            ]
            self.evidence_sources.append("ESC Supraventricular Tachycardia Guideline")
        
        elif rhythm == RhythmPattern.IRREGULAR_NARROW:
            diagnoses = [
                {"diagnosis": "心房颤动", "probability": "高"},
                {"diagnosis": "多源性房性心动过速", "probability": "中"},
            ]
            self.evidence_sources.append("ESC Atrial Fibrillation Guideline 2024")
        
        elif rhythm == RhythmPattern.REGULAR_WIDE:
            diagnoses = [
                {"diagnosis": "室性心动过速(VT)", "probability": "高"},
                {"diagnosis": "室上性心动过速伴差传", "probability": "中"},
            ]
            self.evidence_sources.append("AHA VT/SVT Discrimination Algorithm")
        
        elif rhythm == RhythmPattern.IRREGULAR_WIDE:
            diagnoses = [
                {"diagnosis": "预激综合征伴房颤", "probability": "高-危"},
                {"diagnosis": "多形性室速", "probability": "高-危"},
            ]
            self.evidence_sources.append("AHA Advanced Cardiac Life Support")
        
        return diagnoses
    
    def get_treatment_plan(self, patient: Patient, stability: Stability, 
                          rhythm: RhythmPattern) -> List[Recommendation]:
        """治疗方案"""
        treatments = []
        
        if stability == Stability.UNSTABLE:
            # 不稳定：同步电复律
            treatments.extend([
                Recommendation(
                    priority=1,
                    category="立即处理",
                    content="建立监护、吸氧、静脉通路",
                    evidence="AHA ACLS"
                ),
                Recommendation(
                    priority=1,
                    category="紧急处理",
                    content="立即准备同步电复律",
                    evidence="AHA 2025 Adult Tachyarrhythmia Algorithm"
                ),
                Recommendation(
                    priority=1,
                    category="实验室检查",
                    content="同步抽血: 电解质、血糖、肌钙蛋白、血常规、肾功能",
                    evidence="AHA"
                ),
                Recommendation(
                    priority=2,
                    category="持续监测",
                    content="持续12导联ECG监测",
                    evidence="ESC"
                ),
                Recommendation(
                    priority=2,
                    category="病因排查",
                    content="处理诱因: 缺血、电解质紊乱、感染、药物",
                    evidence="ESC"
                ),
            ])
        
        else:
            # 稳定：根据心律类型处理
            if rhythm == RhythmPattern.REGULAR_NARROW:
                treatments.extend([
                    Recommendation(
                        priority=1,
                        category="诊断性治疗",
                        content="迷走神经刺激(Valsalva动作)",
                        evidence="AHA/ESC"
                    ),
                    Recommendation(
                        priority=2,
                        category="药物治疗",
                        content="如无效，考虑腺苷(诊断+治疗)",
                        evidence="ESC SVT Guideline"
                    ),
                    Recommendation(
                        priority=3,
                        category="长期管理",
                        content="反复发作建议心电生理评估及导管消融",
                        evidence="ESC"
                    ),
                ])
            
            elif rhythm == RhythmPattern.IRREGULAR_NARROW:
                treatments.extend([
                    Recommendation(
                        priority=1,
                        category="评估",
                        content="评估血流动力学、卒中风险(CHADS2-VASc)",
                        evidence="ESC AF Guideline"
                    ),
                    Recommendation(
                        priority=2,
                        category="治疗",
                        content="率控制或节律控制策略",
                        evidence="ESC AF Guideline 2024"
                    ),
                ])
            
            elif rhythm == RhythmPattern.REGULAR_WIDE:
                treatments.extend([
                    Recommendation(
                        priority=1,
                        category="警示",
                        content="按室速处理思路考虑，避免误判",
                        evidence="AHA"
                    ),
                    Recommendation(
                        priority=1,
                        category="紧急处理",
                        content="立即心内科/急诊评估",
                        evidence="AHA"
                    ),
                ])
        
        return treatments
    
    def get_workup(self, patient: Patient) -> List[Recommendation]:
        """推荐检查"""
        workups = [
            Recommendation(
                priority=1,
                category="必查",
                content="12导联心电图",
                evidence="所有胸痛/心动过速患者"
            ),
            Recommendation(
                priority=1,
                category="必查",
                content="电解质(K, Mg, Ca)",
                evidence="心律失常常规"
            ),
            Recommendation(
                priority=1,
                category="必查",
                content="肌钙蛋白(伴胸痛时)",
                evidence="ACS排除"
            ),
            Recommendation(
                priority=2,
                category="选查",
                content="甲状腺功能(原因不明时)",
                evidence="甲亢可致心动过速"
            ),
            Recommendation(
                priority=2,
                category="选查",
                content="超声心动图(怀疑结构性心脏病)",
                evidence="ESC"
            ),
            Recommendation(
                priority=3,
                category="病史",
                content="药物/咖啡因/酒精使用史",
                evidence="常见诱因"
            ),
        ]
        return workups
    
    def analyze(self, patient: Patient) -> Dict:
        """完整分析"""
        # 1. 评估稳定性
        stability = self.assess_stability(patient)
        
        # 2. 识别心律
        rhythm = self.identify_rhythm(patient)
        
        # 3. 鉴别诊断
        self.diagnosis = self.get_differential_diagnosis(patient, rhythm)
        
        # 4. 治疗方案
        treatments = self.get_treatment_plan(patient, stability, rhythm)
        
        # 5. 推荐检查
        workups = self.get_workup(patient)
        
        return {
            "risk_level": self.risk_level,
            "stability": stability.value,
            "rhythm_pattern": rhythm.value,
            "diagnosis": self.diagnosis,
            "treatments": treatments,
            "workups": workups,
            "evidence": list(set(self.evidence_sources))
        }


def demo_case():
    """演示病例"""
    # 不稳定病例
    patient_unstable = Patient(
        age=62,
        gender="male",
        hr=168,
        sbp=86,
        dbp=58,
        spo2=95,
        symptoms=["心悸", "胸闷", "出汗", "烦躁"],
        ecg="规则性心动过速，QRS窄",
        history=["高血压", "2型糖尿病"]
    )
    
    # 稳定病例
    patient_stable = Patient(
        age=35,
        gender="female",
        hr=178,
        sbp=122,
        dbp=76,
        spo2=98,
        symptoms=["心悸"],
        ecg="规则窄QRS心动过速",
        history=[]
    )
    
    engine = TachycardiaEngine()
    result = engine.analyze(patient_unstable)
    
    return result


if __name__ == "__main__":
    result = demo_case()
    import json
    print(json.dumps(result, ensure_ascii=False, indent=2))
