# AegisCLI Research Ledger v0
**Version:** 0.1  
**Last Updated:** Week 0  
**Status:** Initial Setup

---

## 1. Definitions

### MTTR (Mean Time To Remediate)
- **Definition:** Average time from when a security finding is detected to when it is fully remediated and verified.
- **Measurement Unit:** Hours (or days for long-running issues)
- **Formula:** `MTTR = Σ(remediation_time - detection_time) / n_findings`
- **Baseline Target:** Measure pre-AegisCLI MTTR from 50-repo dataset

### Security Debt
- **Definition:** Accumulated unresolved security findings that represent technical debt requiring future remediation effort.
- **Measurement Unit:** Count of unresolved findings weighted by severity (Critical=4, High=3, Medium=2, Low=1)
- **Formula:** `Security Debt = Σ(finding_count × severity_weight)`
- **Tracking Method:** Quarterly snapshots comparing debt velocity (rate of accumulation vs. remediation)

### Tool Sprawl
- **Definition:** The proliferation of multiple disconnected security scanning tools requiring manual context-switching by developers.
- **Measurement Unit:** 
  - Count of distinct tools per team
  - Average context-switch time (minutes) between tools
  - Overhead percentage = (tool_switch_time / total_scan_time) × 100
- **Baseline Metric:** From 50-repo survey, measure average tools per team and switch overhead

### Agentic AI
- **Definition:** AI system that autonomously orchestrates multiple actions (scanner invocation, result normalization, triage decision-making) within defined policy boundaries.
- **Key Characteristics:** 
  - Autonomy level: Orchestration (not autonomous code changes)
  - Decision boundaries: Policy-as-Code rules + confidence thresholds
  - Human-in-the-loop triggers: Low confidence (<0.8) or policy violations

---

## 2. Baselines

### Pre-AegisCLI Scan Times
- **Data Source:** CI/CD logs from 50 target repositories (prior to AegisCLI integration)
- **Collection Period:** Last 6 months (if available) or next 2 weeks during P0
- **Metrics:**
  - Average scan duration per repository: `[TBD - collect during P0]`
  - Tool switch overhead time: `[TBD - measured via developer surveys]`
  - Total pipeline time including security scans: `[TBD]`

### False Positive Rates from 50 Repos
- **Data Source:** Manual annotation of findings from 50 repos baseline scan
- **Collection Method:** Stratified sample (50 findings per severity level = 200 total)
- **Metrics:**
  - Overall FP rate: `[TBD - target baseline <30%]`
  - FP rate by scanner: `semgrep=[TBD], trivy=[TBD], checkov=[TBD]`
  - FP rate by severity: `CRITICAL=[TBD], HIGH=[TBD], MEDIUM=[TBD], LOW=[TBD]`
- **Gold Standard:** 3 senior security engineers, independent labeling, consensus via majority vote

---

## 3. Assumptions

### CodeLlama Accuracy
- **Assumption:** CodeLlama 13B (via Ollama) achieves κ ≥ 0.75 inter-annotator agreement with expert security panel for severity triage.
- **Rationale:** Based on preliminary tests on 20 sample findings (informal, not yet validated)
- **Validation Method:** Module 3.4 Experiment E2 with 200 stratified findings
- **Risk if False:** Fallback to GPT-4 API (privacy tradeoff) or manual triage only

### Policy-as-Code (PaC) Effectiveness
- **Assumption:** OPA/Rego policies reduce security debt accumulation by ≥40% compared to manual policy enforcement.
- **Rationale:** DORA metrics show automation typically improves MTTR by 30-50%
- **Validation Method:** Module 3.4 Experiment E3 (A/B: PaC-enabled vs. manual teams)
- **Risk if False:** Re-evaluate PaC rule complexity; consider hybrid manual+automated approach

### Champion Effect
- **Assumption:** Teams with designated security champions show ≥25% faster MTTR than teams without champions.
- **Rationale:** BSIMM studies show champion programs improve security culture
- **Validation Method:** Module 3.4 Experiment E4 (correlate champion presence with MTTR)
- **Risk if False:** Champion identification criteria may need refinement; effect may be confounded with team maturity

---

## 4. Decisions Log

| Date | Decision | Rationale | Impact | Owner |
|------|----------|-----------|--------|-------|
| Week 0 | Use SARIF v2.1.0 as normalization schema | Industry standard, tool ecosystem support | Enables scanner agnosticism | Engineering Lead |
| Week 0 | CodeLlama 13B over GPT-4 for triage | Privacy (air-gap requirement), cost, reproducibility | Local deployment complexity; may need GPU | Research Lead |
| Week 0 | OPA/Rego for Policy-as-Code | Maturity, performance, open-source | Team must learn Rego syntax | Engineering Lead |
| Week 0 | Go language for CLI core | Concurrency, static binaries (air-gap), performance | Faster development; easier deployment | Engineering Lead |
| Week 0 | 50 repos as baseline dataset | Statistical power (50 repos × 20 commits = 1000 points) | Requires access agreements from 50 repo owners | Research Lead |
| Week 0 | Ollama as LLM runtime | Local-first, no cloud dependencies | Must pre-download models for air-gap | Engineering Lead |
| Week 0 | PostgreSQL + Grafana for dashboard | Open-source, SQL queries for metrics | Requires DB infrastructure setup | Engineering Lead |

---

## 5. Locked Parameters

### Scope
- **Geographic:** Single organization (large-scale, Microsoft-like)
- **Languages:** 5 ecosystems (Node.js, Python, Go, Java, Terraform/IaC)
- **Time Horizon:** 12-month longitudinal study (P0-P4 phases)
- **Team Size:** 500+ engineers, 20+ teams
- **Repository Count:** 50+ repos for baseline, 10+ repos for deep evaluation

### LLM Model
- **Primary:** CodeLlama 13B (quantized, via Ollama)
- **Fallback:** GPT-4 API (only if CodeLlama κ < 0.70, with privacy waiver)
- **Quantization:** Q4_K_M (balance of size vs. accuracy)
- **Context Window:** 4096 tokens (5-shot prompts + finding context)

### Normalization Schema
- **Standard:** SARIF v2.1.0 (OASIS standard)
- **Subset:** Full result objects, rule metadata, location (file/line), severity
- **Extensions:** Custom properties for AegisCLI metadata (confidence, policy_decision, champion_review_flag)

---

## 6. Dependencies

### Scanner Versions
- **semgrep:** v1.45.0+ (SARIF output support)
- **trivy:** v0.48.0+ (SARIF v2.1.0)
- **checkov:** v3.0.0+ (SARIF support)
- **gitleaks:** v8.18.0+ (for secret redaction before LLM context)
- **Note:** Test compatibility with latest versions quarterly; pin versions for reproducibility

### Ollama Version
- **Required:** v0.1.15+ (CodeLlama 13B support)
- **Model:** `codellama:13b` (pinned via `ollama pull codellama:13b`)
- **Storage:** ~7GB per model (Q4_K_M quantization)

### Go Version
- **Required:** Go 1.21+ (for CLI core, scanner adapters)
- **Rationale:** Static binary generation, cross-platform support
- **Build Target:** Linux amd64, Windows amd64 (for air-gap deployments)

### Other Dependencies
- **OPA:** v0.60.0+ (Rego policy engine)
- **Redis:** v7.0+ (optional, for policy decision caching)
- **PostgreSQL:** v15+ (for dashboard/metrics DB)

---

## 7. Placeholders & Future Updates

### 90-Day Rolling Telemetry Policy
- **Status:** [Placeholder - to be defined in Week 2]
- **Policy Document:** `docs/telemetry-policy.md`
- **Requirements:** Opt-in consent, data retention limits, anonymization rules

### IRB Consent Form References
- **Status:** [Placeholder - IRB submission pending]
- **Document ID:** [TBD after IRB approval]
- **Consent Scope:** Interview participants (champions), telemetry opt-in for teams

---

