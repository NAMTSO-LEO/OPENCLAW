"""
Extended Neuro-Oncology Data with RANO and Imaging Features
"""

import pandas as pd
import numpy as np
np.random.seed(42)

# Load base data
df = pd.read_csv('neuro_oncology_data.csv')

# Add extended fields
print("=== Adding Extended Neuro Fields ===")

# 1. RANO Response (instead of RECIST)
# CR, PR, SD, PD, NE
rano_map = {
    'CR': 'Complete Response',
    'PR': 'Partial Response', 
    'SD': 'Stable Disease',
    'PD': 'Progressive Disease',
    'NE': 'Not Evaluable'
}
# Use existing RESP but map to RANO
df['RANO_RESPONSE'] = df['RESPONSE'].map(lambda x: rano_map.get(x, 'NE'))

# 2. Neuro Function Score (expanded)
# Add detailed neuro exam
df['NEURO_EXAM'] = np.random.choice(['Normal', 'Mild Deficit', 'Moderate Deficit', 'Severe Deficit'], 
                                     len(df), p=[0.4, 0.3, 0.2, 0.1])

# 3. Steroid Use (important for neuro)
df['STEROID_DOSE'] = np.random.choice([0, 4, 8, 16, 32], len(df), p=[0.3, 0.3, 0.25, 0.1, 0.05])

# 4. Imaging Features
df['TUMOR_VOLUME_CM3'] = np.random.lognormal(3, 1, len(df)).round(1)
df['EDEMA_VOLUME_CM3'] = np.random.lognormal(2.5, 0.8, len(df)).round(1)
df['CONTRAST_ENHANCEMENT'] = np.random.choice(['None', 'Faint', 'Moderate', 'Strong'], 
                                                 len(df), p=[0.2, 0.3, 0.35, 0.15])

# 5. Molecular markers expanded
df['1P19Q_COC'] = np.random.choice(['Co-deleted', 'Intact', 'Unknown'], len(df), p=[0.25, 0.45, 0.3])
df['ATRX_LOSS'] = np.random.choice([0, 1, 2], len(df), p=[0.5, 0.3, 0.2])  # 0=no, 1=yes, 2=unknown

# 6. Treatment Sequence
df['TREATMENT_SEQ'] = df['TREATMENT'].str.replace('Surgery+', 'S→').str.replace('RT', 'RT').str.replace('Chemo', 'Ch').str.replace('TMZ', 'TMZ')
df['TIME_TO_RT_DAYS'] = np.random.exponential(30, len(df)).round(0)
df['TIME_TO_CHEMO_DAYS'] = np.random.exponential(45, len(df)).round(0)

# 7. Imaging timepoints
df['BASELINE_MRI_DATE'] = 0  # Day 0
df['FIRST_FOLLOWUP_DAYS'] = np.random.choice([30, 60, 90], len(df), p=[0.3, 0.5, 0.2])
df['SECOND_FOLLOWUP_DAYS'] = np.random.choice([90, 180, 270], len(df), p=[0.4, 0.4, 0.2])

# Save extended
df.to_csv('neuro_extended_data.csv', index=False)

print("\n=== Extended Data Summary ===")
print(f"Total: {len(df)} patients")
print(f"\nNew fields added:")
print(f"  - RANO_RESPONSE: {df['RANO_RESPONSE'].value_counts().to_dict()}")
print(f"  - NEURO_EXAM: {df['NEURO_EXAM'].value_counts().to_dict()}")
print(f"  - STEROID_DOSE: {df['STEROID_DOSE'].value_counts().to_dict()}")
print(f"  - IMAGING: tumor volume, edema, enhancement")
print(f"  - MOLECULAR: 1p19q, ATRX")
print(f"  - TREATMENT_SEQ: treatment timeline")

print("\n✅ Extended data saved to neuro_extended_data.csv")
