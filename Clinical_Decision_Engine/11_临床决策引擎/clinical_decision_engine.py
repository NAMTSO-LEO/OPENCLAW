#!/usr/bin/env python3
"""
临床辅助决策引擎
Clinical Decision Support Engine
基于机器学习的疾病预测与临床决策辅助
"""

import pickle
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np

# 模型路径
MODEL_DIR = '/Users/levi/.openclaw/workspace/EvidenceEngine_MVP/model_training'

@dataclass
class PatientInfo:
    """患者信息"""
    age: int
    gender: int  # 0=男, 1=女
    # 症状
    fever: int = 0
    cough: int = 0
    chest_pain: int = 0
    headache: int = 0
    abdominal_pain: int = 0
    fatigue: int = 0
    dizziness: int = 0
    nausea: int = 0
    # 体征
    hr: int = 80  # 心率
    sbp: int = 120  # 收缩压
    dbp: int = 80  # 舒张压
    temp: float = 36.5  # 体温
    spo2: float = 98  # 血氧
    # 既往史
    hypertension: int = 0
    diabetes: int = 0
    heart_disease: int = 0
    smoking: int = 0
    # 实验室检查
    glucose: float = 100
    cholesterol: float = 200
    hemoglobin: float = 140

class ClinicalDecisionEngine:
    """临床决策引擎"""
    
    def __init__(self, model_dir: str = MODEL_DIR):
        self.model_dir = model_dir
        self.models = {}
        self._load_models()
        
    def _load_models(self):
        """加载所有模型"""
        model_files = [f for f in os.listdir(self.model_dir) if f.endswith('_model.pkl')]
        for mf in model_files:
            name = mf.replace('_model.pkl', '').replace('_', ' ')
            try:
                with open(os.path.join(self.model_dir, mf), 'rb') as f:
                    self.models[name] = pickle.load(f)
            except:
                pass
        print(f"已加载 {len(self.models)} 个疾病预测模型")
    
    def predict(self, disease_name: str, features: List[float]) -> Dict:
        """疾病预测"""
        if disease_name not in self.models:
            # 尝试模糊匹配
            for name in self.models:
                if disease_name.lower() in name.lower():
                    disease_name = name
                    break
        
        if disease_name not in self.models:
            return {'error': f'未找到模型: {disease_name}'}
        
        model_data = self.models[disease_name]
        model = model_data['model']
        scaler = model_data['scaler']
        features_list = model_data['features']
        
        try:
            X = scaler.transform([features])
            prob = model.predict_proba(X)[0]
            pred = model.predict(X)[0]
            
            return {
                'disease': disease_name,
                'prediction': int(pred),
                'probability': float(prob[1]) if len(prob) > 1 else float(prob[0]),
                'features_used': features_list
            }
        except Exception as e:
            return {'error': str(e)}
    
    def triage(self, patient: PatientInfo) -> Dict:
        """急诊分诊"""
        score = 0
        urgent = []
        
        # 生命体征评估
        if patient.sbp < 90 or patient.sbp > 200:
            score += 3
            urgent.append('血压异常')
        if patient.hr > 120:
            score += 2
            urgent.append('心动过速')
        if patient.hr < 50:
            score += 2
            urgent.append('心动过缓')
        if patient.spo2 < 90:
            score += 3
            urgent.append('低氧血症')
        if patient.temp > 39 or patient.temp < 35:
            score += 2
            urgent.append('发热/低体温')
            
        # 症状评估
        if patient.chest_pain:
            score += 2
            urgent.append('胸痛')
        if patient.headache:
            score += 1
        if patient.abdominal_pain:
            score += 1
        
        # 既往史
        if patient.hypertension:
            score += 1
        if patient.diabetes:
            score += 1
        
        # 分级
        if score >= 5:
            level = "一级 (危重)"
            color = "red"
        elif score >= 3:
            level = "二级 (急症)"
            color = "orange"
        elif score >= 1:
            level = "三级 (普通)"
            color = "yellow"
        else:
            level = "四级 (非急症)"
            color = "green"
        
        return {
            'triage_level': level,
            'score': score,
            'urgent_reasons': urgent,
            'color': color
        }
    
    def get_recommendations(self, disease: str, risk_level: str) -> Dict[str, List[str]]:
        """获取临床建议"""
        recommendations = {
            'workup': [],
            'treatment': [],
            'monitoring': [],
            'referral': []
        }
        
        disease_lower = disease.lower()
        
        # 心脏病相关
        if 'heart' in disease_lower or 'cardiac' in disease_lower or 'coronary' in disease_lower:
            recommendations['workup'] = ['心电图', '心肌酶谱', '心脏超声', '冠脉CTA']
            recommendations['treatment'] = ['硝酸甘油', 'β受体阻滞剂', '抗血小板药物']
            if risk_level == 'high':
                recommendations['referral'] = ['心内科急诊']
        
        # 糖尿病
        if 'diabetes' in disease_lower:
            recommendations['workup'] = ['空腹血糖', 'HbA1c', '糖耐量试验', '血脂']
            recommendations['treatment'] = ['二甲双胍', '胰岛素', '饮食控制']
            recommendations['monitoring'] = ['血糖监测', '眼底检查', '肾功能']
        
        # 脑卒中
        if 'stroke' in disease_lower or 'cerebral' in disease_lower:
            recommendations['workup'] = ['头颅CT/MRI', '脑血管造影', '心电图']
            recommendations['treatment'] = ['rt-PA溶栓', '抗血小板', '控制血压']
            recommendations['referral'] = ['神经内科急诊']
        
        # 肺炎
        if 'pneumonia' in disease_lower or 'lung' in disease_lower:
            recommendations['workup'] = ['胸片', '血常规', 'CRP', '痰培养']
            recommendations['treatment'] = ['抗生素', '祛痰药', '必要时吸氧']
        
        # 肝病
        if 'liver' in disease_lower or 'hepatic' in disease_lower or 'hepatitis' in disease_lower:
            recommendations['workup'] = ['肝功能', '乙肝五项', '腹部超声', '甲胎蛋白']
            recommendations['treatment'] = ['保肝药物', '抗病毒治疗', '戒酒']
        
        # 肾病
        if 'kidney' in disease_lower or 'renal' in disease_lower:
            recommendations['workup'] = ['肾功能', '尿常规', '肾脏超声']
            recommendations['treatment'] = ['控制血压', '优质低蛋白饮食', '利尿剂']
        
        # 肿瘤
        if 'cancer' in disease_lower or 'tumor' in disease_lower:
            recommendations['workup'] = ['肿瘤标志物', '影像学检查', '病理活检']
            recommendations['treatment'] = ['手术', '化疗', '放疗', '靶向治疗']
            recommendations['referral'] = ['肿瘤科']
        
        return recommendations


def quick_predict(disease: str, **features) -> Dict:
    """快速预测接口"""
    engine = ClinicalDecisionEngine()
    return engine.predict(disease, list(features.values()))


if __name__ == '__main__':
    # 测试
    engine = ClinicalDecisionEngine()
    
    # 测试分诊
    patient = PatientInfo(
        age=65,
        gender=0,
        chest_pain=1,
        hr=110,
        sbp=160,
        hypertension=1
    )
    
    print("急诊分诊测试:")
    print(engine.triage(patient))
    
    print("\n可用模型:")
    for name in sorted(engine.models.keys()):
        print(f"  - {name}")
