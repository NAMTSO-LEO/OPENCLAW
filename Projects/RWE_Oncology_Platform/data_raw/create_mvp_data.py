"""
Create MVP demo data based on real dataset structures
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

# ==============================
# 1. ADaM-like Structure: ADSL (Subject Level)
# ==============================
def create_adsl(n=500):
    """Create subject-level dataset"""
    
    # Generate patient IDs
    patient_ids = [f"P{str(i).zfill(6)}" for i in range(1, n+1)]
    
    # Demographics
    ages = np.random.randint(18, 85, n)
    sexes = np.random.choice(['M', 'F'], n, p=[0.55, 0.45])
    races = np.random.choice(['White', 'Black', 'Asian', 'Other'], n, p=[0.6, 0.15, 0.15, 0.1])
    
    # Clinical baseline
    ecog = np.random.choice([0, 1, 2, 3], n, p=[0.4, 0.35, 0.2, 0.05])
    stage = np.random.choice(['I', 'II', 'III', 'IV'], n, p=[0.15, 0.25, 0.3, 0.3])
    
    # Laboratory (simulated baseline LDH)
    ldh = np.random.lognormal(mean=5.0, sigma=0.5, size=n)
    ldh = np.clip(ldh, 100, 1000)
    
    # Prior lines of therapy
    prior_lines = np.random.choice([1, 2, 3, 4], n, p=[0.4, 0.3, 0.2, 0.1])
    
    # Create dataframe
    df = pd.DataFrame({
        'SUBJID': patient_ids,
        'AGE': ages,
        'SEX': sexes,
        'RACE': races,
        'ECOG': ecog,
        'STAGE': stage,
        'LDH': ldh.round(1),
        'PRIOR_LINES': prior_lines,
        'SITE': np.random.choice(['SiteA', 'SiteB', 'SiteC', 'SiteD'], n)
    })
    
    return df

# ==============================
# 2. ADaM-like Structure: ADTTE (Time-to-Event)
# ==============================
def create_adtte(adsl_df):
    """Create time-to-event dataset"""
    
    n = len(adsl_df)
    
    # Treatment assignment (PD-1 vs non-PD-1) - 60% vs 40%
    treatment = np.random.choice(['PD-1', 'Non-PD-1'], n, p=[0.6, 0.4])
    
    # Generate survival times (months)
    # PD-1 group has better survival (HR ~0.7)
    survival_times = []
    event_flags = []
    
    for i, (t, stage) in enumerate(zip(treatment, adsl_df['STAGE'])):
        # Base survival varies by stage
        if stage == 'IV':
            base_months = np.random.exponential(12)
        elif stage == 'III':
            base_months = np.random.exponential(18)
        elif stage == 'II':
            base_months = np.random.exponential(24)
        else:
            base_months = np.random.exponential(30)
        
        # PD-1 effect (HR ~0.7)
        if t == 'PD-1':
            base_months = base_months * 0.7
        
        # Add noise
        base_months = base_months * np.random.uniform(0.8, 1.2)
        base_months = min(base_months, 36)  # Censor at 3 years
        
        # Event indicator (1=death, 0=censored)
        event = 1 if np.random.random() < 0.7 else 0
        
        survival_times.append(round(base_months, 1))
        event_flags.append(event)
    
    # Random censor times for non-events
    for i in range(n):
        if event_flags[i] == 0:
            survival_times[i] = round(np.random.uniform(6, 36), 1)
    
    df = pd.DataFrame({
        'SUBJID': adsl_df['SUBJID'],
        'TRTP': treatment,
        'AVAL': survival_times,  # Analysis value (time in months)
        'CNSR': event_flags,     # Censor (0=event, 1=censored)
        'EVNTDESC': ['Death' if e==0 else 'Censored' for e in event_flags],
        'ADT': [(datetime.now() - timedelta(days=int(s*30))).strftime('%Y-%m-%d') 
                for s in survival_times]
    })
    
    return df

# ==============================
# 3. ADaM-like Structure: ADAE (Adverse Events)
# ==============================
def create_adae(adsl_df, adtte_df):
    """Create adverse events dataset"""
    
    # For PD-1 patients, generate irAE
    pd1_subjects = adsl_df[adsl_df['SUBJID'].isin(
        adtte_df[adtte_df['TRTP']=='PD-1']['SUBJID']
    )]['SUBJID'].tolist()
    
    # ~30% of PD-1 patients have irAE
    irae_subjects = np.random.choice(pd1_subjects, size=int(len(pd1_subjects)*0.3), replace=False)
    
    # Generate irAE events
    events = []
    for subj in irae_subjects:
        # irAE type
        irae_type = np.random.choice(['Thyroid', 'Skin', 'Colitis', 'Hepatitis', 'Pneumonitis'])
        
        # Timing (months from treatment start)
        onset = np.random.uniform(1, 12)
        
        # Severity
        grade = np.random.choice([1, 2, 3, 4], p=[0.5, 0.3, 0.15, 0.05])
        
        # Outcome
        outcome = np.random.choice(['Resolved', 'Ongoing', 'Resolved with sequelae'])
        
        events.append({
            'USUBJID': subj,
            'AETERM': irae_type,
            'AESTDY': round(onset*30),  # Days
            'AESELEV': grade,
            'AEOUT': outcome,
            'AESTDTC': f"2024-{np.random.randint(1,13):02d}-{np.random.randint(1,28):02d}"
        })
    
    df = pd.DataFrame(events)
    return df

# ==============================
# 4. ADRS (Response) - optional
# ==============================
def create_adrs(adsl_df, adtte_df):
    """Create tumor response dataset"""
    
    responders = adsl_df.sample(frac=0.4)['SUBJID'].tolist()
    
    responses = []
    for subj in responders:
        responses.append({
            'USUBJID': subj,
            'PARAMCD': 'BOR',
            'AVAL': 'CR',  # Could be CR/PR/SD/PD
            'ANL01FL': 'Y'
        })
    
    # Add some non-responders
    non_responders = [s for s in adsl_df['SUBJID'].tolist() if s not in responders]
    for subj in non_responders[:len(responders)//2]:
        responses.append({
            'USUBJID': subj,
            'PARAMCD': 'BOR',
            'AVAL': 'PD',
            'ANL01FL': 'Y'
        })
    
    return pd.DataFrame(responses)

# ==============================
# MAIN: Generate all datasets
# ==============================
print("=== Generating MVP Demo Data ===")

# Create directories
os.makedirs('data_raw', exist_ok=True)
os.makedirs('data_curated', exist_ok=True)

# Generate datasets
print("Creating ADSL...")
adsl = create_adsl(500)
adsl.to_csv('data_raw/adsl.csv', index=False)

print("Creating ADTTE...")
adtte = create_adtte(adsl)
adtte.to_csv('data_raw/adtte.csv', index=False)

print("Creating ADAE (irAE)...")
adae = create_adae(adsl, adtte)
adae.to_csv('data_raw/adae.csv', index=False)

print("Creating ADRS...")
adrs = create_adrs(adsl, adtte)
adrs.to_csv('data_raw/adrs.csv', index=False)

# Summary
print("\n=== Data Summary ===")
print(f"ADSL: {len(adsl)} subjects")
print(f"ADTTE: {len(adtte)} records, {adtte['CNSR'].sum()} events")
print(f"ADAE: {len(adae)} irAE events")
print(f"ADRS: {len(adrs)} response records")

print("\nTreatment distribution:")
print(adtte['TRTP'].value_counts())

print("\nData saved to: data_raw/")
