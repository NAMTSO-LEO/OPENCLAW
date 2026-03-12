#!/usr/bin/env python3
"""
临床决策引擎 (Clinical Decision Engine)
功能：急诊分诊、治疗方案、药物管理、ML预测
基于ML模型 + 临床协议
"""

import pickle
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import numpy as np

MODEL_DIR = '/Users/levi/.openclaw/workspace/EvidenceEngine_MVP/model_training'


@dataclass
class Patient:
    """患者信息"""
    id: str = ""
    name: str = ""
    age: int = 0
    gender: int = 0  # 0=男, 1=女
    
    # 主诉
    chief_complaint: str = ""
    
    # 症状
    fever: int = 0
    cough: int = 0
    chest_pain: int = 0
    dyspnea: int = 0
    headache: int = 0
    abdominal_pain: int = 0
    vomiting: int = 0
    
    # 体征
    hr: int = 80
    sbp: int = 120
    dbp: int = 80
    spo2: float = 98
    temp: float = 36.5
    rr: int = 16
    
    # 既往史
    hypertension: int = 0
    diabetes: int = 0
    coronary_heart_disease: int = 0
    heart_failure: int = 0
    stroke: int = 0
    copd: int = 0
    kidney_disease: int = 0
    
    # 用药
    medications: List[str] = field(default_factory=list)
    allergies: List[str] = field(default_factory=list)


class ClinicalDecisionEngine:
    """
    临床决策引擎
    
    主要功能：
    - 急诊分诊分级
    - 治疗方案推荐
    - 药物相互作用检查
    - ML疾病预测
    - 临床路径管理
    """
    
    def __init__(self, model_dir: str = MODEL_DIR):
        self.model_dir = model_dir
        self.models = {}
        self.treatment_protocols = {}
        self.drug_interactions = {}
        self._load_models()
        self._init_treatment_protocols()
        self._init_drug_interactions()
        
    def _load_models(self):
        """加载ML模型"""
        if not os.path.exists(self.model_dir):
            return
            
        model_files = [f for f in os.listdir(self.model_dir) if f.endswith('_model.pkl')]
        for mf in model_files:
            name = mf.replace('_model.pkl', '').replace('_', ' ')
            try:
                with open(os.path.join(self.model_dir, mf), 'rb') as f:
                    self.models[name] = pickle.load(f)
            except:
                pass
        print(f"ClinicalDecisionEngine: 已加载 {len(self.models)} 个模型")
    
    def _init_treatment_protocols(self):
        """初始化治疗方案协议"""
        self.treatment_protocols = {
            "冠心病": {
                "急性期": ["硝酸甘油 0.5mg 舌下", "阿司匹林 300mg 口服", "氯吡格雷 300mg 口服", "肝素 5000U 静注"],
                "长期": ["阿司匹林 100mg qd", "他汀类药物", "β受体阻滞剂", "ACEI/ARB"],
                "监测": ["血压", "心率", "血脂", "肝肾功能"]
            },
            "高血压": {
                "一线": ["ACEI/ARB", "钙通道阻滞剂", "利尿剂", "β受体阻滞剂"],
                "目标": ["普通<140/90", "糖尿病<130/80", "老年人<150/90"],
                "生活方式": ["限盐<6g/天", "戒烟限酒", "适度运动", "减重"]
            },
            "糖尿病": {
                "口服降糖药": ["二甲双胍 0.5g bid", "磺脲类", "DPP-4抑制剂"],
                "胰岛素": ["基础胰岛素", "餐时胰岛素", "强化治疗"],
                "监测": ["空腹血糖4.4-7.0", "餐后<10", "HbA1c<7%"]
            },
            "肺炎": {
                "抗生素": ["头孢曲松 2g qd", "阿奇霉素 0.5g qd", "呼吸氟喹诺酮"],
                "支持": ["补液", "氧疗", "祛痰"],
                "重症标准": ["CURB-65评分≥2"]
            },
            "脑卒中": {
                "缺血性": ["rt-PA溶栓窗口期内", "抗血小板", "抗凝", "降压"],
                "出血性": ["止血", "降颅压", "手术", "控制血压"],
                "二级预防": ["抗血小板", "他汀", "降压", "戒烟"]
            },
            "慢阻肺": {
                "稳定期": ["LAMA", "LABA", "ICS", "祛痰剂"],
                "急性加重": ["支气管扩张剂", "全身激素", "抗生素"],
                "氧疗": ["长期家庭氧疗", "SaO2<88%"]
            },
            "哮喘": {
                "控制": ["ICS", "LABA", "白三烯受体拮抗剂"],
                "缓解": ["SABA", "全身激素"],
                "阶梯治疗": ["1-5级根据控制水平"]
            },
            "心衰": {
                "急性期": ["利尿剂", "血管扩张剂", "正性肌力药"],
                "慢性期": ["ACEI/ARB", "β受体阻滞剂", "醛固酮拮抗剂", "利尿剂"],
                "监测": ["体重", "血压", "BNP", "肾功能"]
            },
            "消化性溃疡": {
                "根除HP": ["PPI+阿莫西林+克拉霉素", "疗程14天"],
                "抑酸": ["PPI标准剂量"],
                "保护胃黏膜": ["硫糖铝", "米曲霉素"]
            },
            "甲亢": {
                "药物": ["甲硫咪唑", "丙硫氧嘧啶"],
                "手术": ["甲状腺次全切"],
                "碘131": ["放射性碘治疗"]
            }
        }
        
    def _init_drug_interactions(self):
        """初始化药物相互作用"""
        self.drug_interactions = {
            ("阿司匹林", "华法林"): "⚠️ 显著增加出血风险，尽量避免联用",
            ("阿司匹林", "布洛芬"): "⚠️ 布洛芬降低阿司匹林心脏保护作用",
            ("华法林", "维生素K"): "⚠️ 维生素K降低华法林抗凝效果",
            ("华法林", "抗生素"): "⚠️ 抗生素可能增强/减弱华法林作用",
            ("地高辛", "胺碘酮"): "⚠️ 胺碘酮增加地高辛浓度，需减量",
            ("地高辛", "红霉素"): "⚠️ 红霉素增加地高辛毒性",
            ("他汀", "红霉素"): "⚠️ 增加肌病/横纹肌溶解风险",
            ("他汀", "贝特类"): "⚠️ 增加肌病风险，需监测CK",
            ("ACEI", "螺内酯"): "⚠️ 增加高钾血症风险，监测血钾",
            ("ACEI/ARB", "利尿剂"): "⚠️ 首次联用注意低血压",
            ("NSAID", "抗凝药"): "⚠️ 显著增加出血风险",
            ("NSAID", "利尿剂"): "⚠️ 加重肾功能不全",
            ("NSAID", "ACEI/ARB"): "⚠️ 加重肾功能不全",
            ("β受体阻滞剂", "胰岛素"): "⚠️ 掩盖低血糖症状",
            ("β受体阻滞剂", "磺脲类"): "⚠️ 掩盖低血糖症状",
            ("氟喹诺酮", "NSAID"): "⚠️ 增加神经系统毒性风险",
            ("西柚", "他汀"): "⚠️ 增加肌病风险",
            ("酒精", "对乙酰氨基酚"): "⚠️ 增加肝毒性",
            ("酒精", "抗生素"): "⚠️ 双硫仑样反应"
        }
        
    # ==================== 核心功能 ====================
    
    def triage(self, patient: Patient) -> Dict:
        """急诊分诊"""
        score = 0
        reasons = []
        
        # 生命体征评分
        if patient.sbp < 90:
            score += 5
            reasons.append("休克血压")
        elif patient.sbp > 200:
            score += 3
            reasons.append("重度高血压")
            
        if patient.hr > 130:
            score += 3
            reasons.append("心动过速")
        elif patient.hr < 50:
            score += 3
            reasons.append("心动过缓")
            
        if patient.spo2 < 90:
            score += 5
            reasons.append("低氧血症")
        elif patient.spo2 < 94:
            score += 2
            reasons.append("轻度低氧")
            
        if patient.temp > 39.5:
            score += 2
            reasons.append("高热")
        elif patient.temp < 35:
            score += 3
            reasons.append("低体温")
            
        if patient.rr > 30:
            score += 2
            reasons.append("呼吸急促")
        
        # 症状评分
        if patient.chest_pain:
            score += 3
            reasons.append("胸痛")
        if patient.dyspnea:
            score += 3
            reasons.append("呼吸困难")
        if patient.abdominal_pain:
            score += 2
            reasons.append("腹痛")
        if patient.headache:
            score += 1
            reasons.append("头痛")
        if patient.vomiting:
            score += 1
            reasons.append("呕吐")
            
        # 既往史评分
        if patient.hypertension:
            score += 1
        if patient.diabetes:
            score += 1
        if patient.copd:
            score += 1
        if patient.kidney_disease:
            score += 2
            
        # 年龄评分
        if patient.age > 75:
            score += 2
        elif patient.age > 60:
            score += 1
        
        # 分级
        if score >= 8:
            level, color, icon = "一级 (危重)", "🔴", "🚨"
            desc = "立即抢救"
            action = "送入抢救室，启动抢救流程"
        elif score >= 5:
            level, color, icon = "二级 (急症)", "🟠", "⚠️"
            desc = "10分钟内就诊"
            action = "尽快安排就诊，优先处理"
        elif score >= 2:
            level, color, icon = "三级 (普通)", "🟡", "📋"
            desc = "30分钟内就诊"
            action = "按顺序排队候诊"
        else:
            level, color, icon = "四级 (非急诊)", "🟢", "✅"
            desc = "按序就诊"
            action = "可门诊就诊"
        
        return {
            "level": level,
            "color": color,
            "icon": icon,
            "score": score,
            "description": desc,
            "action": action,
            "reasons": reasons,
            "vitals": {
                "hr": patient.hr,
                "sbp": patient.sbp,
                "dbp": patient.dbp,
                "spo2": patient.spo2,
                "temp": patient.temp,
                "rr": patient.rr
            }
        }
    
    def get_treatment_plan(self, disease: str, patient: Patient = None) -> Dict:
        """获取治疗方案"""
        # 模糊匹配
        disease_key = disease.lower().replace(' ', '')
        
        matched_protocol = None
        matched_name = None
        
        for name, protocol in self.treatment_protocols.items():
            if name.lower().replace(' ', '') in disease_key:
                matched_protocol = protocol
                matched_name = name
                break
        
        if not matched_protocol:
            return {
                "disease": disease,
                "status": "no_protocol",
                "message": "暂无该疾病的治疗方案，请咨询专科医生",
                "recommendation": "建议到相应专科就诊"
            }
        
        # 检查药物冲突
        warnings = []
        
        if patient and patient.medications:
            all_drugs = patient.medications + [d for drugs in matched_protocol.values() for d in drugs]
            
            for (d1, d2), warning in self.drug_interactions.items():
                for med in patient.medications:
                    if d1.lower() in med.lower() or d1 in med:
                        for drug in all_drugs:
                            if d2.lower() in drug.lower() or d2 in drug:
                                warnings.append(f"{med} + {drug}: {warning}")
        
        # 检查过敏
        allergy_warnings = []
        if patient and patient.allergies:
            for phase, drugs in matched_protocol.items():
                for drug in drugs:
                    for allergy in patient.allergies:
                        if allergy.lower() in drug.lower():
                            allergy_warnings.append(f"⚠️ 患者对{allergy}过敏: {drug}")
        
        return {
            "disease": matched_name,
            "status": "success",
            "protocol": matched_protocol,
            "drug_warnings": warnings,
            "allergy_warnings": allergy_warnings,
            "precautions": self._get_precautions(matched_name)
        }
    
    def _get_precautions(self, disease: str) -> List[str]:
        """获取注意事项"""
        precautions = {
            "冠心病": ["监测胸痛变化", "注意血压心率", "避免剧烈活动", "随身携带硝酸甘油"],
            "高血压": ["规律服药", "监测血压", "限盐", "避免情绪激动"],
            "糖尿病": ["规律饮食", "监测血糖", "注意低血糖", "足部护理"],
            "肺炎": ["多饮水", "注意休息", "按时服药", "复诊评估"],
            "脑卒中": ["绝对卧床", "密切观察意识", "控制血压", "康复训练"],
            "慢阻肺": ["戒烟", "避免受凉", "氧疗注意", "呼吸康复"],
            "心衰": ["限盐限水", "监测体重", "适度活动", "规律用药"]
        }
        
        return precautions.get(disease, ["遵医嘱用药", "定期复诊", "如有不适及时就医"])
    
    def check_drug_interaction(self, drug1: str, drug2: str) -> Optional[str]:
        """检查药物相互作用"""
        for (d1, d2), warning in self.drug_interactions.items():
            if (d1.lower() in drug1.lower() or d1 in drug1) and \
               (d2.lower() in drug2.lower() or d2 in drug2):
                return warning
            if (d2.lower() in drug1.lower() or d2 in drug1) and \
               (d1.lower() in drug2.lower() or d1 in drug2):
                return warning
        return None
    
    def predict(self, disease_name: str, features: List[float]) -> Dict:
        """ML模型预测"""
        # 匹配模型
        target_model = None
        for name in self.models:
            if disease_name.lower() in name.lower():
                target_model = name
                break
        
        if not target_model:
            return {
                "status": "error",
                "message": f"未找到模型: {disease_name}"
            }
        
        model_data = self.models[target_model]
        
        try:
            X = model_data['scaler'].transform([features])
            prob = model_data['model'].predict_proba(X)[0]
            
            risk = "高" if prob[1] > 0.7 else ("中" if prob[1] > 0.4 else "低")
            
            return {
                "status": "success",
                "disease": target_model,
                "probability": float(prob[1]),
                "risk_level": risk,
                "recommendation": self._get_risk_recommendation(risk)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def _get_risk_recommendation(self, risk: str) -> str:
        """风险建议"""
        recommendations = {
            "高": "建议立即就医，进行进一步检查和治疗",
            "中": "建议门诊就诊，完善相关检查",
            "低": "建议定期体检，保持健康生活方式"
        }
        return recommendations.get(risk, "")
    
    def get_clinical_pathway(self, disease: str) -> Dict:
        """获取临床路径"""
        pathways = {
            "冠心病": {
                "入院": ["急诊心电图", "心肌酶谱", "硝酸甘油", "阿司匹林"],
                "检查": ["心脏超声", "冠脉CTA/造影", "血脂", "血糖"],
                "治疗": ["药物治疗", "PCI/CABG"],
                "出院": ["冠心病二级预防", "随访计划"]
            },
            "肺炎": {
                "入院": ["评估CURB-65", "血常规", "血培养", "胸片"],
                "检查": ["胸部CT", "痰培养", "动脉血气"],
                "治疗": ["抗生素", "支持治疗"],
                "出院": ["口服抗生素", "复诊胸片"]
            },
            "脑卒中": {
                "入院": ["头颅CT/MRI", "NIHSS评分", "溶栓评估"],
                "检查": ["脑血管造影", "心脏评估", "颈部血管"],
                "治疗": ["rt-PA/取栓", "抗血小板", "康复"],
                "出院": ["二级预防", "康复计划"]
            }
        }
        
        return pathways.get(disease, {})


def quick_triage(**vitals) -> Dict:
    """快速分诊"""
    patient = Patient(**vitals)
    engine = ClinicalDecisionEngine()
    return engine.triage(patient)


if __name__ == '__main__':
    engine = ClinicalDecisionEngine()
    
    # 测试分诊
    patient = Patient(
        age=65,
        gender=0,
        chest_pain=1,
        dyspnea=1,
        hr=120,
        sbp=160,
        spo2=92,
        temp=37.5,
        hypertension=1,
        diabetes=1
    )
    
    print("=" * 50)
    print("急诊分诊:")
    print(engine.triage(patient))
    
    print("\n治疗方案 (冠心病):")
    result = engine.get_treatment_plan("冠心病", patient)
    print(f"状态: {result['status']}")
    if result['protocol']:
        for phase, drugs in result['protocol'].items():
            print(f"{phase}: {drugs}")
    
    print("\n药物相互作用:")
    print(engine.check_drug_interaction("阿司匹林", "华法林"))
