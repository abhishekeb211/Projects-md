# PHASE 0: Initialize – Research Ledger Setup

## Project Metadata

| Field | Value |
|-------|-------|
| **Project ID** | ISRO-DL-FOREST-MEGHALAYA-2026 |
| **Date Initiated** | January 13, 2026 |
| **Depth Mode** | Deep |
| **Phase Status** | Initialized |

---

## Project Inputs

### Research Idea (Raw)
Deep Learning approach for tree species identification and structural parameter extraction in selected sites of Meghalaya using Unmanned Aerial Vehicle hyperspectral and LiDAR image data. Development of a Deep-learning-based framework integrating UAV hyperspectral and LiDAR imagery for:
- Tree species identification
- Biodiversity mapping
- Forest type classification
- Structural parameter extraction
- Canopy health assessment

### Domain/Area
| Level | Domain |
|-------|--------|
| **Primary** | Remote Sensing & Earth Observation |
| **Secondary** | Deep Learning / Computer Vision |
| **Tertiary** | Forest Ecology & Biodiversity Conservation |
| **Geographic Focus** | Meghalaya, Northeast India (Indo-Burma Biodiversity Hotspot) |

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
| International Journal of Applied Earth Observation | Journal | Q1, IF ~7.6 | Very Good |
| Ecological Informatics | Journal | Q1, IF ~5.8 | Good |
| IGARSS 2027 | Conference | Top RS Conference | Good |

### Constraints

| Constraint Type | Details | Mitigation |
|-----------------|---------|------------|
| **Time** | 24-36 months (typical ISRO RESPOND cycle) | Phased deliverables |
| **Compute** | GPU cluster required for deep learning | ISRO HPC / Cloud GPU allocation |
| **Data** | UAV flights require permits; monsoon limitations | Pre-monsoon campaigns (Oct-May) |
| **Ethics** | Forest area access; tribal land considerations | MoEFCC clearance; community engagement |
| **Tools** | Hyperspectral processing software licenses | ENVI, ERDAS; open-source alternatives (QGIS, Python) |
| **ISRO Dependency** | HySIS/AVIRIS-NG data availability | Formal data request; backup with UAV-only |
| **Field Access** | Dense forest terrain; remote locations | Local collaborators; phased campaigns |

### Preferred Contribution Style
**New Method + System + Benchmark**
- Novel hybrid deep learning architecture for spectral-spatial-structural fusion
- Operational GIS-based Decision Support System (DSS)
- Benchmark dataset for Meghalaya forest species
- Spectral-structural library for dominant tree species

### Evaluation Setting
**Mixed: Real-world UAV + Satellite + Ground Truth**
- UAV-based hyperspectral and LiDAR acquisition
- ISRO satellite data (HySIS, AVIRIS-NG campaigns)
- Extensive ground-truth collection (field surveys with BSI collaboration)
- Validation against expert botanical identification

### Citation Style
- **IEEE** (primary for TGRS/GRSL)
- **Elsevier/APA** (for RSE, ISPRS, Ecological Informatics)

---

## ISRO Format B – Sections 1-3 (Pre-filled)

### Format B-1: Title
**"Deep Learning Framework for Multi-sensor Forest Species Classification and Structural Parameter Extraction using UAV Hyperspectral-LiDAR Fusion in Meghalaya"**

**Alternative Titles:**
1. "Hybrid Deep Learning Architecture for Tree Species Identification from UAV Hyperspectral and LiDAR Data in Meghalaya's Forests"
2. "UAV-based Forest Species Mapping using Deep Learning: Integrating Hyperspectral Imagery and LiDAR for Biodiversity Assessment in Northeast India"

### Format B-2: Summary (≤200 words)

This research proposes developing an advanced deep learning framework for forest species classification, structural parameter extraction, and biodiversity mapping in Meghalaya using fused UAV-based hyperspectral imagery (HSI) and LiDAR data. Traditional forest monitoring relies on optical imagery and labor-intensive field surveys, failing to capture the spectral-structural complexity of dense tropical forests.

The proposed framework exploits detailed spectral signatures (400+ bands) from hyperspectral sensors combined with 3D structural information from LiDAR for fine-grained species discrimination and canopy structure analysis. A hybrid deep learning architecture incorporating spectral-spatial feature extraction, structural parameter modeling, and multi-modal data fusion will be developed and validated across diverse forest types in Meghalaya.

Key deliverables include: species distribution maps with classification accuracy >85%, forest structural parameter extraction (canopy height, crown density, biomass indicators), canopy health assessment protocols, spectral-structural library for 20+ dominant tree species, and an operational GIS-based Decision Support System (DSS). The research directly supports ISRO's Space Vision 2047 objectives, providing validated methodology for HySIS and AVIRIS-NG data applications and a replicable framework for integration with upcoming hyperspectral/LiDAR satellite missions.

**Word Count: 185**

### Format B-3: Objectives

#### 1. Primary Objective
Develop a hybrid deep learning framework for accurate forest species classification and structural parameter extraction using fused hyperspectral and LiDAR data from UAV platforms.

#### 2. Technical Objectives
- Design spectral-spatial-structural feature fusion architecture achieving >85% species classification accuracy
- Develop automated UAV data processing pipeline for hyperspectral-LiDAR co-registration
- Create species-specific spectral-structural libraries for 20+ dominant tree species of Meghalaya
- Implement algorithms for forest structural parameter extraction (canopy height, crown area, biomass indicators)
- Develop canopy health assessment protocols using spectral indices and structural metrics

#### 3. System Objectives
- Build operational GIS-based Decision Support System (DSS) for forest monitoring
- Establish data fusion protocols compatible with ISRO satellite products (HySIS, AVIRIS-NG)
- Create replicable framework applicable to other Indian biodiversity hotspots
- Integrate UAV data acquisition, processing, and output generation workflows

#### 4. Validation Objectives
- Conduct comprehensive ground-truth data collection (≥500 field plots)
- Validate classification accuracy against expert botanical identification
- Demonstrate transferability across different forest types within Meghalaya
- Evaluate scaling from UAV to satellite resolution

---

## Research Ledger v0 (Initial)

### Definitions

| Term | Definition |
|------|------------|
| HSI | Hyperspectral Imagery (typically 100-400+ contiguous spectral bands) |
| LiDAR | Light Detection and Ranging (3D point cloud data) |
| CHM | Canopy Height Model (LiDAR-derived raster of vegetation height) |
| DSM | Digital Surface Model (elevation including objects) |
| DTM | Digital Terrain Model (bare earth elevation) |
| DSS | Decision Support System |
| TRL | Technology Readiness Level (NASA 1-9 scale) |
| NDVI | Normalized Difference Vegetation Index |
| LAI | Leaf Area Index |
| AGB | Above Ground Biomass |

### Assumptions (To Be Validated)

- [ ] UAV flight permits obtainable for Meghalaya forest areas
- [ ] Sufficient spectral separability exists between target species in VNIR-SWIR range
- [ ] Ground-truth collection feasible in dense forest terrain
- [ ] ISRO data products (HySIS/AVIRIS-NG) available within project timeline
- [ ] LiDAR penetration adequate in dense canopy conditions
- [ ] Deep learning outperforms traditional ML for this task
- [ ] 20+ species coverage sufficient for demonstrating framework utility

### Decisions Log

| Decision | Status | Date |
|----------|--------|------|
| Study area selection | Pending | - |
| Deep learning architecture | Pending | - |
| UAV sensor specifications | Pending | - |
| Number of target species | Pending | - |
| Fusion strategy | Pending | - |
| Ground-truth protocol | Pending | - |

### Baselines (Initial)

| Baseline | Type | Rationale |
|----------|------|-----------|
| Random Forest on spectral features | Traditional ML | Widely used benchmark |
| SVM with RBF kernel | Traditional ML | Strong baseline |
| Standard CNN (2D) on HSI cubes | Deep Learning | Basic DL approach |
| Existing LULC products (NRSC Bhuvan) | Reference | Current operational baseline |
| Field-based inventory | Ground Truth | Gold standard |

---

## Key Research Themes

### 1. UAV Data Handling & Information Extraction
- Hyperspectral data preprocessing (atmospheric correction, geometric correction)
- LiDAR point cloud processing (filtering, classification, normalization)
- Multi-sensor data co-registration and alignment
- Quality control and data validation protocols

### 2. Data Fusion Techniques
- Early fusion (feature concatenation)
- Mid-level fusion (encoder-level integration)
- Late fusion (decision-level combination)
- Attention-based cross-modal fusion
- Comparison of fusion strategies for species discrimination

### 3. Species Classification & Structural Parameter Extraction
- Spectral signature analysis and band selection
- 3D structural feature extraction from LiDAR
- Hybrid deep learning architecture design
- Individual tree detection and crown delineation
- Biomass and carbon stock estimation

### 4. Ground-based Validation
- Field plot design and sampling strategy
- Species identification protocols
- Reference tree measurements
- GPS/GNSS positioning for accurate co-registration
- Seasonal variation documentation

### 5. Replicable Framework Development
- Modular software architecture
- Documentation and user guides
- Training materials for stakeholders
- Integration pathways with ISRO systems

---

## ISRO Relevance Mapping

| Project Component | ISRO Mission/Program | Relevance Level |
|-------------------|---------------------|-----------------|
| Hyperspectral processing | HySIS | Critical |
| Airborne HSI methods | AVIRIS-NG | High |
| Forest mapping | Resourcesat/LISS | Medium |
| DSS development | Bhuvan platform | High |
| AI/ML algorithms | ISRO AI initiative | High |
| Biodiversity mapping | ISRO Earth Observation | High |
| Future mission prep | HySIS-2, LiDAR satellite | Strategic |

---

## Risk Register (Initial)

| Risk ID | Risk Description | Probability | Impact | Mitigation |
|---------|------------------|-------------|--------|------------|
| R1 | UAV permit delays | Medium | High | Early application; multiple sites |
| R2 | Monsoon disruption | High | High | Pre-monsoon campaign planning |
| R3 | Dense canopy LiDAR penetration | Medium | Medium | Full-waveform LiDAR; multi-return |
| R4 | Species identification errors | Medium | High | BSI collaboration; voucher specimens |
| R5 | ISRO data availability | Low | Medium | Formal request; UAV-only backup |
| R6 | Computational resource constraints | Low | Medium | ISRO HPC access; cloud alternatives |

---

## Next Phase
**→ Proceed to PHASE 1: Idea Refinement & Research Foundation**

---

## Phase Status
**PHASE 0: INITIALIZE COMPLETE** ✓
