"""
Create MVP data for multiple tumor types
Extending from DLBCL to: Lung, Breast, Melanoma, GI
"""

import pandas as pd
import numpy as np
import os

np.random.seed(42)

def create_adsl_tumor(n, tumor_type):
    """Create subject-level data for specific tumor"""
    patient_ids = [f"{tumor_type[:3].upper()}{str(i).zfill(6)}" for i in range(1, n+1)]
    
    if tumor_type == 'NSCLC':
        ages = np.random.randint(40, 80, n)
        sexes = np.random.choice(['M', 'F'], n, p=[0.6, 0.4])
        stages = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.1, 0.15, 0.25, 0.5])
        histology = np.random.choice(['Adeno', 'Squamous', 'Small cell'], n, p=[0.5, 0.3, 0.2])
        pd1_indicator = 0.7  # 70% get immunotherapy
    elif tumor_type == 'Melanoma':
        ages = np.random.randint(30, 75, n)
        sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
        stages = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.15, 0.2, 0.3, 0.35])
        histology = np.random.choice(['Cutaneous', 'Mucosal', 'Acral'], n, p=[0.7, 0.2, 0.1])
        pd1_indicator = 0.85  # 85% get immunotherapy
    elif tumor_type == 'Breast':
        ages = np.random.randint(30, 70, n)
        sexes = np.random.choice(['F'], n)  # All female
        stages = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.25, 0.35, 0.25, 0.15])
        histology = np.random.choice(['HR+', 'HER2+', 'TNBC'], n, p=[0.6, 0.2, 0.2])
        pd1_indicator = 0.3  # 30% get immunotherapy (mostly TNBC)
    elif tumor_type == 'GI':
        ages = np.random.randint(35, 75, n)
        sexes = np.random.choice(['M', 'F'], n, p=[0.6, 0.4])
        stages = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.15, 0.25, 0.3, 0.3])
        histology = np.random.choice(['Gastric', 'CRC', 'Pancreas', 'ESOPH'], n, p=[0.25, 0.35, 0.25, 0.15])
        pd1_indicator = 0.4  # 40% get immunotherapy
    else:  # DLBCL (original)
        ages = np.random.randint(18, 85, n)
        sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
        stages = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.15, 0.25, 0.3, 0.3])
        histology = np.random.choice(['GCB', 'ABC', 'PMBCL'], n, p=[0.4, 0.4, 0.2])
        pd1_indicator = 0.6
    
    # Create treatment assignment
    treatments = np.random.choice(['PD-1', 'Chemotherapy', 'Target'], n, 
                                  p=[pd1_indicator, 1-pd1_indicator-0.1, 0.1])
    
    # Additional covariates
    ecog = np.random.choice([0, 1, 2, 3], n, p=[0.4, 0.35, 0.2, 0.05])
    ldh = np.random.lognormal(mean=5.0, sigma=0.5, size=n)
    ldh = np.clip(ldh, 100, 1500)
    
    df = pd.DataFrame({
        'SUBJID': patient_ids,
        'TUMOR_TYPE': tumor_type,
        'AGE': ages,
        'SEX': sexes,
        'STAGE': stages,
        'HISTOLOGY': histology,
        'ECOG': ecog,
        'LDH': ldh.round(1),
        'TRTP': treatments,
        'SITE': np.random.choice(['SiteA', 'SiteB', 'SiteC'], n)
    })
    
    return df

def create_adtte(adsl_df):
    """Create survival data"""
    n = len(adsl_df)
    
    # Base survival by stage
    stage_multipliers = {'I': 3.0, 'II': 2.5, 'III': 1.5, 'IV': 1.0}
    
    # PD-1 effect varies by tumor
    tumor_hr = {
        'NSCLC': 0.65,
        'Melanoma': 0.55,
        'Breast': 0.75,
        'GI': 0.70,
        'DLBCL': 0.70
    }
    
    survival_times = []
    event_flags = []
    
    for i, row in adsl_df.iterrows():
        base = np.random.exponential(12) * stage_multipliers.get(row['STAGE'], 1)
        
        # Apply treatment effect
        if row['TRTP'] == 'PD-1':
            hr = tumor_hr.get(row['TUMOR_TYPE'], 0.7)
            base = base * hr
        
        base = min(base * np.random.uniform(0.8, 1.2), 48)  # Max 4 years
        event = 1 if np.random.random() < 0.65 else 0
        
        survival_times.append(round(base, 1))
        event_flags.append(event)
    
    # Non-events get random censor
    for i in range(n):
        if event_flags[i] == 0:
            survival_times[i] = round(np.random.uniform(6, 48), 1)
    
    df = pd.DataFrame({
        'SUBJID': adsl_df['SUBJID'],
        'TUMOR_TYPE': adsl_df['TUMOR_TYPE'],
        'TRTP': adsl_df['TRTP'],
        'AVAL': survival_times,
        'CNSR': event_flags,
        'EVNTDESC': ['Death' if e==0 else 'Censored' for e in event_flags]
    })
    
    return df

def create_adae(adsl_df):
    """Create adverse events"""
    pd1_patients = adsl_df[adsl_df['TRTP']=='PD-1']['SUBJID'].tolist()
    
    # irAE rates vary by tumor
    irae_rates = {
        'NSCLC': 0.25,
        'Melanoma': 0.40,
        'Breast': 0.20,
        'GI': 0.15,
        'DLBCL': 0.30
    }
    
    events = []
    for subj, tumor in zip(adsl_df['SUBJID'], adsl_df['TUMOR_TYPE']):
        if subj in pd1_patients and np.random.random() < irae_rates.get(tumor, 0.25):
            irae_type = np.random.choice(['Thyroid', 'Skin', 'Colitis', 'Hepatitis', 'Pneumonitis'])
            grade = np.random.choice([1, 2, 3, 4], p=[0.5, 0.3, 0.15, 0.05])
            events.append({
                'USUBJID': subj,
                'TUMOR_TYPE': tumor,
                'AETERM': irae_type,
                'AESELEV': grade,
                'AESTDY': int(np.random.uniform(30, 365))
            })
    
    return pd.DataFrame(events)

# ==============================
# Generate all tumor types
# ==============================
print("=== Creating Multi-Tumor MVP Data ===")

tumor_configs = {
    'DLBCL': 500,      # Original
    'NSCLC': 600,
    'Melanoma': 400,
    'Breast': 500,
    'GI': 450
}

all_adsl = []
all_adtte = []
all_adae = []

for tumor, n in tumor_configs.items():
    print(f"Generating {tumor} ({n} patients)...")
    
    adsl = create_adsl_tumor(n, tumor)
    adtte = create_adtte(adsl)
    adae = create_adae(adsl)
    
    all_adsl.append(adsl)
    all_adtte.append(adtte)
    all_adae.append(adae)

# Combine
combined_adsl = pd.concat(all_adsl, ignore_index=True)
combined_adtte = pd.concat(all_adtte, ignore_index=True)
combined_adae = pd.concat(all_adae, ignore_index=True)

# Save
combined_adsl.to_csv('data_raw/adsl_multi_tumor.csv', index=False)
combined_adtte.to_csv('data_raw/adtte_multi_tumor.csv', index=False)
combined_adae.to_csv('data_raw/adae_multi_tumor.csv', index=False)

# Summary
print("\n=== Multi-Tumor Data Summary ===")
print(f"Total subjects: {len(combined_adsl)}")
print(f"Total events: {sum(combined_adtte['CNSR']==0)}")
print(f"Total irAE: {len(combined_adae)}")

print("\nBy Tumor Type:")
summary = combined_adtte.groupby('TUMOR_TYPE').agg({
    'SUBJID': 'count',
    'CNSR': 'sum'
}).rename(columns={'SUBJID': 'N', 'CNSR': 'Events'})
print(summary)

print("\nTreatment by Tumor:")
print(combined_adsl.groupby(['TUMOR_TYPE', 'TRTP']).size().unstack(fill_value=0))

print("\nData saved to: data_raw/adsl_multi_tumor.csv, etc.")
