# Module 0.2: Research Scope & Constraint Mapping

## Prompt

Map the user-defined constraints to executable boundaries:
- Translate "50K+ LOC" into specific language breakdown targets (Node.js: 15K, Python: 12K, etc.)
- Convert "10,000+ scan runs" into daily/weekly scan quotas per team
- Define "air-gapped environment" technical specs (no outbound network, Ollama local model cache)
- Identify 3 critical feasibility risks (GPU availability, scanner API churn, champion attrition)
- Propose mitigation strategies for each risk with backup plans

Output: `research-ledger/constraints-mapping.md` with risk matrix (Probability × Impact)

## Quality Gate

Each constraint has a quantifiable metric and risk mitigation with assigned owner.

