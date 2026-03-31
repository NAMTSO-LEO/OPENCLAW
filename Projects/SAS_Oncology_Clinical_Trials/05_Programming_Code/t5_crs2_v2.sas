/*soh***************************************************************************
Program name : t5-crs2.sas
Compound : EPCO
Study : M20-621 and GCT3013-02
Milestone : ISS
Description : Create TFL t__5.2.3 - CRS Events Analysis
--------------------------------------------------------------------------------
Details: CRS事件分析表 - 包括发生率、时间分析、等级分布
--------------------------------------------------------------------------------
Program notes:
Author Date Code History Description
------- ------- -----------------------------------------------------------
zhangyx86 20Jan2025 Original
HONGLX1 13NOV2025 Updated
**eoh**************************************************************************/

%init;

%let dtft=date9.;
%let rtyp=TABLE; 
%let groupn=trtn;
%let grpno=7; 
%let ptkey=usubjid; 
%let outputdesc=;

%macro select;
%mend select;

%macro formfoot;
%mend formfoot;
 
%user(prtype=&rtyp,print=YES,bypat=NO);
%create_rtf_style_template(name=RTFSTYLE, parent=RTF);

proc format;
 picture pct (default=7 round fuzz=1e-25)
 low - <0 = '< zero' (noedit)
 0 = ' ' (noedit)
 0< - <0.1 = '(<0.1%)' (noedit)
 0.1 - <100 = '09.9%)' (prefix='(')
 100 = '(100%) ' (noedit)
 100< - high = '009.9%)' (prefix='(')
 other = ' ' (noedit);
 picture pval (default=9 round fuzz=1e-25) 
 0.000 - < 0.001 = '<0.001***' (noedit)
 0.001 - < 0.0104999 = '9.999** '
 0.0104999 - < 0.0504999 = '9.999* '
 0.0504999 - < 0.1004999 = '9.999 '
 0.1004999 - 1.000 = '9.999 '
 low - <0 = '< zero ' (noedit)
 1.000< - high = '> one ' (noedit)
 other = ' - ' (noedit);
run;

************************************************************
 定义分析组别
***********************************************************;

%macro grp;
 /* Group 1: M20-621, TR01AG1N=1, IPIGR1 in (2,3,4,5,4-5) */
 if STUDYID in ("M20-621") and TR01AG1N in (1) and IPIGR1 in ('2','3','4','5','4 - 5') then do;
  &groupn=1;
  output;
 end;
 
 /* Group 2: M20-621, TR01AG1N=2, IPIGR1 in (2,3,4,5,4-5) */
 if STUDYID in ("M20-621") and TR01AG1N in (2) and IPIGR1 in ('2','3','4','5','4 - 5') then do;
  &groupn=2;
  output;
 end;
 
 /* Group 3: GCT3013-02/M20-621, TR01AG1N=1, IPIGR1 in (2,3,4,5,4-5) */
 if STUDYID in ("GCT3013-02","M20-621") and TR01AG1N in (1) and IPIGR1 in ('2','3','4','5','4 - 5') then do;
  &groupn=3;
  output;
 end; 
 
 /* Group 4: M20-621, TR01AG1N=1, IPIGR1 in (3,4,5,4-5) */
 if STUDYID in ("M20-621") and TR01AG1N in (1) and IPIGR1 in ('3','4','5','4 - 5') then do;
  &groupn=4;
  output;
 end;
 
 /* Group 5: M20-621, TR01AG1N=2, IPIGR1 in (3,4,5,4-5) */
 if STUDYID in ("M20-621") and TR01AG1N in (2) and IPIGR1 in ('3','4','5','4 - 5') then do;
  &groupn=5;
  output;
 end;
 
 /* Group 6: GCT3013-02/M20-621, TR01AG1N=1, IPIGR1 in (3,4,5,4-5) */
 if STUDYID in ("GCT3013-02","M20-621") and TR01AG1N in (1) and IPIGR1 in ('3','4','5','4 - 5') then do;
  &groupn=6;
  output;
 end; 
 
 /* Group 7: GCT3013-01/M23-362/GCT3013-05, TR01AG1N=3 */
 if STUDYID in ("GCT3013-01","M23-362","GCT3013-05") and TR01AG1N in (3) then do;
  &groupn=7;
  output;
 end;
%mend;

************************************************************
 获取安全人群受试者数量
***********************************************************;

data adsl;
 set adam.adsl;
 if saffl='Y';
run;

data adsl1;
 set adsl;
 %grp;
run;

proc freq data=adsl1 noprint;
 table &groupn/out=total;
run;

data _null_;
 if _n_=1 then do;
  do i=1 to 7;
   call symput('numd'||strip(put(i,best.)),'0');
  end;
 end;
 set total;
 call symput('numd'||strip(put(&groupn,best.)),compress(put(count,3.)));
run;

%put NOTE: Number of subjects by group: &&numd1 &&numd2 &&numd3 &&numd4 &&numd5 &&numd6 &&numd7;

************************************************************
 获取CRS事件数据 - ADAESI
***********************************************************;

data adaesi;
 set adam.adaesi;
 
 /* 筛选CRS事件 */
 if CRSFL='Y' and trtemfl='Y' and aesicat in ('CYTOKINE RELEASE SYNDROME' 'CRS') and aeptcd in (10052015, 10050685);
 
 /* 转换毒性等级为数值 */
 if ATOXGR='Grade 1' then ATOXGRN=1;
 else if ATOXGR='Grade 2' then ATOXGRN=2;
 else if ATOXGR='Grade 3' then ATOXGRN=3;
 else if ATOXGR='Grade 4' then ATOXGRN=4;
 else if ATOXGR='Grade 5' then ATOXGRN=5;
 else put "Warning: check value for ATOXGR." &ptkey ATOXGR=;
 
 rename ACRSTFL=atocfl;
run;

/* 验证数据 */
proc print data=adaesi (obs=10);
 title "CRS Events Data";
run;

************************************************************
 合并组别信息
***********************************************************;

proc sql;
 create table adaesi1 as
 select a.*, b.&groupn
 from adaesi a
 left join adsl1 b
 on a.usubjid=b.usubjid;
quit;

************************************************************
 Part 1: CRS发生率分析
***********************************************************;

proc sql;
 create table crs_inc as
 select &groupn,
        count(distinct usubjid) as n_pat,
        count(*) as n_evt
 from adaesi1
 group by &groupn;
quit;

/* 计算各组发生率 */
data crs_inc_rate;
 set crs_inc;
 retain cum_n 0;
 
 /* 合并受试者数量 */
 if &groupn=1 then denom=&&numd1;
 else if &groupn=2 then denom=&&numd2;
 else if &groupn=3 then denom=&&numd3;
 else if &groupn=4 then denom=&&numd4;
 else if &groupn=5 then denom=&&numd5;
 else if &groupn=6 then denom=&&numd6;
 else if &groupn=7 then denom=&&numd7;
 
 pct = n_pat / denom * 100;
 
 format pct pct.;
run;

proc print data=crs_inc_rate;
 title "CRS Incidence by Group";
run;

************************************************************
 Part 2: CRS等级分布
***********************************************************;

proc freq data=adaesi1 noprint;
 table &groupn*ATOXGRN / out=grade_dist;
run;

proc transpose data=grade_dist out=grade_pivot;
 by &groupn;
 id ATOXGRN;
 var count;
run;

************************************************************
 Part 3: CRS时间分析
***********************************************************;

proc sql;
 create table crs_tte as
 select &groupn,
        min(ASTDY) as first_crs_day,
        max(ASTDY) as last_crs_day,
        mean(ASTDY) as mean_crs_day,
        min(ASTDY) as min_tox_day,
        max(ASTDY) as max_tox_day
 from adaesi1
 group by &groupn;
quit;

proc print data=crs_tte;
 title "CRS Time to Onset";
run;

************************************************************
 Part 4: ICANS分析 (如果需要)
***********************************************************;

data adainsi;
 set adam.adaesi;
 if CRSEFL='Y' and trtemfl='Y' and aesicat in ('ICANS' 'IMMUNE EFFECTOR CELL-ASSOCIATED NEUROTOXICITY SYNDROME');
run;

proc freq data=adainsi noprint;
 table &groupn*ATOXGRN / out=icans_grade;
run;

************************************************************
 生成TLF输出
***********************************************************;

/* Table 5.2.3: CRS Events Summary */
proc report data=crs_inc_rate nowd split='|';
 columns &groupn n_pat denom pct n_evt;
 
 define &groupn / display "Treatment|Group" width=15;
 define n_pat / display "Number of|Patients with|CRS" width=12;
 define denom / display "Number of|Patients" width=12;
 define pct / display "% of|Patients" width=10;
 define n_evt / display "Number of|CRS Events" width=12;
 
 compute pct;
  if pct.s >= 20 then call define(_col_,"style","style=[foreground=red]");
 endcomp;
 
 title1 "Table 5.2.3";
 title2 "Cytokine Release Syndrome (CRS) - Summary by Treatment Group";
 title3 "Safety Analysis Set";
 
 footnote1 "Note: CRS events defined as events with MedDRA PT in (Cytokine Release Syndrome, CRS)";
 footnote2 "Percentages are calculated based on the number of patients in each treatment group.";
run;

************************************************************
 输出到RTF
***********************************************************;

filename rtfout "&outpath./t5_crs2.rtf";
ods rtf file=rtfout style=RTFSTYLE;

proc report data=crs_inc_rate nowd split='|';
 /* Report code here */
run;

ods rtf close;
filename rtfout clear;

%mend t5_crs2;

/* Run the program */
%t5_crs2;
