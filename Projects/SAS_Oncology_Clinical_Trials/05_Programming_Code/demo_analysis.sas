/*===================================================================
Program:    demo_analysis.sas
Purpose:    Example oncology clinical trial analysis program
Author:     
Date:       
===================================================================*/

%let studyid = EXAMPLE001;
%let inds = adsl;
%let outds = result_summary;

proc sort data=&inds out=sorted;
    by subject;
run;

proc means data=sorted n mean std median min max;
    var age;
    output out=&outds (drop=_type_ _freq_)
        n=n mean=mean std=std median=median min=min max=max;
run;

proc sgplot data=sorted;
    histogram age / binwidth=5;
    xaxis label="Age (years)";
    title "Distribution of Age";
run;

/* Kaplan-Meier for PFS */
proc lifetest data=adttte plots=survival;
    time ttfpfs * censor(0);
    strata arm;
run;
