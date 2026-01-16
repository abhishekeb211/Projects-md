# Phase 7: Submission Preparation

## Research Agent Prompt

**PHASE 7: Submission Preparation**

Create venue compliance checklist, artifact plan, author instructions for placeholders, and final polishing checklist.

---

## 1) Venue Compliance Checklist

### Primary Target: IEEE Transactions on Geoscience and Remote Sensing (TGRS)

#### Format Requirements

| Requirement | Specification | Status | Notes |
|-------------|---------------|--------|-------|
| **Template** | IEEE Transactions format | ✅ Using IEEEtran.cls | Verify latest version |
| **Paper type** | Regular paper (full length) | ✅ | 12-14 pages typical |
| **Columns** | Two-column format | ✅ | IEEEtran default |
| **Font** | Times New Roman, 10pt | ✅ | IEEEtran default |
| **Margins** | IEEE standard | ✅ | Template handles |
| **Page numbers** | Include for review | 🔲 | Add for submission |
| **Line numbers** | Optional but recommended | 🔲 | Add lineno package |

#### Content Requirements

| Requirement | Specification | Status | Action Needed |
|-------------|---------------|--------|---------------|
| **Title** | <100 characters recommended | ✅ | Current: 96 chars |
| **Abstract** | 150-250 words | 🔲 | Verify word count |
| **Keywords** | 4-8 keywords | ✅ | 7 keywords provided |
| **Sections** | Standard structure | ✅ | All required sections |
| **References** | IEEE format | ✅ | Using IEEEtran.bst |
| **Figures** | High resolution (300+ dpi) | 🔲 | Generate final figures |
| **Tables** | Clear, properly formatted | 🔲 | Review all tables |
| **Equations** | Numbered, properly formatted | ✅ | Using amsmath |

#### Anonymity (If Double-Blind Review)

| Requirement | Status | Action Needed |
|-------------|--------|---------------|
| Remove author names | 🔲 | Use \author{} placeholder |
| Remove affiliations | 🔲 | Comment out \thanks{} |
| Remove self-citations | 🔲 | Review and anonymize |
| Remove acknowledgments | 🔲 | Comment out section |
| Remove identifying URLs | 🔲 | Check all links |
| Anonymize dataset name | 🔲 | Use "Dataset A" if needed |

**Note:** TGRS uses single-blind review (authors visible to reviewers).

#### Ethics & Data Requirements

| Requirement | Status | Action Needed |
|-------------|--------|---------------|
| Ethics statement | 🔲 | Add if required by venue |
| Data availability | 🔲 | State dataset release plan |
| Code availability | 🔲 | State code release plan |
| Conflict of interest | 🔲 | Declare any conflicts |
| Funding acknowledgment | 🔲 | Add funding sources |

#### Page Limits

| Content Type | Limit | Current | Status |
|--------------|-------|---------|--------|
| Main text | ~12-14 pages | TBD | 🔲 Verify |
| Figures | Included in page count | 8-10 | 🔲 Verify |
| Tables | Included in page count | 10-11 | 🔲 Verify |
| References | Not counted | 30-50 | 🔲 Verify |
| Supplementary | Unlimited | Optional | 🔲 Consider |

### Alternative Venue Checklist: ISPRS Journal

| Requirement | ISPRS | Action |
|-------------|-------|--------|
| Format | Elsevier template | Different template needed |
| Page limit | No strict limit | More flexible |
| Open access | Optional | Budget consideration |
| Data policy | Data availability encouraged | Plan dataset release |

---

## 2) Artifact Plan

### Code Repository Structure

```
HyperForest/
├── README.md                    # Project overview, installation, usage
├── LICENSE                      # MIT or Apache 2.0
├── requirements.txt             # Python dependencies
├── environment.yml              # Conda environment
│
├── configs/
│   ├── default.yaml             # Default hyperparameters
│   ├── train_config.yaml        # Training configuration
│   └── inference_config.yaml    # Inference configuration
│
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── hsi_encoder.py       # HSI encoder module
│   │   ├── lidar_encoder.py     # LiDAR encoder module
│   │   ├── fusion_module.py     # Cross-Modal Fusion Module
│   │   ├── prediction_head.py   # Classification/regression heads
│   │   └── hyperforest.py       # Full model assembly
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── dataset.py           # PyTorch dataset class
│   │   ├── preprocessing.py     # HSI/LiDAR preprocessing
│   │   └── augmentation.py      # Data augmentation
│   │
│   ├── training/
│   │   ├── __init__.py
│   │   ├── trainer.py           # Training loop
│   │   ├── losses.py            # Loss functions
│   │   └── metrics.py           # Evaluation metrics
│   │
│   └── utils/
│       ├── __init__.py
│       ├── io_utils.py          # File I/O utilities
│       ├── visualization.py     # Plotting functions
│       └── geo_utils.py         # Geospatial utilities
│
├── scripts/
│   ├── train.py                 # Training script
│   ├── evaluate.py              # Evaluation script
│   ├── inference.py             # Inference script
│   └── preprocess_data.py       # Data preprocessing script
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_training_demo.ipynb
│   └── 03_visualization.ipynb
│
├── tests/
│   ├── test_models.py
│   ├── test_data.py
│   └── test_training.py
│
└── docs/
    ├── installation.md
    ├── data_format.md
    └── api_reference.md
```

### README Outline

```markdown
# HyperForest: Deep Learning for Forest Species Classification

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

## Overview
HyperForest is a hybrid deep learning framework for tree species identification 
using UAV-based hyperspectral and LiDAR data fusion.

## Features
- Novel Cross-Modal Fusion Module (CMFM)
- Support for hyperspectral and LiDAR data
- Multi-task learning (classification + structural estimation)
- Pretrained models for Meghalaya forest species

## Installation
```bash
git clone https://github.com/[username]/HyperForest.git
cd HyperForest
pip install -r requirements.txt
```

## Quick Start
[Training, inference examples]

## Data Format
[Expected input formats]

## Citation
[BibTeX entry]

## License
MIT License

## Acknowledgments
[Funding, ISRO, collaborators]
```

### Data Release Plan

| Component | Format | Size (Est.) | Access | License |
|-----------|--------|-------------|--------|---------|
| HSI imagery | GeoTIFF | ~5-10 GB | Zenodo/ISRO | CC-BY-4.0 |
| LiDAR points | LAS/LAZ | ~2-5 GB | Zenodo/ISRO | CC-BY-4.0 |
| Ground truth | GeoJSON/CSV | ~10 MB | GitHub | CC-BY-4.0 |
| Train/test splits | CSV | ~1 MB | GitHub | CC-BY-4.0 |
| Pretrained models | PyTorch .pt | ~500 MB | GitHub/Zenodo | MIT |

### Reproducibility Steps

```markdown
## Reproducing Paper Results

### 1. Environment Setup
```bash
conda env create -f environment.yml
conda activate hyperforest
```

### 2. Data Preparation
```bash
# Download data from Zenodo
wget https://zenodo.org/record/[ID]/files/meghalaya_dataset.zip
unzip meghalaya_dataset.zip -d data/

# Preprocess
python scripts/preprocess_data.py --config configs/default.yaml
```

### 3. Training
```bash
# Train from scratch
python scripts/train.py --config configs/train_config.yaml

# Or use pretrained weights
wget https://github.com/[repo]/releases/download/v1.0/hyperforest_pretrained.pt
```

### 4. Evaluation
```bash
python scripts/evaluate.py --checkpoint checkpoints/best_model.pt \
                           --config configs/default.yaml
```

### 5. Expected Results
| Metric | Expected Value | Tolerance |
|--------|---------------|-----------|
| OA | [X]% | ±1% |
| Kappa | [Y] | ±0.02 |
```

---

## 3) Author Instructions: Placeholder Resolution

### Placeholder Inventory and Resolution Guide

#### Results Placeholders (Experimental)

| Placeholder | Location | How to Fill | Priority |
|-------------|----------|-------------|----------|
| `\result{OA}{TBD}` | Abstract, Results | Run evaluation on test set | Critical |
| `\result{margin}{TBD}` | Abstract | Compute best_baseline - HyperForest | Critical |
| `\result{RF_OA}{TBD}` | Table 7 | Run Random Forest baseline | High |
| `\result{SVM_OA}{TBD}` | Table 7 | Run SVM baseline | High |
| `\result{3DCNN_OA}{TBD}` | Table 7 | Run 3D-CNN baseline | High |
| `\result{HSN_OA}{TBD}` | Table 7 | Run HybridSN baseline | High |
| `\result{SF_OA}{TBD}` | Table 7 | Run SpectralFormer baseline | High |
| `\result{PN_OA}{TBD}` | Table 7 | Run PointNet++ baseline | High |
| `\result{LF_OA}{TBD}` | Table 7 | Run Late Fusion baseline | High |
| `\result{HF_OA}{TBD}` | Table 7 | Run HyperForest evaluation | Critical |
| `\result{h_rmse}{TBD}` | Table 10 | Compute height RMSE | High |
| `\result{d_rmse}{TBD}` | Table 10 | Compute crown diameter RMSE | High |

#### Dataset Placeholders

| Placeholder | Location | How to Fill | Source |
|-------------|----------|-------------|--------|
| `\placeholder{X}` (species count) | Multiple | Count unique species in ground truth | Field data |
| `\placeholder{Y}` (site count) | Experiments | Count collection sites | Field data |
| `\placeholder{N}` (total samples) | Table 4 | Count total patches | Data processing |
| `\placeholder{N_train}` | Table 4 | 60% of N | Data split |
| `\placeholder{N_val}` | Table 4 | 20% of N | Data split |
| `\placeholder{N_test}` | Table 4 | 20% of N | Data split |
| `\placeholder{B}` (bands) | Table 4 | Count spectral bands | Sensor specs |

#### Configuration Placeholders

| Placeholder | Location | How to Fill | Source |
|-------------|----------|-------------|--------|
| `\placeholder{lr}` | Table 6 | Final learning rate | Hyperparameter search |
| `\placeholder{bs}` | Table 6 | Batch size used | Training config |
| `\placeholder{epochs}` | Table 6 | Training epochs | Training log |
| `\placeholder{GPU model}` | Table 6 | GPU used | Hardware |
| `\placeholder{lambda}` | Table 6 | Structural loss weight | Config file |

#### Text Placeholders

| Placeholder | Location | How to Fill | Source |
|-------------|----------|-------------|--------|
| `\placeholder{First Author}` | Title page | Author name | - |
| `\placeholder{Affiliation}` | Title page | Institution | - |
| `\placeholder{email}` | Title page | Corresponding email | - |
| `\placeholder{UAV specifications}` | Sec 5.2 | Platform model, specs | Equipment |
| `\placeholder{Sensor specifications}` | Sec 5.2 | HSI/LiDAR specs | Equipment |

#### Citation Placeholders

| Placeholder | Recommended Reference |
|-------------|----------------------|
| `placeholder_fao` | FAO (2020). Global Forest Resources Assessment |
| `placeholder_ipcc` | IPCC (2019). Climate Change and Land |
| `placeholder_hybridsn` | Roy et al. (2019). HybridSN. IEEE GRSL |
| `placeholder_spectralformer` | Hong et al. (2022). SpectralFormer. IEEE TGRS |
| `placeholder_pointnet` | Qi et al. (2017). PointNet. CVPR |
| `placeholder_pointnetpp` | Qi et al. (2017). PointNet++. NeurIPS |

### Placeholder Resolution Checklist

| Category | Total | Resolved | Remaining |
|----------|-------|----------|-----------|
| Results | 40+ | 0 | 40+ |
| Dataset | 8 | 0 | 8 |
| Config | 5 | 0 | 5 |
| Author info | 5 | 0 | 5 |
| Citations | 30+ | 0 | 30+ |
| **TOTAL** | ~90 | 0 | ~90 |

---

## 4) Final Polishing Checklist

### Title Polish

| Check | Status | Notes |
|-------|--------|-------|
| ≤100 characters | ✅ | 96 characters |
| Contains keywords | ✅ | deep learning, hyperspectral, LiDAR, forest |
| Specific and informative | ✅ | Names method, application, location |
| No abbreviations | ✅ | Except UAV (widely known) |
| Engaging | 🔲 | Consider alternative framings |

### Abstract Polish

| Check | Status | Notes |
|-------|--------|-------|
| 150-250 words | 🔲 | Verify count |
| States problem | ✅ | |
| States approach | ✅ | |
| States key result | 🔲 | Needs numeric results |
| States contribution | ✅ | |
| Self-contained | ✅ | |
| No citations | ✅ | |
| No undefined acronyms | ✅ | Define HSI, LiDAR first use |

### Contributions Polish

| Check | Status | Notes |
|-------|--------|-------|
| 3-5 contributions | ✅ | 5 contributions |
| Specific and verifiable | 🔲 | Add specific numbers |
| Novel claim clear | 🔲 | Clarify "first" claims |
| Ordered by importance | ✅ | Architecture first |
| Evidence referenced | 🔲 | Link to sections/tables |

### Figures Polish

| Figure | High-Res | Caption | Labels | Referenced | Status |
|--------|----------|---------|--------|------------|--------|
| Fig. 1 (Overview) | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Fig. 2 (Data examples) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 3 (Architecture) | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Fig. 4 (CMFM detail) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 5 (Study area) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 6 (Confusion matrix) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 7 (Per-class F1) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 8 (Classification maps) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Fig. 9 (Scatter plots) | 🔲 | 🔲 | 🔲 | 🔲 | Pending |

### Tables Polish

| Table | Headers Clear | Alignment | Spacing | Caption | Referenced | Status |
|-------|---------------|-----------|---------|---------|------------|--------|
| Table 1 (Fusion strategies) | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Table 2 (Related work) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Table 3 (Architecture params) | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Table 4 (Dataset stats) | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Table 5 (UAV sensors) | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Table 6 (Training config) | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | Pending |
| Table 7 (Main results) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Table 8 (Fusion comparison) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Table 9 (Ablation) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Table 10 (Structural) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |
| Table 11 (Efficiency) | 🔲 | 🔲 | 🔲 | 🔲 | ✅ | Pending |

### Language Polish

| Check | Status |
|-------|--------|
| Spell check complete | 🔲 |
| Grammar check complete | 🔲 |
| Consistent terminology | 🔲 |
| Acronyms defined at first use | 🔲 |
| Passive voice minimized | 🔲 |
| Avoid "very", "really", etc. | 🔲 |
| Specific numbers over vague claims | 🔲 |
| Active voice for contributions | 🔲 |

### Final Submission Checklist

| Item | Status | Deadline |
|------|--------|----------|
| Main manuscript PDF | 🔲 | T-7 days |
| Supplementary materials | 🔲 | T-7 days |
| Cover letter | 🔲 | T-3 days |
| Reviewer suggestions | 🔲 | T-3 days |
| Conflict declarations | 🔲 | T-3 days |
| Data availability statement | 🔲 | T-3 days |
| Code availability statement | 🔲 | T-3 days |
| Author contributions | 🔲 | T-3 days |
| Final proofread | 🔲 | T-1 day |
| Submit | 🔲 | Deadline |

---

## Submission Readiness Assessment

| Component | Ready | Blocking Issues |
|-----------|-------|-----------------|
| Title | ✅ | None |
| Abstract | 🔲 | Needs results |
| Introduction | ✅ | None |
| Background | ✅ | None |
| Related Work | 🔲 | Needs complete citations |
| Methodology | ✅ | None |
| Experiments | 🔲 | Needs data details |
| Results | 🔲 | Needs experimental results |
| Discussion | 🔲 | Needs results interpretation |
| Conclusion | 🔲 | Needs results summary |
| Figures | 🔲 | All pending |
| Tables | 🔲 | Most pending data |
| References | 🔲 | ~50% complete |

### Estimated Time to Submission-Ready

| Task | Effort |
|------|--------|
| Run all experiments | 2 weeks |
| Fill all placeholders | 1 week |
| Generate figures | 3 days |
| Final writing polish | 3 days |
| Internal review | 3 days |
| **TOTAL** | ~4 weeks |

---

## Status

**⏹️ STOP.**

Phase 7 complete. All submission preparation materials documented.

---

## Summary: Complete Research Agent Workflow

| Phase | Document | Status |
|-------|----------|--------|
| Phase 0 | Phase_0_Initialize.md | ✅ Complete |
| Phase 1 | Phase_1_Idea_Refinement.md | ✅ Complete |
| Phase 1.5 | Phase_1.5_Lock_Decisions.md | ✅ Complete |
| Phase 2a | Phase_2a_SLR_Protocol.md | ✅ Complete |
| Phase 2b | Phase_2b_Literature_Cards.md | ✅ Complete |
| Phase 2c | Phase_2c_Synthesis_Gap_Confirmation.md | ✅ Complete |
| Phase 3 | Phase_3_Technical_Deep_Dive.md | ✅ Complete |
| Phase 4 | Phase_4_Section_Drafts.md | ✅ Complete |
| Phase 5 | Phase_5_Manuscript_Generation.md | ✅ Complete |
| Phase 6 | Phase_6_Rigor_Review_Simulation.md | ✅ Complete |
| Phase 7 | Phase_7_Submission_Preparation.md | ✅ Complete |

**All phases complete. Ready for execution with real data and experiments.**
