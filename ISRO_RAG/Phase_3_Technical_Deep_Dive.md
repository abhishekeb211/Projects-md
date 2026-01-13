# Phase 3: Technical Deep Dive

## Research Agent Prompt

**PHASE 3: Technical Deep Dive**

Based on Master Document v1, define formal terms, specify architecture, provide algorithms, design evaluation, and expand threat model.

---

## 1) Formal Terms, Constructs, and Notation

### 1.1 Data Representations

#### Hyperspectral Image (HSI)

$$\mathbf{X}_{HSI} \in \mathbb{R}^{H \times W \times B}$$

Where:
- $H$ = Image height (pixels)
- $W$ = Image width (pixels)  
- $B$ = Number of spectral bands (typically 100-400)

**Spectral Signature:** For pixel $(i,j)$:
$$\mathbf{s}_{i,j} = [x_{i,j,1}, x_{i,j,2}, ..., x_{i,j,B}]^T \in \mathbb{R}^B$$

**Patch Extraction:** For classification, extract spatial patches:
$$\mathbf{P}_{i,j} \in \mathbb{R}^{p \times p \times B}$$

Where $p$ is the patch size (typically 7-25 pixels).

#### LiDAR Point Cloud

$$\mathbf{X}_{LiDAR} = \{(\mathbf{p}_n, \mathbf{f}_n)\}_{n=1}^{N}$$

Where:
- $\mathbf{p}_n = (x_n, y_n, z_n) \in \mathbb{R}^3$ = 3D coordinates
- $\mathbf{f}_n \in \mathbb{R}^d$ = Point features (intensity, return number, etc.)
- $N$ = Total number of points

**Local Neighborhood:** For point $\mathbf{p}_n$:
$$\mathcal{N}(\mathbf{p}_n, r) = \{\mathbf{p}_m : ||\mathbf{p}_m - \mathbf{p}_n||_2 < r\}$$

### 1.2 Feature Representations

#### HSI Feature Embedding

$$\mathbf{F}_{HSI} = \phi_{HSI}(\mathbf{P}_{i,j}; \theta_{HSI}) \in \mathbb{R}^{d_{HSI}}$$

Where $\phi_{HSI}$ is the HSI encoder network with parameters $\theta_{HSI}$.

#### LiDAR Feature Embedding

$$\mathbf{F}_{LiDAR} = \phi_{LiDAR}(\mathcal{N}(\mathbf{p}_n, r); \theta_{LiDAR}) \in \mathbb{R}^{d_{LiDAR}}$$

Where $\phi_{LiDAR}$ is the LiDAR encoder network.

### 1.3 Fusion Formulation

#### Fused Representation

$$\mathbf{F}_{fused} = \mathcal{F}(\mathbf{F}_{HSI}, \mathbf{F}_{LiDAR}; \theta_{fusion})$$

Where $\mathcal{F}$ is the fusion function (to be specified).

### 1.4 Classification Formulation

**Species Classification:**
$$\hat{y} = \arg\max_c \, p(y=c | \mathbf{F}_{fused})$$

Where $c \in \{1, 2, ..., C\}$ represents $C$ tree species classes.

**Softmax Output:**
$$p(y=c | \mathbf{F}_{fused}) = \frac{\exp(z_c)}{\sum_{k=1}^{C} \exp(z_k)}$$

Where $\mathbf{z} = W_{cls} \cdot \mathbf{F}_{fused} + \mathbf{b}_{cls}$

### 1.5 Structural Parameter Regression

**Canopy Height:**
$$\hat{h} = g_{height}(\mathbf{F}_{fused}; \theta_{height}) \in \mathbb{R}^+$$

**Crown Diameter:**
$$\hat{d} = g_{crown}(\mathbf{F}_{fused}; \theta_{crown}) \in \mathbb{R}^+$$

### 1.6 Loss Functions

**Classification Loss (Cross-Entropy):**
$$\mathcal{L}_{cls} = -\frac{1}{N}\sum_{i=1}^{N}\sum_{c=1}^{C} y_{i,c} \log(\hat{y}_{i,c})$$

**Structural Regression Loss (Smooth L1):**
$$\mathcal{L}_{struct} = \frac{1}{N}\sum_{i=1}^{N} \text{SmoothL1}(h_i - \hat{h}_i) + \text{SmoothL1}(d_i - \hat{d}_i)$$

**Total Loss:**
$$\mathcal{L}_{total} = \mathcal{L}_{cls} + \lambda_{struct} \mathcal{L}_{struct}$$

Where $\lambda_{struct}$ balances the two objectives.

---

## 2) Method/System Architecture

### 2.1 Overall Architecture: HyperForest Framework

```
┌────────────────────────────────────────────────────────────────────────┐
│                         HyperForest Architecture                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   INPUT STAGE                                                          │
│   ┌────────────────┐        ┌────────────────┐                        │
│   │  HSI Patch     │        │  LiDAR Points  │                        │
│   │  (p×p×B)       │        │  (N×(3+d))     │                        │
│   └───────┬────────┘        └───────┬────────┘                        │
│           │                         │                                  │
│   ENCODER STAGE                     │                                  │
│           ▼                         ▼                                  │
│   ┌────────────────┐        ┌────────────────┐                        │
│   │  HSI Encoder   │        │  LiDAR Encoder │                        │
│   │  (3D-CNN +     │        │  (PointNet++   │                        │
│   │   Transformer) │        │   variant)     │                        │
│   └───────┬────────┘        └───────┬────────┘                        │
│           │                         │                                  │
│           │  F_HSI (d_HSI)          │  F_LiDAR (d_LiDAR)              │
│           │                         │                                  │
│   FUSION STAGE                      │                                  │
│           └──────────┬──────────────┘                                  │
│                      ▼                                                 │
│           ┌─────────────────────┐                                      │
│           │  Cross-Modal Fusion │                                      │
│           │  Module (CMFM)      │                                      │
│           │  - Cross-Attention  │                                      │
│           │  - Gated Fusion     │                                      │
│           └──────────┬──────────┘                                      │
│                      │  F_fused (d_fused)                              │
│   PREDICTION STAGE   │                                                 │
│                      ▼                                                 │
│           ┌─────────────────────┐                                      │
│           │  Multi-Task Head    │                                      │
│           │  ┌───────────────┐  │                                      │
│           │  │ Species Head  │──┼──▶ Species Class (C classes)        │
│           │  └───────────────┘  │                                      │
│           │  ┌───────────────┐  │                                      │
│           │  │ Structure Head│──┼──▶ Height, Crown Diameter           │
│           │  └───────────────┘  │                                      │
│           └─────────────────────┘                                      │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Specifications

#### 2.2.1 HSI Encoder

**Architecture:** Hybrid 3D-CNN + Transformer

```
HSI Encoder Architecture:
├── Input: (B, p, p, B) - Batch of spectral-spatial patches
├── Stage 1: Spectral Feature Extraction
│   ├── Conv3D(1, 32, kernel=(1,1,7), stride=(1,1,2))
│   ├── BatchNorm3D + ReLU
│   ├── Conv3D(32, 64, kernel=(1,1,5), stride=(1,1,2))
│   └── BatchNorm3D + ReLU
├── Stage 2: Spatial Feature Extraction  
│   ├── Conv3D(64, 128, kernel=(3,3,3))
│   ├── BatchNorm3D + ReLU
│   └── MaxPool3D(2,2,2)
├── Stage 3: Spectral-Spatial Transformer
│   ├── Reshape to sequence
│   ├── Positional Encoding
│   ├── TransformerEncoder(4 layers, 8 heads, d_model=256)
│   └── [CLS] token extraction
└── Output: F_HSI ∈ R^(d_HSI) where d_HSI = 256
```

**Key Parameters:**
- Patch size: $p = 15$ pixels
- Spectral bands: $B$ (full or PCA-reduced)
- Hidden dimension: 256
- Transformer layers: 4
- Attention heads: 8

#### 2.2.2 LiDAR Encoder

**Architecture:** Modified PointNet++ with Set Abstraction

```
LiDAR Encoder Architecture:
├── Input: (B, N, 3+d) - Point cloud with features
├── Stage 1: Set Abstraction Layer 1
│   ├── Sampling: FPS to 1024 points
│   ├── Grouping: Ball query, r=0.5m, K=32
│   ├── PointNet: MLP(3+d → 32 → 64 → 128)
│   └── MaxPool per group
├── Stage 2: Set Abstraction Layer 2
│   ├── Sampling: FPS to 256 points
│   ├── Grouping: Ball query, r=1.0m, K=64
│   ├── PointNet: MLP(128+3 → 128 → 256)
│   └── MaxPool per group
├── Stage 3: Set Abstraction Layer 3
│   ├── Sampling: FPS to 64 points
│   ├── Grouping: Ball query, r=2.0m, K=64
│   ├── PointNet: MLP(256+3 → 256 → 512)
│   └── MaxPool per group
├── Stage 4: Global Feature Aggregation
│   ├── MLP(512 → 512 → 256)
│   └── Global MaxPool
└── Output: F_LiDAR ∈ R^(d_LiDAR) where d_LiDAR = 256
```

**Key Parameters:**
- Input points: $N = 4096$ per sample
- Point features: $d = 4$ (intensity, return_number, num_returns, normalized_z)
- Output dimension: 256

#### 2.2.3 Cross-Modal Fusion Module (CMFM)

**Architecture:** Cross-Attention + Gated Fusion

```
Cross-Modal Fusion Module:
├── Input: F_HSI ∈ R^(d_HSI), F_LiDAR ∈ R^(d_LiDAR)
│
├── Cross-Attention Branch:
│   ├── HSI-to-LiDAR Attention:
│   │   ├── Q = Linear(F_HSI)
│   │   ├── K = Linear(F_LiDAR)
│   │   ├── V = Linear(F_LiDAR)
│   │   └── F_HSI→L = Softmax(QK^T/√d)V
│   ├── LiDAR-to-HSI Attention:
│   │   ├── Q = Linear(F_LiDAR)
│   │   ├── K = Linear(F_HSI)
│   │   ├── V = Linear(F_HSI)
│   │   └── F_LiDAR→H = Softmax(QK^T/√d)V
│   └── F_cross = Concat(F_HSI→L, F_LiDAR→H)
│
├── Gated Fusion Branch:
│   ├── g_HSI = Sigmoid(Linear(F_HSI))
│   ├── g_LiDAR = Sigmoid(Linear(F_LiDAR))
│   └── F_gated = g_HSI ⊙ F_HSI + g_LiDAR ⊙ F_LiDAR
│
├── Final Fusion:
│   ├── F_combined = Concat(F_cross, F_gated)
│   ├── F_fused = MLP(F_combined)
│   └── Dropout(0.3)
│
└── Output: F_fused ∈ R^(d_fused) where d_fused = 512
```

#### 2.2.4 Multi-Task Prediction Head

```
Multi-Task Head:
├── Input: F_fused ∈ R^512
│
├── Species Classification Branch:
│   ├── Linear(512 → 256) + ReLU + Dropout(0.5)
│   ├── Linear(256 → C)
│   └── Softmax → p(y|F_fused)
│
├── Structural Regression Branch:
│   ├── Linear(512 → 128) + ReLU
│   ├── Linear(128 → 64) + ReLU
│   └── Linear(64 → 2) → [height, crown_diameter]
│
└── Outputs: Species probabilities, Structural parameters
```

### 2.3 Interfaces

| Interface | Input | Output | Protocol |
|-----------|-------|--------|----------|
| **Data Loader** | Raw HSI/LiDAR files | Tensor batches | PyTorch DataLoader |
| **HSI Preprocessor** | Raw HSI cube | Calibrated, normalized patches | NumPy/GDAL |
| **LiDAR Preprocessor** | LAS/LAZ files | Normalized point arrays | laspy/Open3D |
| **Model Interface** | (HSI_batch, LiDAR_batch) | (species_probs, struct_params) | PyTorch Module |
| **Inference API** | GeoTIFF + LAS | Species map + GeoJSON | REST/gRPC |

### 2.4 Data Flow

```
Data Flow Diagram:

[Raw UAV Data]
      │
      ├──▶ [HSI Processing Pipeline]
      │         │
      │         ├── Radiometric Calibration
      │         ├── Atmospheric Correction
      │         ├── Geometric Correction
      │         ├── Mosaicking
      │         └── Patch Extraction
      │                   │
      │                   ▼
      │              [HSI Patches]
      │                   │
      └──▶ [LiDAR Processing Pipeline]
                │
                ├── Noise Filtering
                ├── Ground Classification
                ├── Height Normalization
                ├── Co-registration with HSI
                └── Point Sampling
                          │
                          ▼
                   [LiDAR Points]
                          │
      ┌───────────────────┴───────────────────┐
      │                                       │
      ▼                                       ▼
[HSI Encoder]                         [LiDAR Encoder]
      │                                       │
      │ F_HSI                         F_LiDAR │
      │                                       │
      └───────────────┬───────────────────────┘
                      │
                      ▼
              [Fusion Module]
                      │
                      │ F_fused
                      ▼
              [Multi-Task Head]
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   [Species Map]         [Structural Params]
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
               [DSS Integration]
                      │
                      ▼
              [Output Products]
              - Classification maps
              - Forest inventory
              - Reports/Visualizations
```

### 2.5 Assumptions and Constraints

#### Technical Assumptions

| ID | Assumption | Justification | Validation Approach |
|----|------------|---------------|---------------------|
| A1 | HSI and LiDAR can be accurately co-registered | Standard GPS/IMU quality | Registration accuracy assessment |
| A2 | Spectral signatures distinguish target species | Literature support | Spectral separability analysis |
| A3 | LiDAR penetrates canopy sufficiently | Multi-return capability | Point density analysis |
| A4 | Training data is representative | Stratified sampling design | Cross-site validation |
| A5 | Species distribution is learnable from data | ML feasibility | Baseline performance check |

#### Constraints

| Constraint | Type | Specification | Impact |
|------------|------|---------------|--------|
| GPU Memory | Hardware | ≤24 GB | Batch size limits |
| Inference Latency | Performance | <1s per patch | Architecture choices |
| Training Time | Resource | <48h total | Hyperparameter search limits |
| Model Size | Deployment | <500 MB | Pruning/quantization may be needed |
| Point Cloud Size | Data | ≤4096 pts/sample | Sampling strategy required |

---

## 3) Algorithms and Procedures

### 3.1 Training Algorithm

```
Algorithm 1: HyperForest Training Procedure

Input:
  - D_train: Training dataset {(X_HSI^i, X_LiDAR^i, y^i, h^i, d^i)}
  - D_val: Validation dataset
  - θ: Model parameters (HSI encoder, LiDAR encoder, fusion, heads)
  - η: Learning rate
  - T: Maximum epochs
  - λ_struct: Structural loss weight

Output:
  - θ*: Optimized model parameters

Procedure:
1: Initialize θ randomly or from pretrained weights
2: optimizer ← AdamW(θ, lr=η, weight_decay=1e-4)
3: scheduler ← CosineAnnealingLR(optimizer, T_max=T)
4: best_val_acc ← 0

5: FOR epoch = 1 TO T DO
6:   // Training phase
7:   model.train()
8:   FOR each batch (X_HSI, X_LiDAR, y, h, d) in D_train DO
9:     F_HSI ← HSI_Encoder(X_HSI)
10:    F_LiDAR ← LiDAR_Encoder(X_LiDAR)
11:    F_fused ← Fusion_Module(F_HSI, F_LiDAR)
12:    y_pred, struct_pred ← Prediction_Head(F_fused)
13:    
14:    L_cls ← CrossEntropyLoss(y_pred, y)
15:    L_struct ← SmoothL1Loss(struct_pred, [h, d])
16:    L_total ← L_cls + λ_struct * L_struct
17:    
18:    optimizer.zero_grad()
19:    L_total.backward()
20:    clip_grad_norm_(θ, max_norm=1.0)
21:    optimizer.step()
22:  END FOR
23:  
24:  // Validation phase
25:  val_acc ← Evaluate(model, D_val)
26:  scheduler.step()
27:  
28:  // Model selection
29:  IF val_acc > best_val_acc THEN
30:    best_val_acc ← val_acc
31:    θ* ← θ
32:    SaveCheckpoint(θ*, epoch)
33:  END IF
34:  
35:  // Early stopping check
36:  IF no improvement for patience epochs THEN
37:    BREAK
38:  END IF
39: END FOR

40: RETURN θ*

Complexity: O(T × |D_train| × (C_HSI + C_LiDAR + C_fusion))
  where C_* represents component forward/backward complexity
```

### 3.2 Inference Algorithm

```
Algorithm 2: HyperForest Inference Pipeline

Input:
  - θ*: Trained model parameters
  - HSI_scene: Full hyperspectral scene (H × W × B)
  - LiDAR_scene: Full LiDAR point cloud
  - patch_size: Spatial patch size
  - stride: Sliding window stride

Output:
  - Species_map: (H × W) classification map
  - Height_map: (H × W) canopy height estimates
  - Crown_map: (H × W) crown diameter estimates
  - Confidence_map: (H × W) prediction confidence

Procedure:
1: model.load(θ*)
2: model.eval()
3: Initialize output maps with zeros

4: // Sliding window inference
5: FOR i = 0 TO H-patch_size STEP stride DO
6:   FOR j = 0 TO W-patch_size STEP stride DO
7:     // Extract HSI patch
8:     HSI_patch ← HSI_scene[i:i+patch_size, j:j+patch_size, :]
9:     
10:    // Extract corresponding LiDAR points
11:    bbox ← GetGeoBoundingBox(i, j, patch_size)
12:    LiDAR_points ← FilterPointsByBBox(LiDAR_scene, bbox)
13:    LiDAR_points ← SamplePoints(LiDAR_points, N=4096)
14:    
15:    // Forward pass
16:    WITH torch.no_grad():
17:      F_HSI ← HSI_Encoder(HSI_patch)
18:      F_LiDAR ← LiDAR_Encoder(LiDAR_points)
19:      F_fused ← Fusion_Module(F_HSI, F_LiDAR)
20:      probs, struct ← Prediction_Head(F_fused)
21:    
22:    // Assign predictions to center pixel
23:    center_i, center_j ← i + patch_size//2, j + patch_size//2
24:    Species_map[center_i, center_j] ← argmax(probs)
25:    Confidence_map[center_i, center_j] ← max(probs)
26:    Height_map[center_i, center_j] ← struct[0]
27:    Crown_map[center_i, center_j] ← struct[1]
28:  END FOR
29: END FOR

30: // Post-processing
31: Species_map ← MorphologicalSmoothing(Species_map)
32: Apply spatial consistency filtering

33: RETURN Species_map, Height_map, Crown_map, Confidence_map

Complexity: O((H/stride) × (W/stride) × C_forward)
Resources: GPU memory scales with batch_size × patch_size × bands
```

### 3.3 Data Preprocessing Algorithm

```
Algorithm 3: HSI-LiDAR Co-registration and Preprocessing

Input:
  - HSI_raw: Raw hyperspectral imagery
  - LiDAR_raw: Raw LAS point cloud
  - GPS_IMU: Navigation data
  - GCP: Ground control points (optional)

Output:
  - HSI_processed: Calibrated, georeferenced HSI
  - LiDAR_processed: Filtered, normalized point cloud
  - Registration_params: Transformation parameters

Procedure:
1: // HSI Preprocessing
2: HSI_radiance ← RadiometricCalibration(HSI_raw, sensor_params)
3: HSI_reflectance ← AtmosphericCorrection(HSI_radiance, MODTRAN)
4: HSI_ortho ← OrthoRectification(HSI_reflectance, DEM, GPS_IMU)
5: IF GCP available THEN
6:   HSI_ortho ← GeometricRefinement(HSI_ortho, GCP)
7: END IF
8: HSI_normalized ← MinMaxNormalize(HSI_ortho)

9: // LiDAR Preprocessing
10: LiDAR_filtered ← NoiseFilter(LiDAR_raw, SOR_params)
11: Ground_points ← GroundClassification(LiDAR_filtered, CSF)
12: DEM_LiDAR ← InterpolateDEM(Ground_points)
13: LiDAR_normalized ← HeightNormalize(LiDAR_filtered, DEM_LiDAR)
14: Add computed features: intensity_norm, return_ratio

15: // Co-registration
16: Registration_params ← ICPAlignment(HSI_ortho, LiDAR_normalized)
17: Validate: RMSE < threshold
18: Apply registration transformation

19: RETURN HSI_normalized, LiDAR_normalized, Registration_params
```

### 3.4 Complexity and Resource Analysis

| Component | Time Complexity | Space Complexity | GPU Memory |
|-----------|-----------------|------------------|------------|
| HSI Encoder | O(p² × B × d) | O(d²) | ~4 GB |
| LiDAR Encoder | O(N × K × d) | O(N × d) | ~2 GB |
| Fusion Module | O(d²) | O(d²) | ~1 GB |
| Full Forward | O(p² × B + N × K) | O(N × d + p² × B) | ~8 GB |
| Full Backward | 2× Forward | 2× Forward | ~16 GB |

**Estimated Training Resources:**
- GPU: NVIDIA RTX 3090 (24GB) or A100 (40GB)
- Training time: ~24-48 hours for full training
- Batch size: 16-32 (depending on GPU)

### 3.5 Failure Modes and Handling

| Failure Mode | Detection | Recovery Strategy |
|--------------|-----------|-------------------|
| Out of Memory | CUDA OOM exception | Reduce batch size, gradient checkpointing |
| NaN in loss | isnan() check | Gradient clipping, learning rate reduction |
| Poor convergence | Validation plateau | Learning rate schedule, architecture adjustment |
| Overfitting | Train-val gap | Dropout increase, data augmentation |
| Registration error | RMSE threshold | Manual correction, exclude sample |
| Missing LiDAR points | Point count < threshold | Fallback to HSI-only inference |

---

## 4) Evaluation Design

### 4.1 Experiments/Studies

#### Experiment 1: Main Species Classification Performance

| Aspect | Specification |
|--------|---------------|
| **Objective** | Evaluate overall classification accuracy |
| **Dataset** | Full Meghalaya dataset, all species |
| **Split** | 60% train, 20% val, 20% test (spatially disjoint) |
| **Metrics** | OA, AA, Kappa, F1-macro, per-class F1, confusion matrix |
| **Baselines** | B1-B11 (all tiers) |
| **Runs** | 5 random seeds, report mean ± std |

#### Experiment 2: Fusion Strategy Ablation

| Aspect | Specification |
|--------|---------------|
| **Objective** | Compare fusion approaches |
| **Variants** | HSI-only, LiDAR-only, Early fusion, Mid fusion, Late fusion, Proposed CMFM |
| **Metrics** | OA, AA, parameter count, inference time |
| **Analysis** | Paired statistical tests between variants |

#### Experiment 3: Structural Parameter Estimation

| Aspect | Specification |
|--------|---------------|
| **Objective** | Evaluate height and crown estimation accuracy |
| **Metrics** | RMSE, MAE, R², bias analysis |
| **Baselines** | LiDAR-only methods, traditional CHM approaches |
| **Validation** | Against field-measured ground truth |

#### Experiment 4: Component Ablation

| Aspect | Specification |
|--------|---------------|
| **Objective** | Understand contribution of each component |
| **Variants** | - HSI encoder variants (CNN-only vs. Transformer) |
|              | - LiDAR encoder variants (PointNet++ vs. alternatives) |
|              | - Fusion variants (attention types) |
| **Metrics** | OA, computational cost |

#### Experiment 5: Efficiency Analysis

| Aspect | Specification |
|--------|---------------|
| **Objective** | Assess operational viability |
| **Metrics** | Training time, inference throughput, GPU memory, model size |
| **Comparison** | Against all baselines |
| **Target** | <1s inference per patch |

#### Experiment 6: Robustness and Generalization

| Aspect | Specification |
|--------|---------------|
| **Objective** | Test generalization capability |
| **Tests** | - Cross-site validation (train on Site A, test on Site B) |
|           | - Different forest types |
|           | - Varying data quality (reduced points, noisy spectra) |
| **Metrics** | OA degradation analysis |

### 4.2 Ablation Studies Design

| Ablation ID | Component Removed/Modified | Purpose |
|-------------|---------------------------|---------|
| AB1 | Remove LiDAR branch | Quantify LiDAR contribution |
| AB2 | Remove HSI branch | Quantify HSI contribution |
| AB3 | Replace cross-attention with concatenation | Test attention importance |
| AB4 | Remove gated fusion | Test gating contribution |
| AB5 | Replace Transformer with CNN-only HSI | Test Transformer benefit |
| AB6 | Reduce spectral bands (PCA to 30) | Test band selection impact |
| AB7 | Reduce LiDAR points (1024 vs 4096) | Test point density sensitivity |
| AB8 | Remove structural regression head | Test multi-task benefit |

### 4.3 Baselines Implementation Notes

| Baseline | Implementation Source | Adaptation Needed |
|----------|----------------------|-------------------|
| Random Forest | scikit-learn | Feature engineering for HSI+LiDAR |
| SVM | scikit-learn | Kernel selection, feature extraction |
| 3D-CNN (HybridSN) | Official GitHub / PyTorch | None |
| SpectralFormer | Official GitHub | None |
| PointNet++ | PyTorch Geometric | Forest domain adaptation |
| Late Fusion | Custom | Combine trained unimodal models |

### 4.4 Statistical Testing Protocol

```
Statistical Analysis Protocol:

1. Normality Test:
   - Shapiro-Wilk test on accuracy distributions
   - If p < 0.05, use non-parametric tests

2. Pairwise Comparison (Proposed vs. Each Baseline):
   - McNemar's test for classification agreement
   - Report χ² statistic and p-value
   - Apply Bonferroni correction for multiple comparisons

3. Overall Comparison:
   - Friedman test for multiple classifier comparison
   - Post-hoc Nemenyi test if significant

4. Effect Size:
   - Cohen's d for accuracy differences
   - Interpret: small (0.2), medium (0.5), large (0.8)

5. Confidence Intervals:
   - Bootstrap 95% CI for all reported metrics
   - Report as: mean [95% CI: lower, upper]
```

---

## 5) Threats to Validity / Threat Model

### 5.1 Internal Validity Threats

| Threat | Description | Mitigation | Residual Risk |
|--------|-------------|------------|---------------|
| **Data leakage** | Spatial autocorrelation between train/test | Spatially disjoint splits with buffer zones | Low |
| **Implementation bias** | Coding errors favoring proposed method | Unit tests, baseline reproduction from papers | Low |
| **Hyperparameter tuning** | Excessive tuning on test set | Nested CV, hyperparameter search on val only | Low |
| **Random initialization** | Results sensitive to seeds | Report mean ± std over 5 seeds | Low |
| **Ground truth errors** | Species misidentification | Expert validation, consensus labeling, error analysis | Medium |
| **Selection bias** | Non-representative sampling | Stratified sampling across species/sites | Medium |

### 5.2 External Validity Threats

| Threat | Description | Mitigation | Residual Risk |
|--------|-------------|------------|---------------|
| **Geographic specificity** | Results may not transfer to other regions | Discuss transferability, cross-site analysis | Medium |
| **Sensor dependency** | Results tied to specific UAV sensors | Document sensors, discuss sensor-agnostic design | Medium |
| **Species set limitation** | Only 15-25 of many forest species | Clear scope statement, scalability discussion | Medium |
| **Temporal limitation** | Single season data | Acknowledge, propose multi-temporal future work | High |
| **Canopy condition** | Results specific to observed forest structure | Stratified sampling, robustness experiments | Medium |

### 5.3 Construct Validity Threats

| Threat | Description | Mitigation | Residual Risk |
|--------|-------------|------------|---------------|
| **Metric completeness** | OA may hide class imbalance issues | Report AA, per-class F1, confusion matrix | Low |
| **Baseline fairness** | Weak baseline implementations | Use published results, official code | Low |
| **Ecological validity** | Lab metrics vs. field utility | Include operational metrics, user study if possible | Medium |
| **Structural accuracy validation** | Ground truth measurement errors | Standard forestry protocols, multiple measurements | Medium |

### 5.4 Reliability Threats

| Threat | Description | Mitigation | Residual Risk |
|--------|-------------|------------|---------------|
| **Reproducibility** | Results not reproducible | Release code, data, exact configurations | Low |
| **Hardware dependency** | Results vary across GPUs | Specify hardware, use deterministic ops | Low |
| **Software versioning** | Package version affects results | Pin dependencies, Docker container | Low |

### 5.5 Threat Summary Matrix

| Threat Category | High Risk | Medium Risk | Low Risk |
|-----------------|-----------|-------------|----------|
| **Internal** | - | Ground truth errors, Selection bias | Data leakage, Implementation, HP tuning, Random seeds |
| **External** | Temporal limitation | Geographic, Sensor, Species, Canopy | - |
| **Construct** | - | Ecological validity, Struct accuracy | Metrics, Baselines |
| **Reliability** | - | - | Reproducibility, Hardware, Software |

---

## Status

**⏹️ STOP. DO NOT WRITE FULL PAPER YET.**

Phase 3 Technical Deep Dive is complete. All formal definitions, architecture specifications, algorithms, and evaluation design are documented.

---

## Next Step

Proceed to **Phase 4: Full Paper Expansion** to draft each section of the manuscript.
