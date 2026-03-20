/*==============================================================================
PROGRAM NAME : m19708-rfs.sas
COMPOUND : ABT-199
INDICATION : AML
STUDY : M19-708
PROJECT : 
DESCRIPTION : To Create Table
 Analysis of Relapse-Free Survival as Assessed by the Investigator
 (Part 1 All Treated Subjects)
===============================================================================
DETAILS: 

HISTORY: 
Ver#  Author     Date       Code History Description 
----  -------   ----------  ---  ----------------------------------------
1     xiekx2    26Jun2023  Original
2     HONGLX1   16Mar2026  Updated
==============================================================================*/

/* SAS options */
%init;
options validvarname=upcase;

%let dtft=date9.;

%let rtyp=TABLE;
%user(PRTYPE=&RTYP);
%create_rtf_style_template(name=RTFSTYLE, parent=RTF);

%let ltr=14.2;
%let xnum1=&ltr.__1.1;
%let xnum2=&ltr.__1.2;

%let ttl1a=Analysis of Relapse-Free Survival as Assessed by the Investigator;
%let ttl2a=Analysis of Relapse-Free Survival as Assessed by the Investigator;
%let ttl1b=(Part 1 All Treated Subjects);
%let ttl2b=(Part 3 All Treated Subjects);

%let group=trtn;
%let grpno=8;
%let files=2;

%macro files(parts=);
 %do i=1 %to &parts.;
 %global tno&i prfile&i dsnum&i;
 %let tno&i=&rtyp &&xnum&i;
 %let dsnum&i=t%sysfunc(translate(%trim(&&xnum&i),"_","."));
 %let prfile&i=t_&&xnum&i...rtf;
 %end;
%mend;

%files(parts=&files);


%macro formfoot;
 line @1 "Note: Data included are subject to a cutoff date of &cutoff.";
 line @1 "CI = confidence interval; KM = Kaplan-Meier.";
%mend formfoot;

%macro rtfhtf;
 title1 j=l "&TIMESTMP <! &PROGNAME >";
 title2 j=l "&DRUGNAME";
 title3 j=l "&RPTHD";
 title4 j=l "%nrstr(R&D)/&pprd - &rpttype";
 title5 j=l "TABLE PAGE ~{THISPAGE} OF ~{LASTPAGE}";

 compute before _page_ / style=[just=c]; 
 line "&&tno&tab~n";
 line "&&ttl&tab.a";
 line "&&ttl&tab.b";
 line "~S={borderbottomcolor=black borderbottomwidth=0.75pt} ";
 endcomp; 

 compute after _page_ / style=[just=l protectspecialchars=on]; 
 %formfoot;
 line @1 "";
 %if %symexist(progpath3) %then %do;
 line @1 "Program Source Code: &progpath.&progpath2.&progpath3";
 %end;
 %else %if %symexist(progpath2) %then %do;
 line @1 "Program Source Code: &progpath.&progpath2";
 %end;
 %else %do;
 line @1 "Program Source Code: &progpath";
 %end;
 endcomp; 
%mend rtfhtf;


options nocenter msglevel=i missing='';

/* Analysis start */
proc format;
 picture PCT (DEFAULT=8 ROUND FUZZ=1E-25)
 LOW - <0 = '< ZERO' (NOEDIT)
 0 = ' ' (NOEDIT)
 0< - <0.1 = '(<0.1)' (NOEDIT)
 0.1 - <100 = '09.9)' (PREFIX='(')
 100 = '(100) ' (NOEDIT)
 100< - HIGH = '009.9)' (PREFIX='(')
 OTHER = ' ' (NOEDIT);
run;

/* DATA SELECTION START */

* CREATE DUMMY RANDOMIZATION FOR THE STUDY if STILL BLINDED;
%macro table(tab=,part=);

/*==============================================================================
 DATA SELECTION - ADSL
==============================================================================*/

data adsl_;
 set adam.adsl;
 if "&cutoff"d ^in (.) then do; /*use cut off date to cut data*/
 if trtsdt>"&cutoff"d then delete; 
 end;
 if saffl="Y"; 
 if trtsdt^=.;
 if trt01an=3 then do; &group=1;output;end;
 if trt01an=2 then do; &group=2;output;end;
 if trt01an=1 then do; &group=3;output;end;
 if dmgroupn=2 and TR01PG1N=1 then do; &group=4;output;end;
 if dmgroupn=2 and TR01PG1N=2 then do; &group=5;output;end;
 if dmgroupn=2 and TR01PG1N=3 then do; &group=6;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2)) then do; &group=7;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2 3)) then do; &group=8;output;end;
run;

/* Count subjects per treatment group */
proc sql noprint;
 select count(distinct usubjid) into: numd1 from adsl_ where &group=1;
 select count(distinct usubjid) into: numd2 from adsl_ where &group=2;
 select count(distinct usubjid) into: numd3 from adsl_ where &group=3;
 select count(distinct usubjid) into: numd4 from adsl_ where &group=4;
 select count(distinct usubjid) into: numd5 from adsl_ where &group=5;
 select count(distinct usubjid) into: numd6 from adsl_ where &group=6;
 select count(distinct usubjid) into: numd7 from adsl_ where &group=7;
 select count(distinct usubjid) into: numd8 from adsl_ where &group=8;
quit;

/*==============================================================================
 DATA SELECTION - ADSL1 (for merge)
==============================================================================*/

data adsl1;
 set adam.adsl;
 if "&cutoff"d ^in (.) then do; /*USE CUT OFF DATE TO CUT DATA*/
 if trtsdt>"&cutoff"d then delete; 
 end;
 if trtsdt^=.;
 if trt01an=3 then do; &group=1;output;end;
 if trt01an=2 then do; &group=2;output;end;
 if trt01an=1 then do; &group=3;output;end;
 if dmgroupn=2 and TR01PG1N=1 then do; &group=4;output;end;
 if dmgroupn=2 and TR01PG1N=2 then do; &group=5;output;end;
 if dmgroupn=2 and TR01PG1N=3 then do; &group=6;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2)) then do; &group=7;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2 3)) then do; &group=8;output;end;
 keep usubjid trt01a trt01an mrdstat &group.;
run;

/*==============================================================================
 Relapse-Free Survival
==============================================================================*/

data dm1_temp_all (keep=usubjid &group trt01an trtsdt trtedt);
 set adsl_;
run;

proc sort data=dm1_temp_all(keep=usubjid trt01an) out=dm1_temp nodupkey; 
 by usubjid; 
run;

data adtte1;
 /*one to many merge*/
 merge dm1_temp(in=a) adam.adtte(in=b); 
 by usubjid;
 if "&cutoff"d ^in (.) then do;
 /* use cut off date to cut data */
 if adt>"&cutoff"d then delete;
 end;
 if a and b;
 if saffl ="Y" and paramcd = "RFS";
 month=(adt-startdt+1)/30.4;
 subjid=input(strip(scan(usubjid,-2,'-')) || strip(scan(usubjid,-1,'-')),best.);
 if cnsr ne .;
 if cnsr=0 then do;
 event=1; /*Reverse Kaplain Meyer*/
 if evntdesc in("RELAPSE") then pdtpcd=1;
 else if evntdesc in("DEATH") then pdtpcd=3;
 end;
 else if cnsr ne . then event=0; 
run;

data adtte3;
 set adtte1;
 if trt01an=3 then do; &group=1;output;end;
 if trt01an=2 then do; &group=2;output;end;
 if trt01an=1 then do; &group=3;output;end;
 if dmgroupn=2 and TR01PG1N=1 then do; &group=4;output;end;
 if dmgroupn=2 and TR01PG1N=2 then do; &group=5;output;end;
 if dmgroupn=2 and TR01PG1N=3 then do; &group=6;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2)) then do; &group=7;output;end;
 if (dmgroupn=2 and TR01PG1N in (1 2 3)) then do; &group=8;output;end;
run;

proc sort data=adtte3;
 by &group usubjid;
run;

/*==============================================================================
 COUNT NUMBER OF SUBJECTS PER TREATMENT GROUP (N IN HEADER)
==============================================================================*/

data pts;
 set adtte3;
run;

proc sort data=pts;
 by &group;
run;

proc freq data=pts;
 tables &group/out=ns;
run;

data dummy;
 do &group=1 to &grpno;
 output;end;
run;

data ns;
 merge ns dummy;
 by &group;
 if count=. then count=0;
run;

proc transpose data=ns out=total(drop=_name_) prefix=total;
 var count;
run;

/****************************************************************************
 CREATE MACRO VARIABLES NUMD1 TO NUMD&GRPNO FOR THE SUBJECT COUNT IN HEADER 
****************************************************************************/
data _null_; 
 set total;
 array total{*} total1-total&grpno;
 do j=1 to &grpno;
 call symput('NUMD'||compress(put(j,best.)),'(N='||compress(put(total{j},4.))||')');
 call symput('N'||compress(put(j,best.)),compress(put(total{j},4.)));
 end;
run;

/*************************************************************
* PERFORM THE PROC LIFETEST TO GET K-M ESTIMATES *
**************************************************************/

proc sort data= adtte3;
 by &group;
run;

ods output quartiles= survqtle
 censoredsummary= survnum
 productlimitestimates= survest;

proc lifetest data=adtte3 alpha = 0.05;
 time month*event(0);
 survival out=pplot stderr;
 by &group;
 title '95% CONFIDENCE INTERVAL OF THE SURVIVAL DISTRIBUTION (APLHA=0.05)';
run;

/**** get number and percent for event, censor, death ****/

data events;
 set adtte3;
 if pdtpcd in (1,2) and event=1 then pd= 1; 
 else if pdtpcd in (3) and event=1 then pd= 3;
 else delete;
 keep subjid &group pd;
run;

proc sort data=events;
 by &group pd;
run;

proc means data= events noprint;
 by &group pd;
 var subjid;
 output out= out1(drop= _type_ _freq_) sum= n=sumev;
run;

data dummy;
 do &group=1 to &grpno;
 do i=1,3;
 pd=i;
 output;
 end;
 end;
 keep &group pd;
run;

proc sort data=out1 (drop=subjid);
 by &group pd;
run;

data out1;
 merge out1 dummy;
 by &group pd;
run;

proc transpose data=out1 out=out2 (drop=_name_) prefix=sumev;
 by &group;
 id pd;
 var sumev;
run;

/*************************************************************
/**** GET NUMBER AND PERCENT FOR EVENT, CENSOR ****/
*************************************************************/

data survnum;
 merge survnum(in=a) out2(in=b keep=&group sumev1 sumev3);
 by &group;

 pctfail=failed*100/total;
 pctnofail=censored*100/total;

 if failed=. then failed=0;
 if censored=. then censored=0;
 if total=. then total=0;

 if failed^=0 then do;
 event = compress(put(failed,3.))||' ('||compress(put(pctfail,5.1))||')';
 end;
 if failed=0 then do;
 event = compress(put(failed,3.));
 end;
 if censored^=0 then do;
 censor = compress(put(censored,3.))||' ('||compress(put(pctnofail,5.1))||')';
 end;
 if censored=0 then do;
 censor = compress(put(censored,3.));
 end;
 
 tot= compress(put(total,4.));

 if sumev1 > . then pded=compress(put(sumev1,3.));
 else if sumev1 eq . then pded='0';

 if sumev3 > . then ded=compress(put(sumev3,3.));
 else if sumev3 eq . then ded='0';
run;

proc transpose data= survnum out= sur;
 by &group;
 var tot event censor ded pded ;
run;

/*************************************************************
/**** GET QUATILS ****/
*************************************************************/

proc sort data=survqtle;
 by &group percent;
run;

data qtle; set survqtle;
 est=estimate;
 ll=lowerlimit;
 uu=upperlimit;

 if est>. & ll>. & uu>. then do;
 ciday=strip(put(est,5.1))||' ['||strip(put(ll,5.1))||', '||strip(put(uu,5.1))||']';
 end;
 else if est>. & uu=. & ll>. then do;
 ciday=strip(put(est,5.1))||' ['||strip(put(ll,5.1))||', - ]';
 end;
 else if est>. & uu>. & ll=. then do;
 ciday=strip(put(est,5.1))||' [ - ,'||strip(put(uu,5.1))||']';
 end;
 else if est>. & uu=. & ll=. then do;
 ciday=strip(put(est,5.1))||' [ - , - ]';
 end;
 else if est=. & ll>. then do;
 ciday=' -'||' ['||strip(put(ll,5.1))||', - ]';
 end;
 else do ;
 ciday=' - [ -, - ]';
 end;

 keep &group percent ciday;
run;

%mend table;

