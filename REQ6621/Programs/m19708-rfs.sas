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
 
%mend table;

