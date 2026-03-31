# Strategy Brief Template

## Use Case 1: PD-1 Effectiveness

### Business Question
PD-1治疗在真实世界中是否比标准挽救治疗更有效？

### Clinical Question
在R/R DLBCL中，PD-1能否延长OS？

### Evidence Question
在校正混杂后，PD-1 vs non-PD-1的HR是多少？

### Decision Owner
临床开发团队 / 医学事务

### Development Phase
注册后证据 / Label extension

### Priority Rationale
- 高价值：直接支持药物上市后证据
- 高监管相关性：可与监管对话
- 方法可复用：IPTW + TTE可推广至其他实体瘤

### Success Criteria
- IPTW校正后的OS HR + 95%CI
- KM曲线显示分离
- SMD < 0.1 for all covariates
- ESS > 50% of original sample
- 可生成完整的evidence package

### Timeline
- Week 5-6: 数据接入
- Week 7-8: 完整分析
- Week 9: Evidence package

---

## Use Case 2: irAE Safety

### Business Question
irAE是否与疗效相关？传统分析是否高估了这种相关性？

### Clinical Question
出现irAE的患者是否生存期更长？（需控制时间依赖偏倚）

### Evidence Question
Time-dependent Cox vs 普通Cox的HR差异有多大？

### Decision Owner
安全团队 / 医学事务

### Development Phase
上市后监测

### Priority Rationale
- 方法学亮点强：解决immortal time bias
- 可发表高水平论文
- 行业高度关注

### Success Criteria
- Time-dependent HR with 95%CI
- 对比图展示普通Cox的bias
- 敏感性分析结果
- 完整的bias assessment报告

### Timeline
- Week 7: 数据构建
- Week 8: Time-dependent分析
- Week 9: 对比与报告

---

## Use Case 3: AI Prediction

### Business Question
哪些患者更可能从PD-1治疗中获益？

### Clinical Question
基于多模态数据能否预测ORR/PFS？

### Evidence Question
ML模型的预测性能是否显著优于临床变量 alone？

### Decision Owner
临床开发 / 精准医疗团队

### Development Phase
探索性 / 精准患者筛选

### Priority Rationale
- AI能力展示
- 多模态融合
- 精准医疗导向

### Success Criteria
- XGBoost/Transformer模型
- AUC/预测性能指标
- SHAP解释输出
- 特征重要性排序

### Timeline
- Week 9-10: 数据准备
- Week 10-11: 模型训练
- Week 11: 解释与报告

---

*MVP Step 2 - Strategy Brief complete*
