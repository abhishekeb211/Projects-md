# 90-Day Rolling Telemetry Policy

**Version:** 1.0  
**Date:** [To be filled - Week 2]  
**Status:** Draft Template  
**Effective Date:** [TBD after IRB approval]

---

## 1. Purpose

This policy defines the telemetry data collection, retention, and privacy practices for the AegisCLI research platform. The policy ensures compliance with GDPR, organizational privacy requirements, and research ethics standards.

---

## 2. Scope

This policy applies to:
- All telemetry data collected by AegisCLI during the research study
- All teams and repositories participating in the study
- All researchers and engineers with access to telemetry data

---

## 3. Opt-In Consent Process

### 3.1 Team Consent
- **Requirement:** Each team must explicitly opt-in to telemetry collection
- **Method:** Team lead signs consent form (IRB-approved)
- **Revocation:** Teams can opt-out at any time via dashboard settings
- **Effect of Opt-Out:** Telemetry collection stops immediately; historical data retained per retention policy

### 3.2 Individual Developer Consent
- **Requirement:** Individual developers are informed of telemetry collection
- **Method:** Notification in AegisCLI CLI output on first run
- **Default:** Opt-in assumed if team has consented (can override individually)

---

## 4. Data Types Collected

### 4.1 Allowed Data Types
- **Scan invocation counts:** Number of scans per repository, per day
- **Tool usage metrics:** Which scanners used, frequency
- **Finding counts:** Aggregated counts by severity (no code snippets)
- **MTTR metrics:** Time from detection to remediation (anonymized)
- **Policy evaluation results:** Count of policy violations (no code context)

### 4.2 Prohibited Data Types
- **Code snippets >5 lines:** Automatically redacted before collection
- **File paths with sensitive names:** Redacted (e.g., `*secret*`, `*password*`)
- **Personal identifiers:** No developer names, emails, or user IDs
- **Repository names:** Anonymized to repository IDs
- **Network addresses:** No IP addresses or hostnames

---

## 5. Data Retention

### 5.1 90-Day Rolling Window
- **Policy:** Telemetry data is retained for 90 days from collection date
- **Automatic Deletion:** Data older than 90 days is automatically purged
- **Exception:** Aggregated statistics (monthly/quarterly summaries) may be retained longer for research analysis

### 5.2 Retention Schedule
- **Daily:** Raw telemetry data retained for 90 days
- **Weekly:** Aggregated weekly summaries retained for 1 year
- **Quarterly:** Aggregated quarterly reports retained for study duration + 2 years

---

## 6. Anonymization Rules

### 6.1 Repository Anonymization
- **Method:** Repository names replaced with unique IDs (hash-based, non-reversible)
- **Mapping:** Repository ID → name mapping stored separately, encrypted
- **Access:** Only research lead has access to ID mapping (for analysis)

### 6.2 Finding Anonymization
- **Code snippets:** Truncated to 5 lines maximum
- **File paths:** Sensitive path components redacted (e.g., `/home/user/` → `/***/`)
- **Rule names:** Preserved (public information, no sensitive data)

### 6.3 Team Anonymization
- **Team names:** Replaced with team IDs
- **Team size:** Reported as ranges (e.g., "5-10 engineers") not exact counts
- **Champion status:** Binary flag (has champion / no champion), no names

---

## 7. Data Access & Security

### 7.1 Access Controls
- **Research Team:** Full access to anonymized telemetry data
- **Engineering Team:** Access to aggregated metrics only (no raw data)
- **External:** No external access (data stays within organization)

### 7.2 Security Measures
- **Encryption:** All telemetry data encrypted at rest (AES-256)
- **Transmission:** All data transmission encrypted (TLS 1.3+)
- **Storage:** Data stored in air-gapped PostgreSQL instance (no cloud)

---

## 8. Data Deletion & Right to Erasure

### 8.1 Opt-Out Deletion
- **Immediate:** New telemetry collection stops immediately upon opt-out
- **Historical:** Historical data deleted within 30 days of opt-out request
- **Exception:** Aggregated statistics may retain anonymized contributions (cannot identify source)

### 8.2 Right to Erasure (GDPR)
- **Request:** Teams/individuals can request data deletion at any time
- **Process:** Submit request to research lead; deletion completed within 30 days
- **Verification:** Confirmation sent after deletion

---

## 9. Compliance & Auditing

### 9.1 Compliance Checks
- **Quarterly:** Review telemetry data for compliance with this policy
- **Annual:** External audit of data handling practices
- **IRB Review:** Annual IRB review of telemetry practices

### 9.2 Audit Logs
- **Access Logs:** All telemetry data access logged (who, when, what)
- **Retention:** Access logs retained for 1 year
- **Review:** Access logs reviewed quarterly for unauthorized access

---

## 10. Policy Updates

### 10.1 Update Process
- **Notification:** Teams notified 30 days before policy changes
- **Consent:** Re-consent required for material changes
- **Version Control:** Policy versions tracked; previous versions archived

### 10.2 Current Version
- **Version:** 1.0
- **Last Updated:** [TBD - Week 2]
- **Next Review:** [TBD - 6 months from effective date]

---

## 11. Contact & Questions

**Research Lead:** [Name, Email]  
**Privacy Officer:** [Name, Email]  
**IRB Contact:** [IRB Office, Email]

For questions about this policy or to exercise data rights, contact the Research Lead.

---

## Appendix A: Data Collection Schema

### Telemetry Event Schema
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "event_type": "scan_completed",
  "repository_id": "hash_abc123",
  "team_id": "team_xyz789",
  "scanner": "semgrep",
  "findings_count": {
    "critical": 2,
    "high": 5,
    "medium": 10,
    "low": 3
  },
  "scan_duration_seconds": 45.2,
  "policy_violations_count": 1
}
```

**Note:** No code snippets, file paths, or personal identifiers included.

---

## Appendix B: Redaction Examples

### Code Snippet Redaction
**Before:**
```python
def process_user_input(user_data):
    query = f"SELECT * FROM users WHERE id = {user_data['id']}"
    # ... 10 more lines
```

**After (redacted):**
```
[Code snippet truncated to 5 lines per policy]
```

### File Path Redaction
**Before:** `/home/john.doe/projects/secret-api/src/main.py`  
**After:** `/***/projects/***/src/main.py`

---

**Policy Status:** Template - To be finalized in Week 2 after IRB review

