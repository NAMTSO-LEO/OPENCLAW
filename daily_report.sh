#!/bin/bash
# 每日报告生成脚本 - 7:00执行

DATE=$(date +%Y-%m-%d)
YESTERDAY=$(date -j -v-1d +%Y-%m-%d)
WORKSPACE="/Users/levi/.openclaw/workspace"
REPORT="$WORKSPACE/memory/Daily_Report_${DATE}.md"

echo "# 每日Workspace报告" > $REPORT
echo "" >> $REPORT
echo "**日期**: $DATE" >> $REPORT
echo "**时间**: 7:00 AM" >> $REPORT
echo "" >> $REPORT

echo "## 📊 文件统计" >> $REPORT
echo "" >> $REPORT

echo "### 总览" >> $REPORT
TOTAL_MD=$(find $WORKSPACE -name "*.md" 2>/dev/null | wc -l)
TOTAL_DIRS=$(find $WORKSPACE -maxdepth 1 -type d 2>/dev/null | wc -l)
echo "- Markdown文件: $TOTAL_MD" >> $REPORT
echo "- 项目文件夹: $TOTAL_DIRS" >> $REPORT
echo "" >> $REPORT

echo "### 空目录 (昨日新增)" >> $REPORT
EMPTY=$(find $WORKSPACE -type d -empty 2>/dev/null | wc -l)
echo "- 空目录数: $EMPTY" >> $REPORT
if [ $EMPTY -gt 0 ]; then
    find $WORKSPACE -type d -empty 2>/dev/null | head -10 >> $REPORT
fi
echo "" >> $REPORT

echo "## 📁 活跃项目" >> $REPORT
echo "" >> $REPORT
for dir in "Acromegaly_GKS_Study" "珠海中科先进技术研究院" "AI_Drug_Dev_Livzon" "Li_Zhuan"; do
    if [ -d "$WORKSPACE/$dir" ]; then
        FILES=$(find "$WORKSPACE/$dir" -name "*.md" 2>/dev/null | wc -l)
        echo "- $dir: $FILES 文件" >> $REPORT
    fi
done
echo "" >> $REPORT

echo "## 🔧 Git状态" >> $REPORT
echo "" >> $REPORT
cd $WORKSPACE
CHANGES=$(git status --short 2>/dev/null | wc -l)
echo "- 未同步更改: $CHANGES" >> $REPORT
if [ $CHANGES -gt 0 ]; then
    git status --short 2>/dev/null | head -10 >> $REPORT
fi
echo "" >> $REPORT

echo "## ✅ 清理状态" >> $REPORT
echo "" >> $REPORT
echo "- 每日自动整理: 已启用 (23:59)" >> $REPORT
echo "- 报告生成: 已完成" >> $REPORT
echo "" >> $REPORT

echo "---" >> $REPORT
echo "*报告生成于 $(date)*" >> $REPORT

echo "✅ 每日报告已生成: $REPORT"
