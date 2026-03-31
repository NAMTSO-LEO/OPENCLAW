"""
Tag Analysis Tool - 标签分析工具
用于分析视频标签数据
"""

import json
from collections import defaultdict

# 标签数据
TAGS_DATA = [
    {"name": "Anal", "count": 387499, "category": "activity"},
    {"name": "Blowjob", "count": 298237, "category": "activity"},
    {"name": "Big Cock", "count": 233474, "category": "body_part"},
    {"name": "Bareback", "count": 230695, "category": "style"},
    {"name": "Cumshot", "count": 218795, "category": "activity"},
    {"name": "Amateur", "count": 216163, "category": "style"},
    {"name": "Twinks", "count": 154655, "category": "demographic"},
    {"name": "Masturbation", "count": 130413, "category": "activity"},
    {"name": "Muscle", "count": 127084, "category": "body_type"},
    {"name": "Gay Sex", "count": 124949, "category": "activity"},
    {"name": "Hunks", "count": 115950, "category": "body_type"},
    {"name": "Tattoo", "count": 94076, "category": "appearance"},
    {"name": "Hardcore", "count": 86866, "category": "style"},
    {"name": "Solo", "count": 83472, "category": "content_type"},
    {"name": "Gay", "count": 81132, "category": "general"},
    {"name": "Asian", "count": 79564, "category": "ethnicity"},
    {"name": "Threesome", "count": 55118, "category": "content_type"},
    {"name": "Daddy", "count": 52919, "category": "demographic"},
    {"name": "Interracial", "count": 49649, "category": "style"},
    {"name": "Twink", "count": 47829, "category": "demographic"},
    {"name": "Pornstars", "count": 41812, "category": "performer"},
    {"name": "Fetish", "count": 41163, "category": "style"},
    {"name": "Big Dick", "count": 40517, "category": "body_part"},
    {"name": "Ebony", "count": 34867, "category": "ethnicity"},
    {"name": "Outdoors", "count": 32674, "category": "setting"},
    {"name": "Webcam", "count": 31835, "category": "source"},
    {"name": "Group Sex", "count": 29044, "category": "content_type"},
    {"name": "Body Builders", "count": 27506, "category": "body_type"},
    {"name": "Hairy", "count": 27374, "category": "appearance"},
    {"name": "Black", "count": 27273, "category": "ethnicity"},
    {"name": "Mature", "count": 26526, "category": "age"},
    {"name": "Domination", "count": 26375, "category": "style"},
    {"name": "Bears", "count": 22974, "category": "body_type"},
    {"name": "Bisexual", "count": 21216, "category": "orientation"},
    {"name": "Gangbang", "count": 18320, "category": "activity"},
    {"name": "Creampie", "count": 18143, "category": "activity"},
    {"name": "Dildo", "count": 17888, "category": "toy"},
    {"name": "First Time", "count": 14486, "category": "style"},
    {"name": "Bondage", "count": 13282, "category": "style"},
    {"name": "POV", "count": 12875, "category": "style"},
    {"name": "Boyfriend", "count": 12678, "category": "relationship"},
    {"name": "Uniform", "count": 12370, "category": "appearance"},
    {"name": "BDSM", "count": 12183, "category": "style"},
    {"name": "Brazilian", "count": 10831, "category": "ethnicity"},
    {"name": "Japanese", "count": 8006, "category": "ethnicity"},
    {"name": "College", "count": 7402, "category": "setting"},
    {"name": "Fisting", "count": 7022, "category": "activity"},
    {"name": "Massage", "count": 15221, "category": "activity"},
    {"name": "Office", "count": 5032, "category": "setting"},
    {"name": "Shower", "count": 3141, "category": "setting"},
]

def get_top_tags(n=10):
    """获取Top N标签"""
    sorted_tags = sorted(TAGS_DATA, key=lambda x: x["count"], reverse=True)
    return sorted_tags[:n]

def get_tags_by_category(category):
    """按分类获取标签"""
    return [t for t in TAGS_DATA if t["category"] == category]

def get_category_stats():
    """分类统计"""
    stats = defaultdict(int)
    for tag in TAGS_DATA:
        stats[tag["category"]] += 1
    return dict(stats)

def search_tags(keyword):
    """搜索标签"""
    keyword = keyword.lower()
    return [t for t in TAGS_DATA if keyword in t["name"].lower()]

def get_related_tags(tag_name, n=5):
    """获取相关标签（同类别）"""
    tag = next((t for t in TAGS_DATA if t["name"] == tag_name), None)
    if not tag:
        return []
    category = tag["category"]
    same_category = [t for t in TAGS_DATA if t["category"] == category and t["name"] != tag_name]
    return sorted(same_category, key=lambda x: x["count"], reverse=True)[:n]

if __name__ == "__main__":
    print("=== Top 10 Tags ===")
    for i, tag in enumerate(get_top_tags(10), 1):
        print(f"{i}. {tag['name']}: {tag['count']:,}")
    
    print("\n=== Category Stats ===")
    for cat, count in get_category_stats().items():
        print(f"{cat}: {count}")
    
    print("\n=== Search 'Asian' ===")
    for tag in search_tags("Asian"):
        print(f"- {tag['name']} ({tag['count']:,})")
