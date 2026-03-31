# SAS Programming Templates

## Common Macro Templates

### 1. Descriptive Statistics Template
```sas
%macro desc_stats(dsn=, var=, by=);
    proc means data=&dsn n mean std median min max;
        var &var;
        &by;
    run;
%mend desc_stats;
```

### 2. Frequency Table Template
```sas
%macro freq_table(dsn=, var=, by=);
    proc freq data=&dsn;
        tables &var / missing;
        &by;
    run;
%mend freq_table;
```

### 3. Kaplan-Meier Template
```sas
proc lifetest data=&dsn plots=survival(cl);
    time &time * &censor(0);
    strata &strata;
run;
```

### 4. AE Summary Template
```sas
proc freq data=adae;
    tables pt*arm / norow nopercent;
run;
```

## Common Formats
- $SEX. (M=Male, F=Female)
- $ARM. (A=Arm A, B=Arm B)
- $RACE.
- GRADE. (1-5)
