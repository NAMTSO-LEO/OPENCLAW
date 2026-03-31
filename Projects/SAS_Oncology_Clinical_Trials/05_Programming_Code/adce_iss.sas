/*===================================================================
Program:    adce_iss.sas
Purpose:    Create ADCE ISS dataset for Integrated Summary of Safety
Author:     
Date:       
===================================================================*/

/*===================================================================
 STEP 1: 按研究分别提取数据
===================================================================*/

/* STUDY_A - 从 SDTM CE 提取 */
proc sql;
    create table study_a_ce as
    select studyid, subjid, usubjid, siteid,
           ceterm, cedecod, cecat, scat,
           cestdtc, ceendtc, ceenrf, ceseq
    from sdtm.ce
    where studyid = "STUDY_A";
quit;

/* STUDY_B - 直接使用已有 ADCE */
proc sql;
    create table study_b_ce as
    select *
    from adam.adce
    where studyid = "STUDY_B";
quit;

/* STUDY_C1 - 从 SDTM CE 提取 */
proc sql;
    create table study_c1_ce as
    select studyid, subjid, usubjid, siteid,
           ceterm, cedecod, cecat, scat,
           cestdtc, ceendtc, ceenrf, ceseq
    from sdtm.ce
    where studyid = "STUDY_C1";
quit;

/* STUDY_C2 - 从 SDTM CE 提取 */
proc sql;
    create table study_c2_ce as
    select studyid, subjid, usubjid, siteid,
           ceterm, cedecod, cecat, scat,
           cestdtc, ceendtc, ceenrf, ceseq
    from sdtm.ce
    where studyid = "STUDY_C2";
quit;

/* STUDY_D - 从 SDTM CE 提取 */
proc sql;
    create table study_d_ce as
    select studyid, subjid, usubjid, siteid,
           ceterm, cedecod, cecat, scat,
          cestdtc, ceendtc, ceenrf, ceseq
    from sdtm.ce
    where studyid = "STUDY_D";
quit;

/* STUDY_E - 从 ADAE 反推构建 CE 风格数据 */
proc sql;
    create table study_e_ce as
    select distinct 
           studyid, subjid, usubjid, siteid,
           aeterm as ceterm, 
           aedecod as cedecod,
           "ADVERSE EVENT" as cecat,
           aescat as scat,
           aestdtc as cestdtc,
           aeenddtc as ceendtc,
           "N" as ceenrf,
           aeseq as ceseq
    from sdtm.adae
    where studyid = "STUDY_E";
quit;


/*===================================================================
 STEP 2: 按研究内规则筛选事件
===================================================================*/

/* STUDY_A: 只保留 SIGNS AND SYMPTOMS */
data study_a_filtered;
    set study_a_ce;
    if cecat = "SIGNS AND SYMPTOMS";
run;

/* STUDY_B: 只保留 SIGNS AND SYMPTOMS */
data study_b_filtered;
    set study_b_ce;
    if cecat = "SIGNS AND SYMPTOMS";
run;

/* STUDY_C1: 只保留 CRS/ICANS 相关 */
data study_c1_filtered;
    set study_c1_ce;
    if scat like "%CRS%" or scat like "%ICANS%";
run;

/* STUDY_C2: 只保留 CRS/ICANS 相关 */
data study_c2_filtered;
    set study_c2_ce;
    if scat like "%CRS%" or scat like "%ICANS%";
run;

/* STUDY_D: 只保留 SIGNS AND SYMPTOMS */
data study_d_filtered;
    set study_d_ce;
    if cecat = "SIGNS AND SYMPTOMS";
run;

/* STUDY_E: 保留所有 AE 事件 */
data study_e_filtered;
    set study_e_ce;
    /* 全部保留 */
run;


/*===================================================================
 STEP 3: 标准化日期和分析时间变量
===================================================================*/

%macro standardize_dates(dsn=, out=);
    data &out;
        set &dsn;
        
        /* 转换开始日期 */
        if not missing(cestdtc) then do;
            cestdat = input(cestdtc, e8601da.);
            format cestdat yymmdd10.;
        end;
        
        /* 转换结束日期 */
        if not missing(ceendtc) then do;
            ceendat = input(ceendtc, e8601da.);
            format ceendat yymmdd10.;
            cendat = ceendat;
            format cendat yymmdd10.;
        end;
        
        /* 计算相对治疗日的分析日 - 需要先与 ADSL 合并获取 TRTSDT */
        /* 此处暂时保留原始值，后续步骤完成 */
        keep studyid subjid usubjid siteid ceterm cedecod cecat scat
             ceseq cestdtc ceendtc cestdat ceendat cendat;
    run;
%mend standardize_dates;

/* 对各研究应用日期标准化 */
%standard_dates(dsn=study_a_filtered, out=study_a_dated);
%standard_dates(dsn=study_b_filtered, out=study_b_dated);
%standard_dates(dsn=study_c1_filtered, out=study_c1_dated);
%standard_dates(dsn=study_c2_filtered, out=study_c2_dated);
%standard_dates(dsn=study_d_filtered, out=study_d_dated);
%standard_dates(dsn=study_e_filtered, out=study_e_dated);


/*===================================================================
 STEP 4: 关联 AE 信息
===================================================================*/

/* 方法1: 直接通过 link group 关联 - STUDY_A, STUDY_B */
proc sql;
    create table study_a_linked as
    select a.*, 
           b.aespid, b.aesicat
    from study_a_dated a
    left join sdtm.relrec b
        on a.studyid = b.studyid 
        and a.subjid = b.subjid
        and a.ceterm = b.term
        and b.reltype = "CE";
quit;

/* 方法2: 通过 RELREC 关联 - STUDY_C1, STUDY_C2 */
proc sql;
    create table study_c1_linked as
    select a.*,
           b.aespid, b.aesicat
    from study_c1_dated a
    left join sdtm.relrec b
        on a.studyid = b.studyid 
        and a.subjid = b.subjid
        and a.ceterm = b.term
        and b.reltype = "CE";
quit;

/* 方法3: 从 ADAE/ADAES 补回 - STUDY_D, STUDY_E */
proc sql;
    create table study_d_linked as
    select a.*,
           b.aespid, b.aesicat
    from study_d_dated a
    left join sdtm.adaes b
        on a.studyid = b.studyid
        and a.subjid = b.subjid
        and a.cedecod = b.aedecod;
quit;


/*===================================================================
 STEP 5: 统一结构并合并所有研究
===================================================================*/

/* 统一变量框架 - 选择所有研究中共同的变量 */
data study_a_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_a_linked;
run;

data study_b_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_b_linked;
run;

data study_c1_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_c1_linked;
run;

data study_c2_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_c2_linked;
run;

data study_d_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_d_linked;
run;

data study_e_std (keep=studyid usubjid subjid siteid ceterm cedecod cecat scat 
                       ceseq cestdat ceendat cendat aespid aesicat);
    set study_e_dated;
run;

/* 纵向合并所有研究 */
data adce_merged;
    set study_a_std study_b_std study_c1_std study_c2_std 
        study_d_std study_e_std;
run;

/* 合并后全局标准化 */
data adce_standardized;
    set adce_merged;
    
    /* 统一 AESICAT 文本 */
    aesticat = strip(aesicat);
    if aesticat = "CRS (cytokine release syndrome)" then aesticat = "CRS";
    if aesticat = "ICANS" then aesticat = "ICANS";
    
    /* 统一 ATOXGR 格式 - 初始为空，后续从其他数据源补充 */
    if atoxgr = "" then atoxgr = "";
    
    /* 确保 STUDYID 正确 */
    /* 如有需要可添加修正逻辑 */
    
run;


/*===================================================================
 STEP 6: 去重、补充 ADSL、生成序号
===================================================================*/

/* 去重 */
proc sort data=adce_standardized nodupkey;
    by studyid usubjid ceterm cescat cestdat cendat;
run;

/* 与 ADSL 合并获取治疗信息和基线变量 */
proc sql;
    create table adce_with_adsl as
    select a.*,
           b.age, b.sex, b.race, 
           b.trtsdt, b.trtedt, b.trtp, b.trta, b.saffl, b.ittfl
    from adce_merged a
    left join adam.adsl b
        on a.studyid = b.studyid and a.usubjid = b.usubjid;
quit;

/* 计算分析日 - 相对治疗开始日 */
data adce_with_days;
    set adce_with_adsl;
    
    /* 计算 CESTDY */
    if not missing(cestdat) and not missing(trtsdt) then do;
        cestdy = cestdat - trtsdt + 1;
    end;
    
    /* 计算 CEEENDY */
    if not missing(ceendat) and not missing(trtsdt) then do;
        ceendy = ceendat - trtsdt + 1;
    end;
    
    /* 计算 CENDY */
    if not missing(cendat) and not missing(trtsdt) then do;
        cendy = cendat - trtsdt + 1;
    end;
    
run;

/* 按受试者生成分析序号 ASEQ */
proc sort data=adce_with_days;
    by studyid usubjid cestdat;
run;

data adam.adce_iss (label="ADCE for ISS Analysis");
    set adce_with_days;
    by studyid usubjid;
    
    retain aseq 0;
    if first.usubjid then do;
        aseq = 0;
    end;
    aseq + 1;
    
    /* 重新排列变量顺序 */
    keep studyid usubjid subjid siteid aseq
         ceterm cedecod cecat scat cescat
         aespid aesicat atoxgr atoxgrn aeser aesev
         cestdtc ceendtc cestdat ceendat cendat
         cestdy ceendy cendy
         trtsdt trtedt trtp trta trtdur
         saffl ittfl age sex race agegr1;
    
    label studyid = "Study Identifier"
          usubjid = "Unique Subject Identifier"
          subjid = "Subject Identifier"
          siteid = "Site Identifier"
          aseq = "Analysis Sequence Number"
          ceterm = "Clinical Event Term"
          cedecod = "Clinical Event Decoded Term"
          cecat = "Clinical Event Category"
          scat = "Subcategory"
          cescat = "Clinical Event Analysis Category"
          aespid = "AE Sequence Number"
          aesicat = "AE Category"
          atoxgr = "Analysis Toxicity Grade"
          atoxgrn = "Analysis Toxicity Grade (Numeric)"
          aeser = "Serious Adverse Event"
          aesev = "Severity"
          cestdtc = "Clinical Event Start Date/Time"
          ceendtc = "Clinical Event End Date/Time"
          cestdat = "Clinical Event Start Date"
          ceendat = "Clinical Event End Date"
          cendat = "Clinical Event End Date for Analysis"
          cestdy = "Clinical Event Start Day"
          ceendy = "Clinical Event End Day"
          cendy = "Clinical Event End Day for Analysis"
          trtsdt = "Date of First Exposure"
          trtedt = "Date of Last Exposure"
          trtp = "Planned Treatment"
          trta = "Actual Treatment"
          trtdur = "Treatment Duration"
          saffl = "Safety Population Flag"
          ittfl = "Intent-to-Treat Population Flag"
          age = "Age"
          sex = "Sex"
          race = "Race"
          agegr1 = "Age Group";
    
    format cestdat ceendat cendat trtsdt trtedt yymmdd10.;
run;

/* 验证输出 */
proc contents data=adam.adce_iss;
run;

proc print data=adam.adce_iss (obs=10);
run;
