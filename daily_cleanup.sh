#!/bin/bash
# 每日文件整理脚本 - 23:59执行

DATE=$(date +%Y-%m-%d)
WORKSPACE="/Users/levi/.openclaw/workspace"

echo "=== $(date) 每日整理开始 ===" >> $WORKSPACE/memory/daily_cleanup.log

# 1. 查找并报告空目录
find $WORKSPACE -type d -empty 2>/dev/null >> $WORKSPACE/memory/daily_cleanup.log

# 2. Git状态
cd $WORKSPACE
git status --short >> $WORKSPACE/memory/daily_cleanup.log 2>&1

echo "=== 整理完成 ===" >> $WORKSPACE/memory/daily_cleanup.log
