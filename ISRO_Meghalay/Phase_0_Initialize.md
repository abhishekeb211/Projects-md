# PHASE 0: Initialize – Research Ledger Setup

## Project Metadata

| Field | Value |
|-------|-------|
| **Project ID** | ISRO-MEGHALAYA-HSI-LIDAR-2026 |
| **Date Initiated** | January 12, 2026 |
| **Depth Mode** | Deep |
| **Phase Status** | Initialized |

---

## Project Inputs

### Research Idea (Raw)
Development of a Deep-learning-based framework integrating UAV hyperspectral and LiDAR imagery for tree species identification, biodiversity mapping, and forest type classification in Meghalaya, India.

### Domain/Area
- **Primary**: Remote Sensing & Earth Observation
- **Secondary**: Deep Learning / Computer Vision
- **Tertiary**: Forest Ecology & Biodiversity Conservation
- **Geographic Focus**: Meghalaya, Northeast India (biodiversity hotspot)

### Paper Type
**Mixed (Empirical + Systems)**
- Empirical: Experimental validation on real UAV/satellite data
- Systems: Development of operational DSS framework

### Target Venue (Options)
| Venue | Type | Impact | Fit |
|-------|------|--------|-----|
| Remote Sensing of Environment | Journal | Q1, IF ~13.5 | Excellent |
| ISPRS Journal of Photogrammetry and Remote Sensing | Journal | Q1, IF ~12.7 | Excellent |
| IEEE Transactions on Geoscience and Remote Sensing | Journal | Q1, IF ~8.2 | Very Good |
| IGARSS 2026 | Conference | Top RS Conference | Good |
| CVPR (Earth Vision Workshop) | Workshop | Top CV Venue | Good |

### Constraints

| Constraint Type | Details | Mitigation |
|-----------------|---------|------------|
| **Time** | 24-36 months (typical ISRO RESPOND cycle) | Phased deliverables |
| **Compute** | GPU cluster required for deep learning | ISRO HPC / Cloud GPU |
| **Data** | UAV flights require permits; monsoon limitations | Pre-monsoon campaigns (Oct-May) |
| **Ethics** | Forest area access; tribal land considerations | MoEFCC clearance; community engagement |
| **Tools** | Hyperspectral processing software licenses | ENVI, ERDAS; open-source alternatives |
| **ISRO Dependency** | HySIS/AVIRIS-NG data availability | Formal data request; backup with UAV-only |

### Preferred Contribution Style
**New Method + System + Benchmark**
- Novel hybrid deep learning architecture (spectral-spatial-structural fusion)
- Operational GIS-based Decision Support System
- Benchmark dataset for Meghalaya forest species

### Evaluation Setting
**Mixed: Real-world UAV + Satellite + Ground Truth**
- UAV-based hyperspectral and LiDAR acquisition
- ISRO satellite data (HySIS, AVIRIS-NG campaigns)
- Extensive ground-truth collection (field surveys)

### Citation Style
**IEEE** (primary for TGRS/GRSL)
**Elsevier/APA** (for RSE, ISPRS)

---

## ISRO Format B – Sections 1-3 (Pre-filled)

### Format B-1: Title
**"Deep Learning Framework for Multi-sensor Forest Species Classification and Biodiversity Mapping using UAV Hyperspectral-LiDAR Fusion in Meghalaya"**

### Format B-2: Summary (≤200 words)
This research proposes the development of an advanced deep learning framework for forest species classification and biodiversity mapping in Meghalaya using fused UAV-based hyperspectral imagery (HSI) and LiDAR data. Traditional forest monitoring relies on optical imagery and labor-intensive field surveys, which fail to capture the spectral-structural complexity of dense tropical forests. The proposed framework will exploit detailed spectral signatures (400+ bands) from hyperspectral sensors combined with 3D structural information from LiDAR to enable fine-grained species discrimination.

A hybrid deep learning architecture will be developed incorporating: (1) spectral feature extraction using 1D/3D CNNs, (2) spatial context modeling via attention mechanisms, and (3) structural parameter integration from LiDAR-derived canopy height models. The framework will be trained and validated using extensive ground-truth data collected across diverse forest types in Meghalaya.

Key deliverables include: species distribution maps, canopy health assessment protocols, and an operational GIS-based Decision Support System (DSS). The research directly supports ISRO's Space Vision 2047 objectives and provides a replicable framework for integration with upcoming hyperspectral/LiDAR satellite missions including HySIS follow-on and NISAR vegetation products.

**Word Count: 189**

### Format B-3: Objectives

1. **Primary Objective**: Develop a hybrid deep learning framework for accurate forest species classification using fused hyperspectral and LiDAR data

2. **Technical Objectives**:
   - Design spectral-spatial-structural feature fusion architecture achieving >85% species classification accuracy
   - Develop automated UAV data processing pipeline for hyperspectral-LiDAR co-registration
   - Create species-specific spectral libraries for 20+ dominant tree species of Meghalaya
   - Implement canopy structure analysis algorithms for forest health assessment

3. **System Objectives**:
   - Build operational GIS-based Decision Support System (DSS) for forest monitoring
   - Establish data fusion protocols compatible with ISRO satellite products (HySIS, AVIRIS-NG)
   - Create replicable framework for other biodiversity hotspots

4. **Validation Objectives**:
   - Conduct comprehensive ground-truth data collection (≥500 field plots)
   - Validate classification accuracy against expert botanical identification
   - Demonstrate transferability across different forest types within Meghalaya

---

## Research Ledger v0 (Initial)

### Definitions
| Term | Definition |
|------|------------|
| HSI | Hyperspectral Imagery (typically 100-400+ contiguous spectral bands) |
| LiDAR | Light Detection and Ranging (3D point cloud data) |
| CHM | Canopy Height Model (LiDAR-derived) |
| DSS | Decision Support System |
| TRL | Technology Readiness Level |

### Assumptions (To Be Validated)
- [ ] UAV flight permits obtainable for Meghalaya forest areas
- [ ] Sufficient spectral separability exists between target species
- [ ] Ground-truth collection feasible in dense forest terrain
- [ ] ISRO data products available within project timeline

### Decisions Log
| Decision | Status | Date |
|----------|--------|------|
| Study area selection | Pending | - |
| Deep learning architecture | Pending | - |
| UAV sensor specifications | Pending | - |
| Number of target species | Pending | - |

### Baselines (Initial)
- Random Forest on spectral features
- SVM with RBF kernel
- Standard CNN (2D) on HSI cubes
- Existing LULC products (NRSC Bhuvan)

---

## Next Phase
**→ Proceed to PHASE 1: Idea Refinement & Research Foundation**
