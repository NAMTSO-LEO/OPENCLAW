#!/usr/bin/env python3
"""
SN SYNC Engine
性健康与需求同步引擎
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
import os


@dataclass
class UserProfile:
    """用户资料"""
    id: str = ""
    name: str = ""
    gender: int = 1  # 0=男, 1=女
    birthday: str = ""
    cycle_length: int = 28
    period_length: int = 5
    last_period_start: str = ""
    partner_name: str = ""
    created_at: str = ""


@dataclass
class PeriodRecord:
    """月经记录"""
    start_date: str
    end_date: str = ""
    flow: str = "中等"  # 少/中/多
    symptoms: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class IntimacyRecord:
    """亲密记录"""
    date: str
    time: str = ""
    intimacy_type: str = "性爱"  # 性爱/口交/手交/其他
    protection: str = "是"  # 是/否
    ejaculated: str = "是"  # 是/否
    lubricant: str = "否"
    notes: str = ""


@dataclass
class SymptomRecord:
    """症状记录"""
    date: str
    symptoms: List[str] = field(default_factory=list)
    mood: str = "正常"  # 很好/正常/低落
    energy: int = 5  # 1-10
    pain_level: int = 0  # 0-10
    notes: str = ""


class SNSyncEngine:
    """
    SN SYNC 引擎
    
    功能：
    - 月经周期计算与预测
    - 排卵期/易孕期计算
    - 症状分析
    - 亲密记录管理
    - 健康建议生成
    """
    
    def __init__(self, user_id: str = "default"):
        self.user_id = user_id
        self.profile = UserProfile()
        self.period_records: List[PeriodRecord] = []
        self.intimacy_records: List[IntimacyRecord] = []
        self.symptom_records: List[SymptomRecord] = []
        
    def set_profile(self, profile: UserProfile):
        """设置用户资料"""
        self.profile = profile
        
    def calculate_cycle(self, last_period_start: str = None) -> Dict:
        """计算月经周期"""
        if last_period_start is None:
            last_period_start = self.profile.last_period_start
            
        if not last_period_start:
            return {}
        
        try:
            last = datetime.strptime(last_period_start, "%Y-%m-%d")
        except:
            return {}
        
        cycle = self.profile.cycle_length
        period = self.profile.period_length
        
        # 排卵日 = 月经开始日 + 周期长度 - 14
        ovulation = last + timedelta(days=cycle - 14)
        
        # 排卵期 (易孕期) = 排卵日前5天到后4天
        fertile_start = ovulation - timedelta(days=5)
        fertile_end = ovulation + timedelta(days=4)
        
        # 下次月经
        next_period = last + timedelta(days=cycle)
        
        # 经期
        period_start = last
        period_end = last + timedelta(days=period - 1)
        
        # 安全期 (排除经期和易孕期)
        # 第一个安全期: 经期结束后到排卵前
        # 第二个安全期: 排卵后到下次月经前
        
        return {
            "last_period_start": last.strftime("%Y-%m-%d"),
            "last_period_end": period_end.strftime("%Y-%m-%d"),
            "next_period_start": next_period.strftime("%Y-%m-%d"),
            "ovulation_date": ovulation.strftime("%Y-%m-%d"),
            "fertile_start": fertile_start.strftime("%Y-%m-%d"),
            "fertile_end": fertile_end.strftime("%Y-%m-%d"),
            "cycle_length": cycle,
            "period_length": period,
            "days_since_period": (datetime.now() - last).days + 1,
            "days_until_next_period": (next_period - datetime.now()).days,
            "days_until_ovulation": (ovulation - datetime.now()).days
        }
    
    def get_date_type(self, date: str) -> str:
        """获取日期类型"""
        cycle = self.calculate_cycle()
        if not cycle:
            return "unknown"
        
        try:
            check_date = datetime.strptime(date, "%Y-%m-%d")
            last = datetime.strptime(cycle["last_period_start"], "%Y-%m-%d")
            fertile_start = datetime.strptime(cycle["fertile_start"], "%Y-%m-%d")
            fertile_end = datetime.strptime(cycle["fertile_end"], "%Y-%m-%d")
            period_end = datetime.strptime(cycle["last_period_end"], "%Y-%m-%d")
            
            # 经期
            if last <= check_date <= period_end:
                return "period"
            # 易孕期
            elif fertile_start <= check_date <= fertile_end:
                return "fertile"
            # 安全期
            else:
                return "safe"
                
        except:
            return "unknown"
    
    def get_pregnancy_chance(self) -> Dict:
        """怀孕几率分析"""
        cycle = self.calculate_cycle()
        if not cycle:
            return {"chance": "未知", "reason": "请设置月经信息"}
        
        days_since = cycle.get("days_since_period", 0)
        
        # 根据周期天数判断
        if 10 <= days_since <= 16:
            return {
                "chance": "高",
                "level": 5,
                "reason": "当前处于易孕期(排卵期附近)"
            }
        elif days_since <= 5:
            return {
                "chance": "低",
                "level": 1,
                "reason": "当前处于月经期"
            }
        elif 17 <= days_since <= 21:
            return {
                "chance": "中",
                "level": 3,
                "reason": "排卵期刚过，仍有少量怀孕可能"
            }
        else:
            return {
                "chance": "低",
                "level": 2,
                "reason": "处于安全期，怀孕可能性较低"
            }
    
    def analyze_symptoms(self, symptoms: List[str]) -> Dict:
        """症状分析"""
        insights = []
        recommendations = []
        
        symptom_analysis = {
            "腹痛": {
                "insight": "可能与子宫收缩或激素变化有关",
                "recommend": "热敷腹部，避免受凉"
            },
            "疲劳": {
                "insight": "激素变化或贫血可能导致",
                "recommend": "保证充足睡眠，补充铁质"
            },
            "头痛": {
                "insight": "可能是经前综合征或偏头痛",
                "recommend": "休息，可服用止痛药"
            },
            "情绪波动": {
                "insight": "激素波动影响情绪",
                "recommend": "保持心情愉悦，适当运动"
            },
            "腹胀": {
                "insight": "激素导致水钠潴留",
                "recommend": "减少盐分摄入"
            },
            "乳房胀痛": {
                "insight": "雌激素水平升高",
                "recommend": "穿舒适内衣"
            },
            "恶心": {
                "insight": "可能与激素变化或怀孕有关",
                "recommend": "少食多餐"
            },
            "腰痛": {
                "insight": "子宫收缩或姿势问题",
                "recommend": "热敷，适当运动"
            }
        }
        
        for symptom in symptoms:
            if symptom in symptom_analysis:
                insights.append(symptom_analysis[symptom]["insight"])
                recommendations.append(symptom_analysis[symptom]["recommend"])
        
        return {
            "symptoms": symptoms,
            "insights": insights,
            "recommendations": recommendations
        }
    
    def get_cycle_phase_info(self) -> Dict:
        """获取周期阶段信息"""
        cycle = self.calculate_cycle()
        if not cycle:
            return {}
        
        days_since = cycle.get("days_since_period", 0)
        
        # 周期阶段
        if days_since <= 5:
            return {
                "phase": "月经期",
                "icon": "🩸",
                "description": "子宫内膜脱落，发生月经",
                "tips": [
                    "注意保暖，避免受凉",
                    "充足睡眠，避免熬夜",
                    "饮食清淡，补充铁质",
                    "适度运动如散步"
                ],
                "recommend_exercise": "轻度运动",
                "recommend_food": "红枣、猪肝、瘦肉"
            }
        elif days_since <= 13:
            return {
                "phase": "卵泡期",
                "icon": "🌸",
                "description": "雌激素升高，卵泡发育",
                "tips": [
                    "身体恢复期",
                    "适合运动健身",
                    "保持规律作息",
                    "补充蛋白质和维生素"
                ],
                "recommend_exercise": "健身运动",
                "recommend_food": "鸡蛋、牛奶、水果"
            }
        elif days_since <= 16:
            return {
                "phase": "排卵期",
                "icon": "🫧",
                "description": "排卵日，易受孕",
                "tips": [
                    "💚 如有备孕计划可开始",
                    "注意休息",
                    "保持心情愉悦",
                    "可进行基础体温监测"
                ],
                "recommend_exercise": "适度运动",
                "recommend_food": "富含叶酸食物"
            }
        else:
            return {
                "phase": "黄体期",
                "icon": "🍂",
                "description": "孕激素升高，可能出现经前综合征",
                "tips": [
                    "可能出现情绪波动",
                    "减少盐分咖啡因",
                    "适当运动缓解压力",
                    "保证充足睡眠"
                ],
                "recommend_exercise": "瑜伽、冥想",
                "recommend_food": "蔬菜、水果、全谷物"
            }
    
    def add_period_record(self, record: PeriodRecord):
        """添加月经记录"""
        self.period_records.append(record)
        # 更新最后月经开始日期
        self.profile.last_period_start = record.start_date
        
    def add_intimacy_record(self, record: IntimacyRecord):
        """添加亲密记录"""
        self.intimacy_records.append(record)
        
    def add_symptom_record(self, record: SymptomRecord):
        """添加症状记录"""
        self.symptom_records.append(record)
    
    def get_statistics(self) -> Dict:
        """获取统计数据"""
        if not self.period_records:
            return {
                "avg_cycle": self.profile.cycle_length,
                "avg_period": self.profile.period_length,
                "total_records": 0
            }
        
        # 计算平均周期
        if len(self.period_records) >= 2:
            cycles = []
            for i in range(1, len(self.period_records)):
                try:
                    prev = datetime.strptime(self.period_records[i-1].start_date, "%Y-%m-%d")
                    curr = datetime.strptime(self.period_records[i].start_date, "%Y-%m-%d")
                    cycles.append((curr - prev).days)
                except:
                    pass
            avg_cycle = sum(cycles) / len(cycles) if cycles else self.profile.cycle_length
        else:
            avg_cycle = self.profile.cycle_length
        
        return {
            "avg_cycle": round(avg_cycle, 1),
            "avg_period": self.profile.period_length,
            "total_periods": len(self.period_records),
            "total_intimacy": len(self.intimacy_records),
            "last_period": self.period_records[-1].start_date if self.period_records else None
        }
    
    def generate_health_report(self) -> str:
        """生成健康报告"""
        cycle = self.calculate_cycle()
        phase = self.get_cycle_phase_info()
        stats = self.get_statistics()
        chance = self.get_pregnancy_chance()
        
        report = f"""
================================================================================
                        SN SYNC 健康报告
================================================================================
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}

【基本信息】
- 周期长度: {stats['avg_cycle']}天
- 经期长度: {stats['avg_period']}天
- 月经记录: {stats['total_periods']}次
- 亲密记录: {stats['total_intimacy']}次

【当前状态】
- 周期阶段: {phase.get('phase', '未知')}
- 距下次月经: {cycle.get('days_until_next_period', '?')}天
- 距排卵日: {cycle.get('days_until_ovulation', '?')}天
- 怀孕几率: {chance['chance']} ({chance['reason']})

【阶段建议】
{chr(10).join(['- ' + t for t in phase.get('tips', [])])}

================================================================================
                              提示
================================================================================
- 本报告仅供参考，不能替代专业医疗建议
- 如有不适，请及时就医
- 建议定期进行妇科检查

================================================================================
"""
        return report


def quick_cycle(last_period: str, cycle: int = 28) -> Dict:
    """快速周期计算"""
    engine = SNSyncEngine()
    engine.profile.cycle_length = cycle
    return engine.calculate_cycle(last_period)


if __name__ == '__main__':
    # 测试
    engine = SNSyncEngine()
    engine.profile.cycle_length = 28
    engine.profile.period_length = 5
    engine.profile.last_period_start = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
    
    print("=== 周期计算 ===")
    print(engine.calculate_cycle())
    
    print("\n=== 怀孕几率 ===")
    print(engine.get_pregnancy_chance())
    
    print("\n=== 周期阶段 ===")
    print(engine.get_cycle_phase_info())
    
    print("\n=== 健康报告 ===")
    print(engine.generate_health_report())
