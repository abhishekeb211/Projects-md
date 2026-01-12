# Phase 1: Idea Deconstruction

## Research Topic
**Deep Learning-based Framework for Forest Species Classification using UAV Hyperspectral & LiDAR Data in Meghalaya**

---

## 1. Problem Statement

### Core Problem
Accurate, scalable, and automated classification of forest tree species, biodiversity mapping, and forest type identification in the ecologically diverse and challenging terrain of Meghalaya, Northeast India.

### Problem Dimensions
| Dimension | Description |
|-----------|-------------|
| **Technical** | Limited spectral resolution of traditional optical sensors fails to capture fine-grained species-level spectral signatures; LiDAR structural data remains underutilized in fusion architectures |
| **Operational** | Field-based surveys are labor-intensive, time-consuming, and spatially limited in dense tropical forests |
| **Scientific** | Lack of validated deep learning frameworks that jointly model spectral, spatial, and structural forest parameters |
| **Policy** | Need for Decision Support Systems (DSS) to inform forest management and conservation strategies |

---

## 2. Stakeholders

### Primary Stakeholders
| Stakeholder | Interest | Impact |
|-------------|----------|--------|
| **ISRO/DOS** | Advancing AI-driven geospatial analytics; validation of HySIS, AVIRIS-NG data products | High |
| **Meghalaya Forest Department** | Forest inventory, biodiversity conservation, illegal logging detection | High |
| **Research Community** | Novel deep learning architectures for hyperspectral-LiDAR fusion | High |

### Secondary Stakeholders
| Stakeholder | Interest | Impact |
|-------------|----------|--------|
| **Ministry of Environment, Forest & Climate Change** | National forest monitoring, REDD+ compliance | Medium |
| **Local Communities** | Sustainable forest management, community forest rights | Medium |
| **Climate Scientists** | Carbon stock estimation, climate change monitoring | Medium |
| **UAV/Sensor Industry** | Operational workflows for UAV-based forest monitoring | Low-Medium |

---

## 3. Why Now? (Temporal Relevance)

### Technology Drivers
- **ISRO's HySIS mission** (2018) and **AVIRIS-NG campaigns** provide unprecedented hyperspectral data availability
- **Deep learning advances** (Transformers, 3D-CNNs, attention mechanisms) enable complex spectral-spatial-structural modeling
- **UAV miniaturization** makes hyperspectral and LiDAR payloads operationally feasible
- **GPU computing accessibility** reduces computational barriers for complex model training

### Policy & Environmental Drivers
- **ISRO Space Vision 2047** emphasizes AI-driven Earth Observation for sustainable resource management
- **India's commitment to 33% forest cover** under National Forest Policy
- **Meghalaya's biodiversity hotspot status** (part of Indo-Burma hotspot) requires urgent monitoring
- **Climate change impacts** on Northeast India's forests demand continuous assessment

### Data Availability
- AVIRIS-NG India campaigns (2015-2020) covering forest regions
- Upcoming ISRO hyperspectral/LiDAR satellite missions
- Increasing availability of UAV-based data acquisition platforms

---

## 4. Feasibility Constraints

### 4.1 Data Constraints
| Constraint | Severity | Mitigation Strategy |
|------------|----------|---------------------|
| Limited labeled training data for Meghalaya species | High | Field campaigns + transfer learning from global datasets |
| Cloud cover in monsoon season | Medium | Multi-temporal acquisition windows; SAR integration |
| Hyperspectral data volume (storage/processing) | Medium | Dimensionality reduction; cloud computing |
| LiDAR point cloud density variations | Low-Medium | Adaptive sampling; point cloud completion networks |

### 4.2 Technical Constraints
| Constraint | Severity | Mitigation Strategy |
|------------|----------|---------------------|
| Spectral-LiDAR registration/alignment | Medium | Multi-sensor calibration protocols; learning-based registration |
| Model generalization across forest types | High | Domain adaptation; multi-site training |
| Real-time processing for DSS | Medium | Model optimization; edge deployment strategies |
| Canopy penetration limitations | Medium | Multi-return LiDAR; understory modeling |

### 4.3 Resource Constraints
| Constraint | Severity | Mitigation Strategy |
|------------|----------|---------------------|
| UAV flight regulations in forest areas | Medium | Coordination with forest department; DGCA compliance |
| GPU compute for training | Low-Medium | ISRO/institutional HPC access; cloud computing |
| Ground truth collection in difficult terrain | High | Strategic sampling; local community involvement |
| Timeline (typical PhD/project duration) | Medium | Phased implementation; modular architecture |

### 4.4 ISRO-Specific Dependencies
| Dependency | Description | Risk Level |
|------------|-------------|------------|
| HySIS data access | Archive data availability and processing levels | Low |
| AVIRIS-NG campaign data | Existing campaign coverage over Meghalaya | Medium |
| Future mission integration | Timeline alignment with upcoming hyperspectral/LiDAR satellites | Low |
| SAC/URSC technical support | Algorithm validation and operational deployment | Low |

---

## 5. Scope Boundaries

### In-Scope
- UAV-based hyperspectral and LiDAR data acquisition over select Meghalaya forest sites
- Deep learning model development for species classification
- Data fusion techniques (spectral + structural)
- GIS-based Decision Support System prototype
- Ground truth validation campaigns
- Framework documentation for replication

### Out-of-Scope
- Real-time operational deployment at state scale
- Integration with existing forest department IT infrastructure
- Policy recommendation development
- Economic valuation of forest resources
- Full automation without human validation

---

## 6. Success Criteria

| Criterion | Target Metric |
|-----------|---------------|
| Classification accuracy | ≥85% overall accuracy for target species |
| Species discrimination | ≥10 tree species reliably classified |
| Spatial resolution | Tree-level (individual crown) mapping |
| DSS functionality | Operational prototype with core modules |
| Validation | ≥200 ground truth points collected and validated |
| Replicability | Framework tested on ≥2 distinct forest sites |
| Publication output | ≥2 peer-reviewed publications in Q1 journals |

---

*Document Version: 1.0*  
*Phase: 1 - Idea Refinement*  
*Status: Complete*
