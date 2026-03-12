/*soh***************************************************************************
Program name : t5_crs_comprehensive.sas
Compound : EPCO (Epcoritamab)
Study : M20-621, M23-362, GCT3013-01/02/05
Milestone : ISS
Description : Create TFL t5.2.3 - CRS Comprehensive Analysis
--------------------------------------------------------------------------------
Details: CRS综合分析 - 发生率、等级、发作时间、治疗、缓解时间
--------------------------------------------------------------------------------
Author : 
Date : 
**eoh**************************************************************************/

%init;
%let outpath=/sasdata/iss/output;
%let groupn=trtn;
%let grpno=7;

************************************************************
 定义治疗组宏
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
 Step 1: 获取ADAESI数据
***********************************************************;
proc sql;
 create table ana0 as
 select a.*, b.&groupn
 from adam.adaesi a
 inner join adam.adsl b
 on a.usubjid=b.usubjid
 where a.CRSFL='Y' and a.trtemfl='Y';
quit;

proc sort data=ana0 nodupkey out=subject;
 by &groupn usubjid;
run;

proc freq data=subject noprint;
 table &groupn/out=total_s;
run;

************************************************************
 Step 2: CRS事件详细数据
***********************************************************;
data ana;
 set ana0;
 
 /* 排序变量 - 等级 */
 ord=1; ord1=1;
 if ATOXGRN=1 then do;ord=1;ord1=1;output;end;
 if ATOXGRN=2 then do;ord=1;ord1=2;output;end;
 if ATOXGRN=3 then do;ord=1;ord1=3;output;end;
 if ATOXGRN=4 then do;ord=1;ord1=4;output;end;
 if ATOXGRN=5 then do;ord=1;ord1=5;output;end;
 
 /* ANL40FL - Cycle 1 */
 if ANL40FL='Y' then do;ord=1.5; ord1=1;output;end;
 
 /* CRS症状 - Fever, Hypotension, Hypoxia, Other */
 if ceterm1>'' or ceterm2>'' or ceterm3>'' or ceterm4>'' then do;ord=2;ord1=.;output;end;
 if index(ceterm1,'Fever') then do;ord=2;ord1=1;output;end;
 if index(ceterm2,'Hypotension') then do;ord=2;ord1=2;output;end;
 if index(ceterm3,'Hypoxia') then do;ord=2;ord1=3;output;end;
 if index(ceterm4,'Other') then do;ord=2;ord1=4;output;end;
 
 /* 治疗 */
 if ANTICYFL='Y' then do;ord=3;ord1=1;output;end;
 if ATOCFL='Y' then do;ord=3;ord1=2;output;end;
 if ANTOCFL='Y' then do;ord=3;ord1=3;output;end;
 if ACORTFL='Y' then do;ord=3;ord1=4;output;end;
 if TEDSINFL='Y' then do;ord=3;ord1=5;output;end;
 if TEDISEPC='Y' then do;ord=3;ord1=6;output;end;
run;

************************************************************
 Step 3: 事件次数统计
***********************************************************;
proc sql;
 create table episodes as 
 select count(*) as count, &groupn, usubjid
 from ana
 group by &groupn, usubjid;
quit;

/* 发作次数分类 */
data episodes1;
 set episodes;
 ord=-1; ord1=1; output;
 if count=1 then do; ord=0; ord1=1; output; end;
 if count>=2 then do; ord=0; ord1=2; output; end;
 if count=2 then do; ord=0; ord1=3; output; end;
 if count=3 then do; ord=0; ord1=4; output; end;
 if count=4 then do; ord=0; ord1=5; output; end;
 if count=5 then do; ord=0; ord1=6; output; end;
 if count=6 then do; ord=0; ord1=7; output; end; 
 if count=10 then do; ord=0; ord1=10; output; end;
run;

proc sql noprint;
 create table dataset1 as
 select count(distinct usubjid) as count, &groupn, ord, ord1
 from episodes1
 group by &groupn, ord, ord1
 order by &groupn, ord, ord1;
quit;

************************************************************
 Step 4: CRS症状汇总
***********************************************************;
proc sql noprint;
 create table dataset as
 select count(*) as count, &groupn, ord, ord1
 from ana
 group by &groupn, ord, ord1
 order by &groupn, ord, ord1;
 
 /* 总事件数 */
 create table total_e as
 select count(*) as total_e, &groupn
 from ana
 group by &groupn
 order by &groupn;
quit;

************************************************************
 Step 5: 合并所有数据
***********************************************************;
data dataset;
 set dataset dataset1;
run;

/* 创建模板 */
proc sort data=dataset out=dummy(keep=ord ord1) nodupkey;
 by ord ord1;
run;

data dummy;
 set dummy;
 do &groupn=1 to 7;
 output;
 end;
run;

proc sort data=dummy;
 by &groupn ord ord1;
run;

proc sort data=dataset;
 by &groupn ord ord1;
run;

data dataset;
 merge dummy(in=a) dataset;
 by &groupn ord ord1;
 if a;
run;

************************************************************
 Step 6: 关联"Other"事件
***********************************************************;
/* 获取CE数据 - Other事件 */
data ce1 ce2 ce3 ce4 cegct;
 set adam.adce;
 if aesicat in ('CYTOKINE RELEASE SYNDROME' 'CRS'); 
 cedecod=upcase(cedecod);
 if upcase(cedecod) not in ('PYREXIA' 'FEVER' 'HYPOTENSION' 'HYPOXIA') or index(ceterm,'OTHER');
 if cedecod='' then cedecod='*** Not coded ***';
 
 if studyid in ("M20-621" "M23-362") then do;
  if aerefid1 ne '' then output ce1;
  if aerefid2 ne '' then output ce2;
  if aerefid3 ne '' then output ce3;
  if aerefid4 ne '' then output ce4;
 end;
 else output cegct;
run;

/* 合并refid */
data ce0;
 length cedecod $200;
 set ce1(rename=(aerefid1=aerefid)) 
      ce2(rename=(aerefid2=aerefid)) 
      ce3(rename=(aerefid3=aerefid)) 
      ce4(rename=(aerefid4=aerefid)); 
 if upcase(ceterm) not in ('PYREXIA' 'FEVER' 'HYPOTENSION' 'HYPOXIA') or index(upcase(ceterm),'OTHER');
 cedecod=ceterm; 
 keep studyid usubjid subjid cedecod aerefid;
run;

proc sort data=ce0 nodupkey out=ce_comb;
 by studyid usubjid cedecod aerefid;
run;

/* 关联治疗组 */
proc sql;
 create table crs_other as
 select distinct a.&groupn, b.cedecod
 from ana0 a
 inner join ce_comb b
 on a.usubjid=b.usubjid and a.grpnum=input(b.aerefid, best.)
 where a.CRSFL='Y';
quit;

/* 添加到汇总 */
proc sql;
 create table crs_other_count as
 select &groupn, cedecod, count(*) as count
 from crs_other
 group by &groupn, cedecod;
quit;

************************************************************
 Step 7: 格式化输出
***********************************************************;
proc sort data=total_e;
 by &groupn;
run;

proc sort data=total_s;
 by &groupn;
run;

proc sort data=dataset;
 by &groupn;
run;

data all;
 merge dataset total_e total_s(rename=(count=total_s));
 by &groupn;
 length _count $200.;
 if count=. then count=0;
 
 /* 发作次数: n (%) */
 if ord=-1 or (ord in (1) and ord1=.) then _count=strip(put(count,best.));
 /* 发作次数分类: n (%) */
 else if ord=0 then _count=strip(put(count,3.))||''||strip(put(count/total_s*100,pct.));
 /* 其他: n (%) */
 else _count=strip(put(count,3.))||''||strip(put(count/total_e*100,pct.));
run;

************************************************************
 Step 8: 时间分析 - CRS发作时间
***********************************************************;
%macro ONSET(para=,tab=);
data adsaftte0;
 set adam.adsaftte;
 where paramcd=&para and TRTEMFL='Y';
run;

data adsaftte0;
 merge adsaftte0(in=a) adsl(in=b);
 by usubjid;
 if a and b;
 %grp;
run;

proc means data=adsaftte0 noprint;
 where &groupn>.;
 class &groupn;
 var aval;
 output out=means n=num mean=mean_ std=std median=median min=min max=max;
run;

data means1;
 length n meansd med range $200;
 set means;
 %if &tab=1 %then %do; ord=3.9; %end;
 %if &tab=2 %then %do; ord=4; %end;
 n=strip(put(num,4.));
 if mean_>. and std>. then meansd=strip(put(mean_,10.1))||' ('||strip(put(std,10.2))||")";
 else if mean_>. and std=. then meansd=strip(put(mean_,10.1))||' (N/A)';
 med=strip(put(median,10.1));
 if 0<min<1 then range='<1, '||strip(put(max,10.0));
 else if min>. and max>. then range=strip(put(min,10.0))||', '||strip(put(max,10.0));
 if &groupn>.;
run;

proc sort data=means1;
 by ord;
 where &groupn>.;
run;

proc transpose data=means1 out=means&tab prefix=result;
 id &groupn;
 var n meansd med range;
 by ord;
run;
%mend;

%ONSET(tab=1,para="CRSDURH");  /* 小时 */
%ONSET(tab=2,para="CRSDURD");  /* 天 */

************************************************************
 Step 9: 时间分析 - CRS缓解时间
***********************************************************;
data adsaftte;
 set adam.adsaftte;
 where paramcd='CRSRSD' and trtemfl='Y' and cnsr=0;
run;

data adsaftte1;
 merge adsaftte(in=a) adsl(in=b);
 by usubjid;
 if a and b;
 %grp;
run;

proc means data=adsaftte1 noprint;
 class &groupn;
 var aval;
 output out=means_ mean=mean_ std=std median=median min=min max=max;
run;

data means_1;
 length meansd med range $200;
 set means_;
 ord=5;
 if mean_>. and std>. then meansd=strip(put(mean_,10.1))||' ('||strip(put(std,10.2))||")";
 else if mean_>. and std=. then meansd=strip(put(mean_,10.1))||' (N/A)';
 med=strip(put(median,10.1));
 if 0<min<1 then range='<1, '||strip(put(max,10.0));
 else if min>. and max>. then range=strip(put(min,10.0))||', '||strip(put(max,10.0));
run;

proc sort data=means_1;
 by ord;
run;

proc transpose data=means_1 out=means_res prefix=result;
 id &groupn;
 var meansd med range;
 by ord;
run;

/* 缓解计数 */
proc sql noprint;
 create table resolve as
 select count(*) as count, &groupn
 from adsaftte1
 where cnsr=0
 group by &groupn;
 
 create table events as
 select count(*) as total, &groupn
 from ana
 group by &groupn;
quit;

data all_res;
 merge resolve events;
 by &groupn;
 length _count $200.;
 if count>. then _count=strip(put(count,3.))||''||strip(put(count/total*100,pct.));
 else _count='0';
run;

proc transpose data=all_res out=all_res1 prefix=result;
 id &groupn;
 var _count;
run;

************************************************************
 Step 10: 创建行标签模板
***********************************************************;
data dummy;
 length rowlbl $200.;
 ord=-1; ord1=1; rowlbl='Subjects with at least one CRS event'; output;
 ord=0; ord1=0; rowlbl='Number of episodes per subject [a]'; output;
 ord=0; ord1=1; rowlbl=' 1 event'; output;
 ord=0; ord1=2; rowlbl=' >=2 events'; output;
 ord=0; ord1=3; rowlbl=' 2 events'; output;
 ord=0; ord1=4; rowlbl=' 3 events'; output;
 ord=0; ord1=5; rowlbl=' 4 events'; output;
 ord=0; ord1=6; rowlbl=' 5 events'; output;
 ord=0; ord1=10; rowlbl=' 10 events'; output;
 ord=1; ord1=0.5; rowlbl='Number of CRS events'; output;
 ord=1; ord1=1; rowlbl=' Grade 1'; output;
 ord=1; ord1=2; rowlbl=' Grade 2'; output;
 ord=1; ord1=3; rowlbl=' Grade 3'; output;
 ord=1; ord1=4; rowlbl=' Grade 4'; output;
 ord=1; ord1=5; rowlbl=' Grade 5'; output;
 ord=1.5; ord1=1; rowlbl=' Number of CRS events in Cycle 1 [b]'; output;
 ord=2; ord1=0.5; rowlbl='Occurrence of any CRS signs and symptoms'; output;
 ord=2; ord1=1; rowlbl=' Fever'; output;
 ord=2; ord1=2; rowlbl=' Hypotension'; output;
 ord=2; ord1=3; rowlbl=' Hypoxia'; output;
 ord=2; ord1=4; rowlbl=' Other'; output;
 ord=3; ord1=0.5; rowlbl='CRS event'; output;
 ord=3; ord1=1; rowlbl=' Treated with anti-cytokine therapy'; output;
 ord=3; ord1=2; rowlbl=' Tocilizumab'; output;
 ord=3; ord1=3; rowlbl=' Other anti-cytokine'; output;
 ord=3; ord1=4; rowlbl=' Treated with corticosteroid for CRS'; output;
 ord=3; ord1=5; rowlbl=' Leading to epcoritamab dose delay'; output;
 ord=3; ord1=6; rowlbl=' Leading to epcoritamab discontinuation'; output;
 ord=3.9; ord1=0.5; rowlbl='Time to CRS onset from epcoritamab most recent dosing (hours)'; output;
 ord=3.9; ord1=1; rowlbl=' n'; output;
 ord=3.9; ord1=2; rowlbl=' Mean (Std Dev)'; output;
 ord=3.9; ord1=3; rowlbl=' Median'; output;
 ord=3.9; ord1=4; rowlbl=' Min, Max'; output;
 ord=4; ord1=0.5; rowlbl='Time to CRS onset from epcoritamab most recent dosing (days)'; output;
 ord=4; ord1=1; rowlbl=' n'; output;
 ord=4; ord1=2; rowlbl=' Mean (Std Dev)'; output;
 ord=4; ord1=3; rowlbl=' Median'; output;
 ord=4; ord1=4; rowlbl=' Min, Max'; output;
 ord=5; ord1=0.5; rowlbl='Time to CRS resolution (days)'; output;
 ord=5; ord1=1; rowlbl=' Resolved CRS'; output;
 ord=5; ord1=2; rowlbl=' Mean (Std Dev)'; output;
 ord=5; ord1=3; rowlbl=' Median'; output;
 ord=5; ord1=4; rowlbl=' Min, Max'; output;
run;

proc sort data=dummy;
 by ord ord1;
run;

************************************************************
 Step 11: 合并所有数据
***********************************************************;
data final_;
 set all means1 means2 means_res all_res1;
 if ord=. and ord1=. and lowcase(_name_)='_count' then do; ord=5; ord1=1; end;
 if ord in (3.9 4) and lowcase(_name_)='n' then ord1=1;
 if ord in (3.9 4 5) and lowcase(_name_)='meansd' then ord1=2;
 if ord in (3.9 4 5) and lowcase(_name_)='med' then ord1=3;
 if ord in (3.9 4 5) and lowcase(_name_)='range' then ord1=4;
 if ord=. then ord =0.5;
 if ord1=. then ord1=0.5;
run;

proc sort data=final_;
 by ord ord1;
run;

data final;
 set final_;
 sortord1=ord;
 sortord2=ord1;
 array result[&grpno];
 do i=1 to &grpno;
  if sortord1 in (0) and sortord2 in (7 10) and result(i)='' then result(i)='0';
  if sortord1 in (1) and sortord2=5 and result(i)='' then result(i)='0';
  if sortord1 in (3) and sortord2=6 and result(i)='' then result(i)='0'; 
  if sortord1 in (0.5) then result(i)=' ';
 end;
 
 /* 特殊处理 */
 if index(rowlbl,'Leading to epcoritamab dose delay') or 
    index(rowlbl,'Leading to epcoritamab discontinuation') then result2='N/A'; 
run;

proc sort data=final;
 by sortord1 sortord2;
run;

************************************************************
 Step 12: 输出RTF
***********************************************************;
filename rtfout "&outpath./t5_crs_comprehensive.rtf";
ods rtf file=rtfout style=RTFSTYLE;

proc report data=final missing nowd split='\' 
 style(report)={width=100%}
 style(header)={just=l}
 style(column)={just=c};
 
 column sortord1 sortord2 rowlbl 
  ("Treatment Group" result1 result2 result3 result4 result5 result6 result7);
 
 define sortord1 / order noprint;
 define sortord2 / order noprint;
 define rowlbl / order flow style=[width=30%] " ";
 define result1 / display style=[width=10%] "Epco+R-CHOP (N=&numd1)";
 define result2 / display style=[width=10%] "R-CHOP (N=&numd2)";
 define result3 / display style=[width=10%] "Pooled (N=&numd3)";
 define result4 / display style=[width=10%] "Epco+R-CHOP IPI3-5 (N=&numd4)";
 define result5 / display style=[width=10%] "R-CHOP IPI3-5 (N=&numd5)";
 define result6 / display style=[width=10%] "Pooled IPI3-5 (N=&numd6)";
 define result7 / display style=[width=10%] "Epco Mono (N=&numd7)";
 
 title1 "Table 5.2.3";
 title2 "Cytokine Release Syndrome (CRS) - Summary";
 title3 "Safety Analysis Set";
 
 footnote1 "[a] Percentages based on number of subjects with at least one CRS event";
 footnote2 "[b] CRS events occurring in Cycle 1";
run;

ods rtf close;
filename rtfout clear;

%mend t5_crs_comprehensive;
