"""
心力衰竭诊治引擎
Heart Failure Decision Engine
Evidence Engine - Common Diseases Module
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class HFStage(Enum):
    """心衰分期"""
    A = "A期（风险期）"
    B = "B期（前期）"
    C = "C期（症状期）"
    D = "D期（晚期）"


class HFType(Enum):
    """心衰类型"""
    HFrEF = "射血分数降低的心衰"
    HFmrEF = "射血分数中间值的心衰"
    HFpEF = "射血分数保留的心衰"
    ACUTE = "急性失代偿性心衰"


class HFSeverity(Enum):
    """心衰严重程度"""
    STABLE = "稳定"
    DECOMPENSATED = "失代偿"
    SEVERE = "重度"


@dataclass
class HeartFailureData:
    """心衰患者数据"""
    # 基本信息
    age: int
    gender: str
    
    # 症状
    dyspnea: bool = False
    orthopnea: bool = False
    pnd: bool = False  # 阵发性夜间呼吸困难
    fatigue: bool = False
    edema: bool = False
    abdominal_distension: bool = False
    
    # 生命体征
    hr: int = 0
    sbp: int = 0
    dbp: int = 0
    rr: int = 0
    spo2: int = 100
    
    # 体征
    jugular_venous: bool = False  # 颈静脉怒张
    rales: bool = False  # 肺部啰音
    s3_gallop: bool = False  # 第三心音
    hepatomegaly: bool = False  # 肝肿大
    peripheral_edema: bool = False  # 外周水肿
    
    # 实验室
    bnpp: str = "normal"  # normal/elevated
    troponin: str = "normal"
    creatinine: str = "normal"
    sodium: str = "normal"
    
    # 影像
    echo_ef: int = 0  # 射血分数
    
    # 病史
    cad: bool = False
    hypertension: bool = False
    diabetes: bool = False
    valvular: bool = False
    cardiomyopathy: bool = False
    afib: bool = False


class HeartFailureEngine:
    """心力衰竭诊治引擎"""
    
    def __init__(self):
        self.severity = HFSeverity.STABLE
        self.hf_type = HFType.HFrEF
        self.recommendations = []
        self.evidence = []
    
    def analyze(self, data: HeartFailureData) -> Dict:
        """分析心衰患者"""
        
        # 1. 严重程度评估
        self.assess_severity(data)
        
        # 2. 类型判断
        self.determine_type(data)
        
        # 3. 检查建议
        self.recommend_workup(data)
        
        # 4. 治疗建议
        self.recommend_treatment(data)
        
        # 5. 证据
        self.get_evidence()
        
        return self.get_result()
    
    def assess_severity(self, data: HeartFailureData):
        """评估严重程度"""
        
        # 急性失代偿指标
        decompensation_signs = []
        
        if data.sbp < 90:
            decompensation_signs.append("低血压")
        if data.spo2 < 90:
            decompensation_signs.append("低氧")
        if data.jugular_venous:
            decompensation_signs.append("颈静脉怒张")
        if data.rales:
            decompensation_signs.append("肺部啰音")
        if data.s3_gallop:
            decompensation_signs.append("第三心音")
        if data.bnpp == "elevated":
            decompensation_signs.append("BNP显著升高")
        if data.troponin == "elevated":
            decompensation_signs.append("心肌损伤")
        
        if len(decompensation_signs) >= 2:
            self.severity = HFSeverity.DECOMPENSATED
        elif len(decompensation_signs) == 1:
            self.severity = HFSeverity.DECOMPENSATED
        else:
            self.severity = HFSeverity.STABLE
    
    def determine_type(self, data: HeartFailureData):
        """判断心衰类型"""
        
        ef = data.echo_ef
        
        if ef >= 50:
            self.hf_type = HFType.HFpEF
        elif ef >= 40:
            self.hf_type = HFType.HFmrEF
        else:
            self.hf_type = HFType.HFrEF
    
    def recommend_workup(self, data: HeartFailureData):
        """检查建议"""
        
        workups = [
            {"name": "心电图", "priority": 1, "reason": "评估心律、心肌缺血"},
            {"name": "胸片", "priority": 1, "reason": "评估肺水肿、胸腔积液"},
            {"name": "BNP/NT-proBNP", "priority": 1, "reason": "心衰诊断和严重程度"},
            {"name": "肌钙蛋白", "priority": 1, "reason": "排除心肌损伤"},
            {"name": "肾功能、电解质", "priority": 1, "reason": "评估肾功能和电解质"},
            {"name": "血常规", "priority": 1, "reason": "排除感染/贫血"},
            {"name": "肝功能", "priority": 2, "reason": "评估淤血性肝损伤"},
            {"name": "超声心动图", "priority": 1, "reason": "评估心脏结构和功能"},
        ]
        
        if self.severity == HFSeverity.DECOMPENSATED:
            workups.extend([
                {"name": "动脉血气", "priority": 1, "reason": "评估氧合和酸碱平衡"},
                {"name": "Swan-Ganz", "priority": 2, "reason": "血流动力学监测（重症）"},
            ])
        
        self.recommendations = workups
    
    def recommend_treatment(self, data: HeartFailureData):
        """治疗建议"""
        
        treatments = []
        
        if self.severity == HFSeverity.DECOMPENSATED:
            # 急性失代偿治疗
            treatments.extend([
                {"category": "一般治疗", "content": "半卧位休息", "priority": 1},
                {"category": "氧疗", "content": "吸氧（SpO2<94%）", "priority": 1},
                {"category": "利尿剂", "content": "静脉呋塞米", "priority": 1},
                {"category": "血管扩张剂", "content": "硝酸甘油/硝普钠（血压允许）", "priority": 1},
                {"category": "正性肌力", "content": "多巴胺/多巴酚丁胺（低灌注时）", "priority": 2},
                {"category": "抗凝", "content": "如合并房颤需抗凝", "priority": 2},
            ])
        else:
            # 慢性稳定性治疗
            treatments.extend([
                {"category": "利尿剂", "content": "呋塞米口服", "priority": 1},
                {"category": "ACEI/ARB/ARNI", "content": "沙库比曲缬沙坦/培哚普利", "priority": 1},
                {"category": "β受体阻滞剂", "content": "美托洛尔/卡维地洛", "priority": 1},
                {"category": "醛固酮拮抗剂", "content": "螺内酯", "priority": 1},
                {"category": "SGLT2抑制剂", "content": "恩格列净/达格列净", "priority": 1},
                {"category": "生活方式", "content": "限盐、限水、戒烟", "priority": 2},
            ])
        
        # 根据类型调整
        if self.hf_type == HFType.HFpEF:
            treatments.extend([
                {"category": "治疗", "content": "控制血压（<130/80mmHg）", "priority": 1},
                {"category": "治疗", "content": "治疗合并症（房颤、糖尿病）", "priority": 1},
            ])
        
        self.treatments = treatments
    
    def get_evidence(self):
        """获取证据"""
        
        self.evidence = [
            {"title": "ESC Heart Failure Guidelines 2021", "key": "HFrEF推荐ARNI、β阻滞剂、MRA、SGLT2i四联治疗"},
            {"title": "ACC/AHA HF Guidelines 2022", "key": "GDMT四联疗法降低死亡率和住院率"},
            {"title": "BNP/NT-proBNP Clinical Practice", "key": "心衰诊断和预后评估"},
        ]
    
    def get_result(self) -> Dict:
        """获取结果"""
        
        return {
            "severity": self.severity.value,
            "hf_type": self.hf_type.value,
            "workup": self.recommendations,
            "treatments": self.treatments,
            "evidence": self.evidence,
            "clinical_judgment": f"心力衰竭，{self.severity.value}性，{self.hf_type.value}"
        }


def create_hf_from_dict(d: dict) -> HeartFailureData:
    """从字典创建心衰数据"""
    return HeartFailureData(
        age=d.get("age", 0),
        gender=d.get("gender", "male"),
        dyspnea=d.get("dyspnea", False),
        orthopnea=d.get("orthopnea", False),
        pnd=d.get("pnd", False),
        fatigue=d.get("fatigue", False),
        edema=d.get("edema", False),
        abdominal_distension=d.get("abdominal_distension", False),
        hr=d.get("hr", 0),
        sbp=d.get("sbp", 0),
        dbp=d.get("dbp", 0),
        rr=d.get("rr", 0),
        spo2=d.get("spo2", 100),
        jugular_venous=d.get("jugular_venous", False),
        rales=d.get("rales", False),
        s3_gallop=d.get("s3_gallop", False),
        hepatomegaly=d.get("hepatomegaly", False),
        peripheral_edema=d.get("peripheral_edema", False),
        bnpp=d.get("bnpp", "normal"),
        troponin=d.get("troponin", "normal"),
        creatinine=d.get("creatinine", "normal"),
        sodium=d.get("sodium", "normal"),
        echo_ef=d.get("echo_ef", 0),
        cad=d.get("cad", False),
        hypertension=d.get("hypertension", False),
        diabetes=d.get("diabetes", False),
        valvular=d.get("valvular", False),
        cardiomyopathy=d.get("cardiomyopathy", False),
        afib=d.get("afib", False)
    )
