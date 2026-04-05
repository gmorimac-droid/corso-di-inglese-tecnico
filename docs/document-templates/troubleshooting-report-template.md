# Troubleshooting Report Template

## Purpose

This template is intended for structured documentation of fault investigation and diagnostic reasoning. It is especially useful when the technical issue is not immediately obvious and a record is required of symptoms, checks performed, intermediate findings, and final resolution.

A troubleshooting report is more analytical than a maintenance log and more focused than a general incident report.

---

## Core Logic

A strong troubleshooting report should normally follow this progression:

**symptom â†’ initial checks â†’ diagnostic steps â†’ identified cause â†’ corrective action â†’ verification**

This sequence allows later reviewers to understand not only what the final problem was, but also how the conclusion was reached.

---

## Template

```md
# Troubleshooting Report

**Report ID:** [Reference]  
**Date:** [DD Month YYYY]  
**Prepared by:** [Name / Team]  
**System / Asset:** [Identifier]

## 1. Problem Statement
[State the technical issue clearly.]

## 2. Observed Symptoms
- [Symptom 1]
- [Symptom 2]
- [Operating condition]

## 3. Initial Checks
[Record the first checks carried out to exclude obvious causes.]

## 4. Diagnostic Actions Performed
### 4.1 [Action]
[What was checked and why]

### 4.2 [Action]
[What was checked and what was found]

## 5. Root Cause / Most Probable Cause
[State the confirmed or most probable cause. If not fully confirmed, indicate the level of confidence.]

## 6. Corrective Action
[Describe the action taken to resolve or mitigate the issue.]

## 7. Verification of Recovery
[State what was tested after the corrective action and whether normal operation was restored.]

## 8. Additional Recommendations
- [Preventive recommendation]
- [Inspection follow-up]
- [Documentation update]
```

---

## Model Example

# Troubleshooting Report

**Report ID:** TR-2026-018  
**Date:** 03 April 2026  
**Prepared by:** Systems Support and Maintenance Analysis  
**System / Asset:** Remote Terminal Assembly RTA-04

## 1. Problem Statement
Intermittent communication loss was reported between the remote terminal assembly and the central processing unit during routine verification.

## 2. Observed Symptoms
- Communication link dropped intermittently during status polling.  
- Power remained stable throughout the event.  
- No abnormal temperature increase was observed.

## 3. Initial Checks
The power supply condition was verified first and found to be stable. Environmental conditions were normal and no visible external damage was identified.

## 4. Diagnostic Actions Performed
### 4.1 Connector Inspection
All accessible connectors were inspected to determine whether loose retention or contamination might be present.

### 4.2 Interface Continuity Check
A continuity check was performed across the communication path. The check indicated inconsistency at the interface panel connection.

### 4.3 Mechanical Verification
Closer mechanical inspection identified a partially loosened connector at the interface panel.

## 5. Root Cause / Most Probable Cause
The root cause was identified as insufficient retention of the interface connector, resulting in intermittent contact during normal operation.

## 6. Corrective Action
The connector was re-secured and the retention condition was verified before system reassembly.

## 7. Verification of Recovery
Following corrective action, stable communication was confirmed over three consecutive checks. No further communication loss was observed.

## 8. Additional Recommendations
- Inspect similar connectors on equivalent units during the next scheduled maintenance cycle.  
- Review whether the retention arrangement should be improved in future revisions.

---

## Review Notes

- Keep the problem statement short and specific.
- Record diagnostic reasoning in sequence.
- Avoid jumping straight to the final cause.
- State whether the cause is confirmed or inferred.
- Always include recovery verification.

## Cross-Links

- [Troubleshooting and Fault Analysis](../modules/14-troubleshooting-and-fault-analysis.md)
- [Phrasebank for Reporting](../language-tools/phrasebank-for-reporting.md)
- [Maintenance and Troubleshooting Exercises](../exercises/maintenance-and-troubleshooting-exercises.md)

