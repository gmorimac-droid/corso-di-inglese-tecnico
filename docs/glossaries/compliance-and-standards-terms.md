# Compliance and Standards Terms

!!! abstract "Scope of this glossary"
    This glossary supports requirement writing, specification review, standards-based documentation, and formal statements about conformity. It is especially useful for learners who need to produce language that is disciplined, auditable, and suitable for controlled engineering documents.

## How to read and reuse the entries

Each entry is written for **active professional use**. The definition gives conceptual precision, the example shows sentence-level application, and the usage note explains where the term is especially valuable in engineering communication. Where helpful, a contrast note is added to prevent common learner mistakes.

## Best fit inside this course

- Best aligned with `modules/12-requirements-specifications-and-compliance.md`, `templates/specification-template.md`, `templates/test-report-template.md`, and `quality-assurance/style-and-editorial-guide.md`.

## Glossary entries

### shall

**Definition.** Shall is the preferred modal verb for stating a mandatory requirement in many formal technical and contractual contexts.

**Example.** The enclosure shall maintain ingress protection under the environmental conditions defined in the specification.

**Usage note.** Use *shall* when the sentence expresses a formal requirement that must be verified or otherwise assessed for compliance.

**Contrast / learner note.** Do not use *shall* for casual future meaning. In controlled documents it normally signals obligation.

**Related terms.** requirement, compliance, verification, mandatory statement

### should

**Definition.** Should expresses recommendation, preferred practice, or strong advice without the full force of a mandatory requirement.

**Example.** Fasteners should be rechecked after the initial vibration test to confirm retention integrity.

**Usage note.** Useful in guidance notes, best-practice sections, and advisory language.

**Contrast / learner note.** If a statement is mandatory, *should* is too weak. Use *shall* or another formally defined mandatory expression.

**Related terms.** recommendation, guidance, preferred practice, may

### may

**Definition.** May expresses permission, allowance, or acceptable possibility within a defined framework.

**Example.** The inspection may be performed using equivalent calibrated equipment, provided that measurement uncertainty remains acceptable.

**Usage note.** Use *may* when the document intentionally allows flexibility or alternative methods.

**Contrast / learner note.** Do not use *may* when the intended meaning is capability. In that case *can* may be clearer, depending on the style guide.

**Related terms.** allowed, optional, permitted, can

### comply with

**Definition.** To comply with something means to meet the requirements of a standard, specification, regulation, contractual clause, or internal rule.

**Example.** The revised design complies with the updated sealing requirement and the applicable environmental standard.

**Usage note.** This phrase is central in declarations of conformity, review notes, and test conclusions.

**Contrast / learner note.** Be careful with weak phrasing such as *is in line with*. In formal compliance writing, *complies with* is stronger and more explicit.

**Related terms.** conformity, requirement, verification evidence, in accordance with

### in accordance with

**Definition.** In accordance with indicates that an action, method, or result follows a stated standard, instruction, procedure, or governing reference.

**Example.** Testing was performed in accordance with the approved procedure and the current issue of the relevant standard.

**Usage note.** Useful in reports, procedures, and audit-ready language when stating how an activity was conducted.

**Contrast / learner note.** This phrase often describes process alignment, while *complies with* often describes outcome or requirement satisfaction. In practice they may appear together.

**Related terms.** according to, procedure, standard, compliance

### acceptance criteria

**Definition.** Acceptance criteria are the defined conditions or performance thresholds that determine whether an item, result, or activity is acceptable.

**Example.** Acceptance criteria required stable communication with no data loss during the full environmental exposure period.

**Usage note.** Common in test plans, verification reports, supplier evaluation, and inspection records.

**Contrast / learner note.** Acceptance criteria should be measurable or at least assessable. Vague criteria produce weak verification evidence.

**Related terms.** pass/fail, requirement, verification, inspection

### deviation

**Definition.** A deviation is a departure from an approved requirement, process, drawing, plan, or expected condition.

**Example.** A documented deviation was raised because the approved cable clamp was temporarily unavailable.

**Usage note.** Use this term when a controlled difference from the baseline or requirement must be recorded and justified.

**Contrast / learner note.** A deviation may be authorised. A nonconformity usually indicates failure to meet a requirement and may not be pre-authorised.

**Related terms.** waiver, nonconformity, change request, concession

### waiver

**Definition.** A waiver is formal authorisation to accept a known departure from a requirement under stated conditions.

**Example.** A temporary waiver was granted pending implementation of the revised mounting arrangement.

**Usage note.** Appropriate in controlled technical programmes where acceptance of a deviation must be traceable.

**Contrast / learner note.** A waiver is a formal decision, not an informal agreement or undocumented tolerance.

**Related terms.** deviation, concession, approval authority, residual risk

### standard

**Definition.** A standard is an established document or reference that defines rules, requirements, methods, terminology, or characteristics for common and repeated use.

**Example.** Material selection was reviewed against the applicable corrosion-resistance standard.

**Usage note.** Use this word carefully and, where possible, cite the exact standard rather than referring to standards in general.

**Contrast / learner note.** A company procedure is not automatically a standard, even if it is mandatory internally.

**Related terms.** specification, procedure, regulation, code

### regulation

**Definition.** A regulation is a rule or set of rules issued by a competent authority and carrying formal legal or mandatory force within its scope.

**Example.** The export review considered the applicable regulation before release of the controlled technical dataset.

**Usage note.** Particularly useful in compliance summaries, audit notes, and institutional communication.

**Contrast / learner note.** A standard may be voluntary or adopted contractually; a regulation usually has authority-based mandatory status.

**Related terms.** authority, compliance, legal requirement, control

### certification

**Definition.** Certification is the formal process or result by which compliance with defined requirements is confirmed by a recognised body or authorised organisation.

**Example.** Certification evidence was updated following the enclosure redesign and repeat environmental testing.

**Usage note.** Useful in compliance communication, supplier qualification, and programme readiness discussions.

**Contrast / learner note.** Certification is not the same as test completion. Test data may support certification, but the formal status depends on the recognised process.

**Related terms.** approval, conformity assessment, qualification, evidence

### conformity

**Definition.** Conformity is the state of meeting specified requirements, standards, or approved criteria.

**Example.** Conformity of the revised assembly was demonstrated through inspection, documentation review, and functional testing.

**Usage note.** Common in formal reports, audit language, and quality statements.

**Contrast / learner note.** Conformity is the condition achieved; compliance is often the action or status of meeting the requirement. In many contexts they overlap, but both should be used carefully.

**Related terms.** compliance, verification, acceptance, nonconformity

## Requirement-writing caution

In controlled documents, modal verbs are not stylistic decoration. They define obligation level. A repository that mixes *shall*, *should*, *may*, *can*, and simple present without discipline becomes difficult to verify and difficult to review.


## Writing patterns worth reusing

The value of a glossary increases when the learner converts terminology into reusable sentence patterns. After studying the entries above, build short patterns such as:

- *The system shall ... under the specified operating conditions.*
- *The inspection confirmed that ...* 
- *The interface between X and Y is responsible for ...*
- *A deviation was recorded because ...*
- *The revised document includes ...*

## Suggested micro-practice

1. Select five entries from this page and write one sentence for each in a different document genre.
2. Rewrite one weak sentence by replacing generic vocabulary with glossary terms.
3. Add one contrast pair to your personal notes, for example *verification vs validation* or *incident vs near miss*.
4. Reuse at least three entries in a module assignment before moving to the next glossary.

## Cross-reference inside the repository

For applied use, connect this page to the relevant modules, phrasebanks, templates, and exercises. Terminology becomes valuable only when it is reused consistently across the documentation set.
