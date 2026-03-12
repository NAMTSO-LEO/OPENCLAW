/*soh***************************************************************************
Program name : t5_crs_other.sas
Compound : EPCO
Study : M20-621, M23-362, GCT3013-02
Milestone : ISS
Description : Create TFL - CRS Other Signs and Symptoms Analysis
--------------------------------------------------------------------------------
Details: CRS其他体征和症状分析 - 非发热/低血压/低氧的CRS事件
--------------------------------------------------------------------------------
**eoh**************************************************************************/

%init;

%let outpath=/sasdata/iss/output;
%let groupn=trtn;
%let grpno=7;

************************************************************
 Step 1: 获取CRS事件数据 (排除主要症状)
***********************************************************;

/* 获取CE数据 - M20-621, M23-362 */
data ce1 ce2 ce3 ce4 cegct;
 set adam.adce;
 
 /* 筛选CRS事件 */
 if aesicat in ('CYTOKINE RELEASE SYNDROME' 'CRS'); 
 cedecod=upcase(cedecod);
 
 /* 排除主要症状: 发热、低血压、低氧 */
 if upcase(cedecod) not in ('PYREXIA' 'FEVER' 'HYPOTENSION' 'HYPOXIA') 
    or index(ceterm,'OTHER');
    
 if cedecod='' then cedecod='*** Not coded ***';
 
 /* 按研究分 */
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
 
 /* 再次排除主要症状 */
 if upcase(ceterm) not in ('PYREXIA' 'FEVER' 'HYPOTENSION' 'HYPOXIA') 
    or index(upcase(ceterm),'OTHER');
    
 cedecod=ceterm; 
 keep studyid usubjid subjid cedecod aerefid;
run;

/* 去重 */
proc sort data=ce0 nodupkey out=ce_comb;
 by studyid usubjid cedecod aerefid;
run; 

************************************************************
 Step 2: 获取ADAES数据用于关联
***********************************************************;

data adaea;
 set adam.adaes;
 where trtemfl="Y" 
   and aesicat in ('CYTOKINE RELEASE SYNDROME' 'CRS') 
   and studyid in ('M20-621' 'M23-362') 
   and upcase(aedecod) in ("CYTOKINE RELEASE SYNDROME", "CYTOKINE STORM") 
   and CRSFL='Y'; 
 keep studyid usubjid subjid grpnum aedecod aestdtc ANL40FL;
run;

/* 创建linkid */
data adaea;
 set adaea;
 aerefid=grpnum;
run;

proc sort data=adaea;
 by usubjid aerefid;
run;

proc sort data=ce_comb;
 by usubjid aerefid;
run;

************************************************************
 Step 3: 合并数据
***********************************************************;

data ce_comb;
 merge adaea(in=b) ce_comb(in=a);
 by usubjid aerefid; 
 if b then output;
run;

/* 去重 */
proc sort data=ce_comb nodupkey;
 by usubjid grpnum cedecod;
run;

************************************************************
 Step 4: 获取ADAESI数据
***********************************************************;

data aesi;
 merge adsl(in=a) adaesi(in=b);
 by usubjid;
 if a and b; 
 
 /* 创建linkid */
 if studyid in ("M20-621" "M23-362") then linkid=grpnum;
 else linkid=aespid;
run;

proc sort data=ce_comb nodupkey;
 by usubjid linkid;
run;

proc sort data=aesi nodupkey;
 by usubjid linkid;
run;

************************************************************
 Step 5: 最终合并
***********************************************************;

data adce; 
 merge ce_comb(in=a) aesi(in=b);
 by usubjid linkid;
 if b;
run;

************************************************************
 Step 6: 筛选"Other"事件
***********************************************************;

data adce2; 
 set adce(where=(index(ceterm,'Other') or index(cedecod,'OTHER')));
 
 if cedecod='' and ceterm1='' and ceterm2='' and ceterm3='' then cedecod='*** Not coded ***';
 
 %grp;
run;

/* 去重 */
proc sort data=adce2 nodupkey;
 by usubjid linkid trtn;
run;

************************************************************
 Step 7: 统计分析 - 按组别和事件汇总
***********************************************************;

proc freq data=adce2 noprint;
 table &groupn*cedecod / out=decod;
run;

/* 按组别排序事件 */
proc sort data=decod out=dummy_d(keep=cedecod count);
 where &groupn=1;
 by cedecod descending count;
run;

proc sort data=decod out=dummy_c(keep=cedecod) nodupkey;
 by cedecod;
run;

data dummy_c;
 merge dummy_c(in=a) dummy_d;
 by cedecod;
 if a;
run;

proc sort data=dummy_c;
 by descending count cedecod;
run;

/* 添加排序变量 */
data dummy_c;
 set dummy_c;
 by descending count cedecod;
 do &groupn=1 to 7;
  ord1=_n_;
  output;
 end;
run;

/* 处理未编码事件 */
data dummy_c;
 set dummy_c;
 if cedecod='*** Not coded ***' then ord1=1;
 else ord1=ord1+1;
 drop count;
run;

proc sort data=dummy_c;
 by &groupn cedecod;
run;

proc sort data=decod;
 by &groupn cedecod;
run;

data decod;
 merge dummy_c(in=a) decod;
 by &groupn cedecod;
 if a;
 if count=. then count=0;
run;

************************************************************
 Step 8: 计算每组受试者数
***********************************************************;

proc sql;
 create table ana0 as
 select a.*, b.&groupn
 from adaesi a
 inner join adsl b
 on a.usubjid=b.usubjid
 where a.CRSFL='Y' and a.trtemfl='Y';
quit;

proc freq data=ana0 noprint;
 table &groupn / out=trt_cnt;
run;

************************************************************
 Step 9: 输出表格
***********************************************************;

/* 创建展示表 */
proc sql;
 create table crs_other_summary as
 select &groupn, cedecod, count, 
        case 
         when &groupn=1 then &numd1
         when &groupn=2 then &numd2
         when &groupn=3 then &numd3
         when &groupn=4 then &numd4
         when &groupn=5 then &numd5
         when &groupn=6 then &numd6
         when &groupn=7 then &numd7
        end as denom,
        round(count / case 
         when &groupn=1 then &numd1
         when &groupn=2 then &numd2
         when &groupn=3 then &numd3
         when &groupn=4 then &numd4
         when &groupn=5 then &numd5
         when &groupn=6 then &numd6
         when &groupn=7 then &numd7
        end * 100, 0.1) as pct
 from decod
 order by &groupn, ord1;
quit;

proc print data=crs_other_summary;
 title "CRS Other Signs and Symptoms by Treatment Group";
run;

************************************************************
 Step 10: 输出RTF
***********************************************************;

filename rtfout "&outpath./t5_crs_other.rtf";
ods rtf file=rtfout style=styles.rtf;

proc report data=crs_other_summary split='|';
 columns &groupn cedecod count denom pct;
 
 define &groupn / display "Treatment|Group" width=10;
 define cedecod / display "CRS Other Sign/Symptom" width=40;
 define count / display "Number of|Events" width=12;
 define denom / display "Number of|Patients" width=12;
 define pct / display "%" width=8;
 
 title1 "Table 5.x.x";
 title2 "CRS Other Signs and Symptoms by Treatment Group";
 title3 "Safety Analysis Set";
 
 footnote1 "Only includes CRS events other than Pyrexia/Fever, Hypotension, and Hypoxia";
 footnote2 "Percentages are calculated based on number of patients with CRS in each group.";
run;

ods rtf close;
filename rtfout clear;

%mend t5_crs_other;
