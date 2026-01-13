# Phase 2b: Literature Cards (Key Papers)

## Research Agent Prompt

Continue PHASE 2.

For each cluster, produce structured "paper cards" for the most important works. End with an initial comparison matrix draft.

---

## Instructions for Paper Card Generation

For each of the 6 thematic clusters, produce structured paper cards for the most important works (at least 5-10 total to start per cluster).

### Paper Card Structure

```markdown
---
## [Short Reference ID]: [Author et al., Year]

### Citation
**Full Citation:** [Authors. "Title." Venue, Year. DOI]

### Core Idea + Method
[2-3 sentences describing the main contribution and approach]

### What It Proves/Claims
- Claim 1: [Specific claim with evidence]
- Claim 2: [Specific claim with evidence]
- Key Result: [Quantitative result]

### Evaluation Setup
- **Dataset:** [Name, size, characteristics]
- **Metrics:** [OA, Kappa, F1, etc.]
- **Baselines:** [What was compared]
- **Validation:** [Train/test split, cross-validation, etc.]

### Strengths
1. [Strength 1]
2. [Strength 2]
3. [Strength 3]

### Limitations/Open Gaps
1. [Limitation 1]
2. [Limitation 2]
3. [Gap that our work could address]

### Direct Relevance to Our RQs
- **PRQ:** [Relevance level: High/Medium/Low + explanation]
- **TRQ1:** [Relevance]
- **TRQ2:** [Relevance]
- **TRQ3:** [Relevance]
- **TRQ4:** [Relevance]

### Follow-Chain
- **Key Papers They Cite:** [2-3 important references]
- **Key Papers Citing Them:** [2-3 important follow-up works]
- **Snowball Priority:** [High/Medium/Low]

### Quality Score: [X/18]
---
```

---

## Cluster 1: Hyperspectral Image Classification Methods

### Target: 8-10 Priority Papers

#### Expected Key Papers to Find and Analyze

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| HSI-01 | HybridSN / 3D-CNN for HSI | Critical |
| HSI-02 | SpectralFormer / Transformer-based HSI | Critical |
| HSI-03 | Attention-based spectral-spatial networks | High |
| HSI-04 | Semi-supervised HSI classification | High |
| HSI-05 | Self-supervised pretraining for HSI | Medium |
| HSI-06 | Multi-scale CNN for HSI | High |
| HSI-07 | Graph neural networks for HSI | Medium |
| HSI-08 | Band selection with deep learning | Medium |
| HSI-09 | HSI classification benchmark comparison | High |
| HSI-10 | Lightweight/efficient HSI networks | Medium |

### Paper Card Template - Cluster 1

```markdown
---
## HSI-01: [To be filled after search]

### Citation
**Full Citation:** [To be completed]

### Core Idea + Method
[Describe the 3D-CNN or hybrid approach for spectral-spatial feature extraction]

### What It Proves/Claims
- Achieves [X]% OA on [Dataset]
- Demonstrates superiority of 3D convolutions over 2D for HSI
- [Other key claims]

### Evaluation Setup
- **Dataset:** Indian Pines, Pavia University, Salinas, [Forest datasets]
- **Metrics:** OA, AA, Kappa
- **Baselines:** SVM, 2D-CNN, traditional methods
- **Validation:** Random split or disjoint train/test

### Strengths
1. Joint spectral-spatial feature learning
2. Strong benchmark performance
3. [Other strengths]

### Limitations/Open Gaps
1. Requires large labeled datasets
2. Limited fusion with structural data
3. [Gaps relevant to our work]

### Direct Relevance to Our RQs
- **PRQ:** High - Core architecture for hyperspectral processing
- **TRQ1:** High - Spectral-spatial feature representations
- **TRQ2:** Medium - No LiDAR integration
- **TRQ3:** Low - Single modality
- **TRQ4:** Medium - Scalability considerations

### Follow-Chain
- **Key Papers They Cite:** [Foundational CNN works]
- **Key Papers Citing Them:** [Recent improvements]
- **Snowball Priority:** High

### Quality Score: [To be assessed]/18
---
```

---

## Cluster 2: LiDAR-Based Forest Structure Analysis

### Target: 6-8 Priority Papers

#### Expected Key Papers to Find and Analyze

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| LID-01 | PointNet++ for forest point clouds | Critical |
| LID-02 | Individual tree segmentation with DL | Critical |
| LID-03 | Canopy height model from LiDAR | High |
| LID-04 | Forest inventory automation | High |
| LID-05 | Crown delineation algorithms | Medium |
| LID-06 | 3D semantic segmentation in forests | High |
| LID-07 | LiDAR + optical fusion for forestry | Medium |
| LID-08 | UAV LiDAR vs. airborne LiDAR comparison | Medium |

### Paper Card Template - Cluster 2

```markdown
---
## LID-01: [To be filled after search]

### Citation
**Full Citation:** [To be completed]

### Core Idea + Method
[Describe point cloud processing approach for forest structure]

### What It Proves/Claims
- Achieves [X]% accuracy for tree detection
- RMSE of [Y]m for height estimation
- [Other key claims]

### Evaluation Setup
- **Dataset:** [Forest LiDAR dataset]
- **Metrics:** Detection accuracy, RMSE, segmentation IoU
- **Baselines:** Traditional algorithms, random forest
- **Validation:** [Method]

### Strengths
1. Direct 3D processing without rasterization
2. Handles varying point density
3. [Other strengths]

### Limitations/Open Gaps
1. Limited spectral information
2. Computational requirements
3. [Gaps relevant to our work]

### Direct Relevance to Our RQs
- **PRQ:** High - Structural parameter extraction
- **TRQ1:** Low - No spectral features
- **TRQ2:** Critical - LiDAR integration component
- **TRQ3:** Medium - Fusion potential
- **TRQ4:** Medium - Scalability

### Follow-Chain
- **Key Papers They Cite:** [PointNet original, forest LiDAR classics]
- **Key Papers Citing Them:** [Recent applications]
- **Snowball Priority:** High

### Quality Score: [To be assessed]/18
---
```

---

## Cluster 3: Multi-Sensor Data Fusion Strategies

### Target: 5-6 Priority Papers

#### Expected Key Papers to Find and Analyze

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| FUS-01 | HSI-LiDAR fusion for land cover | Critical |
| FUS-02 | Multi-modal deep learning fusion | Critical |
| FUS-03 | Early vs. late fusion comparison | High |
| FUS-04 | Cross-modal attention mechanisms | High |
| FUS-05 | Feature-level fusion architectures | Medium |
| FUS-06 | Decision fusion strategies | Medium |

### Paper Card Template - Cluster 3

```markdown
---
## FUS-01: [To be filled after search]

### Citation
**Full Citation:** [To be completed]

### Core Idea + Method
[Describe the fusion strategy for HSI and LiDAR data]

### What It Proves/Claims
- Fusion improves classification by [X]% over single sensor
- [Specific fusion strategy] outperforms alternatives
- [Other key claims]

### Evaluation Setup
- **Dataset:** [Multi-sensor dataset]
- **Metrics:** OA, improvement margin, computational cost
- **Baselines:** Single-sensor methods, alternative fusion
- **Validation:** [Method]

### Strengths
1. Leverages complementary information
2. Systematic fusion comparison
3. [Other strengths]

### Limitations/Open Gaps
1. Dataset-specific findings
2. Limited forest applications
3. [Gaps relevant to our work]

### Direct Relevance to Our RQs
- **PRQ:** Critical - Core fusion methodology
- **TRQ1:** Medium - Spectral feature handling
- **TRQ2:** Critical - Integration approach
- **TRQ3:** Critical - Fusion strategy evaluation
- **TRQ4:** High - Architecture scalability

### Follow-Chain
- **Key Papers They Cite:** [Fusion theory, modality-specific methods]
- **Key Papers Citing Them:** [Recent fusion advances]
- **Snowball Priority:** Critical

### Quality Score: [To be assessed]/18
---
```

---

## Cluster 4: UAV-Based Remote Sensing Systems

### Target: 4-5 Priority Papers

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| UAV-01 | UAV hyperspectral for vegetation | High |
| UAV-02 | UAV LiDAR forest applications | High |
| UAV-03 | UAV data processing pipelines | Medium |
| UAV-04 | Flight planning for forest monitoring | Medium |
| UAV-05 | UAV sensor calibration protocols | Medium |

---

## Cluster 5: Forest Species Classification Applications

### Target: 6-8 Priority Papers

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| SPE-01 | Tropical forest species mapping | Critical |
| SPE-02 | Tree species classification with HSI | Critical |
| SPE-03 | Indian forest remote sensing studies | High |
| SPE-04 | Meghalaya/NE India vegetation studies | High |
| SPE-05 | Species discrimination challenges | Medium |
| SPE-06 | Ground truth collection methods | Medium |
| SPE-07 | ISRO forest monitoring initiatives | High |
| SPE-08 | Biodiversity hotspot mapping | Medium |

---

## Cluster 6: Decision Support Systems & Operational Frameworks

### Target: 3-4 Priority Papers

| Paper ID | Expected Topic | Priority |
|----------|----------------|----------|
| DSS-01 | Forest monitoring DSS architecture | High |
| DSS-02 | GIS integration for remote sensing | Medium |
| DSS-03 | Operational remote sensing systems | High |
| DSS-04 | User requirements for forest DSS | Medium |

---

## Initial Comparison Matrix Draft (Approach × Criteria)

### Matrix Template

| Paper ID | Modality | Architecture | Fusion Type | Forest App | Species Level | Accuracy | Dataset Size | Code Avail |
|----------|----------|--------------|-------------|------------|---------------|----------|--------------|------------|
| HSI-01 | HSI | 3D-CNN | N/A | ☐ | ☐ | [OA%] | [#samples] | [Y/N] |
| HSI-02 | HSI | Transformer | N/A | ☐ | ☐ | [OA%] | [#samples] | [Y/N] |
| LID-01 | LiDAR | PointNet++ | N/A | ☑ | ☐ | [Acc%] | [#points] | [Y/N] |
| FUS-01 | HSI+LiDAR | [Type] | [E/M/L] | ☑ | ☐ | [OA%] | [#samples] | [Y/N] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Criteria Definitions

| Criterion | Description | Values |
|-----------|-------------|--------|
| **Modality** | Input data type | HSI, LiDAR, HSI+LiDAR, Multi |
| **Architecture** | Model type | CNN, 3D-CNN, Transformer, PointNet, Hybrid |
| **Fusion Type** | If multi-modal | Early (E), Mid (M), Late (L), N/A |
| **Forest App** | Applied to forestry | Yes (☑) / No (☐) |
| **Species Level** | Species-level classification | Yes (☑) / No (☐) |
| **Accuracy** | Best reported OA/Accuracy | Percentage |
| **Dataset Size** | Training data volume | Number |
| **Code Avail** | Reproducibility | Yes (Y) / No (N) / Partial (P) |

---

## Comparison Matrix - Detailed View

### Architecture Comparison

| Paper | Input Processing | Feature Extraction | Classification Head | Complexity |
|-------|------------------|-------------------|---------------------|------------|
| [HSI-01] | [Patch extraction] | [3D Conv layers] | [FC layers] | [Params] |
| [LID-01] | [Point sampling] | [Set abstraction] | [MLP] | [Params] |
| [FUS-01] | [Multi-branch] | [Separate encoders] | [Fusion + FC] | [Params] |

### Performance Comparison (To be filled)

| Paper | Dataset | OA (%) | AA (%) | Kappa | Notes |
|-------|---------|--------|--------|-------|-------|
| [HSI-01] | Indian Pines | -- | -- | -- | |
| [HSI-01] | Pavia U | -- | -- | -- | |
| [LID-01] | [Forest] | -- | -- | -- | Tree detection |
| [FUS-01] | [Multi] | -- | -- | -- | Fusion gain |

---

## Literature Card Collection Tracker

| Cluster | Target | Collected | Cards Complete | Status |
|---------|--------|-----------|----------------|--------|
| 1. HSI Classification | 8-10 | 0 | 0 | 🔴 Pending |
| 2. LiDAR Forest | 6-8 | 0 | 0 | 🔴 Pending |
| 3. Data Fusion | 5-6 | 0 | 0 | 🔴 Pending |
| 4. UAV Systems | 4-5 | 0 | 0 | 🔴 Pending |
| 5. Species Classification | 6-8 | 0 | 0 | 🔴 Pending |
| 6. DSS/Operational | 3-4 | 0 | 0 | 🔴 Pending |
| **TOTAL** | **32-41** | **0** | **0** | **🔴 Pending** |

---

## Status

**⏸️ DO NOT START PHASE 3**

Complete all literature cards and comparison matrix before proceeding.

---

## Next Step

After completing literature cards, proceed to **Phase 2c: Critical Synthesis & Gap Confirmation** to synthesize findings and confirm research gaps.
