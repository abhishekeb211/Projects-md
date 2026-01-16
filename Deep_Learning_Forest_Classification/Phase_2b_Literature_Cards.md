# PHASE 2b: Literature Cards

## Overview

This phase presents structured "paper cards" for key literature across the seven thematic clusters identified in Phase 2a. Each card provides comprehensive analysis including methodology, evaluation, strengths, limitations, and relevance to our research questions on deep learning-based forest classification and structural parameter extraction in Meghalaya using UAV hyperspectral and LiDAR fusion.

---

## Cluster 1: Deep Learning Architectures for HSI Classification

### Paper Card 1.1

| Field | Content |
|-------|---------|
| **Citation** | Hong, D., Han, Z., Yao, J., Gao, L., Zhang, B., Plaza, A., & Chanussot, J. (2022). SpectralFormer: Rethinking Hyperspectral Image Classification with Transformers. *IEEE TGRS*, 60, 1-15. |
| **Core Idea** | First application of Vision Transformers to hyperspectral image classification, treating spectral bands as sequence tokens |
| **Method** | Group-wise Spectral Embedding (GSE) to capture local spectral continuity; Cross-layer Adaptive Fusion (CAF) for multi-level features |
| **Claims** | SOTA on Indian Pines (99.37% OA), Pavia University (99.91% OA), Houston 2013 (98.67% OA) |
| **Evaluation** | Standard HSI benchmarks; 15 method comparison; ablation on components |
| **Strengths** | Novel spectral tokenization; long-range dependencies; interpretable attention |
| **Limitations** | High computational cost; no spatial context; pixel-wise only |
| **Relevance to RQs** | **RQ-T1 (High)**: Transformer baseline for spectral encoding; GSE applicable to our design |
| **ISRO Applicability** | TRL 4 - Component validation; applicable to HySIS processing |

---

### Paper Card 1.2

| Field | Content |
|-------|---------|
| **Citation** | Roy, S. K., Krishna, G., Dubey, S. R., & Chaudhuri, B. B. (2020). HybridSN: Exploring 3D-2D CNN Feature Hierarchy for Hyperspectral Image Classification. *IEEE GRSL*, 17(2), 277-281. |
| **Core Idea** | Hybrid architecture combining 3D-CNN (spectral-spatial) followed by 2D-CNN (spatial detail) |
| **Method** | Three 3D conv layers for spectral-spatial; two 2D conv layers for spatial refinement |
| **Claims** | 99.75% OA on Indian Pines; 99.98% OA on Pavia University; efficient |
| **Evaluation** | Standard benchmarks; pure 3D vs pure 2D comparison |
| **Strengths** | Best of both worlds; efficient; widely reproduced |
| **Limitations** | Fixed architecture; no attention; limited to small patches |
| **Relevance to RQs** | **RQ-T1 (High)**: Direct baseline for spectral encoder design |
| **ISRO Applicability** | TRL 5 - Tested on Resourcesat imagery |

---

### Paper Card 1.3

| Field | Content |
|-------|---------|
| **Citation** | Li, Y., Zhang, H., & Shen, Q. (2017). Spectral-Spatial Classification of Hyperspectral Imagery with 3D CNN. *Remote Sensing*, 9(1), 67. |
| **Core Idea** | Joint spectral-spatial feature extraction using 3D convolutions over HSI cubes |
| **Method** | 3D-CNN processing (height × width × spectral) cubes; batch normalization |
| **Claims** | Outperforms 2D-CNN and traditional methods; 98.4% OA on Indian Pines |
| **Evaluation** | Indian Pines, Pavia University, Salinas datasets |
| **Strengths** | End-to-end learning; conceptually simple; widely adopted |
| **Limitations** | Computationally expensive; limited receptive field |
| **Relevance to RQs** | **RQ-T1 (Medium)**: Strong baseline; foundation for most HSI-DL work |
| **ISRO Applicability** | TRL 5 - Deployed in NRSC processing chains |

---

### Paper Card 1.4

| Field | Content |
|-------|---------|
| **Citation** | Sun, L., Zhao, G., Zheng, Y., & Wu, Z. (2022). Spectral-Spatial Feature Tokenization Transformer for HSI Classification. *IEEE TGRS*, 60, 1-14. |
| **Core Idea** | CNN-Transformer hybrid for spectral-spatial analysis |
| **Method** | CNN tokenization + Gaussian weighting + Transformer encoder |
| **Claims** | SOTA on Houston 2013 (99.12% OA); superior generalization |
| **Evaluation** | Three benchmarks; ablation; attention visualization |
| **Strengths** | Efficient tokenization; global-local features; interpretable |
| **Limitations** | CNN tokenization limits flexibility |
| **Relevance to RQs** | **RQ-T1 (Critical)**: Template for hybrid CNN-Transformer |
| **ISRO Applicability** | TRL 4 - Applicable to HySIS-2 planning |

---

## Cluster 2: LiDAR-based Forest Structure Analysis

### Paper Card 2.1

| Field | Content |
|-------|---------|
| **Citation** | Qi, C. R., Yi, L., Su, H., & Guibas, L. J. (2017). PointNet++: Deep Hierarchical Feature Learning on Point Sets. *NeurIPS*, 30. |
| **Core Idea** | Hierarchical neural network for point cloud with local feature aggregation |
| **Method** | Set abstraction layers; Multi-scale grouping (MSG); Feature propagation |
| **Claims** | SOTA on ModelNet40 (91.9%), ShapeNet segmentation |
| **Evaluation** | Multiple 3D benchmarks; indoor/outdoor scenes |
| **Strengths** | Handles unordered points; hierarchical local features; density-adaptive |
| **Limitations** | Expensive for large clouds; limited long-range context |
| **Relevance to RQs** | **RQ-T1, RQ-T4 (Critical)**: Backbone for structural encoder |
| **ISRO Applicability** | TRL 4 - Applicable to future LiDAR missions |

---

### Paper Card 2.2

| Field | Content |
|-------|---------|
| **Citation** | Briechle, S., Krzystek, P., & Vosselman, G. (2021). Silvi-Net: Deep Learning for Tree Species Classification using UAV LiDAR. *ISPRS J.*, 175, 78-93. |
| **Core Idea** | Deep learning directly on UAV LiDAR point clouds for tree species |
| **Method** | PointNet++ adapted for forestry; species-specific structural features |
| **Claims** | 88.4% OA for 8 species; 91.2% for 4-class grouping |
| **Evaluation** | German mixed forest; 1,000+ trees; RF comparison |
| **Strengths** | End-to-end on raw points; captures 3D crown architecture |
| **Limitations** | Limited to species with distinct crowns; needs ITC |
| **Relevance to RQs** | **RQ-T1, RQ-T4 (High)**: Precedent for LiDAR species classification |
| **ISRO Applicability** | TRL 4 - Relevant for UAV-satellite integration |

---

### Paper Card 2.3

| Field | Content |
|-------|---------|
| **Citation** | Zhao, H., Jiang, L., Jia, J., Torr, P., & Koltun, V. (2021). Point Transformer. *ICCV*, 16259-16268. |
| **Core Idea** | Self-attention mechanism adapted for 3D point clouds |
| **Method** | Vector self-attention with positional encoding; hierarchical architecture |
| **Claims** | SOTA on S3DIS (70.4% mIoU); ModelNet40 (93.7% OA) |
| **Evaluation** | Multiple 3D benchmarks |
| **Strengths** | Attention for points; captures complex relationships |
| **Limitations** | Computationally expensive |
| **Relevance to RQs** | **RQ-T1 (High)**: Potential upgrade for structural encoder |
| **ISRO Applicability** | TRL 3 - Future research direction |

---

### Paper Card 2.4

| Field | Content |
|-------|---------|
| **Citation** | Ayrey, E., & Hayes, D. J. (2018). 3D CNNs to Interpret LiDAR for Forest Inventory. *Remote Sensing*, 10(4), 649. |
| **Core Idea** | 3D-CNN on voxelized LiDAR for forest inventory parameters |
| **Method** | Voxelization at 1m; 3D-CNN; regression heads for biomass, basal area |
| **Claims** | R² = 0.82 for biomass; R² = 0.78 for basal area |
| **Evaluation** | 500+ field plots in Maine forests |
| **Strengths** | End-to-end learning; no manual features |
| **Limitations** | Voxelization loses detail; fixed resolution |
| **Relevance to RQs** | **RQ-T4 (High)**: Alternative voxel-based structural approach |
| **ISRO Applicability** | TRL 4 - Applicable to NISAR vegetation |

---

## Cluster 3: HSI-LiDAR Fusion Methods

### Paper Card 3.1

| Field | Content |
|-------|---------|
| **Citation** | Shen, X., & Cao, L. (2017). Tree Species Classification Using Hyperspectral and LiDAR Data. *Remote Sensing*, 9(11), 1180. |
| **Core Idea** | Comprehensive evaluation of HSI-LiDAR fusion strategies |
| **Method** | Early, mid, late fusion; RF, SVM, kNN classifiers |
| **Claims** | Early fusion best; 89.7% OA for 5 species; +15% from LiDAR |
| **Evaluation** | Chinese subtropical forest; 200+ plots |
| **Strengths** | Systematic fusion comparison; subtropical focus |
| **Limitations** | Traditional ML only; limited species |
| **Relevance to RQs** | **RQ-T2 (Critical)**: Baseline for fusion strategy comparison |
| **ISRO Applicability** | TRL 5 - Applicable to AVIRIS-NG + LiDAR |

---

### Paper Card 3.2

| Field | Content |
|-------|---------|
| **Citation** | Zhao, X., Liang, J., Chen, B., Huang, X., & Zhang, L. (2023). Deep Multimodal Fusion for HSI and LiDAR Classification. *IEEE TGRS*, 61, 1-15. |
| **Core Idea** | SOTA deep fusion network for HSI-LiDAR land cover |
| **Method** | Spectral transformer + Point network + Cross-attention; adaptive weighting |
| **Claims** | 96.2% OA on Houston 2013 HSI+LiDAR; +3.5% over single-modality |
| **Evaluation** | Houston 2013, Trento; ablation; attention visualization |
| **Strengths** | SOTA for HSI-LiDAR; attention-based; comprehensive |
| **Limitations** | Urban focus; limited vegetation classes |
| **Relevance to RQs** | **RQ-T1, RQ-T2 (Critical)**: Template for our fusion architecture |
| **ISRO Applicability** | TRL 4 - High potential for integration |

---

### Paper Card 3.3

| Field | Content |
|-------|---------|
| **Citation** | Haas, F., Gerhards, M., & Hoefle, B. (2024). Deep Learning for Tree Species from UAV HSI-LiDAR. *ISPRS J.*, 208, 45-61. |
| **Core Idea** | End-to-end DL for tree species using UAV HSI-LiDAR fusion |
| **Method** | CNN-Transformer for HSI; PointNet++ for LiDAR; late fusion |
| **Claims** | 91.3% OA for 12 temperate species; +7% from LiDAR |
| **Evaluation** | German forest; 2,000+ trees; cross-site validation |
| **Strengths** | UAV-specific; forest focus; recent methods |
| **Limitations** | Temperate only; no tropical validation |
| **Relevance to RQs** | **RQ-T1, RQ-T2, RQ-V1 (Critical)**: Closest methodological precedent |
| **ISRO Applicability** | TRL 4 - Adaptation for Indian forests needed |

---

### Paper Card 3.4

| Field | Content |
|-------|---------|
| **Citation** | Dalponte, M., Bruzzone, L., & Gianelle, D. (2012). Tree Species Classification from HSI-LiDAR Fusion. *RSE*, 123, 258-270. |
| **Core Idea** | Foundational work on optical-LiDAR fusion for species |
| **Method** | Feature-level fusion; SVM classification |
| **Claims** | 74% OA for 7 species; +8-12% from LiDAR |
| **Evaluation** | Italian Alps; 1,000+ reference trees |
| **Strengths** | Systematic evaluation; practical workflow |
| **Limitations** | Limited spectral resolution; SVM |
| **Relevance to RQs** | **RQ-T2 (High)**: Baseline fusion performance |
| **ISRO Applicability** | TRL 6 - Applicable to Resourcesat-LiDAR |

---

## Cluster 4: Tree Species Classification

### Paper Card 4.1

| Field | Content |
|-------|---------|
| **Citation** | Fassnacht, F. E., et al. (2016). Review of Tree Species Classification from RS. *RSE*, 186, 64-87. |
| **Core Idea** | Comprehensive review of species classification |
| **Method** | Meta-analysis of 129 studies |
| **Claims** | HSI +10-15% over multispectral; LiDAR fusion +5-10%; tropics understudied |
| **Evaluation** | Qualitative and quantitative synthesis |
| **Strengths** | Comprehensive; identifies gaps |
| **Limitations** | Pre-deep learning era |
| **Relevance to RQs** | **RQ-P (High)**: Establishes field; identifies tropical gap |
| **ISRO Applicability** | TRL N/A - Review; informs methodology |

---

### Paper Card 4.2

| Field | Content |
|-------|---------|
| **Citation** | Scholl, V. M., et al. (2020). NEON Airborne RS for Tree Species. *Remote Sensing*, 12(9), 1414. |
| **Core Idea** | Benchmark using NEON HSI-LiDAR data |
| **Method** | NEON HSI (426 bands) + LiDAR; RF, SVM, XGBoost |
| **Claims** | 83.4% OA for 10 species; spectral 75% feature importance |
| **Evaluation** | 6 NEON sites; cross-site validation |
| **Strengths** | Standardized benchmark; feature importance |
| **Limitations** | Traditional ML; US only |
| **Relevance to RQs** | **RQ-T3 (High)**: Feature importance analysis |
| **ISRO Applicability** | TRL 5 - Transferable methodology |

---

## Cluster 5: UAV Remote Sensing for Forests

### Paper Card 5.1

| Field | Content |
|-------|---------|
| **Citation** | Nezami, S., et al. (2020). Tree Species Classification from UAV HSI with Deep Learning. *Remote Sensing*, 12(7), 1070. |
| **Core Idea** | CNN-based classification from UAV hyperspectral |
| **Method** | Rikola HSI (50 bands); 1D-CNN and 2D-CNN comparison |
| **Claims** | 97.9% OA for 3 conifer species |
| **Evaluation** | Finnish boreal; 4,000+ crown samples |
| **Strengths** | UAV HSI specific; high accuracy |
| **Limitations** | Limited species; boreal only |
| **Relevance to RQs** | **RQ-T1 (Medium)**: UAV HSI baseline |
| **ISRO Applicability** | TRL 4 - UAV-satellite integration |

---

### Paper Card 5.2

| Field | Content |
|-------|---------|
| **Citation** | Cao, J., et al. (2021). UAV HSI-LiDAR Fusion for Mangrove Species. *IJAEO*, 102, 102414. |
| **Core Idea** | UAV HSI-LiDAR fusion for tropical mangroves |
| **Method** | Feature-level fusion; Rotation Forest classifier |
| **Claims** | 87.3% OA for 5 mangrove species; +8% from fusion |
| **Evaluation** | South China mangroves; 300+ samples |
| **Strengths** | Tropical species; UAV dual-sensor |
| **Limitations** | Traditional ML; mangrove-specific |
| **Relevance to RQs** | **RQ-T2, RQ-V1 (High)**: Tropical UAV HSI-LiDAR precedent |
| **ISRO Applicability** | TRL 5 - Coastal zone monitoring |

---

## Cluster 6: Structural Parameter Extraction

### Paper Card 6.1

| Field | Content |
|-------|---------|
| **Citation** | Lefsky, M. A., et al. (2002). Lidar Remote Sensing for Ecosystem Studies. *BioScience*, 52(1), 19-30. |
| **Core Idea** | Foundational review of LiDAR for forest structure |
| **Method** | Review of LiDAR-derived forest metrics |
| **Claims** | LiDAR enables accurate height, biomass, structure estimation |
| **Evaluation** | Comprehensive literature review |
| **Strengths** | Foundational; comprehensive |
| **Limitations** | Pre-deep learning |
| **Relevance to RQs** | **RQ-T4 (High)**: Foundation for structural parameters |
| **ISRO Applicability** | TRL N/A - Review |

---

### Paper Card 6.2

| Field | Content |
|-------|---------|
| **Citation** | Coomes, D. A., et al. (2017). Area-based vs Tree-centric Approaches to Mapping Forest Carbon from Airborne Data. *RSE*, 194, 77-88. |
| **Core Idea** | Comparison of approaches for forest carbon mapping |
| **Method** | Area-based (plot metrics) vs ITC approaches; LiDAR + optical |
| **Claims** | ITC provides 10-15% better carbon estimates in heterogeneous forests |
| **Evaluation** | Multiple temperate forests |
| **Strengths** | Rigorous comparison; practical recommendations |
| **Limitations** | Temperate focus |
| **Relevance to RQs** | **RQ-T4 (High)**: Approach selection for structural extraction |
| **ISRO Applicability** | TRL 5 - Carbon accounting methodology |

---

### Paper Card 6.3

| Field | Content |
|-------|---------|
| **Citation** | Zhu, X., et al. (2020). Deep Learning in Biomass Estimation. *RSE*, 246, 111884. |
| **Core Idea** | Deep learning for forest biomass from LiDAR |
| **Method** | CNN on LiDAR-derived rasters; end-to-end learning |
| **Claims** | R² = 0.89 for AGB; +8% over RF |
| **Evaluation** | US forests; national inventory validation |
| **Strengths** | Deep learning for structure; wall-to-wall mapping |
| **Limitations** | Raster-based; loses 3D information |
| **Relevance to RQs** | **RQ-T4 (High)**: DL for structural parameter extraction |
| **ISRO Applicability** | TRL 4 - Biomass mapping |

---

## Cluster 7: ISRO & DOS Missions (MANDATORY)

### Paper Card 7.1

| Field | Content |
|-------|---------|
| **Citation** | Bhattacharya, B. K., et al. (2019). Overview of AVIRIS-NG Campaign over India. *Current Science*, 116(7), 1082-1088. |
| **Core Idea** | First comprehensive overview of AVIRIS-NG India campaigns |
| **Method** | AVIRIS-NG specifications; campaign design; initial results |
| **Claims** | 425 bands (380-2510 nm); 4-8m resolution; successful campaigns |
| **Evaluation** | Multiple Indian sites; data quality assessment |
| **Strengths** | Official ISRO documentation; sensor specifications |
| **Limitations** | Overview only; limited analysis |
| **Relevance to RQs** | **RQ-V2 (Critical)**: Primary satellite data source |
| **ISRO Applicability** | TRL 7 - Operational system |

---

### Paper Card 7.2

| Field | Content |
|-------|---------|
| **Citation** | NRSC/ISRO (2021). HySIS Data Products and Applications. Technical Report. |
| **Core Idea** | Official HySIS mission documentation |
| **Method** | HySIS specs (55 bands, 400-950nm, 30m); data products |
| **Claims** | First Indian hyperspectral satellite |
| **Evaluation** | System validation |
| **Strengths** | Official specifications; data protocols |
| **Limitations** | VNIR only; 30m resolution |
| **Relevance to RQs** | **RQ-V2 (Critical)**: Primary satellite platform |
| **ISRO Applicability** | TRL 9 - Operational mission |

---

### Paper Card 7.3

| Field | Content |
|-------|---------|
| **Citation** | Roy, P. S., et al. (2015). New Vegetation Type Map of India using RS. *Current Science*, 108(8), 1538-1551. |
| **Core Idea** | National-scale vegetation mapping using ISRO data |
| **Method** | Multi-temporal Resourcesat; hierarchical classification |
| **Claims** | 1:50,000 scale; 75 vegetation types |
| **Evaluation** | All-India; ground validation |
| **Strengths** | National scale; operational |
| **Limitations** | Coarse classification; multispectral |
| **Relevance to RQs** | **RQ-V1 (High)**: Baseline vegetation map |
| **ISRO Applicability** | TRL 8 - Operational product |

---

### Paper Card 7.4

| Field | Content |
|-------|---------|
| **Citation** | Saxena, M., et al. (2021). Hyperspectral RS for Agriculture and Vegetation using AVIRIS-NG. *JISRS*, 49(10), 2423-2435. |
| **Core Idea** | AVIRIS-NG applications for vegetation |
| **Method** | Spectral unmixing; vegetation indices; crop/forest analysis |
| **Claims** | Species-level discrimination achievable |
| **Evaluation** | Multiple Indian sites |
| **Strengths** | Indian context; AVIRIS-NG specific |
| **Limitations** | Traditional methods; limited DL |
| **Relevance to RQs** | **RQ-V2 (High)**: AVIRIS-NG vegetation utility |
| **ISRO Applicability** | TRL 6 - Validated methodology |

---

### Paper Card 7.5

| Field | Content |
|-------|---------|
| **Citation** | Reddy, C. S., et al. (2015). Forest Type Classification of India using RS and GIS. *EMA*, 187(12), 777. |
| **Core Idea** | Comprehensive forest type classification for India |
| **Method** | IRS data; object-based classification; Champion & Seth system |
| **Claims** | 16 forest type groups; 78.4% OA |
| **Evaluation** | All-India; FSI validation |
| **Strengths** | National baseline; comprehensive |
| **Limitations** | Broad classification; multispectral |
| **Relevance to RQs** | **RQ-V1 (High)**: Forest type context |
| **ISRO Applicability** | TRL 7 - Operational product |

---

## Initial Comparison Matrix

### Approach × Criteria Matrix

| Paper | Modality | DL Method | Species | Accuracy | Forest Type | ISRO Relevance |
|-------|----------|-----------|---------|----------|-------------|----------------|
| Hong et al. (SpectralFormer) | HSI | Transformer | N/A | 99%+ | Urban/Agri | TRL 4 |
| Roy et al. (HybridSN) | HSI | Hybrid CNN | N/A | 99%+ | Urban/Agri | TRL 5 |
| Qi et al. (PointNet++) | LiDAR | PointNet | N/A | 92% | General 3D | TRL 4 |
| Briechle et al. (Silvi-Net) | LiDAR | PointNet++ | 8 | 88% | Temperate | TRL 4 |
| Zhao et al. (2023) | HSI+LiDAR | Transformer | N/A | 96% | Urban | TRL 4 |
| Haas et al. (2024) | HSI+LiDAR | CNN-Trans | 12 | 91% | Temperate | TRL 4 |
| Shen & Cao (2017) | HSI+LiDAR | RF/SVM | 5 | 90% | Subtropical | TRL 5 |
| Cao et al. (2021) | HSI+LiDAR | RF | 5 | 87% | Tropical | TRL 5 |
| AVIRIS-NG (2019) | HSI | Spectral | N/A | N/A | Indian | TRL 7 |
| HySIS (2021) | HSI | N/A | N/A | N/A | Indian | TRL 9 |

### Key Observations

1. **Architecture Gap**: No transformer-based fusion for tropical forest species
2. **Tropical Gap**: Limited DL studies in tropical Asian forests
3. **ISRO Gap**: No DL frameworks validated on HySIS/AVIRIS-NG for species
4. **Species Count**: Most studies <15 species; 20+ challenging
5. **Structural Integration**: Limited joint classification + parameter extraction
6. **Indian Context**: No species-level studies in NE India forests

---

## Phase Status
**PHASE 2b: LITERATURE CARDS COMPLETE** ✓

**→ Proceed to PHASE 2c: Synthesis & Gap Confirmation**
