#!/usr/bin/env python3
"""
增强型临床决策引擎 v2.0
Advanced Clinical Decision Support Engine
包含：疾病诊断、鉴别诊断、治疗方案、药物相互作用、检查建议
"""

import pickle
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import numpy as np

MODEL_DIR = '/Users/levi/.openclaw/workspace/EvidenceEngine_MVP/model_training'

@dataclass
class Patient:
    """完整患者信息"""
    # 基本信息
    id: str = ""
    name: str = ""
    age: int = 0
    gender: int = 0  # 0=男, 1=女
    
    # 主诉
    chief_complaint: str = ""
    symptom_duration: str = ""
    
    # 症状 (二进制)
    fever: int = 0
    chills: int = 0
    cough: int = 0
    sputum: int = 0
    chest_pain: int = 0
    dyspnea: int = 0
    headache: int = 0
    dizziness: int = 0
    nausea: int = 0
    vomiting: int = 0
    abdominal_pain: int = 0
    diarrhea: int = 0
    constipation: int = 0
    fatigue: int = 0
    weight_loss: int = 0
    night_sweat: int = 0
    rash: int = 0
    joint_pain: int = 0
    back_pain: int = 0
    urinary_symptoms: int = 0
    
    # 体征
    hr: int = 80
    sbp: int = 120
    dbp: int = 80
    rr: int = 16
    temp: float = 36.5
    spo2: float = 98
    bmi: float = 22
    
    # 既往史
    hypertension: int = 0
    diabetes: int = 0
    coronary_heart_disease: int = 0
    heart_failure: int = 0
    stroke: int = 0
    copd: int = 0
    asthma: int = 0
    kidney_disease: int = 0
    liver_disease: int = 0
    cancer: int = 0
    tb: int = 0
    hiv: int = 0
    
    # 个人史
    smoking: int = 0
    alcohol: int = 0
    drug_use: int = 0
    
    # 家族史
    family_hypertension: int = 0
    family_diabetes: int = 0
    family_cancer: int = 0
    
    # 过敏史
    allergies: List[str] = field(default_factory=list)
    
    # 用药史
    medications: List[str] = field(default_factory=list)


class EnhancedClinicalEngine:
    """增强型临床决策引擎"""
    
    def __init__(self, model_dir: str = MODEL_DIR):
        self.model_dir = model_dir
        self.models = {}
        self.diagnosis_rules = {}
        self.treatment_protocols = {}
        self.drug_interactions = {}
        self._load_models()
        self._init_clinical_knowledge()
        
    def _load_models(self):
        """加载ML模型"""
        if not os.path.exists(self.model_dir):
            print(f"警告: 模型目录不存在: {self.model_dir}")
            return
            
        model_files = [f for f in os.listdir(self.model_dir) if f.endswith('_model.pkl')]
        for mf in model_files:
            name = mf.replace('_model.pkl', '').replace('_', ' ')
            try:
                with open(os.path.join(self.model_dir, mf), 'rb') as f:
                    self.models[name] = pickle.load(f)
            except Exception as e:
                print(f"加载模型失败 {mf}: {e}")
        print(f"已加载 {len(self.models)} 个疾病预测模型")
    
    def _init_clinical_knowledge(self):
        """初始化临床知识库"""
        
        # 诊断规则 (症状 -> 疾病)
        self.diagnosis_rules = {
            # 心血管系统
            "胸痛+心悸": ["冠心病", "心律失常", "心衰"],
            "胸痛+呼吸困难": ["冠心病", "肺栓塞", "肺炎", "气胸"],
            "胸痛+高血压": ["冠心病", "主动脉夹层"],
            "头晕+心悸": ["心律失常", "贫血", "低血糖"],
            "晕厥+心悸": ["心律失常", "颈动脉窦综合征"],
            
            # 呼吸系统
            "咳嗽+发热": ["肺炎", "支气管炎", "肺结核", "新冠"],
            "咳嗽+咳痰": ["支气管炎", "肺炎", "慢阻肺", "支气管扩张"],
            "咳嗽+咯血": ["肺结核", "支气管扩张", "肺癌", "肺炎"],
            "呼吸困难+喘息": ["哮喘", "慢阻肺", "心衰", "肺栓塞"],
            "呼吸困难+胸痛": ["肺栓塞", "气胸", "肺炎", "心衰"],
            
            # 消化系统
            "腹痛+恶心呕吐": ["胃肠炎", "阑尾炎", "胰腺炎", "肠梗阻"],
            "腹痛+发热": ["阑尾炎", "胆囊炎", "腹膜炎", "盆腔炎"],
            "腹痛+血便": ["肠癌", "炎症性肠病", "痔疮"],
            "腹痛+黄疸": ["肝炎", "胆结石", "胰腺癌"],
            "呕血+黑便": ["消化性溃疡", "食管胃底静脉曲张", "胃癌"],
            "腹泻+发热": ["胃肠炎", "炎症性肠病", "细菌性痢疾"],
            "腹泻+血便": ["溃疡性结肠炎", "肠癌", "细菌性痢疾"],
            
            # 神经系统
            "头痛+发热": ["脑膜炎", "脑炎", "偏头痛"],
            "头痛+呕吐": ["脑膜炎", "脑肿瘤", "偏头痛", "高血压脑病"],
            "头痛+视力障碍": ["青光眼", "脑肿瘤", "偏头痛"],
            "意识障碍+发热": ["脑膜炎", "脑炎", "热射病"],
            "肢体无力+言语不清": ["脑卒中", "吉兰-巴雷综合征"],
            
            # 泌尿系统
            "尿频+尿急+尿痛": ["泌尿道感染", "前列腺炎", "膀胱炎"],
            "腰痛+发热": ["肾盂肾炎", "泌尿系结石"],
            "血尿+蛋白尿": ["肾炎", "泌尿系结石", "肿瘤"],
            "少尿+水肿": ["肾功能不全", "心衰", "肾病综合征"],
            
            # 内分泌
            "多饮+多尿+多食": ["糖尿病", "尿崩症"],
            "体重下降+心悸": ["甲亢", "糖尿病", "恶性肿瘤"],
            "怕热+多汗+手颤": ["甲亢"],
            "怕冷+乏力+便秘": ["甲减"],
            
            # 血液系统
            "乏力+苍白": ["贫血", "慢性病", "白血病"],
            "发热+出血": ["白血病", "血小板减少性紫癜"],
            "淋巴结肿大+发热": ["淋巴瘤", "白血病", "结核"],
            
            # 其他
            "发热+皮疹": ["麻疹", "风疹", "猩红热", "药物热"],
            "关节痛+发热": ["类风湿", "系统性红斑狼疮", "痛风"],
            "发热+淋巴结肿大": ["结核", "淋巴瘤", "HIV"],
        }
        
        # 治疗方案协议
        self.treatment_protocols = {
            "冠心病": {
                "一线": ["阿司匹林", "氯吡格雷", "他汀类", "β受体阻滞剂", "ACEI/ARB"],
                "急诊": ["硝酸甘油", "吗啡", "肝素", "PCI术"],
                "生活方式": ["低盐低脂", "戒烟限酒", "适度运动"]
            },
            "高血压": {
                "一线": ["ACEI/ARB", "钙通道阻滞剂", "利尿剂", "β受体阻滞剂"],
                "目标": ["<140/90 mmHg", "糖尿病<130/80"],
                "生活方式": ["减重", "限盐", "运动", "戒烟"]
            },
            "糖尿病": {
                "一线": ["二甲双胍"],
                "二线": ["磺脲类", "DPP-4抑制剂", "SGLT2抑制剂", "GLP-1激动剂"],
                "胰岛素": ["基础+餐时", "强化治疗"],
                "监测": ["空腹血糖", "餐后血糖", "HbA1c", "眼底", "肾功能"]
            },
            "肺炎": {
                "抗生素": ["头孢类", "呼吸氟喹诺酮", "大环内酯"],
                "支持": ["补液", "氧疗", "祛痰"],
                "重症": ["ICU监护", "机械通气"]
            },
            "脑卒中": {
                "缺血性": ["rt-PA溶栓", "取栓", "抗血小板", "抗凝"],
                "出血性": ["降压", "止血", "手术"],
                "二级预防": ["抗血小板", "他汀", "降压", "戒烟"]
            },
            "慢阻肺": {
                "稳定期": ["LAMA", "LABA", "ICS", "祛痰剂"],
                "急性加重": ["支气管扩张剂", "全身激素", "抗生素"],
                "氧疗": ["长期家庭氧疗"]
            },
            "哮喘": {
                "控制": ["ICS", "LABA", "白三烯受体拮抗剂"],
                "缓解": ["SABA", "全身激素"],
                "严重": ["奥马珠单抗", "美泊利单抗"]
            },
            "胃炎/胃溃疡": {
                "根除HP": ["PPI+抗生素"],
                "保护": ["PPI", "胃黏膜保护剂"],
                "生活方式": ["规律饮食", "戒烟酒", "避免NSAID"]
            },
            "甲亢": {
                "药物": ["甲硫咪唑", "丙硫氧嘧啶"],
                "手术": ["甲状腺次全切"],
                "碘131": ["放射性碘治疗"]
            },
            "甲减": {
                "治疗": ["左甲状腺素"],
                "监测": ["TSH", "游离T4"]
            }
        }
        
        # 药物相互作用
        self.drug_interactions = {
            ("阿司匹林", "华法林"): "增加出血风险",
            ("阿司匹林", "布洛芬"): "降低心脏保护作用",
            ("华法林", "维生素K"): "降低抗凝效果",
            ("地高辛", "胺碘酮"): "增加地高辛毒性",
            ("他汀", "红霉素"): "增加肌病风险",
            ("ACEI", "螺内酯"): "增加高钾血症风险",
            ("NSAID", "抗凝药"): "增加出血风险",
            ("NSAID", "利尿剂"): "加重肾功能不全",
            ("氟喹诺酮", "NSAID"): "增加神经系统毒性",
            ("β受体阻滞剂", "胰岛素"): "掩盖低血糖症状",
            ("西柚", "他汀"): "增加肌病风险",
            ("酒精", "对乙酰氨基酚"): "增加肝毒性",
        }
        
    def diagnose(self, patient: Patient) -> Dict:
        """基于症状的智能诊断"""
        symptoms = []
        if patient.fever: symptoms.append("发热")
        if patient.cough: symptoms.append("咳嗽")
        if patient.chest_pain: symptoms.append("胸痛")
        if patient.dyspnea: symptoms.append("呼吸困难")
        if patient.headache: symptoms.append("头痛")
        if patient.dizziness: symptoms.append("头晕")
        if patient.nausea: symptoms.append("恶心")
        if patient.vomiting: symptoms.append("呕吐")
        if patient.abdominal_pain: symptoms.append("腹痛")
        if patient.diarrhea: symptoms.append("腹泻")
        if patient.fatigue: symptoms.append("乏力")
        if patient.weight_loss: symptoms.append("体重下降")
        if patient.night_sweat: symptoms.append("盗汗")
        
        # 构建症状组合
        possible_diseases = set()
        symptom_key = "+".join(symptoms[:3])  # 取前3个主要症状
        
        # 规则匹配
        for key, diseases in self.diagnosis_rules.items():
            if any(s in key for s in symptoms):
                possible_diseases.update(diseases)
        
        # 既往史加权
        if patient.hypertension:
            possible_diseases.add("冠心病")
            possible_diseases.add("脑卒中")
        if patient.diabetes:
            possible_diseases.add("糖尿病")
            possible_diseases.add("冠心病")
        if patient.smoking:
            possible_diseases.add("慢阻肺")
            possible_diseases.add("肺癌")
            
        return {
            "symptoms": symptoms,
            "possible_diseases": list(possible_diseases),
            "reasoning": self._build_reasoning(symptoms, patient)
        }
    
    def _build_reasoning(self, symptoms: List[str], patient: Patient) -> List[str]:
        """构建诊断推理"""
        reasoning = []
        
        if "胸痛" in symptoms and patient.hypertension:
            reasoning.append("高血压+胸痛 → 需排除冠心病、主动脉夹层")
        if "发热" in symptoms and patient.cough:
            reasoning.append("发热+咳嗽 → 考虑呼吸系统感染")
        if "乏力" in symptoms and patient.weight_loss:
            reasoning.append("乏力+体重下降 → 需排除恶性肿瘤、慢性感染")
        if "头痛" in symptoms and patient.fever:
            reasoning.append("发热+头痛 → 需排除脑膜炎、脑炎")
        if patient.age > 60 and "胸痛" in symptoms:
            reasoning.append("老年+胸痛 → 高度警惕心血管疾病")
            
        return reasoning
    
    def get_treatment_plan(self, disease: str, patient: Patient = None) -> Dict:
        """获取治疗方案"""
        disease_normalized = disease.lower().replace(' ', '')
        
        for protocol_name, protocol in self.treatment_protocols.items():
            if protocol_name.lower().replace(' ', '') in disease_normalized:
                return {
                    "disease": protocol_name,
                    "protocol": protocol,
                    "notes": self._get_drug_warnings(protocol, patient)
                }
        
        return {
            "disease": disease,
            "protocol": {},
            "note": "暂无详细治疗方案，请咨询专科医生"
        }
    
    def _get_drug_warnings(self, protocol: Dict, patient: Patient) -> List[str]:
        """药物警告"""
        warnings = []
        
        if patient and patient.allergies:
            for drug_list in protocol.values():
                for drug in drug_list:
                    if any(a.lower() in drug.lower() for a in patient.allergies):
                        warnings.append(f"⚠️ 患者对{drug}过敏!")
        
        if patient and patient.medications:
            for drug_list in protocol.values():
                for drug in drug_list:
                    for med in patient.medications:
                        key = (med, drug)
                        if key in self.drug_interactions:
                            warnings.append(f"⚠️ {med}与{drug}相互作用: {self.drug_interactions[key]}")
        
        return warnings
    
    def check_drug_interaction(self, drug1: str, drug2: str) -> Optional[str]:
        """检查药物相互作用"""
        key = (drug1.lower(), drug2.lower())
        for (d1, d2), interaction in self.drug_interactions.items():
            if (d1 in drug1.lower() and d2 in drug2.lower()) or \
               (d2 in drug1.lower() and d1 in drug2.lower()):
                return interaction
        return None
    
    def triage(self, patient: Patient) -> Dict:
        """急诊分诊"""
        score = 0
        reasons = []
        
        # 生命体征 (最重要)
        if patient.sbp < 90:
            score += 5
            reasons.append("休克血压")
        elif patient.sbp > 200:
            score += 3
            reasons.append("严重高血压")
            
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
            
        # 症状严重程度
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
        if patient.vomiting:
            score += 1
            
        # 既往史风险
        if patient.hypertension:
            score += 1
        if patient.diabetes:
            score += 1
        if patient.copd:
            score += 1
        if patient.kidney_disease:
            score += 2
            
        # 年龄风险
        if patient.age > 75:
            score += 2
        elif patient.age > 60:
            score += 1
            
        # 分级
        if score >= 8:
            level, color, desc = "一级 (危重)", "🔴", "立即抢救"
        elif score >= 5:
            level, color, desc = "二级 (急症)", "🟠", "10分钟内就诊"
        elif score >= 2:
            level, color, desc = "三级 (普通)", "🟡", "30分钟内就诊"
        else:
            level, color, desc = "四级 (非急诊)", "🟢", "按序就诊"
            
        return {
            "level": level,
            "score": score,
            "reasons": reasons,
            "color": color,
            "description": desc,
            "vital_signs": {
                "hr": patient.hr,
                "sbp": patient.sbp,
                "spo2": patient.spo2,
                "temp": patient.temp
            }
        }
    
    def predict_disease(self, disease_name: str, features: List[float]) -> Dict:
        """ML模型预测"""
        # 尝试匹配模型
        target_model = None
        for name in self.models:
            if disease_name.lower() in name.lower():
                target_model = name
                break
                
        if not target_model:
            return {"error": f"未找到疾病模型: {disease_name}"}
        
        model_data = self.models[target_model]
        
        try:
            X = model_data['scaler'].transform([features])
            prob = model_data['model'].predict_proba(X)[0]
            
            return {
                "disease": target_model,
                "probability": float(prob[1]) if len(prob) > 1 else float(prob[0]),
                "risk_level": "高" if prob[1] > 0.7 else ("中" if prob[1] > 0.4 else "低")
            }
        except Exception as e:
            return {"error": str(e)}
    
    def generate_report(self, patient: Patient) -> str:
        """生成临床报告"""
        diag = self.diagnose(patient)
        tri = self.triage(patient)
        
        report = f"""
==========================================
        临床辅助决策报告
==========================================
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

【患者信息】
姓名: {patient.name or '未记录'}
年龄: {patient.age}岁
性别: {'女' if patient.gender else '男'}

【主诉】
{patient.chief_complaint or '未记录'}

【急诊分诊】
{tri['color']} 分诊等级: {tri['level']}
评分: {tri['score']}
描述: {tri['description']}

【生命体征】
心率: {patient.hr} bpm
血压: {patient.sbp}/{patient.dbp} mmHg
血氧: {patient.spo2}%
体温: {patient.temp}°C

【初步诊断】
可能疾病: {', '.join(diag['possible_diseases']) if diag['possible_diseases'] else '待查'}

【诊断依据】
{chr(10).join(['- ' + r for r in diag['reasoning']]) if diag['reasoning'] else '需进一步检查'}

【建议检查】
- 血常规、尿常规、粪常规
- 生化检查 (肝肾功能、电解质)
- 心电图
- 影像学检查 (根据症状选择)

==========================================
⚠️ 本报告仅供辅助参考，不替代医生判断
==========================================
"""
        return report


# 便捷函数
def quick_diagnose(**symptoms) -> Dict:
    """快速诊断"""
    patient = Patient(**symptoms)
    engine = EnhancedClinicalEngine()
    return engine.diagnose(patient)


def quick_triage(**vitals) -> Dict:
    """快速分诊"""
    patient = Patient(**vitals)
    engine = EnhancedClinicalEngine()
    return engine.triage(patient)


if __name__ == '__main__':
    engine = EnhancedClinicalEngine()
    
    # 测试
    patient = Patient(
        name="张三",
        age=65,
        gender=0,
        chief_complaint="胸痛伴呼吸困难2小时",
        chest_pain=1,
        dyspnea=1,
        fever=0,
        hr=120,
        sbp=160,
        spo2=92,
        temp=36.8,
        hypertension=1,
        diabetes=1,
        smoking=1
    )
    
    print("=" * 50)
    print("诊断结果:")
    print(engine.diagnose(patient))
    
    print("\n分诊结果:")
    print(engine.triage(patient))
    
    print("\n治疗方案 (冠心病):")
    print(engine.get_treatment_plan("冠心病"))
    
    print("\n临床报告:")
    print(engine.generate_report(patient))
