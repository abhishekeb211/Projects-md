# Forensics Mode

## Industry-Grade Architecture: Tool-Backed Crypto Forensics with Deterministic Concurrency and Comprehensive Attack Validation

### Document Overview

This document defines a **complete crypto-forensics and attack validation system** that combines:

1. **Forensics Analysis**: Classify, analyze, and fingerprint unknown cryptographic artifacts
2. **Attack Validation**: Execute 83 cryptographic attacks (across 25 categories) against each artifact, with each attack run 3× for statistical confidence
3. **Evidence-Based Architecture**: Every decision, module execution, and attack outcome is recorded as structured evidence
4. **Production-Grade Discipline**: Determinism, isolation, failure-as-data, resource governance, and caching built in from day one

**Key Innovation**: This is not just a forensics system or just an attack framework—it's a **unified platform** that analyzes artifacts AND validates their security by executing real attacks, producing comprehensive resistance profiles.

**What Makes This Different**:
- **83 attacks implemented**: From frequency analysis to quantum threat simulation
- **3× repeat execution**: Statistical confidence in attack outcomes
- **Attack resistance profiling**: Each artifact gets a vulnerability assessment
- **Deterministic and reproducible**: Same artifact + same toolchain = same results
- **Evidence traceability**: Every attack attempt, success, failure, and timeout is recorded

**Scope**: ~1500+ pages of implementation details, from high-level architecture to task-level to-do lists, budget projections, and feasibility assessments.

---

### Mission

Build a crypto-forensics pipeline that can:
1. Ingest real-world artifacts (ciphertexts, keys, certs, PQC blobs, hashes, captures, binaries)
2. Run tool-backed analysis in reproducible environments
3. **Execute comprehensive cryptographic attack validation** (83 attacks across 25 categories, each run 3 times)
4. Store all attack outputs with encrypted data for analysis and correlation
5. Emit structured evidence for feature extraction, modeling, and reporting
6. Scale to production volumes without sacrificing reproducibility or traceability

**Extended Mission**: Transform unknown artifacts into classified, analyzed, and attack-validated evidence with complete traceability from intake to final report.

---

## Product Requirements (Non-Negotiable)

### Functional

- Classify and parse crypto-related artifacts into meaningful families/types
- Run behavioral, wrapper, protocol, and implementation-level probes
- **Execute comprehensive cryptographic attack validation (83 attacks, 25 categories, each 3×)** (NEW)
- **Generate attack resistance profiles and vulnerability assessments** (NEW)
- Support PQC ground-truth generation and validation using real toolchains
- Identify and classify hash/KDF materials defensively (audit/IR mode)
- Produce evidence-linked reports and model-ready features **including attack validation results** (ENHANCED)

### Non-Functional (industry constraints)

- **Deterministic outputs** across runs given same inputs + toolchain
- **Reproducible environments** (tool versions pinned and recorded)
- **Isolation**: no cross-job temp/config collisions
- **Observability**: every decision backed by structured evidence and provenance
- **Safety controls**: hash module must not "accidentally become cracking"
- **Scalable throughput**: handle thousands to millions of artifacts over time

---

## High-Level System Overview

```
Inputs (Artifacts / Captures / Binaries)
→ Ingestion & Registry
→ Run Control Plane (manifest + policies + inventory)
→ Artifact Job Orchestration (artifact-parallel execution)
→ Tool-Backed Forensics Layer (modules)
→ Evidence Store (Telemetry) (deterministic)
→ Feature Store
→ Tiered Models
→ Reports + APIs
```

---

## 3) Forensics Mode (Real-World Ingest + Analysis)

(This is the "someone handed you a blob and swore it's totally normal" mode. The system's job is to turn chaos into evidence, deterministically, without becoming a security incident.)

---

### A) Goals and Guarantees (Forensics-Specific)

#### Primary goal

Classify and analyze unknown crypto-related artifacts using tool-backed modules

Produce structured, evidence-linked outputs suitable for features, modeling, and reporting

#### Non-negotiable guarantees

- **Deterministic evidence outputs** given same artifact + same run manifest + same tool inventory
- **Isolation**: no cross-artifact collisions in temp dirs, configs, or logs
- **Failure-as-data**: every failure is recorded as structured evidence, not hidden
- **Safety**: hash/KDF handling does not drift into recovery/cracking behavior
- **Traceability**: every claim in reports links back to evidence events and tool provenance

---

### B) Inputs (What Forensics Mode Accepts)

#### Artifact types (examples)

- Ciphertext blobs (raw, wrapped, hybrid)
- Keys (PEM/DER/SPKI, raw, partial)
- Certificates and chains
- PQC keys/ciphertexts/signatures/blobs
- Hash/KDF materials (hash strings, salted outputs, parameter blobs)
- Protocol captures (PCAP, TLS records)
- Binaries (libraries, apps, firmware)

#### Required intake metadata

- source identifier (case/source)
- collection timestamp (when known)
- permissions/tenant/case scope
- optional hints (claimed algorithm, environment, suspected wrapper)

---

## Cryptographic Attacks Framework (Validation & Breaking Layer)

### Purpose

Execute systematic attack validation against artifacts to:
- Validate encryption strength and implementation correctness
- Identify vulnerabilities and weak configurations
- Generate attack resistance profiles
- Produce attack-validated evidence for classification
- Build attack success/failure datasets for model training

### Core Principle

**Every artifact undergoes comprehensive attack validation**: Each applicable attack is executed **3 times** (for statistical confidence), and all outputs are stored with deterministic evidence linking.

---

## Cryptographic Attacks Master Table

### Total: 83 Attacks Across 25 Categories

| # | Category | Attack Name | Target | Complexity | Practical | Year | Severity |
|---|----------|-------------|--------|-----------|----------|------|----------|
| 1 | Ciphertext-Only | Frequency Analysis | Stream/Block Ciphers | Moderate | Limited | 1500s | Low |
| 2 | Ciphertext-Only | Statistical Attack | Symmetric | Moderate | Limited | 1940s | Low |
| 3 | Ciphertext-Only | Correlation Attack | Symmetric | High | Limited | 2000s | Medium |
| 4 | Known-Plaintext | Linear Cryptanalysis | Block Ciphers | High | High | 1990s | High |
| 5 | Known-Plaintext | Differential Cryptanalysis | Block Ciphers | High | Moderate | 1990s | High |
| 6 | Known-Plaintext | Integral Cryptanalysis | Block SPN | High | Moderate | 2000 | Medium |
| 7 | Known-Plaintext | Biclique Attack | Block Ciphers | High | Moderate | 2010 | Medium |
| 8 | Chosen-Plaintext | Differential (CPA) | Block Ciphers | High | High | 1990s | High |
| 9 | Chosen-Plaintext | Integral (Square) | Block SPN | High | High | 2000 | High |
| 10 | Chosen-Plaintext | Adaptive CPA | Block Ciphers | High | Moderate | 1990s | Medium |
| 11 | Chosen-Ciphertext | Padding Oracle | CBC+Padding | Moderate | High | 1998 | High |
| 12 | Chosen-Ciphertext | POODLE | TLS/SSL3 | Moderate | High | 2014 | High |
| 13 | Chosen-Ciphertext | Bleichenbacher | RSA | High | Moderate | 2000 | High |
| 14 | Brute-Force | Brute Force Key Search | Any Cipher | Low-VHigh | Very High | 1900s | Very High |
| 15 | Brute-Force | Dictionary Attack | Passwords | Low | High | 1980s | High |
| 16 | Brute-Force | Rainbow Table | Hashes | Very High | High | 2003 | High |
| 17 | Brute-Force | Hybrid Dictionary | Passwords | Moderate | High | 2000s | High |
| 18 | Collision | Birthday Attack | Hash Functions | High | Moderate | 1977 | High |
| 19 | Collision | Collision Attack | Hash/Sig | Moderate | Moderate | 1990s | Medium |
| 20 | Collision | Multi-collision | Hash | Very High | Limited | 1997 | Medium |
| 21 | Time/Memory | Meet-in-Middle | Symmetric | Moderate | High | 1980 | High |
| 22 | Time/Memory | Rainbow Chain | Hashes | High | High | 2003 | Very High |
| 23 | Time/Memory | Hellman Table | Encryption | Very High | Moderate | 1980 | High |
| 24 | Differential | Differential Cryptanalysis | Block Ciphers | High | Moderate | 1990 | High |
| 25 | Differential | Impossible Differential | Block | Very High | High | 1999 | High |
| 26 | Differential | Boomerang Attack | Block | Very High | Moderate | 1999 | High |
| 27 | Linear | Linear Cryptanalysis (Block) | Block Ciphers | High | High | 1993 | High |
| 28 | Linear | Linear Cryptanalysis (Stream) | Stream | High | High | 2001 | High |
| 29 | Linear | Differential-Linear Attack | Block | Very High | Moderate | 2002 | Medium |
| 30 | MITM | Double Encryption Attack | Double Enc | High | Very High | 1991 | Very High |
| 31 | MITM | 3DES Break | 3DES | Very High | High | 1999 | High |
| 32 | MITM | Generalized MITM | Multi-block | Very High | High | 2003 | High |
| 33 | Algebraic | Interpolation Attack | Block Ciphers | Very High | Limited | 2000 | Medium |
| 34 | Algebraic | Cube Attack | Streams | Very High | Moderate | 2009 | Medium |
| 35 | Algebraic | Algebraic Attack | Symmetric | Very High | Limited | 2015 | Medium |
| 36 | Algebraic | Linearization Attack | Boolean | Very High | Limited | 2007 | Low |
| 37 | Statistical | Correlation Attack | Streams | High | High | 2001 | High |
| 38 | Statistical | Chi-Square Test | Any | Moderate | Limited | 1987 | Low |
| 39 | Statistical | Mod-n Analysis | Modular | Moderate | Limited | 1985 | Low |
| 40 | Timing SCA | Timing Attack (RSA) | RSA | Moderate | Moderate | 1995 | Medium |
| 41 | Timing SCA | Lucky 13 Attack | TLS-AES | Moderate | High | 2013 | High |
| 42 | Timing SCA | Constant-Time Bypass | Timing-Code | Low | Low | 2014 | Medium |
| 43 | Power SCA | SPA | Implementations | Moderate | High | 1998 | High |
| 44 | Power SCA | DPA | Devices | Moderate | Very High | 2003 | High |
| 45 | Power SCA | Higher-Order Power | Processors | High | High | 2015 | Very High |
| 46 | EM SCA | EMA | EM Emissions | Moderate | Moderate | 2000 | Medium |
| 47 | EM SCA | EM Leakage | EM | Moderate | Moderate | 2003 | Medium |
| 48 | EM SCA | TEMPEST | Unshielded | Moderate | Limited | 1970s | Low |
| 49 | Cache SCA | Flush+Reload Attack | L3 Cache | Moderate | Very High | 2005 | Very High |
| 50 | Cache SCA | Prime+Probe Attack | Cache Lines | Low | High | 2005 | Very High |
| 51 | Cache SCA | Evict+Time Attack | Cache | Low | Very High | 2013 | Very High |
| 52 | Acoustic SCA | Acoustic Attack | Acoustic | Moderate | Moderate | 2018 | Medium |
| 53 | Acoustic SCA | Acoustic Cryptanalysis | CPU | Limited | Limited | 2018 | Low |
| 54 | Acoustic SCA | Fan Noise Analysis | Hardware | Limited | Limited | 2019 | Low |
| 55 | Fault Injection | Differential Fault Attack | Block AES | Moderate | High | 2002 | High |
| 56 | Fault Injection | Voltage Glitch Injection | Hardware | Moderate | Very High | 2010 | Very High |
| 57 | Fault Injection | Clock Glitch Attack | Clock | Moderate | Very High | 2012 | Very High |
| 58 | Fault Injection | Laser Fault Injection | Laser | Low | Very High | 2018 | Very High |
| 59 | Weak Key | Weak Key Recovery | Keys | Moderate | High | 1995 | High |
| 60 | Weak Key | Related-Key Attack | Keys | High | High | 2002 | Medium |
| 61 | Weak Key | Key Clustering | Symmetric | Moderate | Moderate | 2012 | Low |
| 62 | Protocol | Padding Oracle (CBC) | TLS CBC | Very High | Very High | 2004 | High |
| 63 | Protocol | BEAST Attack | TLS 1.0 | High | High | 2011 | High |
| 64 | Protocol | CRIME Attack | Compression | High | High | 2012 | High |
| 65 | Protocol | BREACH Attack | Headers | Very High | High | 2019 | Medium |
| 66 | Downgrade | POODLE (SSLv3) | Legacy | Very High | Very High | 2014 | Very High |
| 67 | Downgrade | DROWN Attack | TLS Old | Very High | Very High | 2015 | Very High |
| 68 | Downgrade | Downgrade to SSLv2 | SSLv2 | Very High | High | 2014 | Very High |
| 69 | Password | Dictionary Attack | Passwords | Low | Very High | 1993 | High |
| 70 | Password | Hybrid Dictionary | Passwords | Moderate | High | 2007 | High |
| 71 | Password | Rainbow (Password) | Passwords | Very High | High | 2013 | High |
| 72 | Password | Credential Stuffing | Databases | High | High | 2018 | Medium |
| 73 | Quantum | Shor Algorithm (RSA) | RSA | Very High | High(Future) | 1994 | Critical |
| 74 | Quantum | Shor Algorithm (DLP) | ECDLP | Very High | High(Future) | 1996 | Critical |
| 75 | Quantum | Grover Algorithm | Symmetric | Very High | High(Future) | 2019 | Critical |
| 76 | Speculation | Spectre Attack | Microarch | Low | Very High | 2018 | Very High |
| 77 | Speculation | Meltdown Attack | Memory | Very High | Very High | 2018 | Very High |
| 78 | Speculation | Transient Exec | Transient | High | Very High | 2018 | Very High |
| 79 | Other | Rectangle Attack | Differential | Moderate | Moderate | 1999 | High |
| 80 | Other | Slide Attack | Periodic | High | High | 2010 | High |
| 81 | Other | Contact Analysis | Metadata | Medium | Moderate | 2006 | Medium |
| 82 | Other | Key-Recovery Attack | Keys | High | High | 2013 | High |
| 83 | Other | Distinguishing Attack | Ciphers | Moderate | Moderate | 2002 | Medium |

---

### Attack Categories Summary (25 Categories)

1. **Ciphertext-Only Analysis** (3 attacks) - Weakest attacker position
2. **Known-Plaintext Analysis** (4 attacks) - Plaintext-ciphertext pairs available
3. **Chosen-Plaintext Analysis** (3 attacks) - Attacker chooses plaintexts
4. **Chosen-Ciphertext Analysis** (3 attacks) - Most powerful position
5. **Brute-Force Attacks** (4 attacks) - Exhaustive key search
6. **Collision Attacks** (3 attacks) - Hash function targets
7. **Time/Memory Trade-offs** (3 attacks) - Computational vs storage
8. **Differential Cryptanalysis** (3 attacks) - Plaintext pair differences
9. **Linear Cryptanalysis** (3 attacks) - Linear approximations
10. **Meet-in-the-Middle (MITM)** (3 attacks) - Double encryption breaks
11. **Algebraic Attacks** (4 attacks) - Polynomial equation solving
12. **Statistical Attacks** (3 attacks) - Statistical bias exploitation
13. **Side-Channel (Timing)** (3 attacks) - Execution time analysis
14. **Side-Channel (Power)** (3 attacks) - Power consumption monitoring
15. **Side-Channel (EM)** (3 attacks) - Electromagnetic radiation
16. **Side-Channel (Cache)** (3 attacks) - CPU cache exploitation
17. **Side-Channel (Acoustic)** (3 attacks) - Sound emission analysis
18. **Fault Injection** (4 attacks) - Hardware fault induction
19. **Weak Key** (3 attacks) - Special key properties
20. **Protocol-Level** (4 attacks) - TLS/SSL implementation flaws
21. **Downgrade** (3 attacks) - Force weaker algorithms
22. **Password** (4 attacks) - Password-based attacks
23. **Quantum** (3 attacks) - Quantum computing threats
24. **CPU Speculation** (3 attacks) - Spectre/Meltdown family
25. **Other Advanced** (5 attacks) - Rectangle, Slide, etc.

---

### Attack Severity Distribution

| Severity | Count | Attack IDs | Examples |
|----------|-------|-----------|----------|
| **Critical** | 3 | 73-75 | Shor (RSA/DLP), Grover |
| **Very High** | 18 | 14, 22, 30, 44-45, 49-51, 56-58, 66-68, 76-78 | Brute Force, DPA, Cache Attacks, Fault Injection |
| **High** | 38 | 4-5, 8-9, 11-13, 15, 18, 21, 24-25, 27-28, etc. | Linear, Differential, Birthday, BEAST |
| **Medium** | 18 | 3, 6-7, 10, 19, 26, 29, 33-35, 40, 42, etc. | Integral, Correlation, Acoustic |
| **Low** | 6 | 1-2, 36, 38-39, 48, 53-54 | Frequency Analysis, Chi-Square, TEMPEST |

---

### Attack Practicality Distribution

| Practicality | Count | Attack IDs | Examples |
|--------------|-------|-----------|----------|
| **Very High** | 15 | 14, 22, 30, 44-45, 49-51, 56-58, 62, 66-67, 69, 76-78 | Brute Force, DPA, Cache, Fault, POODLE, Spectre |
| **High** | 30 | 4, 8-9, 11, 15-16, 21, 24-25, 27-28, 31-32, 37, etc. | Linear, Differential, Rainbow, Dictionary |
| **Moderate** | 20 | 1, 5-7, 10, 13, 18-20, 26, 29, 34, 40, 46-47, etc. | Statistical, Biclique, MITM, Cube |
| **Limited** | 18 | 2-3, 20, 33, 35-36, 38-39, 48, 52-54, etc. | Frequency, Interpolation, Acoustic |

---

## Attack Execution Architecture

### Attack Applicability Router

**Purpose**: Determine which attacks are applicable to each artifact based on type classification

**Logic**:
```python
if artifact_type == "SYMMETRIC_CIPHERTEXT":
    applicable_attacks = [1-10, 14, 18, 24-29, 37-39]  # Ciphertext-only, Known-PT, Chosen-PT, etc.
elif artifact_type == "HASH_MATERIAL":
    applicable_attacks = [15-23, 69-72]  # Brute-force, Collision, Time/Memory, Password
elif artifact_type == "RSA_KEY" or "RSA_CIPHERTEXT":
    applicable_attacks = [13, 14, 40, 59-60, 73]  # Bleichenbacher, Timing, Weak Key, Shor
elif artifact_type == "PROTOCOL_CAPTURE":
    applicable_attacks = [11-12, 40-42, 62-68]  # Padding Oracle, Timing, Protocol, Downgrade
# ... continue for all artifact types
```

### Attack Execution Flow

```
Artifact → Type Router → Attack Applicability Filter
    ↓
Attack Job Creation (one job per attack)
    ↓
Attack Execution × 3 (repeat 3 times per attack)
    ↓
    ├─ Attack Attempt 1 → Evidence Event 1
    ├─ Attack Attempt 2 → Evidence Event 2
    └─ Attack Attempt 3 → Evidence Event 3
    ↓
Attack Result Aggregation (statistical analysis of 3 runs)
    ↓
Attack Resistance Profile → Evidence Store
```

### Attack Job Structure

Each attack execution is a job:

```json
{
  "job_type": "attack_execution",
  "artifact_id": "abc123...",
  "attack_id": 11,
  "attack_name": "Padding Oracle",
  "attack_category": "Chosen-Ciphertext",
  "attempt_number": 1,  // 1, 2, or 3
  "attack_seq": 42,  // Deterministic ordering
  "policy": {
    "timeout_seconds": 300,
    "max_queries": 10000,
    "resource_class": "heavy"  // or "light"
  }
}
```

### Attack Output Schema

```json
{
  "event_type": "attack_execution",
  "attack_id": 11,
  "attack_name": "Padding Oracle",
  "attempt_number": 2,
  "artifact_id": "abc123...",
  "attack_seq": 42,
  "event_seq": 1052,
  "result": "SUCCESS" | "FAILED" | "TIMEOUT" | "NOT_APPLICABLE",
  "confidence": 0.95,
  "execution_time_ms": 2543,
  "queries_performed": 8234,
  "recovered_data": "base64:...",  // if SUCCESS
  "partial_results": {...},
  "tool_outputs_ref": "s3://attacks/blobs/xyz789.../",
  "error_category": "TIMEOUT" | null
}
```

### Attack Result Aggregation (After 3 Runs)

```json
{
  "event_type": "attack_summary",
  "attack_id": 11,
  "attack_name": "Padding Oracle",
  "artifact_id": "abc123...",
  "attempts": 3,
  "results": {
    "success_count": 2,
    "failed_count": 0,
    "timeout_count": 1,
    "success_rate": 0.667
  },
  "consistency_score": 0.8,  // How consistent were the 3 runs?
  "average_time_ms": 2310,
  "median_queries": 8100,
  "recovered_data_consistent": true,
  "vulnerability_confirmed": true,
  "evidence_refs": ["event_seq_1052", "event_seq_1053", "event_seq_1054"]
}
```

---

### Attack Pool (Parallel Execution Governance)

**Light Attack Pool** (Fast, parallel-friendly):
- Attacks: 1-3, 14-17, 38-39, 69-70, etc.
- Concurrency: High (50-100 parallel)
- Timeout: Seconds to minutes

**Heavy Attack Pool** (Resource-intensive, throttled):
- Attacks: 4-13, 21-37, 55-58, 73-75, etc.
- Concurrency: Low (2-5 parallel)
- Timeout: Minutes to hours
- Resource limits: Strict CPU/memory caps

**Simulation-Only Pool** (Lab/experimental):
- Attacks: 43-48, 52-54, 76-78 (SCA, Speculation)
- Concurrency: Very low (1-2 parallel)
- Requires specialized hardware or simulation

---

## Attack Storage Layout

```
attacks/
  attack_registry.json          # Metadata for all 83 attacks
  attack_applicability_map.json # Attack → Artifact Type mappings
  
telemetry/
  attack_events/
    attempt_events.jsonl        # Individual attack attempts
    summary_events.jsonl        # Aggregated 3-run summaries
    
  attack_outputs/
    blobs/                      # Raw tool outputs per attack
      {attack_id}_{attempt}/
        stdout.txt
        stderr.txt
        recovered_data.bin
        metrics.json
        
results/
  attack_resistance_profiles/
    {artifact_id}_profile.json  # Consolidated attack results per artifact
    
features/
  attack_features.parquet       # Attack results as features for ML
```

---

## Post-Quantum Attack Considerations

**Quantum attacks (73-75)** are **simulation-only** in current implementation:
- Execute as bounded computational estimates (time-to-break calculations)
- No actual quantum hardware required
- Emit threat assessment based on key sizes and algorithms
- Used for PQC migration recommendations

**Example Output**:
```json
{
  "attack_id": 73,
  "attack_name": "Shor Algorithm (RSA)",
  "result": "SIMULATED_SUCCESS",
  "estimated_qubits_required": 4096,
  "estimated_time_ideal_qc": "8 hours",
  "threat_level": "CRITICAL_BY_2030",
  "recommendation": "Migrate to ML-KEM-768 or hybrid"
}
```

---

## Control Plane (Makes it Feasible in Production)

### C) Ingestion & Artifact Registry (Product-Grade Intake and Identity)

#### Purpose

Product-grade intake and identity management

**Why it matters**: Industry systems don't run "files on disk." They run immutable refs with provenance.

#### Responsibilities

Accept artifacts via API/CLI/batch upload

Compute stable identifiers:

- `artifact_hash` (content hash)
- `artifact_id` (internal UUID)

Store immutable artifact blob in object storage

Record metadata:

- size, MIME/type hints
- source identifier (case/source)
- collection timestamp
- permissions/ACL/tenant scope
- chain-of-custody notes (if relevant)
- optional hints (claimed algorithm, environment, suspected wrapper)

#### Outputs

- `artifact_registry` entry (authoritative index record)
- Immutable blob reference (`artifact_ref`, content-addressed where possible)

#### Operational rules

- No in-place updates to artifacts
- Any "re-upload" is a new artifact entry; relationships are tracked explicitly

---

### C.1) Run Controller (Mandatory for Determinism)

#### Purpose

Make runs deterministic, auditable, and reproducible

#### Responsibilities

Create `run_id`

Capture tool inventory once:

- tool name/version/path
- OS profile (Kali/RHEL) + container/image digest
- provider availability (OpenSSL3 PQC provider, liboqs version)

Freeze run policy:

- concurrency limits
- tool/module timeouts
- seeding rules (deterministic seeds derived from artifact hash + run config)
- safety mode flags (e.g., `audit_only_hashes=true`)

Start telemetry services:

- event writer
- metrics/monitoring hooks

#### Outputs

- `run_manifest.json` (signed/immutable if needed)
- `tool_inventory.json`

---

### C.2) Artifact Job Scheduler (Artifact-Level Parallelism)

#### Purpose

Scale horizontally by making artifacts independent jobs

#### Responsibilities

Create one **Artifact Job** per artifact (or per bundle when needed)

Assign job metadata:

- `artifact_seq` (stable ordering within run)
- job class (light-only vs heavy-eligible)
- per-artifact workspace specification (logical, not shared)

Enforce backpressure:

- maximum in-flight artifact jobs
- priority routing (interactive vs batch)

#### Industry scaling

This is where you plug in **Kafka/SQS/Celery/Ray/Kubernetes Jobs** later. The architecture doesn't change.

---

### C.3) Artifact Worker Pool (Parallel Throughput Tier)

#### Purpose

Execute many artifact jobs concurrently without shared-state bugs

#### Execution Model

- **Parallel across artifacts** (max throughput)
- **Mostly sequential module execution** inside each artifact job (stable state)
- **Bounded "quick-parallel"** inside job only for independent checks

#### Rules

- Workers never write final logs or features directly
- Workers emit events to a centralized telemetry stream
- Per-artifact workspace is isolated (no shared temp dirs, no shared configs)

---

### C.4) Shared Heavy Work Pool (Governor Tier)

#### Purpose

Allow heavy analysis without taking down the system

#### Runs

- Math workbench (Sage/PARI heavy tests)
- PQC batch generation
- Deep reverse engineering (Ghidra-heavy workflows)

#### Discipline majors

- Process isolation
- Strict concurrency caps
- Strict timeouts
- Optional resource limits (memory/CPU)

#### Product behavior

Heavy work is a **scarce resource by design**. The heavy pool is the governor.

---

### C.5) Deterministic Telemetry Pipeline (Single Writer Semantics)

#### Purpose

Stop parallelism from corrupting evidence

#### Responsibilities

Consume emitted events from workers

Persist them deterministically with:

- `artifact_seq` + `event_seq`
- normalized timestamps

Store:

- module events (JSONL or structured log store)
- tool-run events (commands, exit status, parsed outputs)
- pointers to raw logs (content-addressed blobs)

#### Why it matters

Production needs **diffable runs**, **reproducible evaluations**, and **audit trails**.

---

### D) Artifact Job Setup (What Happens Before Analysis Starts)

#### Responsibilities per artifact job

Assign stable ordering within run:

- `artifact_seq` (deterministic, from job planner)

Create isolated workspace:

- unique workspace path per artifact job

Apply execution safety posture:

- no network by default
- sandbox restrictions (containerization, limited privileges)
- bounded stdout/stderr capture

Apply determinism settings:

- fixed locale/formatting environment
- deterministic seed derivation context

Register "job start" evidence event:

- includes workspace spec, applied policy bundle, and artifact metadata snapshot

#### Outputs

- Workspace ready
- Job start evidence event emitted

---

### E) Module Execution Plan (Deterministic, Type-Driven)

#### Principles

- Parallelism is across artifacts, not inside a single artifact (except bounded "quick-parallel")
- Module order is deterministic and recorded
- Every module invocation emits evidence events, even when skipped

#### Typical module order

1. **Artifact Type Router**
2. **CLI Inspection / Wrapper Triage**
3. **Normalizer / Candidate Parser**
4. **Type-Specific Probes**
5. **Implementation Fingerprinting (Light)**
6. **Attack Applicability Determination** (NEW)
7. **Attack Execution (3× per applicable attack)** (NEW)
8. **Attack Aggregation & Resistance Profile** (NEW)
9. **Heavy Escalation Requests** (if allowed and justified)
10. **Completion Summary Event**

**Note**: Attack execution can happen in parallel across different attacks (via attack pools), but each attack runs 3 times sequentially for consistency validation.

---

### F) Artifact Type Router (Mandatory)

#### Purpose

Decide which workflows are valid and prevent nonsense/dangerous paths

#### Inputs

- registry metadata (MIME hints, size)
- magic bytes / file signatures
- early triage outputs (light parsing hints)

#### Outputs

Multi-label type set (examples):

- symmetric ciphertext
- KEM transcript
- signature blob
- hybrid blob
- key material
- hash/KDF material
- protocol capture
- binary target

Routing evidence:

- what signals caused each label assignment
- confidence scores where applicable

#### Built-in safety rules

- **Fail-closed**: hash/KDF materials cannot trigger recovery-style workflows
- Multi-label support prevents hybrid misrouting
- Unknown classification allowed and recorded as a valid outcome

---

### G) CLI Inspection (Fast Triage, Wrapper/Container Identification)

#### Purpose

Extract wrapper signals and parsing outcomes quickly, without deep execution

#### Responsibilities

Detect encodings and wrappers:

- PEM vs DER vs raw
- ASN.1 structure hints
- key/cert container hints
- TLS record or PCAP structure hints

Produce "failure shapes" as first-class evidence:

- tag mismatch
- truncation
- malformed header
- unsupported algorithm id
- parse depth limits reached

#### Outputs

- Wrapper evidence events
- Parsed metadata where possible (non-sensitive)
- Normalized error taxonomy events on failure (not generic "tool failed")

#### Operational controls

- strict timeouts
- bounded outputs
- no network

---

### H) Normalizer / Candidate Parser (Sequential, Bounded)

#### Purpose

Convert raw inputs into candidate "core" regions suitable for probing

#### Responsibilities

Identify stable boundaries and invariants:

- prefix/suffix stability fingerprints
- header/footer patterns

Generate candidate splits:

- offsets and lengths
- extracted core components (ciphertext region, KEM region, signature region)

Score and prune candidates deterministically

#### Built-in controls (non-negotiable)

Hard cap on candidates generated (prevents explosion)

Deterministic pruning rules:

- scoring heuristic must be stable and recorded

Emit events for:

- each candidate accepted
- caps reached and what was dropped

#### Outputs

- Candidate list for probe stage (in-memory objects)
- Evidence events describing candidate generation and pruning

---

### I) Type-Specific Probes (Budgeted, Deterministic)

#### Purpose

Produce measurable signals that inform classification, fingerprinting, and reporting

#### Probe classes

**1. Symmetric ciphertext probes**

- length and overhead patterns
- block alignment (mod 8/16)
- repetition patterns (ECB suspicion)
- entropy statistics (bounded; stable computation settings)
- controlled tamper checks (lab-only or policy-gated)

**2. PQC probes**

- fixed-length geometry fingerprints
- wrapper parsing evidence (SPKI/cert fields, algorithm identifiers)
- verify/decaps behavior (only if required inputs exist and policy allows)

**3. Hybrid probes**

- split scoring improvements
- run symmetric probes on AEAD-like region
- run PQC probes on KEM-like region

**4. Hash/KDF probes (audit-only)**

- format detection
- parameter extraction (salt length, iterations, memory cost, digest id)
- misconfiguration classification (weak params, unsafe defaults)
- **explicitly no recovery attempts**

#### Built-in controls

- per-probe timeout
- per-artifact probe budget
- limit probes to top-K candidates only
- emit "skipped due to budget/policy" events with reasons

#### Outputs

- Probe evidence events per candidate and per probe type
- Normalized error events (timeouts, tool failures, parsing failures)

---

### J) Implementation Fingerprinting (Light Inline, Deep Gated)

#### Purpose

Determine likely crypto library/implementation wiring patterns (especially for binaries)

#### J.1) Light fingerprinting (inline)

**Responsibilities**:

- string and import hints
- symbol presence and library linkage clues
- build IDs and metadata hints
- shallow API usage signatures

**Outputs**:

- fingerprint candidates with confidence
- evidence events describing observed signals

#### J.2) Deep fingerprinting (heavy pool only, gated)

**Trigger conditions (examples)**:

- model confidence low
- router ambiguity high
- fingerprinting would materially change outcome/report

**Controls**:

- strict concurrency caps (heavy pool)
- strict timeouts
- caching by binary hash + toolchain hash
- emit gating decision evidence (why deep was/was not run)

**Outputs**:

- deeper structural clues and wrapper layout hints as evidence events

---

### K) Heavy Escalation (Forensics-Safe, Rare)

Heavy workflows are allowed only when:

- explicitly enabled by run policy
- justified by structured triggers
- bounded by strict resource governance

#### Examples

- math/cryptanalysis workbench tasks (bounded metrics only)
- deep reverse engineering
- intensive protocol analysis
- PQC batch validation in special cases

#### Outputs

- structured metric events
- **never free-form essays as "results"**
- caching evidence (hit/miss, key derivation provenance)

---

### L) Evidence Emission Rules (Forensics Mode)

#### Non-negotiable

Every module action emits an event:

- success event with payload
- failure event with normalized error taxonomy
- skipped event with explicit policy/budget reason

Tools never write directly to features or reports

Raw logs are stored as referenced blobs, not dumped into events

#### Event categories typically include

- routing events
- parsing/triage events
- candidate generation events
- probe events
- fingerprint events
- heavy escalation request/result events
- job completion summary event

---

### M) Outputs of Forensics Mode (What You Deliver)

#### Per artifact

- Multi-label type classification with evidence trace
- Wrapper/container evidence and parsing outcomes
- Candidate regions and scores (where applicable)
- Probe results (signals, metrics, failure shapes)
- Implementation fingerprint candidates (and deep results when run)
- A final artifact summary event:
  - module outcomes
  - budgets/caps hit
  - confidence and ambiguity markers

#### System-level outputs

- Canonical evidence store (events + raw blob refs)
- Replayable feature tables (built later from evidence)
- Reports compiled from evidence and model outputs

---

### N) Forensics Mode Safety Controls (Absolutely Required)

- **No network by default**
- **Hash/KDF restricted to audit-only classification** unless explicitly authorized
- **Strict timeouts everywhere**
- **Candidate and probe budgets enforced**
- **Fail-closed routing rules** prevent dangerous workflows
- **Heavy escalation is gated and scarce**
- **Everything produces evidence**, including failures and skips

---

### P) Attack Applicability Module (NEW - Attack Router)

#### Purpose

Determine which of the 83 attacks are applicable to the artifact based on its classification

#### Inputs

- Artifact type classification (from Router module)
- Artifact metadata (size, wrapper type, algorithm hints)
- Run policy (which attack categories are enabled)

#### Responsibilities

**Build applicability map**:
```python
applicability = {
    "SYMMETRIC_CIPHERTEXT": {
        "always": [1, 2, 14],  # Frequency, Statistical, Brute Force
        "if_has_plaintext_hints": [4-10],  # Known/Chosen plaintext attacks
        "if_CBC_mode": [11, 62],  # Padding Oracle
        "if_weak_IV": [63],  # BEAST
    },
    "HASH_MATERIAL": {
        "always": [15-17, 69-70],  # Dictionary, Brute Force
        "if_unsalted": [16, 22],  # Rainbow tables
        "if_weak_params": [18-20],  # Collision attacks
    },
    "RSA_KEY": {
        "always": [13, 14, 40, 59, 73],  # Bleichenbacher, Timing, Weak Key, Shor
        "if_small_key": [14, 73],  # Brute force, Shor
    },
    # ... complete mapping for all types
}
```

**Filter by policy**:
- Exclude attacks not enabled in run policy
- Exclude simulation-only attacks if `allow_simulation=false`
- Exclude heavy attacks if `allow_heavy=false`

**Emit applicability event**:
```json
{
  "event_type": "attack_applicability",
  "artifact_id": "abc123",
  "applicable_attacks": [1, 2, 11, 14, 15, 62],
  "excluded_attacks": [73, 74, 75],  // Quantum (simulation-only)
  "exclusion_reasons": {"73": "quantum_simulation_disabled"},
  "total_applicable": 6,
  "estimated_time_hours": 2.5
}
```

#### Outputs

- List of applicable attack IDs
- Attack job specifications (priority, resource class, timeout)
- Applicability evidence event

---

### Q) Attack Execution Module (NEW - Attack Orchestrator)

#### Purpose

Execute each applicable attack 3 times and collect results

#### Execution Model

**Per-attack execution loop**:
```python
for attack_id in applicable_attacks:
    for attempt in [1, 2, 3]:
        result = execute_attack(
            attack_id=attack_id,
            artifact=artifact,
            attempt=attempt,
            timeout=get_attack_timeout(attack_id),
            resource_class=get_attack_resource_class(attack_id)
        )
        emit_event(type="attack_attempt", result=result)
```

#### Attack Resource Classification

**Light attacks** (execute in artifact worker pool):
- IDs: 1-3, 14-17, 38-39, 69-70, 81, 83
- Timeout: 30-300 seconds
- Parallel: Yes (across different attacks)

**Heavy attacks** (execute in heavy pool):
- IDs: 4-13, 21-37, 55-58, 73-75
- Timeout: 300-3600 seconds
- Parallel: Limited (2-5 concurrent)
- Requires: Specialized tools (Sage, Ghidra, liboqs)

**Simulation attacks** (special handling):
- IDs: 43-48, 52-54, 73-75, 76-78
- May require specialized hardware or simulation environment
- Often emit estimates rather than actual attack execution

#### Attack Tool Integration

**Mapping attacks to tools**:
```python
ATTACK_TOOLS = {
    1: "frequency_analyzer",      # Frequency Analysis
    4: "linear_cryptanalysis",    # Linear Cryptanalysis
    11: "padding_oracle_tool",    # Padding Oracle
    14: "hashcat",                # Brute Force
    15: "john",                   # Dictionary Attack
    16: "rainbow_crack",          # Rainbow Tables
    27: "matsui_linear",          # Linear Cryptanalysis
    40: "timing_analyzer",        # Timing Attack
    73: "shor_simulator",         # Shor Algorithm (simulation)
    # ... complete mapping
}
```

#### Deterministic Attack Execution

**Seeding per attempt**:
```python
attack_seed = SHA256(
    artifact_hash + 
    run_config_hash + 
    str(attack_id) + 
    str(attempt_number)
)
```

**Why 3 attempts**:
1. Statistical confidence in results
2. Detect nondeterministic attack behavior
3. Validate consistency of success/failure
4. Build variance metrics for modeling

#### Attack Outputs

**Per-attempt event**:
```json
{
  "event_type": "attack_attempt",
  "attack_id": 11,
  "attack_name": "Padding Oracle",
  "attack_category": "Chosen-Ciphertext",
  "attempt_number": 2,
  "artifact_id": "abc123",
  "attack_seq": 42,
  "event_seq": 1052,
  "result": "SUCCESS",
  "execution_time_ms": 2543,
  "queries_performed": 8234,
  "bytes_recovered": 32,
  "tool": "padding_oracle_tool",
  "tool_version": "2.1.0",
  "exit_code": 0,
  "stdout_ref": "s3://attacks/.../stdout.txt",
  "stderr_ref": "s3://attacks/.../stderr.txt",
  "recovered_data_ref": "s3://attacks/.../recovered.bin",
  "metrics": {
    "queries_per_second": 3243,
    "false_positive_rate": 0.02,
    "oracle_response_consistency": 0.98
  }
}
```

#### Built-in Controls

**Timeouts**:
- Per-attack timeout (from attack registry)
- Per-attempt timeout (same value for all 3 attempts)
- Global attack phase timeout

**Query budgets**:
- Max queries per attack (prevents infinite loops)
- Example: Padding Oracle limited to 10,000 queries
- Emit budget exhaustion event if hit

**Resource limits**:
- Memory cap (especially for algebraic attacks)
- CPU throttling for heavy pool attacks
- Network restrictions (most attacks run offline)

**Safety gates**:
- Hash attacks cannot use GPU unless explicitly enabled
- Simulation attacks cannot trigger real quantum hardware
- Fault injection attacks are simulation-only (no real hardware modification)

---

### R) Attack Aggregation Module (NEW - Result Consolidation)

#### Purpose

Aggregate 3 attack attempts into statistical summary and resistance profile

#### Responsibilities

**Per-attack aggregation**:
```python
def aggregate_attack_attempts(attempts):
    return {
        "success_count": count_successes(attempts),
        "failure_count": count_failures(attempts),
        "timeout_count": count_timeouts(attempts),
        "success_rate": success_count / 3,
        "consistency_score": measure_consistency(attempts),
        "average_time_ms": mean([a.time for a in attempts]),
        "recovered_data_consistent": check_data_consistency(attempts),
        "vulnerability_confirmed": success_count >= 2  # 2 of 3
    }
```

**Consistency scoring**:
- Perfect consistency: All 3 attempts have same result (1.0)
- Partial consistency: 2/3 same result (0.67)
- Inconsistent: All different results (0.0)

**Vulnerability confirmation**:
- **Confirmed**: ≥2 of 3 attempts succeeded
- **Possible**: 1 of 3 succeeded
- **Not vulnerable**: 0 of 3 succeeded
- **Inconclusive**: All 3 timed out or failed for different reasons

#### Attack Resistance Profile

**Per-artifact consolidated profile**:
```json
{
  "artifact_id": "abc123",
  "attacks_executed": 25,
  "attacks_per_category": {
    "Ciphertext-Only": 3,
    "Known-Plaintext": 4,
    "Brute-Force": 4,
    "Padding Oracle": 1,
    "Timing": 2,
    "Statistical": 3,
    ...
  },
  "vulnerabilities_confirmed": 3,
  "vulnerabilities_possible": 2,
  "not_vulnerable": 20,
  "resistance_score": 0.88,  // (not_vulnerable / total)
  "severity_breakdown": {
    "Critical": {"vulnerable": 0, "total": 0},
    "Very High": {"vulnerable": 1, "total": 5},
    "High": {"vulnerable": 2, "total": 12},
    "Medium": {"vulnerable": 0, "total": 6},
    "Low": {"vulnerable": 0, "total": 2}
  },
  "confirmed_vulnerabilities": [
    {
      "attack_id": 11,
      "attack_name": "Padding Oracle",
      "severity": "High",
      "success_rate": 0.67,
      "average_time_ms": 2310,
      "impact": "Full plaintext recovery possible"
    },
    {
      "attack_id": 40,
      "attack_name": "Timing Attack (RSA)",
      "severity": "Medium",
      "success_rate": 1.0,
      "average_time_ms": 523,
      "impact": "Private key bits leaked"
    }
  ],
  "recommendations": [
    "Migrate away from CBC mode with PKCS#7 padding",
    "Implement constant-time RSA operations",
    "Consider migration to PQC algorithms"
  ]
}
```

#### Outputs

- Attack summary events (per attack)
- Attack resistance profile (per artifact)
- Vulnerability confirmation events
- Attack features for ML modeling

---

## Tool-Backed Forensics Layer (Complete Module Details)

### O) Environment & Tool Orchestrator

#### Purpose

Standardize execution and normalize failures

#### Responsibilities

**Tool profiles**:

- `kali_profile`: openssl, tshark, radare2, hashcat, etc.
- `rhel_profile`: OpenSSL 3 + system crypto policies + PQC provider

**Standardized invocation**:

- isolated workspace paths
- bounded output
- timeouts

**Normalized error taxonomy**:

- parse failures
- decode failures
- tool failures
- timeouts

**Provenance capture**:

- tool versions
- command args
- env flags

#### Built-in fixes

- Enforce per-artifact temp dir via tool env variables
- Enforce "no network" unless explicitly enabled (security posture)

---

## Built-In Discipline Majors (Production Fixes You Must Ship Day One)

### A) Determinism Contract (Make Runs Diffable)

#### Requirements

Every event must include:

- `run_id` (UUID for this execution)
- `artifact_id` (stable artifact identity)
- `artifact_seq` (deterministic ordering number: 0, 1, 2, ...)
- `event_seq` (per-artifact event counter: 0, 1, 2, ...)
- `module_name` (which module emitted this)
- `timestamp_ns` (monotonic, assigned by writer)

#### Deterministic seed derivation

```python
seed = SHA256(artifact_hash + run_config_hash + module_name + artifact_seq)
# Never use: time.time(), random.random(), os.getpid(), system entropy
```

#### Single-writer architecture

- Workers produce events → submit to queue (channel/pipe/socket)
- Single writer thread consumes queue → assigns `event_seq` → persists to storage
- Writer is the source of truth for ordering

#### Testing determinism

```bash
# Run same artifact twice with same manifest
./forensics run --manifest run_001.json artifact.bin > events_001.jsonl
./forensics run --manifest run_001.json artifact.bin > events_002.jsonl
diff events_001.jsonl events_002.jsonl  # Must be identical
```

#### Common determinism breaks

- Tool outputs with timestamps → parse out stable fields only
- Floating point summations → use stable algorithm (Kahan summation) + round
- Hash iteration order (Python dicts pre-3.7) → use sorted keys
- Parallel map results → sort by stable key before emitting
- File globbing order (filesystem dependent) → sort paths before processing

---

### B) Resource Governance (Prevent Runaway Costs)

#### Separate worker pools

**Artifact pool (throughput tier)**:
- Max workers: 10-50 (tunable based on CPU cores)
- Target latency: seconds to minutes per artifact
- Concurrency model: parallel across artifacts, sequential within artifact

**Heavy pool (governor tier)**:
- Max workers: 2-4 (scarce resource)
- Target latency: minutes (with strict timeout)
- Concurrency model: gated by explicit triggers

#### Timeout hierarchy (nested, enforced at every level)

```
Run timeout (e.g., 24 hours)
├─ Artifact job timeout (e.g., 30 minutes)
│  ├─ Module timeout (e.g., 5 minutes)
│  │  ├─ Tool invocation timeout (e.g., 60 seconds)
│  │  │  └─ [tool runs with subprocess timeout]
│  │  └─ Probe timeout (e.g., 10 seconds per probe)
│  └─ Heavy escalation timeout (e.g., 10 minutes)
└─ Feature build timeout (e.g., 1 hour)
```

#### Budget enforcement

- **Candidate splits**: Hard cap at 100 per artifact
- **Probes per candidate**: Top-K only (K=10)
- **Heavy escalation**: Only if `policy.allow_heavy=true` AND trigger condition met
- **Math workbench**: Max N candidates (N=5), timeout per candidate

#### Enforcement mechanisms

```python
# Example: candidate cap enforcement
candidates = generate_candidates(artifact)
if len(candidates) > MAX_CANDIDATES:
    emit_event(type="candidate_cap_hit", count=len(candidates), max=MAX_CANDIDATES)
    candidates = prune_candidates(candidates, max_count=MAX_CANDIDATES)
```

---

### C) Failure Semantics (Failures Are Data, Not Bugs)

#### Core principle

Every failure must emit a structured event with:
- Failure category (timeout, parse_error, tool_error, etc.)
- Context (which tool, which input, what operation)
- Partial results (if any)
- Exit code / error message (normalized)

#### Normalized error taxonomy

```json
{
  "event_type": "tool_failure",
  "tool": "openssl",
  "operation": "asn1parse",
  "exit_code": 1,
  "error_category": "ASN1_TAG_MISMATCH",
  "stderr_snippet": "Error: expecting tag 0x30, got 0x04",
  "artifact_id": "...",
  "artifact_seq": 42,
  "event_seq": 105
}
```

#### Error categories (examples)

- `TIMEOUT`: process exceeded timeout
- `PARSE_ERROR`: malformed input detected
- `ASN1_TAG_MISMATCH`: specific ASN.1 parsing failure
- `TRUNCATED_INPUT`: input too short for expected structure
- `UNSUPPORTED_ALGORITHM`: algorithm ID not recognized
- `TOOL_CRASH`: segfault / uncaught exception
- `RESOURCE_EXHAUSTED`: OOM / disk full

#### No silent failures

```python
# BAD: swallow exception
try:
    result = parse_pem(artifact)
except Exception:
    pass  # WRONG: silent failure

# GOOD: emit failure event
try:
    result = parse_pem(artifact)
    emit_event(type="parse_success", result=result)
except ParseError as e:
    emit_event(type="parse_failure", error_category="PEM_DECODE_ERROR", 
               message=str(e))
    result = None  # continue with failure recorded
```

#### Partial results are valid

- If tool produces partial output before failure, emit both success (partial) + failure event
- Example: ASN.1 parser extracts first 3 fields before hitting error → emit both

---

### D) Isolation Rules (Prevent Cross-Contamination)

#### Per-artifact workspace isolation

```bash
# Create unique workspace per artifact job
workspace_root=/tmp/forensics/run_{run_id}/
artifact_workspace=${workspace_root}/artifact_{artifact_seq}/

# Set environment for tool invocations
export TMPDIR=${artifact_workspace}/tmp
export HOME=${artifact_workspace}/home
export XDG_CONFIG_HOME=${artifact_workspace}/config
```

#### No shared state

- Each artifact job gets fresh temp directory
- No global caches written during analysis (read-only caches OK)
- No shared lock files

#### Network isolation by default

```python
# Use network namespace or enforce via policy
subprocess.run(
    ["unshare", "--net", "openssl", "asn1parse", "-in", artifact_path],
    timeout=60,
    # Network unavailable in this namespace
)
```

#### Raw logs stored separately

```json
{
  "event_type": "tool_execution",
  "tool": "openssl",
  "exit_code": 0,
  "stdout_ref": "s3://evidence/blobs/af3c92.../stdout.txt",
  "stderr_ref": "s3://evidence/blobs/af3c92.../stderr.txt",
  "parsed_output": { /* structured fields only */ }
}
```

**Why**: Raw logs can be megabytes; don't bloat event stream. Reference by content hash.

#### Isolation testing

```bash
# Run two artifacts with same filename in parallel
./forensics run --parallel artifact1/file.bin artifact2/file.bin
# Verify no cross-talk (e.g., artifact1 events don't reference artifact2 data)
```

---

### E) Caching Rules (Make Scaling Affordable Without Corruption)

#### Cache key structure

```python
cache_key = {
    "artifact_hash": "sha256:abc123...",
    "toolchain_hash": "sha256:def456...",  # Hash of tool inventory
    "module": "deep_fingerprint",
    "module_version": "1.2.3"
}
```

#### Immutable cache entries

- Once written, cache entries are never modified
- Cache miss → compute → write
- Cache hit → read → emit event with `cache_hit=true`

#### Cache invalidation

```python
# When tool version changes, toolchain_hash changes
# Old cache entries remain but are never hit (different key)
# Optional: GC old entries after N days
```

#### Cache types

**Expensive RE (Ghidra analysis)**:
- Cache key: `(binary_hash, ghidra_version, analysis_script_hash)`
- Value: structural analysis results (JSON)
- TTL: 90 days

**Optional: CLI parsing results**:
- Cache key: `(artifact_hash, openssl_version)`
- Value: parsed ASN.1 structure
- TTL: 30 days
- Note: Only cache if parse is expensive (usually it's fast enough)

**PQC generation templates**:
- Cache key: `(algorithm, params, template_version, toolchain_hash)`
- Value: generated artifacts batch
- TTL: indefinite (immutable)

#### Cache observability

```json
{
  "event_type": "cache_access",
  "cache_name": "ghidra_analysis",
  "result": "hit",
  "key_hash": "sha256:...",
  "latency_ms": 5
}
```

#### Cache testing

```bash
# Run artifact, verify cache miss
./forensics run artifact.bin --no-cache
# Run again, verify cache hit
./forensics run artifact.bin  # should be faster
# Change tool version, verify cache miss
./forensics run artifact.bin --toolchain updated  # cache miss expected
```

---

### F) Observability Contract (Know Why Things Failed)

#### Every decision must be traceable

- Why did router assign label X? → Emit routing_evidence event with signals
- Why was heavy escalation triggered? → Emit trigger_evaluation event
- Why was candidate pruned? → Emit pruning_decision event with score

#### Event schema must support drill-down

```json
{
  "event_type": "routing_decision",
  "labels": ["HYBRID_BLOB", "KEM_TRANSCRIPT"],
  "confidence": {"HYBRID_BLOB": 0.85, "KEM_TRANSCRIPT": 0.72},
  "signals": [
    {"signal": "length_matches_kyber768", "weight": 0.4},
    {"signal": "has_asn1_wrapper", "weight": 0.3},
    {"signal": "entropy_high", "weight": 0.15}
  ]
}
```

#### Emit events at decision points, not just results

```python
# BAD: only emit final classification
emit_event(type="classification", label="AES_CBC")

# GOOD: emit decision trail
emit_event(type="length_check", length=32, matches="AES256_key")
emit_event(type="entropy_check", entropy=7.99, threshold=7.5, result="pass")
emit_event(type="block_alignment", mod16=0, result="aligned")
emit_event(type="classification", label="AES_CBC", confidence=0.9,
           evidence_count=3)
```

---

### G) Testing Contract (Validate Discipline Majors)

#### Determinism tests (must pass on every commit)

```bash
# Test: same input → same output
pytest tests/test_determinism.py::test_artifact_reproducibility

# Test: feature replay matches streaming
pytest tests/test_determinism.py::test_feature_replay_equivalence
```

#### Isolation tests

```bash
# Test: parallel runs don't collide
pytest tests/test_isolation.py::test_concurrent_artifacts

# Test: no shared temp files
pytest tests/test_isolation.py::test_workspace_separation
```

#### Timeout tests

```bash
# Test: all timeouts enforced
pytest tests/test_governance.py::test_timeout_enforcement

# Test: heavy pool concurrency cap
pytest tests/test_governance.py::test_heavy_pool_limit
```

#### Failure tests

```bash
# Test: tool failures produce events
pytest tests/test_failures.py::test_tool_error_event_emitted

# Test: no silent failures
pytest tests/test_failures.py::test_all_invocations_logged
```

#### Cache tests

```bash
# Test: cache invalidation on toolchain change
pytest tests/test_caching.py::test_cache_invalidation

# Test: cache hit/miss correctness
pytest tests/test_caching.py::test_cache_correctness
```

---

**Implementation order**: These are not "nice to haves" you add later. They are architectural foundations. Implement them in Phase 0-1, test them rigorously, then build modules on top. Retrofitting these contracts after building modules is a rewrite.

---

## Scaling to an Industry Product

### Phase 1: Single machine, production discipline

- Artifact parallel workers + heavy pool + single writer
- Object storage for blobs + JSONL/Parquet for events/features
- Works for thousands to tens of thousands artifacts per run

### Phase 2: Distributed execution (no architecture change)

- Scheduler backed by queue (Kafka/SQS)
- Artifact workers deployed horizontally (Kubernetes)
- Heavy pool becomes a dedicated service tier (scarce resource)
- Telemetry writer becomes log service (or writes to event store)

### Phase 3: Multi-tenant productization

- tenancy boundaries in registry and telemetry
- rate limits, quotas, priority queues
- audit logging and permission gating
- model versioning + evidence replay for compliance

---

## Storage Layout (Product-Ready with Attack Framework)

```
manifests/
  run_manifest.json
  tool_inventory.json
  attack_registry.json           # NEW: Metadata for all 83 attacks
  attack_applicability_map.json  # NEW: Attack → Artifact Type mappings

artifacts/
  blobs/ (immutable object storage)

telemetry/
  tool_run_events.jsonl
  module_events/
    router.jsonl
    cli_inspection.jsonl
    normalization.jsonl
    probes.jsonl
    re_fingerprint.jsonl
    math_workbench.jsonl
    pqc.jsonl
    hashes.jsonl
    attack_applicability.jsonl   # NEW
    attack_attempts.jsonl        # NEW: Individual attack executions
    attack_summaries.jsonl       # NEW: Aggregated 3-run results
    attack_resistance.jsonl      # NEW: Consolidated profiles
    
  attack_outputs/                 # NEW: Raw attack tool outputs
    blobs/
      {attack_id}_{artifact_id}_{attempt}/
        stdout.txt
        stderr.txt
        recovered_data.bin
        metrics.json
        tool_trace.log

features/
  features.parquet
  attack_features.parquet         # NEW: Attack results as ML features
  feature_schema.json
  attack_feature_schema.json      # NEW

models/
  model_registry/
  attack_prediction_models/       # NEW: Models trained on attack outcomes

reports/
  report_artifacts/
  attack_resistance_reports/      # NEW: Per-artifact vulnerability reports
```

---

## Corrected Feasibility Summary (No Wishcasting)

### Straightforward (Weeks, not months)

- **Artifact registry with content-addressed storage**: S3/MinIO + SQLite/Postgres registry
- **Basic run controller**: JSON manifests + tool version capture via subprocess
- **Job queue with stable ordering**: In-memory queue initially, message queue later
- **Simple worker pool**: Python multiprocessing or thread pool with semaphores
- **JSONL event logging**: Append-only writes with sequence numbers
- **File signature and magic byte detection**: Use `file` command + libmagic
- **PEM/DER parsing**: OpenSSL CLI wrappers with error capture
- **Basic timeout enforcement**: subprocess.run() with timeout parameter

### Requires Engineering Discipline (Months, very doable with focus)

**Single-writer telemetry with deterministic ordering**
- **Challenge**: Parallel workers + concurrent writes = race conditions
- **Solution**: Single dedicated writer thread/process consuming from queue
- **Gotcha**: Queue must preserve submission order (use numbered tickets)
- **Testing**: Parallel run determinism tests (same input → byte-identical output)

**Per-artifact workspace isolation**
- **Challenge**: Tool temp dirs, config files, environment variables leak across jobs
- **Solution**: Create unique `/tmp/artifact_{job_id}/` per job + custom TMPDIR/HOME
- **Gotcha**: Some tools ignore env vars and write to hardcoded paths
- **Testing**: Run two artifacts with colliding filenames in parallel, verify no cross-talk

**Deterministic seeding for all randomness**
- **Challenge**: Tools use system entropy, timestamps, PIDs for randomness
- **Solution**: Derive seeds from `SHA256(artifact_hash + run_config_hash + module_name)`
- **Gotcha**: Not all tools accept seeds; need wrappers or accept non-determinism for those tools
- **Testing**: Run same artifact 10 times, diff all outputs

**Tool inventory pinning and provenance**
- **Challenge**: Tool versions change, container rebuilds alter behavior
- **Solution**: Capture `tool --version`, binary SHA256, container digest at run start
- **Gotcha**: Version strings are unstructured; need parsing + normalization
- **Testing**: Compare manifests across runs, verify no drift

**Normalized error taxonomy**
- **Challenge**: Every tool has different error messages and exit codes
- **Solution**: Parse stderr/stdout + exit codes → structured error categories
- **Gotcha**: Regex-based parsing is brittle; needs maintenance per tool
- **Testing**: Inject known failures (truncated files, bad encoding), verify correct classification

**Candidate explosion control**
- **Challenge**: Hybrid artifacts can generate O(n²) candidate splits
- **Solution**: Hard cap at 100 candidates + deterministic scoring + top-K pruning
- **Gotcha**: Scoring heuristic must be deterministic (no floating point non-determinism)
- **Testing**: Craft adversarial input, verify cap is enforced

**Heavy pool concurrency governance**
- **Challenge**: Ghidra/Sage can consume 10GB+ RAM and saturate CPU
- **Solution**: Separate pool with max_workers=2-4, strict timeouts (5-10 min)
- **Gotcha**: Process isolation must be enforced (cgroups/containers)
- **Testing**: Launch 100 heavy jobs, verify only N run concurrently

**Caching by content hash with invalidation**
- **Challenge**: Cache hits must be safe (hash collisions = wrong results)
- **Solution**: SHA256 keys, store (hash, toolchain_hash) → results
- **Gotcha**: Cache invalidation on toolchain change requires tracking dependencies
- **Testing**: Change one tool version, verify cache misses for affected artifacts

### Hard but Feasible (Requires specialists, 6-12 months)

**Deep reverse engineering with Ghidra/radare2**
- **Reality check**: Ghidra analysis can take 30+ minutes for large binaries
- **Solution**: Cache by binary hash, run only when gated by trigger policy
- **Gotcha**: Ghidra is stateful and has quirks; needs custom scripting layer
- **Feasibility**: Doable but requires RE expertise + Ghidra API knowledge

**Math/cryptanalysis workbench (Sage, PARI)**
- **Reality check**: Some analyses are computationally expensive (minutes to hours)
- **Solution**: Strict budgets (e.g., max 10 candidates, 5 min timeout per candidate)
- **Gotcha**: Sage startup time is ~2-3 seconds; needs persistent process pool
- **Feasibility**: Doable with strict resource caps + queue throttling

**PQC toolchain integration (liboqs, real implementations)**
- **Reality check**: PQC APIs are evolving; bindings may break
- **Solution**: Pin specific liboqs version, container freeze
- **Gotcha**: KEM/signature parameter sets proliferate; need exhaustive test matrix
- **Feasibility**: Doable but needs PQC domain expertise + ongoing maintenance

**Streaming feature builder that matches batch exactly**
- **Reality check**: Streaming aggregations can have numerical drift vs batch
- **Solution**: Use identical code path for both modes, test equivalence rigorously
- **Gotcha**: Floating point associativity issues; use stable summation
- **Feasibility**: Doable with careful design + extensive testing

**Multi-label classification with confidence scoring**
- **Reality check**: Hybrid artifacts have ambiguous boundaries
- **Solution**: Router emits multiple labels with confidence, downstream modules handle sets
- **Gotcha**: Confidence calibration is hard; needs training data
- **Feasibility**: Doable but requires ML expertise

### What WILL Break in Production (and mitigations)

**1. Nondeterministic tool outputs**
- **Symptom**: Same artifact produces different evidence across runs
- **Cause**: Tools use timestamps, PIDs, system entropy in outputs
- **Mitigation**: Parse outputs to extract stable fields only; accept nondeterminism in unstable fields (log but don't diff)
- **Detection**: Automated diff tests on repeated runs

**2. Tool environment collisions**
- **Symptom**: Parallel jobs corrupt each other's temp files or configs
- **Cause**: Hardcoded paths in tools (e.g., `/tmp/tool.lock`)
- **Mitigation**: Per-artifact namespace (mount namespaces or unique temp dirs + env vars)
- **Detection**: Run stress tests with intentionally colliding artifacts

**3. Heavy workload runaway**
- **Symptom**: System becomes unresponsive, OOM kills workers
- **Cause**: Too many Ghidra/Sage jobs running simultaneously
- **Mitigation**: Strict heavy pool concurrency caps (N=2-4) + memory limits (cgroups)
- **Detection**: Resource monitoring + alerting on queue depth

**4. Silent tool failures**
- **Symptom**: Missing data in reports, no indication of failure
- **Cause**: Tool exit code 0 despite internal error, or partial output
- **Mitigation**: Every tool invocation emits event (success/failure/timeout); parse outputs for error markers
- **Detection**: Validate all expected fields present in events

**5. Event ordering corruption**
- **Symptom**: Evidence replays produce different features than original run
- **Cause**: Concurrent writes to event log without ordering guarantee
- **Mitigation**: Single-writer architecture with sequence numbers; workers submit to queue, writer consumes sequentially
- **Detection**: Replay tests (features from evidence must match original)

**6. Cache poisoning**
- **Symptom**: Wrong results served from cache after tool update
- **Cause**: Cache key doesn't include toolchain version
- **Mitigation**: Cache key = (artifact_hash, toolchain_hash); invalidate on toolchain change
- **Detection**: Verify cache miss after tool version bump

**7. Floating point nondeterminism**
- **Symptom**: Entropy calculations differ slightly across runs
- **Cause**: FP associativity, compiler optimizations, CPU architecture differences
- **Mitigation**: Use fixed precision (e.g., round to 6 decimals), stable summation algorithms
- **Detection**: Diff numeric features across runs on different machines

**8. Module interdependencies causing deadlocks**
- **Symptom**: Jobs hang waiting for heavy pool while heavy pool is full
- **Cause**: Light workers spawning heavy jobs without backpressure
- **Mitigation**: Heavy escalation must be async with timeout + fallback
- **Detection**: Deadlock detection (timeout on job completion)

**9. TOCTOU (Time-of-Check-Time-of-Use) in artifact registry**
- **Symptom**: Artifact modified between registry entry and analysis
- **Cause**: Mutable artifact storage
- **Mitigation**: Immutable blob storage (S3 versioning, content-addressed)
- **Detection**: Hash artifact at read time, verify matches registry

**10. Telemetry writer single point of failure**
- **Symptom**: Writer crash loses all subsequent events
- **Cause**: No redundancy in writer
- **Mitigation**: Periodic checkpoints, durable queue (Kafka), idempotent writes
- **Detection**: Health checks + alerting on writer process

---

**Bottom line**: This is feasible to implement and credible as an industry product **IF AND ONLY IF** you ship the discipline majors from day one. Attempting to "add determinism later" or "fix isolation after MVP" will result in a rewrite. The hard parts are not algorithms—they're operational discipline (isolation, determinism, failure-as-data, caching, timeouts). Get these wrong and you have a demo that works once, which is basically every security research project ever.

---

**That's Forensics Mode implemented as an actual build plan: what comes in, what runs, what gets emitted, what's forbidden, and how it stays reproducible.**

---

## Common Implementation Antipatterns (What NOT to Do)

### Antipattern 1: "We'll add determinism later"

**Symptom**: Build entire pipeline with prints/logs, plan to "make it deterministic" later

**Why it fails**: Non-deterministic code has dependencies baked into every layer. Retrofit requires rewrite.

**Correct approach**: Single-writer telemetry from day one. Workers emit events, never write directly.

---

### Antipattern 2: "Let's use filesystem for coordination"

**Symptom**: Workers write to shared directories, use lock files, check "done" files

**Why it fails**: Race conditions, TOCTOU bugs, no ordering guarantee, cleanup failures leave stale state

**Correct approach**: In-memory queues or message queue (Kafka/SQS) for coordination. Filesystem only for immutable blobs.

---

### Antipattern 3: "Exceptions are for exceptional cases"

**Symptom**: Tool failures raise exceptions, get caught at top level, logged generically

**Why it fails**: Loses context, no structured error data, failures are invisible in reports

**Correct approach**: Every failure emits structured event with category, context, partial results. Failures are data.

---

### Antipattern 4: "We'll optimize caching later"

**Symptom**: No caching initially. Later, add caching without considering cache key correctness.

**Why it fails**: Cache poisoning (wrong results after tool update), missing invalidation, cache hits on stale data

**Correct approach**: Design cache keys with `(artifact_hash, toolchain_hash)` from start. No cache is better than wrong cache.

---

### Antipattern 5: "Timeouts are for production"

**Symptom**: No timeouts during development. Add them later when jobs hang.

**Why it fails**: Timeout handling is control flow. Adding timeouts late breaks assumptions (e.g., "this always completes").

**Correct approach**: Timeout every subprocess, tool invocation, module, job from day one. Test timeout paths.

---

### Antipattern 6: "Just catch Exception and continue"

**Symptom**: Broad exception handlers swallow errors to keep pipeline running

**Why it fails**: Silent failures, missing data, no visibility into what broke

**Correct approach**: Catch specific exceptions, emit failure events, continue with failure recorded.

---

### Antipattern 7: "Floating point is close enough"

**Symptom**: Entropy calculations differ by 0.000001 across runs. "It's close enough."

**Why it fails**: Breaks determinism tests, diffs are noisy, features drift over time

**Correct approach**: Round to fixed precision, use stable summation, accept non-determinism only where documented.

---

### Antipattern 8: "Global state is convenient"

**Symptom**: Module initialization sets global variables, caches, config

**Why it fails**: Cross-artifact contamination, test pollution, non-reentrant code

**Correct approach**: Pass state explicitly (job context, workspace paths). Modules are pure functions.

---

### Antipattern 9: "Print debugging works fine"

**Symptom**: Scattered print statements, logs to stdout/stderr, no structure

**Why it fails**: Logs are unparseable, ordering is nondeterministic, grep is not a query language

**Correct approach**: Structured events only (JSON), single writer, queryable storage.

---

### Antipattern 10: "We'll scale when we need to"

**Symptom**: Design for single-machine, plan to "add distribution later"

**Why it fails**: Shared state assumptions (filesystem paths, in-process queues) don't transfer. Rewrite required.

**Correct approach**: Design for distribution from start (message queues, object storage). Run single-machine initially but architecture doesn't change.

---

### Antipattern 11: "Tool X never fails"

**Symptom**: Assume OpenSSL/Ghidra/etc. always succeeds. No error handling.

**Why it fails**: Tools fail on malformed inputs (the entire point of forensics). Pipeline crashes or produces garbage.

**Correct approach**: Every tool invocation can fail. Capture exit code, stderr, emit failure event.

---

### Antipattern 12: "Tests are expensive, we'll add them later"

**Symptom**: Build pipeline, plan to "add tests before shipping"

**Why it fails**: Untested code has hidden assumptions. Adding tests finds bugs that require refactoring.

**Correct approach**: TDD for discipline majors (determinism, isolation, timeouts). Test each module as built.

---

### Antipattern 13: "Parallel is faster, let's parallelize everything"

**Symptom**: Parallel execution within artifact job (parallel module invocation)

**Why it fails**: Nondeterministic ordering, race conditions, complex state management

**Correct approach**: Parallel across artifacts, sequential within artifact. Bounded parallelism only for proven-independent checks.

---

### Antipattern 14: "We'll document it later"

**Symptom**: No schema documentation for events, no manifest format spec, no module contracts

**Why it fails**: Impossible to validate, incompatible changes break replay, tribal knowledge only

**Correct approach**: Document schemas in code (Pydantic/JSON Schema). Generate docs from schemas.

---

### Antipattern 15: "Hash module can crack passwords, but we'll be careful"

**Symptom**: Hash module has recovery capabilities, rely on policy to prevent abuse

**Why it fails**: Someone will use it wrong (accidentally or intentionally). Security by policy doesn't work.

**Correct approach**: Hash module physically cannot crack (no dictionary, no GPU hooks). Audit-only mode is the only mode.

---

## Critical Implementation Dependencies (Build Order Matters)

### You CANNOT skip these ordering dependencies:

```
Phase 0: Storage + Data Models
    ↓
Phase 1: Run Controller + Tool Inventory + Telemetry Writer
    ↓ (determinism foundation must exist)
Phase 1: Job Scheduler + Worker Pools
    ↓ (infrastructure must exist)
Phase 2: Tool Orchestrator + Artifact Job Setup
    ↓ (execution environment must exist)
Phase 2: Modules (Router → CLI → Normalizer → Probes → Fingerprint)
    ↓ (modules must emit events)
Phase 4: Feature Builder + Models
    ↓ (features must exist)
Phase 4: Reports
```

**You CAN parallelize**:
- Different modules (after tool orchestrator exists)
- Different probe types (after probe framework exists)
- Tests (always, in parallel with development)

**You CANNOT parallelize**:
- Control plane before storage (no place to write manifests)
- Modules before tool orchestrator (no execution environment)
- Features before evidence (no data to process)
- Reports before features (no features to report on)

---

## Attack Framework Quick Reference

### Attack Execution Summary

**Total Attacks**: 83 across 25 categories

**Execution Model**: Each applicable attack runs **3 times** per artifact

**Attack Pools**:
- **Light Pool**: 50-100 concurrent (attacks 1-3, 14-17, 38-39, 69-70, 81, 83)
- **Heavy Pool**: 2-5 concurrent (attacks 4-13, 21-37, 55-58, 73-75)
- **Simulation Pool**: 1-2 concurrent (attacks 43-48, 52-54, 76-78)

**Per-Artifact Flow**:
```
1. Artifact Type Classification
2. Attack Applicability Determination (which of 83 apply?)
3. For each applicable attack:
   - Execute attempt 1 → emit event
   - Execute attempt 2 → emit event
   - Execute attempt 3 → emit event
   - Aggregate 3 attempts → emit summary
4. Generate Attack Resistance Profile
5. Store all outputs with artifact
```

**Outputs Per Artifact**:
- Individual attack attempt events (N × 3, where N = applicable attacks)
- Attack summary events (N summaries)
- Attack resistance profile (consolidated vulnerability assessment)
- Attack features for ML modeling
- Raw attack tool outputs (stdout, stderr, recovered data)

### Attack Categories by Severity

- **Critical (3)**: Quantum attacks (Shor, Grover) - simulation only
- **Very High (18)**: Brute force, DPA, cache attacks, fault injection, POODLE, Spectre
- **High (38)**: Linear/differential cryptanalysis, birthday, dictionary, BEAST, timing
- **Medium (18)**: Integral, correlation, acoustic, EM analysis
- **Low (6)**: Frequency analysis, chi-square, TEMPEST

### Attack Tool Dependencies

**Core Tools (MVP - 10-15 attacks)**:
- OpenSSL (CLI inspection, some attacks)
- hashcat (brute force, dictionary)
- john (password attacks)
- Custom tools (frequency, statistical, linear cryptanalysis basics)

**Advanced Tools (Full Suite - 83 attacks)**:
- Sage (algebraic attacks)
- Ghidra (reverse engineering for binary attacks)
- liboqs (PQC attacks)
- SCA simulators (power, EM, cache)
- Fault injection simulators
- Specialized cryptanalysis tools (MITM, differential, etc.)

**Hardware (Advanced Phase)**:
- Power analysis equipment ($50k-100k)
- EM probes ($30k-50k)
- Fault injection equipment ($200k-300k)
- Specialized oscilloscopes and analyzers

### Attack Framework Costs

**Development**:
- MVP (10-15 attacks): +3 months, +1 engineer, +$300k
- Full suite (83 attacks): +12 months, +2 engineers, +$2M
- Hardware SCA: +12 months, +1 engineer, +$1M (including equipment)

**Infrastructure (monthly)**:
- Light attack pool: +$2,300
- Heavy attack pool (doubled): +$5,000
- GPU instances (hashcat): +$6,000
- Storage (increased): +$500
- **Total increase**: +$14k/month (+$168k/year)

**ROI Justification**:
- **Without attacks**: Classify artifacts (what is it?)
- **With attacks**: Classify + validate security (what is it? is it vulnerable?)
- **Value add**: Vulnerability assessment, remediation recommendations, threat modeling
- **Target customers**: Security audit firms, government agencies, research labs

---

## Implementation To-Do List

### Phase 0: Foundation & Infrastructure

- [ ] **Storage Layer Setup**
  - [ ] Design and implement object storage backend for immutable artifacts
  - [ ] Create blob storage with content-addressable references
  - [ ] Set up JSONL/Parquet storage for telemetry events
  - [ ] Implement storage layout structure (manifests/, artifacts/, telemetry/, features/, models/, reports/)

- [ ] **Core Data Models**
  - [ ] Define artifact registry schema (artifact_id, artifact_hash, metadata)
  - [ ] Define run manifest schema (run_id, policies, tool inventory, job list)
  - [ ] Define evidence event schema (event types, sequences, timestamps)
  - [ ] Define feature table schema

### Phase 1: Control Plane

- [ ] **Run Controller**
  - [ ] Implement run_id generation
  - [ ] Build tool inventory capture (scan environment, capture versions/paths)
  - [ ] Implement OS profile detection (Kali/RHEL, container digests)
  - [ ] Create run policy configuration system
  - [ ] Implement deterministic seeding rules (artifact hash + config hash)
  - [ ] Build telemetry service initialization
  - [ ] Generate and persist run_manifest.json
  - [ ] Generate and persist tool_inventory.json

- [ ] **Artifact Registry & Ingestion**
  - [ ] Build API endpoint for artifact upload (REST/gRPC)
  - [ ] Build CLI for artifact submission
  - [ ] Build batch upload handler
  - [ ] Implement artifact_hash computation (SHA256 content hash)
  - [ ] Implement artifact_id generation (UUID)
  - [ ] Build metadata capture and validation
  - [ ] Implement registry persistence layer
  - [ ] Add permissions/ACL/tenant scope handling
  - [ ] Implement chain-of-custody logging

- [ ] **Artifact Job Scheduler**
  - [ ] Design job queue data structure
  - [ ] Implement artifact_seq assignment (deterministic ordering)
  - [ ] Build job metadata creation
  - [ ] Implement job class routing (light-only vs heavy-eligible)
  - [ ] Build backpressure controls (max in-flight limit)
  - [ ] Implement priority queue (interactive vs batch)
  - [ ] Prepare for queue backend integration (Kafka/SQS/Celery placeholder)

- [ ] **Worker Pool Management**
  - [ ] Implement artifact worker pool (throughput tier)
  - [ ] Implement heavy worker pool (governor tier)
  - [ ] Build worker health monitoring
  - [ ] Implement concurrency caps per pool
  - [ ] Build worker process isolation
  - [ ] Implement graceful shutdown handlers

- [ ] **Deterministic Telemetry Pipeline**
  - [ ] Implement single-writer event consumer
  - [ ] Build event sequencing logic (artifact_seq + event_seq)
  - [ ] Implement normalized timestamp generation
  - [ ] Build event persistence to JSONL/structured store
  - [ ] Implement raw log blob storage with references
  - [ ] Create event replay capabilities
  - [ ] Build telemetry query interface

### Phase 2: Tool-Backed Forensics Layer

- [ ] **Environment & Tool Orchestrator**
  - [ ] Define tool profiles (Kali, RHEL)
  - [ ] Build tool inventory scanner (OpenSSL, tshark, radare2, hashcat, etc.)
  - [ ] Implement per-artifact workspace isolation
  - [ ] Build tool invocation wrapper (standardized execution)
  - [ ] Implement timeout enforcement per tool
  - [ ] Build bounded output capture (stdout/stderr limits)
  - [ ] Implement normalized error taxonomy
  - [ ] Build tool provenance capture (version, args, env)
  - [ ] Implement "no network" enforcement
  - [ ] Add sandbox/containerization support

- [ ] **Artifact Job Setup**
  - [ ] Implement isolated workspace creation per artifact
  - [ ] Build deterministic seed derivation context
  - [ ] Implement fixed locale/formatting environment
  - [ ] Build safety posture application (network disable, privilege limits)
  - [ ] Emit "job start" evidence event

- [ ] **Artifact Type Router (Module)**
  - [ ] Implement magic bytes / file signature detection
  - [ ] Build MIME type detection
  - [ ] Create multi-label classification logic
  - [ ] Define type labels (SYM_CIPHERTEXT, KEM_TRANSCRIPT, SIGNATURE, HYBRID_BLOB, etc.)
  - [ ] Implement fail-closed routing rules
  - [ ] Build confidence scoring
  - [ ] Emit routing evidence events with signals
  - [ ] Implement unknown classification path

- [ ] **CLI Inspection Module**
  - [ ] Build PEM/DER format detection
  - [ ] Implement ASN.1 structure parsing
  - [ ] Add key/cert container identification
  - [ ] Implement TLS record structure detection
  - [ ] Build PCAP structure hints
  - [ ] Create "failure shapes" taxonomy (tag mismatch, truncation, etc.)
  - [ ] Implement strict timeouts
  - [ ] Emit wrapper evidence events
  - [ ] Emit normalized error events

- [ ] **Normalizer / Candidate Parser Module**
  - [ ] Implement prefix/suffix stability analysis
  - [ ] Build header/footer pattern detection
  - [ ] Create candidate split generation
  - [ ] Implement offset/length computation for regions
  - [ ] Build candidate scoring heuristics (deterministic)
  - [ ] Implement hard cap on candidate count
  - [ ] Build deterministic pruning logic
  - [ ] Emit candidate generation events
  - [ ] Emit budget cap hit events

- [ ] **Type-Specific Probes Module**
  - [ ] **Symmetric Ciphertext Probes**
    - [ ] Implement length/overhead pattern analysis
    - [ ] Build block alignment checks (mod 8/16)
    - [ ] Implement repetition pattern detection (ECB suspicion)
    - [ ] Build entropy statistics (stable computation)
    - [ ] Implement controlled tamper checks (policy-gated)
  - [ ] **PQC Probes**
    - [ ] Build fixed-length geometry fingerprinting
    - [ ] Implement SPKI/cert field parsing
    - [ ] Build verify/decaps behavior checks (policy-gated)
  - [ ] **Hybrid Probes**
    - [ ] Implement split scoring improvements
    - [ ] Run symmetric probes on AEAD-like regions
    - [ ] Run PQC probes on KEM-like regions
  - [ ] **Hash/KDF Probes (Audit-Only)**
    - [ ] Implement format detection (bcrypt, scrypt, argon2, etc.)
    - [ ] Build parameter extraction (salt length, iterations, memory cost)
    - [ ] Implement misconfiguration classification
    - [ ] Enforce no-recovery guarantees
  - [ ] Implement per-probe timeouts
  - [ ] Build per-artifact probe budgets
  - [ ] Implement top-K candidate limiting
  - [ ] Emit probe evidence events
  - [ ] Emit skipped events with reasons

- [ ] **Implementation Fingerprinting Module**
  - [ ] **Light Fingerprinting (inline)**
    - [ ] Build string/import extraction
    - [ ] Implement symbol presence detection
    - [ ] Add library linkage analysis
    - [ ] Extract build IDs and metadata
    - [ ] Build shallow API usage signatures
    - [ ] Emit fingerprint candidate events
  - [ ] **Deep Fingerprinting (heavy pool)**
    - [ ] Integrate Ghidra/radare2 for deep analysis
    - [ ] Implement trigger condition evaluation
    - [ ] Build gating decision logic
    - [ ] Implement caching by binary hash + toolchain hash
    - [ ] Add strict timeouts
    - [ ] Enforce heavy pool concurrency caps
    - [ ] Emit deep analysis events
    - [ ] Emit gating decision evidence

- [ ] **Heavy Escalation Module**
  - [ ] Build trigger policy evaluation
  - [ ] Implement math/cryptanalysis workbench integration (Sage/PARI)
  - [ ] Add deep reverse engineering workflows
  - [ ] Implement intensive protocol analysis
  - [ ] Build PQC batch validation
  - [ ] Enforce strict resource limits (time/memory/CPU)
  - [ ] Implement bounded runtime controls
  - [ ] Build result caching by hash
  - [ ] Emit structured metric events only (no essays)

- [ ] **Module Execution Orchestrator**
  - [ ] Implement deterministic module ordering
  - [ ] Build sequential execution within artifact job
  - [ ] Add bounded "quick-parallel" support for independent checks
  - [ ] Emit module start/end events
  - [ ] Emit completion summary event per artifact
  - [ ] Handle module skips with evidence
  - [ ] Handle module failures as data

### Phase 3: Attack Framework Implementation (NEW)

- [ ] **Attack Registry & Configuration**
  - [ ] Define attack_registry.json schema (all 83 attacks metadata)
  - [ ] Build attack_applicability_map.json (attack → artifact type mappings)
  - [ ] Implement attack severity and practicality metadata
  - [ ] Create attack category taxonomy (25 categories)
  - [ ] Define attack resource classification (light/heavy/simulation)
  - [ ] Build attack timeout and budget configuration per attack
  - [ ] Document attack tool requirements and dependencies

- [ ] **Attack Applicability Module**
  - [ ] Build artifact type → applicable attacks mapping logic
  - [ ] Implement policy-based attack filtering (enabled/disabled categories)
  - [ ] Create simulation attack gating logic
  - [ ] Build heavy attack permission checking
  - [ ] Implement attack priority and ordering logic
  - [ ] Emit attack applicability evidence events
  - [ ] Build estimated time calculation for attack suite

- [ ] **Attack Pool Management**
  - [ ] Implement light attack pool (high concurrency)
  - [ ] Implement heavy attack pool (throttled, 2-5 concurrent)
  - [ ] Implement simulation attack pool (special handling)
  - [ ] Build attack queue with priority routing
  - [ ] Add attack-specific resource limits (memory, CPU, queries)
  - [ ] Implement attack backpressure and throttling
  - [ ] Build attack pool monitoring and metrics

- [ ] **Attack Tool Integration**
  - [ ] **Ciphertext-Only Attacks (1-3)**
    - [ ] Integrate frequency_analyzer
    - [ ] Integrate statistical_attack_tool
    - [ ] Integrate correlation_analyzer
  - [ ] **Known/Chosen Plaintext (4-10)**
    - [ ] Integrate linear_cryptanalysis tool (Matsui)
    - [ ] Integrate differential_cryptanalysis tool
    - [ ] Integrate integral_cryptanalysis
    - [ ] Integrate biclique_attack
  - [ ] **Chosen Ciphertext (11-13)**
    - [ ] Integrate padding_oracle tool
    - [ ] Integrate POODLE attack tool
    - [ ] Integrate Bleichenbacher attack tool
  - [ ] **Brute-Force (14-17)**
    - [ ] Integrate hashcat for brute force
    - [ ] Integrate john for dictionary attacks
    - [ ] Integrate rainbow_crack for rainbow tables
    - [ ] Integrate hybrid dictionary tools
  - [ ] **Collision (18-20)**
    - [ ] Integrate birthday_attack tool
    - [ ] Integrate collision_finder
    - [ ] Integrate multi-collision tool
  - [ ] **Time/Memory (21-23)**
    - [ ] Integrate MITM attack tools
    - [ ] Integrate rainbow chain generator
    - [ ] Integrate Hellman table generator
  - [ ] **Differential (24-26)**
    - [ ] Integrate impossible differential tool
    - [ ] Integrate boomerang attack
  - [ ] **Linear (27-29)**
    - [ ] Integrate linear cryptanalysis (block)
    - [ ] Integrate linear cryptanalysis (stream)
    - [ ] Integrate differential-linear attack
  - [ ] **MITM (30-32)**
    - [ ] Integrate double encryption attack
    - [ ] Integrate 3DES break tool
    - [ ] Integrate generalized MITM
  - [ ] **Algebraic (33-36)**
    - [ ] Integrate interpolation attack (Sage)
    - [ ] Integrate cube attack
    - [ ] Integrate algebraic attack (Sage)
    - [ ] Integrate linearization attack
  - [ ] **Statistical (37-39)**
    - [ ] Integrate correlation attack
    - [ ] Integrate chi-square test
    - [ ] Integrate mod-n analysis
  - [ ] **Timing SCA (40-42)**
    - [ ] Integrate timing_analyzer (RSA)
    - [ ] Integrate Lucky 13 attack tool
    - [ ] Integrate constant-time bypass detector
  - [ ] **Power/EM/Cache/Acoustic SCA (43-54)**
    - [ ] Build SCA simulation framework
    - [ ] Integrate power analysis simulators (SPA/DPA)
    - [ ] Integrate EM analysis simulators
    - [ ] Integrate cache attack tools (Flush+Reload, Prime+Probe, Evict+Time)
    - [ ] Integrate acoustic analysis (simulation)
  - [ ] **Fault Injection (55-58)**
    - [ ] Build fault injection simulation framework
    - [ ] Integrate differential fault analysis
    - [ ] Simulate voltage/clock/laser glitch attacks
  - [ ] **Weak Key (59-61)**
    - [ ] Integrate weak key detector
    - [ ] Integrate related-key attack
    - [ ] Integrate key clustering analyzer
  - [ ] **Protocol (62-65)**
    - [ ] Integrate padding oracle (CBC)
    - [ ] Integrate BEAST attack
    - [ ] Integrate CRIME attack
    - [ ] Integrate BREACH attack
  - [ ] **Downgrade (66-68)**
    - [ ] Integrate POODLE downgrade
    - [ ] Integrate DROWN attack
    - [ ] Integrate SSLv2 downgrade detector
  - [ ] **Password (69-72)**
    - [ ] Integrate dictionary attacks (john, hashcat)
    - [ ] Integrate rainbow tables (rainbow_crack)
    - [ ] Integrate credential stuffing detector
  - [ ] **Quantum (73-75)**
    - [ ] Build Shor algorithm simulator (RSA/DLP)
    - [ ] Build Grover algorithm simulator (symmetric)
    - [ ] Implement time-to-break estimation
  - [ ] **Speculation (76-78)**
    - [ ] Build Spectre/Meltdown simulation
    - [ ] Build transient execution analyzer
  - [ ] **Other (79-83)**
    - [ ] Integrate rectangle attack
    - [ ] Integrate slide attack
    - [ ] Integrate key-recovery tools
    - [ ] Integrate distinguishing attack

- [ ] **Attack Execution Orchestrator**
  - [ ] Implement 3×repeat execution logic per attack
  - [ ] Build deterministic seeding per attempt
  - [ ] Implement per-attack timeout enforcement
  - [ ] Build query budget enforcement
  - [ ] Implement attack attempt evidence emission
  - [ ] Build attack stdout/stderr capture and storage
  - [ ] Implement recovered data storage (if success)
  - [ ] Build attack metrics collection
  - [ ] Handle attack failures as data (structured events)
  - [ ] Implement attack tool error normalization

- [ ] **Attack Aggregation Module**
  - [ ] Implement 3-run statistical aggregation
  - [ ] Build consistency scoring algorithm
  - [ ] Implement vulnerability confirmation logic (2 of 3 rule)
  - [ ] Build attack summary event generation
  - [ ] Create attack resistance profile per artifact
  - [ ] Calculate resistance score
  - [ ] Build severity breakdown analysis
  - [ ] Generate attack-based recommendations
  - [ ] Emit consolidated resistance evidence

- [ ] **Attack Result Storage**
  - [ ] Implement attack attempt event persistence (JSONL)
  - [ ] Implement attack summary event persistence
  - [ ] Build attack_outputs blob storage
  - [ ] Implement attack resistance profile storage
  - [ ] Create attack features for ML (Parquet)
  - [ ] Build attack result query interface

### Phase 4: PQC Toolchain Integration

- [ ] **PQC Validation**
  - [ ] Integrate liboqs for KEM operations
  - [ ] Implement signature verification
  - [ ] Build decapsulation workflows
  - [ ] Add SPKI/DER key parsing
  - [ ] Emit validation evidence events

- [ ] **PQC Dataset Expansion (Heavy Pool)**
  - [ ] Build KEM artifact generation
  - [ ] Build signature artifact generation
  - [ ] Implement hybrid construction generation
  - [ ] Add wrapper realism variants (core bytes, DER/SPKI, TLS-ish)
  - [ ] Implement deterministic seed derivation for generation
  - [ ] Add toolchain version pinning enforcement
  - [ ] Emit generation events with provenance

### Phase 5: Evidence → Features → Models

- [ ] **Feature Builder**
  - [ ] Implement streaming feature builder (real-time)
  - [ ] Implement batch feature builder (replay from evidence)
  - [ ] Build wrapper evidence feature extraction
  - [ ] Build implementation fingerprint feature extraction
  - [ ] Build probe result feature extraction
  - [ ] Build math metrics feature extraction
  - [ ] Build PQC geometry feature extraction
  - [ ] Build hash/KDF parameter features
  - [ ] Ensure streaming and batch produce identical results
  - [ ] Persist features to Parquet

- [ ] **Tiered Models**
  - [ ] Build Tier 0: artifact type confirmation model
  - [ ] Build Tier 1: family classification per type
  - [ ] Build Tier 2: parameter set/mode classification
  - [ ] Build Tier 3: deployment/wrapper pattern model (optional)
  - [ ] Implement OOS (out-of-sample) detection
  - [ ] Build model versioning system
  - [ ] Store model outputs as evidence events
  - [ ] Build model registry

- [ ] **Reporting Layer**
  - [ ] Design report templates
  - [ ] Build evidence trace visualization
  - [ ] Implement wrapper vs core vs fingerprint breakdown
  - [ ] Add toolchain manifest references
  - [ ] Show failure events and confidence drops
  - [ ] Build per-artifact reports
  - [ ] Build system-level summary reports
  - [ ] Create report artifacts storage

### Phase 6: Production Discipline (Built-In Fixes)

- [ ] **Determinism Contract**
  - [ ] Enforce run_id, artifact_id, artifact_seq, event_seq in all events
  - [ ] Validate deterministic seed derivation everywhere
  - [ ] Test and verify single-writer stable ordering
  - [ ] Build run diff tooling (compare runs)

- [ ] **Resource Governance**
  - [ ] Implement separate budgets for artifact workers and heavy pool
  - [ ] Enforce hard timeouts at all levels (tool, probe, module, job)
  - [ ] Implement bounded candidate splits
  - [ ] Implement probe budgets
  - [ ] Add resource monitoring and alerting

- [ ] **Failure Semantics**
  - [ ] Ensure all failures emit normalized events
  - [ ] Build failure taxonomy (tool errors, parse failures, timeouts)
  - [ ] Test failure-as-data paths
  - [ ] Validate no silent failures anywhere

- [ ] **Isolation Rules**
  - [ ] Test per-artifact workspace isolation
  - [ ] Validate no shared temp dirs
  - [ ] Enforce no network by default
  - [ ] Verify raw logs are stored separately with references
  - [ ] Test tool environment isolation

- [ ] **Caching Rules**
  - [ ] Implement caching for expensive steps by immutable hash
  - [ ] Cache binary hash → RE results
  - [ ] Cache artifact hash → CLI parsing (optional)
  - [ ] Cache PQC generation templates
  - [ ] Implement cache invalidation on toolchain hash change
  - [ ] Build cache hit/miss metrics

### Phase 7: Observability & Operations

- [ ] **Per-Run Visibility**
  - [ ] Build progress tracking by job count
  - [ ] Show module stage progress
  - [ ] Track success/fail/timeout counts
  - [ ] Build run dashboard

- [ ] **Per-Module Visibility**
  - [ ] Track runtime percentiles
  - [ ] Build failure taxonomy rates
  - [ ] Track tool version failure correlation
  - [ ] Build module performance dashboard

- [ ] **Heavy Pool Visibility**
  - [ ] Track queue depth
  - [ ] Measure wait times
  - [ ] Track cache hit rates
  - [ ] Build heavy pool monitoring dashboard

- [ ] **System Health**
  - [ ] Implement health checks for all services
  - [ ] Build alerting for failures and anomalies
  - [ ] Track throughput metrics
  - [ ] Monitor resource utilization

### Phase 8: Testing & Validation

- [ ] **Unit Tests**
  - [ ] Test artifact registry operations
  - [ ] Test run controller logic
  - [ ] Test job scheduler
  - [ ] Test each forensics module independently
  - [ ] Test telemetry pipeline
  - [ ] Test feature builder

- [ ] **Integration Tests**
  - [ ] Test full pipeline with synthetic artifacts
  - [ ] Test determinism (same input → same output)
  - [ ] Test isolation (parallel jobs don't collide)
  - [ ] Test timeout enforcement
  - [ ] Test failure paths
  - [ ] Test caching correctness

- [ ] **End-to-End Tests**
  - [ ] Test ciphertext analysis flow
  - [ ] Test PQC artifact flow
  - [ ] Test hash/KDF analysis flow
  - [ ] Test binary analysis flow
  - [ ] Test hybrid artifact flow
  - [ ] Test heavy escalation flow

- [ ] **Reproducibility Tests**
  - [ ] Run same artifact multiple times, verify identical evidence
  - [ ] Test feature replay from evidence
  - [ ] Test report regeneration from evidence
  - [ ] Verify tool inventory pinning works

- [ ] **Safety Tests**
  - [ ] Verify hash module cannot trigger recovery
  - [ ] Verify fail-closed routing blocks dangerous paths
  - [ ] Verify network isolation
  - [ ] Verify resource limits work
  - [ ] Test timeout enforcement under load

- [ ] **Attack Framework Tests (NEW)**
  - [ ] Test attack applicability routing (correct attacks for artifact types)
  - [ ] Test 3×repeat execution determinism (same seed → same results)
  - [ ] Test attack timeout enforcement
  - [ ] Test attack query budget enforcement
  - [ ] Test attack pool concurrency limits (heavy pool caps work)
  - [ ] Test attack result aggregation (consistency scoring correct)
  - [ ] Test vulnerability confirmation logic (2 of 3 rule)
  - [ ] Test attack resistance profile generation
  - [ ] Test attack tool error handling (failures emit events)
  - [ ] Test attack output storage (blobs, events, summaries)
  - [ ] Validate all 83 attacks emit structured events
  - [ ] Test attack feature extraction for ML
  - [ ] End-to-end attack validation flow per artifact type

### Phase 9: Scaling & Productization

- [ ] **Distributed Execution Preparation**
  - [ ] Abstract job queue behind interface
  - [ ] Prepare for Kafka/SQS integration
  - [ ] Prepare for Kubernetes job deployment
  - [ ] Design horizontal scaling strategy for workers

- [ ] **Multi-Tenancy**
  - [ ] Implement tenancy boundaries in registry
  - [ ] Add tenancy to telemetry
  - [ ] Build rate limits per tenant
  - [ ] Implement quotas
  - [ ] Build tenant isolation

- [ ] **API & Interface**
  - [ ] Build REST API for artifact submission
  - [ ] Build REST API for run status queries
  - [ ] Build REST API for report retrieval
  - [ ] Build CLI tool
  - [ ] Build SDK/client libraries
  - [ ] Document API

- [ ] **Deployment & Operations**
  - [ ] Build deployment automation (Terraform/Kubernetes)
  - [ ] Create container images with pinned tool versions
  - [ ] Build configuration management
  - [ ] Create operational runbooks
  - [ ] Build backup/disaster recovery procedures
  - [ ] Implement audit logging

### Phase 10: Documentation

- [ ] Write architecture overview
- [ ] Document all modules and their contracts
- [ ] Document evidence event schemas
- [ ] Document feature schemas
- [ ] Create operator guide
- [ ] Create developer guide
- [ ] Write API reference
- [ ] Create troubleshooting guide
- [ ] Document security posture and safety controls

---

## Critical Path (Minimum Viable Product with Attack Validation)

For a working MVP, focus on:

1. **Core Infrastructure** (Phase 0 + Phase 1 basics)
2. **Simple Artifact Flow** (Registry → Scheduler → Worker → Telemetry)
3. **2-3 Basic Modules** (Router + CLI Inspection + Basic Probes)
4. **Attack Registry & Applicability** (10-15 core attacks only) **(NEW)**
5. **Attack Pools** (Light + Basic Heavy) **(NEW)**
6. **Core Attack Integration** **(NEW)**:
   - Frequency Analysis (1)
   - Statistical Attack (2)
   - Linear Cryptanalysis (4)
   - Padding Oracle (11)
   - Brute Force (14)
   - Dictionary Attack (15-16)
   - Linear Cryptanalysis Block (27)
   - Timing Attack RSA (40)
   - Dictionary + Hybrid (69-70)
7. **3×Repeat Execution + Aggregation** **(NEW)**
8. **Evidence Store** (Simple JSONL persistence + attack events)
9. **Basic Feature Extraction** (Batch mode + attack features)
10. **Simple Report** (Evidence trace + basic classification + attack resistance profile)
11. **Essential Safety** (Timeouts + Isolation + No-network + Attack budgets)
12. **Basic Tests** (Unit + Integration + Attack validation for critical path)

**MVP Delivers**:
- Artifact analysis with 10-15 validated attacks
- Each attack run 3 times for statistical confidence
- Attack resistance profile per artifact
- Full evidence traceability

Then iterate to add:
- Remaining 68+ attacks (phases)
- Heavy pool attacks (algebraic, SCA, fault injection)
- Advanced models
- Distributed execution
- Hardware SCA integration

---

## Implementation Complexity Matrix

| Component | Complexity | Time Estimate | Critical Dependencies | Risk Level | Notes |
|-----------|-----------|---------------|----------------------|------------|-------|
| **Object storage backend** | Low | 1-2 weeks | None | Low | Use S3/MinIO, well-trodden path |
| **Artifact registry** | Low | 1-2 weeks | Object storage | Low | SQLite/Postgres + simple CRUD |
| **Run controller + manifest** | Low-Med | 2-3 weeks | Storage | Med | Tool inventory capture is tricky |
| **Job scheduler (in-memory)** | Med | 2-3 weeks | Registry | Med | Stable ordering is critical |
| **Single-writer telemetry** | Med | 3-4 weeks | Scheduler | High | Get this wrong = nondeterminism everywhere |
| **Worker pool (basic)** | Med | 2-3 weeks | Scheduler, Telemetry | Med | Process isolation is key |
| **Tool orchestrator** | Med-High | 4-6 weeks | Worker pool | High | Error normalization is tedious |
| **Artifact workspace isolation** | Med | 2-3 weeks | Worker pool | High | Env var leakage is subtle |
| **Timeout enforcement** | Med | 2-3 weeks | Tool orchestrator | Med | Nested timeouts need testing |
| **Router module** | Med | 3-4 weeks | Tool orchestrator | Med | Multi-label logic is fiddly |
| **CLI inspection module** | Med | 3-4 weeks | Tool orchestrator | Low | Wrapper for OpenSSL mostly |
| **Normalizer module** | Med-High | 4-5 weeks | Router | Med | Candidate explosion control is critical |
| **Symmetric probes** | Med | 3-4 weeks | Normalizer | Low | Entropy, alignment, etc. straightforward |
| **PQC probes** | High | 6-8 weeks | Normalizer, liboqs | High | PQC tooling is evolving |
| **Hash probes (audit-only)** | Med | 3-4 weeks | Router | High | Security: must not enable cracking |
| **Light fingerprinting** | Med | 3-4 weeks | CLI inspection | Low | Strings/symbols extraction |
| **Heavy pool** | Med-High | 4-5 weeks | Worker pool | High | Concurrency cap enforcement critical |
| **Deep fingerprinting (Ghidra)** | High | 8-12 weeks | Heavy pool | High | Requires RE expertise |
| **Math workbench (Sage)** | High | 8-10 weeks | Heavy pool | High | Requires crypto/math expertise |
| **PQC dataset generation** | High | 6-8 weeks | Heavy pool, liboqs | High | Determinism + versioning critical |
| **Feature builder (batch)** | Med | 4-5 weeks | Telemetry | Med | Replay correctness testing needed |
| **Feature builder (streaming)** | High | 6-8 weeks | Batch builder | High | Must match batch exactly |
| **Tiered models (Tier 0-1)** | Med-High | 6-8 weeks | Features | Med | ML expertise required |
| **Tiered models (Tier 2-3)** | High | 8-10 weeks | Tier 0-1 | Med | Training data acquisition hard |
| **Reporting layer** | Med | 4-5 weeks | Models | Low | Templating + evidence trace |
| **Caching layer** | Med | 3-4 weeks | Any cached component | High | Invalidation correctness critical |
| **Observability/monitoring** | Med | 4-6 weeks | All components | Med | Ongoing throughout project |
| **Attack registry & config** | Low-Med | 2-3 weeks | None | Med | 83 attacks metadata |
| **Attack applicability module** | Med | 3-4 weeks | Router | Med | Mapping logic complex |
| **Attack pool management** | Med-High | 4-5 weeks | Worker pools | High | Resource governance critical |
| **Attack tool integration (basic)** | Med-High | 6-8 weeks | Attack pools | High | 10-15 key attacks first |
| **Attack tool integration (full)** | Very High | 16-24 weeks | Basic attacks | Very High | All 83 attacks + tools |
| **Attack execution orchestrator** | Med-High | 4-6 weeks | Attack tools | High | 3×repeat logic + seeding |
| **Attack aggregation module** | Med | 3-4 weeks | Orchestrator | Med | Statistical analysis |
| **Attack result storage** | Med | 2-3 weeks | Telemetry | Low | Extend existing storage |
| **Testing framework** | Med | 3-4 weeks | None (parallel) | High | Needed from day one |
| **Distributed execution (K8s)** | High | 10-12 weeks | Single-machine working | Med | Async after core works |
| **Multi-tenancy** | Med-High | 6-8 weeks | Distributed | Med | Async, productization phase |

---

## Realistic Project Timeline

### Minimal Viable Product (MVP)
**Goal**: Single-machine system analyzing ciphertexts and keys with basic classification and 10-15 core attacks

**Timeline**: 9-12 months with 3-4 engineers

**Includes**:
- Object storage + registry
- Run controller + telemetry (single-writer)
- Job scheduler + worker pool (artifact-parallel)
- Tool orchestrator + workspace isolation
- Router + CLI inspection + symmetric probes
- **Attack registry + applicability module (NEW)**
- **Attack pools (light + basic heavy) (NEW)**
- **10-15 core attacks integrated (1, 2, 4, 11, 14-17, 27, 40, 69-70) (NEW)**
- **3×repeat execution + aggregation (NEW)**
- Basic feature extraction (batch mode) including attack features
- Simple classification (Tier 0-1 models)
- Essential safety (timeouts, isolation, no-network)
- Core tests (determinism, isolation, failures, attack validation)

**Excludes**:
- Full 83-attack suite (only core 10-15 attacks)
- Advanced heavy pool attacks (Sage, algebraic, SCA simulations)
- PQC probes (use liboqs later)
- Streaming features
- Tier 2-3 models
- Distributed execution
- Multi-tenancy

---

### Production-Ready System
**Goal**: Industry-grade system with heavy analysis, PQC support, full 83-attack suite, distributed execution

**Timeline**: 24-30 months with 5-7 engineers

**Includes**:
- Everything in MVP
- **Full 83-attack suite integrated (all categories) (NEW)**
- **Advanced attack tools (Sage algebraic, SCA simulations, fault injection) (NEW)**
- **Attack resistance profiling + recommendations (NEW)**
- **Attack-based ML models (vulnerability prediction) (NEW)**
- Heavy pool + Ghidra integration + Sage workbench
- PQC probes + dataset generation
- Hash/KDF audit module
- Streaming + batch features (tested equivalent) including attack features
- Tiered models (Tier 0-3 + OOS detection)
- Caching layer (with invalidation) including attack result caching
- Comprehensive observability including attack pool metrics
- Distributed execution (Kubernetes)
- Full test coverage (unit + integration + E2E + all attacks)
- Multi-tenancy + quotas

**Excludes**:
- Advanced modeling techniques (can iterate)
- Protocol capture analysis (complex, add later)
- Dynamic analysis (sandbox execution)
- Real hardware-based SCA (simulation only)

---

### Production-Ready + Advanced Features
**Goal**: Enterprise product with all bells and whistles including real hardware SCA

**Timeline**: 36-48 months with 8-12 engineers

**Includes**:
- Everything in Production-Ready
- **Real hardware-based SCA testing (power/EM/acoustic with actual equipment) (NEW)**
- **Physical fault injection lab (voltage/clock/laser glitching) (NEW)**
- **Quantum threat assessment and PQC migration planning (NEW)**
- **Attack correlation analysis (multi-attack patterns) (NEW)**
- Protocol capture analysis (PCAP/TLS dissection)
- Binary dynamic analysis (sandboxed execution)
- Advanced modeling (ensemble, deep learning) for attack prediction
- Real-time interactive mode with live attack execution
- Multi-region deployment
- SLAs and compliance certifications
- Customer-facing UI/dashboard with attack visualization
- Automated vulnerability remediation recommendations

---

## Team Composition Recommendations

### MVP Phase (9-12 months)
- **1x Backend Engineer (Senior)**: Control plane, telemetry, worker pools, attack pools
- **2x Security/Crypto Engineers**: Tool orchestrator, modules, attack integration, safety controls
- **1x DevOps/Infra Engineer**: Storage, containerization, testing infrastructure
- *Part-time: ML Engineer for basic models*
- *Part-time: Cryptanalysis Expert for attack validation*

### Production Phase (24-30 months)
- **2x Backend Engineers (Senior)**: Distributed execution, caching, scaling, attack orchestration
- **3x Security/Crypto Engineers**: Heavy modules (RE, math workbench), full attack suite, PQC integration
- **1x Cryptanalysis Specialist**: Advanced attacks (algebraic, SCA, fault injection)
- **1x ML Engineer**: Feature engineering, tiered models, attack prediction, OOS detection
- **1x DevOps/SRE Engineer**: Kubernetes, monitoring, reliability, attack infrastructure
- *Part-time: Product Manager for prioritization*

### Advanced Phase (36-48 months)
- **3x Backend Engineers**: Protocol analysis, dynamic analysis, performance, attack correlation
- **3x Security/Crypto Engineers**: Advanced analysis, new cryptosystems, hardware SCA integration
- **1x Hardware Security Engineer (NEW)**: Physical SCA lab, fault injection, equipment integration
- **2x ML Engineers**: Advanced modeling, attack prediction, A/B testing, model deployment
- **1x Frontend Engineer**: UI/dashboard with attack visualization
- **2x DevOps/SRE Engineers**: Multi-region, compliance, reliability, attack infrastructure scaling
- **1x Product Manager**: Customer feedback, roadmap, prioritization

---

## Budget Reality Check

### Infrastructure Costs (Monthly, Production Scale with Attack Framework)

| Resource | Spec | Cost (AWS) | Notes |
|----------|------|-----------|-------|
| **Artifact worker nodes** | 10x c5.2xlarge | ~$2,500 | 8 vCPU, 16GB each |
| **Light attack pool nodes** | 15x c5.xlarge | ~$2,300 | 4 vCPU, 8GB each (NEW) |
| **Heavy attack pool nodes** | 8x c5.9xlarge | ~$10,000 | 36 vCPU, 72GB each (doubled for attacks) |
| **GPU instances (hashcat)** | 2x p3.2xlarge | ~$6,000 | V100 GPU for brute force (NEW) |
| **Object storage (S3)** | 25TB + requests | ~$625 | Artifacts + attack outputs + raw logs (increased) |
| **Event storage (Parquet)** | 3TB + requests | ~$90 | Telemetry + attack events (increased) |
| **Database (RDS)** | db.r5.2xlarge | ~$1,000 | Registry + metadata + attack registry (upgraded) |
| **Message queue (MSK)** | 3 brokers | ~$800 | Job queue (if Kafka) |
| **Monitoring** | CloudWatch/Datadog | ~$800 | Logs + metrics + alerts + attack metrics |
| **Load balancers** | 2x ALB | ~$50 | API ingress |
| **Total** | | **~$24,165/mo** | ~$290k/year |

### Personnel Costs (Annual, Loaded - Production Phase)

| Role | Count | Salary (US) | Notes |
|------|-------|-------------|-------|
| **Senior Backend Engineer** | 2 | $180k | $360k total |
| **Security/Crypto Engineer** | 3 | $200k | $600k total (specialized, attack integration) |
| **Cryptanalysis Specialist** | 1 | $220k | $220k (highly specialized, attack expertise) |
| **ML Engineer** | 1 | $170k | $170k |
| **DevOps/SRE Engineer** | 1 | $160k | $160k |
| **Product Manager** | 0.5 | $150k | $75k (part-time) |
| **Total** | 8.5 | | **$1.59M/year** |

### Total 4-Year Cost Projection (With Attack Framework)

| Phase | Duration | Personnel | Infrastructure | Total |
|-------|----------|-----------|----------------|-------|
| **MVP (10-15 attacks)** | 12 months | $950k | $60k | **$1.01M** |
| **Production (Full 83 attacks)** | 18 months | $2.4M | $435k | **$2.84M** |
| **Advanced (Hardware SCA)** | 18 months | $2.3M | $550k | **$2.85M** |
| **Total** | 48 months | $5.65M | $1.05M | **~$6.7M** |

**Additional One-Time Costs**:
- **Attack tool licenses**: ~$100k (Ghidra Pro, Sage, specialized tools)
- **Hardware SCA equipment** (Advanced phase): ~$500k (power analyzers, EM probes, fault injection equipment)
- **Rainbow table storage**: ~$50k (pre-computed tables for common hashes)

**Grand Total (4 years)**: **~$7.35M**

*Note: Costs assume US-based team. International hiring or contractors can reduce by 30-50%. Without attack framework, costs would be ~$4-5M (40% reduction).*

---

## Go/No-Go Decision Criteria

### ✅ GO if you have:
- Commitment to 6+ month MVP timeline (no shortcuts)
- Budget for 2-3 engineers minimum
- Willingness to implement discipline majors from day one
- Real artifacts and use cases to validate against
- Stakeholder buy-in on determinism/reproducibility requirements
- Infrastructure support (cloud credits, compute resources)

### ❌ NO-GO if:
- "We need this in 3 months" (not feasible)
- "Can one engineer build this?" (not for production)
- "We'll add safety later" (recipe for disaster)
- "Determinism isn't critical" (then this design is overkill)
- No crypto/security expertise available
- Expectation of 100% accuracy from day one (ML models take time)

---

## Final Reality Check

**This is a hard system to build correctly, and the attack framework makes it significantly harder.**

The hard parts are not the algorithms (parsing ASN.1, computing entropy, implementing attacks). The hard parts are:

1. **Determinism across parallel execution** (single-writer, sequencing, seeding) **+ attack repeatability**
2. **Isolation without performance death** (per-artifact workspaces, no collisions) **+ attack workspace isolation**
3. **Failure-as-data discipline** (structured events, no silent failures) **+ attack failure taxonomy**
4. **Resource governance at scale** (timeouts, budgets, heavy pool caps) **+ attack pool governance**
5. **Tool integration hell** (error normalization across OpenSSL, Ghidra, Sage, liboqs) **+ 83 attack tools**
6. **Testing reproducibility** (same artifact → same evidence, byte-for-byte) **+ 3×repeat attack validation**
7. **Attack framework complexity** (NEW):
   - Integrating 83 different attack tools with varying interfaces
   - Ensuring each attack runs 3× deterministically with same results
   - Managing attack pools (light vs heavy vs simulation)
   - Aggregating attack results statistically
   - Building attack resistance profiles
   - Preventing attack tools from becoming security incidents (no GPU cracking unless authorized)

**Complexity Multiplier**: The attack framework roughly **doubles** the system complexity and cost compared to forensics-only mode.

**Attack Framework Risks**:
- **Tool availability**: Many advanced attacks don't have production-ready tools
- **Determinism**: Some attacks are inherently nondeterministic (need statistical handling)
- **Safety**: Brute-force tools can accidentally become cracking tools
- **Licensing**: Commercial cryptanalysis tools are expensive ($10k-100k per license)
- **Hardware**: Physical SCA requires $500k+ in specialized equipment
- **Expertise**: Finding cryptanalysis experts is harder than finding crypto engineers

**Realistic Assessment**:
- **Without attack framework**: $4-5M, 36 months, feasible for most security companies
- **With 10-15 core attacks (MVP)**: $5-6M, 42 months, feasible but challenging
- **With full 83 attacks**: $7-8M, 48 months, feasible only for well-funded organizations
- **With hardware SCA**: $9-10M+, 60+ months, research-lab tier complexity

If you shortcut any of the core discipline majors, you get a demo that works once. If you build them correctly from day one, you get an industry-grade product.

**Choose wisely. Consider starting with forensics-only (no attacks) and adding attacks in phases.**
