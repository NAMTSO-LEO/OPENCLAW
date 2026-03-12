"""
治疗建议引擎 - Treatment Engine
Evidence Engine - Tachycardia Care Pathway Assistant
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Treatment:
    """治疗建议"""
    category: str
    priority: int  # 1=立即, 2=尽快, 3=择期
    content: str
    evidence: str
    notes: str = ""


class TreatmentEngine:
    """治疗建议引擎"""
    
    def __init__(self):
        self.treatments = []
        self.escalation = []
        self.clinical_judgment = ""
    
    def recommend(self, stability: str, pathway: str, patient_data: dict) -> Dict:
        """生成治疗建议"""
        
        self.treatments = []
        self.escalation = []
        
        if stability == "不稳定":
            self.get_unstable_treatment(pathway, patient_data)
        else:
            self.get_stable_treatment(pathway, patient_data)
        
        return self.get_result()
    
    def get_unstable_treatment(self, pathway: str, patient_data: dict):
        """不稳定患者治疗建议"""
        
        # 立即处理
        self.treatments.extend([
            Treatment(
                category="立即处理",
                priority=1,
                content="建立心电监护、吸氧、静脉通路",
                evidence="AHA ACLS",
                notes="基础生命支持"
            ),
            Treatment(
                category="紧急处理",
                priority=1,
                content="立即准备同步电复律",
                evidence="AHA 2025 Adult Tachyarrhythmia Algorithm",
                notes="不稳定心动过速首选"
            ),
            Treatment(
                category="实验室检查",
                priority=1,
                content="同步抽血：电解质、血糖、肌钙蛋白、血常规、肾功能",
                evidence="AHA",
                notes="评估可纠正诱因"
            ),
            Treatment(
                category="持续监测",
                priority=1,
                content="持续12导联心电监测",
                evidence="ESC",
                notes="观察节律变化"
            ),
            Treatment(
                category="病因处理",
                priority=2,
                content="同步排查并处理诱因：缺血、电解质紊乱、感染、药物",
                evidence="ESC",
                notes="不能只处理心律"
            ),
        ])
        
        # 升级提醒
        self.escalation.extend([
            "若血流动力学进一步恶化",
            "若出现意识改变",
            "若需要反复电复律",
            "若诊断不明确",
        ])
        
        self.clinical_judgment = "不稳定性有脉性心动过速，需立即按ACLS心动过速流程处理"
    
    def get_stable_treatment(self, pathway: str, patient_data: dict):
        """稳定患者治疗建议"""
        
        if "规则窄QRS" in pathway:
            self.treatments.extend([
                Treatment(
                    category="诊断性治疗",
                    priority=1,
                    content="迷走神经刺激 (Valsalva动作)",
                    evidence="AHA/ESC Class I",
                    notes="首选一线"
                ),
                Treatment(
                    category="药物治疗",
                    priority=2,
                    content="腺苷静脉注射 (6-12mg快速推注)",
                    evidence="ESC SVT Guideline Class I",
                    notes="诊断+治疗双重作用"
                ),
                Treatment(
                    category="药物治疗",
                    priority=2,
                    content="如腺苷无效：β受体阻滞剂或钙通道阻滞剂",
                    evidence="ESC Class IIa",
                        notes="注意低血压"
                ),
                Treatment(
                    category="长期管理",
                    priority=3,
                    content="反复发作建议心电生理评估及导管消融",
                    evidence="ESC Class I",
                    notes="根治性治疗"
                ),
            ])
        
        elif "不规则窄QRS" in pathway:
            self.treatments.extend([
                Treatment(
                    category="评估",
                    priority=1,
                    content="评估血流动力学和卒中风险 (CHA2DS2-VASc)",
                    evidence="ESC AF Guideline 2024",
                    notes="决定抗凝策略"
                ),
                Treatment(
                    category="率控制",
                    priority=2,
                    content="β受体阻滞剂或钙通道阻滞剂控制心率",
                    evidence="ESC Class I",
                    notes="急性期控制"
                ),
                Treatment(
                    category="节律控制",
                    priority=2,
                    content="如年轻/症状明显：可考虑药物复律或电复律",
                    evidence="ESC Class IIa",
                    notes="个体化选择"
                ),
                Treatment(
                    category="抗凝",
                    priority=2,
                    content="根据CHA2DS2-VASc评分决定抗凝",
                    evidence="ESC 2024",
                    notes="卒中预防"
                ),
            ])
        
        elif "规则宽QRS" in pathway:
            self.treatments.extend([
                Treatment(
                    category="警示",
                    priority=1,
                    content="按室速处理思路考虑，避免误判为普通室上速",
                    evidence="AHA",
                    notes="宽QRS需谨慎"
                ),
                Treatment(
                    category="紧急处理",
                    priority=1,
                    content="立即心内科/急诊评估",
                    evidence="AHA",
                    notes="需要专科支持"
                ),
                Treatment(
                    category="检查",
                    priority=1,
                    content="详细询问病史、既往ECG、用药史",
                    evidence="临床实践",
                    notes="鉴别差异传导"
                ),
            ])
        
        elif "不规则宽QRS" in pathway:
            self.treatments.extend([
                Treatment(
                    category="高危警示",
                    priority=1,
                    content="立即急诊处理，避免延误",
                    evidence="AHA ACLS",
                    notes="高危心律失常"
                ),
                Treatment(
                    category="紧急处理",
                    priority=1,
                    content="同步电复律准备",
                    evidence="AHA",
                    notes="可能需要紧急复律"
                ),
                Treatment(
                    category="评估",
                    priority=1,
                    content="评估是否为预激综合征伴房颤",
                    evidence="AHA",
                    notes="避免使用房室结阻滞剂"
                ),
            ])
        
        # 升级提醒
        self.escalation.extend([
            "若出现胸痛",
            "若出现晕厥/接近晕厥",
            "若呼吸困难加重",
            "若血压下降",
            "若心率持续不缓解",
            "若出现意识改变",
        ])
        
        self.clinical_judgment = f"稳定性{pathway}，可按常规路径处理"
    
    def get_result(self) -> Dict:
        """获取结果"""
        return {
            "clinical_judgment": self.clinical_judgment,
            "treatments": [
                {
                    "category": t.category,
                    "priority": t.priority,
                    "content": t.content,
                    "evidence": t.evidence,
                    "notes": t.notes
                }
                for t in self.treatments
            ],
            "escalation": self.escalation
        }
