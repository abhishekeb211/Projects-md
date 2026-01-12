# PHASE 2a: Systematic Literature Review (SLR) Protocol

## A. SLR Protocol Definition

### A.1 Review Objectives

| Objective | Description |
|-----------|-------------|
| **Primary** | Identify state-of-the-art methods for HSI-LiDAR fusion in forest species classification |
| **Secondary** | Catalog deep learning architectures applied to hyperspectral vegetation analysis |
| **Tertiary** | Document forest monitoring applications in Indian/tropical contexts |
| **Methodological** | Establish baseline performance metrics and evaluation standards |

### A.2 Sources and Databases

| Database | Type | Coverage | Priority |
|----------|------|----------|----------|
| **Web of Science** | Multidisciplinary | High-impact journals | Primary |
| **Scopus** | Multidisciplinary | Comprehensive coverage | Primary |
| **IEEE Xplore** | Engineering/CS | DL and RS methods | Primary |
| **Google Scholar** | Broad | Grey literature; preprints | Secondary |
| **arXiv** | Preprints | Latest DL methods | Secondary |
| **ISPRS Archives** | Remote Sensing | Conference proceedings | Primary |
| **NASA Technical Reports** | Space agency | AVIRIS applications | Secondary |
| **ISRO Publications** | Space agency | Indian RS applications | **Mandatory** |
| **SAC Technical Reports** | ISRO center | Hyperspectral processing | **Mandatory** |
| **URSC Technical Reports** | ISRO center | Satellite/sensor specs | **Mandatory** |

### A.3 Search Strings

#### Primary Search String
```
("hyperspectral" OR "imaging spectroscopy" OR "HSI") 
AND 
("LiDAR" OR "laser scanning" OR "ALS" OR "point cloud")
AND 
("forest" OR "tree species" OR "vegetation" OR "canopy")
AND 
("classification" OR "mapping" OR "identification" OR "deep learning")
```

#### Secondary Search Strings

**S1: Deep Learning for Hyperspectral**
```
("deep learning" OR "CNN" OR "convolutional neural network" OR "transformer" OR "attention")
AND 
("hyperspectral" OR "imaging spectroscopy")
AND 
("vegetation" OR "forest" OR "tree" OR "plant species")
```

**S2: LiDAR Forest Applications**
```
("LiDAR" OR "laser scanning" OR "ALS" OR "TLS")
AND 
("forest structure" OR "canopy height" OR "tree detection" OR "individual tree")
AND 
("classification" OR "segmentation" OR "deep learning")
```

**S3: Multi-sensor Fusion**
```
("data fusion" OR "sensor fusion" OR "multi-modal" OR "multi-source")
AND 
("hyperspectral" OR "multispectral")
AND 
("LiDAR" OR "3D" OR "point cloud")
AND 
("forest" OR "vegetation")
```

**S4: Indian Forest Remote Sensing**
```
("India" OR "Indian" OR "Meghalaya" OR "Northeast India" OR "Western Ghats")
AND 
("forest" OR "biodiversity" OR "tree species")
AND 
("remote sensing" OR "satellite" OR "hyperspectral" OR "ISRO")
```

**S5: ISRO Missions**
```
("HySIS" OR "AVIRIS-NG" OR "Resourcesat" OR "RISAT")
AND 
("vegetation" OR "forest" OR "biodiversity" OR "land cover")
```

#### Synonym Expansion

| Concept | Synonyms/Variants |
|---------|-------------------|
| Hyperspectral | imaging spectroscopy, HSI, imaging spectrometer, narrowband |
| LiDAR | laser scanning, ALS (airborne), TLS (terrestrial), point cloud, 3D |
| Deep Learning | CNN, neural network, transformer, attention, machine learning |
| Forest | woodland, tree, vegetation, canopy, stand |
| Classification | mapping, identification, discrimination, recognition |
| Fusion | integration, combination, multi-modal, multi-sensor, synergy |

### A.4 Inclusion/Exclusion Criteria

#### Inclusion Criteria

| Code | Criterion | Rationale |
|------|-----------|-----------|
| I1 | Peer-reviewed journal articles or top conference papers | Quality assurance |
| I2 | Published 2015-2026 | Relevance; DL era |
| I3 | Uses hyperspectral and/or LiDAR data | Core technology focus |
| I4 | Application to forest/vegetation | Domain relevance |
| I5 | Reports quantitative accuracy metrics | Comparability |
| I6 | English language | Accessibility |
| I7 | Full text accessible | Review feasibility |

#### Exclusion Criteria

| Code | Criterion | Rationale |
|------|-----------|-----------|
| E1 | Review/survey papers (catalog separately) | Not primary research |
| E2 | Purely agricultural applications (crops only) | Scope limitation |
| E3 | Urban vegetation without forest context | Scope limitation |
| E4 | No classification/mapping component | Methodological focus |
| E5 | Simulation-only studies | Empirical requirement |
| E6 | <10 citations AND published >3 years ago | Impact filter |

### A.5 Quality Assessment Rubric

| Criterion | Weight | Score 1 (Low) | Score 2 (Medium) | Score 3 (High) |
|-----------|--------|---------------|------------------|----------------|
| **Methodological Rigor** | 25% | Unclear methods; no validation | Standard methods; basic validation | Rigorous methods; comprehensive validation |
| **Data Quality** | 20% | Limited data; poor documentation | Adequate data; reasonable documentation | Extensive data; excellent documentation |
| **Evaluation Metrics** | 15% | Single metric; no statistics | Multiple metrics; basic statistics | Comprehensive metrics; statistical tests |
| **Reproducibility** | 15% | No code/data; insufficient details | Partial availability; adequate details | Open code/data; full reproducibility |
| **Relevance to RQs** | 15% | Tangentially related | Related to 1-2 RQs | Directly addresses multiple RQs |
| **Novelty/Impact** | 10% | Incremental; low citations | Moderate novelty; decent citations | Significant novelty; high impact |

**Scoring**: Papers scoring ≥2.0 weighted average included in detailed review

---

## B. Thematic Clusters

### Cluster 1: Deep Learning Architectures for HSI Classification
**Focus**: CNN, RNN, Transformer architectures specifically designed for hyperspectral data
**Key Topics**: 3D-CNN, spectral attention, spatial-spectral networks, SpectralFormer
**Expected Papers**: 15-20

### Cluster 2: LiDAR-based Forest Structure Analysis
**Focus**: Individual tree detection, canopy modeling, structural parameter extraction
**Key Topics**: PointNet, point cloud segmentation, CHM analysis, crown delineation
**Expected Papers**: 10-15

### Cluster 3: HSI-LiDAR Fusion Methods
**Focus**: Multi-modal fusion strategies for vegetation analysis
**Key Topics**: Early/mid/late fusion, feature-level integration, decision fusion
**Expected Papers**: 8-12

### Cluster 4: Tree Species Classification from Remote Sensing
**Focus**: Species-level discrimination using various RS data
**Key Topics**: Spectral libraries, species separability, tropical forests
**Expected Papers**: 12-18

### Cluster 5: UAV Remote Sensing for Forest Monitoring
**Focus**: UAV-based hyperspectral and LiDAR applications
**Key Topics**: Data acquisition protocols, processing pipelines, operational systems
**Expected Papers**: 10-15

### Cluster 6: ISRO & DOS Missions for Vegetation Analysis (**MANDATORY**)
**Focus**: Applications using ISRO satellite data for forest/biodiversity
**Key Topics**: HySIS, AVIRIS-NG campaigns, Resourcesat, NRSC products
**Expected Papers**: 8-12
**Additional Sources**: SAC/URSC technical reports; ISRO conference proceedings

---

## C. Paper Collection Plan

### Phase 1: Initial Database Search (Week 1-2)

| Database | Search Strings | Target Papers |
|----------|---------------|---------------|
| Web of Science | S1, S2, S3, S4 | 200-300 |
| Scopus | S1, S2, S3, S4 | 250-350 |
| IEEE Xplore | S1, S2, S3 | 100-150 |
| ISPRS Archives | S1, S2, S3, S4 | 50-80 |

**Estimated Initial Pool**: 600-880 papers (with ~40% overlap)
**After Deduplication**: ~400-500 unique papers

### Phase 2: Title/Abstract Screening (Week 2-3)

| Step | Action | Expected Retention |
|------|--------|-------------------|
| 2.1 | Apply inclusion criteria (title) | 60% |
| 2.2 | Apply inclusion criteria (abstract) | 50% |
| 2.3 | Apply exclusion criteria | 70% |

**Expected After Screening**: 80-120 papers

### Phase 3: Full-text Review (Week 3-4)

| Step | Action | Expected Retention |
|------|--------|-------------------|
| 3.1 | Full-text availability check | 95% |
| 3.2 | Quality assessment scoring | 75% |
| 3.3 | Final relevance check | 90% |

**Expected Final Corpus**: 50-80 papers

### Phase 4: Cluster Distribution

| Cluster | Target Papers | Priority |
|---------|--------------|----------|
| C1: DL for HSI | 12-15 | High |
| C2: LiDAR Forest | 8-10 | High |
| C3: HSI-LiDAR Fusion | 8-10 | Critical |
| C4: Tree Species | 10-12 | High |
| C5: UAV RS | 8-10 | Medium |
| C6: ISRO Missions | 8-10 | **Mandatory** |

### Phase 5: Snowball Sampling (Week 4-5)

**Forward Snowballing**:
- Track citations of high-quality papers (QA score ≥2.5)
- Focus on 2023-2026 papers citing seminal works

**Backward Snowballing**:
- Review references of key papers
- Identify foundational works and benchmark datasets

**Expected Additional Papers**: 10-20

### Phase 6: ISRO-Specific Collection (Parallel)

| Source | Method | Target |
|--------|--------|--------|
| ISRO website publications | Manual search | 5-8 |
| SAC Annual Reports | Document review | 3-5 |
| URSC Technical Documents | Request/search | 2-3 |
| Indian RS conferences (ISRS, ISPRS-India) | Proceedings search | 5-10 |
| NRSC technical bulletins | Direct contact | 3-5 |

---

## D. Data Management

### Reference Management
- **Tool**: Zotero with Better BibTeX plugin
- **Organization**: Folders by cluster; tags for cross-cutting themes
- **Naming**: `[FirstAuthor]_[Year]_[ShortTitle]`

### Paper Tracking Spreadsheet

| Column | Description |
|--------|-------------|
| ID | Unique identifier |
| Citation | Full citation |
| Cluster | Primary cluster assignment |
| QA_Score | Quality assessment score |
| Relevance | 1-5 relevance rating |
| Status | Screening/Reviewed/Included/Excluded |
| Notes | Key observations |
| ISRO_Applicability | TRL level for ISRO missions |

### Quality Control
- 10% random sample double-reviewed
- Disagreements resolved by discussion
- Inter-rater reliability check (Cohen's kappa ≥0.7)

---

## ISRO Cluster Special Protocol

### Mandatory Searches
```
site:isro.gov.in ("hyperspectral" OR "vegetation" OR "forest")
site:sac.gov.in ("hyperspectral" OR "vegetation" OR "forest")  
site:nrsc.gov.in ("forest" OR "biodiversity" OR "vegetation mapping")
```

### Required Inclusions
- [ ] HySIS mission overview and applications (SAC documentation)
- [ ] AVIRIS-NG India campaign reports
- [ ] Bhuvan forest products documentation
- [ ] NRSC vegetation studies
- [ ] Any RESPOND project reports on vegetation

### ISRO Mission Applicability Assessment

For each included paper, assess:

| Field | Scale | Description |
|-------|-------|-------------|
| TRL_Current | 1-9 | Current Technology Readiness Level |
| TRL_Potential | 1-9 | Potential TRL with ISRO integration |
| Mission_Fit | HySIS/AVIRIS-NG/Future | Applicable mission |
| Scalability | Low/Medium/High | Potential for satellite-scale |

---

## Timeline Summary

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1 | Database searches | Raw paper list |
| 2 | Deduplication + Title screening | Screened list |
| 3 | Abstract screening + Full-text collection | Review corpus |
| 4 | Full-text review + QA scoring | Scored papers |
| 5 | Snowballing + ISRO collection | Final corpus |
| 6 | Paper cards + Synthesis | Lit review draft |

---

## Phase Status
**PHASE 2a: SLR PROTOCOL COMPLETE** ✓

**→ Proceed to PHASE 2b: Literature Cards**
