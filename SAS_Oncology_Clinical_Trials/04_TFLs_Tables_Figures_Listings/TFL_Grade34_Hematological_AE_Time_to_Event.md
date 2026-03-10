# TFL 方案：首次给药至Grade 3-4血液学不良事件时间分析表

## 一、表基本信息

### 1.1 表格描述

| 项目 | 内容 |
|------|------|
| 表格编号 | 预计为 AE 相关表格序号 |
| 标题 | Time from first dose (any study drug) to first onset of grade 3–4 [ hematological event ] (days) |
| 所属章节 | 安全性分析 / 不良事件分析 |
| 数据来源 | ADSL + ADAE |
| 是否需要 ADEXSUM | 否（仅需 ADSL.TRTSDT + ADAE.ASTDT） |

---

### 1.2 分析目的

评估首次给药后至首次发生 Grade 3-4 血液学不良事件的时间分布，按治疗组进行汇总分析。

---

## 二、人群定义

### 2.1 人群来源

| 来源 | 数据集 | 说明 |
|------|--------|------|
| 分析人群 | ADSL | SAFFL = 'Y' 的受试者 |
| 列头分组 | ADSL | 按 Treatment Display Group |

### 2.2 人群筛选条件

```sas
data t_pop;
    set adsl;
    where saffl = 'Y' and not missing(trtsdt);
    
    * 按 Shell 定义列头分组
    if trta = 'Epco + R-CHOP' then coln = 1;
    else if trta = 'R-CHOP' then coln = 2;
    * ... 其他分组逻辑
    
    keep usubjid trtsdt coln;
run;
```

### 2.3 关键变量

| 变量 | 来源 | 说明 |
|------|------|------|
| USUBJID | ADSL | 受试者唯一标识 |
| TRTSDT | ADSL | 首次给药日期 |
| SAFFL | ADSL | 安全性人群标志 |
| COLN | 派生 | 列序号 |
| COLLBL | 派生 | 列标签 |

---

## 三、事件定义

### 3.1 事件来源

| 来源 | 数据集 | 说明 |
|------|--------|------|
| 目标事件 | ADAE | Grade 3-4 血液学不良事件 |

### 3.2 事件筛选条件

```sas
data t_ae0;
    set adae;
    where trtemfl = 'Y'          /* Treatment-emergent */
          and tesfl = 'Y'         /* 首次发生/加重 */
          and aetoxgrn in (3, 4); /* Grade 3-4 */
    
    * 按 AEDECOD 映射至目标事件 block
    select (upcase(strip(aedecod)));
        when ('LEUKOPENIA') do;
            eventcd = 'LEUKOPENIA';
            eventlbl = 'Leukopenia - white blood cells (hypo)';
            roword = 1;
        end;
        when ('NEUTROPENIA') do;
            eventcd = 'NEUTROPENIA';
            eventlbl = 'Neutropenia - absolute neutrophil count (hypo)';
            roword = 2;
        end;
        when ('LYMPHOPENIA') do;
            eventcd = 'LYMPHOPENIA';
            eventlbl = 'Lymphopenia - lymphocytes (hypo)';
            roword = 3;
        end;
        when ('THROMBOCYTOPENIA') do;
            eventcd = 'THROMBOCYTOPENIA';
            eventlbl = 'Thrombocytopenia - platelet count (hypo)';
            roword = 4;
        end;
        when ('ANEMIA') do;
            eventcd = 'ANEMIA';
            eventlbl = 'Anemia - hemoglobin (hypo)';
            roword = 5;
        end;
        otherwise delete;
    end;
    
    onsetdt = astdt;  /* 事件开始日期 */
    
    keep usubjid eventcd eventlbl roword onsetdt;
run;
```

### 3.3 目标事件列表

| Row Order | Event Code | Event Label |
|-----------|------------|-------------|
| 1 | LEUKOPENIA | Leukopenia - white blood cells (hypo) |
| 2 | NEUTROPENIA | Neutropenia - absolute neutrophil count (hypo) |
| 3 | LYMPHOPENIA | Lymphopenia - lymphocytes (hypo) |
| 4 | THROMBOCYTOPENIA | Thrombocytopenia - platelet count (hypo) |
| 5 | ANEMIA | Anemia - hemoglobin (hypo) |

### 3.4 关键变量

| 变量 | 来源 | 说明 |
|------|------|------|
| USUBJID | ADAE | 受试者唯一标识 |
| EVENTCD | 派生 | 事件代码 |
| EVENTLBL | 派生 | 事件标签 |
| ROWORD | 派生 | 行序号 |
| ONSETDT | ADAE.ASTDT | 事件开始日期 |

---

## 四、时间变量计算

### 4.1 时间计算公式

```
AVAL = ONSETDT - TRTSDT + 1
```

### 4.2 筛选规则

- 仅保留 AVAL >= 1 的记录
- 排除 AVAL <= 0 的异常记录（需单独 QC）

### 4.3 合并逻辑

```sas
proc sort data=t_pop; by usubjid; run;
proc sort data=t_ae1; by usubjid; run;

data t_tte;
    merge t_ae1(in=a) t_pop(in=b);
    by usubjid;
    if a and b;
    
    aval = onsetdt - trtsdt + 1;
    if aval >= 1;
    
    keep usubjid eventcd eventlbl roword coln aval;
run;
```

---

## 五、统计量输出

### 5.1 统计量定义

| 统计量 | 说明 |
|--------|------|
| n | 事件发生例数 |
| Mean (Std Dev) | 均值（标准差） |
| Median | 中位数 |
| Min, Max | 最小值，最大值 |

### 5.2 汇总维度

- **行维度**：ROWORD / EVENTCD / EVENTLBL
- **列维度**：COLN（治疗组）

### 5.3 汇总程序

```sas
proc means data=t_tte noprint;
    class roword eventcd eventlbl coln;
    var aval;
    output out=t_stat
        n=n
        mean=mean
        std=std
        median=median
        min=min
        max=max;
run;
```

### 5.4 格式化输出

```sas
data t_stat2;
    set t_stat;
    where not missing(eventcd) and not missing(coln);
    
    length c_n $50 c_meanstd $50 c_median $50 c_minmax $50;
    
    c_n = strip(put(n, 8.));
    
    if n > 0 then do;
        c_meanstd = cats(put(mean, 5.1), ' (', put(std, 6.2), ')');
        c_median = put(median, 5.1);
        c_minmax = cats(put(min, 5.1), ', ', put(max, 5.1));
    end;
    else do;
        c_meanstd = '';
        c_median = '';
        c_minmax = '';
    end;
    
    keep roword eventcd eventlbl coln c_n c_meanstd c_median c_minmax;
run;
```

---

## 六、表头 N 计算

### 6.1 列头 N 值来源

表头中的 (N=xxx) 来自 ADSL 中各治疗组的受试者人数。

```sas
proc sql;
    create table t_n as
    select coln,
           count(distinct usubjid) as n
    from t_pop
    group by coln;
quit;
```

### 6.2 宏变量使用

将 N 值传入 PROC REPORT：

```sas
%let n1 = ...;  /* 从 t_n 获取 */
%let n2 = ...;

proc report data=t_final headline headskip;
    columns ("Epco + R-CHOP (N=&n1)" col1, ...);
    ...
run;
```

---

## 七、完整 SAS 程序骨架

```sas
/*---------------------------*
* 1. Population from ADSL  *
*---------------------------*/
data t_pop;
    set adsl;
    where saffl = 'Y' and not missing(trtsdt);
    
    * 按 Shell 定义列头分组
    if trta = 'Epco + R-CHOP' then coln = 1;
    else if trta = 'R-CHOP' then coln = 2;
    else delete;
    
    keep usubjid trtsdt coln;
run;

/*---------------------------*
* 2. Event from ADAE       *
*---------------------------*/
data t_ae0;
    set adae;
    where trtemfl = 'Y'
          and tesfl = 'Y'
          and aetoxgrn in (3, 4);
    
    length eventcd $40 eventlbl $200;
    length roword 8;
    
    select (upcase(strip(aedecod)));
        when ('LEUKOPENIA') do;
            eventcd = 'LEUKOPENIA';
            eventlbl = 'Leukopenia - white blood cells (hypo)';
            roword = 1;
        end;
        when ('NEUTROPENIA') do;
            eventcd = 'NEUTROPENIA';
            eventlbl = 'Neutropenia - absolute neutrophil count (hypo)';
            roword = 2;
        end;
        when ('LYMPHOPENIA') do;
            eventcd = 'LYMPHOPENIA';
            eventlbl = 'Lymphopenia - lymphocytes (hypo)';
            roword = 3;
        end;
        when ('THROMBOCYTOPENIA') do;
            eventcd = 'THROMBOCYTOPENIA';
            eventlbl = 'Thrombocytopenia - platelet count (hypo)';
            roword = 4;
        end;
        when ('ANEMIA') do;
            eventcd = 'ANEMIA';
            eventlbl = 'Anemia - hemoglobin (hypo)';
            roword = 5;
        end;
        otherwise delete;
    end;
    
    onsetdt = astdt;
    keep usubjid eventcd eventlbl roword onsetdt;
run;

proc sort data=t_ae0;
    by usubjid eventcd onsetdt;
run;

data t_ae1;
    set t_ae0;
    by usubjid eventcd onsetdt;
    if first.eventcd;
run;

/*---------------------------*
* 3. Calculate time        *
*---------------------------*/
proc sort data=t_pop; by usubjid; run;
proc sort data=t_ae1; by usubjid; run;

data t_tte;
    merge t_ae1(in=a) t_pop(in=b);
    by usubjid;
    if a and b;
    
    aval = onsetdt - trtsdt + 1;
    if aval >= 1;
    
    keep usubjid eventcd eventlbl roword coln aval;
run;

/*---------------------------*
* 4. Summary stats          *
*---------------------------*/
proc means data=t_tte noprint;
    class roword eventcd eventlbl coln;
    var aval;
    output out=t_stat
        n=n
        mean=mean
        std=std
        median=median
        min=min
        max=max;
run;

/* 后续按 Section 五、六格式化输出 */
```

---

## 八、QC 检查点

### 8.1 人群级 QC
- [ ] SAFFL 筛选后受试者人数
- [ ] TRTSDT 缺失检查
- [ ] 列头分组完整性

### 8.2 事件级 QC
- [ ] TRTEMFL + TESFL 筛选后记录数
- [ ] Grade 3-4 筛选条件
- [ ] 目标事件映射完整性
- [ ] 去重后每 Subject × Event 唯一性

### 8.3 时间计算 QC
- [ ] AVAL 分布检查（应有 >= 1）
- [ ] AVAL <= 0 的异常记录

### 8.4 汇总级 QC
- [ ] Denominator 与表头 N 一致性
- [ ] 统计量计算正确性
- [ ] Shell 格式一致性

---

## 九、为什么不需要 ADEXSUM

### 9.1 ADEXSUM 适用场景
- Treatment Duration
- Total Dose
- Number of Doses
- Interruption Summary

### 9.2 本表适用场景
本表仅需两个核心日期：
- **首剂日期**：ADSL.TRTSDT
- **首次 G3-4 事件日期**：ADAE.ASTDT

因此，直接使用 **ADSL + ADAE** 即可满足需求，无需绕道 ADEXSUM。

---

## 十、注意事项

### 10.1 TRTSDT 确认
需确认 **ADSL.TRTSDT** 即为 Shell 认可的 "first dose (any study drug)"。

### 10.2 事件定义确认
需确认 5 个 Block 是否仅按 **AEDECOD** 单个 PT 抓取，若 Shell/Footnote 有更宽定义，需补充 Mapping List。

### 10.3 TESFL vs TRTEMFL
- **TRTEMFL = 'Y'**：确保为 Treatment-Emergent
- **TESFL = 'Y'**：确保为首次发生/加重
- 两个条件建议同时使用

---

## 十一、输出格式示意

| | Epco + R-CHOP (N=xx) | R-CHOP (N=xx) |
|---|---|---|
| **Leukopenia - white blood cells (hypo)** | | |
| Time from first dose to first onset of grade 3-4 (days) | | |
| n | | |
| Mean (Std Dev) | | |
| Median | | |
| Min, Max | | |
| **Neutropenia - absolute neutrophil count (hypo)** | | |
| ... | ... | ... |

---

## 十二、参考文档

- SAP 相关章节
- TFL Shell
- ADAE Specification
- ADSL Specification
- ADaM IG v1.1
