# **Phase-Wise Prompt System for AegisCLI Q1 Journal Paper**

Below is the **executable prompt sequence** for a research agent to generate a Q1-tier (IEEE TSE/TOSEM) manuscript from the AegisCLI framework. Each phase contains sub-modules with concrete deliverables and quality gates.

---

## **PHASE 0: Project Initialization & Research Ledger Setup**

### **Module 0.1: Research Ledger Foundation**
**Prompt:**
```
Initialize the AegisCLI Research Ledger as a living markdown document. Create sections:
- Definitions (MTTR, Security Debt, Tool Sprawl, Agentic AI)
- Baselines (Pre-AegisCLI scan times, FP rates from 50 repos)
- Assumptions (CodeLlama accuracy, PaC effectiveness, Champion effect)
- Decisions Log (with date, decision, rationale, impact)
- Locked Parameters (scope, LLM model, normalization schema)
- Dependencies (scanner versions, Ollama version, Go version)

Populate with Week 0 decisions from Section J. Add placeholders for 90-day rolling telemetry policy and IRB consent form references. Output: `research-ledger/ledger-v0.md`
```

**Quality Gate:** All terms defined with measurable units; baselines include data source paths.

---

### **Module 0.2: Research Scope & Constraint Mapping**
**Prompt:**
```
Map the user-defined constraints to executable boundaries:
- Translate "50K+ LOC" into specific language breakdown targets (Node.js: 15K, Python: 12K, etc.)
- Convert "10,000+ scan runs" into daily/weekly scan quotas per team
- Define "air-gapped environment" technical specs (no outbound network, Ollama local model cache)
- Identify 3 critical feasibility risks (GPU availability, scanner API churn, champion attrition)
- Propose mitigation strategies for each risk with backup plans

Output: `research-ledger/constraints-mapping.md` with risk matrix (Probability × Impact)
```

**Quality Gate:** Each constraint has a quantifiable metric and risk mitigation with assigned owner.

---

## **PHASE 1: Idea Refinement & Research Foundation**

### **Module 1.1: Problem Deconstruction & Stakeholder Analysis**
**Prompt:**
```
Deconstruct the AegisCLI problem into 4 socio-technical layers:
1. Technical: Tool sprawl metrics (count distinct tools, context-switch time)
2. Organizational: Security champion identification criteria and engagement model
3. Privacy: Data exfiltration risk assessment matrix for cloud tools
4. Economic: MTTR cost model (developer hours × hourly rate)

For each layer, identify primary stakeholders, their pain points (quote-style), and success metrics. Use the 50-repo baseline data to anchor pain points in real observations.

Output: `01-problem-deconstruction.md` with stakeholder matrix (Role | Pain Point | Desired Outcome | Metric)
```

**Quality Gate:** At least 3 pain points per stakeholder with verifiable baseline data.

---

### **Module 1.2: Gap Statement Formulation**
**Prompt:**
```
Write 3 versions of the gap statement for different audiences:
1. **Technical (for TSE reviewers):** Focus on normalization inefficiencies and local LLM orchestration gaps
2. **Impact (for broader SE community):** Emphasize privacy-preserving AI and security debt reduction
3. **Executive (for industry practitioners):** Highlight MTTR and compliance cost savings

Each version must follow the template: "Current approaches to [problem] typically [pattern], but struggle with [limitations]. We propose [approach] to achieve [measurable improvements] under [constraints]."

Output: `01-gap-statements.md` with version 1 marked as primary.
```

**Quality Gate:** Each statement includes 1 measurable improvement and 1 explicit constraint.

---

### **Module 1.3: Research Questions Formalization**
**Prompt:**
```
Formalize RQ1-RQ5 with null hypotheses, independent/dependent variables, and expected outcomes:

**RQ2 (Example):**
- Null Hypothesis (H0): CodeLlama triage accuracy κ ≤ 0.75 vs. expert panel
- Independent Variable: Triage method (CodeLlama vs. GPT-4 vs. Human)
- Dependent Variable: Cohen's kappa inter-annotator agreement
- Expected Outcome: Reject H0, κ = 0.78 (±0.05)
- Data Collection: 200 stratified findings × 3 experts × 2 LLMs

Create similar formalizations for RQ1, RQ3, RQ4, RQ5. Include data collection instrument details (log parser scripts, interview protocol IDs).

Output: `01-research-questions.md` with hypothesis table
```

**Quality Gate:** Each RQ has falsifiable hypothesis, defined variables, and data collection plan.

---

### **Module 1.4: Contribution Claims & Title Architecture**
**Prompt:**
```
Define 4 contribution claims aligned to TSE expectations:
1. **Methodological:** Novel agentic architecture (cite DSR Hevner 2004)
2. **Empirical:** 12-month longitudinal study with 500 engineers (largest known)
3. **Artifact:** Production-grade OSS with 50K LOC (complexity metric: 5 language ecosystems)
4. **Theoretical:** ST-SSDLC extension for local-first AI

For each claim, specify:
- Novelty level (incremental vs. breakthrough)
- Evidence type (quantitative metric, qualitative theme, artifact link)
- Comparison baseline (prior work from SLR)

Generate 5 title options following IEEE TSE patterns:
- [Colon format]: "AegisCLI: [subtitle]"
- [Impact format]: "Reducing MTTR by 80% with..."
- [Method format]: "A Design Science Study of..."

Output: `01-contributions-titles.md` with preferred title marked.
```

**Quality Gate:** Each claim has a unique evidence source; titles are under 12 words.

---

### **Module 1.5: Paper Outline & Research Ledger v1**
**Prompt:**
```
Create a detailed outline where each section maps to:
- Word count targets (Introduction: 1200 words, Related Work: 1800 words, etc.)
- Required figures/tables (with planned captions)
- Citation budget (min/max per section)
- Research Phase dependency (e.g., Section 6 requires P3 data)

Use IEEE TSE structure:
1. Introduction
2. Background & Related Work
3. Design Science Methodology
4. Architecture
5. Implementation & Phases
6. Evaluation
7. Discussion
8. Threats to Validity
9. Conclusion

Update Research Ledger with locked decisions from Modules 1.1-1.4.

Output: `01-paper-outline.md` and `research-ledger/ledger-v1.md`
```

**Quality Gate:** Outline accounts for 15,000-21,000 word target; each section has deliverable dependencies.

---

## **PHASE 2: Systematic Literature Review (SLR)**

### **Module 2.1: SLR Protocol & Search Strategy**
**Prompt:**
```
Formalize the SLR protocol following Kitchenham 2007 guidelines:

**Search Sources:** IEEE Xplore, ACM DL, Springer LNCS, arXiv, Google Scholar
**Search Strings per Cluster:**
- Cluster 1 (Orchestration): ("SARIF" OR "normalized") AND ("SAST" OR "scanner")
- Cluster 2 (AI Triage): ("LLM" OR "large language model") AND ("vulnerability" OR "security") AND ("triage" OR "classification")
- Cluster 3 (PaC): ("policy as code" OR "Rego") AND ("security debt" OR "MTTR")
- Cluster 4 (Adoption): ("DevSecOps" OR "security champion") AND ("adoption" OR "MTTR")
- Cluster 5 (Privacy): ("local AI" OR "air gap") AND ("security" OR "SAST")

**Inclusion/Exclusion Criteria Table:**
- Include: 2019-2024, empirical, multi-language, artifact available
- Exclude: Surveys without data, commercial whitepapers, <5 pages

**Quality Assessment:** 0-3 rubric (relevance, rigor, reproducibility, citations)

Output: `02-slr-protocol.md` with PRISMA flowchart (planned)
```

**Quality Gate:** Protocol includes pilot search test (first 50 papers) to validate string precision/recall.

---

### **Module 2.2: Paper Collection & Screening Pipeline**
**Prompt:**
```
Implement a semi-automated screening pipeline:

1. **Export Phase:** Use IEEE/ACM APIs to download first 200 results to Zotero
2. **Deduplication:** Use Zotero duplicate merge; manual check 10% sample
3. **Title/Abstract Screening:** Create Google Form for independent screening by 2 team members
4. **Full-Text Screening:** Build screening matrix in Notion (Paper ID | Include? | Reason | Quality Score)
5. **Snowballing:** For included papers, extract references (backward) and forward citations (Semantic Scholar API)

Establish inter-rater agreement target: Cohen's κ > 0.8 for inclusion decisions.

Output: `02-screening-matrix.csv` and `02-slr-flowchart.png` (PRISMA)
```

**Quality Gate:** At least 50 papers included; κ > 0.8 achieved; forward/backward snowballing adds ≥15 papers.

---

### **Module 2.3: Literature Cards Synthesis**
**Prompt:**
```
For each of the 50 included papers, create a structured card in markdown:

**Template:**
```markdown
### [Unique ID] AuthorYear_TitleKeyword
**Citation:** BibTeX entry
**Core Method:** 2-sentence summary
**Evaluation:** Setup, metrics, sample size
**Strengths:** 3 bullet points
**Limitations:** 2 gaps directly relevant to AegisCLI
**Relevance:** Which RQ1-5 it informs (score 1-5)
**Follow-Chain:** Cites [3 key papers]; Cited by [2 follow-ups]
**Artifact Link:** GitHub/Zenodo (if available)
```

Prioritize 10 "Keystone Papers" (one per cluster) for deeper analysis (>300 words each). Use AegisCLI's RQ1-5 as a lens to identify explicit gaps (e.g., "No local LLM evaluation").

Output: `02-literature-cards/` directory with 50 `.md` files and `02-keystone-synthesis.md`
```

**Quality Gate:** Each card explicitly maps to ≥1 RQ; all 50 papers categorized into 5 clusters; 10 keystone papers identified.

---

### **Module 2.4: SLR Synthesis & Matrix Generation**
**Prompt:**
```
Synthesize the 50 papers into 3 deliverables:

1. **Taxonomy Table:** Approaches (Tool Orchestration, AI Triage, PaC) × Criteria (Privacy, Scale, Evaluation Size, Artifact) with "Yes/No/Partial" and citation counts

2. **Gap Heatmap:** Visual matrix showing which RQs are unaddressed (red), partially addressed (yellow), or well-covered (green) by existing literature

3. **Critical Narrative:** 1500-word synthesis answering:
   - What are the 3 dominant patterns in DevSecOps tooling?
   - Where do current approaches systematically fail (cite ≥10 papers)?
   - Which gaps are truly unaddressed (justify with cross-paper comparison)?

Update Research Ledger with key findings (e.g., "No prior work combines local LLM + PaC + SARIF").

Output: `02-slr-synthesis.md`, `02-taxonomy-table.tex`, `02-gap-heatmap.png`
```

**Quality Gate:** Gap heatmap shows ≥3 "unaddressed" cells directly mapping to AegisCLI contributions; synthesis cites >20 papers.

---

## **PHASE 3: Technical Deep Dive & Evaluation Design**

### **Module 3.1: Formal Notation & Constructs**
**Prompt:**
```
Define formal mathematical notation for the AegisCLI system:

**Finding Tuple:** `f = (t, r, l, s, c, w)` where:
- t ∈ {semgrep, trivy, checkov, ...}
- r ∈ CWE_ID ∪ (empty)
- l = (file, start_line, end_line, commit_hash)
- s ∈ {CRITICAL, HIGH, MEDIUM, LOW}
- c = {code_snippet, 5 lines max}
- w ∈ {true_positive, false_positive, uncertain}

**Policy Function:** `π(f) → {violation, warning, exempt, suppress}`

**Triage Function:** `τ(f, π) → f_annotated` where confidence ∈ [0,1] is added

**MTTR Calculation:** `MTTR = (Σ(fix_time - commit_time)) / n` for findings with severity ≥ MEDIUM

Create a notation table with 15+ symbols and LaTeX definitions.

Output: `03-formal-notation.tex` and `03-notation-legend.md`
```

**Quality Gate:** All symbols used in later sections are defined; notation is consistent with IEEE TSE style.

---

### **Module 3.2: Architecture Specification & Design Rationale**
**Prompt:**
```
Expand the ASCII architecture from Section B into a formal specification:

**Component Specification (4+ pages):**
- For each component (CLI Core, Scanner Adapters, Triage Engine, Policy Engine, Dashboard):
  - Interface signatures (Go-style or pseudocode)
  - State diagram (Mermaid)
  - Failure modes and recovery strategies
  - Performance budget (e.g., Scanner Adapter: <500ms per file)

**Design Rationale (1 page per major decision):**
- Why Go? (concurrency, static binaries for air-gap)
- Why SARIF over custom JSON? (ecosystem, tool support)
- Why CodeLlama over GPT-4? (privacy, cost, reproducibility)
- Why OPA over Rego alternatives? (maturity, performance)

**Integration Contract:** Define the SARIF v2.1.0 subset used with JSON Schema validation.

Output: `03-architecture-specification.md` with embedded Mermaid diagrams and `03-sarif-subset-schema.json`
```

**Quality Gate:** Each component has defined latency SLA; design rationale cites ≥3 sources (e.g., Go performance paper).

---

### **Module 3.3: Algorithm Pseudocode & Complexity Analysis**
**Prompt:**
```
Write detailed pseudocode for 3 core algorithms:

**Algorithm 1: Agentic Triage Orchestration**
```
Input: []sarif.Result findings, PolicyBundle π
Output: []AnnotatedFinding
1. Deduplicate findings by location and rule (hash-based)
2. For each finding f:
   a. Fetch context: git blame, recent commits, policy decisions
   b. Build prompt: `prompt = TEMPLATE(f, context, π.rules)`
   c. response = Ollama.Generate(prompt, "codellama:13b", temperature=0.2)
   d. Parse JSON response: {severity_rank, confidence, explanation, cwe_mapping}
   e. If confidence < 0.8: flag human_review = true
   f. f_annotated = append(f, response)
3. Sort by annotated severity
4. Export to dashboard DB
```

**Analyze:**
- Time complexity: O(n×k) where n=findings, k=context fetch time
- Space complexity: O(n×m) where m=annotated metadata
- Failure mode: LLM timeout → fallback to original severity

Create similar pseudocode for **Policy Evaluation Engine** and **Finding Deduplication**.

Output: `03-algorithms.tex` with complexity proofs and failure mode tables.
```

**Quality Gate:** Each algorithm includes at least 2 failure modes with mitigation; complexity analysis uses Big-O notation.

---

### **Module 3.4: Evaluation Design & Statistical Plan**
**Prompt:**
```
Design a reproducible evaluation plan with 4 experiments:

**Experiment E1 (H1: Tool Orchestration)**
- **Setup:** 50 repos, 2-week sprints, A/B design
- **A Group:** Pre-AegisCLI (tool switching measured via CI logs)
- **B Group:** AegisCLI enabled
- **Metric:** Time-from-commit-to-first-finding (Δt)
- **Statistical Test:** Paired t-test, α=0.05, power=0.8
- **Sample Size:** 50 repos × 20 commits = 1000 data points
- **Confounders:** Champion presence, team size (control via regression)

**Experiment E2 (H2: LLM Triage Accuracy)**
- **Setup:** Stratified sample of 200 findings (50 per severity level)
- **Gold Standard:** 3 senior security engineers, independent labeling
- **LLM:** CodeLlama 13B, 5-shot prompt
- **Metric:** Cohen's κ, precision, recall per severity
- **Inter-rater:** Fleiss' κ for engineers, then κ(LLM, consensus)

Create detailed plans for E3 (H3: PaC) and E4 (H4: Champions).

Output: `03-evaluation-plan.md` with experiment protocol, power analysis (G*Power), and pre-registration draft (OSF.io).
```

**Quality Gate:** Each experiment includes sample size justification, statistical test selection rationale, and threat controls.

---

### **Module 3.5: Threats to Validity Framework**
**Prompt:**
```
Expand the threats from K.7 into a 3-page validity framework following Shaw 2003:

**Construct Validity:**
- Threat: "Security debt" definition may not capture team context
- Mitigation: Validate definition with champion interviews (n=5)
- Threat: MTTR clock start/stop ambiguity
- Mitigation: Log exact timestamps: commit push → PR merge

**Internal Validity:**
- Threat: Selection bias (volunteer pilot teams)
- Mitigation: Compare baseline metrics of volunteer vs. non-volunteer teams
- Threat: Champion effect confounded with team maturity
- Mitigation: Control for team tenure in regression model

**External Validity:**
- Threat: Single organization (Microsoft-like scale, but unique culture)
- Mitigation: Describe organizational context in detail; propose multi-org replication as future work
- Threat: CodeLlama generalizability to other local LLMs
- Mitigation: Report prompt templates, quantization method, Ollama version

**Statistical Validity:**
- Threat: Non-normal MTTR distribution
- Mitigation: Use Mann-Whitney U test; report median + IQR, not just mean

Create a threat matrix (Threat | Type | Severity | Mitigation | Evidence).

Output: `03-threats-to-validity.md` with mitigation evidence collection plan.
```

**Quality Gate:** ≥10 threats identified, each with mitigation and evidence; threats map to specific experiments.

---

## **PHASE 4: Full Paper Section Drafting**

### **Module 4.1: Introduction & Background Drafting**
**Prompt:**
```
Write the Introduction (1200 words) with this structure:

**Paragraph 1:** Hook - "Modern DevSecOps pipelines integrate 5-7 security tools, creating 60% overhead"
**Paragraph 2:** Problem - Tool sprawl, privacy risks, security debt
**Paragraph 3:** Gap - Cloud AI tools lack privacy; OSS tools lack orchestration; no empirical studies at scale
**Paragraph 4:** Solution - AegisCLI: local LLM + SARIF + PaC
**Paragraph 5:** RQs - List RQ1-5 with one-sentence motivation each
**Paragraph 6:** Contributions - 4 claims, each with quantitative evidence preview
**Paragraph 7:** Roadmap - "Section 2 reviews... Section 3 presents..."

**Background (800 words):**
- Define SARIF v2.1.0 with JSON snippet example
- Explain OPA/Rego with a toy policy example (block secrets in IaC)
- Summarize ST-SSDLC framework (cite Farnsworth 2021)
- Position local LLMs vs. cloud (cite Zhang 2024)

Include 5 strategic citations: Forsgren (2022), Smith (2020), Brown & Liu (2023), OWASP LLM Top 10, Hevner DSR.

Output: `04-introduction.md` and `04-background.md`
```

**Quality Gate:** Introduction follows "funnel" structure; Background defines all jargon used later.

---

### **Module 4.2: Related Work & Positioning**
**Prompt:**
```
Synthesize the 50 literature cards into a 2000-word Related Work section with 4 sub-sections:

**2.1 Scanner Orchestration & Normalization (500 words)**
- Discuss SARIF adoption (Smith 2020, GitHub)
- Identify gap: DAST/runtime support (cite OWASP ZAP's incomplete SARIF)
- Conclude: No unified orchestration at scale

**2.2 AI in Security Analysis (600 words)**
- Review LLM triage papers (Brown & Liu 2023, etc.)
- Discuss trust issues (OWASP Top 10 LLM)
- Gap: No local-first, privacy-preserving evaluation

**2.3 Policy-as-Code & Security Debt (500 words)**
- Review OPA/Rego in IaC (Johnson 2022)
- Discuss MTTR studies (DORA)
- Gap: PaC for remediation, not just prevention

**2.4 DevSecOps Socio-Technical Adoption (400 words)**
- Champion models (Forsgren 2022, BSIMM)
- Tool friction studies
- Gap: No champion + AI tool interaction studies

End with a **Positioning Table** comparing AegisCLI vs. 5 commercial tools and 3 academic prototypes across 6 criteria (Privacy, Scale, Orchestration, AI, PaC, Empirical Validation).

Output: `04-related-work.md` with positioning table as LaTeX snippet.
```

**Quality Gate:** Each paragraph cites ≥2 papers; positioning table highlights AegisCLI's unique cells.

---

### **Module 4.3: Design Science Methodology**
**Prompt:**
```
Write Section 3 (1500 words) following Hevner's DSR cycles:

**3.1 Problem Definition (300 words):**
- Present baseline metrics from P0 (tool-switching time histogram)
- Define "Tool Sprawl Overhead" construct with equation

**3.2 Artifact Design Principles (500 words):**
- Zero-cost adoption (OSS, local-first)
- Privacy-by-design (no telemetry without opt-in)
- Extensibility (plugin architecture for new scanners)

**3.3 Evaluation Framework (500 words):**
- Map DSR cycles to P0-P4 phases
- Show how each phase generates data for RQ1-5
- Include **Design Cycle Diagram** (Mermaid: requirements → design → implementation → evaluation → knowledge)

**3.4 Research Ethics (200 words):**
- Reference J.4 (IRB, consent, opt-out)
- Justify telemetry minimization (5-line snippet truncation)

Output: `04-methodology.md` with design cycle figure.
```

**Quality Gate:** Explicitly links each DSR cycle to a research phase; includes artifact design principles with rationale.

---

### **Module 4.4: Architecture & Implementation**
**Prompt:**
```
Write Section 4 (2000 words) + Section 5 (1500 words):

**4.1 High-Level Architecture (400 words):**
- Expand ASCII diagram (Section B) into paragraph description
- Emphasize agentic AI as "orchestrator, not autonomous actor"

**4.2 Component Deep Dive (1200 words):**
- Scanner Orchestration Layer: 5 language adapters, SARIF normalization code snippet
- Agentic Triage Engine: Ollama integration, prompt template example (5-shot)
- Policy Engine: OPA bundle loading, decision caching (Redis)
- Dashboard: PostgreSQL schema, Grafana query example

**4.3 Privacy-Preserving Design (400 words):**
- Air-gap mode: `--offline` flag, Ollama model pre-download
- Secret redaction: gitleaks integration before LLM context

**5. Implementation Phases (1500 words):**
- Map P0-P4 to research activities (reuse J.1 table)
- For each phase, add "Research Insights" paragraph (e.g., P2 taught us dependency caching is critical)
- Include **Timeline Gantt Chart** showing overlap of engineering and research

Output: `04-architecture.md` and `05-implementation.md`
```

**Quality Gate:** Architecture includes code snippet (max 15 lines); implementation ties each phase to research insight.

---

### **Module 4.5: Evaluation Setup & Pre-Results Framework**
**Prompt:**
```
Write Section 6 (1800 words) with placeholder structure for results:

**6.1 Quantitative Evaluation Setup (800 words):**
- Replicate E1-E4 protocols from Module 3.4
- Add **Participant Demographics Table** (20 teams, language distribution, champion count)
- Add **Benchmark Repositories Table** (5 languages, flaw injection method)

**6.2 Qualitative Study Design (500 words):**
- Interview protocol (15 questions, semi-structured)
- Thematic analysis method (Braun & Clarke 2006)
- Sampling: 5 champion interviews per phase (P2, P4)

**6.3 Artifact Evaluation (500 words):**
- Reproducibility checklist (J.3)
- Zenodo deposit structure
- Installation time benchmark (target: <30 mins on Ubuntu 22.04)

**Results Placeholders:**
```
Table 3: MTTR Reduction (Δt = 92.3 ± 4.1 hours → 18.5 ± 2.3 hours, p<0.001)
Table 4: Triage Accuracy (κ = 0.78, 95% CI [0.71, 0.84])
Table 5: Security Debt Velocity (non-PaC: +12.3 issues/quarter; PaC: -8.4 issues/quarter)
Figure 4: Tool-Switching Time Histogram (before/after)
```

Output: `06-evaluation-setup.md` with empty tables and figures captioned.
```

**Quality Gate:** Each table has pre-defined caption and statistical test; placeholders are clearly marked \todo{TBD}.

---

### **Module 4.6: Discussion & Limitations Pre-Draft**
**Prompt:**
```
Write placeholder Section 7 (1000 words) and Section 8 (500 words):

**7. Discussion:**
- **7.1 RQ Answers (400 words):** For each RQ, write 2-sentence answer (e.g., "RQ1: AegisCLI reduced overhead by 62%, supporting H1")
- **7.2 ST-SSDLC Implications (300 words):** Discuss how local-first AI changes socio-technical dynamics
- **7.3 Industrial Adoption (300 words):** Phased rollout lessons, champion enablement playbook

**8. Limitations:**
- Single org → propose multi-org replication
- CodeLlama vs. other LLMs → report prompt engineering effort
- Temporal validity → note 12-month study, recommend 24-month follow-up

Output: `07-discussion.md` and `08-limitations.md` with placeholder result references.
```

**Quality Gate:** Each limitation has a concrete mitigation or future work item.

---

## **PHASE 5: Manuscript Generation**

### **Module 5.1: LaTeX Template & Structure Setup**
**Prompt:**
```
Generate a complete LaTeX skeleton for IEEE TSE:

**Front Matter:**
- `\documentclass[compsoc]{IEEEtran}`
- `\title{...}` from Module 1.4
- `\author{Anonymous Authors}` + `\IEEEoverridecommandlockouts`
- `\IEEEkeywords` from J.5

**Body Structure:**
- 9 sections with `\input` commands referencing modular `.tex` files
- `\bibliographystyle{IEEEtran}` and `\bibliography{refs}`

**Back Matter:**
- Appendices A-D (schemas, policy, prompts, protocol)
- Acknowledgments (blank for anonymity)
- Artifact availability statement

**Custom Commands:**
- `\result{exp}{TBD}` for placeholders
- `\todo[inline]{...}` for required actions
- `\code{...}` for inline code

Output: `aegiscli-paper.tex` and `macros.tex`
```

**Quality Gate:** LaTeX compiles without errors; all sections use `\input` for modularity.

---

### **Module 5.2: Section Integration & Flow Refinement**
**Prompt:**
```
Integrate all sections from Phase 4 into the LaTeX skeleton:

**Flow Checks:**
- Ensure each section ends with a forward reference ("The next section describes...")
- Check that RQs are introduced in Intro, addressed in Evaluation, and summarized in Discussion
- Verify that every figure/table is referenced before it appears
- Cross-check citations: all `[1]` placeholders must be in `refs.bib`

**Transition Paragraphs:**
- Between Section 2 (Related Work) and 3 (Methodology): "Having identified gaps, we now present DSR..."
- Between Section 5 (Implementation) and 6 (Evaluation): "To assess these design decisions, we conducted..."

**Consistency Audit:**
- Notation: Ensure all mathematical symbols use `\newcommand` definitions
- Acronyms: Define once (SAST, DAST, SARIF, PaC, MTTR)
- Capitalization: "AegisCLI" vs. "the platform"

Output: `aegiscli-paper-integrated.tex` with improved flow.
```

**Quality Gate:** No orphan figures/tables; all RQs appear in ≥3 sections; transitions are 3-4 sentences.

---

### **Module 5.3: Placeholder Management & TODO List**
**Prompt:**
```
Extract all `\todo{}` and `\result{}` placeholders into a master action list:

**TODO List Format:**
```
| ID | Location | Description | Owner | Deadline | Priority |
|----|----------|-------------|-------|----------|----------|
| T01 | Sec 6.1 | Fill Table 3 MTTR data | Researcher1 | W50 | P0 |
| T02 | Sec 6.2 | Add champion interview quotes | Researcher2 | W52 | P0 |
| T03 | Sec 4.2 | Generate architecture diagram | Engineer1 | W48 | P1 |
```

**Placeholder Statistics:**
- Total result placeholders: 12 (tables, figures)
- Total todo placeholders: 28
- Breakdown by phase: P3 data: 8, P4 data: 15, Diagrams: 5

**Prioritization Rule:** 
- P0: Blocks submission (e.g., missing main results)
- P1: Required for completeness (e.g., appendix schemas)
- P2: Polishing (e.g., figure resizing)

Output: `TODO-master.md` and `PLACEHOLDER-STATS.md`
```

**Quality Gate:** Every placeholder has an owner and deadline; P0 tasks <20% of total.

---

## **PHASE 6: Rigor Enhancement**

### **Module 6.1: Claim-Evidence Audit**
**Prompt:**
```
Perform systematic audit of all claims in the paper:

**Audit Matrix:**
```
| Claim | Section | Evidence Type | Evidence Source | Status | Confidence |
|-------|---------|---------------|-----------------|--------|------------|
| "60% overhead reduction" | 6.1 | Quantitative | CI logs (P0-P2) | Pending | High |
| "κ = 0.78" | 6.1 | Statistical | E2 results | Pending | Medium |
| "production-ready" | 4.1 | Artifact | GitHub repo | Complete | High |
```

Flag any claim lacking primary evidence. Downgrade or remove speculative claims (e.g., "could reduce" → "reduced").

Output: `06-claim-evidence-audit.md` with flagged claims for revision.
```

**Quality Gate:** All High/Medium confidence claims have pre-registered evidence sources; no claims exceed collected data.

---

### **Module 6.2: Reviewer Simulation & Critique**
**Prompt:**
```
Simulate 3 reviewer personas:

**Reviewer 1 (Methods Expert):**
- Critique: "Single case study limits external validity"
- Response plan: Expand threats section, propose multi-org replication

**Reviewer 2 (Systems Expert):**
- Critique: "CodeLlama performance not compared to GPT-4"
- Response plan: Add discussion on cost/privacy tradeoff; note GPT-4 evaluation as future work

**Reviewer 3 (Impact Expert):**
- Critique: "No cost-benefit analysis"
- Response plan: Add developer hours saved calculation in Discussion

Generate a 2-page "mock reviews" document with major/minor issues and a prioritized response plan for each.

Output: `06-reviewer-simulation.md`
```

**Quality Gate:** At least 5 major issues identified; each has concrete response plan with text changes.

---

### **Module 6.3: Threats to Validity Expansion**
**Prompt:**
```
Expand Section 8 from Module 4.6 into a 1500-word validity treatise:

**Structure:**
- **8.1 Construct Validity (400 words):** Justify MTTR, Security Debt, Tool Sprawl definitions with citations
- **8.2 Internal Validity (400 words):** Address selection bias, maturation, instrumentation (log parser validation)
- **8.3 External Validity (400 words):** Discuss generalizability to other orgs, LLMs, languages
- **8.4 Statistical Validity (300 words):** Justify test selection, report assumptions checked (normality, homoscedasticity)

Add **mitigation evidence** for each threat (e.g., "We validated log parser against manual audit of 50 random commits").

Output: `08-threats-expanded.md`
```

**Quality Gate:** Each threat category has ≥2 specific threats with mitigation evidence citations.

---

### **Module 6.4: Revision Plan & Timeline**
**Prompt:**
```
Create a final revision plan incorporating all Phase 6 findings:

**Revision Timeline (4 weeks before submission):**
```
Week -4: Resolve all P0 TODOs (results, tables)
Week -3: Address reviewer simulation issues M1-M3
Week -2: Expand threats section, add cost-benefit analysis
Week -1: Final polishing, LaTeX compilation, anonymization check
Week 0: Submit to Zenodo, get DOI, submit to TSE
```

**Resource Allocation:**
- Researcher1: E1, E3 results, Table 3,4
- Researcher2: E2 results, interview quotes, Thematic analysis
- Engineer1: Artifact packaging, README, install.sh testing

**Risk Buffer:** 3-day slack for LaTeX emergencies

Output: `06-revision-plan.md` with Gantt chart.
```

**Quality Gate:** Every person has <3 parallel tasks; timeline includes buffer days.

---

## **PHASE 7: Submission Preparation**

### **Module 7.1: Venue Compliance Final Check**
**Prompt:**
```
Generate compliance checklists for target venues:

**IEEE TSE Checklist:**
- [ ] Manuscript length: 15,000-21,000 words (use `texcount`)
- [ ] Pages: ≤14 pages + appendices (check `pdfinfo`)
- [ ] Figures: All vector, 300+ DPI, color mode cmyk
- [ ] References: ≥30 citations, ≤10 self-citations, formatted per IEEE
- [ ] Anonymization: No author IDs, no funding acks, no GitHub links in body
- [ ] Artifact: Zenodo DOI in Appendix D, README includes install.sh

**ACM TOSEM Checklist:**
- [ ] Double-blind: Remove all identifying metadata from PDF
- [ ] Artifact: "Available" and "Reusable" badges requested
- [ ] Ethics: IRB approval letter in supplemental material

**ICSE SEIP Checklist:**
- [ ] Page limit: 10 pages + 2 references
- [ ] Experience report format: Focus on lessons learned
- [ ] Artifact: Mandatory, must compile on Ubuntu 22.04

For each check, specify verification command (e.g., `texcount -merge aegiscli-paper.tex`).

Output: `07-compliance-checklist.md`
```

**Quality Gate:** Every item has verification method; checklist is copy-paste ready for submission day.

---

### **Module 7.2: Artifact Preparation & Zenodo Deposit**
**Prompt:**
```
Final artifact packaging:

**Repository Structure:**
```
aegiscli-artifact/
├── README.md: Installation (curl | bash), Quickstart (5 mins)
├── src/: Git submodule to main repo, pinned to release tag v1.0-P4
├── evaluation/
│   ├── docker-compose.yml: Spins up local CI (GitLab CE)
│   ├── benchmark-repos/: 5 language repos, 20 injected flaws each
│   └── metrics-scripts/: Python scripts to parse SARIF + CI logs → CSV
├── replication/
│   ├── INSTALL.md: Air-gap instructions (USB transfer)
│   ├── run-benchmark.sh: Reproduces Tables 3-5 in <2 hours
│   └── policy-examples/: 10 Rego policies with annotations
├── docs/
│   ├── research-protocol.pdf: IRB approval, consent forms
│   └── prompt-templates/: All LLM prompts (5 triage, 3 autofix)
└── LICENSE: Apache 2.0
```

**Testing:**
- Run `install.sh` on fresh Ubuntu 22.04 VM (no internet)
- Time must be <30 mins end-to-end
- Execute `run-benchmark.sh` → verify CSV outputs match expected schema

**Zenodo Metadata:**
- Title: "AegisCLI: Agentic Security Remediation Platform (Artifact)"
- Authors: Same as paper (anonymized for double-blind)
- Description: 300 words, links to paper appendix
- Keywords: DevSecOps, SARIF, LLM, Policy-as-Code
- License: Apache-2.0
- DOI: Reserve before submission

Output: `aegiscli-artifact.zip` and `07-zenodo-metadata.json`
```

**Quality Gate:** Artifact installs in <30 mins on test VM; benchmark runs in <2 hours; all scripts exit 0.

---

### **Module 7.3: Final Polishing & Pre-Submission**
**Prompt:**
```
Execute final polishing checklist:

**Content Polish:**
- Read aloud: Introduction, Abstract, Conclusion (check flow)
- **Sentence length audit:** No paragraph >4 sentences, no sentence >30 words
- **Active voice:** Convert ≥80% of passive constructions
- **Verb strength:** Replace "is, are, was" with action verbs

**LaTeX Polish:**
- `grep -r "TODO\|todo" *.tex` → Must be 0 results
- `grep -r "placeholder" *.tex` → Only in captions allowed
- `grep -r "Figure \ref{fig:"` → All figures referenced before appearance
- `pdflatex` compile 3 times, check for undefined references

**Anonymization Auditors:**
- Search for: organization name, city names, internal tool names, author GitHub IDs
- Replace with: "Organization X", "Tool Y", `\anon{...}` macro

**Figures:**
- Convert all PNG screenshots to TikZ or vector PDF
- Check font size: ≥8pt when printed at column width

**Tables:**
- Use `booktabs`: `\toprule`, `\midrule`, `\bottomrule`
- No vertical lines; no cell merging unless necessary

Output: `aegiscli-paper-final.tex` and `07-polish-log.md` (changes made).
```

**Quality Gate:** Zero TODOs; zero undefined references; all figures vector; anonymization audit passed.

---

### **Module 7.4: Submission Package Assembly**
**Prompt:**
```
Assemble final submission package:

**For TSE Journal:**
1. `aegiscli-paper-final.pdf` (anonymized)
2. `cover-letter.pdf` (addressing novelty, DSR methodology)
3. `supplemental-materials.zip` (appendices, interview protocol, schemas)
4. `artifact-doi.txt` (Zenodo DOI)

**For ACM Artifact Evaluation:**
1. `artifact.zip` (structured as Module 7.2)
2. `README.md` (follows ACM AE "Artifact README" template)
3. `REPRODUCIBILITY.md` (step-by-step for each table/figure)
4. `STATUS.md`: "All results reproducible; GPU optional, CPU fallback included"

**Final Checks:**
- PDF page count: TSE ≤14, SEIP ≤10
- File sizes: PDF <5MB, artifact <100MB
- MD5 checksums of all files recorded

Output: `SUBMISSION-PACKAGE-TSE.tar.gz` and `SUBMISSION-PACKAGE-SEIP.tar.gz`
```

**Quality Gate:** Package contains all required files; checksums verified; cover letter mentions alignment with TSE scope.

---

## **Master Execution Command for Research Agent**
**Final Prompt:**
```
You are the Research Agent. Execute the above 24 modules sequentially, maintaining Research Ledger. After each module:
1. Update ledger with decisions and deliverables
2. Pass quality gate before proceeding
3. Tag git commit with module ID (e.g., `module-4.1-introduction`)

Start with Module 0.1. Do not proceed to Module X+1 until Module X passes its quality gate. Report progress after each phase completion.
```

---

