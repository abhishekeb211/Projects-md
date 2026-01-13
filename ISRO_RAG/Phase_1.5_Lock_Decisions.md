# Phase 1.5: Lock Decisions Before Literature Review

## Research Agent Prompt

Before Phase 2 (Systematic Literature Review), list the minimum author decisions needed to avoid wasted SLR work.

Give options with pros/cons for each decision (e.g., scope boundaries, target baselines, evaluation setting, datasets).

---

## Critical Decisions Required

The following decisions must be locked before proceeding with the Systematic Literature Review to ensure focused, efficient literature collection.

---

## Decision 1: Scope Boundaries - Sensor Modality Focus

### Question
Should the literature review focus exclusively on UAV-based sensors, or include satellite-based hyperspectral/LiDAR systems?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: UAV-Only** | Focus exclusively on UAV-based HSI and LiDAR | Directly relevant; manageable scope; operational focus | Misses satellite fusion techniques; limits ISRO integration insights |
| **B: UAV + Satellite** | Include both UAV and satellite-based approaches | Comprehensive; supports ISRO satellite integration; multi-scale perspective | Larger literature scope; may dilute UAV-specific insights |
| **C: Multi-Platform Emphasis** | UAV primary with satellite as secondary context | Balanced approach; addresses ISRO requirements | Requires careful prioritization |

### Recommendation
**Option C: Multi-Platform Emphasis** - UAV-based methods as primary focus, with satellite-based approaches included where they inform fusion strategies or ISRO integration.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 2: Geographic Scope - Forest Types

### Question
Should the methodology target only Meghalaya's specific forest types, or aim for generalizability across tropical/subtropical forests?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Meghalaya-Specific** | Focus exclusively on Meghalaya forest types (tropical wet evergreen, subtropical pine, bamboo) | Deep domain expertise; precise species selection; manageable ground truth | Limited generalizability claims; niche contribution |
| **B: Tropical Forest General** | Design for broad tropical forest applicability | Higher impact; wider applicability; stronger contribution | Requires diverse validation; may oversimplify regional complexity |
| **C: Meghalaya Primary + Transferability** | Develop for Meghalaya with explicit transferability analysis | Best of both; demonstrates generalization potential | Requires additional experiments; higher effort |

### Recommendation
**Option C: Meghalaya Primary + Transferability** - Primary validation in Meghalaya with transferability experiments to other forest types (if data available) or explicit analysis of generalization potential.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 3: Target Species Set

### Question
How many and which tree species should be included in the classification study?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Limited (5-10 species)** | Focus on dominant/flagship species only | Feasible ground truth; clearer results | May miss biodiversity complexity; limited practical utility |
| **B: Moderate (15-25 species)** | Include major species across forest types | Balanced complexity; realistic operational scenario | Requires significant ground truth effort |
| **C: Comprehensive (30+ species)** | Include all identifiable species | Maximum biodiversity coverage; high ecological value | Challenging ground truth; class imbalance issues; higher noise |

### Candidate Species Categories

| Forest Type | Example Species | Priority |
|-------------|-----------------|----------|
| Tropical Wet Evergreen | *Mesua ferrea*, *Castanopsis*, *Schima wallichii* | High |
| Subtropical Pine | *Pinus kesiya* | High |
| Mixed Deciduous | *Shorea robusta*, *Terminalia* spp. | Medium |
| Bamboo | *Dendrocalamus*, *Bambusa* spp. | Medium |
| Jhum Fallows | Secondary succession species | Low |

### Recommendation
**Option B: Moderate (15-25 species)** - Focus on 15-25 ecologically and commercially significant species across Meghalaya's major forest types.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 4: Deep Learning Architecture Scope

### Question
Should the study propose a novel architecture or adapt/ensemble existing architectures?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Novel Architecture** | Design new spectral-structural fusion network | Highest contribution; publication appeal | Risk of underperformance; high development effort |
| **B: Architecture Adaptation** | Adapt proven architectures (ResNet, ViT, PointNet++) | Lower risk; faster implementation; strong baselines | Lower novelty claims |
| **C: Hybrid Approach** | Novel fusion strategy with adapted backbone components | Balanced novelty and reliability; focused contribution | Requires clear delineation of contributions |

### Recommendation
**Option C: Hybrid Approach** - Novel multi-modal fusion mechanism with proven backbone architectures (e.g., 3D-CNN for HSI, PointNet++ for LiDAR).

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 5: Evaluation Baselines

### Question
Which baseline categories should be included for comprehensive comparison?

### Options

| Category | Must Include | Nice to Have |
|----------|--------------|--------------|
| **Traditional ML** | RF, SVM with handcrafted features | Gradient Boosting, MLP |
| **CNN-based HSI** | 3D-CNN, HybridSN | 2D-CNN, spectral attention networks |
| **Transformer-based HSI** | SpectralFormer or equivalent | Vision Transformer adaptations |
| **LiDAR-specific** | PointNet++ for forest structure | Random Forest on LiDAR metrics |
| **Existing Fusion** | At least 2 published HSI-LiDAR methods | Multi-modal transformers |
| **Commercial/Standard** | ENVI classification tools | eCognition, Google Earth Engine |

### Recommendation
Include **minimum 6-8 baselines** spanning all major categories to ensure comprehensive evaluation.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 6: Evaluation Metrics Selection

### Question
Which metrics should be prioritized for evaluation?

### Options

| Metric Category | Recommended Metrics | Justification |
|-----------------|---------------------|---------------|
| **Classification** | OA, AA, Kappa, F1-macro, per-class F1 | Standard in remote sensing literature |
| **Structural** | RMSE, MAE, R² for height/diameter | Quantitative accuracy for parameters |
| **Efficiency** | Training time, inference time, model size | Operational deployment relevance |
| **Statistical** | McNemar's test, confidence intervals | Rigor for method comparison |

### Recommendation
All categories should be included for a comprehensive Empirical/Systems paper.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 7: Data Collection Strategy

### Question
What is the data collection and ground truth strategy?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: New UAV Collection Only** | Collect all data fresh for this study | Full control; optimized protocols | Time/cost intensive; weather dependency |
| **B: Existing + New Data** | Leverage existing datasets + targeted new collection | Faster; builds on prior work | May have protocol inconsistencies |
| **C: Simulated + Limited Real** | Heavy simulation with limited real validation | Fastest; lower cost | Reduced real-world credibility |

### Recommendation
**Option B: Existing + New Data** - Leverage any existing UAV/satellite data from ISRO or partners, supplemented with targeted new collection in key sites.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision 8: DSS Scope and Integration

### Question
How comprehensive should the Decision Support System (DSS) be?

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Minimal DSS** | Classification outputs + basic visualization | Faster development; focused on DL contribution | Weaker systems contribution |
| **B: Operational DSS** | Full pipeline: data ingestion → processing → visualization → reporting | Strong systems contribution; operational value | Significant development effort |
| **C: Framework + Prototype** | DSS architecture design with working prototype | Balanced; demonstrates feasibility | May seem incomplete |

### Recommendation
**Option C: Framework + Prototype** - Comprehensive DSS architecture with functional prototype demonstrating key capabilities.

### Decision Status: 🔴 AWAITING LOCK

---

## Decision Summary Table

| ID | Decision Area | Recommended Option | Priority |
|----|---------------|-------------------|----------|
| D1 | Sensor Modality Scope | C: Multi-Platform Emphasis | Critical |
| D2 | Geographic Scope | C: Meghalaya + Transferability | Critical |
| D3 | Target Species Set | B: Moderate (15-25) | High |
| D4 | Architecture Scope | C: Hybrid Approach | Critical |
| D5 | Evaluation Baselines | 6-8 spanning all categories | High |
| D6 | Evaluation Metrics | All categories | Medium |
| D7 | Data Collection | B: Existing + New | High |
| D8 | DSS Scope | C: Framework + Prototype | Medium |

---

## Lock Confirmation Template

Before proceeding to Phase 2, confirm each decision:

```markdown
## Decision Lock Confirmation

| ID | Decision | Locked Choice | Confirmed |
|----|----------|---------------|-----------|
| D1 | Sensor Scope | [ ] | ☐ |
| D2 | Geographic Scope | [ ] | ☐ |
| D3 | Species Set | [ ] | ☐ |
| D4 | Architecture | [ ] | ☐ |
| D5 | Baselines | [ ] | ☐ |
| D6 | Metrics | [ ] | ☐ |
| D7 | Data Strategy | [ ] | ☐ |
| D8 | DSS Scope | [ ] | ☐ |

Locked by: [Author Name]
Date: [Date]
```

---

## Status

**⏸️ WAITING FOR AUTHOR DECISIONS**

Phase 2 (Systematic Literature Review) will begin only after all critical decisions (D1, D2, D4) are locked.

---

## Next Step

After locking decisions, proceed to **Phase 2a: SLR Protocol** to define the systematic literature review methodology.
