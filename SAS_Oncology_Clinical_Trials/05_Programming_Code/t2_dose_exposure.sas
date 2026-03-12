/*soh***************************************************************************
Program name : t2_dose_exposure.sas
Compound : EPCO (Epcoritamab)
Study : M20-621, GCT3013-02, M23-362, GCT3013-01/05
Milestone : ISS
Description : Create TFL t2.x.x - Dose Exposure Analysis
--------------------------------------------------------------------------------
Details: 剂量暴露分析 - 治疗持续时间、剂量强度、治疗周期
--------------------------------------------------------------------------------
**eoh**************************************************************************/

%init;
%let rtyp=TABLE;
%user(PRTYPE=&RTYP);
%create_rtf_style_template(name=RTFSTYLE, parent=RTF);

%let groupn=trtn;
%let grpno=7;
%let outputdesc=;
%let open=N;
%let ptkey=usubjid;

proc format;
 picture pct (default=8 round fuzz=1e-25)
 low - <0 = '< ZERO' (noedit)
 0 = ' ' (noedit)
 0< - <0.1 = '(<0.1%)' (noedit)
 0.1 - <100 = '09.9%)' (prefix='(')
 100 = '(100%) ' (noedit)
 100< - high = '009.9%)' (prefix='(')
 other = ' ' (noedit);
run;

************************************************************
 定义治疗组
***********************************************************;
%macro grp;
 if STUDYID in ("M20-621") and TR01AG1N in (1) and IPIGR1 in ('2','3','4','5','4 - 5') then do; &groupn=1; output; end;
 if STUDYID in ("M20-621") and TR01AG1N in (2) and IPIGR1 in ('2','3','4','5','4 - 5') then do; &groupn=2; output; end;
 if STUDYID in ("GCT3013-02","M20-621") and TR01AG1N in (1) and IPIGR1 in ('2','3','4','5','4 - 5') then do; &groupn=3; output; end;
 if STUDYID in ("M20-621") and TR01AG1N in (1) and IPIGR1 in ('3','4','5','4 - 5') then do; &groupn=4; output; end;
 if STUDYID in ("M20-621") and TR01AG1N in (2) and IPIGR1 in ('3','4','5','4 - 5') then do; &groupn=5; output; end;
 if STUDYID in ("GCT3013-02","M20-621") and TR01AG1N in (1) and IPIGR1 in ('3','4','5','4 - 5') then do; &groupn=6; output; end;
 if STUDYID in ("GCT3013-01","M23-362","GCT3013-05") and TR01AG1N in (3) then do; &groupn=7; output; end;
%mend;

************************************************************
 Step 1: 获取安全人群
***********************************************************;
data adsl;
 set adam.adsl;
 if saffl='Y';
run;

data pop1;
 set adsl;
 %grp;
run;

proc sql noprint;
 select count(unique(usubjid)) into: n1 from pop1 where &groupn=1;
 select count(unique(usubjid)) into: n2 from pop1 where &groupn=2;
 select count(unique(usubjid)) into: n3 from pop1 where &groupn=3;
 select count(unique(usubjid)) into: n4 from pop1 where &groupn=4;
 select count(unique(usubjid)) into: n5 from pop1 where &groupn=5;
 select count(unique(usubjid)) into: n6 from pop1 where &groupn=6;
 select count(unique(usubjid)) into: n7 from pop1 where &groupn=7;
quit;

%put NOTE: Subject counts: n1=&n1, n2=&n2, n3=&n3, n4=&n4, n5=&n5, n6=&n6, n7=&n7;

proc sql;
 create table pop2 as 
 select &groupn, count(distinct USUBJID) as tot 
 from pop1 
 group by &groupn;
quit;

************************************************************
 Step 2: 获取暴露数据 (ADEX)
***********************************************************;
data adex;
 set adam.adex;
run;

/* 筛选特定治疗药物 */
data ex;
 merge adex(in=a) adsl(in=b keep=usubjid studyid ipigr1 tr01ag1n);
 by usubjid;
 if a and b;
 %grp;
run;

/* 剂量调整分析 */
data ex_adj;
 set ex;
 if EXDELADJ ne '' then do;
  if EXDELADJ='Adverse Event' then exadj=EXDELADJ;
  else exadj='Other';
 end;
run;

/* 按组汇总剂量调整 */
proc freq data=ex_adj noprint;
 table &groupn*exadj / out=ex_adj_freq;
run;

************************************************************
 Step 3: 获取暴露汇总数据 (ADEXSUM)
***********************************************************;
data exsum1;
 merge adam.adexsum(in=a) adam.adsl(in=b keep=usubjid studyid ipigr1 tr01ag1n);
 by usubjid;
 if a;
 %grp;
run;

/* 扩展周期数据 */
data exsum_cycles;
 set exsum1;
 where paramcd='NUMCYCL'; /* 治疗周期数 */
 if aval > 1 then do;
  do i=1 to aval;
   cycle=i;
   output;
  end;
 end;
 else do;
  cycle=aval;
  output;
 end;
run;

/* 剂量延迟数据 */
data exsum_delay;
 set exsum1;
 where paramcd='DOSDL'; /* 剂量延迟 */
 if aval > 1 then do;
  do i=1 to aval;
   delay_num=i;
   output;
  end;
 end;
 else do;
  delay_num=aval;
  output;
 end;
run;

************************************************************
 Step 4: 分析 - 治疗周期数
***********************************************************;
proc sql;
 create table cycles_summary as
 select &groupn,
        count(distinct usubjid) as n_pat,
        mean(aval) as mean_cycles,
        median(aval) as median_cycles,
        min(aval) as min_cycles,
        max(aval) as max_cycles
 from exsum1
 where paramcd='NUMCYCL'
 group by &groupn;
quit;

proc print data=cycles_summary;
 title "Treatment Cycles Summary";
run;

************************************************************
 Step 5: 分析 - 相对剂量强度
***********************************************************;
proc sql;
 create table dose_intensity as
 select &groupn,
        count(distinct usubjid) as n_pat,
        mean(aval) as mean_rdi,
        median(aval) as median_rdi
 from exsum1
 where paramcd='RELDOSE' /* 相对剂量强度 */
 group by &groupn;
quit;

************************************************************
 Step 6: 分析 - 治疗持续时间
***********************************************************;
proc sql;
 create table treatment_duration as
 select &groupn,
        count(distinct usubjid) as n_pat,
        mean(aval) as mean_dur,
        median(aval) as median_dur,
        min(aval) as min_dur,
        max(aval) as max_dur
 from exsum1
 where paramcd='DURDAY' /* 治疗持续天数 */
 group by &groupn;
quit;

************************************************************
 Step 7: 分析 - 剂量调整
***********************************************************;
proc sql;
 create table dose_mod as
 select &groupn, exadj,
        count(distinct usubjid) as n_pat
 from ex_adj
 where exadj ne ''
 group by &groupn, exadj;
quit;

/* 转为横向 */
proc transpose data=dose_mod out=dose_mod_pivot;
 by &groupn;
 id exadj;
 var n_pat;
run;

************************************************************
 Step 8: 输出表格
***********************************************************;
/* Table: Treatment Exposure Summary */
proc report data=cycles_summary nowd split='|';
 columns &groupn n_pat mean_cycles median_cycles min_cycles max_cycles;
 
 define &groupn / display "Treatment|Group" width=10;
 define n_pat / display "N" width=8;
 define mean_cycles / display "Mean" width=10;
 define median_cycles / display "Median" width=10;
 define min_cycles / display "Min" width=8;
 define max_cycles / display "Max" width=8;
 
 title1 "Table 2.x.x";
 title2 "Treatment Exposure Summary";
 title3 "Safety Analysis Set";
 
 footnote1 "Only includes subjects who received at least one dose";
run;

************************************************************
 输出RTF
***********************************************************;
filename rtfout "&outpath./t2_dose_exposure.rtf";
ods rtf file=rtfout style=RTFSTYLE;

proc report data=cycles_summary nowd split='|';
 columns &groupn n_pat mean_cycles median_cycles min_cycles max_cycles;
 
 define &groupn / display "Treatment|Group" width=10;
 define n_pat / display "N" width=8;
 define mean_cycles / display "Mean" width=10;
 define median_cycles / display "Median" width=10;
 define min_cycles / display "Min" width=8;
 define max_cycles / display "Max" width=8;
 
 title1 "Table 2.x.x";
 title2 "Treatment Exposure - Number of Cycles";
 title3 "Safety Analysis Set";
run;

ods rtf close;
filename rtfout clear;

%mend t2_dose_exposure;

/* 运行程序 */
%t2_dose_exposure;
