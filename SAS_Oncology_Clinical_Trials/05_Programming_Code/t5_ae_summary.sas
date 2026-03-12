/*soh***************************************************************************
Program name : t5_ae_summary.sas
Compound : EPCO
Study : M20-621 and GCT3013-02 (ISS)
Milestone : ISS
Description : Create TFL t5.3.1 - Adverse Events Summary
--------------------------------------------------------------------------------
Details: 不良事件汇总表 - 所有AE、治疗相关AE、严重AE、导致停药AE
--------------------------------------------------------------------------------
**eoh**************************************************************************/

%init;

%let outpath=/sasdata/iss/output;
%let dtft=date9.;

************************************************************
 获取安全人群
***********************************************************;

data adsl;
 set adam.adsl;
 if saffl='Y';
run;

proc freq data=adsl noprint;
 table studyid*trta / out=trt_cnt;
run;

************************************************************
 获取所有不良事件
***********************************************************;

data adae;
 set adam.adae;
 if saffl='Y';
run;

/* 事件计数 */
proc sql;
 create table ae_summary as
 select studyid, trta,
        count(*) as n_ae,
        count(distinct usubjid) as n_pat_ae,
        count(case when aerel in ('RELATED','POSSIBLY RELATED') then 1 end) as n_rel_ae,
        count(distinct case when aerel in ('RELATED','POSSIBLY RELATED') then usubjid end) as n_pat_rel,
        count(case when aeser='Y' then 1 end) as n_ser_ae,
        count(distinct case when aeser='Y' then usubjid end) as n_pat_ser,
        count(case when aestaus='FATAL' then 1 end) as n_fatal,
        count(case when aestaus='FATAL' then usubjid end) as n_pat_fatal,
        count(case when aedcq='Y' then 1 end) as n_dq_ae,
        count(case when aedcl='Y' then 1 end) as n_dc_ae,
        count(distinct case when aedcl='Y' then usubjid end) as n_pat_dc
 from adae
 group by studyid, trta;
quit;

/* 计算发生率 */
proc sql;
 create table ae_summary_rate as
 select a.*, b.n as denom,
        round(a.n_pat_ae/denom*100,0.1) as pct_ae,
        round(a.n_pat_rel/denom*100,0.1) as pct_rel,
        round(a.n_pat_ser/denom*100,0.1) as pct_ser,
        round(a.n_pat_fatal/denom*100,0.1) as pct_fatal,
        round(a.n_pat_dc/denom*100,0.1) as pct_dc
 from ae_summary a
 left join trt_cnt b
 on a.studyid=b.studyid and a.trta=b.trta;
quit;

proc print data=ae_summary_rate;
 title "Adverse Events Summary";
run;

************************************************************
 按系统器官分类 (SOC) 和PT汇总
***********************************************************;

proc freq data=adae noprint;
 table studyid*trta*aebodsoc*pt / out=aesoc_freq;
run;

proc sort data=aesoc_freq;
 by studyid trta descending count;
run;

/* 常见AE (≥5%) */
proc sql;
 create table common_ae as
 select studyid, trta, aebodsoc, pt, count(*) as n, 
        count(distinct usubjid) as n_pat
 from adae
 group by studyid, trta, aebodsoc, pt
 having n_pat >= 5
 order by studyid, trta, descending n_pat;
quit;

proc print data=common_ae (obs=30);
 title "Common Adverse Events (>=5%)";
run;

************************************************************
 3-5级AE分析
***********************************************************;

proc sql;
 create table ae_gr34 as
 select studyid, trta, aebodsoc, pt,
        count(case when atoxgrn in (3,4,5) then 1 end) as n_gr34,
        count(distinct case when atoxgrn in (3,4,5) then usubjid end) as n_pat_gr34
 from adae
 group by studyid, trta, aebodsoc, pt;
quit;

proc print data=ae_gr34;
 title "Grade 3-5 Adverse Events";
run;

************************************************************
 输出RTF
***********************************************************;

filename rtfout "&outpath./t5_ae_summary.rtf";
ods rtf file=rtfout style=styles.rtf;

proc report data=ae_summary_rate split='|';
 columns studyid trta n_ae n_pat_ae pct_ae n_pat_rel pct_ser n_pat_dc pct_dc;
 
 define studyid / display "Study" width=12;
 define trta / display "Treatment" width=15;
 define n_ae / display "Number of|AEs" width=10;
 define n_pat_ae / display "Patients with|Any AE" width=12;
 define pct_ae / display "%" width=8;
 define n_pat_rel / display "Patients with|Treatment-|related AE" width=12;
 define pct_ser / display "%" width=8;
 define n_pat_dc / display "Patients with|AE Leading to|Discontinuation" width=12;
 define pct_dc / display "%" width=8;
 
 title1 "Table 5.3.1";
 title2 "Adverse Events Summary";
 title3 "Safety Analysis Set";
 
 footnote1 "AE = Adverse Event";
 footnote2 "Related = Possibly Related or Related";
run;

ods rtf close;
filename rtfout clear;

%mend t5_ae_summary;
