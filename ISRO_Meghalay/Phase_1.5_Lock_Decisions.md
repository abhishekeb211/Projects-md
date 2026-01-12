# PHASE 1.5: Lock Decisions

## Pre-Phase 2 Decision Requirements

Before initiating the Systematic Literature Review (SLR), the following decisions must be locked to avoid wasted effort and ensure focused literature search.

---

## Decision Matrix

### D1: Study Area Scope

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Single District** | Focus on one district (e.g., East Khasi Hills) | Deep analysis; manageable logistics | Limited generalization; narrow scope | None |
| **B: Three Districts** | East Khasi Hills + West Garo Hills + Ri-Bhoi | Diverse forest types; good coverage | Moderate logistics; increased field work | May need multiple AVIRIS-NG scenes |
| **C: All Meghalaya** | State-wide sampling across 11 districts | Maximum generalization; comprehensive | High cost; complex logistics; extended timeline | Extensive satellite coverage needed |

**Recommendation**: Option B (Three Districts)
- Covers subtropical broadleaf, tropical semi-evergreen, and pine forests
- Feasible within 24-month timeline
- Aligned with AVIRIS-NG campaign coverage

---

### D2: Target Species Count

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: 10-15 species** | Dominant canopy species only | Easier validation; cleaner dataset | Limited biodiversity representation | Sufficient for mission validation |
| **B: 20-25 species** | Major canopy + understory species | Good balance; demonstrates scalability | Moderate field effort | Good for HySIS utility demo |
| **C: 30+ species** | Comprehensive inventory | Maximum scientific value | High complexity; species confusion likely | Excellent for future missions |

**Recommendation**: Option B (20-25 species)
- Captures ecological diversity
- Achievable with botanical collaboration
- Demonstrates practical utility

---

### D3: Deep Learning Architecture

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Pure CNN** | 3D-CNN for HSI + PointNet for LiDAR | Proven; interpretable | May miss long-range dependencies | None |
| **B: Pure Transformer** | ViT-style for both modalities | State-of-art; attention weights | Data hungry; computationally expensive | HPC access helpful |
| **C: Hybrid CNN-Transformer** | CNN feature extraction + Transformer fusion | Best of both; efficient | Architecture complexity | HPC access helpful |

**Recommendation**: Option C (Hybrid CNN-Transformer)
- HyLiFormer architecture
- Efficient feature extraction with global context
- Interpretable attention maps

---

### D4: Fusion Strategy (For Systematic Evaluation)

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Early Fusion** | Concatenate raw/low-level features | Simple; joint learning | Modality dominance risk | None |
| **B: Mid Fusion** | Fuse intermediate representations | Balanced; flexible | Architecture design complexity | None |
| **C: Late Fusion** | Combine decision-level outputs | Modality-specific optimization | Suboptimal joint patterns | None |
| **D: Evaluate All** | Systematic comparison | Scientific rigor; comprehensive | Increased experiments | None |

**Recommendation**: Option D (Evaluate All)
- Addresses RQ-T2 directly
- Provides generalizable insights
- Standard practice in fusion research

---

### D5: UAV Sensor Selection

| Option | Specifications | Pros | Cons | ISRO Dependency |
|--------|---------------|------|------|-----------------|
| **A: Headwall Nano-Hyperspec** | 270 bands, 400-1000nm, 640 px | Compact; proven | VNIR only; no SWIR | Good for HySIS comparison |
| **B: Specim AFX-10** | 224 bands, 400-1000nm, 1024 px | High resolution; robust | VNIR only | Good for HySIS comparison |
| **C: HySpex Mjolnir VS-620** | 620 bands, 400-2500nm | Full VNIR-SWIR; comprehensive | Heavy; expensive | Excellent for AVIRIS-NG comparison |
| **D: Custom Integration** | Mix sensors for coverage | Flexible; optimized | Integration challenges | Variable |

**Recommendation**: Option C or partnership with existing facility
- SWIR critical for species discrimination
- Aligns with AVIRIS-NG spectral range
- SAC/IIRS may have suitable equipment

---

### D6: LiDAR Specifications

| Option | Specifications | Pros | Cons | ISRO Dependency |
|--------|---------------|------|------|-----------------|
| **A: DJI Zenmuse L1** | 240m range, 240k pts/sec | Integrated; affordable | Limited penetration | None |
| **B: RIEGL miniVUX** | 250m range, 100k pts/sec | High accuracy; multi-return | Expensive; heavier | None |
| **C: YellowScan Mapper+** | 100m range, 300k pts/sec | Good penetration; compact | Mid-range specs | None |

**Recommendation**: Option B (RIEGL miniVUX) or equivalent
- Multi-return essential for canopy penetration
- High point density for individual tree detection

---

### D7: Ground Truth Protocol

| Option | Description | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: Plot-based** | Fixed plots (20x20m), all trees identified | Standard; comparable | Time consuming; limited spatial coverage | None |
| **B: Individual Tree** | GPS-tagged individual trees | Precise; direct validation | Labor intensive; access issues | None |
| **C: Hybrid** | Plots + individual reference trees | Balanced; multi-scale validation | Moderate effort | None |

**Recommendation**: Option C (Hybrid)
- Plot-level for species composition
- Individual trees for spectral library
- Comparable to forest inventory standards

---

### D8: Evaluation Metrics

| Metric Category | Metrics | Rationale |
|-----------------|---------|-----------|
| **Classification** | Overall Accuracy (OA), Kappa, F1-score | Standard; comprehensive |
| **Per-class** | Producer's Accuracy, User's Accuracy, Per-class F1 | Species-level performance |
| **Statistical** | McNemar's test, confidence intervals | Significance validation |
| **Computational** | Inference time, model parameters, FLOPS | Operational feasibility |

**Recommendation**: All above metrics
- OA and Kappa as primary
- Per-class F1 for species analysis
- McNemar's for baseline comparisons

---

### D9: Satellite Data Strategy

| Option | Data Source | Pros | Cons | ISRO Dependency |
|--------|-------------|------|------|-----------------|
| **A: HySIS Only** | ISRO HySIS (55 bands, 30m) | Operational; accessible | Limited spectral range | High - data request required |
| **B: AVIRIS-NG Only** | NASA-ISRO campaigns (425 bands, 4-8m) | High spectral resolution | Limited coverage; campaign-based | Medium - data availability |
| **C: Both** | HySIS + AVIRIS-NG | Comprehensive; multi-scale | Complex data management | High |
| **D: UAV Primary, Satellite Secondary** | Focus on UAV; satellite for scaling demo | Controlled experiments | Scaling validation limited | Low initial; High later |

**Recommendation**: Option D initially, transitioning to C
- Establish methodology with UAV data
- Scale to satellite for validation
- Formal ISRO data requests in parallel

---

## ISRO Dependency Summary

| Dependency Type | Items | Priority | Lead Time |
|-----------------|-------|----------|-----------|
| **Satellite Data** | HySIS scenes; AVIRIS-NG archives | High | 3-6 months |
| **HPC Access** | Training infrastructure | Medium | 1-2 months |
| **Technical Collaboration** | SAC expertise; sensor calibration | Medium | 2-3 months |
| **Future Mission Inputs** | HySIS-2 specs; LiDAR satellite plans | Low | Ongoing |

---

## Locked Decisions Summary

| ID | Decision | Selection | Lock Status |
|----|----------|-----------|-------------|
| D1 | Study Area | Three Districts (East Khasi Hills, West Garo Hills, Ri-Bhoi) | 🔒 LOCKED |
| D2 | Species Count | 20-25 species | 🔒 LOCKED |
| D3 | Architecture | Hybrid CNN-Transformer (HyLiFormer) | 🔒 LOCKED |
| D4 | Fusion Strategy | Systematic evaluation of all strategies | 🔒 LOCKED |
| D5 | HSI Sensor | VNIR-SWIR capable (HySpex or equivalent) | 🔓 PENDING (budget) |
| D6 | LiDAR Sensor | Multi-return, high density | 🔓 PENDING (budget) |
| D7 | Ground Truth | Hybrid plot + individual tree | 🔒 LOCKED |
| D8 | Metrics | OA, Kappa, F1, McNemar's | 🔒 LOCKED |
| D9 | Satellite Data | UAV primary; satellite scaling | 🔒 LOCKED |

---

## Decision Impact on SLR

With these decisions locked, the SLR can now focus on:

1. **Tropical forest HSI-LiDAR fusion** (not general fusion)
2. **CNN-Transformer hybrid architectures** (not pure CNN review)
3. **Species-level classification** (not land cover mapping)
4. **UAV-based studies** with satellite scaling
5. **Indian/Asian tropical forests** (priority) + other tropical forests

---

## Phase Status
**LOCK DECISIONS COMPLETE** ✓

**→ Proceed to PHASE 2: Systematic Literature Review**
