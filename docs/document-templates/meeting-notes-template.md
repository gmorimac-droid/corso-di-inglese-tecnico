# Meeting Notes Template

## Purpose

This template supports the production of concise and traceable meeting notes for technical coordination meetings, design reviews, progress reviews, issue resolution sessions, and documentation alignment meetings.

Meeting notes are not a verbatim transcript. Their purpose is to capture decisions, actions, responsibilities, and technical clarifications in a form that can be reviewed later and used as a reference point for project continuity.

---

## Recommended Structure

A professional set of meeting notes should normally include:

- meeting title and date;
- participants;
- purpose of the meeting;
- key discussion points;
- decisions made;
- open issues;
- action items with owners and due dates.

---

## Template

```md
# [Meeting Title]

**Date:** [DD Month YYYY]  
**Time:** [Startâ€“End]  
**Format:** [In person / Remote / Hybrid]  
**Chair:** [Name]  
**Participants:** [List of attendees]  
**Apologies / Not present:** [If relevant]

## 1. Meeting Purpose
[State why the meeting was held and what it was intended to achieve.]

## 2. Key Discussion Points
### 2.1 [Topic]
[Summarize the discussion objectively and concisely.]

### 2.2 [Topic]
[Record technical clarifications, dependencies, and concerns.]

## 3. Decisions
- [Decision 1]
- [Decision 2]
- [Decision 3]

## 4. Open Issues
- [Issue / required clarification / dependency]

## 5. Action Items
| ID | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| A1 | [Action] | [Name / Team] | [Date] | Open |
| A2 | [Action] | [Name / Team] | [Date] | Open |

## 6. References
- [Documents, drawings, minutes, specifications, links]

## 7. Next Meeting / Follow-Up
[State whether a follow-up meeting is planned or whether closure is expected via email/document review.]
```

---

## Model Example

# Electrical Interface Review Meeting

**Date:** 18 April 2026  
**Time:** 10:00â€“11:15  
**Format:** Remote  
**Chair:** Systems Engineering Lead  
**Participants:** Systems, Electrical Design, Integration, Technical Documentation  
**Apologies / Not present:** Quality Assurance Representative

## 1. Meeting Purpose
The meeting was held to review the latest electrical interface assumptions for the sensor enclosure and to confirm the actions required before document release.

## 2. Key Discussion Points
### 2.1 Connector Allocation
The electrical design team confirmed that the proposed connector remains compatible with the current layout constraints. However, the reserved pins are not yet identified consistently across the specification and the wiring note.

### 2.2 Supply Voltage Tolerance
It was noted that the descriptive section of the specification refers to nominal voltage only, while the requirements section does not yet define the acceptable operating tolerance.

### 2.3 Environmental Assumptions
The integration team requested alignment between the installation paragraph and the current environmental profile. The present wording is considered too generic for release.

## 3. Decisions
- The connector pin table will be revised to include reserved and unused pins explicitly.
- Voltage tolerance will be added to the requirement section.
- The environmental paragraph will be updated before the next issue.

## 4. Open Issues
- Confirmation is still required on the final cable shielding approach.

## 5. Action Items
| ID | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| A1 | Update connector allocation table | Electrical Design | 22 April 2026 | Open |
| A2 | Add voltage tolerance requirement | Systems Engineering | 22 April 2026 | Open |
| A3 | Revise environmental wording | Technical Documentation | 23 April 2026 | Open |

## 6. References
- Electrical Interface Specification, Rev. B  
- Wiring Note, Draft Issue 2  
- Environmental Profile Summary, Issue 1

## 7. Next Meeting / Follow-Up
Follow-up will take place by document review unless unresolved issues remain after revision.

---

## Review Notes

- Record what was decided, not what was said informally.
- Use past tense for discussion and decision summary.
- Use action verbs in the action table.
- Ensure responsibilities are explicit.
- If a point is still uncertain, label it as an open issue rather than a decision.

## Cross-Links

- [Phrasebank for Meetings](../language-tools/phrasebank-for-meetings.md)
- [Reports, Summaries and Meeting Notes](../modules/11-reports-summaries-and-meeting-notes.md)
- [Oral Communication Tasks](../exercises/oral-communication-tasks.md)

