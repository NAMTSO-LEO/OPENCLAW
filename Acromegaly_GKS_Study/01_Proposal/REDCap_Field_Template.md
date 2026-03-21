# REDCap Field Template

## Study: GKS for Cavernous Sinus-Invading Acromegaly

---

## 1. REDCap Instrument Structure

### 16 Instruments

1. 11_Site_Subject_ID
2. 22_Eligibility
3. 33_Baseline_Clinical
4. 44_Prior_Surgery (repeating)
5. 55_Prior_Medical_Therapy (repeating)
6. 66_PreGKS_Endocrine (repeating)
7. 77_PreGKS_Imaging (repeating)
8. 88_GKS_Treatment
9. 99_PostGKS_Endocrine (repeating)
10. 10_PostGKS_Imaging (repeating)
11. 11_PostGKS_Pituitary_Function (repeating)
12. 12_PostGKS_Toxicity (repeating)
13. 13_Salvage_Treatment (repeating)
14. 14_Vital_Status_Last_Followup
15. 15_Adjudication_Form
16. 16_Query_Resolution_Log

---

## 2. Instrument 01: Site_Subject_ID

| Variable | Field Type | Choices/Notes |
|----------|-----------|---------------|
| site_id | text | Center code |
| country | text | |
| subject_id | text | Local ID |
| study_subjid | calc/text | [site_id]-[subject_id] |
| age_gks | integer | Years |
| sex | radio | 1=Male, 2=Female, 3=Other, 9=Unknown |

---

## 3. Instrument 02: Eligibility

| Variable | Field Type | Choices |
|----------|-----------|---------|
| inc_acro_diag | yesno | |
| inc_csi | yesno | |
| inc_gks | yesno | |
| inc_fu12m | yesno | |
| inc_postendo | yesno | |
| inc_postmri | yesno | |
| exc_no_csi | yesno | |
| exc_non_gh | yesno | |
| exc_prior_fxrt | yesno | |
| exc_prior_srs | yesno | |
| exc_inadeq_fu | yesno | |
| exc_miss_base_endo | yesno | |
| exc_unclass_plan | yesno | |
| eligible_fl | radio | 1=Yes, 0=No |
| elig_reason | notes | Show if eligible_fl='0' |

---

## 4. Instrument 03: Baseline_Clinical

| Variable | Field Type | Choices |
|----------|-----------|---------|
| acro_diag_dt | text | date_ymd |
| present_headache | yesno | |
| present_visual | yesno | |
| present_diplopia | yesno | |
| present_acrofeat | yesno | |
| present_hypopit | yesno | |
| comorb_dm | yesno | |
| comorb_htn | yesno | |
| comorb_cv | yesno | |
| comorb_osa | yesno | |

---

## 5. Instrument 04: Prior_Surgery (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| surg_seq | integer | Auto |
| surg_dt | text | date_ymd |
| surg_approach | dropdown | 1=Endoscopic, 2=Microscopic, 3=Transcranial, 4=Other |
| surg_intent | dropdown | 1=Primary, 2=Repeat, 3=Debulking, 4=Salvage |
| surg_result | dropdown | 1=GTR, 2=STR, 3=PR, 9=Unknown |
| surg_compl | yesno | |
| surg_notes | notes | |

---

## 6. Instrument 05: Prior_Medical_Therapy (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| med_seq | integer | |
| med_name | dropdown | 1=SSA, 2=Pegvisomant, 3=Dopamine agonist, 4=Other |
| med_name_other | text | Show if med_name='4' |
| med_startdt | text | date_ymd |
| med_stopdt | text | date_ymd |
| med_ongoing_gks | yesno | |
| med_hold_perigks | yesno | |
| med_hold_days_before | integer | |
| med_resume_days_after | integer | |

---

## 7. Instrument 06: PreGKS_Endocrine (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| endo_seq | integer | |
| endo_dt | text | date_ymd |
| endo_base_fl | yesno | Only one = Yes |
| igf1 | number | |
| igf1_unit | text | |
| igf1_uln | number | |
| igf1_lln | number | |
| gh | number | |
| gh_unit | text | |
| ogtt_done | yesno | |
| ogtt_nadir_gh | number | Show if ogtt_done='1' |
| endo_onmed | yesno | |
| endo_interp | dropdown | 1=Uncontrolled, 2=Controlled, 3=Remission, 4=Recurrence, 9=Unknown |

---

## 8. Instrument 07: PreGKS_Imaging (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| img_seq | integer | |
| mri_dt | text | date_ymd |
| img_base_fl | yesno | Only one = Yes |
| knosp_grade | dropdown | 0,1,2,3,4 |
| csi_evidence | dropdown | 1=Knosp, 2=MRI residual, 3=Plan target, 4=Other |
| tumor_vol | number | cc |
| tumor_maxdim | number | mm |
| residual_cs | yesno | |
| residual_sella | yesno | |
| optic_prox | yesno | |
| img_interp | dropdown | 1=Residual, 2=Recurrent, 3=Stable, 4=Progression, 9=Unknown |

---

## 9. Instrument 08: GKS_Treatment

| Variable | Field Type | Choices |
|----------|-----------|---------|
| gks_dt | text | date_ymd |
| gks_role | dropdown | 1=Adjuvant, 2=Recurrence, 3=Primary |
| plan_type | dropdown | 1=Targeted, 2=Whole-sella, 3=Mixed, 9=Unknown |
| target_desc | notes | |
| target_vol_cc | number | |
| margin_dose | number | Gy |
| max_dose | number | Gy |
| isodose_line | number | % |
| optic_max_dose | number | Gy |
| cn_max_dose | number | Gy |
| n_isocenters | integer | |
| bed | number | |
| bed_method | text | |
| plan_notes | notes | |

---

## 10. Instrument 09: PostGKS_Endocrine (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| post_endo_seq | integer | |
| post_endo_dt | text | date_ymd |
| post_igf1 | number | |
| post_igf1_unit | text | |
| post_igf1_uln | number | |
| post_gh | number | |
| post_ogtt_done | yesno | |
| post_ogtt_nadir_gh | number | Show if post_ogtt_done='1' |
| post_onmed | yesno | |
| post_med_names | text | |
| endo_status_site | dropdown | 1=Uncontrolled, 2=Controlled, 3=Remission, 4=Recurrence, 9=Unknown |
| new_horm_tx | yesno | |

---

## 11. Instrument 10: PostGKS_Imaging (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| post_img_seq | integer | |
| post_mri_dt | text | date_ymd |
| post_tumor_vol | number | cc |
| vol_method | dropdown | 1=Manual, 2=Software, 3=Estimated, 9=Unknown |
| volchg_pct | number | % |
| mri_response | dropdown | 1=Decreased, 2=Stable, 3=Progressed, 4=Unevaluable |
| mri_prog | yesno | |
| mri_notes | notes | |

---

## 12. Instrument 11: PostGKS_Pituitary_Function (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| pit_seq | integer | |
| pit_dt | text | date_ymd |
| axis | dropdown | 1=Thyroid, 2=Adrenal, 3=Gonadal, 4=GH, 5=Posterior |
| base_deficit | yesno | |
| new_deficit | yesno | |
| replacement_started | yesno | |
| replacement_type | text | |
| pit_notes | notes | |

---

## 13. Instrument 12: PostGKS_Toxicity (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| tox_seq | integer | |
| tox_dt | text | date_ymd |
| tox_type | dropdown | 1=Visual, 2=Field, 3=Optic, 4=CN, 5=ARE, 6=Radionecrosis, 7=Other |
| tox_type_other | text | Show if tox_type='7' |
| tox_grade | text | |
| tox_new | dropdown | 1=New, 2=Worsened, 3=Pre-existing unchanged |
| tox_related | radio | 1=Yes, 0=No, 9=Unknown |
| tox_resolved | yesno | |
| tox_notes | notes | |

---

## 14. Instrument 13: Salvage_Treatment (Repeating)

| Variable | Field Type | Choices |
|----------|-----------|---------|
| salv_seq | integer | |
| salv_dt | text | date_ymd |
| salv_type | dropdown | 1=Repeat surgery, 2=Repeat SRS, 3=Fractionated RT, 4=Med escalation |
| salv_reason | dropdown | 1=Persistent, 2=Recurrence, 3=Progression, 4=Combined, 5=Other |
| salv_reason_other | text | Show if salv_reason='5' |
| salv_notes | notes | |

---

## 15. Instrument 14: Vital_Status_Last_Followup

| Variable | Field Type | Choices |
|----------|-----------|---------|
| lastfu_dt | text | date_ymd |
| lastfu_type | dropdown | 1=Endo, 2=Imaging, 3=Clinical, 4=Telephone, 5=Chart |
| alive_fl | yesno | |
| death_dt | text | Show if alive_fl='0' |
| death_cause | notes | |

---

## 16. Instrument 15: Adjudication_Form

| Variable | Field Type | Choices |
|----------|-----------|---------|
| adj_needed | yesno | |
| adj_domain | dropdown | 1=Remission, 2=Recurrence, 3=Progression, 4=Hypopit, 5=Toxicity, 6=Salvage |
| adj_reason | notes | |
| adj_decision | notes | |
| adj_dt | text | date_ymd |
| adj_reviewer | text | |

---

## 17. Instrument 16: Query_Resolution_Log

| Variable | Field Type | Choices |
|----------|-----------|---------|
| query_id | text | |
| query_dt | text | date_ymd |
| query_domain | dropdown | Endo/Imaging/Toxicity/Salvage/Follow-up |
| query_text | notes | |
| site_response | notes | |
| resolved_fl | yesno | |
| resolved_dt | text | date_ymd |

---

## 18. Minimum Required Instruments

**Phase 1 (Core):**
- 11_Site_Subject_ID
- 22_Eligibility
- 66_PreGKS_Endocrine
- 77_PreGKS_Imaging
- 88_GKS_Treatment
- 99_PostGKS_Endocrine
- 10_PostGKS_Imaging
- 13_Salvage_Treatment
- 14_Vital_Status_Last_Followup

**Phase 2 (Extended):**
- 11_PostGKS_Pituitary_Function
- 12_PostGKS_Toxicity
- 15_Adjudication_Form
- 16_Query_Resolution_Log

---

*Created: 2026-03-21*
