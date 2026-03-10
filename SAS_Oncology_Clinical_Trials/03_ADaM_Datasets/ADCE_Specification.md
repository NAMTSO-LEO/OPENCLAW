# ADCE Dataset Specification

## Dataset Description
ADCE (Analysis Dataset for Concentrations) is used for pharmacokinetic (PK) and pharmacodynamic (PD) analyses in clinical trials. It contains concentration-time data and related parameters.

## Dataset Location
`/Users/levi/.openclaw/workspace/SAS_Oncology_Clinical_Trials/03_ADaM_Datasets/`

## Key Variables

### Identification Variables
| Variable | Label | Type | Source |
|----------|-------|------|--------|
| STUDYID | Study Identifier | Char | Raw |
| SUBJID | Subject Identifier | Char | Raw |
| USUBJID | Unique Subject Identifier | Char | Derived |
| SITEID | Site Identifier | Char | Raw |
| ARMCD | Planned Arm Code | Char | Raw |
| ARM | Planned Arm | Char | Raw |

### Time and Date Variables
| Variable | Label | Type | Source |
|----------|-------|------|--------|
| EXSTDTC | Exposure Start Date/Time | Char | Raw |
| EXENDTC | Exposure End Date/Time | Char | Raw |
| EXDOSE | Exposure Dose | Num | Raw |
| EXDOSU | Dose Unit | Char | Raw |
| DOSEMAX | Maximum Dose | Num | Derived |

### PK Concentration Variables
| Variable | Label | Type | Source |
|----------|-------|------|--------|
| PCNAM | Pharmacokinetic Parameter Name | Char | Raw |
| PCSPEC | Specimen Type | Char | Raw |
| PCNAMCD | Parameter Code | Num | Raw |
| PCORRES | Original Result | Char | Raw |
| PCSTRES | Standardized Result | Num | Derived |
| PCSTRESN | Standardized Result (Numeric) | Num | Derived |
| PCSTRESC | Standardized Result (Character) | Char | Derived |
| PCENotes | Result as Originally Collected | Char | Raw |
| PCREASND | Reason for Missing Result | Char | Raw |
| PCSTAT | Completion Status | Char | Raw |
| PCNAM | Parameter Name | Char | Derived |

### Nominal Time Variables
| Variable | Label | Type | Source |
|----------|-------|------|--------|
| EXLOVALD | Dose Level | Num | Raw |
| EXADJ | Dose Adjusted | Char | Raw |
| EXADJP | Dose Adjustment Period | Num | Raw |
| EXVAMT | Volume Administered | Num | Raw |
| EXVAMTU | Volume Administered Unit | Char | Raw |

### Analysis Variables
| Variable | Label | Type | Source |
|----------|-------|------|--------|
| VISITNUM | Visit Number | Num | Raw |
| VISIT | Visit Name | Char | Raw |
| VISITDY | Planned Visit Day | Num | Derived |
| AVMIN | Actual Time Value (Minutes) | Num | Derived |
| AVAL | Analysis Value | Num | Derived |
| AVALC | Analysis Value (Character) | Char | Derived |
| AVALU | Analysis Value Unit | Char | Derived |
| BASE | Baseline Value | Num | Derived |
| CHG | Change from Baseline | Num | Derived |
| PCHG | Percent Change from Baseline | Num | Derived |

## Derivations

### Concentrations
- Convert all concentrations to standard units
- Handle below quantification limit (BQL) values
- Apply imputation rules for missing concentrations

### Time Variables
- Calculate actual sample time relative to dose
- Compute nominal time since last dose
- Derive actual day/time for each PK sample

## Example Records

| STUDYID | SUBJID | USUBJID | PCSPEC | PCNAM | AVAL | AVALU | AVISIT |
|---------|--------|---------|--------|-------|------|-------|--------|
| ABC001 | 001 | ABC001-001 | Plasma | Concentration | 0.5 | ug/mL | Visit 1 |
| ABC001 | 001 | ABC001-001 | Plasma | Concentration | 2.3 | ug/mL | Visit 2 |
| ABC001 | 001 | ABC001-001 | Plasma | Concentration | 1.8 | ug/mL | Visit 3 |

## QC Checks
- Verify all required variables present
- Check concentration units consistency
- Validate subject-level data completeness
- Verify dose and time alignment
- Check for duplicate records
- Validate reference range compliance

## References
- ADaM Implementation Guide v1.1
- CDISC PK Domain Model
- FDA Guidance on Population PK
