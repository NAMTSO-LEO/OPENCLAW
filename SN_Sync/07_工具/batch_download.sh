#!/bin/bash
# 批量下载脚本 - YouTube视频
# 使用方法: ./batch_download.sh

export PATH="$PATH:/Users/levi/Library/Python/3.9/bin"

# 创建下载目录
mkdir -p ~/Downloads/Video_素材/{muscle,twink,couple}

echo "========================================="
echo "   YouTube 视频批量下载"
echo "========================================="

# 亚洲肌肉男
muscle_ids=(
"fb1JlxvXKmY"
"gpF2bLjJcz0"
"DVhKYkdXSn8"
"m22uqC29xTs"
"R6E49rs01dI"
"vlltUiOwhsw"
"CDjHY-EnvDo"
"8Ul5vhDM_CY"
"W3K2_cZi39M"
"NVJ23PLb0dU"
"cGVKC63E7uw"
"ZpmRMWEiuXw"
)

# 亚洲鲜肉
twink_ids=(
"3-fMRJk_1N4"
"-1psP2GcI0M"
"Aqkok-Y8JxU"
"Qz6w0HlP5tA"
"8DVJMH4CpuA"
"K_rcshH1iFY"
"rm8uHoaJV6k"
"AnBaNqM1UVY"
"2DuhkVhRx6U"
)

# 亚洲情侣
couple_ids=(
"DEMQFNqSzfU"
"IupJh_nO10E"
"Ug8lT4SU7A8"
"HoM69OCHNZU"
"pVV1w66oCpk"
"3VDOUHmIK9w"
"9vLpd4ySHyQ"
)

# 下载函数
download_video() {
    local id=$1
    local output=$2
    echo "下载: $id"
    yt-dlp "https://www.youtube.com/watch?v=$id" \
        --extractor-args "youtube:player_client=android" \
        -o "$output/$id.mp4" \
        --quiet
}

# 下载亚洲肌肉男
echo ""
echo ">>> 下载亚洲肌肉男..."
for id in "${muscle_ids[@]}"; do
    download_video "$id" "~/Downloads/Video_素材/muscle"
done

# 下载亚洲鲜肉
echo ""
echo ">>> 下载亚洲鲜肉..."
for id in "${twink_ids[@]}"; do
    download_video "$id" "~/Downloads/Video_素材/twink"
done

# 下载亚洲情侣
echo ""
echo ">>> 下载亚洲情侣..."
for id in "${couple_ids[@]}"; do
    download_video "$id" "~/Downloads/Video_素材/couple"
done

echo ""
echo "========================================="
echo "   全部完成!"
echo "========================================="
