# PHASE 6: Rigor & Reviewer Simulation

## 1. Claim-Evidence Audit

| Claim | Evidence Type | Status | Gap |
|-------|---------------|--------|-----|
| SOTA accuracy | Quantitative | Pending | Experiments needed |
| Cross-modal attention improves fusion | Ablation | Pending | None |
| First DL for tropical Asian HSI-LiDAR | Literature | Complete | Document search |
| Multi-task improves over single-task | Ablation | Pending | None |
| Framework generalizes | Cross-site validation | Pending | None |
| Satellite scaling feasible | Experiments | Pending | Need actual HySIS |
| DSS meets requirements | User study | Pending | None |

---

## 2. Missing Citations

| Topic | Recommended |
|-------|-------------|
| Focal Loss | Lin et al., 2017 |
| AdamW | Loshchilov & Hutter, 2019 |
| Spatial Blocking | Roberts et al., 2017 |
| FLAASH | Adler-Golden et al., 1999 |
| CSF Algorithm | Zhang et al., 2016 |

---

## 3. Stress Testing

### Confounders
| Confounder | Mitigation |
|------------|------------|
| Illumination | BRDF correction |
| Phenology | Document season |
| GPS error | RTK-GNSS |
| Species misID | Expert verification |

### Threats to Validity

**Internal**:
- Spatial autocorrelation → Spatial blocking
- Overfitting → Early stopping, dropout
- Data leakage → Strict separation

**External**:
- Geographic scope → 3 diverse sites
- Temporal scope → Document; propose multi-temporal
- Sensor specificity → Domain adaptation

---

## 4. Simulated Reviews

### Reviewer 1 (DL Expert)
**Major Issues**:
1. Missing recent fusion baselines (2023-2024)
2. Computational cost justification needed
3. Attention visualization lacking

**Response**: Add baselines; efficiency comparison; visualization

### Reviewer 2 (Forest RS Expert)
**Major Issues**:
1. Canopy-dominant species bias
2. Lack of ecological interpretation
3. Ground-truth protocol unclear

**Response**: Expand limitations; add trait analysis; clarify protocol

### Reviewer 3 (ISRO Perspective)
**Major Issues**:
1. HySIS validation is simulated
2. Operational deployment path unclear

**Response**: Request actual HySIS; expand DSS section

### Reviewer 4 (Statistics)
**Major Issues**:
1. Multiple comparison correction
2. CI methodology unclear

**Response**: Apply Bonferroni; clarify statistics

---

## 5. Revision Plan

### Critical Priority
- C1: Acquire actual HySIS data
- C2: Add recent baselines
- C3: Attention visualization
- C4: Multiple comparison correction

### High Priority
- H1: Ecological interpretation
- H2: Ground-truth protocol clarity
- H3: Computational justification

### Medium Priority
- M1: Additional ablations
- M2: DSS deployment details
- M3: TRL assessment

---

## 6. Space-Worthiness (ISRO)

### TRL Assessment
| Component | Current | Target |
|-----------|---------|--------|
| Algorithm | TRL 4 | TRL 6 |
| Spectral Encoder | TRL 4 | TRL 5 |
| Structural Encoder | TRL 4 | TRL 5 |
| DSS | TRL 4 | TRL 6 |

### Future Mission Relevance
- HySIS: Primary data source
- HySIS-2: Enhanced range
- NISAR: SAR structure alternative
- Future LiDAR sat: Direct integration

---

## 7. Revised Claims

### Original → Revised

**Claim 1**: "SOTA performance"
→ "[X.X]% OA for 25 species, outperforming SpectralFormer by [Y.Y]% (p<0.001, McNemar's with Bonferroni)"

**Claim 2**: "First DL for tropical Asian"
→ "First peer-reviewed DL framework for HSI-LiDAR fusion in tropical Asian forests (systematic search January 2026)"

**Claim 3**: "Scaling validated"
→ "Scaling demonstrated via simulation; actual HySIS validation pending data availability"

---

## Phase Status
**PHASE 6: RIGOR REVIEW COMPLETE** ✓

**→ Proceed to PHASE 7: Submission Preparation**
