# Phase 1: Gap Statement & Research Questions

## Research Topic
**Deep Learning-based Framework for Forest Species Classification using UAV Hyperspectral & LiDAR Data in Meghalaya**

---

## 1. Gap Statement

> **Current approaches** to forest species classification in tropical/subtropical regions **typically** rely on multispectral satellite imagery (Landsat, Sentinel-2) with traditional machine learning classifiers (Random Forest, SVM) or single-modality deep learning models, **but struggle with**:
> - Fine-grained species-level discrimination due to limited spectral bands
> - Distinguishing species with similar spectral signatures but different structural characteristics
> - Generalizing across heterogeneous forest ecosystems with mixed canopy structures
> - Integrating multi-modal data (spectral + structural) in end-to-end learnable frameworks
> 
> **We propose** a hybrid deep learning architecture that jointly models hyperspectral signatures and LiDAR-derived structural parameters through attention-based fusion mechanisms **to achieve**:
> - ≥85% species-level classification accuracy for Meghalaya's diverse forest types
> - Tree-level (individual crown) mapping capability
> - Transferable framework aligned with ISRO's Earth Observation missions
> 
> **Under constraints of**:
> - Limited labeled training data for endemic species
> - Challenging terrain and monsoon-affected data acquisition windows
> - Operational deployment requirements for forest management DSS

---

## 2. Research Questions

### 2.1 Primary Research Question (PRQ)

**PRQ:** *How can a deep learning framework effectively fuse UAV-based hyperspectral imagery and LiDAR point clouds to achieve accurate, fine-grained forest species classification and biodiversity mapping in Meghalaya's diverse forest ecosystems?*

#### Sub-components:
- What architectural design enables optimal spectral-spatial-structural feature learning?
- How does the fused approach compare to single-modality baselines?
- What are the operational requirements for deployment in a forest management DSS?

---

### 2.2 Technical Research Questions (TRQs)

#### TRQ-1: Spectral Feature Learning
*What deep learning architecture most effectively captures discriminative spectral signatures from hyperspectral imagery for tree species differentiation in tropical/subtropical forests?*

**Hypotheses:**
- H1a: 3D-CNN architectures outperform 2D-CNNs for joint spectral-spatial feature extraction
- H1b: Attention mechanisms improve focus on species-discriminative spectral bands
- H1c: Spectral dimensionality reduction as preprocessing improves model efficiency without significant accuracy loss

**Metrics:** Per-class F1-score, spectral band importance weights, computational efficiency

---

#### TRQ-2: Structural Feature Extraction
*How can LiDAR-derived structural parameters (canopy height, crown geometry, vertical profiles) be optimally encoded for integration with spectral features?*

**Hypotheses:**
- H2a: Point cloud-native architectures (PointNet++, DGCNN) preserve more structural information than rasterized approaches
- H2b: Multi-scale structural features (tree, stand, landscape) improve classification robustness
- H2c: Canopy height models (CHM) alone are insufficient; full 3D structure is needed for species discrimination

**Metrics:** Structural feature discriminability, reconstruction accuracy, inter-species structural variance

---

#### TRQ-3: Multi-Modal Fusion Strategy
*What fusion strategy (early, late, or hybrid) yields optimal performance for hyperspectral-LiDAR integration in forest classification?*

**Hypotheses:**
- H3a: Attention-based fusion outperforms simple concatenation or averaging
- H3b: Cross-modal attention enables the model to leverage complementary information
- H3c: Intermediate (hybrid) fusion preserves modality-specific features while enabling interaction

**Metrics:** Fusion gain (vs. single modality), attention weight interpretability, feature complementarity measures

---

#### TRQ-4: Data Efficiency & Transfer Learning
*How can the framework maintain high accuracy under limited labeled training data conditions typical of forest monitoring applications?*

**Hypotheses:**
- H4a: Pre-training on global hyperspectral datasets improves Meghalaya-specific fine-tuning
- H4b: Self-supervised learning on unlabeled UAV data reduces annotation requirements
- H4c: Active learning strategies optimize ground truth collection efficiency

**Metrics:** Learning curves, sample efficiency, transfer learning gain, annotation cost reduction

---

### 2.3 Validation Research Questions (VRQs)

#### VRQ-1: Generalization & Robustness
*How well does the trained model generalize across different forest types, seasonal conditions, and sensor configurations within Meghalaya and beyond?*

**Evaluation Dimensions:**
- Cross-site validation (training on Site A, testing on Site B)
- Temporal robustness (different seasons/years)
- Sensor transferability (UAV vs. satellite hyperspectral)
- Forest type adaptation (tropical wet → subtropical pine)

**Metrics:** Domain shift degradation, adaptation efficiency, confidence calibration

---

#### VRQ-2: Operational Viability
*What are the computational, data quality, and workflow requirements for deploying the framework in an operational forest monitoring DSS?*

**Evaluation Dimensions:**
- Inference speed and resource requirements
- Minimum data quality thresholds
- User expertise requirements
- Integration with existing GIS workflows

**Metrics:** Processing time per hectare, minimum training samples, user acceptance testing results

---

## 3. Research Questions Mapping

### RQ → Contribution Mapping
| Research Question | Primary Contribution | ISRO Relevance |
|-------------------|---------------------|----------------|
| PRQ | Overall framework | Space Vision 2047 AI-EO goals |
| TRQ-1 | Spectral encoding module | HySIS, AVIRIS-NG data utilization |
| TRQ-2 | Structural encoding module | Future LiDAR mission prep |
| TRQ-3 | Fusion architecture | Multi-sensor integration paradigm |
| TRQ-4 | Training strategies | Operational scalability |
| VRQ-1 | Generalization studies | Pan-India deployment potential |
| VRQ-2 | DSS design | Practical implementation |

### RQ → Methodology Mapping
| Research Question | Primary Method | Data Requirements |
|-------------------|----------------|-------------------|
| TRQ-1 | Ablation studies on spectral architectures | Hyperspectral imagery + labels |
| TRQ-2 | Comparative analysis of point cloud encoders | LiDAR point clouds + labels |
| TRQ-3 | Fusion strategy experiments | Co-registered HS + LiDAR |
| TRQ-4 | Transfer learning experiments | Multi-source datasets |
| VRQ-1 | Cross-validation studies | Multi-site, multi-temporal data |
| VRQ-2 | System benchmarking + user studies | DSS prototype |

---

## 4. Research Questions Prioritization

### Priority Matrix
| RQ | Scientific Impact | ISRO Alignment | Feasibility | Priority Score |
|----|-------------------|----------------|-------------|----------------|
| PRQ | High | High | Medium | **Critical** |
| TRQ-3 | High | High | Medium | **High** |
| TRQ-1 | High | High | High | **High** |
| TRQ-2 | Medium-High | Medium-High | Medium | **Medium-High** |
| TRQ-4 | Medium | High | Medium | **Medium-High** |
| VRQ-1 | Medium | High | Medium | **Medium** |
| VRQ-2 | Medium | High | High | **Medium** |

### Recommended Execution Order
1. **TRQ-1** → Establish spectral baseline
2. **TRQ-2** → Establish structural baseline
3. **TRQ-3** → Develop and validate fusion
4. **PRQ** → Integrate into complete framework
5. **TRQ-4** → Optimize for data efficiency
6. **VRQ-1** → Validate generalization
7. **VRQ-2** → Operational deployment studies

---

*Document Version: 1.0*  
*Phase: 1 - Idea Refinement*  
*Status: Complete*
