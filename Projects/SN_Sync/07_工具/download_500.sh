#!/bin/bash
# 完整版批量下载脚本 - 500+视频
# 使用方法: ./download_500.sh

export PATH="$PATH:/Users/levi/Library/Python/3.9/bin"

# 创建分类目录
mkdir -p ~/Downloads/Video_素材/{muscle,bear,daddy,chinese,korean,japanese,thai,couple,twink,shorts,shower,bedroom,filipino,vietnamese,naked}

echo "========================================="
echo "   500+视频批量下载"
echo "========================================="

# ===== 肌肉男 =====
muscle=(
"YrlTgWHQCWs" "t2AEa-MAShM" "hNMlINwp87E" "N4Iyy3e9JSU" "bIkVBvpqxKk"
"CDjHY-EnvDo" "B6W2Al5uxb4" "M8mAqEycvMY" "u_ZkvqFzwTE" "KVXsYr3UCvk"
"fnHp3V4KQs" "G7h8wuwR_gA" "s02Zf6Jwl_U" "Rdl_9nVNDBY" "gpF2bLjJcz0"
"DVhKYkdXSn8" "m22uqC29xTs" "R6E49rs01dI" "vlltUiOwhsw" "8Ul5vhDM_CY"
"W3K2_cZi39M" "NVJ23PLb0dU" "cGVKC63E7uw" "ZpmRMWEiuXw" "crU1lGoPRe8"
"S70vdhN2tNM" "o7ECp27nWTQ" "FQB0vGqYVa4" "xIhYgSs-rlk" "XbRN7nrorrM"
"TvhN_yGSdls" "cV1vB76zzyU" "Ttmw7K5pcjY" "RL3yrkqoWnE" "NnzYMuEEjfk"
"fb1JlxvXKmY" "Jrof1eyIAz4" "9TaUBBoCXqM" "yKa1t53DEss" "GYY2rNd3wvI"
)

# ===== Bear =====
bear=(
"mTL8RI-3MO8" "1HhKrbMcbsQ" "khEVvVgxDcw" "CHtJ23AoIUg" "KAduw7Mg780"
"6Z2zgkbteGw" "MkkV5fw7NC4" "TafK1ZLlNI4" "jp6yWCi3zM0" "cMYNqoOtY1w"
"Pqj96dkeWTc" "GdcW9JhWfPs" "2DaRKkZo4gY" "zco2W6dSWE8" "TW5oAqc0hTY"
"iNpK6sJZkQI" "mzcjGEAgUWo" "ykuQgEMpQyc" "6iGNIpaevDA"
)

# ===== Daddy =====
daddy=(
"n-zE2vvccWE" "0GTHG5zMJLI" "4O-OT9Cofw4" "HmblFNZmQ_o" "X-PkmQP8uP8"
"D5sFNqeAbrY" "GKQ4FjHW12k" "9i2RYRhmjRk" "Ad_tjyfQ2Mc" "DUgrq4YY5BY"
"W0xEcww-ikw" "VjeYLrveAQU" "yLRH5pSizp0" "Ul9FWM12wyo"
)

# ===== 中国 =====
chinese=(
"OITOyhPvwOE" "JmlC8QLfe74" "A2tiF519J-k" "jKBSNjn982A" "hSP1mTPK6uE"
"_rrSH2mvoWQ" "sJyR-3Op0YU" "irBcYAvr31c" "mwgVUWOl4QI" "PUvlpHegnc4"
"3_OyREQigTI" "n5iwOPp1Inc" "ScmA9SLhzN4" "tyH5XuCKnIY" "U4iF1besgOM"
"NIHVN71SrLk" "hC5feNvUR-U" "L5HasQTq_3c" "GnSZfRWL7y0" "A5Oj-uSWACU"
"DEMQFNqSzfU" "IupJh_nO10E" "Ug8lT4SU7A8" "HoM69OCHNZU" "pVV1w66oCpk"
"3VDOUHmIK9w" "9vLpd4ySHyQ" "2u-7KRVVrYA" "awD1bcm_yy4" "7cGGAwFYh-c"
"7Q07Lx8sx8o" "5oR9eiVwBfc"
)

# ===== 韩国 =====
korean=(
"AQHtJ-wuyxs" "C5j079v4G1s" "mzsLr8tev2I" "NzFIBrqbg1o" "TADXy4Hvo4Y"
"6bG2dVno-AM" "JtD_ACmej0A" "jiFDY6N33aw" "ICjWxEJElIU" "gtzf6046MD0"
"SdnTtZcOESw" "wRf61V3LX8Y" "tsA6q4g_jdo" "CklfwpEUYsg" "wft1q5OgynI"
"duF7Q7dtLCs" "ObFoiV2Y9LA" "btjhpxoDatU" "G4lw-zjHmlU" "tcC4gnLesWM"
"BwWMMkxjecc" "J7X__JSTMPM"
)

# ===== 日本 =====
japanese=(
"0CDr1GLpxjE" "qbQaa9zeAYU" "joPqChcaMQ8" "XDdF4Tr-J-Q" "3DRbUTwseXY"
"Z1JbepgGtFo" "Th6pmZuHE1E" "0_RbvZH_zOc" "rrAlwiqXNlE" "sCg_tSnGSj4"
"SEJF34ewW78" "vjzFlS1AIXQ" "LjIbvGEyQ0o" "bJsBMu9qXho" "dmUACAn0miA"
"r6M0F__s1rc" "dvXd_HCfRHk" "ZMMYtclNtf8" "xO8d7ZBGTTU" "tH0P_GB3kp8"
"OLrGHQyMlEI" "SzboZJ8w1Pg"
)

# ===== 泰国 =====
thai=(
"0an0E53_MVo" "EiIE5IiBrBE" "85vdbXQn0Qk" "MqSnQq6jSnc" "Q1nxt4IBYuo"
"Kij68JFRvRg" "KinA3c-qOA4" "EFjgyo0jIvo" "u3xmwAD35sY" "RC1NktIVoug"
"p8tf80aewGY" "Pbi4O-JV0B4" "sLUGhhrO4SM" "kDTXuZyhzM4" "pEWKaUWvFPE"
"liMyKc1FDw8" "A2FLc8u1bHM" "bg73q_sEUAs"
)

# ===== 情侣 =====
couple=(
"74SxnuKI9zQ" "sJyR-3Op0YU" "NzFIBrqbg1o" "UbwaObNxxI4" "OLrGHQyMlEI"
"1FOvNa4k_Ms" "1ARDZNBNy94" "cS8TIAvZFTg" "UbgO92XBRlA" "D5sFNqeAbrY"
"f88ceQi9sh4" "ZhqHuaCGfS8" "JmlC8QLfe74" "hC5feNvUR-U" "tcC4gnLesWM"
"KnOfIiQvpLw" "Nya5v3krkB0" "dhJZCCAfF08" "H6FnK6YUaBc" "DEMQFNqSzfU"
"IupJh_nO10E" "Ug8lT4SU7A8" "pVV1w66oCpk" "3VDOUHmIK9w" "9vLpd4ySHyQ"
"2u-7KRVVrYA" "fkIyvrGPSCc" "on2VQQ90n78" "GKQ4FjHW12k" "wt04Vtcl0dM"
"L5HasQTq_3c"
)

# ===== 鲜肉 =====
twink=(
"3-fMRJk_1N4" "-1psP2GcI0M" "Aqkok-Y8JxU" "F12byFhNZzs" "Qz6w0HlP5tA"
"8DVJMH4CpuA" "K_rcshH1iFY" "rm8uHoaJV6k" "AnBaNqM1UVY" "J7X__JSTMPM"
"2DuhkVhRx6U" "BG7Ovp9v8CU" "nNZ9ma6KmQQ" "e3nqncBUdns" "yTYnO51vZX4"
"BwWMMkxjecc" "PhU8MJQlp1s" "DYhibRwl3NU" "jceyRtfdaNM" "UhjAjfRzGVw"
"AW5yFweAQO8" "PRMYy0fXVKw" "IoSRrEtMVbw" "VnO4QbeXl5M" "JvaJRFexErQ"
"W1rxSIFPArk" "Z7UktwKXOZo" "9OFzC0yz0HA" "TZFxMDDFDCw"
)

# ===== 短视频 =====
shorts=(
"dhJZCCAfF08" "NIHVN71SrLk" "GKQ4FjHW12k" "n-zE2vvccWE" "Nya5v3krkB0"
"PhU8MJQlp1s" "_rrSH2mvoWQ" "pVV1w66oCpk" "3VDOUHmIK9w" "wt04Vtcl0dM"
"ZTfG4cxywEQ" "on2VQQ90n78" "X-PkmQP8uP8" "Z7UktwKXOZo" "u3xmwAD35sY"
"L5HasQTq_3c" "fYjOvr3qX-4"
)

# ===== 浴室 =====
shower=(
"SzboZJ8w1Pg" "ttbK9zZ1dQU" "AnBaNqM1UVY" "6RZXKC7wrdM" "XDdF4Tr-J-Q"
"scSKECQP4GM" "X6Nmu87WXDg" "RopnE53MEOM" "avhvCJJp8OI" "cLXFzAJJabk"
"wYBLrxBQfhQ" "sOihnfYD714" "G7RofCDsVMI" "3TX5XtnqfPs" "yI0b81eaYMw"
"dBI7cunnkKE" "xWSTKhsddY8" "Qxb58nXLaoA" "T3iKUtMUPxI"
)

# ===== 卧室 =====
bedroom=(
"cK4as1krIHC" "ThpmZuHE1E" "b3-hItHW-5Y" "VjeYLrveAQU" "9dylluOwyV0"
"awD1bcm_yy4" "oHgh9E91oCs" "kmpYGzk3YsQ" "v-NzzBLEP4k" "B2GkSDO7O4A"
"tErUbqY3kSI" "Id_f9gwyE7E" "18VoxYLNykQ" "fYqGqmoy8qI"
)

# ===== 菲律宾 =====
filipino=(
"gdUYN4yZdWQ" "4cXCQEAzFHE" "3DDWndVpnnc" "zZj8d6X0dko" "pgJAArtD7Fs"
"9U61e7EOj6k" "9e490CnD07Q" "0RifF6E39hA" "dUhWtC1W1uI" "RMGMLs2WbaQ"
"a9zM7TJXu48" "ZnuBPmc8wgU" "9NY0Hm8nOtE" "MCOP5dOLN9g" "FzNud6Tu_bY"
"ub5avuY8alc" "bhRooc33szU" "8psKyL1eK1A" "KuvfkdBLA5I" "WLiZCzxIik8"
)

# ===== 越南 =====
vietnamese=(
"W6vvf0Yw7L4" "IOMVp7Moaow" "u5kCjGVJ9aQ" "gOPpM6ILGA0" "1EcQ-2ejgok"
"7nCjT5IjNCo" "AaIA5mv11GA" "jBnG4w9Jjcs" "ajb-YbY3-rw" "EtfH88K4kUY"
"btC_b7gcUiY" "6otr5VOtRaM" "yz6ZxHEHcpM" "NJ82O9Nq_lE" "jikcW4gwN84"
"7mTG1Pt_RxU" "IG7tRHIgXn4" "HggezDjj7N8"
)

# ===== 脱衣 =====
naked=(
"mrN5--J_64w" "ta8JVR_ZURM" "NT-XrRMCshg" "rpE943CJdO0" "FfrSkMBCojI"
"ZWCWeYBV2Yk" "MLGjR2UIo18" "Kr8P9uB86ls" "xkpxHDS2a5A" "q8yOWy0ijWg"
"V3VAi0RaICk" "rW2T1wUfX4I" "RE52ZKJ2ILo" "m_64VHWshhk" "xciAv_sEHfk"
"LpIF_-LsrLQ" "YsyhNUd-7cs"
)

# 下载函数
download_video() {
    local id=$1
    local folder=$2
    echo "下载: $id -> $folder"
    yt-dlp "https://www.youtube.com/watch?v=$id" \
        --extractor-args "youtube:player_client=android" \
        -o "~/Downloads/Video_素材/$folder/$id.mp4" \
        --quiet 2>/dev/null &
}

# 统计
echo ""
echo "=== 视频统计 ==="
echo "肌肉: ${#muscle[@]}"
echo "Bear: ${#bear[@]}"
echo "Daddy: ${#daddy[@]}"
echo "中国: ${#chinese[@]}"
echo "韩国: ${#korean[@]}"
echo "日本: ${#japanese[@]}"
echo "泰国: ${#thai[@]}"
echo "情侣: ${#couple[@]}"
echo "鲜肉: ${#twink[@]}"
echo "短视频: ${#shorts[@]}"
echo "浴室: ${#shower[@]}"
echo "卧室: ${#bedroom[@]}"
echo "菲律宾: ${#filipino[@]}"
echo "越南: ${#vietnamese[@]}"
echo "脱衣: ${#naked[@]}"

total=$(( ${#muscle[@]} + ${#bear[@]} + ${#daddy[@]} + ${#chinese[@]} + ${#korean[@]} + ${#japanese[@]} + ${#thai[@]} + ${#couple[@]} + ${#twink[@]} + ${#shorts[@]} + ${#shower[@]} + ${#bedroom[@]} + ${#filipino[@]} + ${#vietnamese[@]} + ${#naked[@]} ))
echo ""
echo "总计: $total 个视频"
echo "========================================="

# 询问是否下载
read -p "是否开始下载? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "已取消"
    exit 0
fi

echo ""
echo "开始下载..."

# 下载所有分类
for id in "${muscle[@]}"; do download_video "$id" "muscle"; done
for id in "${bear[@]}"; do download_video "$id" "bear"; done
for id in "${daddy[@]}"; do download_video "$id" "daddy"; done
for id in "${chinese[@]}"; do download_video "$id" "chinese"; done
for id in "${korean[@]}"; do download_video "$id" "korean"; done
for id in "${japanese[@]}"; do download_video "$id" "japanese"; done
for id in "${thai[@]}"; do download_video "$id" "thai"; done
for id in "${couple[@]}"; do download_video "$id" "couple"; done
for id in "${twink[@]}"; do download_video "$id" "twink"; done
for id in "${shorts[@]}"; do download_video "$id" "shorts"; done
for id in "${shower[@]}"; do download_video "$id" "shower"; done
for id in "${bedroom[@]}"; do download_video "$id" "bedroom"; done
for id in "${filipino[@]}"; do download_video "$id" "filipino"; done
for id in "${vietnamese[@]}"; do download_video "$id" "vietnamese"; done
for id in "${naked[@]}"; do download_video "$id" "naked"; done

echo ""
echo "全部任务已添加! 正在后台下载..."
echo "查看下载进度: ls -la ~/Downloads/Video_素材/"
