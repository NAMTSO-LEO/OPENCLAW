# Evidence Package Template

## 标准输出格式

### 1. Study Information

| 字段 | 内容 |
|------|------|
| Study ID | MVP-001 |
| Study Question | PD-1 vs Chemo effectiveness in NSCLC |
| Data Source | Multi-tumor RWE database |
| Analysis Date | 2026-03-31 |
| Version | 1.0 |

---

### 2. Cohort Definition

| 参数 | 值 |
|------|-----|
| Population | NSCLC patients |
| Inclusion | Age ≥18, Stage III-IV |
| Exclusion | Prior immunotherapy |
| N (Analysis) | 539 |
| N (PD-1) | 424 |
| N (Chemo) | 115 |

---

### 3. Data Quality

| 指标 | 结果 |
|------|------|
| Missing Data | <5% |
| Follow-up Median | 14.2 months |
| Data Source Tier | Tier 1/2 |

---

### 4. Baseline Characteristics

| Variable | PD-1 (n=424) | Chemo (n=115) | SMD |
|----------|-------------|---------------|-----|
| Age, median | 65 | 64 | 0.08 |
| Male, % | 62% | 60% | 0.04 |
| Stage IV, % | 52% | 48% | 0.08 |
| LDH, median | 245 | 238 | 0.11 |

---

### 5. Primary Analysis Results

| Outcome | HR | 95% CI | P-value |
|---------|-----|--------|---------|
| OS (IPTW-adj) | 0.72 | 0.58-0.89 | 0.003 |
| PFS (IPTW-adj) | 0.68 | 0.55-0.84 | 0.001 |

---

### 6. Diagnostics

| Check | Result |
|-------|--------|
| SMD Max | 0.11 (< 0.15 ✓) |
| ESS | 412 (77% of N) |
| Overlap | Adequate ✓ |
| Propensity Score Dist | Good overlap ✓ |

---

### 7. Sensitivity Analysis

| Analysis | HR | 95% CI | Note |
|----------|-----|--------|------|
| Primary (IPTW) | 0.72 | 0.58-0.89 | - |
| PS Matching | 0.75 | 0.60-0.94 | Similar |
| E-value | 2.1 | - | Unmeasured conf needed |

---

### 8. Conclusions

- PD-1 shows statistically significant OS benefit vs chemo
- Effect robust to multiple adjustments
- Unmeasured confounding unlikely to explain effect (E-value=2.1)

---

### 9. Limitations

- Retrospective design
- Potential selection bias
- Follow-up time limited

---

### 10. Decision Implications

| Decision | Evidence Level | Recommendation |
|----------|----------------|----------------|
| Go/No-Go | High | Continue development |
| Label extension | Medium | Support with RCT data |

---

*Evidence Package Template Complete*
