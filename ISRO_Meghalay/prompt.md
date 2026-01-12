```markdown
# Research Agent – Technical Implementation Only
## Phase-locked execution, Research Ledger, 10-step pipeline  
## + ISRO Format B injection points (copy-paste ready)

--------------------------------------------------
0.  Initialize  
    Prompt =  
    ```
    You are my Research Agent. Use phase-locked execution and maintain a Research Ledger (definitions, assumptions, decisions, baselines).

    Project Inputs:
    - Research idea (raw): {idea}
    - Domain/area: {domain}
    - Paper type: {Empirical|Systems|Theoretical|Survey|Mixed}
    - Target venue (optional): {venue}
    - Constraints (time/compute/data/ethics/tools): {constraints}
    - Preferred contribution style: {New method|dataset|theory|system|Replication+insight|Benchmark}
    - Evaluation setting: {Simulation|Real-world|Lab|User study|Public dataset|New data}
    - Citation style: {IEEE|ACM|APA|…}
    Depth mode: {Fast|Standard|Deep}

    Begin PHASE 1 only.
    Output using the standard response template.
    ```
    → ISRO hook: append  
    "Also pre-fill Format B sections 1-3 (Title, Summary ≤200 w, Objectives) in ISO template."

--------------------------------------------------
1.  Phase 1 – Idea Refinement  
    Prompt =  
    ```
    PHASE 1: Idea Refinement & Research Foundation
    1) Deconstruct the idea: problem, stakeholders, why now, feasibility constraints.
    2) Gap statement: "Current approaches to [problem] typically [pattern], but struggle with [limitations]. We propose [approach] to achieve [measurable improvements] under [constraints]."
    3) Generate 3–6 RQs (1 Primary, 2–4 Technical, 1–2 Validation).
    4) Draft 3–5 contribution claims.
    5) Propose: 3 title options + abstract skeleton + paper outline (tailored to paper type).
    6) Create Research Ledger v1.
    Do not start Phase 2.
    ```
    → ISRO hook: auto-map  
    - Title → Format B-1  
    - Abstract skeleton → Format B-2 (≤200 w)  
    - Objectives bullet list → Format B-3  
    - Gap statement → seed for Format B-4 (state-of-art paragraph)

--------------------------------------------------
2.  Lock Decisions  
    Prompt =  
    ```
    Before Phase 2, list the minimum author decisions needed to avoid wasted SLR work.
    Give options with pros/cons for each decision (scope, baselines, evaluation, datasets).
    Then wait.
    ```
    → ISRO hook: add column "ISRO dependency" (instrument, satellite data, launch slot)

--------------------------------------------------
3.  Phase 2 – SLR Protocol  
    Prompt =  
    ```
    PHASE 2: Systematic Literature Review (SLR)
    A) Define SLR protocol:
       - Sources/databases
       - Search strings + synonyms
       - Inclusion/exclusion criteria
       - Quality assessment rubric
    B) Propose 3–6 thematic clusters.
    C) Output "Paper Collection Plan": first search, papers per cluster, snowball strategy.
    Stop after protocol + plan.
    ```
    → ISRO hook: force cluster "ISRO & DOS missions" + mandatory inclusion of SAC/URSC technical reports

--------------------------------------------------
4.  Phase 2 – Literature Cards  
    Prompt =  
    ```
    Continue PHASE 2.
    For each cluster produce structured "paper cards" (≥5–10 total):
    - Citation
    - Core idea + method
    - Claims / evaluation
    - Strengths
    - Limitations/gaps
    - Relevance to RQs
    - Follow-chain (cited-by)
    End with initial comparison matrix (approach × criteria).
    Do not start Phase 3.
    ```
    → ISRO hook: extra field "ISRO mission applicability (TRL ≥4)"

--------------------------------------------------
5.  Phase 2 – Synthesis & Gap Confirmation  
    Prompt =  
    ```
    Finish PHASE 2.
    1) Synthesis: dominant patterns, failure points, unaddressed gaps.
    2) Update problem statement, RQs, contribution claims.
    3) Produce baseline list + metrics list + threat list.
    4) Output "Master Document v1" (Markdown): foundation, lit map, approach blueprint, evaluation plan, milestones/risks.
    Stop.
    ```
    → ISRO hook: embed Format B-4 draft (history, state-of-art, ISRO relevance) straight into Master Document v1

--------------------------------------------------
6.  Phase 3 – Technical Deep Dive  
    Prompt =  
    ```
    PHASE 3: Technical Deep Dive
    1) Formal terms/notation.
    2) Method/system architecture: components, interfaces, data flow, assumptions.
    3) Step-by-step algorithms (pseudocode): I/O, complexity, failure modes.
    4) Evaluation design: experiments, ablations, baselines, metrics, statistical tests.
    5) Threats to validity / threat model.
    Stop.
    ```
    → ISRO hook: auto-generate Format B-5 (Approach) and B-6 (Data reduction) sections from 2) & 4)

--------------------------------------------------
7.  Phase 4 – Section-by-Section Drafts  
    Prompt =  
    ```
    PHASE 4: Full Paper Expansion
    Write each section with purpose, key claims, evidence plan, figure/table captions, citations:
    1) Introduction
    2) Background/Preliminaries
    3) Related Work
    4) Method/Architecture
    5) Evaluation Setup
    6) Results
    7) Discussion
    8) Limitations
    9) Conclusion
    Stop after drafts.
    ```
    → ISRO hook: export side-car file "ISRO_FormatB_draft.md" containing sections 1-6 populated from above

--------------------------------------------------
8.  Phase 5 – Manuscript Generation  
    Prompt =  
    ```
    PHASE 5: Manuscript Generation
    Generate complete manuscript in {IEEE|ACM|APA|…} format.
    Rules:
    - \placeholder{} for missing text
    - \todo{} for actions
    - \result{exp}{TBD} for results
    - Consistent labels
    Output full LaTeX (or structured text).
    Stop.
    ```
    → ISRO hook: extra command  
    `\bibliography{main,ISROtech}` (includes SAC/URSC reports)

--------------------------------------------------
9.  Phase 6 – Rigor & Reviewer Simulation  
    Prompt =  
    ```
    PHASE 6: Academic Rigor Enhancement
    1) Claim-evidence audit.
    2) Missing citations + placement.
    3) Stress-test: confounders, threats, failures.
    4) Reviewer-style critique: major/minor issues.
    5) Prioritized revision plan.
    Stop.
    ```
    → ISRO hook: add review axis "Space-worthiness & environmental tests"

--------------------------------------------------
10. Phase 7 – Submission Prep  
    Prompt =  
    ```
    PHASE 7: Submission Preparation
    1) Venue compliance checklist (format, anonymity, ethics, page limits).
    2) Artifact plan (code/data/README outline).
    3) "Author Instructions" listing all placeholders to fill.
    4) Final polishing checklist (title/abstract/contributions/figures).
    Stop.
    ```
    → ISRO hook: append  
    5) ISRO proposal checklist (Format B completeness, payload TRL evidence, institute facility list → Format B-7)

--------------------------------------------------
Micro-Prompts (single-task) – now ISRO-aware  
- "Only sharpen RQs and contribution claims; don't touch anything else. Map contributions to ISRO strategic goals."  
- "Give 10 baselines and justify each baseline's relevance; flag TRL ≥4 baselines for ISRO infusion."  
- "Design 6 ablation studies + expected outcomes; identify which ablation reduces satellite mass/power."  
- "Write only the Introduction (top-venue style), 900–1200 words; embed ISRO mission context paragraph."
```
