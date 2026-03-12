"""
证据引擎 - Evidence Engine
Evidence Engine - Tachycardia Care Pathway Assistant
"""

from typing import Dict, List


EVIDENCE_DATABASE = {
    # AHA 指南
    "AHA Tachycardia Algorithm": {
        "title": "AHA成人有脉性心动过速算法",
        "year": 2025,
        "url": "https://cpr.heart.org/",
        "key_points": [
            "不稳定征象：低血压、休克体征、缺血性胸痛、急性心衰、意识改变",
            "不稳定：有脉性心动过速 → 同步电复律",
            "稳定：根据QRS形态和节律分类处理"
        ]
    },
    
    "AHA ACLS": {
        "title": "AHA高级心血管生命支持",
        "year": 2025,
        "url": "https://cpr.heart.org/",
        "key_points": [
            "室性心动过速：同步电复律",
            "室上性心动过速：迷走刺激→腺苷→同步电复律"
        ]
    },
    
    # ESC 指南
    "ESC SVT Guideline": {
        "title": "ESC室上性心动过速管理指南",
        "year": 2023,
        "url": "https://www.escardio.org/",
        "key_points": [
            "规则窄QRS心动过速：迷走刺激→腺苷",
            "反复发作：导管消融作为一线治疗",
            "腺苷：诊断+治疗双重作用"
        ]
    },
    
    "ESC AF Guideline 2024": {
        "title": "ESC心房颤动管理指南",
        "year": 2024,
        "url": "https://www.escardio.org/",
        "key_points": [
            "CHA2DS2-VASc评分决定抗凝策略",
            "率控制：β受体阻滞剂、钙通道阻滞剂",
            "节律控制：药物复律、电复律、导管消融"
        ]
    },
    
    # 临床要点
    "Clinical Pearls": {
        "title": "临床要点",
        "year": 2024,
        "url": "",
        "key_points": [
            "宽QRS心动过速：首选考虑室速，直至有明确证据排除",
            "不规则宽QRS：预激综合征伴房颤需紧急处理",
            "电解质紊乱是常见可纠正诱因",
            "甲状腺功能异常是持续性心动过速的常见原因"
        ]
    }
}


class EvidenceEngine:
    """证据引擎"""
    
    def __init__(self):
        self.evidence = []
    
    def get_evidence_for_stability(self, stability: str) -> List[Dict]:
        """获取稳定性相关证据"""
        
        if stability == "不稳定":
            return [
                {
                    "title": "AHA 2025 Adult Tachyarrhythmia With a Pulse Algorithm",
                    "key_point": "不稳定有脉性心动过速：立即同步电复律，不应反复药物尝试",
                    "level": "Class I",
                    "source": "AHA"
                }
            ]
        return []
    
    def get_evidence_for_pathway(self, pathway: str) -> List[Dict]:
        """获取路径相关证据"""
        
        evidence_map = {
            "规则窄QRS": [
                {
                    "title": "ESC Supraventricular Tachycardia Guideline 2023",
                    "key_point": "迷走神经刺激是一线，腺苷可用于诊断和治疗",
                    "level": "Class I",
                    "source": "ESC"
                }
            ],
            "不规则窄QRS": [
                {
                    "title": "ESC Atrial Fibrillation Guideline 2024",
                    "key_point": "根据CHA2DS2-VASc评分制定抗凝策略",
                    "level": "Class I",
                    "source": "ESC"
                }
            ],
            "宽QRS": [
                {
                    "title": "AHA VT/SVT Discrimination",
                    "key_point": "宽QRS心动过速：首选考虑室速",
                    "level": "Class I",
                    "source": "AHA"
                }
            ]
        }
        
        for key, ev in evidence_map.items():
            if key in pathway:
                return ev
        
        return []
    
    def get_all_evidence(self, stability: str, pathway: str) -> Dict:
        """获取所有相关证据"""
        
        all_evidence = []
        
        # 添加稳定性证据
        all_evidence.extend(self.get_evidence_for_stability(stability))
        
        # 添加路径证据
        all_evidence.extend(self.get_evidence_for_pathway(pathway))
        
        # 添加临床要点
        all_evidence.append({
            "title": "临床要点",
            "key_point": "心动过速评估原则：先评估稳定性，再分析节律，最后寻找病因",
            "level": "Best Practice",
            "source": "Clinical"
        })
        
        return {
            "evidence": all_evidence,
            "guidelines": list(EVIDENCE_DATABASE.keys())
        }
    
    def get_evidence_summary(self, stability: str, pathway: str) -> str:
        """获取证据摘要"""
        
        summary = "### 核心证据摘要\n\n"
        
        if stability == "不稳定":
            summary += "**不稳定心动过速**：\n"
            summary += "- AHA指南：优先同步电复律\n"
            summary += "- 不应反复药物尝试，以免延误\n\n"
        
        if "规则窄QRS" in pathway:
            summary += "**规则窄QRS心动过速**：\n"
            summary += "- ESC指南：迷走刺激→腺苷→消融\n\n"
        
        if "不规则窄QRS" in pathway:
            summary += "**不规则窄QRS心动过速（房颤）**：\n"
            summary += "- ESC 2024：CHA2DS2-VASc指导抗凝\n\n"
        
        if "宽QRS" in pathway:
            summary += "**宽QRS心动过速**：\n"
            summary += "- 首选考虑室速，避免误诊\n\n"
        
        return summary
