/*soh***************************************************************************
Program name : t7_efficacy.sas
Compound : EPCO
Study : M20-621 and GCT3013-02 (ISS)
Milestone : ISS
Description : Create TFL t7.1 - Efficacy Analysis
--------------------------------------------------------------------------------
Details: 疗效分析 - ORR, DCR, DoR, PFS, OS
--------------------------------------------------------------------------------
**eoh**************************************************************************/

%init;

%let outpath=/sasdata/iss/output;

************************************************************
 获取疗效数据
***********************************************************;

data adtt;
 set adam.adtt; /* Time-to-event */
 where ittfl='Y';
run;

data adrs;
 set adam.adrs; /* Response */
 where ittfl='Y';
run;

************************************************************
 ORR分析 (Overall Response Rate)
***********************************************************;

/* 最佳总体疗效 */
proc sql;
 create table best_resp as
 select usubjid, trta, 
        max(case when rsresp in ('CR','PR') then 1 else 0 end) as best_resp,
        max(case when rsresp='CR' then 1 else 0 end) as best_cr,
        max(case when rsresp='PR' then 1 else 0 end) as best_pr,
        max(case when rsresp='SD' then 1 else 0 end) as best_sd,
        max(case when rsresp='PD' then 1 else 0 end) as best_pd,
        max(case when rsresp='NE' then 1 else 0 end) as best_ne
 from adrs
 group by usubjid, trta;
quit;

/* 计算ORR */
proc sql;
 create table orr_summary as
 select trta,
        count(*) as n,
        sum(best_resp) as n_resp,
        sum(best_cr) as n_cr,
        sum(best_pr) as n_pr,
        sum(best_sd) as n_sd,
        sum(best_pd) as n_pd,
        (sum(best_resp) / count(*)) * 100 as orr,
        (sum(best_cr) / count(*)) * 100 as cr_rate,
        (sum(best_pr) / count(*)) * 100 as pr_rate
 from best_resp
 group by trta;
quit;

proc print data=orr_summary;
 title "Overall Response Rate (ITT)";
run;

************************************************************
 DCR分析 (Disease Control Rate)
***********************************************************;

proc sql;
 create table dcr_summary as
 select trta,
        count(*) as n,
        sum(case when best_resp=1 or best_sd=1 then 1 else 0 end) as n_dcr,
        (sum(case when best_resp=1 or best_sd=1 then 1 else 0 end) / count(*)) * 100 as dcr
 from best_resp
 group by trta;
quit;

************************************************************
 DoR分析 (Duration of Response)
***********************************************************;

/* 仅对CR/PR患者分析 */
proc sql;
 create table dor_data as
 select usubjid, trta, rsstdtc, rslstdtc
 from adrs
 where rsresp in ('CR','PR') and rslstdtc^='';
quit;

/* 计算DoR */
data dor_data2;
 set dor_data;
 format rslstdat yymmdd10.;
 rslstdat = input(rslstdtc, yymmdd10.);
 rsstdat = input(rsstdtc, yymmdd10.);
 dor = rslstdat - rsstdat;
run;

proc means data=dor_data2 mean median min max;
 var dor;
 class trta;
 title "Duration of Response (Months)";
run;

************************************************************
 PFS分析 (Progression-Free Survival)
***********************************************************;

proc lifetest data=adtt timelist=0 3 6 9 12 15 18 method=pl plots=(s) ;
 time pfsdtn * pfsenr(0);
 strata trta;
 title "Progression-Free Survival";
run;

/* 中位PFS */
proc means data=adtt median;
 var pfsdtn;
 class trta;
 title "Median PFS (Months)";
run;

************************************************************
 OS分析 (Overall Survival)
***********************************************************;

proc lifetest data=adtt timelist=0 6 12 18 24 30 36 method=pl plots=(s);
 time osdtn * osenr(0);
 strata trta;
 title "Overall Survival";
run;

/* 中位OS */
proc means data=adtt median;
 var osdtn;
 class trta;
 title "Median OS (Months)";
run;

************************************************************
 亚组分析
***********************************************************;

/* 年龄亚组 */
proc sql;
 create table age_subgroup as
 select case 
         when age < 65 then '<65'
         when age >= 65 then '>=65'
        end as agegrp,
        trta,
        count(*) as n,
        sum(best_resp) as n_resp,
        (sum(best_resp) / count(*)) * 100 as orr
 from best_resp a
 left join adam.adsl b
 on a.usubjid=b.usubjid
 group by calculated agegrp, trta;
quit;

/* 性别亚组 */
proc sql;
 create table sex_subgroup as
 select sex, trta,
        count(*) as n,
        sum(best_resp) as n_resp,
        (sum(best_resp) / count(*)) * 100 as orr
 from best_resp a
 left join adam.adsl b
 on a.usubjid=b.usubjid
 group by sex, trta;
quit;

proc print data=age_subgroup;
 title "ORR by Age Subgroup";
run;

proc print data=sex_subgroup;
 title "ORR by Sex Subgroup";
run;

************************************************************
 森林图数据准备
***********************************************************;

proc sql;
 create table forest_data as
 select 'Overall' as subgroup, trta,
        count(*) as n, sum(best_resp) as n_resp,
        (sum(best_resp)/count(*))*100 as orr
 from best_resp
 group by trta
 
 union all
  
 select 'Age <65' as subgroup, trta,
        count(*) as n, sum(best_resp) as n_resp,
        (sum(best_resp)/count(*))*100 as orr
 from best_resp a
 left join adam.adsl b on a.usubjid=b.usubjid
 where age < 65
 group by trta
  
 union all
  
 select 'Age >=65' as subgroup, trta,
        count(*) as n, sum(best_resp) as n_resp,
        (sum(best_resp)/count(*))*100 as orr
 from best_resp a
 left join adam.adsl b on a.usubjid=b.usubjid
 where age >= 65
 group by trta;
quit;

proc print data=forest_data;
 title "Forest Plot Data";
run;

************************************************************
 输出RTF
***********************************************************;

filename rtfout "&outpath./t7_efficacy.rtf";
ods rtf file=rtfout style=styles.rtf;

/* ORR Table */
proc report data=orr_summary split='|';
 columns trta n n_cr n_pr n_sd n_pd orr cr_rate pr_rate;
 
 define trta / display "Treatment" width=15;
 define n / display "N" width=8;
 define n_cr / display "CR" width=8;
 define n_pr / display "PR" width=8;
 define n_sd / display "SD" width=8;
 define n_pd / display "PD" width=8;
 define orr / display "ORR (%)" width=10;
 define cr_rate / display "CR Rate (%)" width=12;
 define pr_rate / display "PR Rate (%)" width=12;
 
 title1 "Table 7.1";
 title2 "Tumor Response - Best Overall Response";
 title3 "Intent-to-Treat Analysis Set";
run;

ods rtf close;
filename rtfout clear;

%mend t7_efficacy;
