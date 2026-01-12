# PHASE 3: Technical Deep Dive

## 1. Formal Terms and Notation

### 1.1 Data Representations

| Symbol | Description | Dimensions |
|--------|-------------|------------|
| $\mathbf{X}_{HSI}$ | Hyperspectral image cube | $H \times W \times B$ |
| $H, W$ | Spatial dimensions (height, width) | Scalar |
| $B$ | Number of spectral bands | Scalar (typically 224-425) |
| $\mathbf{x}_i$ | Spectral signature at pixel $i$ | $\mathbb{R}^B$ |
| $\mathbf{P}_{LiDAR}$ | LiDAR point cloud | $N \times D$ |
| $N$ | Number of points | Scalar (typically $10^5 - 10^7$) |
| $D$ | Point feature dimension (xyz + intensity + returns) | $D = 5-7$ |
| $\mathbf{p}_j$ | Individual point | $\mathbb{R}^D$ |

### 1.2 Model Components

| Symbol | Description | Dimensions |
|--------|-------------|------------|
| $\mathbf{F}_{spec}$ | Spectral feature map | $H' \times W' \times C_{spec}$ |
| $\mathbf{F}_{struct}$ | Structural feature vector | $\mathbb{R}^{C_{struct}}$ |
| $\mathbf{F}_{fused}$ | Fused representation | $\mathbb{R}^{C_{fused}}$ |
| $\mathbf{A}_{cross}$ | Cross-modal attention weights | $C_{spec} \times C_{struct}$ |
| $\hat{\mathbf{y}}$ | Predicted class probabilities | $\mathbb{R}^K$ |
| $K$ | Number of species classes | Scalar (25) |

### 1.3 Training Notation

| Symbol | Description |
|--------|-------------|
| $\mathcal{D}_{train}$ | Training dataset: $\{(\mathbf{X}^{(i)}, \mathbf{P}^{(i)}, y^{(i)})\}_{i=1}^{N_{train}}$ |
| $\mathcal{L}_{CE}$ | Cross-entropy loss |
| $\mathcal{L}_{focal}$ | Focal loss for class imbalance |
| $\theta$ | All learnable parameters |
| $\eta$ | Learning rate |
| $\lambda$ | Regularization coefficient |

### 1.4 Evaluation Metrics

| Symbol | Formula |
|--------|---------|
| $OA$ | $\frac{\sum_{k=1}^{K} TP_k}{\sum_{k=1}^{K} (TP_k + FP_k + FN_k + TN_k)}$ |
| $\kappa$ | $\frac{OA - P_e}{1 - P_e}$, where $P_e = \sum_{k} \frac{(TP_k + FP_k)(TP_k + FN_k)}{N^2}$ |
| $F1_k$ | $\frac{2 \cdot P_k \cdot R_k}{P_k + R_k}$ |
| $Macro F1$ | $\frac{1}{K}\sum_{k=1}^{K} F1_k$ |

---

## 2. System Architecture

### 2.1 High-Level Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HyLiFormer SYSTEM ARCHITECTURE                      │
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
│  │(Atm. Corr., │     │(Filtering,  │                                       │
│  │ Geocoding)  │     │ Align, CHM) │                                       │
│  └──────┬──────┘     └──────┬──────┘                                       │
│         │                   │                                               │
│         ▼                   ▼                                               │
│  ┌─────────────────────────────────────────────┐                           │
│  │             CO-REGISTRATION MODULE           │                           │
│  │    (Spatial alignment of HSI and LiDAR)     │                           │
│  └─────────────────────┬───────────────────────┘                           │
│                        │                                                    │
│         ┌──────────────┴──────────────┐                                    │
│         ▼                             ▼                                    │
│  ┌─────────────┐              ┌─────────────┐                              │
│  │  SPECTRAL   │              │ STRUCTURAL  │                              │
│  │  ENCODER    │              │  ENCODER    │                              │
│  │   (GSA)     │              │   (HSE)     │                              │
│  │             │              │             │                              │
│  │ 3D-CNN +    │              │ PointNet++  │                              │
│  │ Transformer │              │  Backbone   │                              │
│  └──────┬──────┘              └──────┬──────┘                              │
│         │                            │                                      │
│         │      F_spec                │      F_struct                       │
│         │                            │                                      │
│         └───────────┬────────────────┘                                     │
│                     ▼                                                       │
│         ┌─────────────────────┐                                            │
│         │  CROSS-MODAL FUSION │                                            │
│         │       (CMAF)        │                                            │
│         │                     │                                            │
│         │  Cross-Attention +  │                                            │
│         │  Gated Fusion       │                                            │
│         └──────────┬──────────┘                                            │
│                    │                                                        │
│                    ▼    F_fused                                            │
│         ┌─────────────────────┐                                            │
│         │  CLASSIFICATION     │                                            │
│         │      HEAD           │                                            │
│         │                     │                                            │
│         │  MLP + Softmax      │                                            │
│         └──────────┬──────────┘                                            │
│                    │                                                        │
│                    ▼                                                        │
│         ┌─────────────────────┐                                            │
│         │   SPECIES MAP +     │                                            │
│         │   CONFIDENCE        │                                            │
│         └─────────────────────┘                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Interfaces

#### Interface 1: HSI Preprocessing → Spectral Encoder

```python
Input:
    raw_hsi: np.ndarray       # Shape: (H, W, B_raw), dtype: uint16
    metadata: dict            # Sensor calibration, acquisition time
    
Output:
    preprocessed_hsi: Tensor  # Shape: (H, W, B), dtype: float32, normalized
    wavelengths: Tensor       # Shape: (B,), center wavelengths in nm
```

**Preprocessing Steps**:
1. Radiometric calibration (DN → radiance)
2. Atmospheric correction (FLAASH/ATCOR)
3. Geometric correction and orthorectification
4. Bad band removal (water absorption: 1350-1450nm, 1800-1950nm)
5. Spectral smoothing (Savitzky-Golay filter)
6. Normalization (per-band z-score or min-max)

#### Interface 2: LiDAR Processing → Structural Encoder

```python
Input:
    raw_las: laspy.LasData    # Raw LAS/LAZ file
    roi: Polygon              # Region of interest
    
Output:
    point_cloud: Tensor       # Shape: (N, D), xyz + features
    chm: Tensor               # Shape: (H', W'), Canopy Height Model
    metrics: dict             # Height percentiles, density metrics
```

**Processing Steps**:
1. Ground classification (CSF or PMF algorithm)
2. Height normalization (z - DTM)
3. Noise filtering (statistical outlier removal)
4. Return decomposition (first, intermediate, last)
5. Intensity normalization
6. CHM generation (max height in grid cells)

#### Interface 3: Cross-Modal Alignment

```python
Input:
    hsi_georef: Tensor        # Georeferenced HSI with CRS
    pointcloud_georef: Tensor # Georeferenced point cloud with CRS
    
Output:
    aligned_hsi: Tensor       # Resampled to common grid
    aligned_points: Tensor    # Spatially matched points
    correspondence: dict      # Pixel-to-point mapping
```

**Alignment Steps**:
1. CRS harmonization (project to common UTM zone)
2. Spatial resampling (HSI to point cloud extent)
3. Point-to-pixel assignment (within HSI GSD)
4. Quality check (spatial offset < 0.5 pixel)

### 2.3 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA FLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STAGE 1: RAW DATA                                                          │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐                           │
│  │ HSI Cube  │    │ LiDAR LAS │    │ Field GPS │                           │
│  │(H×W×425)  │    │ (N points)│    │ (species) │                           │
│  └─────┬─────┘    └─────┬─────┘    └─────┬─────┘                           │
│        │                │                │                                  │
│        ▼                ▼                ▼                                  │
│  STAGE 2: PREPROCESSED DATA                                                 │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐                           │
│  │ HSI Norm  │    │Point Cloud│    │ Labels    │                           │
│  │(H×W×224)  │    │ (N×7)     │    │ (one-hot) │                           │
│  └─────┬─────┘    └─────┬─────┘    └─────┬─────┘                           │
│        │                │                │                                  │
│        └───────┬────────┴────────┬───────┘                                 │
│                ▼                 ▼                                          │
│  STAGE 3: PATCH EXTRACTION                                                  │
│  ┌─────────────────────────────────────┐                                   │
│  │         Training Samples            │                                   │
│  │  {(hsi_patch, point_set, label)}   │                                   │
│  │       N_samples × (P×P×224, M×7, K) │                                   │
│  └─────────────────┬───────────────────┘                                   │
│                    ▼                                                        │
│  STAGE 4: FEATURE ENCODING                                                  │
│  ┌───────────┐              ┌───────────┐                                  │
│  │ F_spec    │              │ F_struct  │                                  │
│  │ (P'×P'×   │              │ (C_struct)│                                  │
│  │  C_spec)  │              │           │                                  │
│  └─────┬─────┘              └─────┬─────┘                                  │
│        │                          │                                         │
│        └──────────┬───────────────┘                                        │
│                   ▼                                                         │
│  STAGE 5: FUSION                                                            │
│  ┌───────────────────┐                                                     │
│  │     F_fused       │                                                     │
│  │    (C_fused)      │                                                     │
│  └─────────┬─────────┘                                                     │
│            ▼                                                                │
│  STAGE 6: OUTPUT                                                            │
│  ┌───────────────────┐                                                     │
│  │   y_pred (K)      │                                                     │
│  │   + confidence    │                                                     │
│  └───────────────────┘                                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Architecture: HyLiFormer

### 3.1 Spectral Encoder with Group-wise Spectral Attention (GSA)

#### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SPECTRAL ENCODER (GSA)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: HSI Patch (P × P × B)                                              │
│         P = 11 (spatial), B = 224 (spectral)                               │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │        3D Convolutional Block          │                                │
│  │  Conv3D(1, 32, kernel=(3,3,7))        │                                │
│  │  BatchNorm3D + ReLU                    │                                │
│  │  Conv3D(32, 64, kernel=(3,3,5))       │                                │
│  │  BatchNorm3D + ReLU                    │                                │
│  │  Output: (9 × 9 × 210 × 64)           │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      Spectral Reshaping                │                                │
│  │  Flatten spatial: (81, 210, 64)       │                                │
│  │  Group bands: G=30 groups of 7 bands  │                                │
│  │  Shape: (81, 30, 7×64=448)            │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │   Group-wise Spectral Attention (GSA)  │                                │
│  │                                        │                                │
│  │   For each group g ∈ {1,...,G}:       │                                │
│  │     Q_g = W_Q · group_features_g      │                                │
│  │     K_g = W_K · group_features_g      │                                │
│  │     V_g = W_V · group_features_g      │                                │
│  │     Attn_g = softmax(Q_g K_g^T / √d)  │                                │
│  │     Output_g = Attn_g · V_g           │                                │
│  │                                        │                                │
│  │   Cross-group attention:              │                                │
│  │     Q_cross = W_Q · all_groups        │                                │
│  │     K_cross = W_K · all_groups        │                                │
│  │     Output = softmax(QK^T/√d) · V     │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      Transformer Encoder Blocks (×4)   │                                │
│  │                                        │                                │
│  │  LayerNorm → MultiHead Attention       │                                │
│  │  → Residual → LayerNorm → FFN          │                                │
│  │  → Residual                            │                                │
│  │                                        │                                │
│  │  Heads = 8, d_model = 512              │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │      Spatial Aggregation               │                                │
│  │  Global Average Pool (spatial)         │                                │
│  │  Output: F_spec ∈ R^512                │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Mathematical Formulation

**3D Convolution**:
$$\mathbf{H}^{(1)} = \text{ReLU}(\text{BN}(\mathbf{W}^{(1)} * \mathbf{X}_{HSI} + \mathbf{b}^{(1)}))$$

where $\mathbf{W}^{(1)} \in \mathbb{R}^{32 \times 1 \times 3 \times 3 \times 7}$

**Group-wise Attention**:
For spectral group $g$ containing bands $\{b_{g,1}, ..., b_{g,7}\}$:

$$\mathbf{Q}_g = \mathbf{H}_g \mathbf{W}_Q, \quad \mathbf{K}_g = \mathbf{H}_g \mathbf{W}_K, \quad \mathbf{V}_g = \mathbf{H}_g \mathbf{W}_V$$

$$\text{Attention}_g = \text{softmax}\left(\frac{\mathbf{Q}_g \mathbf{K}_g^T}{\sqrt{d_k}}\right) \mathbf{V}_g$$

**Cross-Group Attention**:
$$\mathbf{F}_{spec} = \text{GlobalPool}\left(\text{TransformerEncoder}\left(\text{Concat}(\text{Attention}_1, ..., \text{Attention}_G)\right)\right)$$

### 3.2 Structural Encoder with Hierarchical Structure Encoding (HSE)

#### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STRUCTURAL ENCODER (HSE)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: Point Cloud (N × D)                                                │
│         N = 2048 (sampled), D = 7 (xyz, intensity, returns, nDSM, class)   │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 1            │                                │
│  │                                        │                                │
│  │  Sample: N₁ = 512 centroids (FPS)      │                                │
│  │  Group: k = 32 neighbors (ball query)  │                                │
│  │  PointNet: MLP(7→64→128)              │                                │
│  │  Max Pool within groups                │                                │
│  │  Output: (512, 128)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 2            │                                │
│  │                                        │                                │
│  │  Sample: N₂ = 128 centroids            │                                │
│  │  Group: k = 64 neighbors               │                                │
│  │  PointNet: MLP(128→256→512)           │                                │
│  │  Max Pool                              │                                │
│  │  Output: (128, 512)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Set Abstraction Level 3            │                                │
│  │                                        │                                │
│  │  Sample: N₃ = 32 centroids             │                                │
│  │  Group: k = 64 neighbors               │                                │
│  │  PointNet: MLP(512→512→1024)          │                                │
│  │  Max Pool                              │                                │
│  │  Output: (32, 1024)                    │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │     Global Aggregation                 │                                │
│  │                                        │                                │
│  │  Global Max Pool: (1, 1024)           │                                │
│  │  Global Avg Pool: (1, 1024)           │                                │
│  │  Concat: (1, 2048)                    │                                │
│  │  MLP: 2048 → 512                       │                                │
│  │  Output: F_struct ∈ R^512              │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
│  FOREST-SPECIFIC ENHANCEMENTS:                                             │
│  • Height stratification (ground, understory, canopy)                      │
│  • Crown boundary detection via local curvature                            │
│  • Multi-return weighting for penetration depth                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Mathematical Formulation

**Farthest Point Sampling (FPS)**:
$$\mathbf{c}_i = \arg\max_{\mathbf{p} \in \mathbf{P}} \min_{j < i} \|\mathbf{p} - \mathbf{c}_j\|_2$$

**Ball Query Grouping**:
$$\mathcal{N}_i = \{\mathbf{p}_j : \|\mathbf{p}_j - \mathbf{c}_i\|_2 < r, \mathbf{p}_j \in \mathbf{P}\}$$

**PointNet Layer**:
$$\mathbf{f}_i = \max_{\mathbf{p}_j \in \mathcal{N}_i} \text{MLP}(\mathbf{p}_j - \mathbf{c}_i)$$

**Structural Feature**:
$$\mathbf{F}_{struct} = \text{MLP}\left(\text{Concat}\left(\max_i \mathbf{f}_i^{(3)}, \text{avg}_i \mathbf{f}_i^{(3)}\right)\right)$$

### 3.3 Cross-Modal Attention Fusion (CMAF)

#### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  CROSS-MODAL ATTENTION FUSION (CMAF)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Inputs: F_spec ∈ R^512, F_struct ∈ R^512                                  │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │    Spectral-to-Structural Attention    │                                │
│  │                                        │                                │
│  │    Q_s2l = W_Q^{s2l} · F_spec         │                                │
│  │    K_s2l = W_K^{s2l} · F_struct       │                                │
│  │    V_s2l = W_V^{s2l} · F_struct       │                                │
│  │                                        │                                │
│  │    α_s2l = softmax(Q_s2l · K_s2l^T)   │                                │
│  │    F_spec' = F_spec + α_s2l · V_s2l   │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    │                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │    Structural-to-Spectral Attention    │                                │
│  │                                        │                                │
│  │    Q_l2s = W_Q^{l2s} · F_struct       │                                │
│  │    K_l2s = W_K^{l2s} · F_spec         │                                │
│  │    V_l2s = W_V^{l2s} · F_spec         │                                │
│  │                                        │                                │
│  │    α_l2s = softmax(Q_l2s · K_l2s^T)   │                                │
│  │    F_struct' = F_struct + α_l2s·V_l2s │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    │                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │         Gated Fusion                   │                                │
│  │                                        │                                │
│  │    g = σ(W_g · [F_spec'; F_struct'])  │                                │
│  │    F_fused = g ⊙ F_spec' + (1-g) ⊙ F_struct'                          │
│  │                                        │                                │
│  │    Output: F_fused ∈ R^512             │                                │
│  └────────────────────────────────────────┘                                │
│                                                                             │
│  ADAPTIVE WEIGHTING:                                                        │
│  • Per-species learned gate biases                                         │
│  • Uncertainty-based modality weighting                                    │
│  • Attention visualization for interpretability                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Mathematical Formulation

**Cross-Attention (Spectral → Structural)**:
$$\mathbf{Q}_{s \to l} = \mathbf{F}_{spec} \mathbf{W}_Q^{s \to l}$$
$$\mathbf{K}_{s \to l} = \mathbf{F}_{struct} \mathbf{W}_K^{s \to l}$$
$$\mathbf{V}_{s \to l} = \mathbf{F}_{struct} \mathbf{W}_V^{s \to l}$$
$$\mathbf{F}'_{spec} = \mathbf{F}_{spec} + \text{softmax}\left(\frac{\mathbf{Q}_{s \to l} \mathbf{K}_{s \to l}^T}{\sqrt{d}}\right) \mathbf{V}_{s \to l}$$

**Gated Fusion**:
$$\mathbf{g} = \sigma\left(\mathbf{W}_g \left[\mathbf{F}'_{spec}; \mathbf{F}'_{struct}\right] + \mathbf{b}_g\right)$$
$$\mathbf{F}_{fused} = \mathbf{g} \odot \mathbf{F}'_{spec} + (1 - \mathbf{g}) \odot \mathbf{F}'_{struct}$$

### 3.4 Classification Head

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CLASSIFICATION HEAD                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Input: F_fused ∈ R^512                                                    │
│                                                                             │
│  ┌────────────────────────────────────────┐                                │
│  │    MLP Block 1                         │                                │
│  │    Linear(512 → 256) + BatchNorm       │                                │
│  │    ReLU + Dropout(0.5)                 │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │    MLP Block 2                         │                                │
│  │    Linear(256 → 128) + BatchNorm       │                                │
│  │    ReLU + Dropout(0.3)                 │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  ┌────────────────────────────────────────┐                                │
│  │    Output Layer                        │                                │
│  │    Linear(128 → K=25)                  │                                │
│  │    Softmax (for probabilities)         │                                │
│  └─────────────────┬──────────────────────┘                                │
│                    ▼                                                        │
│  Output: ŷ ∈ R^25 (species probabilities)                                  │
│          confidence = max(ŷ)                                               │
│          prediction = argmax(ŷ)                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Step-by-Step Algorithms

### Algorithm 1: HSI Preprocessing Pipeline

```
ALGORITHM: HSI_Preprocessing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT:  raw_hsi (H × W × B_raw), radiance calibration file, DEM
OUTPUT: processed_hsi (H × W × B), wavelengths (B,)

1:  FUNCTION HSI_Preprocessing(raw_hsi, calibration, dem):
2:      # Step 1: Radiometric Calibration
3:      radiance = raw_hsi * calibration.gain + calibration.offset
4:      
5:      # Step 2: Atmospheric Correction (FLAASH)
6:      reflectance = FLAASH_Correction(
7:          radiance, 
8:          sensor_altitude = 120m,  # UAV altitude AGL
9:          ground_elevation = dem,
10:         atmosphere_model = "tropical",
11:         aerosol_model = "rural"
12:     )
13:     
14:     # Step 3: Remove Bad Bands (water absorption)
15:     bad_bands = [b for b in range(B_raw) if 
16:                  wavelengths[b] in [1350-1450nm, 1800-1950nm]]
17:     good_hsi = remove_bands(reflectance, bad_bands)
18:     good_wavelengths = remove_wavelengths(wavelengths, bad_bands)
19:     
20:     # Step 4: Spectral Smoothing (Savitzky-Golay)
21:     smoothed_hsi = savgol_filter(good_hsi, window=7, order=2, axis=2)
22:     
23:     # Step 5: Normalization
24:     FOR each band b in range(B):
25:         mean_b = mean(smoothed_hsi[:,:,b])
26:         std_b = std(smoothed_hsi[:,:,b])
27:         normalized_hsi[:,:,b] = (smoothed_hsi[:,:,b] - mean_b) / std_b
28:     
29:     RETURN normalized_hsi, good_wavelengths

COMPLEXITY: O(H × W × B) time, O(H × W × B) space
FAILURE MODES:
  - Saturation in bright pixels → Mask and interpolate
  - Cloud shadows → Detect via shadow index; exclude from training
  - Sensor noise → Increase smoothing window
```

### Algorithm 2: LiDAR Point Cloud Processing

```
ALGORITHM: LiDAR_Processing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT:  raw_las (LAS file), roi (polygon)
OUTPUT: processed_points (N × D), chm (H' × W')

1:  FUNCTION LiDAR_Processing(raw_las, roi):
2:      # Step 1: Clip to ROI
3:      points = clip_to_polygon(raw_las, roi)
4:      
5:      # Step 2: Statistical Outlier Removal
6:      points = statistical_outlier_removal(
7:          points, k_neighbors=30, std_ratio=2.0
8:      )
9:      
10:     # Step 3: Ground Classification (CSF - Cloth Simulation Filter)
11:     ground_mask = csf_classify(
12:         points,
13:         cloth_resolution = 0.5,
14:         class_threshold = 0.5,
15:         iterations = 500
16:     )
17:     ground_points = points[ground_mask]
18:     
19:     # Step 4: Generate DTM from ground points
20:     dtm = interpolate_surface(ground_points, resolution=1.0)
21:     
22:     # Step 5: Height Normalization
23:     FOR each point p in points:
24:         p.z_normalized = p.z - dtm.sample(p.x, p.y)
25:     
26:     # Step 6: Generate CHM
27:     chm = grid_max(points.z_normalized, resolution=1.0)
28:     
29:     # Step 7: Feature Augmentation
30:     FOR each point p in points:
31:         p.intensity_norm = p.intensity / max_intensity
32:         p.return_ratio = p.return_number / p.num_returns
33:         p.height_class = classify_height(p.z_normalized)  # 0:ground, 1:understory, 2:canopy
34:     
35:     RETURN points, chm

COMPLEXITY: O(N log N) for ground classification, O(N) for normalization
FAILURE MODES:
  - Dense canopy → Low ground point density → Increase CSF iterations
  - Steep terrain → Ground misclassification → Use slope-adaptive threshold
  - Multi-path returns → Duplicate points → Filter by return number
```

### Algorithm 3: HyLiFormer Forward Pass

```
ALGORITHM: HyLiFormer_Forward
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT:  hsi_patch (P × P × B), point_cloud (N × D)
OUTPUT: class_probs (K,), features (C_fused,)

1:  FUNCTION HyLiFormer_Forward(hsi_patch, point_cloud):
2:      
3:      # ============ SPECTRAL ENCODING ============
4:      # 3D Convolution
5:      h1 = Conv3D(hsi_patch, W_conv1)    # (P-2, P-2, B-6, 32)
6:      h1 = BatchNorm3D(h1)
7:      h1 = ReLU(h1)
8:      
9:      h2 = Conv3D(h1, W_conv2)           # (P-4, P-4, B-10, 64)
10:     h2 = BatchNorm3D(h2)
11:     h2 = ReLU(h2)
12:     
13:     # Reshape for Transformer
14:     h_flat = Flatten_Spatial(h2)        # (S, B', 64) where S = spatial, B' = spectral
15:     
16:     # Group-wise Spectral Attention
17:     groups = Split_Spectral_Groups(h_flat, num_groups=30)
18:     FOR g in range(num_groups):
19:         Q_g = Linear(groups[g], W_Q)
20:         K_g = Linear(groups[g], W_K)
21:         V_g = Linear(groups[g], W_V)
22:         attn_g = Softmax(Q_g @ K_g.T / sqrt(d_k)) @ V_g
23:         groups[g] = groups[g] + attn_g
24:     
25:     h_grouped = Concat(groups)          # (S, G, d_group)
26:     
27:     # Transformer Encoder (4 layers)
28:     FOR layer in range(4):
29:         h_grouped = TransformerEncoderLayer(h_grouped)
30:     
31:     F_spec = GlobalAveragePool(h_grouped)  # (512,)
32:     
33:     # ============ STRUCTURAL ENCODING ============
34:     # Set Abstraction Level 1
35:     centroids_1 = FarthestPointSampling(point_cloud, n=512)
36:     groups_1 = BallQuery(point_cloud, centroids_1, radius=0.5, k=32)
37:     f_1 = PointNetMLP(groups_1)          # (512, 128)
38:     
39:     # Set Abstraction Level 2
40:     centroids_2 = FarthestPointSampling(centroids_1, n=128)
41:     groups_2 = BallQuery(f_1, centroids_2, radius=1.0, k=64)
42:     f_2 = PointNetMLP(groups_2)          # (128, 512)
43:     
44:     # Set Abstraction Level 3
45:     centroids_3 = FarthestPointSampling(centroids_2, n=32)
46:     groups_3 = BallQuery(f_2, centroids_3, radius=2.0, k=64)
47:     f_3 = PointNetMLP(groups_3)          # (32, 1024)
48:     
49:     # Global Aggregation
50:     f_max = GlobalMaxPool(f_3)           # (1024,)
51:     f_avg = GlobalAvgPool(f_3)           # (1024,)
52:     F_struct = MLP(Concat(f_max, f_avg)) # (512,)
53:     
54:     # ============ CROSS-MODAL FUSION ============
55:     # Spectral-to-Structural Attention
56:     Q_s2l = Linear(F_spec, W_Q_s2l)
57:     K_s2l = Linear(F_struct, W_K_s2l)
58:     V_s2l = Linear(F_struct, W_V_s2l)
59:     alpha_s2l = Softmax(Q_s2l @ K_s2l.T / sqrt(d))
60:     F_spec_prime = F_spec + alpha_s2l @ V_s2l
61:     
62:     # Structural-to-Spectral Attention
63:     Q_l2s = Linear(F_struct, W_Q_l2s)
64:     K_l2s = Linear(F_spec, W_K_l2s)
65:     V_l2s = Linear(F_spec, W_V_l2s)
66:     alpha_l2s = Softmax(Q_l2s @ K_l2s.T / sqrt(d))
67:     F_struct_prime = F_struct + alpha_l2s @ V_l2s
68:     
69:     # Gated Fusion
70:     gate = Sigmoid(Linear(Concat(F_spec_prime, F_struct_prime), W_gate))
71:     F_fused = gate * F_spec_prime + (1 - gate) * F_struct_prime
72:     
73:     # ============ CLASSIFICATION ============
74:     h = ReLU(BatchNorm(Linear(F_fused, 256)))
75:     h = Dropout(h, p=0.5)
76:     h = ReLU(BatchNorm(Linear(h, 128)))
77:     h = Dropout(h, p=0.3)
78:     logits = Linear(h, K)
79:     class_probs = Softmax(logits)
80:     
81:     RETURN class_probs, F_fused

COMPLEXITY: 
  - Spectral Encoder: O(P² × B × C) + O(S × G² × d) for attention
  - Structural Encoder: O(N log N) for FPS + O(N × k) for grouping
  - Fusion: O(C²) for cross-attention
  - Total: O(N log N + P² × B × C) ≈ O(N log N) for large point clouds

PARAMETERS:
  - Spectral Encoder: ~8M params
  - Structural Encoder: ~4M params  
  - Fusion + Classification: ~2M params
  - Total: ~14M params
```

### Algorithm 4: Training Loop

```
ALGORITHM: Train_HyLiFormer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT:  train_dataset, val_dataset, hyperparams
OUTPUT: trained_model, training_history

1:  FUNCTION Train_HyLiFormer(train_data, val_data, config):
2:      # Initialize
3:      model = HyLiFormer(config)
4:      optimizer = AdamW(model.parameters(), lr=config.lr, weight_decay=1e-4)
5:      scheduler = CosineAnnealingLR(optimizer, T_max=config.epochs)
6:      
7:      # Class weights for imbalanced data
8:      class_weights = compute_class_weights(train_data.labels)
9:      criterion = FocalLoss(alpha=class_weights, gamma=2.0)
10:     
11:     best_val_acc = 0
12:     patience_counter = 0
13:     
14:     FOR epoch in range(config.epochs):
15:         model.train()
16:         epoch_loss = 0
17:         
18:         # Training loop
19:         FOR batch in DataLoader(train_data, batch_size=32, shuffle=True):
20:             hsi_batch, lidar_batch, labels = batch
21:             
22:             # Data Augmentation
23:             hsi_batch = spectral_augment(hsi_batch)      # Random band dropout
24:             lidar_batch = point_augment(lidar_batch)    # Random jitter, rotation
25:             
26:             # Forward pass
27:             optimizer.zero_grad()
28:             probs, features = model(hsi_batch, lidar_batch)
29:             
30:             # Loss computation
31:             loss = criterion(probs, labels)
32:             
33:             # Backward pass
34:             loss.backward()
35:             torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
36:             optimizer.step()
37:             
38:             epoch_loss += loss.item()
39:         
40:         scheduler.step()
41:         
42:         # Validation
43:         val_acc, val_f1 = evaluate(model, val_data)
44:         
45:         # Early stopping check
46:         IF val_acc > best_val_acc:
47:             best_val_acc = val_acc
48:             save_checkpoint(model, "best_model.pth")
49:             patience_counter = 0
50:         ELSE:
51:             patience_counter += 1
52:             IF patience_counter >= config.patience:
53:                 PRINT("Early stopping triggered")
54:                 BREAK
55:         
56:         PRINT(f"Epoch {epoch}: Loss={epoch_loss:.4f}, Val_Acc={val_acc:.2%}")
57:     
58:     RETURN load_checkpoint("best_model.pth"), history

HYPERPARAMETERS:
  - Learning rate: 1e-4 (initial)
  - Batch size: 32
  - Epochs: 200 (max)
  - Early stopping patience: 20
  - Focal loss gamma: 2.0
  - Dropout: 0.5 (MLP), 0.1 (Attention)
  - Weight decay: 1e-4
```

---

## 5. Evaluation Design

### 5.1 Main Experiments

#### Experiment 1: Overall Classification Performance

**Objective**: Validate HyLiFormer achieves target accuracy on MeghalayaForest-25

| Parameter | Setting |
|-----------|---------|
| Dataset | Full MeghalayaForest-25 (25 species) |
| Split | 60% train / 20% val / 20% test (stratified) |
| Spatial blocking | 500m buffer between train/test |
| Repetitions | 5 runs with different seeds |
| Metrics | OA, Kappa, Macro-F1, per-class F1 |

**Baseline Comparisons**:
- B1: RF + Spectral Features
- B2: SVM-RBF + PCA
- B3: XGBoost + Engineered Features
- B4: 3D-CNN (Li et al., 2017)
- B5: HybridSN (Roy et al., 2020)
- B6: SpectralFormer (Hong et al., 2022)

#### Experiment 2: Cross-Site Generalization

**Objective**: Assess model transferability across forest types

| Parameter | Setting |
|-----------|---------|
| Sites | Site A (subtropical), Site B (semi-evergreen), Site C (pine) |
| Protocol | Leave-one-site-out cross-validation |
| Domain adaptation | Fine-tuning vs adversarial vs no adaptation |
| Metrics | OA per site, accuracy drop from in-site |

#### Experiment 3: Satellite Scaling

**Objective**: Evaluate performance degradation from UAV to satellite

| Parameter | Setting |
|-----------|---------|
| Resolution levels | 1m (UAV) → 4m (AVIRIS-NG) → 30m (HySIS) |
| Spectral resampling | UAV (224 bands) → AVIRIS-NG (425) → HySIS (55) |
| Domain adaptation | Fine-tuning, adversarial, spectral matching |
| Metrics | OA at each scale, correlation with UAV predictions |

### 5.2 Ablation Studies

| ID | Ablation | Hypothesis | Expected Result |
|----|----------|------------|-----------------|
| A1 | Remove LiDAR (HSI only) | LiDAR adds structural information | -5-8% OA |
| A2 | Remove HSI (LiDAR only) | HSI provides species-specific signatures | -10-15% OA |
| A3 | Replace cross-attention with concatenation | Attention learns optimal fusion | -3-5% OA |
| A4 | Replace Transformer with CNN encoder | Transformer captures long-range | -2-4% OA |
| A5 | Remove group-wise spectral attention | GSA captures local spectral continuity | -2-3% OA |
| A6 | Reduce spectral bands (224→100→50) | Identify minimum spectral requirement | <-2% until 100 bands |

### 5.3 Statistical Tests

**Pairwise Comparisons** (McNemar's Test):
$$\chi^2 = \frac{(|n_{01} - n_{10}| - 1)^2}{n_{01} + n_{10}}$$

where $n_{01}$ = samples correct by baseline, wrong by HyLiFormer
      $n_{10}$ = samples wrong by baseline, correct by HyLiFormer

**Significance threshold**: p < 0.05 with Bonferroni correction

**Confidence Intervals** (Bootstrap):
- 1000 bootstrap samples of test set
- Report 95% CI for OA, Kappa, Macro-F1

---

## 6. Threats to Validity & Mitigation

### 6.1 Threat Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        THREAT MODEL                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  INTERNAL VALIDITY                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │  Overfitting                                                     │       │
│  │    ├── Spatial autocorrelation → Spatial blocking               │       │
│  │    ├── Small sample size → Data augmentation                    │       │
│  │    └── Model complexity → Regularization, early stopping        │       │
│  │                                                                  │       │
│  │  Label Noise                                                     │       │
│  │    ├── Misidentification → Expert verification                  │       │
│  │    └── GPS error → High-precision GNSS                          │       │
│  │                                                                  │       │
│  │  Confounders                                                     │       │
│  │    ├── Illumination variation → Atmospheric correction          │       │
│  │    └── Phenological stage → Multi-season data                   │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  EXTERNAL VALIDITY                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │  Geographic Limitation                                           │       │
│  │    └── 3 districts only → Diverse site selection                │       │
│  │                                                                  │       │
│  │  Temporal Limitation                                             │       │
│  │    └── Single season → Document phenological stage              │       │
│  │                                                                  │       │
│  │  Sensor Specificity                                              │       │
│  │    └── UAV sensors differ from satellites → Domain adaptation   │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  CONSTRUCT VALIDITY                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │  Species Definition                                              │       │
│  │    └── Taxonomic ambiguity → Follow regional flora              │       │
│  │                                                                  │       │
│  │  Ground Truth Quality                                            │       │
│  │    └── Expert disagreement → Multiple botanists, consensus      │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Mitigation Strategies Summary

| Threat | Strategy | Implementation |
|--------|----------|----------------|
| Spatial autocorrelation | Spatial blocking | 500m buffer between train/test |
| Small sample size | Augmentation | Spectral noise, rotation, mixup |
| Label noise | Expert verification | 2+ botanists; voucher specimens |
| Illumination | Atmospheric correction | FLAASH with local parameters |
| Sensor shift | Domain adaptation | Adversarial training; fine-tuning |
| Taxonomic ambiguity | Regional flora | Follow Botanical Survey of India |

---

## 7. ISRO Format B-5 & B-6 Drafts

### Format B-5: Approach/Methodology

**Data Acquisition**:
1. UAV campaigns across 3 districts using DJI M600 Pro platform
2. Hyperspectral sensor: VNIR-SWIR (380-2500nm, 224 bands, 1m GSD)
3. LiDAR sensor: Multi-return, 50+ points/m², 0.03m vertical accuracy
4. Minimum 15 flights per site covering 50+ ha each

**Processing Pipeline**:
1. Radiometric and atmospheric correction of HSI
2. LiDAR ground classification and height normalization
3. Co-registration to common coordinate system (sub-pixel accuracy)
4. Training sample extraction at field plot locations

**Deep Learning Framework**:
1. HyLiFormer architecture: CNN-Transformer hybrid for HSI + PointNet++ for LiDAR
2. Cross-modal attention fusion for adaptive feature combination
3. Training with focal loss and data augmentation
4. Spatial cross-validation for robust evaluation

**Validation**:
1. 500+ field plots with expert species identification
2. Stratified sampling across forest types
3. Independent test set with spatial blocking
4. Statistical significance testing (McNemar's test)

### Format B-6: Data Reduction/Analysis

**Input Data Volumes**:
- HSI: ~50 GB per site (1m resolution, 224 bands)
- LiDAR: ~100 GB per site (50 pts/m²)
- Total raw data: ~450 GB for 3 sites

**Processing Outputs**:
- Preprocessed HSI: ~15 GB per site
- Processed point clouds: ~30 GB per site
- Training samples: ~2 GB (patches + points)

**Model Outputs**:
- Species classification maps (25 classes)
- Confidence maps (per-pixel uncertainty)
- Attention visualizations (interpretability)

**DSS Integration**:
- GeoTIFF format for GIS compatibility
- Web mapping service for Bhuvan integration
- API endpoints for programmatic access

---

## Phase Status
**PHASE 3: TECHNICAL DEEP DIVE COMPLETE** ✓

**→ Proceed to PHASE 4: Section-by-Section Drafts**
