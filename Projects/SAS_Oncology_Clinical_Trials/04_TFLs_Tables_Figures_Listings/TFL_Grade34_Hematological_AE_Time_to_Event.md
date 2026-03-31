# TFL 方案：首次给药至Grade 3-4血液学不良事件时间分析表

## 一、表基本信息

### 1.1 表格描述

| 项目 | 内容 |
|------|------|
| 表格编号 | 预计为 AE 相关表格序号 |
| 标题 | Time from first dose (any study drug) to first onset of grade 3–4 [ hematological event ] (days) |
| 所属章节 | 安全性分析 / 不良事件分析 |
| 数据来源 | ADSAFTTE + ADSL |
| 前置数据集 | ADSL → ADAE → ADAES → ADSAFTTE |

---

## 二、数据流程概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                     TFL 数据流程（ADSAFTTE 路线）                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   SDTM                                                            │
│     │                                                              │
│     ▼                                                              │
│   ADAE ──────────────────────────────────────────────────────────→│
│     │                                                              │
│     ▼                                                              │
│   ADAES ─────────────────────────────────────────────────────────→ │
│     │                                                              │
│     ▼                                                              │
│   ADSAFTTE ─────────────────────────────────────────────────────→ │
│     │                                                              │
│     ▼                                                              │
│   TFL (Tables, Listings, Figures)                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### ISS 中 TTE 数据集的派生层级

| 层级 | 数据集 | 作用 |
|------|--------|------|
| 1 | ADAE | 原始不良事件记录 |
| 2 | ADAES | 按受试者+事件汇总，派生 Grade 标记 |
| 3 | ADSAFTTE | Time-to-Event 派生，生成 AVAL |
| 4 | TFL | 汇总统计与输出 |

---

## 三、ADSAFTTE 关键变量

### 3.1 本表所需变量

| 变量 | 说明 | 来源 |
|------|------|------|
| USUBJID | 受试者唯一标识 | ADSAFTTE |
| PARAMCD | 参数代码 | ADSAFTTE |
| PARAM | 参数名称 | ADSAFTTE |
| AVAL | 分析值（天数） | ADSAFTTE = ADT - STARTDT + 1 |
| TRTEMFL | Treatment-Emergent 标志 | ADSAFTTE |
| ANL02FL | Earliest Event 标志 | ADSAFTTE |
| TRTA | 实际治疗组 | ADSL |

### 3.2 目标 PARAMCD

| PARAMCD | 说明 |
|---------|------|
| STT3PLBD | Time to first Grade ≥3 leukopenia |
| STT3PNGD | Time to first Grade ≥3 neutropenia |
| STT3PYGD | Time to first Grade ≥3 lymphopenia |
| STT3PTGD | Time to first Grade ≥3 thrombocytopenia |
| STT3PABD | Time to first Grade ≥3 anemia |

### 3.3 ADSAFTTE 派生逻辑

AVAL 已在 ADSAFTTE 中派生完成：

```
AVAL = ADT - STARTDT + 1
```

即：事件分析日期 - 治疗开始日期 + 1（天数）

---

## 四、TLF 数据筛选

### 4.1 筛选条件

```sas
proc sql;
    create table tte as
        select
            a.usubjid,
            a.paramcd,
            a.param,
            a.aval,
            b.trta as trt
        from adsaftte a
        left join adsl b
            on a.usubjid = b.usubjid
        where
            a.trtemfl = 'Y'
            and a.anl02fl = 'Y'
            and a.paramcd in (
                'STT3PLBD',
                'STT3PNGD',
                'STT3PYGD',
                'STT3PTGD',
                'STT3PABD'
            );
quit;
```

### 4.2 筛选条件解释

| 条件 | 说明 |
|------|------|
| TRTEMFL = 'Y' | Treatment-Emergent，仅纳入治疗期间发生的事件 |
| ANL02FL = 'Y' | Earliest Event，仅纳入每类事件的首次发生记录 |
| PARAMCD in (...) | 仅纳入 5 个目标血液学 Grade ≥3 事件 |

---

## 五、统计逻辑

### 5.1 统计量

| 统计量 | 说明 |
|--------|------|
| n | 事件发生例数 |
| Mean (SD) | 均值（标准差） |
| Median | 中位数 |
| Min | 最小值 |
| Max | 最大值 |

### 5.2 汇总维度

- **行维度**：PARAMCD / PARAM
- **列维度**：Treatment Group（TRTA）

### 5.3 汇总程序

```sas
proc means data=tte n mean std median min max noprint;
    class paramcd trt;
    var aval;
    output out=stats
        n=n
        mean=mean
        std=sd
        median=median
        min=min
        max=max;
run;
```

---

## 六、格式整理

### 6.1 格式化显示值

```sas
data stats_fmt;
    set stats;
    
    length mean_sd $30 minmax $30;
    
    /* Format Mean (SD) */
    mean_sd = cats(put(mean, 6.1), ' (', put(sd, 6.2), ')');
    
    /* Format Min, Max */
    minmax = cats(put(min, 6.1), ', ', put(max, 6.1));
    
    keep paramcd trt n mean_sd minmax;
run;
```

### 6.2 最终输出结构

| 列 | 说明 |
|----|------|
| PARAM | 事件名称 |
| n | 例数 |
| Mean (SD) | 均值（标准差） |
| Median | 中位数 |
| Min, Max | 最小值，最大值 |

列：按 Treatment Group 分组

---

## 七、完整 SAS 程序骨架

```sas
/*------------------------------------------------------------
Step 1: Prepare TTE analysis dataset from ADSAFTTE
------------------------------------------------------------*/
proc sql;
    create table tte as
        select
            a.usubjid,
            a.paramcd,
            a.param,
            a.aval,
            b.trta as trt
        from adsaftte a
        left join adsl b
            on a.usubjid = b.usubjid
        where
            a.trtemfl = 'Y'
            and a.anl02fl = 'Y'
            and a.paramcd in (
                'STT3PLBD',
                'STT3PNGD',
                'STT3PYGD',
                'STT3PTGD',
                'STT3PABD'
            );
quit;

/*------------------------------------------------------------
Step 2: Summary statistics
------------------------------------------------------------*/
proc means data=tte n mean std median min max noprint;
    class paramcd trt;
    var aval;
    output out=stats
        n=n
        mean=mean
        std=sd
        median=median
        min=min
        max=max;
run;

/*------------------------------------------------------------
Step 3: Format display values
------------------------------------------------------------*/
data stats_fmt;
    set stats;
    
    length mean_sd $30 minmax $30;
    
    /* Format Mean (SD) */
    mean_sd = cats(put(mean, 6.1), ' (', put(sd, 6.2), ')');
    
    /* Format Min, Max */
    minmax = cats(put(min, 6.1), ', ', put(max, 6.1));
    
    keep paramcd trt n mean_sd minmax;
run;

/*------------------------------------------------------------
Step 4: PROC REPORT output
------------------------------------------------------------*/
/* 后续接 PROC REPORT 生成最终 TFL */
```

---

## 八、QC 检查点

### 8.1 数据集级 QC
- [ ] ADSAFTTE 记录数
- [ ] TRTEMFL + ANL02FL 筛选后记录数
- [ ] 5 个 PARAMCD 是否全部命中

### 8.2 逻辑级 QC
- [ ] AVAL 计算逻辑（应为天数）
- [ ] 与 ADSL merge 后 TRTA 完整性

### 8.3 汇总级 QC
- [ ] n 与实际事件例数一致性
- [ ] 统计量计算正确性

---

## 九、关键理解（ISS TTE 表的核心逻辑）

### 9.1 为什么不能直接从 ADAE 做表

ISS 中的 Time-to-Event 表格**不应重新派生**，而应直接使用已派生好的 ADSAFTTE：

| 层级 | 说明 |
|------|------|
| ADAE | 原始 AE 记录 |
| ADAES | 按 Subject + Term 汇总，派生 Grade 标记（如 ANL18FL, ANL15FL 等） |
| ADSAFTTE | 派生 Time-to-Event（AVAL = ADT - STARTDT + 1） |
| TFL | 直接使用 ADSAFTTE 进行汇总统计 |

### 9.2 正确路线

```
ADAE → ADAES → ADSAFTTE → TFL
```

TFL 不重新做 derivation。

---

## 十、Grade 标记在 ADAES 中的对应关系

| Grade ≥3 事件 | ADAES 中的分析标志 |
|---------------|-------------------|
| Leukopenia | ANL18FL |
| Neutropenia | ANL15FL |
| Lymphopenia | ANL17FL |
| Thrombocytopenia | ANL19FL |
| Anemia | ANL34FL |

---

## 十一、输出格式示意

| | Treatment A (N=xx) | Treatment B (N=xx) |
|---|---|---|
| **Time to first Grade ≥3 leukopenia (days)** | | |
| n | | |
| Mean (SD) | | |
| Median | | |
| Min, Max | | |
| **Time to first Grade ≥3 neutropenia (days)** | | |
| n | | |
| Mean (SD) | | |
| Median | | |
| Min, Max | | |
| ... | ... | ... |

---

## 十二、参考文档

- ADSAFTTE Specification
- ADAES Specification
- ADAE Specification
- ADSL Specification
- TFL Shell
- SAP 相关章节
- ADaM IG v1.1
