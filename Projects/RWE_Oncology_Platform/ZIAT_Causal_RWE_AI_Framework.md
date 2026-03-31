# 珠海中科先进技术研究院 - 因果RWE+AI决策模型框架
## Causal-RWE-AI Decision Pipeline for ZIAT

---

## 一、总体架构（5层 + AI增强层）

### 1. 数据层 (Data Foundation)
- 临床试验 (RCT via CDISC/ADaM)
- 真实世界数据 (EHR、Claims、Registry、医疗器械使用数据)
- **珠海先进院优势**: 高质量医疗器械大数据集

### 2. 关联层 (Association)
- 传统统计: 描述性 + 简单回归 (SAS PROC REG / LOGISTIC / PHREG)

### 3. 因果推断层 (Causal Inference Core) ← 升级重点
- DAG建模定义confounder
- Propensity Score + IPTW (带stabilized weights)
- Target Trial Emulation (把真实世界数据模拟成RCT)
- 进阶: Doubly Robust、Instrumental Variable

### 4. RWE层 (Real-World Evidence Generation)
- 用因果方法产生可用于监管的证据
- 外部对照臂 (External Control Arm)
- 长程安全性、label extension支持

### 5. 决策层 (Regulatory / Clinical / HEOR / 器械注册决策)
- 输出: HR/RR/RD、cost-effectiveness、QALY
- 支持FDA/NMPA注册申报

### AI增强层 (珠海先进院特色)
- AI大模型辅助: 自动生成申报材料、数据清洗、信号检测
- 对接"医疗器械注册申报AI大模型"

---

## 二、SAS实战模板 (Oncology/医疗器械生存/安全性)

```sas
/* 1. 数据准备 */
proc logistic data=analysis_data descending;
    model treatment = age sex stage comorbidity;
    output out=ps_data pred=ps;
run;

/* 2. Stabilized IPTW 计算 */
proc means data=ps_data noprint;
    var treatment;
    output out=mean_trt mean=mean_trt;
run;

data iptw_data;
    set ps_data;
    if _n_=1 then set mean_trt(keep=mean_trt);
    if treatment=1 then iptw = mean_trt / ps;
    else iptw = (1-mean_trt) / (1-ps);
    /* Trimming */
    if iptw > 10 or iptw < 0.1 then delete;
run;

/* 3. 平衡性检查 (SMD) */
proc psmatch data=iptw_data;
    class treatment;
    psmodel treatment = age sex stage comorbidity;
    assess ps var=(age sex stage comorbidity) / plots=all weight=iptw;
run;

/* 4. 加权Cox模型 */
proc phreg data=iptw_data;
    class treatment;
    model time*event(0) = treatment / ties=efron;
    weight iptw;
    hazardratio treatment / diff=ref;
run;
```

---

## 三、项目级流程图

```
开始
  ↓
1. 问题定义 + Target Trial Emulation协议
   - Eligibility criteria
   - Index date
   - Treatment strategy
   - Follow-up & Outcome
   - Causal contrast (ATE/ATT)
  ↓
2. 数据整合 (SAS + CDISC标准)
  ↓
3. DAG构建
   - 识别confounders、mediators、colliders
  ↓
4. 因果估计 (PS/IPTW + Doubly Robust)
  ↓
5. RWE生成与验证
   - 主分析 + Sensitivity
   - 平衡诊断
  ↓
6. AI增强输出 (对接先进院大模型)
  ↓
7. 决策支持
   - NMPA/FDA申报
   - HEOR报告
  ↓
结束
```

---

## 四、适用场景

| 场景 | 适用性 |
|------|--------|
| 生物医药新药RWE补充 | ✅ |
| 医疗器械长期安全性/有效性 | ✅ |
| AI注册申报大模型结合 | ✅ |
| oncology/罕见病器械 | ✅ |

---

## 五、升级路线

| 阶段 | 内容 |
|------|------|
| 短期 | PS/IPTW模板 ✅ |
| 中期 | DAG + Target Trial Emulation |
| 高级 | IV + Causal ML + 医疗器械版 |

---

## 六、珠海先进院优势对接

- 医疗器械大数据集
- 注册申报AI大模型
- 生物医药与AI大数据交叉领域

---

*Framework created: 2026-03-28*
*For: 珠海中科先进技术研究院项目适配*