# Forensics Mode

## Industry-Grade Architecture: Tool-Backed Crypto Forensics with Deterministic Concurrency

### Mission

Build a crypto-forensics pipeline that can ingest real-world artifacts (ciphertexts, keys, certs, PQC blobs, hashes, captures, binaries), run tool-backed analysis in reproducible environments, and emit structured evidence for feature extraction, modeling, and reporting. The system must scale to production volumes without sacrificing reproducibility or traceability.

---

## Product Requirements (Non-Negotiable)

### Functional

- Classify and parse crypto-related artifacts into meaningful families/types
- Run behavioral, wrapper, protocol, and implementation-level probes
- Support PQC ground-truth generation and validation using real toolchains
- Identify and classify hash/KDF materials defensively (audit/IR mode)
- Produce evidence-linked reports and model-ready features

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
6. **Heavy Escalation Requests** (if allowed and justified)
7. **Completion Summary Event**

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

**That's Forensics Mode implemented as an actual build plan: what comes in, what runs, what gets emitted, what's forbidden, and how it stays reproducible.**
