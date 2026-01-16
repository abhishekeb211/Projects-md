# PHASE 3: Technical Deep Dive

## 1. Formal Terms and Notation

### 1.1 Data Representations

| Symbol | Description | Dimensions |
|--------|-------------|------------|
| $\mathbf{X}_{HSI}$ | Hyperspectral image cube | $H \times W \times B$ |
| $H, W$ | Spatial dimensions | Scalar |
| $B$ | Number of spectral bands | Scalar (200-425) |
| $\mathbf{x}_i$ | Spectral signature at pixel $i$ | $\mathbb{R}^B$ |
| $\mathbf{P}_{LiDAR}$ | LiDAR point cloud | $N \times D$ |
| $N$ | Number of points | Scalar ($10^5 - 10^7$) |
| $D$ | Point feature dimension | $D = 6-8$ (xyz + features) |
| $\mathbf{p}_j$ | Individual point | $\mathbb{R}^D$ |

### 1.2 Model Components

| Symbol | Description | Dimensions |
|--------|-------------|------------|
| $\mathbf{F}_{spec}$ | Spectral feature map | $\mathbb{R}^{C_{spec}}$ |
| $\mathbf{F}_{struct}$ | Structural feature vector | $\mathbb{R}^{C_{struct}}$ |
| $\mathbf{F}_{fused}$ | Fused representation | $\mathbb{R}^{C_{fused}}$ |
| $\mathbf{A}_{cross}$ | Cross-modal attention | $C_{spec} \times C_{struct}$ |
| $\hat{\mathbf{y}}_{cls}$ | Class probabilities | $\mathbb{R}^K$ |
| $\hat{\mathbf{y}}_{struct}$ | Structural predictions | $\mathbb{R}^M$ |
| $K$ | Number of species | Scalar (25) |
| $M$ | Number of structural params | Scalar (5) |

### 1.3 Training Notation

| Symbol | Description |
|--------|-------------|
| $\mathcal{D}_{train}$ | Training set: $\{(\mathbf{X}^{(i)}, \mathbf{P}^{(i)}, y^{(i)}, \mathbf{s}^{(i)})\}$ |
| $\mathcal{L}_{cls}$ | Classification loss |
| $\mathcal{L}_{struct}$ | Structural regression loss |
| $\mathcal{L}_{total}$ | Combined multi-task loss |
| $\theta$ | All learnable parameters |
| $\eta$ | Learning rate |
| $\lambda$ | Task weighting coefficient |

---

## 2. System Architecture

### 2.1 High-Level Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              FOREST SPECIES & STRUCTURE ANALYSIS FRAMEWORK                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐                                       │
│  │  UAV HSI    │     │  UAV LiDAR  │                                       │
│  │   Sensor    │     │   Sensor    │                                       │
│  └──────┬──────┘     └──────┬──────┘                                       │
│         │                   │                                               │
│         ▼                   ▼                                               │
│  ┌─────────────┐     ┌─────────────┐                                       │
│  │Preprocessing│     │Point Cloud  │                                       │
│  │  Pipeline   │     │ Processing  │                                       │
│  └──────┬──────┘     └──────┬──────┘                                       │
│         │                   │                                               │
│         ▼                   ▼                                               │
│  ┌─────────────────────────────────────────────┐                           │
│  │           CO-REGISTRATION MODULE             │                           │
│  └─────────────────────┬───────────────────────┘                           │
│                        │                                                    │
│         ┌──────────────┴──────────────┐                                    │
│         ▼                             ▼                                    │
│  ┌─────────────┐              ┌─────────────┐                              │
│  │  SPECTRAL   │              │ STRUCTURAL  │                              │
│  │  ENCODER    │              │  ENCODER    │                              │
│  │ (Hybrid CNN │              │ (PointNet++ │                              │
│  │ Transformer)│              │  based)     │                              │
│  └──────┬──────┘              └──────┬──────┘                              │
│         │    F_spec                  │    F_struct                         │
│         └───────────┬────────────────┘                                     │
│                     ▼                                                       │
│         ┌─────────────────────┐                                            │
│         │  CROSS-MODAL FUSION │                                            │
│         │  (Attention + Gate) │                                            │
│         └──────────┬──────────┘                                            │
│                    │    F_fused                                            │
│         ┌─────────────────────────────────┐                                │
│         │       MULTI-TASK HEADS          │                                │
│         │                                 │                                │
│         │  ┌──────────┐   ┌────────────┐ │                                │
│         │  │SPECIES   │   │STRUCTURAL  │ │                                │
│         │  │CLASSIFIER│   │REGRESSOR   │ │                                │
│         │  └────┬─────┘   └─────┬──────┘ │                                │
│         └───────┼───────────────┼────────┘                                │
│                 ▼               ▼                                          │
│         ┌───────────┐   ┌────────────┐                                    │
│         │SPECIES MAP│   │STRUCTURE   │                                    │
│         │+CONFIDENCE│   │PARAMETERS  │                                    │
│         └───────────┘   └────────────┘                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Interfaces

#### Spectral Encoder Input/Output
```python
Input:
    hsi_patch: Tensor       # Shape: (B, C, H, W) or (B, H, W, C)
                            # B=batch, C=bands, H=W=patch_size
Output:
    F_spec: Tensor          # Shape: (B, 512)
    attention_weights: Tensor  # For visualization
```

#### Structural Encoder Input/Output
```python
Input:
    point_cloud: Tensor     # Shape: (B, N, D)
                            # N=2048 points, D=6-8 features
Output:
    F_struct: Tensor        # Shape: (B, 512)
    point_features: Tensor  # Intermediate for visualization
```

#### Fusion Module Input/Output
```python
Input:
    F_spec: Tensor          # Shape: (B, 512)
    F_struct: Tensor        # Shape: (B, 512)
Output:
    F_fused: Tensor         # Shape: (B, 512)
    attention_map: Tensor   # Cross-modal attention
    gate_values: Tensor     # Modality weighting
```

---

## 3. Detailed Architecture

### 3.1 Spectral Encoder (Hybrid CNN-Transformer)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SPECTRAL ENCODER                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: HSI Patch (P × P × B)  [P=15, B=224]                               │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │        3D Convolutional Stem           │                                │
│  │  Conv3D(1→32, k=(3,3,7)) + BN + ReLU   │                                │
│  │  Conv3D(32→64, k=(3,3,5)) + BN + ReLU  │                                │
│  │  Output: (11 × 11 × 210 × 64)          │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      2D Spatial Refinement             │                                │
│  │  Reshape: (11 × 11 × 13440)            │                                │
│  │  Conv2D(13440→256, k=3) + BN + ReLU    │                                │
│  │  Conv2D(256→128, k=3) + BN + ReLU      │                                │
│  │  Output: (7 × 7 × 128)                 │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      Spectral Tokenization             │                                │
│  │  Flatten spatial: (49, 128)            │                                │
│  │  Linear projection: (49, 512)          │                                │
│  │  Add positional encoding               │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │   Transformer Encoder (4 layers)       │                                │
│  │                                        │                                │
│  │   For each layer:                      │                                │
│  │     LayerNorm → MultiHead Attention    │                                │
│  │     → Residual → LayerNorm → FFN       │                                │
│  │     → Residual                         │                                │
│  │                                        │                                │
│  │   Heads = 8, d_model = 512, d_ff=2048 │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      Global Aggregation                │                                │
│  │  [CLS] token or Global Average Pool    │                                │
│  │  Output: F_spec ∈ R^512                │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Structural Encoder (PointNet++ Variant)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STRUCTURAL ENCODER                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: Point Cloud (N × D) [N=2048, D=7: xyz, intensity, returns, nDSM]   │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 1            │                                │
│  │                                        │                                │
│  │  FPS: N₁ = 512 centroids               │                                │
│  │  Ball Query: r=0.5m, k=32 neighbors    │                                │
│  │  PointNet: MLP(7→64→128)               │                                │
│  │  Max Pool within groups                │                                │
│  │  Output: (512, 128)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 2            │                                │
│  │                                        │                                │
│  │  FPS: N₂ = 128 centroids               │                                │
│  │  Ball Query: r=1.0m, k=64 neighbors    │                                │
│  │  PointNet: MLP(128→256→512)            │                                │
│  │  Output: (128, 512)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 3            │                                │
│  │                                        │                                │
│  │  FPS: N₃ = 32 centroids                │                                │
│  │  Ball Query: r=2.0m, k=64 neighbors    │                                │
│  │  PointNet: MLP(512→512→1024)           │                                │
│  │  Output: (32, 1024)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Global Aggregation                 │                                │
│  │                                        │                                │
│  │  Global Max Pool: (1024,)              │                                │
│  │  Global Avg Pool: (1024,)              │                                │
│  │  Concat + MLP: 2048 → 512              │                                │
│  │  Output: F_struct ∈ R^512              │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
│  FOREST-SPECIFIC ADAPTATIONS:                                              │
│  • Height-stratified grouping (ground/understory/canopy)                   │
│  • Multi-return weighting for penetration depth                            │
│  • Normalized height as key feature (nDSM)                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Cross-Modal Attention Fusion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  CROSS-MODAL ATTENTION FUSION                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Inputs: F_spec ∈ R^512, F_struct ∈ R^512                                  │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │    Spectral-to-Structural Attention    │                                │
│  │                                        │                                │
│  │    Q = W_Q · F_spec      [512×512]     │                                │
│  │    K = W_K · F_struct    [512×512]     │                                │
│  │    V = W_V · F_struct    [512×512]     │                                │
│  │                                        │                                │
│  │    α = softmax(Q · K^T / √d)           │                                │
│  │    F_spec' = F_spec + α · V            │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    │                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │    Structural-to-Spectral Attention    │                                │
│  │                                        │                                │
│  │    Q = W_Q · F_struct                  │                                │
│  │    K = W_K · F_spec                    │                                │
│  │    V = W_V · F_spec                    │                                │
│  │                                        │                                │
│  │    α = softmax(Q · K^T / √d)           │                                │
│  │    F_struct' = F_struct + α · V        │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    │                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │         Gated Fusion                   │                                │
│  │                                        │                                │
│  │    g = σ(W_g · [F_spec'; F_struct'])   │                                │
│  │    F_fused = g ⊙ F_spec' + (1-g) ⊙ F_struct'                           │
│  │                                        │                                │
│  │    Output: F_fused ∈ R^512             │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.4 Multi-Task Heads

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MULTI-TASK HEADS                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: F_fused ∈ R^512                                                    │
│                                                                             │
│  ┌─────────────────────┐      ┌─────────────────────┐                      │
│  │   CLASSIFICATION    │      │   STRUCTURAL        │                      │
│  │   HEAD              │      │   REGRESSION HEAD   │                      │
│  │                     │      │                     │                      │
│  │  Linear(512→256)    │      │  Linear(512→256)    │                      │
│  │  BatchNorm + ReLU   │      │  BatchNorm + ReLU   │                      │
│  │  Dropout(0.5)       │      │  Dropout(0.3)       │                      │
│  │  Linear(256→128)    │      │  Linear(256→128)    │                      │
│  │  BatchNorm + ReLU   │      │  BatchNorm + ReLU   │                      │
│  │  Dropout(0.3)       │      │                     │                      │
│  │  Linear(128→K=25)   │      │  Linear(128→M=5)    │                      │
│  │  Softmax            │      │  (no activation)    │                      │
│  │                     │      │                     │                      │
│  │  Output: y_cls      │      │  Output: y_struct   │                      │
│  │  (25 probabilities) │      │  (5 parameters)     │                      │
│  └─────────────────────┘      └─────────────────────┘                      │
│                                                                             │
│  Structural Parameters:                                                     │
│    1. Canopy Height (m)                                                    │
│    2. Crown Area (m²)                                                      │
│    3. Tree Density (trees/ha) - area normalized                            │
│    4. Crown Volume (m³)                                                    │
│    5. Estimated DBH (cm) - via allometry                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Training Strategy

### 4.1 Multi-Task Loss Function

```
Total Loss = λ_cls · L_cls + λ_struct · L_struct

L_cls = Focal Loss with class weights
      = -α_t (1-p_t)^γ log(p_t), γ=2.0

L_struct = Weighted MSE + Huber
         = Σ w_m · SmoothL1(y_m, ŷ_m)

λ_cls = 1.0 (fixed)
λ_struct = 0.5 (tunable via validation)
```

### 4.2 Training Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | AdamW |
| Learning Rate | 1e-4 (initial) |
| LR Schedule | Cosine Annealing |
| Batch Size | 32 |
| Max Epochs | 200 |
| Early Stopping | Patience=20 |
| Weight Decay | 1e-4 |
| Gradient Clipping | max_norm=1.0 |

### 4.3 Data Augmentation

| Modality | Augmentation | Parameters |
|----------|--------------|------------|
| HSI | Spectral noise | SNR 30-50 dB |
| HSI | Band dropout | 5% random bands |
| HSI | Spatial flip | H, V, HV |
| HSI | Random crop | ±2 pixels |
| LiDAR | Jittering | σ=0.01m |
| LiDAR | Rotation | z-axis, 0-360° |
| LiDAR | Point dropout | 5% random |
| LiDAR | Scaling | 0.95-1.05 |

---

## 5. Evaluation Design

### 5.1 Main Experiments

#### Experiment 1: Overall Performance
- Full MeghalayaForest-25 dataset
- 60/20/20 train/val/test split
- Spatial blocking (500m buffer)
- 5 runs with different seeds
- Compare all baselines

#### Experiment 2: Ablation Studies
- A1: HSI only
- A2: LiDAR only
- A3: No cross-attention
- A4: CNN only (no transformer)
- A5: Early fusion
- A6: Late fusion
- A7: Single-task (classification only)

#### Experiment 3: Cross-Site Generalization
- Leave-one-site-out validation
- Domain adaptation comparison

#### Experiment 4: Satellite Scaling
- UAV (1m) → AVIRIS-NG (4m) → HySIS (30m)
- Spectral resampling protocols
- Accuracy degradation analysis

### 5.2 Statistical Analysis

| Test | Application |
|------|-------------|
| McNemar's | Pairwise classifier comparison |
| Bootstrap CI | 95% confidence intervals |
| Paired t-test | Cross-validation comparison |
| Bonferroni | Multiple comparison correction |

---

## 6. ISRO Format B-5 & B-6 Drafts

### B-5: Approach/Methodology

**Data Acquisition**:
- UAV campaigns using DJI M600 Pro or equivalent
- HSI sensor: VNIR-SWIR (380-2500nm, 200+ bands, 1m GSD)
- LiDAR: Multi-return, 50+ pts/m²
- 3 sites covering diverse forest types

**Processing Pipeline**:
- Atmospheric correction, LiDAR normalization
- Sub-pixel co-registration
- Patch/point extraction at field plot locations

**Deep Learning Framework**:
- Hybrid CNN-Transformer architecture
- Cross-modal attention fusion
- Multi-task learning for classification + structure

**Validation**:
- 500+ field plots
- Expert identification with BSI
- Spatial cross-validation

### B-6: Data Reduction/Analysis

**Input Volumes**:
- HSI: ~50 GB/site
- LiDAR: ~100 GB/site
- Total: ~450 GB

**Outputs**:
- Species maps (25-class GeoTIFF)
- Structural parameter maps (CHM, crown area)
- Confidence maps
- Spectral-structural library

**Computational**:
- Training: ~24 hours (GPU)
- Inference: <5 sec/ha

---

## Phase Status
**PHASE 3: TECHNICAL DEEP DIVE COMPLETE** ✓

**→ Proceed to PHASE 4: Section-by-Section Drafts**
