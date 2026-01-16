# Phase 2a: Systematic Literature Review (SLR) Protocol

## Research Agent Prompt

**PHASE 2: Systematic Literature Review (SLR)**

Define the SLR protocol, propose thematic clusters, and output a Paper Collection Plan.

---

## A) SLR Protocol Definition

### A.1 Sources/Databases to Use (Field-Appropriate)

| Database | Coverage | Priority | Access |
|----------|----------|----------|--------|
| **Web of Science** | Comprehensive scientific literature | High | Institutional |
| **Scopus** | Engineering, remote sensing focus | High | Institutional |
| **IEEE Xplore** | Deep learning, signal processing | High | Institutional |
| **Google Scholar** | Broad coverage, preprints | Medium | Open |
| **ISPRS Archives** | Photogrammetry, remote sensing | High | Open |
| **arXiv (cs.CV, eess.IV)** | Latest deep learning methods | Medium | Open |
| **NASA ADS / EarthArXiv** | Earth observation literature | Medium | Open |
| **ISRO Publications** | Indian space program context | High | ISRO Portal |
| **ResearchGate** | Grey literature, preprints | Low | Open |
| **Forest Research Institute Dehradun** | Indian forestry literature | Medium | Limited |

### A.2 Search Strings + Synonyms

#### Primary Search String
```
("hyperspectral" OR "imaging spectroscopy") AND 
("LiDAR" OR "laser scanning" OR "point cloud") AND 
("forest" OR "vegetation" OR "tree species") AND 
("classification" OR "identification" OR "mapping") AND 
("deep learning" OR "neural network" OR "CNN" OR "machine learning")
```

#### Domain-Specific Search Strings

**String 1: Hyperspectral Forest Classification**
```
("hyperspectral imaging" OR "hyperspectral remote sensing") AND 
("forest classification" OR "tree species identification" OR "vegetation mapping") AND 
("deep learning" OR "convolutional neural network" OR "spectral-spatial")
```

**String 2: LiDAR Forest Structure**
```
("LiDAR" OR "airborne laser scanning" OR "ALS" OR "point cloud") AND 
("forest structure" OR "canopy height" OR "tree segmentation" OR "crown delineation") AND 
("deep learning" OR "PointNet" OR "3D CNN")
```

**String 3: Multi-Sensor Fusion**
```
("data fusion" OR "multi-modal" OR "multi-sensor") AND 
("hyperspectral" AND "LiDAR") AND 
("forest" OR "vegetation") AND 
("classification" OR "mapping")
```

**String 4: UAV Remote Sensing**
```
("UAV" OR "UAS" OR "drone" OR "unmanned aerial") AND 
("hyperspectral" OR "LiDAR") AND 
("forest" OR "vegetation" OR "tree") AND 
("classification" OR "monitoring")
```

**String 5: Deep Learning Remote Sensing**
```
("deep learning" OR "CNN" OR "transformer" OR "attention mechanism") AND 
("remote sensing" OR "hyperspectral" OR "multispectral") AND 
("classification" OR "segmentation")
```

#### Synonym Mapping

| Concept | Synonyms/Alternatives |
|---------|----------------------|
| Hyperspectral | imaging spectroscopy, hyperspectral imaging, HSI, narrowband |
| LiDAR | laser scanning, ALS, TLS, point cloud, 3D scanning |
| Forest | vegetation, woodland, canopy, tree, timber |
| Classification | identification, mapping, recognition, categorization |
| Deep Learning | neural network, CNN, DNN, transformer, attention |
| UAV | UAS, drone, unmanned aerial vehicle, RPAS |
| Fusion | integration, combination, multi-modal, multi-source |

### A.3 Inclusion/Exclusion Criteria

#### Inclusion Criteria

| ID | Criterion | Rationale |
|----|-----------|-----------|
| I1 | Published 2015-2025 | Focus on deep learning era |
| I2 | Peer-reviewed or reputable preprint | Quality assurance |
| I3 | English language | Accessibility |
| I4 | Uses hyperspectral AND/OR LiDAR for vegetation | Direct relevance |
| I5 | Employs machine learning/deep learning methods | Methodological alignment |
| I6 | Forest/vegetation application domain | Domain relevance |
| I7 | Includes quantitative evaluation | Baseline comparison potential |

#### Exclusion Criteria

| ID | Criterion | Rationale |
|----|-----------|-----------|
| E1 | Published before 2015 | Pre-deep learning methods outdated |
| E2 | Non-vegetation applications (urban, geology) | Out of scope |
| E3 | Review/survey papers (retain for background only) | Primary focus on original research |
| E4 | No quantitative results reported | Cannot extract baselines |
| E5 | Satellite-only without UAV relevance | Scope boundary |
| E6 | Agricultural crops only (no forestry) | Domain mismatch |
| E7 | Simulation-only without real data | Limited practical relevance |

### A.4 Quality Assessment Rubric

#### Quality Scoring Criteria (0-3 scale each)

| Criterion | 0 (Poor) | 1 (Fair) | 2 (Good) | 3 (Excellent) |
|-----------|----------|----------|----------|---------------|
| **Methodological Rigor** | No details | Partial description | Clear methodology | Reproducible protocol |
| **Dataset Quality** | Undefined | Small/limited | Moderate with ground truth | Large, well-documented |
| **Evaluation Completeness** | No metrics | Single metric | Multiple metrics | Comprehensive + statistical tests |
| **Novelty** | Incremental | Minor improvement | Novel component | Significant innovation |
| **Relevance to RQs** | Tangential | Partially relevant | Directly relevant | Core reference |
| **Reproducibility** | No code/data | Partial availability | Code OR data available | Full reproducibility |

**Quality Threshold:** Include papers scoring ≥8/18 for detailed review.

---

## B) Thematic Clusters for Organizing Papers

### Cluster 1: Hyperspectral Image Classification Methods
**Focus:** Deep learning architectures for hyperspectral imagery
- 3D-CNNs for spectral-spatial feature extraction
- Transformer-based hyperspectral classification
- Attention mechanisms for band selection
- Semi-supervised and self-supervised HSI methods

**Key Questions:**
- What architectures achieve SOTA on benchmark datasets?
- How do methods handle limited labeled data?
- What spectral-spatial feature representations work best?

### Cluster 2: LiDAR-Based Forest Structure Analysis
**Focus:** Deep learning for 3D point cloud processing in forestry
- Individual tree detection and segmentation
- Canopy height and structure estimation
- Crown delineation algorithms
- Forest inventory from LiDAR

**Key Questions:**
- How effective is PointNet/PointNet++ for forest applications?
- What structural parameters can be reliably extracted?
- How do methods handle varying point density?

### Cluster 3: Multi-Sensor Data Fusion Strategies
**Focus:** Methods for integrating hyperspectral and LiDAR data
- Early fusion (feature-level)
- Mid fusion (intermediate representation)
- Late fusion (decision-level)
- Cross-modal attention mechanisms

**Key Questions:**
- Which fusion strategy performs best for forest classification?
- How is complementary information leveraged?
- What are computational trade-offs?

### Cluster 4: UAV-Based Remote Sensing Systems
**Focus:** UAV platforms and data collection for forestry
- UAV hyperspectral sensors and calibration
- UAV LiDAR systems
- Flight planning for forest monitoring
- Operational constraints and best practices

**Key Questions:**
- What are current sensor capabilities and limitations?
- How do UAV datasets differ from satellite datasets?
- What are practical deployment considerations?

### Cluster 5: Forest Species Classification Applications
**Focus:** Applied studies on tree species mapping
- Tropical/subtropical forest studies
- Species discrimination challenges
- Ground truth collection methodologies
- Regional forest monitoring systems

**Key Questions:**
- What accuracies are achievable for species-level classification?
- Which species/forest types are most challenging?
- How do studies validate results?

### Cluster 6: Decision Support Systems & Operational Frameworks
**Focus:** End-to-end systems for forest monitoring
- GIS integration approaches
- Workflow automation
- User interface design
- Scalability and deployment

**Key Questions:**
- What system architectures are used?
- How are DSS evaluated in practice?
- What are adoption barriers?

---

## C) Paper Collection Plan

### C.1 Search Execution Order

| Phase | Search Focus | Databases | Timeline |
|-------|--------------|-----------|----------|
| **Phase 1** | Core HSI-LiDAR fusion papers | Scopus, IEEE, Web of Science | Week 1 |
| **Phase 2** | Deep learning for HSI classification | arXiv, IEEE, Google Scholar | Week 1-2 |
| **Phase 3** | LiDAR forest structure methods | ISPRS, Scopus | Week 2 |
| **Phase 4** | UAV remote sensing applications | All databases | Week 2-3 |
| **Phase 5** | Forest species classification studies | Scopus, Google Scholar | Week 3 |
| **Phase 6** | DSS and operational systems | Grey literature, ISRO | Week 3-4 |

### C.2 Target Papers Per Cluster

| Cluster | Target Count | Priority Papers | Secondary Papers |
|---------|--------------|-----------------|------------------|
| **Cluster 1:** HSI Classification | 15-20 | 8-10 | 7-10 |
| **Cluster 2:** LiDAR Forest | 12-15 | 6-8 | 6-7 |
| **Cluster 3:** Data Fusion | 10-12 | 5-6 | 5-6 |
| **Cluster 4:** UAV Systems | 8-10 | 4-5 | 4-5 |
| **Cluster 5:** Species Classification | 12-15 | 6-8 | 6-7 |
| **Cluster 6:** DSS/Operational | 6-8 | 3-4 | 3-4 |
| **TOTAL** | **63-80** | **32-41** | **31-39** |

### C.3 Snowball Citation Strategy

#### Backward Snowballing (References)
For each priority paper:
1. Extract references list
2. Identify foundational papers (pre-2015 if highly cited)
3. Identify methodological sources
4. Add relevant papers to collection

**Target:** 2-3 additional papers per priority paper via backward snowballing

#### Forward Snowballing (Citations)
For each priority paper:
1. Use Google Scholar "Cited by" feature
2. Identify recent papers building on the work
3. Prioritize papers from 2023-2025
4. Check for newer methods/datasets

**Target:** 1-2 additional papers per priority paper via forward snowballing

### C.4 Initial Seed Papers

#### Must-Find Papers (Known Important Works)

| Paper Type | Expected Papers | Search Priority |
|------------|-----------------|-----------------|
| HybridSN and variants | HSI classification benchmark | Immediate |
| SpectralFormer | Transformer for HSI | Immediate |
| PointNet/PointNet++ forest applications | LiDAR deep learning | Immediate |
| AVIRIS-NG forest studies | ISRO-relevant HSI | High |
| Meghalaya/NE India forest studies | Regional context | High |
| HSI-LiDAR fusion review papers | Synthesis guidance | Immediate |

### C.5 Data Extraction Template

For each collected paper, extract:

```markdown
## Paper Card Template

### Bibliographic Information
- **Citation:** [Author et al., Year]
- **Title:** 
- **Venue:** 
- **DOI/Link:** 

### Content Summary
- **Core Idea:** 
- **Method:** 
- **Key Innovation:** 

### Technical Details
- **Architecture:** 
- **Input Data:** 
- **Output:** 
- **Training Details:** 

### Evaluation
- **Dataset(s):** 
- **Metrics Used:** 
- **Key Results:** 
- **Baselines Compared:** 

### Relevance Assessment
- **Relevance to RQs:** [PRQ/TRQ1/TRQ2/...]
- **Potential as Baseline:** [Yes/No]
- **Gaps/Limitations:** 
- **Follow-up Papers:** 

### Quality Score
- **Total:** [X/18]
```

---

## SLR Protocol Summary

| Component | Status |
|-----------|--------|
| Databases identified | ✅ Complete |
| Search strings defined | ✅ Complete |
| Inclusion/Exclusion criteria | ✅ Complete |
| Quality rubric | ✅ Complete |
| Thematic clusters | ✅ Complete (6 clusters) |
| Paper collection plan | ✅ Complete |
| Snowball strategy | ✅ Complete |

---

## Status

**⏸️ STOP AFTER PROTOCOL + PLAN**

Do not summarize papers yet. Proceed to **Phase 2b: Literature Cards** after executing the search protocol.

---

## Next Step

Execute the search protocol, collect papers, and proceed to **Phase 2b: Literature Cards** to create structured summaries of key papers.
