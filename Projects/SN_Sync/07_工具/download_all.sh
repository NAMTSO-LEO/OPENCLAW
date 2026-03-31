# 视频ID列表 - 可直接复制

## 亚洲肌肉男
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

## 亚洲鲜肉
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

## 亚洲情侣
couple_ids=(
"DEMQFNqSzfU"
"IupJh_nO10E"
"Ug8lT4SU7A8"
"HoM69OCHNZU"
"pVV1w66oCpk"
"3VDOUHmIK9w"
"9vLpd4ySHyQ"
)

# 下载所有
echo "开始下载亚洲肌肉男..."
for id in "${muscle_ids[@]}"; do
    echo "下载: $id"
    yt-dlp "https://www.youtube.com/watch?v=$id" -o ~/Downloads/Video_素材/muscle_$id.mp4
done

echo "开始下载亚洲鲜肉..."
for id in "${twink_ids[@]}"; do
    echo "下载: $id"
    yt-dlp "https://www.youtube.com/watch?v=$id" -o ~/Downloads/Video_素材/twink_$id.mp4
done

echo "开始下载亚洲情侣..."
for id in "${couple_ids[@]}"; do
    echo "下载: $id"
    yt-dlp "https://www.youtube.com/watch?v=$id" -o ~/Downloads/Video_素材/couple_$id.mp4
done

echo "全部完成!"
