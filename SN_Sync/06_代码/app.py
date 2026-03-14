#!/usr/bin/env python3
"""
SN SYNC - Sexual Health & Needs Sync App
性健康与需求同步应用

功能：
- 月经周期跟踪
- 排卵期预测
- 症状记录
- 亲密行为记录
- 生育建议
- 健康分析
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List, Optional
import calendar

# 页面配置
st.set_page_config(
    page_title="SN SYNC - 性健康同步",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS样式
st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .stButton>button {
        background-color: #e91e63;
        color: white;
        border-radius: 20px;
    }
    .header {
        background: linear-gradient(135deg, #e91e63, #9c27b0);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .period-day {
        background-color: #e91e63;
        color: white;
        border-radius: 50%;
        padding: 10px;
        text-align: center;
    }
    .fertile-day {
        background-color: #4caf50;
        color: white;
        border-radius: 50%;
        padding: 10px;
        text-align: center;
    }
    .safe-day {
        background-color: #2196f3;
        color: white;
        border-radius: 50%;
        padding: 10px;
        text-align: center;
    }
    .today {
        border: 3px solid #e91e63;
    }
    .metric-card {
        background: linear-gradient(135deg, #fce4ec, #f8bbd9);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .insight-box {
        background: linear-gradient(135deg, #fff3e0, #ffe0b2);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ff9800;
    }
    .warning-box {
        background: #ffebee;
        border-left: 4px solid #f44336;
        padding: 10px;
        border-radius: 5px;
    }
    .success-box {
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)


@dataclass
class UserProfile:
    """用户资料"""
    name: str = ""
    birthday: str = ""
    gender: int = 1  # 0=男, 1=女
    cycle_length: int = 28  # 月经周期
    period_length: int = 5  # 经期长度
    last_period_start: str = ""  # 上次月经开始日期
    partner_name: str = ""


class SNSyncEngine:
    """SN SYNC 引擎"""
    
    def __init__(self):
        self.profile = None
        self.records = []
        
    def calculate_cycle(self, last_period: str, cycle_length: int = 28) -> Dict:
        """计算月经周期"""
        try:
            last = datetime.strptime(last_period, "%Y-%m-%d")
        except:
            return {}
        
        # 排卵日 = 月经开始日 + 周期长度 - 14
        ovulation = last + timedelta(days=cycle_length - 14)
        
        # 排卵期 = 排卵日前5天到后4天
        fertile_start = ovulation - timedelta(days=5)
        fertile_end = ovulation + timedelta(days=4)
        
        # 经期
        period_start = last
        period_end = last + timedelta(days=cycle_length - 1)
        
        return {
            "last_period": last.strftime("%Y-%m-%d"),
            "next_period": (last + timedelta(days=cycle_length)).strftime("%Y-%m-%d"),
            "ovulation": ovulation.strftime("%Y-%m-%d"),
            "fertile_start": fertile_start.strftime("%Y-%m-%d"),
            "fertile_end": fertile_end.strftime("%Y-%m-%d"),
            "cycle_length": cycle_length
        }
    
    def get_calendar(self, year: int, month: int, cycle_info: Dict) -> List[List[Dict]]:
        """获取日历"""
        cal = calendar.monthcalendar(year, month)
        calendar_data = []
        
        for week in cal:
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append({"day": "", "type": "empty"})
                else:
                    date = datetime(year, month, day).strftime("%Y-%m-%d")
                    
                    # 判断日期类型
                    if cycle_info:
                        last = datetime.strptime(cycle_info["last_period"], "%Y-%m-%d")
                        fertile_start = datetime.strptime(cycle_info["fertile_start"], "%Y-%m-%d")
                        fertile_end = datetime.strptime(cycle_info["fertile_end"], "%Y-%m-%d")
                        current = datetime(year, month, day)
                        
                        # 经期 (假设5天)
                        period_end = last + timedelta(days=4)
                        if last <= current <= period_end:
                            day_type = "period"
                        # 排卵期
                        elif fertile_start <= current <= fertile_end:
                            day_type = "fertile"
                        # 安全期
                        else:
                            day_type = "safe"
                    else:
                        day_type = "unknown"
                    
                    week_data.append({
                        "day": day,
                        "type": day_type,
                        "date": date
                    })
            calendar_data.append(week_data)
        
        return calendar_data
    
    def analyze_health(self, symptoms: List[str], cycle_day: int) -> Dict:
        """健康分析"""
        insights = []
        recommendations = []
        
        # 经期相关
        if cycle_day <= 5:
            insights.append("🌸 您目前处于月经期，注意休息保暖")
            recommendations.append("多喝热水，避免剧烈运动")
        elif 6 <= cycle_day <= 14:
            insights.append("🌱 卵泡期，身体机能逐渐恢复")
            recommendations.append("适合运动健身，保持良好作息")
        elif 15 <= cycle_day <= 21:
            insights.append("🫧 排卵期，身体机能最佳")
            if "易孕期" in symptoms:
                insights.append("💚 当前为易孕期，如有备孕计划可开始")
        elif cycle_day > 21:
            insights.append("🍂 黄体期，可能出现经前综合征")
            if "情绪波动" in symptoms or "腹胀" in symptoms:
                recommendations.append("注意情绪调节，减少盐分摄入")
        
        # 症状分析
        if "腹痛" in symptoms:
            insights.append("⚠️ 腹痛可能与激素变化有关")
        if "疲劳" in symptoms:
            insights.append("💤 注意休息，保证充足睡眠")
        if "头痛" in symptoms:
            insights.append("🤕 可尝试热敷缓解")
        
        return {
            "insights": insights,
            "recommendations": recommendations,
            "cycle_phase": self._get_cycle_phase(cycle_day)
        }
    
    def _get_cycle_phase(self, day: int) -> str:
        """获取周期阶段"""
        if day <= 5:
            return "月经期"
        elif day <= 14:
            return "卵泡期"
        elif day <= 21:
            return "排卵期"
        else:
            return "黄体期"


def main():
    st.markdown("""
    <div class="header">
        <h1>💕 SN SYNC</h1>
        <h3>性健康与需求同步</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # 初始化引擎
    engine = SNSyncEngine()
    
    # 侧边栏
    st.sidebar.title("💕 SN SYNC")
    st.sidebar.markdown("---")
    
    mode = st.sidebar.radio(
        "功能菜单",
        ["📅 日历", "📊 统计", "💑 亲密记录", "👤 个人设置", "💡 健康建议"]
    )
    
    # 获取当前月份
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    
    # 模拟用户数据 (实际应用中应该从数据库读取)
    default_cycle = {
        "last_period": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
        "cycle_length": 28,
        "next_period": (today + timedelta(days=18)).strftime("%Y-%m-%d"),
        "ovulation": (today + timedelta(days=4)).strftime("%Y-%m-%d"),
        "fertile_start": (today - timedelta(days=1)).strftime("%Y-%m-%d"),
        "fertile_end": (today + timedelta(days=9)).strftime("%Y-%m-%d")
    }
    
    # ========== 日历 ==========
    if mode == "📅 日历":
        st.header("📅 健康日历")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # 月份选择
            col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
            with col_nav1:
                st.button("◀", key="prev_month")
            with col_nav2:
                st.markdown(f"### {current_year}年 {current_month}月")
            with col_nav3:
                st.button("▶", key="next_month")
            
            # 日历显示
            calendar_data = engine.get_calendar(current_year, current_month, default_cycle)
            
            # 表头
            cols = st.columns(7)
            days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
            for i, d in enumerate(days):
                cols[i].markdown(f"**{d}**")
            
            # 日历内容
            for week in calendar_data:
                cols = st.columns(7)
                for day_data in week:
                    if day_data["day"]:
                        day = day_data["day"]
                        date_type = day_data["type"]
                        
                        # 样式
                        if date_type == "period":
                            style = "period-day"
                        elif date_type == "fertile":
                            style = "fertile-day"
                        elif date_type == "safe":
                            style = "safe-day"
                        else:
                            style = ""
                        
                        # 今日标记
                        is_today = (day == today.day)
                        border = "today" if is_today else ""
                        
                        cols[calendar_data.index(week)].markdown(f"""
                        <div class="{style} {border}" style="margin: 5px 0; padding: 8px;">
                            {day}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        cols[calendar_data.index(week)].write("")
        
        with col2:
            # 今日状态
            st.markdown("### 💫 今日状态")
            
            # 计算周期天数
            last_period = datetime.strptime(default_cycle["last_period"], "%Y-%m-%d")
            days_since = (today - last_period).days + 1
            cycle_day = days_since % 28
            if cycle_day == 0:
                cycle_day = 28
            
            st.metric("周期第几天", f"第{cycle_day}天")
            
            # 阶段
            if cycle_day <= 5:
                phase = "🩸 月经期"
                color = "#e91e63"
            elif cycle_day <= 14:
                phase = "🌸 卵泡期"
                color = "#4caf50"
            elif cycle_day <= 21:
                phase = "🫧 排卵期"
                color = "#ff9800"
            else:
                phase = "🍂 黄体期"
                color = "#9c27b0"
            
            st.markdown(f"**阶段:** {phase}")
            
            # 怀孕几率
            if 10 <= cycle_day <= 16:
                chance = "⭐⭐⭐⭐⭐ 高"
                st.success(f"怀孕几率: {chance}")
            elif cycle_day <= 5:
                chance = "⭐ 低 (月经期)"
                st.info(f"怀孕几率: {chance}")
            else:
                chance = "⭐⭐ 中低"
                st.info(f"怀孕几率: {chance}")
            
            # 下次月经
            next_period = datetime.strptime(default_cycle["next_period"], "%Y-%m-%d")
            days_until = (next_period - today).days
            
            st.metric("距下次月经", f"{days_until}天")
            
            # 排卵日
            ovulation = datetime.strptime(default_cycle["ovulation"], "%Y-%m-%d")
            days_to_ovulation = (ovulation - today).days
            
            if days_to_ovulation > 0:
                st.metric("距排卵日", f"{days_to_ovulation}天")
            else:
                st.warning("排卵日已过")
        
        # 图例
        st.markdown("---")
        st.markdown("""
        **图例:**
        🩸 红色 = 月经期
        🟢 绿色 = 排卵期(易孕期)
        🔵 蓝色 = 安全期
        🔴 边框 = 今日
        """)
    
    # ========== 统计 ==========
    elif mode == "📊 统计":
        st.header("📊 健康统计")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h2>28</h2>
                <p>平均周期(天)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h2>5</h2>
                <p>平均经期(天)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h2>14</h2>
                <p>平均排卵日</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-card">
                <h2>6</h2>
                <p>易孕期(天)</p>
            </div>
            """, unsafe_allow_html=True)
        
        # 周期趋势
        st.subheader("📈 周期趋势")
        
        # 模拟数据
        days = list(range(1, 29))
        hormone_levels = []
        for d in days:
            if d <= 5:  # 月经期
                hormone_levels.append(20 + d * 5)
            elif d <= 14:  # 卵泡期
                hormone_levels.append(45 + (d-5) * 8)
            elif d <= 21:  # 排卵期
                hormone_levels.append(100 - (d-14) * 10)
            else:  # 黄体期
                hormone_levels.append(50 - (d-21) * 4)
        
        chart_data = pd.DataFrame({
            "周期天": days,
            "激素水平": hormone_levels
        })
        
        st.line_chart(chart_data.set_index("周期天"))
        
        # 症状记录
        st.subheader("📝 最近症状")
        
        symptoms_col1, symptoms_col2 = st.columns(2)
        
        with symptoms_col1:
            st.checkbox("腹痛")
            st.checkbox("疲劳")
            st.checkbox("头痛")
        
        with symptoms_col2:
            st.checkbox("情绪波动")
            st.checkbox("腹胀")
            st.checkbox("乳房胀痛")
    
    # ========== 亲密记录 ==========
    elif mode == "💑 亲密记录":
        st.header("💑 亲密记录")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 记录")
            
            date = st.date_input("日期", today)
            time = st.time_input("时间", datetime.now().time())
            
            st.selectbox("亲密类型", ["性爱", "口交", "手交", "其他"])
            
            st.checkbox("使用避孕套")
            st.checkbox("射精体内")
            st.checkbox("使用润滑剂")
            
            st.text_area("备注", placeholder="可以添加备注...")
            
            if st.button("保存记录", type="primary"):
                st.success("记录已保存! 💕")
        
        with col2:
            st.subheader("📅 历史记录")
            
            # 模拟记录
            records = [
                {"date": "2026-03-10", "type": "性爱", "protection": "是", "note": ""},
                {"date": "2026-03-08", "type": "性爱", "protection": "否", "note": "排卵期"},
                {"date": "2026-03-05", "type": "口交", "protection": "N/A", "note": ""},
                {"date": "2026-03-01", "type": "性爱", "protection": "是", "note": ""},
            ]
            
            for r in records:
                st.markdown(f"""
                <div class="card">
                    <p><strong>{r['date']}</strong> - {r['type']}</p>
                    <p>避孕: {r['protection']} | 备注: {r['note']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # ========== 个人设置 ==========
    elif mode == "👤 个人设置":
        st.header("👤 个人设置")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("基本信息")
            
            name = st.text_input("昵称", "用户")
            birthday = st.date_input("生日", datetime(1995, 1, 1))
            gender = st.radio("性别", ["女", "男", "其他"])
            
            st.subheader("月经设置")
            cycle_length = st.slider("月经周期(天)", 21, 35, 28)
            period_length = st.slider("经期长度(天)", 3, 10, 5)
            last_period = st.date_input("上次月经开始日期", today - timedelta(days=10))
        
        with col2:
            st.subheader("伴侣信息")
            
            partner_name = st.text_input("伴侣昵称", "")
            partner_birthday = st.date_input("伴侣生日", datetime(1993, 1, 1))
            
            st.subheader("通知设置")
            st.checkbox("月经提醒")
            st.checkbox("排卵期提醒")
            st.checkbox("亲密记录提醒")
            
            st.subheader("数据管理")
            st.button("导出数据")
            st.button("清除数据", type="primary")
        
        if st.button("保存设置", type="primary"):
            st.success("设置已保存! 💕")
    
    # ========== 健康建议 ==========
    elif mode == "💡 健康建议":
        st.header("💡 健康建议")
        
        # 今日建议
        st.subheader("✨ 今日建议")
        
        # 周期阶段
        last_period = datetime.strptime(default_cycle["last_period"], "%Y-%m-%d")
        days_since = (today - last_period).days + 1
        cycle_day = days_since % 28
        if cycle_day == 0:
            cycle_day = 28
        
        # 根据阶段显示建议
        if cycle_day <= 5:
            st.markdown("""
            <div class="insight-box">
                <h4>🩸 月经期建议</h4>
                <ul>
                    <li>注意保暖，避免受凉</li>
                    <li>充足睡眠，避免熬夜</li>
                    <li>饮食清淡，减少辛辣</li>
                    <li>适度运动，如散步</li>
                    <li>补充铁质，如红枣、猪肝</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        elif cycle_day <= 14:
            st.markdown("""
            <div class="insight-box">
                <h4>🌸 卵泡期建议</h4>
                <ul>
                    <li>身体恢复期，适合运动健身</li>
                    <li>保持规律作息</li>
                    <li>补充蛋白质和维生素</li>
                    <li>皮肤状态较好，可进行美容</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        elif cycle_day <= 21:
            st.markdown("""
            <div class="insight-box">
                <h4>🫧 排卵期建议</h4>
                <ul>
                    <li>💚 易孕期，如有备孕计划可开始</li>
                    <li>注意休息，避免过度疲劳</li>
                    <li>保持心情愉悦</li>
                    <li>如有生育计划，建议同房</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div class="insight-box">
                <h4>🍂 黄体期建议</h4>
                <ul>
                    <li>可能出现经前综合征</li>
                    <li>注意情绪调节</li>
                    <li>减少盐分和咖啡因摄入</li>
                    <li>适当运动缓解压力</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # 避孕知识
        st.subheader("💚 避孕知识")
        
        with st.expander("避孕方法比较"):
            st.markdown("""
            | 方法 | 成功率 | 优点 | 缺点 |
            |------|--------|------|------|
            | 避孕套 | 85-98% | 防病避孕 | 可能破裂 |
            | 口服避孕药 | 99% | 调经避孕 | 需每天服用 |
            | 事后避孕药 | 72小时内95% | 紧急避孕 | 副作用大 |
            | 安全期 | 76-88% | 无药物 | 不稳定 |
            | 体外射精 | 78-96% | 无成本 | 需控制 |
            """)
        
        # 健康知识
        st.subheader("📚 健康知识")
        
        with st.expander("月经不调的原因"):
            st.markdown("""
            - 压力过大
            - 体重骤变
            - 运动过度
            - 多囊卵巢综合征
            - 甲状腺问题
            - 子宫内膜异位
            """)
        
        with st.expander("排卵期症状"):
            st.markdown("""
            - 基础体温升高
            - 宫颈黏液增多
            - 轻微腹痛
            - 性欲增强
            - 乳房胀痛
            """)
        
        # 警告
        st.subheader("⚠️ 注意事项")
        
        st.markdown("""
        <div class="warning-box">
            <ul>
                <li>如有异常出血、剧烈腹痛等症状，请及时就医</li>
                <li>本应用仅供参考，不能替代专业医疗建议</li>
                <li>建议定期进行妇科检查</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 页脚
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px;">
        <p>💕 SN SYNC v1.0 - 性健康同步应用</p>
        <p>您的隐私数据将严格保密</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
