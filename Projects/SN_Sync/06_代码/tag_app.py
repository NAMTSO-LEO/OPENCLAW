"""
Tag Analysis Web App - 标签分析网页应用
"""

import streamlit as st
from tag_analyzer import TAGS_DATA, get_top_tags, get_tags_by_category, get_category_stats, search_tags, get_related_tags

st.set_page_config(page_title="Tag Analyzer", page_icon="📊")

st.title("📊 Tag Analysis Tool")
st.write("标签分析工具 - 热门标签统计与分类")

# 侧边栏
st.sidebar.header("功能菜单")
mode = st.sidebar.radio("选择功能", ["Top Tags", "分类浏览", "搜索", "相关标签"])

if mode == "Top Tags":
    st.header("🔥 Top 热门标签")
    
    n = st.slider("显示数量", 5, 50, 10)
    tags = get_top_tags(n)
    
    for i, tag in enumerate(tags, 1):
        st.write(f"**{i}. {tag['name']}** - {tag['count']:,} 次")
        st.progress(min(tag['count'] / 400000, 1.0))
    
    # 图表
    import pandas as pd
    df = pd.DataFrame(tags)
    st.bar_chart(df.set_index('name')['count'])

elif mode == "分类浏览":
    st.header("📂 标签分类")
    
    stats = get_category_stats()
    category = st.selectbox("选择分类", list(stats.keys()))
    
    tags = get_tags_by_category(category)
    st.write(f"**{category}** 分类共有 {len(tags)} 个标签:")
    
    for tag in sorted(tags, key=lambda x: x['count'], reverse=True):
        st.write(f"- {tag['name']}: {tag['count']:,}")

elif mode == "搜索":
    st.header("🔍 标签搜索")
    
    keyword = st.text_input("输入关键词")
    if keyword:
        results = search_tags(keyword)
        if results:
            st.write(f"找到 {len(results)} 个结果:")
            for tag in results:
                st.write(f"**{tag['name']}** - {tag['count']:,} ({tag['category']})")
        else:
            st.write("未找到结果")

elif mode == "相关标签":
    st.header("🔗 相关标签推荐")
    
    # 选择标签
    tag_names = [t['name'] for t in TAGS_DATA]
    selected = st.selectbox("选择一个标签", tag_names)
    
    if selected:
        related = get_related_tags(selected)
        st.write(f"与 **{selected}** 相关的标签:")
        for tag in related:
            st.write(f"- {tag['name']}: {tag['count']:,} ({tag['category']})")

# 统计信息
st.sidebar.markdown("---")
st.sidebar.write("**统计信息:**")
st.sidebar.write(f"- 总标签数: {len(TAGS_DATA)}")
st.sidebar.write(f"- 分类数: {len(get_category_stats())}")
