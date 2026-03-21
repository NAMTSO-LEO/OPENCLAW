# Data Validation Checklist

## Study: GKS for Cavernous Sinus-Invading Acromegaly

---

## A. Subject-Level Completeness Checks

### Required Fields Per Patient
- [ ] site_id
- [ ] study_subjid
- [ ] sex
- [ ] age_gks
- [ ] eligible_fl = Yes
- [ ] gks_dt
- [ ] At least one baseline endocrine record
- [ ] At least one baseline MRI record
- [ ] At least one post-GKS endocrine record
- [ ] At least one post-GKS MRI record
- [ ] lastfu_dt

### Consistency Checks
- [ ] eligible_fl = Yes → No exclusion = Yes
- [ ] eligible_fl = No → Excluded from analysis set

---

## B. Date Logic Checks

### Basic Timeline
- [ ] acro_diag_dt ≤ gks_dt
- [ ] surg_dt < gks_dt
- [ ] Baseline endocrine date ≤ gks_dt
- [ ] Baseline MRI date ≤ gks_dt
- [ ] Post-GKS dates > gks_dt
- [ ] death_dt ≥ gks_dt
- [ ] lastfu_dt ≥ gks_dt

### Medication Logic
- [ ] med_ongoing_gks = Yes → med_startdt ≤ gks_dt
- [ ] med_hold_perigks = Yes → med_ongoing_gks not empty

### Salvage Logic
- [ ] salvage date > gks_dt

---

## C. Baseline Uniqueness Checks

- [ ] Only one endo_base_fl = Yes
- [ ] Only one img_base_fl = Yes
- [ ] Multiple baseline flags = Yes → Query
- [ ] No baseline flag = Yes → Derive by proximity, flag

---

## D. Endocrine Consistency Checks

### Numeric Logic
- [ ] IGF1 present → IGF1_ULN present
- [ ] ogtt_done = Yes → ogtt_nadir_gh not missing
- [ ] endo_status_site = Remission → post_onmed = No
- [ ] endo_status_site = Controlled → post_onmed = Yes

### Clinical Logic
- [ ] IGF-1/ULN ≤ 1 AND post_onmed = No but site ≠ Remission → Adjudication
- [ ] Site = Recurrence but no prior remission → Query

---

## E. Imaging Consistency Checks

- [ ] mri_prog = Yes → mri_response = Progressed
- [ ] mri_response = Progressed → mri_prog ≠ No
- [ ] Volume changes > tolerance → Query
- [ ] csi_evidence = Knosp → knosp_grade not missing

---

## F. Pituitary Function Consistency

- [ ] new_deficit = Yes → base_deficit = No (same axis)
- [ ] replacement_started = Yes but new_deficit = No → Check if continued therapy
- [ ] Same axis/same date → No conflicting records

---

## G. Toxicity Consistency

- [ ] tox_type = Other → tox_type_other completed
- [ ] tox_new = Pre-existing unchanged → tox_related ≠ Yes
- [ ] Visual/CN event date < GKS → Check if pre-existing

---

## H. Salvage Treatment Consistency

- [ ] salv_type = Medication escalation → salv_reason completed
- [ ] Salvage exists but no persistent/recurrence/progression → Query
- [ ] Salvage date < remission date but reason = recurrence → Query

---

## I. Survival/Follow-up Consistency

- [ ] alive_fl = No → death_dt completed
- [ ] alive_fl = Yes → death_dt empty
- [ ] lastfu_dt not earlier than any post-GKS assessment
- [ ] Post-GKS records but no lastfu_dt → Query

---

## J. Derivation Support Flags

Add these variables to support QC:
- [ ] raw_complete_fl
- [ ] baseline_endo_derv_fl
- [ ] baseline_img_derv_fl
- [ ] date_impute_fl
- [ ] adj_needed_fl
- [ ] adj_done_fl
- [ ] major_query_fl

---

## K. Central Review Workflow

### Step 1: Submit Core CRF
Centers submit initial data

### Step 2: Run Checks
Data manager runs completeness + logic checks

### Step 3: Generate Queries
Query list sent back to centers

### Step 4: Adjudication
Review:
- [ ] Remission vs medication status conflict
- [ ] Recurrence without prior remission
- [ ] Vague progression
- [ ] New hypopituitarism vs baseline deficit conflict
- [ ] Unclear salvage reason

### Step 5: Database Lock
Generate listings:
- [ ] Eligibility listing
- [ ] Remission listing
- [ ] Recurrence listing
- [ ] Progression listing
- [ ] Hypopituitarism listing

---

## M. Query Categories

| Category | Description |
|----------|-------------|
| ELIGIBILITY | Inclusion/exclusion criteria |
| ENDOCRINE | Lab values, remission status |
| IMAGING | MRI, volume, progression |
| TOXICITY | Adverse events |
| SALVAGE | Treatment interventions |
| FOLLOW-UP | Last contact dates |

---

## N. Query Resolution Rules

1. Query must be resolved before database lock
2. All resolutions documented in Query_Resolution_Log
3. Unresolved queries → Major query flag → Report in deliverables

---

## O. Validation Summary Report

Generate report with:
- Total records submitted
- Queries generated
- Query resolution rate
- Data completeness by field
- Date logic failures
- Adjudications required

---

*Created: 2026-03-21*
