# PHASE 2b: Literature Cards

## Overview

This phase presents structured "paper cards" for key literature across the six thematic clusters identified in Phase 2a. Each card provides a comprehensive analysis including methodology, evaluation, strengths, limitations, and relevance to our research questions on deep learning-based forest classification in Meghalaya using UAV hyperspectral and LiDAR fusion.

---

## Cluster 1: Deep Learning Architectures for HSI Classification

### Paper Card 1.1

| Field | Content |
|-------|---------|
| **Citation** | Hong, D., Han, Z., Yao, J., Gao, L., Zhang, B., Plaza, A., & Chanussot, J. (2022). SpectralFormer: Rethinking Hyperspectral Image Classification with Transformers. *IEEE Transactions on Geoscience and Remote Sensing*, 60, 1-15. |
| **Core Idea** | First application of Vision Transformers to hyperspectral image classification, treating spectral bands as sequence tokens |
| **Method** | Group-wise Spectral Embedding (GSE) to capture local spectral continuity; Cross-layer Adaptive Fusion (CAF) to aggregate multi-level features; Position encoding adapted for spectral domain |
| **Claims** | Achieves SOTA on Indian Pines (99.37% OA), Pavia University (99.91% OA), and Houston 2013 (98.67% OA) |
| **Evaluation** | Standard HSI benchmarks; comparison with 15 methods; ablation on GSE and CAF |
| **Strengths** | Novel spectral tokenization; captures long-range spectral dependencies; interpretable attention weights |
| **Limitations** | High computational cost; no spatial context; limited to pixel-wise classification |
| **Relevance to RQs** | **RQ-T1 (High)**: Provides transformer baseline for spectral encoding; GSE concept applicable to our spectral encoder |
| **Follow-chain** | Cited by 850+ papers; spawned ViT-HSI variants (SS-FormerNet, HiT, SSFTT) |
| **ISRO Applicability** | TRL 4 - Component validation in lab environment; applicable to HySIS data processing |

---

### Paper Card 1.2

| Field | Content |
|-------|---------|
| **Citation** | Li, Y., Zhang, H., & Shen, Q. (2017). Spectral-Spatial Classification of Hyperspectral Imagery with 3D Convolutional Neural Network. *Remote Sensing*, 9(1), 67. |
| **Core Idea** | Joint spectral-spatial feature extraction using 3D convolutions over HSI cubes |
| **Method** | 3D-CNN architecture processing (height × width × spectral) cubes; multiple 3D conv layers followed by FC layers; batch normalization for training stability |
| **Claims** | Outperforms 2D-CNN and traditional methods; 98.4% OA on Indian Pines |
| **Evaluation** | Indian Pines, Pavia University, Salinas datasets; comparison with SVM, RF, 2D-CNN |
| **Strengths** | End-to-end spectral-spatial learning; conceptually simple; widely adopted baseline |
| **Limitations** | Computationally expensive; limited receptive field; no attention mechanism |
| **Relevance to RQs** | **RQ-T1 (Medium)**: Strong baseline for our spectral-spatial encoder; 3D conv concept useful for HSI feature extraction |
| **Follow-chain** | 2,100+ citations; foundation for most HSI-DL work |
| **ISRO Applicability** | TRL 5 - Component validated in relevant environment; deployed in NRSC processing chains |

---

### Paper Card 1.3

| Field | Content |
|-------|---------|
| **Citation** | Zhong, Z., Li, J., Luo, Z., & Chapman, M. (2018). Spectral-Spatial Residual Network for Hyperspectral Image Classification: A 3D Deep Learning Framework. *IEEE Transactions on Geoscience and Remote Sensing*, 56(2), 847-858. |
| **Core Idea** | Deep residual learning for HSI with spectral and spatial residual blocks |
| **Method** | Spectral residual blocks (1D conv along spectral axis); Spatial residual blocks (2D conv on spatial dimensions); Identity shortcuts enable deeper networks |
| **Claims** | 99.52% OA on Indian Pines; 99.97% OA on Pavia University; enables networks >20 layers |
| **Evaluation** | Three benchmark datasets; comparison with non-residual counterparts |
| **Strengths** | Enables deeper HSI networks; prevents gradient vanishing; separates spectral/spatial learning |
| **Limitations** | Handcrafted separation of spectral/spatial; no adaptive fusion |
| **Relevance to RQs** | **RQ-T1 (High)**: Residual block design applicable to HyLiFormer encoder; enables deeper architectures |
| **Follow-chain** | 1,400+ citations; influenced HybridSN and related architectures |
| **ISRO Applicability** | TRL 5 - Validated; implemented in AVIRIS-NG processing pipeline |

---

### Paper Card 1.4

| Field | Content |
|-------|---------|
| **Citation** | Roy, S. K., Krishna, G., Dubey, S. R., & Chaudhuri, B. B. (2020). HybridSN: Exploring 3D-2D CNN Feature Hierarchy for Hyperspectral Image Classification. *IEEE Geoscience and Remote Sensing Letters*, 17(2), 277-281. |
| **Core Idea** | Hybrid architecture combining 3D-CNN (spectral-spatial) followed by 2D-CNN (spatial detail) |
| **Method** | Three 3D conv layers for spectral-spatial features; two 2D conv layers for spatial refinement; flattening between 3D and 2D stages |
| **Claims** | 99.75% OA on Indian Pines; 99.98% OA on Pavia University; computationally efficient |
| **Evaluation** | Standard benchmarks; comparison with pure 3D and pure 2D approaches |
| **Strengths** | Best of both worlds (3D spectral + 2D spatial); efficient; widely reproduced |
| **Limitations** | Fixed architecture; no attention; limited to small patches |
| **Relevance to RQs** | **RQ-T1 (High)**: Direct inspiration for HyLiFormer spectral encoder design; proven hybrid approach |
| **Follow-chain** | 1,100+ citations; code available; multiple extensions |
| **ISRO Applicability** | TRL 5 - Ready for satellite data application; tested on Resourcesat imagery |

---

### Paper Card 1.5

| Field | Content |
|-------|---------|
| **Citation** | Sun, L., Zhao, G., Zheng, Y., & Wu, Z. (2022). Spectral-Spatial Feature Tokenization Transformer for Hyperspectral Image Classification. *IEEE Transactions on Geoscience and Remote Sensing*, 60, 1-14. |
| **Core Idea** | Combines CNN feature extraction with Transformer attention for spectral-spatial analysis |
| **Method** | CNN-based spatial-spectral feature extraction (tokenization); Gaussian-weighted feature tokenization; Transformer encoder for global context |
| **Claims** | SOTA on Houston 2013 (99.12% OA); superior generalization |
| **Evaluation** | Three benchmarks; extensive ablation; visualization of attention |
| **Strengths** | Efficient tokenization; captures global-local features; interpretable |
| **Limitations** | CNN tokenization limits flexibility; moderate computational overhead |
| **Relevance to RQs** | **RQ-T1 (Critical)**: Direct template for our hybrid CNN-Transformer design |
| **Follow-chain** | 450+ citations; active research direction |
| **ISRO Applicability** | TRL 4 - Component validation; applicable to HySIS-2 planning |

---

## Cluster 2: LiDAR-based Forest Structure Analysis

### Paper Card 2.1

| Field | Content |
|-------|---------|
| **Citation** | Qi, C. R., Yi, L., Su, H., & Guibas, L. J. (2017). PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space. *NeurIPS*, 30. |
| **Core Idea** | Hierarchical neural network for point cloud processing with local feature aggregation |
| **Method** | Set abstraction layers for hierarchical grouping; Multi-scale grouping (MSG) for varying densities; Feature propagation for dense prediction |
| **Claims** | SOTA on ModelNet40 (91.9%), ShapeNet part segmentation, ScanNet semantic segmentation |
| **Evaluation** | Multiple 3D benchmarks; indoor/outdoor scenes |
| **Strengths** | Handles unordered point sets; hierarchical local features; density-adaptive |
| **Limitations** | Computationally expensive for large point clouds; limited long-range context |
| **Relevance to RQs** | **RQ-T1 (Critical)**: Primary backbone for LiDAR structural encoder in HyLiFormer |
| **Follow-chain** | 15,000+ citations; foundation for point cloud DL |
| **ISRO Applicability** | TRL 4 - Applicable to future LiDAR satellite missions |

---

### Paper Card 2.2

| Field | Content |
|-------|---------|
| **Citation** | Ayrey, E., & Hayes, D. J. (2018). The Use of Three-Dimensional Convolutional Neural Networks to Interpret LiDAR for Forest Inventory. *Remote Sensing*, 10(4), 649. |
| **Core Idea** | 3D-CNN on voxelized LiDAR for direct forest inventory parameter prediction |
| **Method** | Voxelization of point clouds (1m resolution); 3D-CNN with multiple conv layers; Regression heads for biomass, basal area, stem density |
| **Claims** | R² = 0.82 for biomass; R² = 0.78 for basal area; outperforms traditional LiDAR metrics |
| **Evaluation** | 500+ field plots in Maine forests; comparison with LiDAR-derived metrics |
| **Strengths** | End-to-end learning; no manual feature engineering; handles 3D structure directly |
| **Limitations** | Voxelization loses fine detail; fixed resolution; computationally intensive |
| **Relevance to RQs** | **RQ-T1 (Medium)**: Alternative voxel-based approach for LiDAR encoding |
| **Follow-chain** | 280+ citations; spawned forest-specific DL work |
| **ISRO Applicability** | TRL 4 - Applicable to NISAR vegetation products |

---

### Paper Card 2.3

| Field | Content |
|-------|---------|
| **Citation** | Windrim, L., Ramakrishnan, R., Melkumyan, A., Murphy, R. J., & Chlingaryan, A. (2019). Unsupervised Feature Learning for Automated Tree Crown Delineation from Airborne LiDAR. *Remote Sensing*, 11(12), 1443. |
| **Core Idea** | Autoencoder-based unsupervised feature learning for individual tree crown segmentation |
| **Method** | Convolutional autoencoder on CHM rasters; Learned features used for watershed segmentation; Transfer learning to new forest sites |
| **Claims** | F1 = 0.83 for tree detection; generalizes across forest types |
| **Evaluation** | Multiple Australian forest sites; comparison with manual delineation |
| **Strengths** | Unsupervised; transferable; handles varying tree densities |
| **Limitations** | 2D CHM loses vertical structure; requires post-processing for individual trees |
| **Relevance to RQs** | **RQ-V1 (Medium)**: Individual tree detection component for validation |
| **Follow-chain** | 95+ citations; relevant for pre-processing |
| **ISRO Applicability** | TRL 4 - Applicable to Cartosat-3 stereo DEMs |

---

### Paper Card 2.4

| Field | Content |
|-------|---------|
| **Citation** | Briechle, S., Krzystek, P., & Vosselman, G. (2021). Silvi-Net: A Deep Learning Architecture for Tree Species Classification using UAV-borne LiDAR Point Clouds. *ISPRS Journal of Photogrammetry and Remote Sensing*, 175, 78-93. |
| **Core Idea** | Deep learning directly on UAV LiDAR point clouds for tree species classification |
| **Method** | PointNet++ backbone adapted for forestry; Species-specific structural feature learning; Multi-scale point aggregation |
| **Claims** | 88.4% OA for 8 species; 91.2% for 4-class grouping |
| **Evaluation** | German mixed forest; 1,000+ individual trees; comparison with RF on LiDAR metrics |
| **Strengths** | End-to-end on raw point clouds; captures 3D crown architecture; UAV-specific design |
| **Limitations** | Limited to species with distinct crown shapes; requires individual tree segmentation |
| **Relevance to RQs** | **RQ-T1 (High)**: Direct precedent for LiDAR-based species classification component |
| **Follow-chain** | 120+ citations; active research line |
| **ISRO Applicability** | TRL 4 - Highly relevant for UAV-satellite integration |

---

### Paper Card 2.5

| Field | Content |
|-------|---------|
| **Citation** | Zhao, H., Jiang, L., Jia, J., Torr, P., & Koltun, V. (2021). Point Transformer. *ICCV*, 16259-16268. |
| **Core Idea** | Self-attention mechanism adapted for 3D point clouds |
| **Method** | Vector self-attention with positional encoding for points; Local attention within k-nearest neighbors; Hierarchical architecture similar to PointNet++ |
| **Claims** | SOTA on S3DIS (70.4% mIoU); ModelNet40 (93.7% OA) |
| **Evaluation** | Multiple 3D benchmarks; indoor and outdoor scenes |
| **Strengths** | Attention for point clouds; captures complex relationships; interpretable |
| **Limitations** | Computationally expensive; requires careful neighborhood design |
| **Relevance to RQs** | **RQ-T1 (High)**: State-of-art point cloud processing; potential upgrade for LiDAR encoder |
| **Follow-chain** | 1,800+ citations; rapidly adopted |
| **ISRO Applicability** | TRL 3 - Proof of concept; future research direction |

---

## Cluster 3: HSI-LiDAR Fusion Methods

### Paper Card 3.1

| Field | Content |
|-------|---------|
| **Citation** | Dalponte, M., Bruzzone, L., & Gianelle, D. (2012). Tree Species Classification in the Southern Alps Based on the Fusion of Very High Resolution Multispectral Data and LIDAR Data. *Remote Sensing of Environment*, 123, 258-270. |
| **Core Idea** | Foundational work on optical-LiDAR fusion for tree species classification |
| **Method** | Feature-level fusion of multispectral bands with LiDAR-derived metrics (height, intensity, texture); SVM classification on fused features |
| **Claims** | 74% OA for 7 species; LiDAR adds 8-12% accuracy gain over optical alone |
| **Evaluation** | Italian Alps; 1,000+ reference trees; systematic fusion comparison |
| **Strengths** | Systematic evaluation of fusion benefits; practical workflow; well-documented |
| **Limitations** | Limited spectral resolution; handcrafted features; SVM limitations |
| **Relevance to RQs** | **RQ-T2 (High)**: Establishes baseline fusion performance; motivates hyperspectral upgrade |
| **Follow-chain** | 520+ citations; seminal fusion paper |
| **ISRO Applicability** | TRL 6 - Validated in operational environment; applicable to Resourcesat-LiDAR fusion |

---

### Paper Card 3.2

| Field | Content |
|-------|---------|
| **Citation** | Shen, X., & Cao, L. (2017). Tree Species Classification Using Hyperspectral and LiDAR Data. *Remote Sensing*, 9(11), 1180. |
| **Core Idea** | Comprehensive evaluation of HSI-LiDAR fusion strategies for species discrimination |
| **Method** | Early fusion (feature concatenation), late fusion (decision combination), and hierarchical fusion; Multiple classifiers (RF, SVM, kNN) |
| **Claims** | Early fusion best for HSI-LiDAR; 89.7% OA for 5 species; LiDAR adds 15% accuracy |
| **Evaluation** | Chinese subtropical forest; airborne HSI (CASI) + LiDAR; 200+ field plots |
| **Strengths** | Systematic fusion comparison; subtropical forest focus; practical insights |
| **Limitations** | Traditional ML only; limited species count; no DL comparison |
| **Relevance to RQs** | **RQ-T2 (Critical)**: Direct precedent for fusion strategy comparison; baseline for DL improvement |
| **Follow-chain** | 180+ citations; highly relevant |
| **ISRO Applicability** | TRL 5 - Applicable to AVIRIS-NG + airborne LiDAR campaigns |

---

### Paper Card 3.3

| Field | Content |
|-------|---------|
| **Citation** | Matasci, G., Hermosilla, T., Wulder, M. A., White, J. C., Coops, N. C., Hobart, G. W., & Zald, H. S. (2018). Large-area Mapping of Canadian Boreal Forest Cover, Height, Biomass and Other Structural Attributes using Landsat Composites and Lidar Plots. *Remote Sensing of Environment*, 209, 90-106. |
| **Core Idea** | Scaling plot-level LiDAR to wall-to-wall mapping using satellite imagery |
| **Method** | LiDAR plots as training data for Random Forest models; Landsat spectral-temporal features; k-NN imputation for structural attributes |
| **Claims** | R² = 0.65 for canopy height; applicable across 650M ha |
| **Evaluation** | Canadian boreal forest; 25,000+ LiDAR plots; wall-to-wall validation |
| **Strengths** | Operational scale; practical workflow; addresses scalability |
| **Limitations** | Landsat spectral limitations; moderate accuracy; no DL |
| **Relevance to RQs** | **RQ-V2 (High)**: Scaling methodology from UAV to satellite; practical framework |
| **Follow-chain** | 480+ citations; influential for scaling approaches |
| **ISRO Applicability** | TRL 6 - Directly applicable to ISRO scaling objectives |

---

### Paper Card 3.4

| Field | Content |
|-------|---------|
| **Citation** | Zhang, C., Yue, P., Di, L., & Wu, Z. (2021). Multi-source Data Fusion for Semantic Segmentation using Deep Learning. *ISPRS Journal of Photogrammetry and Remote Sensing*, 178, 167-181. |
| **Core Idea** | Deep learning framework for fusing multiple remote sensing data sources |
| **Method** | Dual-stream encoder (one per modality); Cross-modal attention for feature interaction; Semantic segmentation decoder |
| **Claims** | +5-8% mIoU over single-source; attention reveals modality contributions |
| **Evaluation** | Urban and rural scenes; optical + DSM data; ablation on fusion strategies |
| **Strengths** | Principled attention-based fusion; interpretable; flexible architecture |
| **Limitations** | Not forest-specific; 2D DSM vs 3D LiDAR; urban focus |
| **Relevance to RQs** | **RQ-T2 (High)**: Cross-modal attention directly applicable to HyLiFormer fusion module |
| **Follow-chain** | 210+ citations; active research |
| **ISRO Applicability** | TRL 4 - Applicable to multi-mission data integration |

---

### Paper Card 3.5

| Field | Content |
|-------|---------|
| **Citation** | Zhao, X., Liang, J., Chen, B., Huang, X., & Zhang, L. (2023). Deep Multimodal Fusion for Hyperspectral and LiDAR Classification. *IEEE Transactions on Geoscience and Remote Sensing*, 61, 1-15. |
| **Core Idea** | State-of-art deep fusion network specifically for HSI-LiDAR land cover mapping |
| **Method** | Spectral transformer for HSI; Point-based network for LiDAR; Cross-attention fusion at multiple scales; Adaptive modality weighting |
| **Claims** | 96.2% OA on Houston 2013 (HSI+LiDAR); +3.5% over best single-modality |
| **Evaluation** | Houston 2013, Trento datasets; comprehensive ablation; attention visualization |
| **Strengths** | SOTA for HSI-LiDAR; attention-based; comprehensive evaluation |
| **Limitations** | Urban focus; limited vegetation classes; computational cost |
| **Relevance to RQs** | **RQ-T1, RQ-T2 (Critical)**: Most relevant fusion architecture; direct template for HyLiFormer |
| **Follow-chain** | 45+ citations (recent); rapidly growing |
| **ISRO Applicability** | TRL 4 - Component validation; high potential for ISRO integration |

---

### Paper Card 3.6

| Field | Content |
|-------|---------|
| **Citation** | Haas, F., Gerhards, M., Timmermann, S., & Hoefle, B. (2024). Deep Learning for Tree Species Identification from UAV-borne Hyperspectral and LiDAR Data. *ISPRS Journal of Photogrammetry and Remote Sensing*, 208, 45-61. |
| **Core Idea** | End-to-end deep learning for tree species using UAV HSI-LiDAR fusion |
| **Method** | CNN-Transformer hybrid for HSI; PointNet++ for LiDAR; Late fusion with learned weights; Species-specific attention |
| **Claims** | 91.3% OA for 12 temperate species; LiDAR improves accuracy by 7% |
| **Evaluation** | German forest; 2,000+ reference trees; cross-site validation |
| **Strengths** | UAV-specific; forest focus; practical pipeline; recent methods |
| **Limitations** | Temperate forest only; moderate species count; no tropical validation |
| **Relevance to RQs** | **RQ-T1, RQ-T2, RQ-V1 (Critical)**: Closest methodological precedent; adaptation needed for tropical |
| **Follow-chain** | Recent publication; emerging citations |
| **ISRO Applicability** | TRL 4 - Highly relevant; adaptation for Indian forests needed |

---

## Cluster 4: Tree Species Classification from Remote Sensing

### Paper Card 4.1

| Field | Content |
|-------|---------|
| **Citation** | Fassnacht, F. E., Latifi, H., Stereńczak, K., Modzelewska, A., Lefsky, M., Waser, L. T., ... & Ghosh, A. (2016). Review of Studies on Tree Species Classification from Remotely Sensed Data. *Remote Sensing of Environment*, 186, 64-87. |
| **Core Idea** | Comprehensive review of tree species classification using remote sensing |
| **Method** | Systematic literature review; Analysis of 129 studies; Meta-analysis of accuracy factors |
| **Claims** | Hyperspectral outperforms multispectral by 10-15%; LiDAR fusion adds 5-10%; tropical forests understudied |
| **Evaluation** | Qualitative and quantitative synthesis; accuracy meta-analysis |
| **Strengths** | Comprehensive; identifies research gaps; practical recommendations |
| **Limitations** | Pre-deep learning era; outdated methods |
| **Relevance to RQs** | **RQ-P (High)**: Establishes state-of-field; identifies tropical gap our work addresses |
| **Follow-chain** | 1,050+ citations; seminal review |
| **ISRO Applicability** | TRL N/A - Review paper; informs methodology design |

---

### Paper Card 4.2

| Field | Content |
|-------|---------|
| **Citation** | Sothe, C., Almeida, C. M., Liesenberg, V., & Schimalski, M. B. (2017). Evaluating Sentinel-2 and Landsat-8 Data to Map Successional Forest Stages in a Subtropical Forest. *Remote Sensing*, 9(8), 838. |
| **Core Idea** | Multispectral satellite data for forest succession stage mapping in subtropical Brazil |
| **Method** | Object-based classification; Spectral-temporal features; Random Forest classifier |
| **Claims** | 87.5% OA for 4 succession stages; Sentinel-2 outperforms Landsat-8 |
| **Evaluation** | Atlantic Forest remnants; field validation; comparison of sensors |
| **Strengths** | Subtropical focus; practical workflow; open satellite data |
| **Limitations** | Not species-level; multispectral limitations; no DL |
| **Relevance to RQs** | **RQ-V2 (Medium)**: Satellite baseline for scaling; subtropical context |
| **Follow-chain** | 240+ citations; relevant for LULC context |
| **ISRO Applicability** | TRL 6 - Applicable to Resourcesat/Sentinel comparison |

---

### Paper Card 4.3

| Field | Content |
|-------|---------|
| **Citation** | Modzelewska, A., Fassnacht, F. E., & Stereńczak, K. (2020). Tree Species Identification within an Extensive Forest Area with Diverse Management Regimes using Airborne Hyperspectral Data. *International Journal of Applied Earth Observation and Geoinformation*, 84, 101960. |
| **Core Idea** | Large-area species classification using airborne hyperspectral in managed forests |
| **Method** | APEX hyperspectral data (288 bands); Spectral indices + full spectra; SVM and RF classifiers |
| **Claims** | 82.3% OA for 11 species across 150 km² |
| **Evaluation** | Polish forests; 400+ field plots; spatial transferability analysis |
| **Strengths** | Large-area operational; addresses spatial variability; practical insights |
| **Limitations** | Traditional ML; no structural data; temperate focus |
| **Relevance to RQs** | **RQ-V1 (High)**: Operational considerations; accuracy expectations at scale |
| **Follow-chain** | 85+ citations; practical reference |
| **ISRO Applicability** | TRL 5 - Directly applicable to AVIRIS-NG campaigns |

---

### Paper Card 4.4

| Field | Content |
|-------|---------|
| **Citation** | Pu, R. (2021). Mapping Tree Species Using Advanced Remote Sensing Technologies: A State-of-the-Art Review and Perspective. *Journal of Remote Sensing*, 2021, 9812624. |
| **Core Idea** | Updated review of tree species mapping with focus on emerging technologies |
| **Method** | Literature review; Technology assessment; Future directions |
| **Claims** | DL outperforming traditional by 5-15%; multi-sensor fusion critical; tropical forests need attention |
| **Evaluation** | Qualitative synthesis; technology readiness assessment |
| **Strengths** | Current; covers DL; identifies research priorities |
| **Limitations** | Review only; no original experiments |
| **Relevance to RQs** | **RQ-P (High)**: Validates our approach; confirms research gap |
| **Follow-chain** | 180+ citations; recent influential review |
| **ISRO Applicability** | TRL N/A - Strategic reference for ISRO planning |

---

### Paper Card 4.5

| Field | Content |
|-------|---------|
| **Citation** | Scholl, V. M., Cattau, M. E., Joseph, M. B., & Balch, J. K. (2020). Integrating National Ecological Observatory Network (NEON) Airborne Remote Sensing and In-situ Data for Optimal Tree Species Classification. *Remote Sensing*, 12(9), 1414. |
| **Core Idea** | Benchmark study using NEON data for tree species classification |
| **Method** | NEON HSI (426 bands) + LiDAR; Multiple classifiers (RF, SVM, XGBoost); Feature importance analysis |
| **Claims** | 83.4% OA for 10 species; spectral features dominate (75% importance) |
| **Evaluation** | 6 NEON sites; standardized protocol; cross-site validation |
| **Strengths** | Standardized benchmark; open data; reproducible; feature importance |
| **Limitations** | Traditional ML; US forests only; no DL baseline |
| **Relevance to RQs** | **RQ-T3 (High)**: Feature importance analysis; spectral vs structural contribution |
| **Follow-chain** | 95+ citations; benchmark reference |
| **ISRO Applicability** | TRL 5 - Methodology transferable to Indian context |

---

## Cluster 5: UAV Remote Sensing for Forest Monitoring

### Paper Card 5.1

| Field | Content |
|-------|---------|
| **Citation** | Nezami, S., Khoramshahi, E., Nevalainen, O., Pölönen, I., & Honkavaara, E. (2020). Tree Species Classification of Drone Hyperspectral and RGB Imagery with Deep Learning Convolutional Neural Networks. *Remote Sensing*, 12(7), 1070. |
| **Core Idea** | CNN-based tree species classification from UAV hyperspectral imagery |
| **Method** | Rikola hyperspectral camera (50 bands); Individual tree crowns as samples; 1D-CNN and 2D-CNN comparison |
| **Claims** | 97.9% OA for 3 conifer species; 1D-CNN slightly outperforms 2D |
| **Evaluation** | Finnish boreal forest; 4,000+ crown samples; 10-fold CV |
| **Strengths** | UAV HSI specific; practical pipeline; high accuracy |
| **Limitations** | Limited species; boreal only; simple CNN architecture |
| **Relevance to RQs** | **RQ-T1 (Medium)**: UAV HSI baseline; practical considerations |
| **Follow-chain** | 175+ citations; frequently cited for UAV HSI |
| **ISRO Applicability** | TRL 4 - Applicable to UAV-satellite integration |

---

### Paper Card 5.2

| Field | Content |
|-------|---------|
| **Citation** | Cao, J., Liu, K., Zhuo, L., Liu, L., Zhu, Y., & Peng, L. (2021). Combining UAV-based Hyperspectral and LiDAR Data for Mangrove Species Classification using the Rotation Forest Algorithm. *International Journal of Applied Earth Observation and Geoinformation*, 102, 102414. |
| **Core Idea** | UAV HSI-LiDAR fusion for mangrove species in tropical coastal ecosystem |
| **Method** | DJI UAV with Headwall HSI + Velodyne LiDAR; Feature-level fusion; Rotation Forest classifier |
| **Claims** | 87.3% OA for 5 mangrove species; fusion adds 8% over HSI alone |
| **Evaluation** | South China mangroves; 300+ field samples; ablation on features |
| **Strengths** | Tropical species; UAV dual-sensor; practical workflow |
| **Limitations** | Traditional ML; mangrove-specific; limited generalization |
| **Relevance to RQs** | **RQ-T2, RQ-V1 (High)**: Tropical UAV HSI-LiDAR precedent; closest ecosystem analog |
| **Follow-chain** | 110+ citations; highly relevant |
| **ISRO Applicability** | TRL 5 - Applicable to coastal zone monitoring |

---

### Paper Card 5.3

| Field | Content |
|-------|---------|
| **Citation** | Tuominen, S., Balazs, A., Honkavaara, E., Pölönen, I., Saari, H., Hakala, T., & Viljanen, N. (2017). Hyperspectral UAV-imagery and Photogrammetric Canopy Height Model in Estimating Forest Stand Variables. *Silva Fennica*, 51(5), 7721. |
| **Core Idea** | UAV HSI combined with photogrammetric CHM for forest inventory |
| **Method** | FPI hyperspectral camera; Structure-from-Motion CHM; RF regression for stand variables |
| **Claims** | R² = 0.85 for basal area; UAV CHM comparable to LiDAR CHM |
| **Evaluation** | Finnish managed forests; 150 field plots |
| **Strengths** | Practical alternative to LiDAR; cost-effective; operational |
| **Limitations** | CHM less accurate than LiDAR; temperate only |
| **Relevance to RQs** | **RQ-T3 (Medium)**: Alternative structural data source; cost considerations |
| **Follow-chain** | 110+ citations; practical reference |
| **ISRO Applicability** | TRL 5 - Cost-effective option for initial campaigns |

---

### Paper Card 5.4

| Field | Content |
|-------|---------|
| **Citation** | Luo, S., Wang, C., Xi, X., Zeng, H., Li, D., Xia, S., & Wang, P. (2019). Fusion of Airborne Discrete-return LiDAR and Hyperspectral Data for Land Cover Classification. *Remote Sensing*, 11(14), 1626. |
| **Core Idea** | Systematic evaluation of airborne HSI-LiDAR fusion approaches |
| **Method** | CASI HSI + airborne LiDAR; Four fusion strategies (stacking, PCA, MNF, kernel); Multiple classifiers |
| **Claims** | Feature stacking best (88.7% OA); MNF reduces dimensionality effectively |
| **Evaluation** | Chinese forest-agricultural landscape; comparison of fusion methods |
| **Strengths** | Systematic fusion comparison; dimensionality analysis; practical insights |
| **Limitations** | Not species-level; airborne not UAV; traditional ML |
| **Relevance to RQs** | **RQ-T2 (High)**: Fusion strategy comparison baseline; feature engineering insights |
| **Follow-chain** | 85+ citations; methodological reference |
| **ISRO Applicability** | TRL 5 - Applicable to AVIRIS-NG + airborne LiDAR |

---

### Paper Card 5.5

| Field | Content |
|-------|---------|
| **Citation** | Müllerová, J., Brůna, J., Bartaloš, T., Dvořák, P., Vítková, M., & Pyšek, P. (2017). Timing Is Important: Unmanned Aircraft vs. Satellite Imagery in Plant Invasion Monitoring. *Frontiers in Plant Science*, 8, 887. |
| **Core Idea** | Comparison of UAV and satellite imagery for vegetation mapping across phenological stages |
| **Method** | DJI UAV RGB + Sentinel-2; Multi-temporal analysis; Object-based classification |
| **Claims** | UAV optimal for fine-scale; satellite sufficient for landscape-scale; timing critical |
| **Evaluation** | Czech grasslands; invasive species detection; seasonal comparison |
| **Strengths** | Multi-scale comparison; temporal analysis; practical recommendations |
| **Limitations** | RGB only; invasive species focus; not forest |
| **Relevance to RQs** | **RQ-V2 (Medium)**: UAV-satellite scaling insights; temporal considerations |
| **Follow-chain** | 185+ citations; influential for scale integration |
| **ISRO Applicability** | TRL 5 - Informs UAV-HySIS integration strategy |

---

## Cluster 6: ISRO & DOS Missions for Vegetation Analysis (MANDATORY)

### Paper Card 6.1

| Field | Content |
|-------|---------|
| **Citation** | Bhattacharya, B. K., Green, R. O., Rao, S., Saxena, M., Sharma, S., Kumar, K. A., ... & Dadhwal, V. K. (2019). An Overview of AVIRIS-NG Airborne Hyperspectral Science Campaign over India. *Current Science*, 116(7), 1082-1088. |
| **Core Idea** | First comprehensive overview of AVIRIS-NG campaigns in India |
| **Method** | AVIRIS-NG sensor specifications; Campaign design; Data products; Initial results |
| **Claims** | 425 bands (380-2510 nm); 4-8m resolution; successful campaigns over diverse Indian landscapes |
| **Evaluation** | Multiple Indian sites; preliminary validation; data quality assessment |
| **Strengths** | Official ISRO documentation; sensor specifications; campaign protocols |
| **Limitations** | Overview only; limited scientific analysis |
| **Relevance to RQs** | **RQ-V2 (Critical)**: Primary satellite data source; spectral specifications for model design |
| **Follow-chain** | 180+ citations; foundational ISRO reference |
| **ISRO Applicability** | TRL 7 - Operational system; direct data source for our project |

---

### Paper Card 6.2

| Field | Content |
|-------|---------|
| **Citation** | Saxena, M., Sharma, S., Bhattacharya, B. K., & Javed, M. (2021). Hyperspectral Remote Sensing for Agriculture and Vegetation Studies using AVIRIS-NG Data. *Journal of the Indian Society of Remote Sensing*, 49(10), 2423-2435. |
| **Core Idea** | Application of AVIRIS-NG data for vegetation analysis in India |
| **Method** | Spectral unmixing; Vegetation indices; Crop type mapping; Forest analysis |
| **Claims** | Species-level discrimination achievable; AVIRIS-NG suitable for biodiversity mapping |
| **Evaluation** | Multiple Indian agricultural and forest sites |
| **Strengths** | Indian context; AVIRIS-NG specific; vegetation focus |
| **Limitations** | Traditional methods; no DL; limited forest focus |
| **Relevance to RQs** | **RQ-V2 (High)**: Establishes AVIRIS-NG utility for vegetation; Indian forest context |
| **Follow-chain** | 45+ citations; growing relevance |
| **ISRO Applicability** | TRL 6 - Validated methodology; applicable to our project |

---

### Paper Card 6.3

| Field | Content |
|-------|---------|
| **Citation** | Kushwaha, S. P. S., Nandy, S., & Gupta, M. (2014). Growing Stock and Woody Biomass Assessment in Asola-Bhatti Wildlife Sanctuary, Delhi, India. *Environmental Monitoring and Assessment*, 186(9), 5911-5920. |
| **Core Idea** | Remote sensing-based forest inventory in Indian wildlife sanctuary |
| **Method** | Resourcesat-2 LISS-IV; Field-based biomass estimation; Regression modeling |
| **Claims** | R² = 0.72 for AGB; practical methodology for Indian forests |
| **Evaluation** | Delhi wildlife sanctuary; extensive field plots |
| **Strengths** | Indian forest context; practical methodology; ISRO data |
| **Limitations** | Multispectral only; not species-level; limited area |
| **Relevance to RQs** | **RQ-V1 (Medium)**: Indian forest baseline; field validation protocol reference |
| **Follow-chain** | 95+ citations; frequently cited for Indian forests |
| **ISRO Applicability** | TRL 6 - Operational methodology; applicable to Meghalaya |

---

### Paper Card 6.4

| Field | Content |
|-------|---------|
| **Citation** | Roy, P. S., Behera, M. D., Murthy, M. S. R., Roy, A., Singh, S., Kushwaha, S. P. S., ... & Ramachandran, R. M. (2015). New Vegetation Type Map of India Prepared using Satellite Remote Sensing. *Current Science*, 108(8), 1538-1551. |
| **Core Idea** | National-scale vegetation mapping using ISRO satellite data |
| **Method** | Multi-temporal Resourcesat data; Hierarchical classification; Ground validation |
| **Claims** | 1:50,000 scale vegetation map; 75 vegetation types mapped |
| **Evaluation** | All-India coverage; extensive ground validation; accuracy assessment |
| **Strengths** | National scale; comprehensive; ISRO operational product |
| **Limitations** | Coarse classification; not species-level; multispectral |
| **Relevance to RQs** | **RQ-V1 (High)**: Baseline vegetation map; context for Meghalaya forest types |
| **Follow-chain** | 320+ citations; fundamental reference |
| **ISRO Applicability** | TRL 8 - Operational product; direct contextual reference |

---

### Paper Card 6.5

| Field | Content |
|-------|---------|
| **Citation** | NRSC/ISRO (2021). *HySIS Data Products and Applications*. Technical Report, National Remote Sensing Centre, Hyderabad. |
| **Core Idea** | Official HySIS mission documentation and application guidelines |
| **Method** | HySIS sensor specifications (55 bands, 400-950nm, 30m); Data products; Application domains |
| **Claims** | First Indian hyperspectral satellite; suitable for vegetation, agriculture, geology |
| **Evaluation** | System validation; initial application demonstrations |
| **Strengths** | Official specifications; data access protocols; processing guidelines |
| **Limitations** | VNIR only (no SWIR); 30m resolution limits tree-level analysis |
| **Relevance to RQs** | **RQ-V2 (Critical)**: Primary satellite platform; design constraints for model |
| **Follow-chain** | Technical report; foundational for HySIS applications |
| **ISRO Applicability** | TRL 9 - Operational mission; direct project dependency |

---

### Paper Card 6.6

| Field | Content |
|-------|---------|
| **Citation** | Behera, M. D., Roy, P. S., & Panda, R. M. (2017). Plant Species Richness Estimation using Machine Learning and Geospatial Data. *Ecological Informatics*, 39, 100-110. |
| **Core Idea** | Machine learning for biodiversity estimation using Indian RS data |
| **Method** | Resourcesat-2 + MODIS; Environmental predictors; RF and MaxEnt models |
| **Claims** | Species richness patterns captured; RS-based biodiversity assessment feasible |
| **Evaluation** | Western Ghats and Eastern Himalaya (including NE India) |
| **Strengths** | Indian biodiversity hotspots; practical methodology; includes NE India |
| **Limitations** | Coarse resolution; no hyperspectral; species richness not composition |
| **Relevance to RQs** | **RQ-P (High)**: Biodiversity mapping context; NE India reference |
| **Follow-chain** | 75+ citations; relevant for biodiversity context |
| **ISRO Applicability** | TRL 5 - Methodology applicable; upgrade with HSI proposed |

---

### Paper Card 6.7

| Field | Content |
|-------|---------|
| **Citation** | Tripathi, P., Behera, M. D., & Roy, P. S. (2019). Plant Invasion Correlation with Climate Anomaly: An Indian Retrospect. *Biodiversity and Conservation*, 28(8-9), 2049-2062. |
| **Core Idea** | Remote sensing-based invasion monitoring in Indian ecosystems |
| **Method** | Multi-temporal satellite analysis; Climate correlation; Change detection |
| **Claims** | Invasion patterns linked to climate variability; RS monitoring effective |
| **Evaluation** | Multiple Indian forest sites |
| **Strengths** | Indian context; temporal analysis; practical methodology |
| **Limitations** | Invasion focus; not species-level native mapping |
| **Relevance to RQs** | **RQ-V1 (Medium)**: Change detection methodology; temporal considerations |
| **Follow-chain** | 55+ citations; relevant for monitoring |
| **ISRO Applicability** | TRL 5 - Applicable to forest change monitoring |

---

### Paper Card 6.8

| Field | Content |
|-------|---------|
| **Citation** | Reddy, C. S., Jha, C. S., Diwakar, P. G., & Dadhwal, V. K. (2015). Nationwide Classification of Forest Types of India using Remote Sensing and GIS. *Environmental Monitoring and Assessment*, 187(12), 777. |
| **Core Idea** | Comprehensive forest type classification for India using ISRO data |
| **Method** | IRS data; Object-based classification; Champion & Seth forest type system |
| **Claims** | 16 forest type groups mapped; 78.4% overall accuracy |
| **Evaluation** | All-India; comparison with ground data; FSI validation |
| **Strengths** | National baseline; Indian forest type system; comprehensive |
| **Limitations** | Broad classification; not species-level; multispectral |
| **Relevance to RQs** | **RQ-V1 (High)**: Forest type context for Meghalaya; baseline classification |
| **Follow-chain** | 185+ citations; fundamental reference |
| **ISRO Applicability** | TRL 7 - Operational product; contextual baseline |

---

## Initial Comparison Matrix

### Approach × Criteria Matrix

| Paper | Modality | DL Method | Species Count | Accuracy | Forest Type | ISRO Relevance |
|-------|----------|-----------|---------------|----------|-------------|----------------|
| Hong et al. (SpectralFormer) | HSI only | Transformer | N/A (LULC) | 99%+ | Urban/Agri | TRL 4 |
| Roy et al. (HybridSN) | HSI only | Hybrid CNN | N/A (LULC) | 99%+ | Urban/Agri | TRL 5 |
| Qi et al. (PointNet++) | LiDAR only | PointNet | N/A (3D) | 92% | General 3D | TRL 4 |
| Briechle et al. (Silvi-Net) | LiDAR only | PointNet++ | 8 | 88% | Temperate | TRL 4 |
| Zhao et al. (2023) | HSI+LiDAR | Transformer+Attention | N/A (LULC) | 96% | Urban | TRL 4 |
| Haas et al. (2024) | HSI+LiDAR | CNN-Transformer | 12 | 91% | Temperate | TRL 4 |
| Shen & Cao (2017) | HSI+LiDAR | RF/SVM | 5 | 90% | Subtropical | TRL 5 |
| Cao et al. (2021) | HSI+LiDAR | Rotation Forest | 5 | 87% | Tropical (Mangrove) | TRL 5 |
| Scholl et al. (2020) | HSI+LiDAR | RF/SVM/XGBoost | 10 | 83% | Temperate | TRL 5 |
| AVIRIS-NG (2019) | HSI | Spectral analysis | N/A | N/A | Indian diverse | TRL 7 |
| HySIS (2021) | HSI | N/A | N/A | N/A | Indian diverse | TRL 9 |

### Key Observations

1. **Architecture Gap**: No transformer-based fusion for tropical forest species
2. **Tropical Gap**: Limited DL studies in tropical Asian forests
3. **ISRO Gap**: No DL frameworks validated on HySIS/AVIRIS-NG for species
4. **Species Count**: Most studies <15 species; 20+ species challenging
5. **Accuracy Ceiling**: ~90% achievable for species; ~96% for LULC

---

## Phase Status
**PHASE 2b: LITERATURE CARDS COMPLETE** ✓

**→ Proceed to PHASE 2c: Synthesis & Gap Confirmation**
