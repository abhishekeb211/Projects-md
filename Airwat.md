# Airwat

## 1) High-Level End-to-End Flow (Unified)

(One spine, two modes: Forensics + Experiment. Same control plane, same evidence pipeline, same storage. Because building two separate systems is how teams slowly die inside.)

---

### A) System Modes (What "Unified" actually means)

#### Forensics Mode

**Inputs**: unknown real-world artifacts (ciphertexts, keys, certs, PQC blobs, hashes/KDF strings, protocol captures, binaries)

**Goal**: classify + analyze + fingerprint + emit evidence-linked results, features, and reports

#### Experiment Mode (Lab Harness)

**Inputs**: configs describing corpus, sizes, algorithms, parameter sets, simulation models

**Goal**: generate datasets → encrypt → validate → run simulations/estimators → metrics → reports

#### Unification rule

Both modes must:

- create a run manifest
- use tool inventory pinning
- emit evidence events only
- persist through single-writer deterministic telemetry
- generate features by replay
- render reports from evidence

---

### B) End-to-End Pipeline Stages (Top-Level)

#### Stage 0: Input Intake

- **Forensics**: artifact upload/ingest
- **Experiment**: experiment config intake

#### Stage 1: Run Initialization

- manifest creation + policy freeze
- tool inventory capture
- deterministic seeding setup

#### Stage 2: Job Expansion

Convert inputs into independent jobs:

- artifact jobs (forensics)
- dataset/encryption/simulation jobs (experiment)

#### Stage 3: Execution

- **throughput tier**: artifact workers (parallel)
- **governor tier**: heavy pool (throttled)
- all tools executed in isolated per-job workspaces

#### Stage 4: Evidence Capture

- workers emit structured events
- telemetry writer persists them deterministically (single-writer ordering)

#### Stage 5: Feature Build

- batch replay (canonical) and optional streaming (must match replay)

#### Stage 6: Modeling

- tiered models run on feature tables
- predictions stored as evidence events

#### Stage 7: Reporting + API

- evidence-linked reports + APIs
- everything traceable back to run manifest + events

---

### C) Unified Dataflow (What goes where)

#### Inputs

- **Forensics artifacts**: blobs + metadata
- **Experiment configs**: corpus + sizes + algorithms + "attack models"

#### Outputs

- **Evidence store** (canonical truth)
- **Feature tables** (derived, replayable)
- **Model outputs** (stored as evidence)
- **Reports** (compiled from evidence + predictions)

---

### D) Control Plane vs Data Plane (Clear separation)

#### Control Plane (decides what happens)

**Run Controller**

- freezes configs
- locks toolchain inventory
- enforces policies (timeouts, budgets, safety flags)

**Scheduler**

- creates jobs with stable ordering
- enforces backpressure + priorities

#### Data Plane (does the work)

**Artifact workers and heavy workers**

- run tool-backed modules
- emit evidence events

**Telemetry writer**

- enforces deterministic ordering
- persists evidence

---

### E) Core Contracts (These make "unified" real)

#### Run Manifest Contract

Every run produces an immutable manifest defining:

- policies and budgets
- tool inventory reference
- module plan version
- deterministic seed rules
- job list and stable job ordering

#### Evidence-Only Contract

Workers never write:

- final features
- final reports
- "truth" tables

Workers only emit:

- structured evidence events
- raw blob references

#### Deterministic Telemetry Contract

Single writer assigns canonical ordering, making runs diffable and replayable

#### Replay Contract

- Features must be reconstructible from evidence alone
- Reports must be reconstructible from evidence + manifest (and model versions)

---

### F) Job Types (Unified Scheduler View)

#### Forensics Jobs

- **Artifact analysis job** (one per artifact, or per bundle)
- **Optional heavy escalation job** (deep RE, math workbench)

#### Experiment Jobs

- **Dataset generation job** (corpus → normalized → size variants)
- **Encryption job** (dataset → ciphertext + validation)
- **Simulation/estimator job** (ciphertext → raw logs + signals)
- **Metrics aggregation job** (logs → results)
- **Reporting job** (results → charts/tables/report)

All of these are treated the same operationally:

- stable job IDs
- deterministic subtask IDs
- bounded time/resources
- event emission only

---

### G) Worker Pools (Throughput vs Governor)

#### Artifact Worker Pool (throughput tier)

- high concurrency
- runs fast-to-moderate modules
- keeps jobs mostly sequential internally for stable state

#### Heavy Pool (governor tier)

Low concurrency (scarce resource)

Runs expensive tasks only:

- deep reverse engineering
- heavy math/cryptanalysis workbench
- PQC dataset expansion batches

Strict resource limits and gating

---

### H) Evidence Flow (What happens to logs/outputs)

#### Workers produce

- structured evidence events per module/tool action
- raw outputs (stdout/stderr, dumps, intermediate artifacts) saved as blobs

#### Telemetry Writer produces

- canonical event streams partitioned by run and job/artifact sequence
- deterministic event sequence numbers
- stable references to raw blobs

**Key rule**:

No "print logs and hope."

Everything is structured evidence, or referenced blobs.

---

### I) Safety and Policy Gates (Applied globally)

#### No-network by default

- Hash/KDF handling restricted
- audit-only classification and parameter extraction by default
- no recovery-style workflows unless explicitly permitted (and typically experiment-only)

#### Timeouts and budgets everywhere

- module timeouts
- tool timeouts
- candidate caps
- probe budgets

#### Fail-closed routing

Ambiguous inputs must not trigger dangerous modules

---

### J) Determinism Guarantees (What the unified flow must ensure)

#### Stable ordering

- jobs have stable sequence numbers
- events have deterministic IDs
- writer assigns canonical event order consistently

#### Stable execution

- deterministic seeds derived from artifact hash + run config hash
- pinned tool versions and container image digests

#### Stable derivation

- features replay from evidence must be stable
- reports generated from evidence must be stable

---

### K) Observability (Product-level visibility)

#### Per-run visibility

- progress by job count and module stage
- success/fail/timeout counts

#### Per-module visibility

- runtime percentiles
- failure taxonomy rates
- tool version failure correlation

#### Heavy pool visibility

- queue depth
- wait time
- cache hit rates

---

### L) Deliverables Produced by This Unified Flow

- Immutable run manifest + tool inventory
- Immutable artifacts (datasets, ciphertexts, captures, binaries)
- Canonical evidence store (events + raw blob references)
- Feature tables (replayable)
- Model outputs as evidence events
- Evidence-linked reports

---

**That's the end-to-end flow written in a way engineers can actually implement without translating poetry into infrastructure.**
