#!/usr/bin/env python3
"""
临床辅助引擎 (Clinical Assistant Engine)
功能：智能诊断、鉴别诊断、症状分析、临床建议
基于规则的知识库系统
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import os

@dataclass
class Patient:
    """患者信息"""
    id: str = ""
    name: str = ""
    age: int = 0
    gender: int = 0  # 0=男, 1=女
    
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
    hematuria: int = 0
    edema: int = 0
    palpitations: int = 0
    
    # 体征
    hr: int = 80
    sbp: int = 120
    dbp: int = 80
    rr: int = 16
    temp: float = 36.5
    spo2: float = 98
    
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
    
    # 个人史
    smoking: int = 0
    alcohol: int = 0
    
    # 过敏史
    allergies: List[str] = field(default_factory=list)


class ClinicalAssistantEngine:
    """
    临床辅助引擎
    
    主要功能：
    - 症状分析
    - 鉴别诊断建议
    - 检查项目建议
    - 临床注意事项提醒
    """
    
    def __init__(self):
        self._init_symptom_rules()
        self._init_diagnosis_rules()
        self._init_exam_suggestions()
        
    def _init_symptom_rules(self):
        """初始化症状分析规则"""
        self.symptom_analysis = {
            "发热": {
                "可能的病因": ["感染", "炎症", "肿瘤", "免疫性疾病"],
                "分析要点": ["热型", "持续时间", "伴随症状"],
                "提醒": "持续发热>3天需及时就医"
            },
            "胸痛": {
                "可能的病因": ["冠心病", "肺栓塞", "主动脉夹层", "肺炎", "胸膜炎"],
                "分析要点": ["疼痛性质", "部位", "放射", "诱发因素"],
                "提醒": "剧烈胸痛可能致命，需立即就医"
            },
            "呼吸困难": {
                "可能的病因": ["心衰", "肺炎", "慢阻肺", "哮喘", "肺栓塞"],
                "分析要点": ["起病急缓", "活动后加重", "伴随症状"],
                "提醒": "急性呼吸困难是急诊信号"
            },
            "腹痛": {
                "可能的病因": ["阑尾炎", "胆囊炎", "胰腺炎", "肠梗阻", "妇科急症"],
                "分析要点": ["部位", "性质", "转移性", "伴随症状"],
                "提醒": "急腹症需紧急评估"
            },
            "头痛": {
                "可能的病因": ["偏头痛", "紧张性头痛", "脑膜炎", "脑肿瘤", "高血压"],
                "分析要点": ["部位", "性质", "持续时间", "伴随症状"],
                "提醒": "突发剧烈头痛需排除脑部急症"
            }
        }
        
    def _init_diagnosis_rules(self):
        """初始化诊断规则库"""
        # 症状组合 -> 可能疾病 (按概率排序)
        self.diagnosis_rules = {
            # 心血管
            ("胸痛", "心悸"): ["冠心病", "心律失常", "心肌炎"],
            ("胸痛", "呼吸困难"): ["冠心病", "肺栓塞", "心衰"],
            ("胸痛", "高血压"): ["冠心病", "主动脉夹层"],
            ("胸痛", "出汗"): ["急性心肌梗死"],
            ("心悸", "头晕"): ["心律失常", "贫血"],
            ("晕厥", "心悸"): ["心律失常", "颈动脉窦综合征"],
            
            # 呼吸
            ("咳嗽", "发热"): ["肺炎", "支气管炎", "肺结核", "新冠"],
            ("咳嗽", "咳痰"): ["支气管炎", "肺炎", "慢阻肺"],
            ("咳嗽", "咯血"): ["肺结核", "支气管扩张", "肺癌"],
            ("呼吸困难", "喘息"): ["哮喘", "慢阻肺", "心衰"],
            ("呼吸困难", "胸痛"): ["肺栓塞", "气胸", "心衰"],
            
            # 消化
            ("腹痛", "恶心"): ["胃肠炎", "阑尾炎", "胰腺炎"],
            ("腹痛", "发热"): ["阑尾炎", "胆囊炎", "腹膜炎"],
            ("腹痛", "血便"): ["肠癌", "炎症性肠病"],
            ("腹痛", "黄疸"): ["肝炎", "胆结石", "胰腺癌"],
            ("呕血", "黑便"): ["消化性溃疡", "食管胃底静脉曲张"],
            ("腹泻", "发热"): ["胃肠炎", "炎症性肠病"],
            
            # 神经
            ("头痛", "发热"): ["脑膜炎", "脑炎", "偏头痛"],
            ("头痛", "呕吐"): ["脑膜炎", "脑肿瘤", "偏头痛"],
            ("意识障碍", "发热"): ["脑膜炎", "脑炎"],
            ("肢体无力", "言语不清"): ["脑卒中"],
            
            # 泌尿
            ("尿频", "尿急", "尿痛"): ["泌尿道感染", "前列腺炎"],
            ("腰痛", "发热"): ["肾盂肾炎", "泌尿系结石"],
            ("血尿", "蛋白尿"): ["肾炎", "泌尿系结石"],
            
            # 内分泌
            ("多饮", "多尿"): ["糖尿病", "尿崩症"],
            ("体重下降", "心悸"): ["甲亢", "糖尿病", "恶性肿瘤"],
            ("怕热", "多汗"): ["甲亢"],
            ("怕冷", "乏力"): ["甲减"],
            
            # 其他
            ("乏力", "苍白"): ["贫血", "慢性病"],
            ("发热", "皮疹"): ["麻疹", "风疹", "药物热"],
            ("关节痛", "发热"): ["类风湿", "系统性红斑狼疮"],
            ("淋巴结肿大", "发热"): ["淋巴瘤", "结核", "HIV"],
        }
        
        # 既往史相关疾病
        self.risk_factors = {
            "高血压": ["冠心病", "脑卒中", "肾功能不全", "心衰"],
            "糖尿病": ["冠心病", "脑卒中", "肾病", "视网膜病变"],
            "吸烟": ["肺癌", "慢阻肺", "心血管疾病"],
            "冠心病": ["心肌梗死", "心衰", "心律失常"],
            "慢阻肺": ["呼吸衰竭", "肺心病"],
        }
        
    def _init_exam_suggestions(self):
        """初始化检查建议"""
        self.exam_suggestions = {
            "发热": ["血常规", "CRP", "血培养", "尿常规", "胸片"],
            "胸痛": ["心电图", "心肌酶谱", "心脏超声", "冠脉CTA"],
            "呼吸困难": ["胸片", "血气分析", "D-二聚体", "心脏超声"],
            "腹痛": ["腹部超声", "腹部CT", "血常规", "淀粉酶"],
            "头痛": ["头颅CT/MRI", "脑电图", "血压"],
            "乏力": ["血常规", "肝肾功能", "电解质", "甲状腺功能"],
            "黄疸": ["肝功能", "腹部超声", "肝炎病毒"],
            "水肿": ["肝肾功能", "尿常规", "心脏超声", "甲状腺功能"],
        }
        
        # 通用检查
        self.general_exams = [
            "血常规", "尿常规", "粪常规", 
            "肝肾功能", "电解质", "血糖", "血脂",
            "心电图", "胸部X线"
        ]
    
    # ==================== 核心功能 ====================
    
    def analyze_symptoms(self, patient: Patient) -> Dict:
        """症状分析"""
        symptoms = []
        
        # 收集症状
        symptom_map = {
            "fever": "发热", "chills": "寒战", "cough": "咳嗽",
            "sputum": "咳痰", "chest_pain": "胸痛", "dyspnea": "呼吸困难",
            "headache": "头痛", "dizziness": "头晕", "nausea": "恶心",
            "vomiting": "呕吐", "abdominal_pain": "腹痛", "diarrhea": "腹泻",
            "fatigue": "乏力", "weight_loss": "体重下降", "night_sweat": "盗汗",
            "joint_pain": "关节痛", "back_pain": "腰痛", "urinary_symptoms": "排尿不适",
            "hematuria": "血尿", "edema": "水肿", "palpitations": "心悸"
        }
        
        for attr, name in symptom_map.items():
            if getattr(patient, attr, 0):
                symptoms.append(name)
        
        # 分析每个主要症状
        analysis = {}
        for s in symptoms:
            if s in self.symptom_analysis:
                analysis[s] = self.symptom_analysis[s]
        
        return {
            "symptoms": symptoms,
            "analysis": analysis,
            "count": len(symptoms)
        }
    
    def differential_diagnosis(self, patient: Patient) -> Dict:
        """鉴别诊断"""
        symptoms = []
        symptom_map = {
            "fever": "发热", "chills": "寒战", "cough": "咳嗽",
            "sputum": "咳痰", "chest_pain": "胸痛", "dyspnea": "呼吸困难",
            "headache": "头痛", "dizziness": "头晕", "nausea": "恶心",
            "vomiting": "呕吐", "abdominal_pain": "腹痛", "diarrhea": "腹泻",
            "fatigue": "乏力", "weight_loss": "体重下降", "night_sweat": "盗汗",
            "joint_pain": "关节痛", "back_pain": "腰痛", "urinary_symptoms": "排尿不适",
            "hematuria": "血尿", "edema": "水肿", "palpitations": "心悸"
        }
        
        for attr, name in symptom_map.items():
            if getattr(patient, attr, 0):
                symptoms.append(name)
        
        # 规则匹配
        possible_diseases = set()
        
        # 组合症状匹配
        for symptom_tuple, diseases in self.diagnosis_rules.items():
            match = sum(1 for s in symptoms if s in symptom_tuple)
            if match >= min(2, len(symptom_tuple)):
                possible_diseases.update(diseases)
        
        # 既往史加权
        if patient.hypertension:
            possible_diseases.update(self.risk_factors.get("高血压", []))
        if patient.diabetes:
            possible_diseases.update(self.risk_factors.get("糖尿病", []))
        if patient.smoking:
            possible_diseases.update(self.risk_factors.get("吸烟", []))
        if patient.coronary_heart_disease:
            possible_diseases.update(self.risk_factors.get("冠心病", []))
        if patient.copd:
            possible_diseases.update(self.risk_factors.get("慢阻肺", []))
        
        # 年龄相关
        if patient.age > 50:
            possible_diseases.add("肿瘤筛查")
        
        # 按系统分类
        system_classification = {
            "心血管系统": ["冠心病", "心律失常", "心肌炎", "心衰", "心肌梗死"],
            "呼吸系统": ["肺炎", "支气管炎", "肺结核", "慢阻肺", "哮喘", "肺癌", "肺栓塞"],
            "消化系统": ["胃肠炎", "阑尾炎", "胰腺炎", "胆囊炎", "肝炎", "消化性溃疡", "肠癌"],
            "神经系统": ["脑卒中", "脑膜炎", "偏头痛", "脑肿瘤"],
            "内分泌系统": ["甲亢", "甲减", "糖尿病"],
            "泌尿系统": ["泌尿道感染", "肾炎", "肾盂肾炎"],
            "其他": ["肿瘤筛查"]
        }
        
        classified = {}
        for disease in possible_diseases:
            for system, diseases in system_classification.items():
                if disease in diseases:
                    if system not in classified:
                        classified[system] = []
                    classified[system].append(disease)
        
        return {
            "symptoms": symptoms,
            "possible_diseases": list(possible_diseases),
            "by_system": classified,
            "count": len(possible_diseases)
        }
    
    def suggest_examinations(self, patient: Patient) -> Dict:
        """检查建议"""
        symptoms = []
        symptom_map = {
            "fever": "发热", "chest_pain": "胸痛", "dyspnea": "呼吸困难",
            "abdominal_pain": "腹痛", "headache": "头痛", "fatigue": "乏力",
            "weight_loss": "体重下降", "night_sweat": "盗汗", "edema": "水肿"
        }
        
        for attr, name in symptom_map.items():
            if getattr(patient, attr, 0):
                symptoms.append(name)
        
        # 症状相关检查
        suggested_exams = []
        for s in symptoms:
            if s in self.exam_suggestions:
                suggested_exams.extend(self.exam_suggestions[s])
        
        # 去重但保持顺序
        seen = set()
        unique_exams = []
        for exam in suggested_exams:
            if exam not in seen:
                seen.add(exam)
                unique_exams.append(exam)
        
        # 添加通用检查
        for exam in self.general_exams:
            if exam not in seen:
                unique_exams.append(exam)
        
        # 根据既往史添加
        if patient.hypertension:
            unique_exams.extend(["动态血压监测", "超声心动图"])
        if patient.diabetes:
            unique_exams.extend(["糖化血红蛋白", "眼底检查"])
        if patient.age > 50:
            unique_exams.extend(["肿瘤标志物", "腹部超声"])
        
        return {
            "suggested_exams": unique_exams,
            "priority": "急诊" if self._is_urgent(patient) else "择期",
            "reasons": self._get_exam_reasons(symptoms)
        }
    
    def _is_urgent(self, patient: Patient) -> bool:
        """判断是否紧急"""
        urgent_symptoms = ["胸痛", "呼吸困难", "剧烈腹痛", "意识障碍", "大出血"]
        symptoms = []
        
        symptom_map = {
            "chest_pain": "胸痛", "dyspnea": "呼吸困难",
            "abdominal_pain": "腹痛"
        }
        
        for attr, name in symptom_map.items():
            if getattr(patient, attr, 0):
                symptoms.append(name)
        
        # 生命体征异常
        if patient.sbp < 90 or patient.sbp > 200:
            return True
        if patient.hr > 120 or patient.hr < 50:
            return True
        if patient.spo2 < 90:
            return True
        if patient.temp > 39 or patient.temp < 35:
            return True
        
        return any(s in urgent_symptoms for s in symptoms)
    
    def _get_exam_reasons(self, symptoms: List[str]) -> List[str]:
        """检查原因"""
        reasons = []
        if "发热" in symptoms:
            reasons.append("发热需排查感染")
        if "胸痛" in symptoms:
            reasons.append("胸痛需排除心血管急症")
        if "呼吸困难" in symptoms:
            reasons.append("呼吸困难需评估心肺功能")
        if "腹痛" in symptoms:
            reasons.append("腹痛需排查急腹症")
        if "乏力" in symptoms:
            reasons.append("乏力需排查贫血、甲亢等")
        
        return reasons
    
    def get_warnings(self, patient: Patient) -> List[str]:
        """获取临床注意事项"""
        warnings = []
        
        # 症状相关警告
        if patient.chest_pain and patient.hypertension:
            warnings.append("高血压+胸痛：警惕急性冠脉综合征")
        if patient.chest_pain and patient.dyspnea:
            warnings.append("胸痛+呼吸困难：警惕肺栓塞、主动脉夹层")
        if patient.fever and patient.headache:
            warnings.append("发热+头痛：警惕脑膜炎、脑炎")
        if patient.fever and patient.abdominal_pain:
            warnings.append("发热+腹痛：警惕阑尾炎、胆囊炎等急腹症")
        if patient.dyspnea and patient.spo2 < 94:
            warnings.append("低氧血症：需要氧疗评估")
        
        # 生命体征警告
        if patient.sbp < 90:
            warnings.append("低血压：警惕休克")
        if patient.sbp > 180:
            warnings.append("重度高血压：警惕高血压急症")
        if patient.hr > 130:
            warnings.append("心动过速：需要排查原因")
        if patient.hr < 50:
            warnings.append("心动过缓：注意排除病窦综合征")
        if patient.temp > 40:
            warnings.append("高热：警惕热射病、严重感染")
        
        # 既往史警告
        if patient.hypertension and patient.diabetes:
            warnings.append("高血压+糖尿病：强化心血管风险管理")
        if patient.smoking and patient.cough:
            warnings.append("吸烟+咳嗽：建议肺部CT排查")
        
        return warnings
    
    def generate_assessment(self, patient: Patient) -> Dict:
        """综合评估报告"""
        symptom_analysis = self.analyze_symptoms(patient)
        diff_diag = self.differential_diagnosis(patient)
        exams = self.suggest_examinations(patient)
        warnings = self.get_warnings(patient)
        
        return {
            "patient": {
                "age": patient.age,
                "gender": "女" if patient.gender else "男"
            },
            "symptom_analysis": symptom_analysis,
            "differential_diagnosis": diff_diagnosis,
            "suggested_exams": exams,
            "warnings": warnings,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


def quick_assist(**symptoms) -> Dict:
    """快速辅助诊断"""
    patient = Patient(**symptoms)
    engine = ClinicalAssistantEngine()
    return engine.differential_diagnosis(patient)


if __name__ == '__main__':
    # 测试
    engine = ClinicalAssistantEngine()
    
    patient = Patient(
        age=65,
        gender=0,
        chest_pain=1,
        dyspnea=1,
        fever=0,
        hypertension=1,
        diabetes=1,
        smoking=1
    )
    
    print("=" * 50)
    print("症状分析:")
    print(engine.analyze_symptoms(patient))
    
    print("\n鉴别诊断:")
    print(engine.differential_diagnosis(patient))
    
    print("\n检查建议:")
    print(engine.suggest_examinations(patient))
    
    print("\n注意事项:")
    print(engine.get_warnings(patient))
