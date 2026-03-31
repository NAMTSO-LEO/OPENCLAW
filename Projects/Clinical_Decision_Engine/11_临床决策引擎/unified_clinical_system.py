#!/usr/bin/env python3
"""
统一临床决策系统
整合 临床辅助引擎 + 临床决策引擎
"""

from typing import Dict, List
from clinical_assistant_engine import ClinicalAssistantEngine, Patient as AssistPatient
from clinical_decision_engine import ClinicalDecisionEngine, Patient as DecisionPatient

# 统一患者类
class UnifiedPatient:
    """统一患者数据模型"""
    
    def __init__(self, **kwargs):
        self.age = kwargs.get('age', 0)
        self.gender = kwargs.get('gender', 0)
        self.name = kwargs.get('name', '')
        
        # 症状
        self.fever = kwargs.get('fever', 0)
        self.cough = kwargs.get('cough', 0)
        self.sputum = kwargs.get('sputum', 0)
        self.chest_pain = kwargs.get('chest_pain', 0)
        self.dyspnea = kwargs.get('dyspnea', 0)
        self.headache = kwargs.get('headache', 0)
        self.dizziness = kwargs.get('dizziness', 0)
        self.nausea = kwargs.get('nausea', 0)
        self.vomiting = kwargs.get('vomiting', 0)
        self.abdominal_pain = kwargs.get('abdominal_pain', 0)
        self.diarrhea = kwargs.get('diarrhea', 0)
        self.fatigue = kwargs.get('fatigue', 0)
        self.weight_loss = kwargs.get('weight_loss', 0)
        self.night_sweat = kwargs.get('night_sweat', 0)
        self.joint_pain = kwargs.get('joint_pain', 0)
        self.back_pain = kwargs.get('back_pain', 0)
        self.hematuria = kwargs.get('hematuria', 0)
        self.edema = kwargs.get('edema', 0)
        self.palpitations = kwargs.get('palpitations', 0)
        
        # 体征
        self.hr = kwargs.get('hr', 80)
        self.sbp = kwargs.get('sbp', 120)
        self.dbp = kwargs.get('dbp', 80)
        self.spo2 = kwargs.get('spo2', 98)
        self.temp = kwargs.get('temp', 36.5)
        self.rr = kwargs.get('rr', 16)
        
        # 既往史
        self.hypertension = kwargs.get('hypertension', 0)
        self.diabetes = kwargs.get('diabetes', 0)
        self.coronary_heart_disease = kwargs.get('coronary_heart_disease', 0)
        self.heart_failure = kwargs.get('heart_failure', 0)
        self.stroke = kwargs.get('stroke', 0)
        self.copd = kwargs.get('copd', 0)
        self.asthma = kwargs.get('asthma', 0)
        self.kidney_disease = kwargs.get('kidney_disease', 0)
        self.liver_disease = kwargs.get('liver_disease', 0)
        self.cancer = kwargs.get('cancer', 0)
        self.tb = kwargs.get('tb', 0)
        
        # 个人史
        self.smoking = kwargs.get('smoking', 0)
        self.alcohol = kwargs.get('alcohol', 0)
        
        # 主诉
        self.chief_complaint = kwargs.get('chief_complaint', '')
        
        # 用药/过敏
        self.medications = kwargs.get('medications', [])
        self.allergies = kwargs.get('allergies', [])
    
    def to_assist_patient(self) -> AssistPatient:
        """转换为辅助引擎患者"""
        return AssistPatient(
            age=self.age,
            gender=self.gender,
            fever=self.fever,
            cough=self.cough,
            sputum=self.sputum,
            chest_pain=self.chest_pain,
            dyspnea=self.dyspnea,
            headache=self.headache,
            dizziness=self.dizziness,
            nausea=self.nausea,
            vomiting=self.vomiting,
            abdominal_pain=self.abdominal_pain,
            diarrhea=self.diarrhea,
            fatigue=self.fatigue,
            weight_loss=self.weight_loss,
            night_sweat=self.night_sweat,
            joint_pain=self.joint_pain,
            back_pain=self.back_pain,
            urinary_symptoms=self.hematuria,
            hematuria=self.hematuria,
            edema=self.edema,
            palpitations=self.palpitations,
            hr=self.hr,
            sbp=self.sbp,
            dbp=self.dbp,
            spo2=self.spo2,
            temp=self.temp,
            hypertension=self.hypertension,
            diabetes=self.diabetes,
            coronary_heart_disease=self.coronary_heart_disease,
            heart_failure=self.heart_failure,
            stroke=self.stroke,
            copd=self.copd,
            asthma=self.asthma,
            kidney_disease=self.kidney_disease,
            liver_disease=self.liver_disease,
            cancer=self.cancer,
            tb=self.tb,
            smoking=self.smoking,
            alcohol=self.alcohol,
            allergies=self.allergies
        )
    
    def to_decision_patient(self) -> DecisionPatient:
        """转换为决策引擎患者"""
        return DecisionPatient(
            age=self.age,
            gender=self.gender,
            chief_complaint=self.chief_complaint,
            fever=self.fever,
            cough=self.cough,
            chest_pain=self.chest_pain,
            dyspnea=self.dyspnea,
            headache=self.headache,
            abdominal_pain=self.abdominal_pain,
            vomiting=self.vomiting,
            hr=self.hr,
            sbp=self.sbp,
            dbp=self.dbp,
            spo2=self.spo2,
            temp=self.temp,
            rr=self.rr,
            hypertension=self.hypertension,
            diabetes=self.diabetes,
            coronary_heart_disease=self.coronary_heart_disease,
            heart_failure=self.heart_failure,
            stroke=self.stroke,
            copd=self.copd,
            kidney_disease=self.kidney_disease,
            medications=self.medications,
            allergies=self.allergies
        )


class UnifiedClinicalSystem:
    """
    统一临床决策系统
    
    整合两个引擎:
    - ClinicalAssistantEngine: 临床辅助 (诊断、鉴别诊断、检查建议)
    - ClinicalDecisionEngine: 临床决策 (分诊、治疗方案、ML预测)
    """
    
    def __init__(self):
        self.assistant = ClinicalAssistantEngine()
        self.decision = ClinicalDecisionEngine()
        
    def full_assessment(self, patient: UnifiedPatient) -> Dict:
        """完整临床评估"""
        # 辅助引擎分析
        assist_patient = patient.to_assist_patient()
        symptom_analysis = self.assistant.analyze_symptoms(assist_patient)
        differential = self.assistant.differential_diagnosis(assist_patient)
        exam_suggestions = self.assistant.suggest_examinations(assist_patient)
        warnings = self.assistant.get_warnings(assist_patient)
        
        # 决策引擎分析
        decision_patient = patient.to_decision_patient()
        triage = self.decision.triage(decision_patient)
        
        return {
            # 辅助系统
            "symptom_analysis": symptom_analysis,
            "differential_diagnosis": differential,
            "exam_suggestions": exam_suggestions,
            "clinical_warnings": warnings,
            
            # 决策系统
            "triage": triage,
            
            # 综合建议
            "summary": self._generate_summary(triage, differential, warnings)
        }
    
    def _generate_summary(self, triage: Dict, differential: Dict, warnings: List[str]) -> str:
        """生成摘要"""
        summary = f"""
【急诊分诊】{triage['icon']} {triage['level']} ({triage['description']})

【可能疾病】{', '.join(differential['possible_diseases'][:5])}

【注意事项】
"""
        for w in warnings[:3]:
            summary += f"- {w}\n"
        
        summary += f"\n【建议行动】{triage['action']}"
        
        return summary


# 便捷函数
def assess_patient(**kwargs) -> Dict:
    """快速评估患者"""
    patient = UnifiedPatient(**kwargs)
    system = UnifiedClinicalSystem()
    return system.full_assessment(patient)


if __name__ == '__main__':
    # 测试
    patient = UnifiedPatient(
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
    
    system = UnifiedClinicalSystem()
    
    print("=" * 60)
    print("完整临床评估")
    print("=" * 60)
    
    result = system.full_assessment(patient)
    
    print("\n【分诊结果】")
    print(f"等级: {result['triage']['level']}")
    print(f"评分: {result['triage']['score']}")
    print(f"行动: {result['triage']['action']}")
    
    print("\n【鉴别诊断】")
    for disease in result['differential_diagnosis']['possible_diseases'][:5]:
        print(f"  - {disease}")
    
    print("\n【检查建议】")
    for exam in result['exam_suggestions']['suggested_exams'][:5]:
        print(f"  - {exam}")
    
    print("\n【注意事项】")
    for w in result['clinical_warnings'][:3]:
        print(f"  - {w}")
