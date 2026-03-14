#!/bin/bash
# 自动下载500+视频 - 直接运行
export PATH="$PATH:/Users/levi/Library/Python/3.9/bin"

# 创建目录
mkdir -p ~/Downloads/Video_素材/{muscle,twink,couple,chinese,korean,japanese,thai,other}

echo "开始自动下载..."

# 肌肉
for id in fb1JlxvXKmY gpF2bLjJcz0 DVhKYkdXSn8 m22uqC29xTs R6E49rs01dI Jrof1eyIAz4 GoL3__f6Um0 9TaUBBoCXqM yKa1t53DEss 8Ul5vhDM_CY CDjHY-EnvDo N4Iyy3e9JSU W3K2_cZi39M t2AEa-MAShM vlltUiOwhsw TkVzODICScs m-fvLoFz1Qc 06bJJ0rWcYg DIQ1eEzAI2U crU1lGoPRe8 k9HAA47Q2b4 IOWOFb33U78 pkvhccQNXls eVGzrXZ0Pms u_ZkvqFzwTE 7Q07Lx8sx8s IfVvTy0Sf9s Yp53d7llY-U i7cEUgOtX9M YrlTgWHQCWs N4Iyy3e9JSU bIkVBvpqxKk CDjHY-EnvDo u_ZkvqFzwTE S70vdhN2tNM SYgOm_H0Zzo o7ECp27nWTQ xIhYgSs-rlk Rdl_9nVNDBY 1aSzgdxK_fI s02Zf6Jwl_U XbRN7nrorrM TvhN_yGSdls cV1vB76zzyU Ttmw7K5pcjY; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/music/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

# 鲜肉
for id in 3-fMRJk_1N4 -1psP2GcI0M rm8uHoaJV6k BwWMMkxjecc ILN6IOD7QJk 61Rm4Gdpd8A c8eN0n2a8rc IH--CySxClA -8OHUUH8LnU 9xBwLq8BLnY Y0LDOftYqwg cZLUSUb_QRI spyWAHQeswc XOMJwptSPqY IpXg9DRc6mE rrilFQKK2A8 39LeOP0ced0 OMw69Ss0kgw 2ykGb5qW7YM kH7c6pn9zlk qgPMUbNsyQE uZ5GXWL3Hc0 uMQpi1zulpU yQePQ9q6BQ4 dOb1c-5uzgM TwDjri4lHqg -2QE-LI2EgA FKaWdVRviu4 8SCJsvi8OcU SAjxGOa0jkg; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/twink/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

# 情侣
for id in _rrSH2mvoWQ FIcX3jZFoT8 DEMQFNqSzfU IupJh_nO10E cnBYYFuYDi0 OMPssIcZezs Ug8lT4SU7A8 pVV1w66oCpk 3VDOUHmIK9w GKQ4FjHW12k 9vLpd4ySHyQ 2u-7KRVVrYA fkIyvrGPSCc HoM69OCHNZU hhp24tF1fug 0_RbvZH_zOc CTXvlL4qJYc dhJZCCAfF08 3gRmDdDMijg 1FOvNa4k_Ms Th6pmZuHE1E Ul9FWM12wyo IaGAuT8jEKU tg_G1tcOiRI AK-y_yrQeyA AEUKESqjIjg Hgh6sZNFGwk UhjAjfRzGVw ksvsckm5RMI NM5XGV4qjd8; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/couple/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

# 中国
for id in JmlC8QLfe74 jKBSNjn982A irBcYAvr31c URDvMcAKVNE LwooyFdXDmY zWCRPLanvS0 kY8L-WefjWk tS2VXSroznY sJyR-3Op0YU o5PXc08K0Vo UNgmdGJGoTE IoGYl_m5EYw guQ09SalUwo Nc3hJLHMMRM SMLURXHfFtw CP0sl_xZD3A PVfeLeTKeJA 8wCuNIiqiNw EK9HqSmffJE 81VckvNfuew LEXme91w0AQ 9nLp3nF-pyM _DAOphjcHmM jiFDY6N33aw dRITHPT7bu8 sC46nr7n824 aQF8BMvmP_U 0USfpGB1iow MnUOw6ak3Zg XjIIp3YrTBw; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/chinese/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

# 韩国
for id in wOaRUruTEnw Nya5v3krkB0 AQHtJ-wuyxs C5j079v4G1s mzsLr8tev2I aAUcZo46INI _rrSH2mvoWQ cy-kWlIxrBQ VWlovqcesUQ NzFIBrqbg1o XhuamGlx5n8 -3jNzIWVNzo 9vLpd4ySHyQ BF6STrPEuVA dhJZCCAfF08 IaGAuT8jEKU SI5LpA1kxEc gnDhz9NQP7s WJVNSzMkg0I wWGghURSm58 YDsWBYOVKPs Uu3me40N6JE TADXy4Hvo4Y jEB1ZyQ7q-0 FYtxsUKDj7I 6bG2dVno-AM 50wuI2xhx2M G7RofCDsVMI 9OFzC0yz0HA; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/korean/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

# 日本
for id in 0CDr1GLpxjE qbQaa9zeAYU joPqChcaMQ8 _j13Y-LeMRw XDdF4Tr-J-Q 3DRbUTwseXY Z1JbepgGtFo Th6pmZuHE1E 0_RbvZH_zOc _qYIPBVpBDI rrAlwiqXNlE sCg_tSnGSj4 SEJF34ewW78 bJsBMu9qXho vjzFlS1AIXQ r6M0F__s1rc KUG46stK26s LjIbvGEyQ0o wiFZUlEvbzI 04OPMdVkFUM dmUACAn0miA bhHLIB-yqZA SsJTMElwJ40 JYNniXFqUpM dvXd_HCfRHk ZMMYtclNtf8 xO8d7ZBGTTU xswaCtCtdt4; do
    yt-dlp "https://www.youtube.com/watch?v=$id" --extractor-args "youtube:player_client=android" -o "~/Downloads/Video_素材/japanese/%(title)s.%(ext)s" --quiet 2>/dev/null &
done

echo "下载任务已添加! 等待完成..."
sleep 5
echo "查看目录: ls ~/Downloads/Video_素材/"
