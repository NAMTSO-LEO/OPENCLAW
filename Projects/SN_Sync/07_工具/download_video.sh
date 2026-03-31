#!/bin/bash
# yt-dlp 视频下载脚本
# 使用方法: ./download.sh "视频URL"

# 添加到PATH
export PATH="$PATH:/Users/levi/Library/Python/3.9/bin"

# 创建下载目录
mkdir -p ~/Downloads/Video_素材

# 默认参数
QUALITY="bestvideo[height>=720]+bestaudio/best"
OUTPUT_DIR="~/Downloads/Video_素材"

echo "========================================="
echo "   Gay视频素材下载工具"
echo "========================================="
echo ""
echo "用法:"
echo "  ./download.sh <URL>"
echo ""
echo "示例:"
echo "  ./download.sh https://www.youtube.com/watch?v=xxx"
echo "  ./download.sh https://www.pornhub.com/viewvideo.php?viewkey=xxx"
echo ""

# 如果提供了URL则下载
if [ -n "$1" ]; then
    echo "正在下载: $1"
    echo "保存位置: $OUTPUT_DIR"
    echo ""
    
    yt-dlp \
        -f "$QUALITY" \
        -o "$OUTPUT_DIR/%(title)s.%(ext)s" \
        --merge-output-format mp4 \
        --no-playlist \
        "$1"
    
    echo ""
    echo "下载完成!"
else
    echo "请提供视频URL"
fi
