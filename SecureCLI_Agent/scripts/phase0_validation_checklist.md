# Phase 0 Validation Checklist

Use this checklist to track completion of Phase 0 validation tasks.

## Week 1 Checklist

### Day 1: Directory & File Setup
- [ ] Research ledger directory created (`research-ledger/`)
- [ ] Research Ledger v0 exported to `research-ledger/ledger-v0.md`
- [ ] Constraints mapping exported to `research-ledger/constraints-mapping.md`
- [ ] Documentation directory created (`docs/`)

### Day 2-3: LOC Count Validation
- [ ] Install `cloc` or `tokei` tool
- [ ] Run LOC count on 50 baseline repositories
- [ ] Verify ≥50K LOC total
- [ ] Verify language breakdown targets:
  - [ ] Node.js/TypeScript: ≥15,000 LOC
  - [ ] Python: ≥12,000 LOC
  - [ ] Go: ≥10,000 LOC
  - [ ] Java: ≥8,000 LOC
  - [ ] Terraform/IaC: ≥5,000 LOC
- [ ] Document actual LOC counts in `research-ledger/constraints-mapping.md`
- [ ] Run: `python scripts/validate_loc_counts.py --repos-dir /path/to/repos --output loc_report.json`

### Day 3-5: Scanner Version Pinning
- [ ] Install semgrep v1.45.0+
- [ ] Install trivy v0.48.0+
- [ ] Install checkov v3.0.0+
- [ ] Install gitleaks v8.18.0+
- [ ] Test SARIF output for each scanner
- [ ] Document version pinning in research ledger
- [ ] Run: `python scripts/validate_scanner_versions.py --output scanner_validation.json`

### Day 5: Ollama Model Setup
- [ ] Install Ollama v0.1.15+
- [ ] Download CodeLlama 13B: `ollama pull codellama:13b`
- [ ] Verify model size (~7GB)
- [ ] Test model inference with sample prompt
- [ ] Pre-download models for air-gap deployment

### Day 1-5: GPU Availability Check
- [ ] Identify target air-gap systems
- [ ] Check GPU availability (nvidia-smi or lspci)
- [ ] Verify GPU has 8GB+ VRAM
- [ ] Test CodeLlama 13B inference speed (<5s target)
- [ ] Document GPU validation results
- [ ] Run: `python scripts/validate_gpu.py --output gpu_validation.json`

## Week 2 Checklist

### Day 1-2: GPU Validation Complete
- [ ] GPU validation results documented
- [ ] If GPU unavailable: Make fallback decision (CodeLlama 7B or batch processing)
- [ ] Update research ledger with GPU status

### Day 3-5: Air-Gap Deployment Test
- [ ] Set up isolated Ubuntu 22.04 VM (network disabled)
- [ ] Install AegisCLI (static Go binaries + Ollama binary)
- [ ] Transfer Ollama models via USB/internal network
- [ ] Verify scanner execution (semgrep, trivy, checkov)
- [ ] Verify SARIF normalization
- [ ] Verify LLM triage (CodeLlama via Ollama)
- [ ] Verify policy evaluation (OPA/Rego)
- [ ] Verify dashboard (PostgreSQL + Grafana)
- [ ] Document deployment test results

### Week 2: Telemetry Policy
- [ ] Review telemetry policy template
- [ ] Customize policy for organization
- [ ] Get IRB review/approval
- [ ] Finalize `docs/telemetry-policy.md`
- [ ] Update research ledger with policy reference

### Week 2-3: IRB Application
- [ ] Prepare IRB application
- [ ] Include interview protocol (champion interviews)
- [ ] Include telemetry opt-in consent process
- [ ] Submit IRB application
- [ ] Get IRB approval document ID
- [ ] Update research ledger with IRB document ID

## Week 1-4: Ongoing Tasks

### Champion Identification
- [ ] Identify primary security champions for 20 teams
- [ ] Identify backup champions (2 per team)
- [ ] Document champion identification criteria
- [ ] Set up monthly attrition monitoring

### Scan Run Monitoring Setup
- [ ] Identify 20 teams for tracking
- [ ] Set up CI/CD log monitoring
- [ ] Implement scan invocation counter in AegisCLI
- [ ] Verify scan quotas (440 scans/week target)

### Baseline Data Collection (Ongoing)
- [ ] Collect pre-AegisCLI scan times from CI/CD logs
- [ ] Measure false positive rates (200 findings, 3 engineers)
- [ ] Calculate FP rates: overall, by scanner, by severity
- [ ] Document baseline metrics in research ledger

## Validation Scripts Usage

### LOC Count Validation
```bash
python scripts/validate_loc_counts.py \
  --repos-dir /path/to/50/repos \
  --output loc_report.json \
  --tool cloc
```

### Scanner Version Validation
```bash
python scripts/validate_scanner_versions.py \
  --output scanner_validation.json
```

### GPU Validation
```bash
python scripts/validate_gpu.py \
  --output gpu_validation.json
```

## Quality Gates

Before proceeding to Phase 1, ensure:
- ✅ LOC count validation: ≥50K LOC confirmed
- ✅ Scanner versions: All pinned and SARIF-compatible
- ✅ GPU validation: Complete (pass or fallback decision made)
- ✅ Ollama setup: Model downloaded and tested
- ✅ Air-gap test: All components functional (or issues documented)
- ✅ Telemetry policy: Created and IRB-reviewed
- ✅ IRB application: Submitted (approval pending acceptable)

## Notes

- All validation scripts output JSON reports for documentation
- Update research ledger after each validation task
- Document any deviations from expected results
- Keep validation reports for Phase 3-4 evaluation design

