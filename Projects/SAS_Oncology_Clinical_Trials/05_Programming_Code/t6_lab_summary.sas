/*soh***************************************************************************
Program name : t6_lab_summary.sas
Compound : EPCO
Study : M20-621 and GCT3013-02 (ISS)
Milestone : ISS
Description : Create TFL t6.1 - Laboratory Abnormalities Summary
--------------------------------------------------------------------------------
Details: 实验室检查异常汇总 - 按CTCAE分级
--------------------------------------------------------------------------------
**eoh**************************************************************************/

%init;

%let outpath=/sasdata/iss/output;

************************************************************
 获取实验室数据
***********************************************************;

data adlb;
 set adam.adlb;
 if saffl='Y' andylan='Y';
run;

/* 获取基线和治疗期间最大值 */
proc sql;
 create table lb_baseline as
 select usubjid, lbtcid, lbtest, lbstress, lbstresn as base_lb,
        lbblfl
 from adlb
 where lbblfl='Y';
quit;

proc sql;
 create table lb_post as
 select usubjid, lbtcid, lbtest, lbstress, lbstresn as post_lb,
        lbdtc, aycnt
 from adlb
 where lbblfl='N';
quit;

/* 合并基线和治疗后值 */
proc sql;
 create table lb_change as
 select a.*, b.post_lb, b.aycnt as post_visit
 from lb_baseline a
 left join lb_post b
 on a.usubjid=b.usubjid and a.lbtcid=b.lbtcid;
quit;

/* 计算变化 */
data lb_change2;
 set lb_change;
 if not missing(base_lb) and not missing(post_lb) then do;
  change = post_lb - base_lb;
  pct_change = change / base_lb * 100;
 end;
run;

************************************************************
 按分级汇总 (CTCAE)
***********************************************************;

/* 获取毒性分级 */
proc sql;
 create table lb_grade as
 select usubjid, lbtcid, lbtest, lbstress, 
        lbstresn, lbstrnlo, lbstrnhi, lbtoxgr,
        case 
         when lbtoxgr='1' then 1
         when lbtoxgr='2' then 2
         when lbtoxgr='3' then 3
         when lbtoxgr='4' then 4
         when lbtoxgr='5' then 5
        end as lbtoxgrn
 from adlb
 where not missing(lbtoxgr);
quit;

/* 按测试和分级汇总 */
proc freq data=lb_grade noprint;
 table lbtcid*lbtoxgrn / out=lb_grade_freq;
run;

/* 转为横向表 */
proc transpose data=lb_grade_freq out=lb_grade_pivot;
 by lbtcid;
 id lbtoxgrn;
 var count;
run;

************************************************************
 特定实验室指标分析
***********************************************************;

/* 血液学 */
proc sql;
 create table hem_lb as
 select lbtcid, count(distinct usubjid) as n,
        count(case when lbtoxgrn>=3 then 1 end) as n_gr34,
        count(case when lbtoxgrn>=4 then 1 end) as n_gr4
 from lb_grade
 where lbtcid in ('HEMOGLOBIN','NEUTROPHILS','PLATELETS','LYMPHOCYTES')
 group by lbtcid;
quit;

/* 生化 */
proc sql;
 create table chem_lb as
 select lbtcid, count(distinct usubjid) as n,
        count(case when lbtoxgrn>=3 then 1 end) as n_gr34,
        count(case when lbtoxgrn>=4 then 1 end) as n_gr4
 from lb_grade
 where lbtcid in ('ALT','AST','BILIRUBIN','CREATININE','SODIUM','POTASSIUM')
 group by lbtcid;
quit;

/* 肝功能 */
proc sql;
 create table hepatic_ae as
 select usubjid, lbtcid, max(lbtoxgrn) as max_gr
 from lb_grade
 where lbtcid in ('ALT','AST','BILIRUBIN')
 group by usubjid, lbtcid;
quit;

/* Hy's Law 分析 */
proc sql;
 create table hys_law as
 select usubjid
 from hepatic_ae
 group by usubjid
 having max(max_gr) >= 3 and count(distinct case when lbtcid='BILIRUBIN' and max_gr>=3 then 1 end) >= 1
        and count(distinct case when lbtcid in ('ALT','AST') and max_gr>=3 then 1 end) >= 1;
quit;

proc sql;
 create table hys_law_summary as
 select a.lbtcid, count(distinct a.usubjid) as n_pat,
        count(distinct case when a.max_gr>=3 then a.usubjid end) as n_gr34,
        (calculated n_gr34 / count(distinct a.usubjid) * 100) as pct_gr34
 from hepatic_ae a
 group by a.lbtcid;
quit;

proc print data=hys_law_summary;
 title "Hy's Law Analysis";
run;

************************************************************
 输出RTF
***********************************************************;

filename rtfout "&outpath./t6_lab_summary.rtf";
ods rtf file=rtfout style=styles.rtf;

proc report data=hys_law_summary split='|';
 columns lbtcid n_pat n_gr34 pct_gr34;
 
 define lbtcid / display "Laboratory Test" width=20;
 define n_pat / display "Number of|Patients" width=12;
 define n_gr34 / display "Grade 3-4|Abnormalities" width=12;
 define pct_gr34 / display "%" width=8;
 
 title1 "Table 6.1";
 title2 "Laboratory Abnormalities - Hy's Law Analysis";
 title3 "Safety Analysis Set";
run;

ods rtf close;
filename rtfout clear;

%mend t6_lab_summary;
