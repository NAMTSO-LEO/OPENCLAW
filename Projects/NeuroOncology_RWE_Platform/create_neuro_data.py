"""
Neuro-Oncology RWE Platform - Complete MVP Data
Brain Tumor Types: Glioma, Glioblastoma, Astrocytoma, Meningioma, Medulloblastoma
"""

import pandas as pd
import numpy as np
np.random.seed(42)

# ==============================
# Generate Neuro-Oncology Data
# ==============================
print("=== Creating Neuro-Oncology Platform Data ===")

configs = {
    'Glioblastoma': {'n': 400, 'age_range': (40, 80), 'kps_low': 50},
    'Glioma': {'n': 350, 'age_range': (20, 70), 'kps_low': 60},
    'Astrocytoma': {'n': 300, 'age_range': (20, 70), 'kps_low': 60},
    'Meningioma': {'n': 350, 'age_range': (30, 75), 'kps_low': 70},
    'Medulloblastoma': {'n': 200, 'age_range': (5, 25), 'kps_low': 70}
}

all_data = []

for tumor, cfg in configs.items():
    n = cfg['n']
    
    # Demographics
    ages = np.random.randint(cfg['age_range'][0], cfg['age_range'][1], n)
    sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
    
    # KPS (Karnofsky Performance Status) - critical for neuro-oncology
    kps = np.random.choice([50, 60, 70, 80, 90, 100], n, 
                          p=[0.1, 0.2, 0.3, 0.25, 0.1, 0.05])
    
    # Molecular markers - key for neuro
    if tumor in ['Glioblastoma', 'Glioma', 'Astrocytoma']:
        mgmt = np.random.choice([0, 1], n, p=[0.45, 0.55])  # MGMT methylated
        idh = np.random.choice([0, 1], n, p=[0.5, 0.5])  # IDH mutation
    else:
        mgmt = np.random.choice([0, 1], n, p=[0.8, 0.2])
        idh = np.random.choice([0, 1], n, p=[0.9, 0.1])
    
    # Location
    if tumor == 'Meningioma':
        loc = np.random.choice(['Convexity', 'SkullBase', 'Parasagittal'], n, p=[0.4, 0.4, 0.2])
    else:
        loc = np.random.choice(['Frontal', 'Temporal', 'Parietal', 'Occipital', 'Brainstem'], n, p=[0.3, 0.25, 0.2, 0.1, 0.15])
    
    # WHO Grade
    if tumor == 'Glioblastoma':
        grade = np.random.choice(['IV'], n)
    elif tumor == 'Medulloblastoma':
        grade = np.random.choice(['III', 'IV'], n, p=[0.3, 0.7])
    elif tumor == 'Meningioma':
        grade = np.random.choice(['I', 'II', 'III'], n, p=[0.7, 0.2, 0.1])
    else:
        grade = np.random.choice(['II', 'III', 'IV'], n, p=[0.3, 0.4, 0.3])
    
    # Extent of resection (EOR)
    eor = np.random.choice(['GTR', 'STR', 'Biopsy'], n, p=[0.4, 0.4, 0.2])
    
    # Treatment - neuro specific protocols
    if tumor == 'Glioblastoma':
        trt = np.random.choice(['Surgery+RT+TMZ', 'Surgery+RT', 'RT+TMZ'], n, p=[0.5, 0.3, 0.2])
    elif tumor == 'Meningioma':
        trt = np.random.choice(['Surgery', 'Surgery+RT', 'RT', 'Observation'], n, p=[0.6, 0.25, 0.1, 0.05])
    else:
        trt = np.random.choice(['Surgery+RT+Chemo', 'Surgery+RT', 'Surgery+Chemo'], n, p=[0.4, 0.35, 0.25])
    
    # Labs
    ldh = np.random.lognormal(4.8, 0.4, n).clip(100, 800).round(1)
    alb = np.random.normal(4, 0.4, n).clip(2.5, 5.5).round(1)
    
    # Complications
    seizures = np.random.choice([0, 1], n, p=[0.65, 0.35])
    edema = np.random.choice([0, 1], n, p=[0.55, 0.45])
    
    # Response
    resp = np.random.choice(['CR', 'PR', 'SD', 'PD', 'NE'], n, p=[0.1, 0.2, 0.35, 0.25, 0.1])
    
    # Survival - tumor/grade specific
    base_survival = {'II': 36, 'III': 18, 'IV': 8}
    os = []
    for g, t, e in zip(grade, trt, eor):
        base = np.random.exponential(24)
        
        # Treatment benefit
        if 'TMZ' in t:
            base *= 0.75
        if 'RT' in t:
            base *= 0.85
        
        # EOR impact
        if e == 'GTR':
            base *= 0.6
        elif e == 'STR':
            base *= 0.8
        
        # Grade impact
        base *= base_survival.get(g, 1) / 24
        
        base = min(base * np.random.uniform(0.7, 1.3), 60)
        os.append(round(base, 1))
    
    # Event
    event = [1 if o < 48 else 0 for o in os]
    
    # PFS
    pfs = [min(o * np.random.uniform(0.5, 0.9), o-0.5) for o in os]
    pfs_evt = [1 if p < o-1 else 0 for p, o in zip(pfs, os)]
    
    df = pd.DataFrame({
        'SUBJID': [f"NEURO{tumor[:3].upper()}{i:05d}" for i in range(1, n+1)],
        'TUMOR': tumor, 'AGE': ages, 'SEX': sexes, 'KPS': kps,
        'MGMT_METH': mgmt, 'IDH_MUT': idh,
        'LOCATION': loc, 'GRADE': grade, 'EOR': eor, 'TREATMENT': trt,
        'LDH': ldh, 'ALBUMIN': alb,
        'SEIZURES': seizures, 'EDEMA': edema,
        'RESPONSE': resp, 'OS': os, 'OS_EVENT': event,
        'PFS': pfs, 'PFS_EVENT': pfs_evt
    })
    all_data.append(df)

# Combine
neuro_df = pd.concat(all_data, ignore_index=True)
neuro_df.to_csv('neuro_oncology_data.csv', index=False)

# ==============================
# Summary
# ==============================
print(f"\n=== Neuro-Oncology Platform Data ===")
print(f"Total patients: {len(neuro_df)}")
print(f"\nTumor distribution:")
print(neuro_df['TUMOR'].value_counts().to_string())

print(f"\n=== Key Neuro Features ===")
print(f"KPS: {neuro_df['KPS'].min()}-{neuro_df['KPS'].max()}")
print(f"MGMT methylated: {neuro_df['MGMT_METH'].sum()} ({neuro_df['MGMT_METH'].mean()*100:.1f}%)")
print(f"IDH mutated: {neuro_df['IDH_MUT'].sum()} ({neuro_df['IDH_MUT'].mean()*100:.1f}%)")
print(f"EOR: {neuro_df['EOR'].value_counts().to_dict()}")
print(f"\nTreatment: {neuro_df['TREATMENT'].value_counts().to_dict()}")

# Median OS by tumor
print(f"\n=== Median OS by Tumor ===")
for t in neuro_df['TUMOR'].unique():
    median_os = neuro_df[neuro_df['TUMOR']==t]['OS'].median()
    print(f"{t}: {median_os:.1f} months")

print("\n✓ Neuro data saved to: neuro_oncology_data.csv")
