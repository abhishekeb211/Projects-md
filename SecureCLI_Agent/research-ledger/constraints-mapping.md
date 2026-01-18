# Research Scope & Constraint Mapping

**Version:** 1.0  
**Date:** Week 0  
**Status:** Initial Mapping

---

## 1. Code Size Constraints (50K+ LOC)

### Language Breakdown Targets

| Language/Ecosystem | Target LOC | Rationale | Priority |
|-------------------|------------|-----------|----------|
| Node.js/TypeScript | 15,000 LOC | High adoption, npm ecosystem vulnerabilities | P0 |
| Python | 12,000 LOC | Common in ML/data teams, dependency issues | P0 |
| Go | 10,000 LOC | Infrastructure code, static analysis needs | P1 |
| Java | 8,000 LOC | Enterprise codebases, Maven/Gradle scans | P1 |
| Terraform/IaC | 5,000 LOC | Infrastructure-as-Code security critical | P0 |

**Total Target:** 50,000 LOC minimum  
**Measurement Method:** `cloc` or `tokei` tool per repository  
**Validation:** Run LOC counts on 50 baseline repos; ensure ≥50K total

---

## 2. Scan Run Targets (10,000+ Scan Runs)

### Daily/Weekly Scan Quotas

| Team Category | Teams | Scans/Week per Team | Total Scans/Week | Annual Target |
|--------------|-------|---------------------|------------------|---------------|
| High-activity teams (P0 repos) | 5 | 40 scans | 200 | 10,400 |
| Medium-activity teams | 10 | 20 scans | 200 | 10,400 |
| Low-activity teams | 5 | 8 scans | 40 | 2,080 |
| **Total** | **20** | **Varies** | **440/week** | **22,880/year** |

**Note:** 10,000 scans = ~6 months at 440 scans/week, or 1 year at 192 scans/week

### Distribution Assumptions
- **Per-repo frequency:** Average 4 scans/week (daily CI + manual)
- **Peak periods:** Sprint ends may see 2× frequency
- **Holiday/lull periods:** 0.5× frequency acceptable

**Validation Method:** Monitor CI/CD integration logs; track scan invocation counts via AegisCLI telemetry

---

## 3. Air-Gapped Environment Technical Specs

### Network Constraints
- **Outbound Network:** Blocked (no external API calls after initial setup)
- **Inbound Network:** Blocked (no cloud services, no telemetry uploads)
- **Local Network:** Allowed (within organization firewall)
- **USB Transfer:** Allowed (for model distribution, artifact updates)

### Ollama Local Model Cache Requirements
- **Model Storage:** ~7GB per model (CodeLlama 13B Q4_K_M)
- **Cache Location:** `/var/lib/ollama/models/` (configurable via `OLLAMA_MODELS` env var)
- **Pre-deployment:** Models must be downloaded and transferred via USB/internal network before air-gap activation
- **Update Mechanism:** Manual USB transfer of new model versions (quarterly updates expected)

### Deployment Specifications
- **Installation Method:** Static Go binaries + Ollama binary (no internet required post-install)
- **Configuration:** YAML config files (no cloud-based config services)
- **Database:** Local PostgreSQL instance (no cloud DB connections)
- **Artifact Distribution:** Via internal artifact repository or USB drives

**Validation Test:** Deploy AegisCLI on isolated Ubuntu 22.04 VM (network disabled) and verify full functionality

---

## 4. Critical Feasibility Risks

### Risk 1: GPU Availability for CodeLlama 13B

**Probability:** Medium (60%)  
**Impact:** High (blocks LLM triage feature)  
**Risk Score:** 18/25 (High Risk)

**Description:**
- CodeLlama 13B requires GPU (8GB+ VRAM) for acceptable inference speed (<5s per finding)
- Air-gapped environments may not have GPU infrastructure
- CPU-only inference is 10-20× slower, making real-time triage impractical

**Mitigation Strategy:**
- **Primary:** Pre-validate GPU availability on target air-gap systems (Week 1)
- **Backup Plan 1:** Use quantized smaller model (CodeLlama 7B) if GPU unavailable (accuracy tradeoff: κ may drop to 0.70)
- **Backup Plan 2:** Batch processing (queue findings, process overnight) if CPU-only required
- **Backup Plan 3:** Hybrid approach: Critical findings → GPT-4 API (with privacy waiver), others → CPU CodeLlama

**Owner:** Engineering Lead  
**Timeline:** GPU validation by Week 2; fallback decision by Week 3

---

### Risk 2: Scanner API Churn

**Probability:** Medium (50%)  
**Impact:** Medium (requires adapter updates)  
**Risk Score:** 12.5/25 (Medium Risk)

**Description:**
- Scanner tools (semgrep, trivy, checkov) update frequently; SARIF output format may change
- Breaking changes could break AegisCLI scanner adapters
- May cause delays in research timeline if adapters need rewriting

**Mitigation Strategy:**
- **Primary:** Pin scanner versions in baseline (semgrep v1.45.0, trivy v0.48.0, checkov v3.0.0)
- **Backup Plan 1:** Version compatibility matrix (test new versions quarterly, update adapters if needed)
- **Backup Plan 2:** SARIF schema validation (fail-fast if format unexpected)
- **Backup Plan 3:** Maintain fork/patched versions of scanners if upstream breaks compatibility

**Owner:** Engineering Lead  
**Timeline:** Version pinning in Week 1; quarterly compatibility tests

---

### Risk 3: Champion Attrition

**Probability:** Low (30%)  
**Impact:** High (reduces adoption data quality)  
**Risk Score:** 9/25 (Medium Risk)

**Description:**
- Security champions may leave organization, change roles, or lose engagement
- Champion effect (H4) requires consistent champion presence over 12 months
- Loss of champions in P2-P4 phases could reduce statistical power for E4 experiment

**Mitigation Strategy:**
- **Primary:** Identify backup champions (2 per team) at P0; rotate if primary champion unavailable
- **Backup Plan 1:** Champion training program (standardize knowledge, reduce dependency on individuals)
- **Backup Plan 2:** Adjust E4 design to use "champion-months" as exposure variable (handles partial participation)
- **Backup Plan 3:** Expand sample size by 20% (buffer for attrition) - recruit 24 teams instead of 20

**Owner:** Research Lead  
**Timeline:** Backup champion identification by Week 4; attrition monitoring monthly

---

## 5. Risk Matrix

| Risk ID | Risk Description | Probability | Impact | Risk Score | Mitigation Owner | Status |
|---------|------------------|-------------|--------|------------|------------------|--------|
| R1 | GPU Availability | Medium (60%) | High | 18/25 | Engineering Lead | Monitoring |
| R2 | Scanner API Churn | Medium (50%) | Medium | 12.5/25 | Engineering Lead | Mitigated (version pinning) |
| R3 | Champion Attrition | Low (30%) | High | 9/25 | Research Lead | Mitigated (backup champions) |

**Risk Score Calculation:** Probability (1-5 scale) × Impact (1-5 scale) = Risk Score (1-25 scale)

**Risk Thresholds:**
- **Critical (20-25):** Immediate action required
- **High (12-19):** Mitigation plan active, monitor weekly
- **Medium (6-11):** Mitigation plan defined, monitor monthly
- **Low (1-5):** Acceptable risk, monitor quarterly

---

## 6. Additional Constraints & Boundaries

### Time Constraints
- **Phase 0-1 (Setup):** 4 weeks
- **Phase 2 (SLR):** 8 weeks
- **Phase 3-4 (Development & Evaluation):** 32 weeks
- **Phase 5-7 (Writing & Submission):** 16 weeks
- **Total Timeline:** 60 weeks (~15 months)

### Resource Constraints
- **Engineering Team:** 2-3 engineers part-time (50% allocation)
- **Research Team:** 2 researchers full-time
- **Infrastructure:** Shared (no dedicated GPU clusters; must use existing air-gap systems)

### Data Constraints
- **Privacy:** No code snippets >5 lines in telemetry (redaction required)
- **Consent:** IRB approval required for interviews; opt-in telemetry for teams
- **Retention:** 90-day rolling window for telemetry data (policy TBD)

---

## Summary

All constraints have been mapped to quantifiable metrics with validation methods. Three critical risks identified with mitigation strategies and assigned owners. Risk matrix shows R1 (GPU) as highest priority for monitoring.

