"""
病因与诱因引擎 - Causes Engine
Evidence Engine - Tachycardia Care Pathway Assistant
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Cause:
    """病因/诱因"""
    category: str
    name: str
    priority: int  # 1=必须排查, 2=建议排查, 3=可选
    recommendation: str


class CausesEngine:
    """病因与诱因引擎"""
    
    def __init__(self):
        self.causes = []
        self.recommendations = []
    
    def analyze(self, patient_data: dict) -> Dict:
        """分析病因和诱因"""
        
        causes = []
        
        # 心血管相关
        if patient_data.get("chest_pain"):
            causes.append(Cause(
                category="心血管",
                name="急性冠脉综合征 (ACS)",
                priority=1,
                recommendation="立即心电图、肌钙蛋白"
            ))
        
        if patient_data.get("hf"):
            causes.append(Cause(
                category="心血管",
                name="急性心衰",
                priority=1,
                recommendation="BNP/NT-proBNP、床旁超声"
            ))
        
        # 电解质紊乱
        if not patient_data.get("electrolytes_done"):
            causes.append(Cause(
                category="代谢",
                name="电解质紊乱 (K, Mg, Ca)",
                priority=1,
                recommendation="急查电解质"
            ))
        
        # 甲状腺
        if patient_data.get("thyroid") or patient_data.get("hr", 0) > 150:
            causes.append(Cause(
                category="内分泌",
                name="甲状腺功能异常",
                priority=2,
                recommendation="查TSH、FT4"
            ))
        
        # 感染
        if patient_data.get("fever"):
            causes.append(Cause(
                category="感染",
                name="感染/脓毒症",
                priority=1,
                recommendation="血常规、PCT、CRP、培养"
            ))
        
        # 缺氧
        if patient_data.get("spo2", 100) < 95:
            causes.append(Cause(
                category="呼吸",
                name="缺氧",
                priority=1,
                recommendation="血气分析、胸部X线"
            ))
        
        # 贫血
        if not patient_data.get("cbc_done"):
            causes.append(Cause(
                category="血液",
                name="贫血",
                priority=2,
                recommendation="血常规"
            ))
        
        # 药物/物质
        if patient_data.get("caffeine"):
            causes.append(Cause(
                category="物质",
                name="咖啡因过量",
                priority=2,
                recommendation="询问摄入量"
            ))
        
        if patient_data.get("alcohol"):
            causes.append(Cause(
                category="物质",
                name="酒精相关",
                priority=2,
                recommendation="询问饮酒史"
            ))
        
        if patient_data.get("drug_use"):
            causes.append(Cause(
                category="物质",
                name="药物相关 (拟交感神经药物等)",
                priority=2,
                recommendation="询问用药史"
            ))
        
        # 糖尿病
        if patient_data.get("diabetes"):
            causes.append(Cause(
                category="代谢",
                name="糖尿病酮症酸中毒",
                priority=2,
                recommendation="血糖、血气分析"
            ))
        
        # 糖代谢
        if not patient_data.get("glucose_done"):
            causes.append(Cause(
                category="代谢",
                name="低血糖/高血糖",
                priority=2,
                recommendation="急查血糖"
            ))
        
        # 高血压危象
        if patient_data.get("sbp", 0) > 180:
            causes.append(Cause(
                category="心血管",
                name="高血压危象",
                priority=2,
                recommendation="评估靶器官损害"
            ))
        
        # 按优先级排序
        causes.sort(key=lambda x: x.priority)
        
        # 生成推荐检查列表
        workup = self.generate_workup(causes, patient_data)
        
        return {
            "causes": [
                {"category": c.category, "name": c.name, "priority": c.priority, "recommendation": c.recommendation}
                for c in causes
            ],
            "workup": workup
        }
    
    def generate_workup(self, causes: List[Cause], patient_data: dict) -> List[Dict]:
        """生成推荐检查列表"""
        
        workup = []
        
        # 必须检查
        workup_items = [
            {"name": "12导联心电图", "priority": 1, "reason": "心动过速评估基础"},
            {"name": "电解质 (K, Mg, Ca)", "priority": 1, "reason": "常见可纠正诱因"},
        ]
        
        # 根据症状添加
        if patient_data.get("chest_pain"):
            workup_items.append({"name": "肌钙蛋白", "priority": 1, "reason": "排除ACS"})
        
        if patient_data.get("dyspnea"):
            workup_items.append({"name": "BNP/NT-proBNP", "priority": 1, "reason": "评估心衰"})
            workup_items.append({"name": "床旁超声", "priority": 2, "reason": "评估心脏功能"})
        
        if patient_data.get("fever"):
            workup_items.append({"name": "血常规", "priority": 1, "reason": "感染评估"})
            workup_items.append({"name": "PCT/CRP", "priority": 2, "reason": "炎症指标"})
        
        # 常规检查
        if not patient_data.get("glucose_done"):
            workup_items.append({"name": "血糖", "priority": 2, "reason": "代谢因素"})
        
        if not patient_data.get("cbc_done"):
            workup_items.append({"name": "血常规", "priority": 2, "reason": "贫血评估"})
        
        if patient_data.get("thyroid") or patient_data.get("hr", 0) > 150:
            workup_items.append({"name": "甲状腺功能", "priority": 2, "reason": "甲亢/甲减"})
        
        if patient_data.get("alcohol"):
            workup_items.append({"name": "肝功能/酒精水平", "priority": 3, "reason": "酒精相关"})
        
        # 特殊检查
        if patient_data.get("qrs") == "wide":
            workup_items.append({"name": "持续心电监护", "priority": 1, "reason": "警惕恶性心律失常"})
        
        # 按优先级排序
        workup_items.sort(key=lambda x: x["priority"])
        
        return workup_items
