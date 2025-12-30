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

## Built-In Discipline Majors (Production Fixes You Must Ship)

### A) Determinism Contract

Every event includes:

- `run_id`, `artifact_id`, `artifact_seq`, `event_seq`

Seeds derived deterministically from:

- artifact hash + run config hash (or toolchain hash for generation)

Single writer ensures stable output ordering

### B) Resource Governance

Separate budgets:

- artifact workers (throughput)
- heavy pool (governor)

Hard timeouts everywhere

Bounded candidate splits and probe budgets

### C) Failure Semantics

Failures are data, not exceptions:

- tool errors are emitted as normalized events
- parse failure kinds are features

No silent failures:

- every tool invocation yields an event

### D) Isolation Rules

- Per-artifact workspace and tool env isolation mandatory
- No shared temp dirs
- No network by default
- Raw logs stored separately and referenced, not dumped inline

### E) Caching Rules (Make scaling affordable)

Cache expensive steps by immutable hashes:

- binary hash → RE results
- artifact hash → CLI parsing results (optional)
- PQC generation templates → batch outputs

Cache invalidation keyed on toolchain hash

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

## Storage Layout (Product-Ready)

```
manifests/
  run_manifest.json
  tool_inventory.json

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

features/
  features.parquet
  feature_schema.json

models/
  model_registry/

reports/
  report_artifacts/
```

---

## Corrected Feasibility Summary (No Wishcasting)

### Straightforward and solid

- artifact-parallel execution
- single-writer deterministic telemetry
- tool inventory + manifest capture
- CLI inspection + hash classification
- routing + normalization + probes with budgets

### Feasible with strict discipline (still doable)

- deep RE (Ghidra): must be gated, cached, throttled
- math workbench: must be bounded and rare
- PQC dataset expansion: must be batch, deterministic, version-pinned

### What breaks in real life (and how this design prevents it)

- **nondeterministic logs** → single writer + seq fields
- **tool collisions** → per-artifact workspace + env isolation
- **runaway heavy workloads** → heavy pool caps + strict timeouts
- **silent failures** → normalized error events always emitted
- **cost blowups** → caching keyed by hashes + toolchain hash

---

**Bottom line**: This is feasible to implement and credible as an industry product if you ship the discipline majors (determinism, isolation, governance, failure-as-data, caching). Without those, it's a demo that works until someone touches it, which is basically every demo ever made.

---

**That's Forensics Mode implemented as an actual build plan: what comes in, what runs, what gets emitted, what's forbidden, and how it stays reproducible.**

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

### Phase 3: PQC Toolchain Integration

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

### Phase 4: Evidence → Features → Models

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

### Phase 5: Production Discipline (Built-In Fixes)

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

### Phase 6: Observability & Operations

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

### Phase 7: Testing & Validation

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

### Phase 8: Scaling & Productization

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

### Phase 9: Documentation

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

## Critical Path (Minimum Viable Product)

For a working MVP, focus on:

1. **Core Infrastructure** (Phase 0 + Phase 1 basics)
2. **Simple Artifact Flow** (Registry → Scheduler → Worker → Telemetry)
3. **2-3 Basic Modules** (Router + CLI Inspection + Basic Probes)
4. **Evidence Store** (Simple JSONL persistence)
5. **Basic Feature Extraction** (Batch mode)
6. **Simple Report** (Evidence trace + basic classification)
7. **Essential Safety** (Timeouts + Isolation + No-network)
8. **Basic Tests** (Unit + Integration for critical path)

Then iterate to add more modules, heavy pool, models, and scaling features.
