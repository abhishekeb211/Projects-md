# PHASE 1.5: Lock Decisions

## Pre-Phase 2 Decision Requirements

Before initiating the Systematic Literature Review (SLR), the following decisions must be locked to avoid wasted effort and ensure focused literature search.

---

## Decision Matrix

### D1: Study Area Scope

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Single District** | Focus on one district (e.g., East Khasi Hills) | Deep analysis; manageable logistics; intensive sampling | Limited generalization; narrow scope | None |
| **B: Three Districts** | East Khasi Hills + West Garo Hills + Ri-Bhoi | Diverse forest types; good coverage; validates transferability | Moderate logistics; increased field work | May need multiple AVIRIS-NG scenes |
| **C: Five Districts** | Expanded coverage across state | Maximum generalization; comprehensive | High cost; complex logistics; extended timeline | Extensive satellite coverage needed |

**Recommendation**: Option B (Three Districts)
- Covers subtropical broadleaf, tropical semi-evergreen, and pine forests
- Feasible within 24-month timeline
- Aligned with AVIRIS-NG campaign coverage
- Allows cross-site generalization testing

---

### D2: Target Species Count

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: 10-15 species** | Dominant canopy species only | Easier validation; cleaner dataset; higher per-species samples | Limited biodiversity representation | Sufficient for mission validation |
| **B: 20-25 species** | Major canopy + key understory species | Good balance; demonstrates scalability; ecological relevance | Moderate field effort; some species challenging | Good for HySIS utility demo |
| **C: 30+ species** | Comprehensive inventory | Maximum scientific value; comprehensive library | High complexity; species confusion likely; logistics | Excellent for future missions |

**Recommendation**: Option B (20-25 species)
- Captures ecological diversity across forest types
- Achievable with botanical collaboration
- Demonstrates practical utility for forest management
- Sufficient for validating deep learning approach

---

### D3: Deep Learning Architecture Strategy

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Pure CNN** | 3D-CNN for HSI + CNN/PointNet for LiDAR | Proven; interpretable; less data hungry | May miss long-range dependencies | None |
| **B: Pure Transformer** | ViT-style for both modalities | State-of-art; attention weights interpretable | Data hungry; computationally expensive | HPC access helpful |
| **C: Hybrid CNN-Transformer** | CNN feature extraction + Transformer fusion | Best of both; efficient; flexible | Architecture complexity | HPC access helpful |
| **D: Evaluate Multiple** | Systematic comparison of architectures | Scientific rigor; comprehensive | More experiments needed | HPC access required |

**Recommendation**: Option D (Evaluate Multiple) with primary focus on C (Hybrid)
- Provides scientific contribution through systematic comparison
- Hybrid approach likely optimal based on literature
- Addresses RQ-T1 directly

---

### D4: Fusion Strategy (For Systematic Evaluation)

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Early Fusion** | Concatenate raw/low-level features | Simple; joint learning from start | Modality dominance risk; dim explosion | None |
| **B: Mid Fusion** | Fuse intermediate representations | Balanced; flexible; common approach | Architecture design complexity | None |
| **C: Late Fusion** | Combine decision-level outputs | Modality-specific optimization; simple | Suboptimal joint patterns; limited interaction | None |
| **D: Attention Fusion** | Cross-modal attention mechanisms | Adaptive; interpretable; SOTA | Complex; more parameters | None |
| **E: Evaluate All** | Systematic comparison | Scientific rigor; comprehensive | Increased experiments | None |

**Recommendation**: Option E (Evaluate All)
- Addresses RQ-T2 directly
- Provides generalizable insights for community
- Standard practice in fusion research

---

### D5: UAV Hyperspectral Sensor Selection

| Option | Specifications | Pros | Cons | ISRO Dependency |
|--------|---------------|------|------|-----------------|
| **A: VNIR-only** | 400-1000nm, ~100-150 bands | Lighter; affordable; adequate for many species | Misses SWIR water/cellulose features | Good for HySIS comparison (VNIR) |
| **B: Full VNIR-SWIR** | 400-2500nm, 200+ bands | Comprehensive; best discrimination; matches AVIRIS-NG | Heavy; expensive; more complex processing | Excellent for AVIRIS-NG comparison |
| **C: Custom Integration** | Mix sensors for coverage | Flexible; optimized for budget | Integration challenges; calibration issues | Variable |

**Recommendation**: Option B (Full VNIR-SWIR) or partnership with existing facility
- SWIR critical for species discrimination (water, lignin, cellulose)
- Aligns with AVIRIS-NG spectral range (380-2500nm)
- SAC/IIRS/universities may have suitable equipment
- Consider rental or collaboration if purchase not feasible

---

### D6: LiDAR Specifications

| Option | Specifications | Pros | Cons | ISRO Dependency |
|--------|---------------|------|------|-----------------|
| **A: Basic LiDAR** | Single return, 20-30 pts/m² | Affordable; lighter; easier processing | Limited canopy penetration; no vertical structure | None |
| **B: Multi-return LiDAR** | 3-5 returns, 50+ pts/m² | Good penetration; vertical profiles; crown detail | Moderate cost; heavier | None |
| **C: Full-waveform** | Continuous waveform digitization | Best penetration; full vertical structure | Expensive; complex processing; heavy | None |

**Recommendation**: Option B (Multi-return LiDAR)
- Multi-return essential for canopy penetration in dense forests
- High point density for individual tree detection
- RIEGL miniVUX, YellowScan, or similar
- Balance of capability and feasibility

---

### D7: Ground Truth Protocol

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Plot-based** | Fixed plots (20x20m or 30x30m), all trees identified | Standard; comparable to FSI; comprehensive | Time consuming; limited spatial coverage | None |
| **B: Individual Tree** | GPS-tagged individual reference trees only | Precise; direct validation; efficient | Labor intensive for large numbers; access issues | None |
| **C: Hybrid** | Plots + additional individual reference trees | Balanced; multi-scale validation; flexible | Moderate effort; requires planning | None |

**Recommendation**: Option C (Hybrid)
- Plot-level for species composition and density
- Individual reference trees for spectral library development
- Compatible with forest inventory standards
- Enables both pixel-level and object-based validation

---

### D8: Structural Parameters to Extract

| Parameter | Priority | Measurement Method | Validation Approach |
|-----------|----------|-------------------|---------------------|
| **Canopy Height** | Critical | LiDAR CHM | Field measurements (clinometer, rangefinder) |
| **Crown Area/Diameter** | High | Crown delineation from LiDAR/HSI | Field measurements |
| **Tree Density** | High | Individual tree detection | Plot counts |
| **Crown Volume** | Medium | 3D crown modeling | Allometric relationships |
| **DBH (estimated)** | Medium | Height-DBH allometry | Field measurements |
| **Canopy Cover** | Medium | Point density analysis | Hemispherical photography |
| **Vertical Structure** | Medium | LiDAR height distribution | Visual assessment |
| **LAI** | Low | Spectral indices + LiDAR | LAI-2200 measurements |

**Recommendation**: Focus on top 5 (Canopy Height, Crown Area, Tree Density, Crown Volume, DBH estimation)
- Most relevant for forest management
- Directly derivable from HSI-LiDAR
- Well-established validation methods

---

### D9: Evaluation Metrics

| Metric Category | Metrics | Rationale |
|-----------------|---------|-----------|
| **Classification** | Overall Accuracy (OA), Kappa, F1-score (macro, weighted) | Standard; comprehensive |
| **Per-class** | Producer's Accuracy, User's Accuracy, Per-class F1 | Species-level performance |
| **Statistical** | McNemar's test, confidence intervals (bootstrap) | Significance validation |
| **Computational** | Inference time, model parameters, FLOPS, memory | Operational feasibility |
| **Structural** | RMSE, MAE, R², bias for each parameter | Regression accuracy |

**Recommendation**: All above metrics
- OA and Kappa as primary classification metrics
- Per-class F1 for species analysis
- McNemar's for baseline comparisons
- RMSE and R² for structural parameters

---

### D10: Satellite Data Strategy

| Option | Data Source | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: HySIS Only** | ISRO HySIS (55 bands, 30m, VNIR) | Operational; accessible; Indian | Limited spectral range; coarse resolution | High - data request required |
| **B: AVIRIS-NG Only** | NASA-ISRO campaigns (425 bands, 4-8m) | High spectral resolution; proven quality | Limited coverage; campaign-based | Medium - data availability |
| **C: Both** | HySIS + AVIRIS-NG | Comprehensive; multi-scale | Complex data management | High |
| **D: UAV Primary, Satellite Secondary** | Focus on UAV; satellite for scaling demo | Controlled experiments; realistic scope | Scaling validation limited | Low initial; High later |

**Recommendation**: Option D initially, transitioning to C
- Establish methodology with UAV data (controlled)
- Scale to satellite for validation and operational demo
- Formal ISRO data requests in parallel (early submission)

---

## ISRO Dependency Summary

| Dependency Type | Items | Priority | Lead Time |
|-----------------|-------|----------|-----------|
| **Satellite Data** | HySIS scenes over study area; AVIRIS-NG archive | High | 3-6 months |
| **HPC Access** | GPU resources for training | Medium | 1-2 months |
| **Technical Collaboration** | SAC expertise; sensor calibration advice | Medium | 2-3 months |
| **Future Mission Inputs** | HySIS-2 specs; LiDAR satellite plans | Low | Ongoing |

---

## Locked Decisions Summary

| ID | Decision | Selection | Lock Status |
|----|----------|-----------|-------------|
| D1 | Study Area | Three Districts (East Khasi Hills, West Garo Hills, Ri-Bhoi) | 🔒 LOCKED |
| D2 | Species Count | 20-25 species | 🔒 LOCKED |
| D3 | Architecture | Hybrid CNN-Transformer with comparison study | 🔒 LOCKED |
| D4 | Fusion Strategy | Systematic evaluation of all strategies | 🔒 LOCKED |
| D5 | HSI Sensor | VNIR-SWIR capable (target full range) | 🔓 PENDING (budget/availability) |
| D6 | LiDAR Sensor | Multi-return, high density (50+ pts/m²) | 🔓 PENDING (budget) |
| D7 | Ground Truth | Hybrid plot + individual tree | 🔒 LOCKED |
| D8 | Structural Params | Height, Crown area, Density, Volume, DBH | 🔒 LOCKED |
| D9 | Metrics | Full suite (classification + structural) | 🔒 LOCKED |
| D10 | Satellite Data | UAV primary; satellite scaling | 🔒 LOCKED |

---

## Decision Impact on SLR

With these decisions locked, the SLR can now focus on:

1. **Tropical forest HSI-LiDAR fusion** (not general fusion)
2. **CNN-Transformer hybrid architectures** (not pure CNN review only)
3. **Species-level classification** (not land cover mapping)
4. **Structural parameter extraction** from remote sensing
5. **UAV-based studies** with satellite scaling
6. **Indian/Asian tropical forests** (priority) + other tropical forests
7. **Multi-task learning** (classification + regression)

---

## Pre-SLR Preparation Checklist

- [x] Study area defined
- [x] Target species count determined
- [x] Architecture approach selected
- [x] Fusion strategy scope defined
- [ ] Sensor specifications finalized (pending budget)
- [x] Ground truth protocol designed
- [x] Evaluation metrics selected
- [x] Satellite data strategy defined

---

## Phase Status
**LOCK DECISIONS COMPLETE** ✓

**→ Proceed to PHASE 2: Systematic Literature Review**
