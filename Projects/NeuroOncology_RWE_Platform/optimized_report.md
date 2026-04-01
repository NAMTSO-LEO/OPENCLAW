# Optimized Model Training Report

## Results

- **LR_Tuned**: AUC = 0.5900, CV = 0.5922 ± 0.0095
- **AdaBoost**: AUC = 0.5851, CV = 0.5929 ± 0.0088
- **Ensemble**: AUC = 0.5734, CV = 0.5827 ± 0.0055
- **RF_Tuned**: AUC = 0.5724, CV = 0.5752 ± 0.0046
- **GB_Tuned**: AUC = 0.5486, CV = 0.5633 ± 0.0064
- **MLP**: AUC = 0.5337, CV = 0.5135 ± 0.0135

## Best Model: LR_Tuned (AUC = 0.5900)

## Feature Importance
           Feature  Importance
         EDEMA_VOL    0.115054
        VOLUME_LOG    0.101261
         TUMOR_VOL    0.100114
           AGE_KPS    0.096329
        RISK_SCORE    0.094031
               LDH    0.092236
               AGE    0.084509
           ALBUMIN    0.083074
           EOR_GTR    0.049657
               KPS    0.031615
TRT_Surgery+RT+TMZ    0.024212
           EOR_STR    0.017462
              MGMT    0.015696
               IDH    0.015440
  TUMOR_Meningioma    0.013228