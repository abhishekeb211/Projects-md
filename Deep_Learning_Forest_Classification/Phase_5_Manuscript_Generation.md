# PHASE 5: Manuscript Generation

## Document Metadata

| Field | Value |
|-------|-------|
| **Format** | IEEE Transactions (two-column) / Elsevier |
| **Citation Style** | IEEE Numbered / Author-Date |
| **Target Length** | 12-15 pages |

---

## ISRO Format B Complete Draft

### B-1: Title

**Deep Learning Framework for Multi-sensor Forest Species Classification and Structural Parameter Extraction using UAV Hyperspectral-LiDAR Fusion in Meghalaya**

---

### B-2: Summary (≤200 words)

This research proposes developing an advanced deep learning framework for forest species classification, structural parameter extraction, and biodiversity mapping in Meghalaya using fused UAV-based hyperspectral imagery (HSI) and LiDAR data. Traditional forest monitoring relies on optical imagery and labor-intensive field surveys, failing to capture the spectral-structural complexity of dense tropical forests.

The proposed framework exploits detailed spectral signatures (200+ bands) from hyperspectral sensors combined with 3D structural information from LiDAR for fine-grained species discrimination and canopy structure analysis. A hybrid deep learning architecture incorporating CNN-based feature extraction, transformer attention mechanisms, and cross-modal fusion will be developed and validated across diverse forest types in Meghalaya.

Key deliverables include: species distribution maps with >85% classification accuracy for 25+ tree species, forest structural parameter extraction (canopy height, crown area, biomass indicators), spectral-structural library for Meghalaya forests, and an operational GIS-based Decision Support System (DSS). The research directly supports ISRO's Space Vision 2047 objectives, providing validated methodology for HySIS and AVIRIS-NG data applications.

**Word Count: 172**

---

### B-3: Objectives

#### Primary Objective
Develop a hybrid deep learning framework for accurate forest species classification and structural parameter extraction using fused hyperspectral and LiDAR data.

#### Technical Objectives
1. Design spectral-spatial-structural feature fusion architecture achieving >85% species classification accuracy
2. Develop automated UAV data processing pipeline for HSI-LiDAR co-registration
3. Create species-specific spectral-structural libraries for 25+ dominant tree species
4. Implement multi-task learning for joint classification and structural parameter extraction
5. Develop algorithms for canopy height, crown area, and biomass indicator extraction

#### System Objectives
1. Build operational GIS-based Decision Support System (DSS)
2. Establish data fusion protocols compatible with ISRO satellite products
3. Create replicable framework for other biodiversity hotspots

#### Validation Objectives
1. Comprehensive ground-truth collection (≥500 field plots)
2. Validate against expert botanical identification
3. Demonstrate cross-site generalization
4. Evaluate UAV to satellite scaling

---

### B-4: State of the Art

#### Historical Context
Remote sensing-based forest monitoring in India evolved from Landsat MSS (1980s) through IRS-1A (1988) to Resourcesat missions. National vegetation type mapping achieved 78% accuracy (Roy et al., 2015).

#### Current State: Hyperspectral
ISRO's HySIS (2018) provides 55 VNIR bands at 30m. AVIRIS-NG campaigns acquired 425-band data. Applications remain limited to spectral analysis without deep learning for species classification.

#### Current State: Deep Learning
Significant advances from 3D-CNN through HybridSN to SpectralFormer. Application to forest species limited, especially for tropical Asian forests with no published studies combining HSI-LiDAR deep learning.

#### Research Gap
No integrated framework for: (1) joint spectral-structural learning, (2) tropical Asian forests, (3) ISRO data validation, (4) simultaneous classification and parameter extraction.

#### ISRO Relevance
Supports Space Vision 2047: EO applications, AI-driven analytics, multi-mission integration, hyperspectral utility demonstration.

---

### B-5: Approach/Methodology

#### Phase 1: Data Acquisition (Months 1-8)
- UAV campaigns across 3 districts
- HSI sensor: VNIR-SWIR (380-2500nm, 200+ bands)
- LiDAR: Multi-return, 50+ pts/m²
- Ground-truth: 500+ plots with BSI collaboration

#### Phase 2: Algorithm Development (Months 6-14)
- Preprocessing pipeline (atmospheric correction, LiDAR processing)
- Hybrid CNN-Transformer architecture
- Cross-modal attention fusion
- Multi-task heads for classification + structure

#### Phase 3: Validation (Months 12-20)
- Spatially-blocked cross-validation
- Baseline comparisons (8+ methods)
- Ablation studies
- Satellite scaling experiments

#### Phase 4: DSS Development (Months 16-22)
- System architecture
- Web interface
- ISRO Bhuvan integration
- User testing

#### Phase 5: Documentation (Months 20-24)
- Dataset release
- Publications
- Technology transfer

---

### B-6: Data Reduction/Analysis

#### Input Data

| Type | Volume/Site | Total |
|------|-------------|-------|
| Raw HSI | ~50 GB | 150 GB |
| Raw LiDAR | ~100 GB | 300 GB |
| Satellite | ~15 GB | 45 GB |

#### Processing Pipeline
1. Radiometric/atmospheric correction
2. LiDAR ground classification, normalization
3. Sub-pixel co-registration
4. Sample extraction
5. Model training/inference

#### Outputs

| Product | Format |
|---------|--------|
| Species Maps | GeoTIFF (25-class) |
| Structural Maps | GeoTIFF (height, crown) |
| Confidence Maps | GeoTIFF |
| Spectral Library | CSV/HDF5 |
| DSS | Web service |

---

### B-7: Facilities Required

#### From Institute
- GPU cluster (training)
- GIS software
- Field equipment

#### From ISRO
- HySIS/AVIRIS-NG data
- Technical consultation
- HPC access (if needed)
- Bhuvan integration support

---

### B-8: Time Schedule

| Phase | Months |
|-------|--------|
| Literature review, planning | 1-2 |
| UAV campaign preparation | 2-4 |
| Data acquisition | 4-10 |
| Ground-truth collection | 4-12 |
| Preprocessing development | 6-10 |
| Algorithm implementation | 8-14 |
| Training and validation | 12-18 |
| DSS development | 14-20 |
| Satellite scaling | 16-20 |
| User testing | 18-22 |
| Documentation | 20-24 |

**Total Duration: 24 months**

---

### B-9: Expected Outcomes

#### Scientific
- 2-3 journal papers
- 2 conference papers
- MeghalayaForest-25 dataset
- Spectral-structural library

#### Technical
- Open-source implementation
- Operational DSS
- Processing protocols

#### Capacity Building
- 2-3 research scholars trained
- Forest department workshop
- Technology transfer

---

### B-10: Budget Summary

| Category | Year 1 | Year 2 | Total |
|----------|--------|--------|-------|
| Equipment | 15 | 5 | 20 |
| Consumables | 8 | 8 | 16 |
| Travel/Field | 12 | 8 | 20 |
| Contingency | 3 | 3 | 6 |
| Overhead | 4 | 4 | 8 |
| **Total (₹ Lakhs)** | **42** | **28** | **70** |

---

## Placeholder Registry

| ID | Description | Status |
|----|-------------|--------|
| `\result{main_oa}` | Overall accuracy | Pending |
| `\result{main_kappa}` | Kappa coefficient | Pending |
| `\result{ablation_*}` | Ablation results | Pending |
| `\result{height_r2}` | Height R² | Pending |
| `\result{cross_site}` | Cross-site OA | Pending |
| `\result{scale_*}` | Scaling results | Pending |

---

## Phase Status
**PHASE 5: MANUSCRIPT GENERATION COMPLETE** ✓

**→ Proceed to PHASE 6: Rigor & Review Simulation**
