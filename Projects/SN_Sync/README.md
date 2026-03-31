# SN_Sync 项目

## 项目简介

SN_Sync 是一个面向BL/同志内容创作者的AI短视频创作工具。通过AI配音、素材整理和自动化工具，帮助创作者高效制作短视频内容。

---

## 文件目录

```
SN_Sync/
├── 01_小说/          # 原创小说
├── 02_剧本/          # 短视频剧本
├── 03_方案/          # 创作方案指南
├── 04_分析/          # 数据分析
├── 05_链接/          # 素材链接
├── 06_代码/          # 核心代码
└── 07_工具/          # 自动化脚本
```

---

## 内容说明

### 01_小说

| 文件 | 说明 |
|------|------|
| monk_novel.md | 禅心 - 寺庙BL小说 |
| ten_years_novel.md | 十年 - BL恋爱小说 |

### 02_剧本

| 文件 | 说明 |
|------|------|
| gay_scripts.md | BL短视频剧本 (第一批) |
| gay_scripts_more.md | BL短视频剧本 (第二批) |
| monk_scripts.md | 寺庙BL剧本 |

### 03_方案

| 文件 | 说明 |
|------|------|
| short_video_plan.md | 短视频制作计划 |
| best_gay_video_plan.md | 优质BL视频方案 |
| compilation_plan.md | 合集制作计划 |
| free_video_guide.md | 免费工具使用指南 |

### 04_分析

| 文件 | 说明 |
|------|------|
| tag_analysis.md | 标签分析 |
| asian_tags_analysis.md | 亚洲内容标签分析 |
| niche_recommendation.md | 细分市场推荐 |
| chinese_actor_classification.md | 中文演员分类 |

### 05_链接

| 文件 | 说明 |
|------|------|
| youtube_links.md | YouTube视频链接 |
| video_ids.sh | 视频ID列表 |

### 06_代码

| 文件 | 说明 |
|------|------|
| app.py | 主应用 |
| sn_sync_engine.py | 同步引擎 |
| tag_analyzer.py | 标签分析器 |
| tag_app.py | 标签应用 |
| requirements.txt | 依赖列表 |

### 07_工具

| 文件 | 说明 |
|------|------|
| batch_download.sh | 批量下载 |
| auto_download.sh | 自动下载 |
| download_video.sh | 视频下载 |
| download_500.sh | 500个下载 |
| download_all.sh | 全部下载 |

---

## 技术栈

- **语音合成**: ElevenLabs API
- **视频处理**: OpenShot, FFmpeg
- **下载工具**: yt-dlp
- **编程语言**: Python

---

## 使用流程

1. **获取素材** - 使用05_链接中的脚本下载视频
2. **创作剧本** - 参考02_剧本或原创
3. **生成配音** - 使用ElevenLabs API
4. **剪辑视频** - 使用OpenShot/剪映
5. **发布** - 抖音/B站/快手

---

## 更新记录

| 日期 | 内容 |
|------|------|
| 2026-03-13 | 创建项目，生成20集《十年》配音 |
| 2026-03-14 | 整理文件夹结构 |

---

*最后更新: 2026-03-14*
