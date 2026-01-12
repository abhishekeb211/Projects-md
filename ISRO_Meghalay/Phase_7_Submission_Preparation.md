# PHASE 7: Submission Preparation

## 1. Venue Compliance Checklist

### Primary Venue: Remote Sensing of Environment (RSE)

| Requirement | Specification | Status | Action |
|-------------|---------------|--------|--------|
| **Manuscript Type** | Research Article | ✓ | N/A |
| **Word Limit** | No strict limit (typically 8000-12000) | ✓ | Current ~10000 words |
| **Abstract** | ≤300 words | ✓ | Current ~180 words |
| **Keywords** | 4-6 keywords | ✓ | 8 keywords - reduce to 6 |
| **Figures** | High resolution (300 dpi minimum) | ⚠ | Ensure all figures meet spec |
| **Tables** | Editable format (not images) | ✓ | All tables in LaTeX |
| **References** | Elsevier standard | ✓ | Using BibTeX |
| **Supplementary** | Allowed; separate files | ✓ | Plan: Dataset description, extended results |
| **Data Availability** | Required statement | ⚠ | Add data availability section |
| **Code Availability** | Encouraged | ⚠ | Prepare GitHub repository |
| **Author Contributions** | CRediT format required | ⚠ | Add CRediT statement |
| **Conflicts of Interest** | Required declaration | ⚠ | Add declaration |
| **Funding** | Required acknowledgment | ⚠ | Add ISRO RESPOND acknowledgment |

### Alternative Venue: IEEE TGRS

| Requirement | Specification | Status | Action |
|-------------|---------------|--------|--------|
| **Manuscript Type** | Regular Paper | ✓ | N/A |
| **Page Limit** | 12-15 pages (two-column) | ✓ | Current fits |
| **Abstract** | ≤250 words | ✓ | May need slight reduction |
| **Keywords** | ≤5 keywords | ⚠ | Reduce from 8 |
| **Format** | IEEE two-column | ✓ | Template ready |
| **Figures** | EPS/PDF preferred | ⚠ | Convert all figures |
| **References** | IEEE numbered | ✓ | Using IEEEtran |
| **Double-Blind** | No (single-blind) | ✓ | Author info included |
| **Supplementary** | IEEE DataPort encouraged | ⚠ | Prepare DataPort submission |
| **Graphical Abstract** | Not required | ✓ | N/A |

---

## 2. Format Checklist

### Document Structure

| Section | RSE Format | IEEE TGRS Format | Status |
|---------|------------|------------------|--------|
| Title | ≤20 words recommended | ≤12 words recommended | ⚠ Current 23 words - shorten |
| Abstract | Unstructured | Unstructured | ✓ |
| Introduction | Standard | Standard | ✓ |
| Related Work | May combine with Intro | Separate section | ✓ |
| Methods | Detailed | Detailed | ✓ |
| Results | Separate from Discussion | May combine | ✓ |
| Discussion | Detailed interpretation | May combine with Results | ✓ |
| Conclusion | Concise summary | Concise summary | ✓ |
| Acknowledgments | Before references | After conclusion | ✓ |
| References | Author-date (Elsevier) | Numbered (IEEE) | ⚠ Prepare both |

### Title Options (Shortened)

**Option 1 (18 words)**:
> "HyLiFormer: Transformer-based Deep Learning for Forest Species Classification from UAV Hyperspectral-LiDAR Fusion"

**Option 2 (15 words)**:
> "Deep Learning Framework for Forest Species Mapping using UAV Hyperspectral and LiDAR Data"

**Option 3 (12 words - IEEE preferred)**:
> "HyLiFormer: HSI-LiDAR Fusion for Tropical Forest Species Classification"

### Figure Checklist

| Figure | Description | Resolution | Format | Status |
|--------|-------------|------------|--------|--------|
| Fig. 1 | Study area map | 300 dpi | TIFF/PDF | ⚠ Create |
| Fig. 2 | HyLiFormer architecture | Vector | PDF | ⚠ Create |
| Fig. 3 | GSA detail diagram | Vector | PDF | ⚠ Create |
| Fig. 4 | Confusion matrix | 300 dpi | TIFF/PDF | ⚠ Pending results |
| Fig. 5 | Per-species F1 bar chart | Vector | PDF | ⚠ Pending results |
| Fig. 6 | Scaling curve | Vector | PDF | ⚠ Pending results |
| Fig. 7 | Attention visualization | 300 dpi | TIFF/PDF | ⚠ Pending results |
| Fig. 8 | DSS interface | 300 dpi | PNG/TIFF | ⚠ Pending development |

### Table Checklist

| Table | Description | Status |
|-------|-------------|--------|
| Table 1 | Sensor specifications | ⚠ Complete specs needed |
| Table 2 | Literature positioning matrix | ✓ Draft complete |
| Table 3 | Site characteristics | ⚠ Add coordinates, elevation |
| Table 4 | Species list with sample counts | ⚠ Pending field work |
| Table 5 | Architecture layer specifications | ✓ Draft complete |
| Table 6 | Main results comparison | ⚠ Pending experiments |
| Table 7 | Ablation results | ⚠ Pending experiments |
| Table 8 | Cross-site generalization | ⚠ Pending experiments |

---

## 3. Anonymity Compliance (If Double-Blind)

**Note**: RSE and IEEE TGRS are single-blind; anonymity not required.

For workshops/conferences requiring double-blind:

| Item | Check | Status |
|------|-------|--------|
| Author names removed | N/A | Single-blind |
| Affiliations removed | N/A | Single-blind |
| Self-citations anonymized | N/A | Single-blind |
| Acknowledgments removed | N/A | Single-blind |
| File metadata cleaned | ⚠ | Clean before submission |

---

## 4. Ethics Compliance

### Research Ethics

| Requirement | Status | Evidence |
|-------------|--------|----------|
| No human subjects | ✓ | Remote sensing data only |
| No animal subjects | ✓ | Remote sensing data only |
| Forest access permits | ⚠ | Required from Meghalaya Forest Dept |
| UAV flight permits | ⚠ | DGCA approval required |
| Protected area clearance | ⚠ | If sites include reserved forests |
| Community consent | ⚠ | For tribal land access |

### Data Ethics

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Data sovereignty | ✓ | All data collected within India; processed in India |
| ISRO data license | ⚠ | Formal request for HySIS/AVIRIS-NG |
| Open data commitment | ✓ | Dataset to be released |
| Privacy considerations | ✓ | No personal data collected |

### AI Ethics Statement (If Required)

> "This research uses deep learning for forest classification. The AI system was trained exclusively on remote sensing imagery and LiDAR data with human-verified ground truth labels. Model predictions are intended to assist, not replace, expert judgment in forest management decisions. The authors acknowledge potential biases in training data (canopy-dominant species emphasis) and recommend validation before operational deployment."

---

## 5. Artifact Plan

### 5.1 Code Repository

**Repository**: `github.com/[organization]/HyLiFormer`

**Structure**:
```
HyLiFormer/
├── README.md                 # Overview, installation, usage
├── LICENSE                   # Apache 2.0 or MIT
├── requirements.txt          # Python dependencies
├── setup.py                  # Package installation
├── configs/
│   ├── default.yaml         # Default hyperparameters
│   ├── meghalaya.yaml       # Dataset-specific config
│   └── satellite.yaml       # Satellite scaling config
├── data/
│   ├── download.py          # Dataset download scripts
│   └── preprocess.py        # Preprocessing utilities
├── models/
│   ├── spectral_encoder.py  # GSA implementation
│   ├── structural_encoder.py # HSE implementation
│   ├── fusion.py            # CMAF implementation
│   ├── hyliformer.py        # Full model
│   └── baselines/           # Baseline implementations
├── training/
│   ├── train.py             # Training script
│   ├── losses.py            # Focal loss, etc.
│   └── augmentation.py      # Data augmentation
├── evaluation/
│   ├── evaluate.py          # Evaluation script
│   ├── metrics.py           # OA, Kappa, F1
│   └── visualization.py     # Attention maps, confusion matrix
├── experiments/
│   ├── main_experiment.py   # Main classification
│   ├── ablation.py          # Ablation studies
│   └── scaling.py           # Satellite scaling
├── notebooks/
│   ├── demo.ipynb           # Usage demonstration
│   └── visualization.ipynb  # Result visualization
└── tests/
    └── test_model.py        # Unit tests
```

**README Outline**:
```markdown
# HyLiFormer

Transformer-based Deep Learning for Forest Species Classification from UAV Hyperspectral and LiDAR Data

## Overview
[Brief description]

## Installation
[pip/conda instructions]

## Quick Start
[5-line example]

## Dataset
[Link to MeghalayaForest-25 download]

## Training
[Training command]

## Evaluation
[Evaluation command]

## Pre-trained Models
[Link to model weights]

## Citation
[BibTeX]

## License
[Apache 2.0]

## Acknowledgments
[ISRO RESPOND, collaborators]
```

### 5.2 Dataset Release

**Repository**: Zenodo or IEEE DataPort

**Dataset Name**: MeghalayaForest-25

**Contents**:
```
MeghalayaForest-25/
├── README.md                 # Dataset documentation
├── LICENSE                   # CC-BY-4.0
├── data/
│   ├── site_A/
│   │   ├── hsi/             # Hyperspectral patches (HDF5)
│   │   ├── lidar/           # Point clouds (LAZ)
│   │   └── labels/          # Ground truth (CSV)
│   ├── site_B/
│   └── site_C/
├── splits/
│   ├── train.txt            # Training sample IDs
│   ├── val.txt              # Validation sample IDs
│   └── test.txt             # Test sample IDs
├── spectral_library/
│   └── species_signatures.csv # Mean spectra per species
├── metadata/
│   ├── species_list.csv     # 25 species with traits
│   ├── site_info.csv        # Site coordinates, elevation
│   └── sensor_specs.json    # Sensor specifications
└── benchmarks/
    └── baseline_results.csv # Baseline comparison results
```

**Data Availability Statement**:
> "The MeghalayaForest-25 dataset supporting this study is available at [DOI]. The dataset includes UAV hyperspectral patches, LiDAR point clouds, and ground-truth labels for 25 tree species across three forest sites in Meghalaya, India. Access requires acceptance of a data use agreement acknowledging ISRO RESPOND program support."

### 5.3 Pre-trained Models

**Release**: HuggingFace Hub or GitHub Releases

**Models**:
- `hyliformer-meghalaya-25.pth` - Full model trained on MeghalayaForest-25
- `hyliformer-spectral-only.pth` - Ablation: spectral encoder only
- `hyliformer-structural-only.pth` - Ablation: structural encoder only

---

## 6. Author Instructions (Placeholders to Fill)

### Experimental Results

| Placeholder | Section | Responsible | Due Date |
|-------------|---------|-------------|----------|
| `\result{main_oa}` | Abstract, Sec 6.1 | Author 1 | Before submission |
| `\result{main_gain}` | Abstract, Sec 6.1 | Author 1 | Before submission |
| `\result{main_kappa}` | Sec 6.1 | Author 1 | Before submission |
| `\result{spectralformer_oa}` | Sec 6.1 | Author 1 | Before submission |
| `\result{cmaf_gain}` | Sec 6.1, 6.3 | Author 1 | Before submission |
| `\result{ablation_*}` | Sec 6.3 | Author 1 | Before submission |
| `\result{cross_site_*}` | Sec 6.4 | Author 2 | Before submission |
| `\result{scale_*}` | Sec 6.5 | Author 1 | Before submission |
| `\result{dss_*}` | Sec 8.4 | Author 3 | Before submission |

### Figures to Create

| Figure | Responsible | Tools | Due Date |
|--------|-------------|-------|----------|
| Fig. 1 (Study area) | Author 2 | QGIS, Inkscape | Week 1 |
| Fig. 2 (Architecture) | Author 1 | draw.io, Inkscape | Week 1 |
| Fig. 3 (GSA detail) | Author 1 | draw.io, Inkscape | Week 1 |
| Fig. 4-7 (Results) | Author 1 | Python/Matplotlib | After experiments |
| Fig. 8 (DSS) | Author 3 | Screenshot + annotation | After DSS complete |

### Tables to Complete

| Table | Responsible | Data Source | Due Date |
|-------|-------------|-------------|----------|
| Table 1 (Sensors) | Author 2 | Sensor datasheets | Week 1 |
| Table 3 (Sites) | Author 2 | Field notes | Week 1 |
| Table 4 (Species) | Author 2 | Field database | After field work |
| Tables 6-8 (Results) | Author 1 | Experiments | After experiments |

### Writing Tasks

| Section | Responsible | Status | Due Date |
|---------|-------------|--------|----------|
| Abstract | All | Draft complete | Final review |
| Introduction | Author 1 | Draft complete | Revision needed |
| Related Work | Author 1 | Draft complete | Add recent citations |
| Study Area | Author 2 | Draft complete | Add coordinates |
| Methods | Author 1 | Draft complete | Final review |
| Results | Author 1 | Template ready | After experiments |
| Discussion | Author 1 | Template ready | After experiments |
| DSS Section | Author 3 | Draft pending | After development |
| Conclusion | All | Template ready | After results |

---

## 7. Final Polishing Checklist

### Title & Abstract

- [ ] Title ≤20 words (RSE) or ≤12 words (IEEE)
- [ ] Title includes key terms: deep learning, hyperspectral, LiDAR, forest, species
- [ ] Abstract ≤300 words (RSE) or ≤250 words (IEEE)
- [ ] Abstract includes: motivation, gap, method, results, significance
- [ ] No citations in abstract
- [ ] No undefined acronyms in abstract

### Contributions

- [ ] Contributions clearly numbered (5 items)
- [ ] Each contribution is specific and verifiable
- [ ] Contributions match abstract claims
- [ ] No overclaiming (use "we demonstrate" not "we prove")

### Figures

- [ ] All figures cited in text in order
- [ ] Figure captions are self-contained
- [ ] Color figures readable in grayscale
- [ ] Font size ≥8pt in all figures
- [ ] No stretched/distorted images
- [ ] Consistent style across figures

### Tables

- [ ] All tables cited in text in order
- [ ] Table captions above tables
- [ ] No vertical lines (modern style)
- [ ] Consistent decimal places
- [ ] Units clearly specified
- [ ] Bold for best results

### References

- [ ] All citations have complete information
- [ ] Consistent citation format
- [ ] Recent works included (2023-2024)
- [ ] Seminal works cited
- [ ] ISRO publications included
- [ ] Self-citations ≤15% of total

### Language & Style

- [ ] American English spelling (RSE) or British (as appropriate)
- [ ] Consistent terminology throughout
- [ ] No contractions (don't → do not)
- [ ] Active voice preferred
- [ ] Past tense for methods/results
- [ ] Present tense for general truths
- [ ] No first person plural overuse ("we" sparingly)

### Technical Correctness

- [ ] All equations numbered and referenced
- [ ] Variables defined before use
- [ ] Units consistent (SI preferred)
- [ ] Statistical tests appropriate
- [ ] P-values correctly reported
- [ ] Confidence intervals included

---

## 8. ISRO Proposal Checklist (Format B)

### Format B Completeness

| Section | Status | Notes |
|---------|--------|-------|
| B-1: Title | ✓ | Complete |
| B-2: Summary | ✓ | 178 words |
| B-3: Objectives | ✓ | 4 categories |
| B-4: State of Art | ✓ | Includes ISRO relevance |
| B-5: Approach | ✓ | 5 phases |
| B-6: Data Reduction | ✓ | Volumes and products |
| B-7: Facilities | ⚠ | Need institute confirmation |
| B-8: Time Schedule | ✓ | 24 months |
| B-9: Expected Outcomes | ✓ | 4 categories |
| B-10: Budget | ⚠ | Need detailed breakdown |

### Payload TRL Evidence

| Component | TRL Claim | Evidence Required |
|-----------|-----------|-------------------|
| HSI Processing | TRL 5 | Cite AVIRIS-NG processing papers |
| LiDAR Processing | TRL 5 | Cite operational forestry studies |
| Deep Learning | TRL 4 | Cite similar RS-DL deployments |
| DSS Platform | TRL 4 | Cite web-GIS deployments |

### Institute Facility List

| Facility | Institute | Availability |
|----------|-----------|--------------|
| GPU Cluster | IIT Guwahati | Confirmed |
| GIS Lab | IIT Guwahati | Confirmed |
| Field Equipment | BSI Eastern Circle | MoU required |
| UAV Platform | External rental | Budget allocated |
| HPC Access | ISRO/SAC | Request submitted |

---

## 9. Pre-Submission Final Review

### Day Before Submission

- [ ] PDF generated and reviewed
- [ ] All placeholders filled
- [ ] All figures render correctly
- [ ] All tables readable
- [ ] Page count within limits
- [ ] File size acceptable
- [ ] Co-author approval obtained
- [ ] Cover letter prepared
- [ ] Suggested reviewers listed (if required)
- [ ] Excluded reviewers listed (if needed)
- [ ] Conflict of interest declared
- [ ] Funding acknowledged
- [ ] Data availability statement included
- [ ] Code availability statement included
- [ ] CRediT author contributions included

### Submission Day

- [ ] Account created on submission system
- [ ] Manuscript files uploaded
- [ ] Supplementary files uploaded
- [ ] Metadata entered correctly
- [ ] Keywords selected
- [ ] Subject area selected
- [ ] Cover letter attached
- [ ] Reviewers suggested
- [ ] Final review before "Submit"
- [ ] Submission confirmation received
- [ ] Confirmation email archived

---

## 10. Post-Submission Tasks

### Immediate (Week 1)

- [ ] Share submission confirmation with co-authors
- [ ] Archive submitted version
- [ ] Update project tracking
- [ ] Prepare for potential desk rejection response

### During Review (Weeks 2-12)

- [ ] Continue experiments for revision preparation
- [ ] Prepare additional analyses for reviewer requests
- [ ] Monitor for reviewer assignment notification
- [ ] Prepare presentation for potential acceptance

### If Major Revision

- [ ] Create response document template
- [ ] Address each reviewer comment systematically
- [ ] Highlight changes in revised manuscript
- [ ] Re-run experiments if methodology concerns
- [ ] Resubmit within deadline

### If Accepted

- [ ] Complete proof corrections promptly
- [ ] Prepare press release / research highlight
- [ ] Update project website
- [ ] Archive final published version
- [ ] Submit to institutional repository

---

## Phase Status
**PHASE 7: SUBMISSION PREPARATION COMPLETE** ✓

---

## RESEARCH PIPELINE COMPLETE

### Summary of Deliverables

| Phase | Deliverable | Status |
|-------|-------------|--------|
| Phase 0 | Research Ledger Setup | ✓ |
| Phase 1 | Idea Refinement | ✓ |
| Phase 1.5 | Locked Decisions | ✓ |
| Phase 2a | SLR Protocol | ✓ |
| Phase 2b | Literature Cards | ✓ |
| Phase 2c | Synthesis & Gap Confirmation | ✓ |
| Phase 3 | Technical Deep Dive | ✓ |
| Phase 4 | Section-by-Section Drafts | ✓ |
| Phase 5 | Manuscript Generation | ✓ |
| Phase 6 | Rigor & Reviewer Simulation | ✓ |
| Phase 7 | Submission Preparation | ✓ |

### ISRO Format B Sections

| Section | Status |
|---------|--------|
| B-1: Title | ✓ |
| B-2: Summary | ✓ |
| B-3: Objectives | ✓ |
| B-4: State of Art | ✓ |
| B-5: Approach | ✓ |
| B-6: Data Reduction | ✓ |
| B-7: Facilities | Draft |
| B-8: Timeline | ✓ |
| B-9: Outcomes | ✓ |
| B-10: Budget | Draft |

### Next Steps

1. **Execute experiments** to fill result placeholders
2. **Create figures** (architecture diagrams, maps)
3. **Complete field work** for ground-truth collection
4. **Develop DSS** for operational validation
5. **Request ISRO data** (HySIS, AVIRIS-NG)
6. **Submit manuscript** to target venue
7. **Submit ISRO RESPOND** proposal

---

*Document generated by Research Agent Pipeline*
*Project: ISRO-MEGHALAYA-HSI-LIDAR-2026*
*Date: January 12, 2026*
