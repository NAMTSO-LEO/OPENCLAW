# Decision Support Layer

## 决策适配框架

### Evidence Level Classification

| Level | Criteria | Use Case |
|-------|----------|----------|
| **High** | IPTW + diagnostics pass + sensitivity robust | Regulatory discussion, label decisions |
| **Medium** | Standard analysis, some limitations | Internal decisions, development planning |
| **Low** | Exploratory, multiple limitations | Hypothesis generation |

---

## 决策类型映射

### 1. Go/No-Go Decision

| Input | Output | Confidence |
|-------|--------|------------|
| OS HR + 95% CI | Continue/Stop | High if CI doesn't cross 1 |

### 2. Safety Signal Escalation

| Input | Output | Confidence |
|-------|--------|------------|
| irAE rate + severity | Monitor/Escalate | Medium |

### 3. Label Extension Support

| Input | Output | Confidence |
|-------|--------|------------|
| ECA construction | Support/Not support | High with proper governance |

### 4. Patient Stratification

| Input | Output | Confidence |
|-------|--------|------------|
| Prediction model | High/Low risk | Medium |

---

## Quick Decision Matrix

```
                        HR < 0.8         HR 0.8-1.0      HR > 1.0
High quality data     → Strong Continue → Consider    → Stop
Medium quality       → Consider          → Monitor     → Stop
Low quality           → Explore          → More data   → Negative
```

---

*Decision Support Layer Defined*
