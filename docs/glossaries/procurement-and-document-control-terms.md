# Procurement and Document Control Terms

!!! abstract "Scope of this glossary"
    This glossary supports communication about technical procurement, supplier interaction, deliverables, revision logic, and controlled documentation. It is particularly useful for learners who work around engineering governance, configuration control, programme administration, or supplier-facing documentation.

## How to read and reuse the entries

Each entry is written for **active professional use**. The definition gives conceptual precision, the example shows sentence-level application, and the usage note explains where the term is especially valuable in engineering communication. Where helpful, a contrast note is added to prevent common learner mistakes.

## Best fit inside this course

- Best aligned with `modules/17-procurement-and-programme-language.md`, `modules/18-mkdocs-and-github-documentation-project.md`, `document-templates/technical-email-template.md`, and `quality-assurance/repository-governance.md`.

## Glossary entries

### request for proposal

**Definition.** A request for proposal is a formal invitation asking suppliers or contractors to submit a technical and commercial proposal in response to stated needs and evaluation criteria.

**Example.** The request for proposal included mandatory interface requirements, environmental limits, and delivery milestones.

**Usage note.** In writing, it is common to introduce the full term once and then use the abbreviation only if the context supports it.

**Contrast / learner note.** A request for proposal is broader than a purchase order because it begins a competitive or evaluative procurement phase.

**Related terms.** statement of work, compliance matrix, supplier response, evaluation

### statement of work

**Definition.** A statement of work is the document section that defines the tasks, scope, outputs, responsibilities, and boundaries of the contracted effort.

**Example.** The statement of work required monthly progress reporting and delivery of a controlled interface document.

**Usage note.** Useful in procurement, subcontracting, and programme governance.

**Contrast / learner note.** A specification defines what the technical solution must satisfy; a statement of work defines what effort shall be performed.

**Related terms.** scope, deliverable, milestone, contractual requirement

### deliverable

**Definition.** A deliverable is a document, item, dataset, service, or completed output that must be provided as part of a project, contract, or agreed work package.

**Example.** The verification report is a contractual deliverable and must be issued in controlled form.

**Usage note.** Use this term when discussing obligations, planning, review status, and customer-facing outputs.

**Contrast / learner note.** A task is an activity; a deliverable is the output resulting from the activity.

**Related terms.** output, submission, milestone, acceptance

### milestone

**Definition.** A milestone is a defined project event or achievement used to monitor progress, sequence decisions, or trigger subsequent work.

**Example.** Completion of the integration readiness review was treated as a milestone before field acceptance testing.

**Usage note.** Useful in schedule discussions, progress updates, and programme dashboards.

**Contrast / learner note.** A milestone is not the same as a deadline, although milestones often have scheduled dates.

**Related terms.** schedule, review gate, phase completion, deliverable

### revision

**Definition.** A revision is a formally identified version change to a controlled document, drawing, or dataset resulting from approved modification.

**Example.** Revision B incorporated the updated connector specification and corrected the inspection interval table.

**Usage note.** This term is essential in document control, change notes, and repository governance.

**Contrast / learner note.** Do not confuse revision with informal editing. A revision normally implies formal traceability.

**Related terms.** issue, version, change record, baseline

### issue

**Definition.** Issue can refer either to a formal published version of a document or to a problem requiring resolution, depending on context.

**Example.** The latest document issue was released after closure of the review comments.

**Usage note.** Because the word has two meanings, good technical writing should make the intended meaning obvious.

**Contrast / learner note.** When referring to a problem, pair the word with context such as *technical issue* or *open issue*. When referring to document status, pair it with *document issue* or a revision identifier.

**Related terms.** revision, release, problem, action item

### controlled copy

**Definition.** A controlled copy is a document instance that is subject to formal update, distribution, and revision control procedures.

**Example.** Only the controlled copy in the repository shall be used for release and audit purposes.

**Usage note.** Useful in quality systems, formal document control, and training guidance.

**Contrast / learner note.** A downloaded local file may become uncontrolled unless the system explicitly maintains its status.

**Related terms.** document control, distribution, revision, master record

### document register

**Definition.** A document register is the structured list or database that records controlled documents, their status, identifiers, owners, and revision information.

**Example.** The document register was updated to reflect withdrawal of the obsolete test procedure.

**Usage note.** Appropriate in programme governance, quality assurance, and repository administration.

**Contrast / learner note.** A folder listing is not automatically a document register unless it records controlled metadata and status.

**Related terms.** index, controlled copy, revision history, ownership

### version

**Definition.** Version is the identified state of a document, software item, dataset, or configuration at a given point in its development or release history.

**Example.** The analysis was repeated using software version 3.4.2 and the current approved hardware baseline.

**Usage note.** This term is broad and widely useful, but the repository should define how versions relate to revisions, releases, and baseline states.

**Contrast / learner note.** In some organisations *revision* is used for documents and *version* for software; consistency matters more than preference.

**Related terms.** revision, release, baseline, change history

### approval authority

**Definition.** An approval authority is the person or function formally empowered to accept, approve, release, or authorise a document, change, waiver, or deliverable.

**Example.** Final approval authority remained with the project technical lead following completion of the review cycle.

**Usage note.** Useful in controlled workflows and governance language.

**Contrast / learner note.** Reviewing a document does not automatically mean holding approval authority.

**Related terms.** authorisation, sign-off, review, release

### lead time

**Definition.** Lead time is the elapsed time between initiation of a request or order and the availability, delivery, or completion of the requested output.

**Example.** Long lead time for the replacement interface board influenced the temporary support plan.

**Usage note.** Important in procurement, logistics, maintenance support, and schedule risk discussions.

**Contrast / learner note.** Lead time is different from processing time or transit time, although these may contribute to total lead time.

**Related terms.** schedule risk, availability, spare part, procurement planning

### compliance matrix

**Definition.** A compliance matrix is a structured table showing how a proposal, design, or deliverable addresses each stated requirement or evaluation criterion.

**Example.** The supplier response included a compliance matrix linking each requirement to evidence, assumptions, and planned verification.

**Usage note.** Very useful in proposal evaluation, requirement review, and structured technical assessment.

**Contrast / learner note.** A matrix is valuable only if statements are evidence-based rather than declarative and unsupported.

**Related terms.** traceability, requirement, evidence, evaluation

## Repository governance language to prefer

- issue a revised document
- record the current status in the document register
- use the controlled copy as the reference source
- submit the deliverable by the agreed milestone
- identify the approval authority before release


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

