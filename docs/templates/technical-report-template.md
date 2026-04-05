# Technical Report Template

## Purpose

This template supports the preparation of a structured technical report suitable for engineering reviews, design status summaries, evaluation activities, technical investigations, configuration change assessments, and documentation packages that require more depth than an email or meeting note.

A technical report should not merely collect information. It should guide the reader through the purpose, technical basis, findings, and conclusions in a logical sequence.

---

## Recommended Structure

The exact structure will vary depending on project needs, but the following sequence is generally robust:

1. Title and reference data
2. Purpose and scope
3. Background or context
4. Technical description or method
5. Findings or observations
6. Analysis
7. Conclusions
8. Recommendations or next actions
9. References and appendices

---

## Template

```md
# [Report Title]

**Document ID:** [Reference]  
**Revision:** [A / B / 1 / Draft]  
**Date:** [DD Month YYYY]  
**Prepared by:** [Name / Team]  
**Reviewed by:** [If applicable]  
**Approved by:** [If applicable]

## 1. Purpose
[State why the report was produced.]

## 2. Scope
[Define what is covered and what is excluded.]

## 3. Background
[Provide the project, system, operational, or documentary background needed to understand the report.]

## 4. Technical Basis / Method
[Describe the method, data source, inspection activity, review approach, or evaluation basis used.]

## 5. Findings
### 5.1 [Finding]
[Describe the observation clearly and objectively.]

### 5.2 [Finding]
[State the evidence and relevance.]

## 6. Analysis
[Interpret the findings. Distinguish clearly between observation and evaluation.]

## 7. Conclusions
[Summarize the main technical conclusions.]

## 8. Recommendations / Actions
- [Recommendation 1]
- [Recommendation 2]
- [Action 1]

## 9. References
- [Document / drawing / procedure / test record]

## 10. Appendices
[Optional supporting material, tables, data extracts, photographs, or supplementary notes]
```

---

## Model Example

# Preliminary Technical Assessment of Sensor Enclosure Revision C

**Document ID:** TA-SEC-014  
**Revision:** Draft 1  
**Date:** 03 April 2026  
**Prepared by:** Technical Documentation and Systems Support

## 1. Purpose
The purpose of this report is to provide a preliminary technical assessment of sensor enclosure revision C prior to formal release for integration activities.

## 2. Scope
This report covers external configuration changes, environmental wording, maintainability implications, and documentation consistency. Detailed qualification evidence is outside the scope of the present assessment.

## 3. Background
Revision C was introduced to improve cable routing, simplify maintenance access, and align the enclosure design with the updated installation envelope. Following the design update, a focused review was requested to identify any outstanding documentation or integration concerns.

## 4. Technical Basis / Method
The assessment was based on the current drawing package, the enclosure specification draft, the latest installation note, and comments recorded during the design coordination meeting of 28 March 2026.

## 5. Findings
### 5.1 Improved Routing Clarity
The revised internal arrangement reduces cable routing ambiguity and supports clearer assembly instructions.

### 5.2 Alignment Tolerance Not Yet Formalized
Although installation alignment is referenced in the descriptive text, the tolerance itself is not yet stated in the requirements section.

### 5.3 Environmental Description Remains Generic
The environmental paragraph has been updated partially, but the current wording remains broader than the verified installation assumptions.

## 6. Analysis
The revision offers tangible documentation and maintainability benefits. However, two points remain significant for release quality: the absence of explicit alignment tolerance in the requirement structure and the incomplete normalization of environmental language. These issues do not invalidate the revision, but they reduce documentary robustness.

## 7. Conclusions
The revised enclosure configuration is technically acceptable at preliminary review level. Formal release is recommended only after requirement wording and environmental constraints have been aligned with the current baseline.

## 8. Recommendations / Actions
- Add explicit alignment tolerance to the requirement section.
- Revise the environmental paragraph to reflect validated conditions only.
- Re-issue the document package for focused closure review.

## 9. References
- Sensor Enclosure Drawing Package, Rev. C  
- Installation Note, Issue 2  
- Design Coordination Minutes, 28 March 2026

---

## Review Guidance

- The title should state the document function, not just the topic.
- Findings should be evidence-based and neutral.
- Analysis should explain significance, not repeat findings.
- Conclusions should be shorter than the analysis section.
- Recommendations should be actionable.

## Cross-Links

- [Technical Writing Module](../modules/09-principles-of-technical-writing.md)
- [Reports, Summaries and Meeting Notes](../modules/11-reports-summaries-and-meeting-notes.md)
- [Report Writing Exercises](../exercises/report-writing-exercises.md)
