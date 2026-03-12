# Evidence Engine MVP
医疗证据操作系统 - 最小可行产品

## 功能
- 描述性统计
- 组间比较(t检验、卡方检验)
- 回归分析(Logistic回归)
- 生存分析(Kaplan-Meier)
- 倾向评分匹配

## 安装

```bash
pip install -r requirements.txt
```

## 运行

```bash
cd app
streamlit run app.py
```

## 技术栈
- Python 3.9+
- Streamlit (Web界面)
- Pandas/NumPy (数据处理)
- SciPy/Statsmodels (统计分析)
- Scikit-learn (机器学习)
- Lifelines (生存分析)

## 目录结构
```
EvidenceEngine_MVP/
├── app/
│   └── app.py          # Web界面
├── core/
│   └── analyzer.py    # 核心分析引擎
├── data/
│   └── README.md
└── requirements.txt
```

## 版本
MVP v0.1 - 2026-03-11
