#!/bin/bash
# 科研材料整理脚本
# 为珠海中科先进院项目整理科研成果PDF

# 源目录
SOURCE_DIR="/Users/levi/.openclaw/media/inbound"

# 目标目录
TARGET_DIR="/Users/levi/.openclaw/workspace/珠海中科先进技术研究院/材料准备/科研成果"

# 创建分类目录
mkdir -p "$TARGET_DIR/01_GammaKnife_放射外科"
mkdir -p "$TARGET_DIR/02_垂体瘤_综合治疗"
mkdir -p "$TARGET_DIR/03_肢端肥大症_Acromegaly"
mkdir -p "$TARGET_DIR/04_机器学习_ML"
mkdir -p "$TARGET_DIR/05_其他临床研究"
mkdir -p "$TARGET_DIR/00_索引"

echo "=== 开始整理科研材料 ==="

# Gamma Knife / 放射外科相关
cp "$SOURCE_DIR"/Stereotactic_radiosurgery_for_acromegaly_*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null
cp "$SOURCE_DIR"/Gamma_Knife*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null
cp "$SOURCE_DIR"/fractionated_radiotherapy*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null
cp "$SOURCE_DIR"/GKRS*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null
cp "$SOURCE_DIR"/low_dose_gamma_knife*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null
cp "$SOURCE_DIR"/Kissing_cartoid*.pdf "$TARGET_DIR/01_GammaKnife_放射外科/" 2>/dev/null

# 垂体瘤相关
cp "$SOURCE_DIR"/pituitary*.pdf "$TARGET_DIR/02_垂体瘤_综合治疗/" 2>/dev/null
cp "$SOURCE_DIR"/hypopituitarism*.pdf "$TARGET_DIR/02_垂体瘤_综合治疗/" 2>/dev/null
cp "$SOURCE_DIR"/postoperative_gamma_knife*.pdf "$TARGET_DIR/02_垂体瘤_综合治疗/" 2>/dev/null

# 肢端肥大症
cp "$SOURCE_DIR"/acromegaly*.pdf "$TARGET_DIR/03_肢端肥大症_Acromegaly/" 2>/dev/null
cp "$SOURCE_DIR"/Endoscopic_Transsphenoidal*.pdf "$TARGET_DIR/03_肢端肥大症_Acromegaly/" 2>/dev/null
cp "$SOURCE_DIR"/remission*.pdf "$TARGET_DIR/03_肢端肥大症_Acromegaly/" 2>/dev/null

# 机器学习
cp "$SOURCE_DIR"/machine_learning*.pdf "$TARGET_DIR/04_机器学习_ML/" 2>/dev/null
cp "$SOURCE_DIR"/supervised_learning*.pdf "$TARGET_DIR/04_机器学习_ML/" 2>/dev/null

# 生成索引文件
echo "# 科研成果索引" > "$TARGET_DIR/00_索引/文献索引.md"
echo "" >> "$TARGET_DIR/00_索引/文献索引.md"
echo "## 1. GammaKnife放射外科" >> "$TARGET_DIR/00_索引/文献索引.md"
ls "$TARGET_DIR/01_GammaKnife_放射外科/" >> "$TARGET_DIR/00_索引/文献索引.md" 2>/dev/null
echo "" >> "$TARGET_DIR/00_索引/文献索引.md"
echo "## 2. 垂体瘤综合治疗" >> "$TARGET_DIR/00_索引/文献索引.md"
ls "$TARGET_DIR/02_垂体瘤_综合治疗/" >> "$TARGET_DIR/00_索引/文献索引.md" 2>/dev/null
echo "" >> "$TARGET_DIR/00_索引/文献索引.md"
echo "## 3. 肢端肥大症" >> "$TARGET_DIR/00_索引/文献索引.md"
ls "$TARGET_DIR/03_肢端肥大症_Acromegaly/" >> "$TARGET_DIR/00_索引/文献索引.md" 2>/dev/null
echo "" >> "$TARGET_DIR/00_索引/文献索引.md"
echo "## 4. 机器学习" >> "$TARGET_DIR/00_索引/文献索引.md"
ls "$TARGET_DIR/04_机器学习_ML/" >> "$TARGET_DIR/00_索引/文献索引.md" 2>/dev/null

echo "=== 整理完成 ==="
echo "文件已复制到: $TARGET_DIR"
echo "索引位置: $TARGET_DIR/00_索引/文献索引.md"
