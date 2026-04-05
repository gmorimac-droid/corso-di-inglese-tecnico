# Maintenance Log Template

## Purpose

This template provides a structured format for recording maintenance activity in a concise but traceable way. A maintenance log is not a full report. It is a controlled operational record that captures what was inspected, what was found, what was done, and what the resulting status is.

It is particularly useful for:
- scheduled maintenance;
- corrective interventions;
- component replacement;
- post-inspection follow-up;
- supportability and traceability records.

---

## Template

```md
# Maintenance Log Entry

**Log ID:** [Reference]  
**Date:** [DD Month YYYY]  
**Technician / Team:** [Name / Team]  
**System / Asset:** [Identifier]  
**Location:** [If relevant]

## 1. Maintenance Type
[Preventive / Corrective / Inspection / Replacement / Verification]

## 2. Trigger / Reason for Activity
[Scheduled interval, observed fault, inspection requirement, preventive action, etc.]

## 3. Work Performed
[Describe the activity completed in concise operational language.]

## 4. Findings
[Record the technical condition observed during the activity.]

## 5. Parts Replaced / Tools Used
- [Part / serial / quantity]
- [Tool / equipment if relevant]

## 6. Functional Check / Post-Maintenance Verification
[State whether a check was performed and what the result was.]

## 7. Resulting Status
[Operational / Restricted / Awaiting further action / Removed from service]

## 8. Additional Notes
[Any relevant observation, residual concern, or recommendation]
```

---

## Model Example

# Maintenance Log Entry

**Log ID:** ML-2026-044  
**Date:** 03 April 2026  
**Technician / Team:** Field Maintenance Team B  
**System / Asset:** Remote Sensor Unit RSU-17  
**Location:** Workshop Area 4

## 1. Maintenance Type
Corrective maintenance

## 2. Trigger / Reason for Activity
The activity was initiated following repeated reports of intermittent communication loss during routine system checks.

## 3. Work Performed
The unit was opened for inspection, interface connectors were examined, cable routing was checked, and the communication connector was re-secured. A continuity verification was then performed.

## 4. Findings
A partially loosened connector was identified at the interface panel. No visible damage to the cable insulation or adjacent components was observed.

## 5. Parts Replaced / Tools Used
- No parts replaced  
- Standard connector tools and continuity test equipment used

## 6. Functional Check / Post-Maintenance Verification
A communication check was performed after reassembly. Stable communication was confirmed over three consecutive verification cycles.

## 7. Resulting Status
Operational

## 8. Additional Notes
Although the issue was resolved locally, repeated inspection of the connector retention arrangement is recommended at the next scheduled maintenance interval.

---

## Good Practice Notes

- Record the maintenance type explicitly.
- Use past tense for completed actions.
- Keep findings factual and concise.
- Always include resulting status.
- If the issue may recur, record the recommendation in the notes section.

## Cross-Links

- [Maintenance Terms](../glossaries/maintenance-terms.md)
- [Maintenance English](../modules/13-maintenance-english.md)
- [Maintenance and Troubleshooting Exercises](../exercises/maintenance-and-troubleshooting-exercises.md)
