# Safety and Risk Terms

!!! abstract "Scope of this glossary"
    This glossary supports professional communication about hazards, exposure, protective measures, and incident-related reasoning. The goal is to help learners write safety-oriented English that is precise, calm, and non-dramatic, which is a key feature of competent engineering communication.

## How to read and reuse the entries

Each entry is written for **active professional use**. The definition gives conceptual precision, the example shows sentence-level application, and the usage note explains where the term is especially valuable in engineering communication. Where helpful, a contrast note is added to prevent common learner mistakes.

## Best fit inside this course

- Best aligned with `modules/05-safety-and-compliance.md`, `modules/15-safety-risk-and-incident-communication.md`, `document-templates/incident-report-template.md`, and `quality-assurance/repository-review-playbook.md`.

## Glossary entries

### hazard

**Definition.** A hazard is a source, situation, or condition with the potential to cause harm, damage, or other adverse consequences.

**Example.** Exposed conductive surfaces created an electrical hazard during maintenance access.

**Usage note.** Use hazard to identify the source of possible harm, not the probability that harm will occur.

**Contrast / learner note.** Hazard and risk are not the same. The hazard is the source of danger; the risk combines likelihood and severity.

**Related terms.** risk, exposure, control measure, unsafe condition

### risk

**Definition.** Risk is the combination of the likelihood of occurrence of harm and the severity of the consequences if the harmful event occurs.

**Example.** The residual risk was considered acceptable after additional guarding and lockout measures were introduced.

**Usage note.** Risk language should normally be supported by an assessment method, rating logic, or qualitative judgement framework.

**Contrast / learner note.** Avoid using *risk* as a loose synonym for *problem*. In safety writing, the term has a structured meaning.

**Related terms.** hazard, severity, likelihood, mitigation

### mitigation

**Definition.** Mitigation is the reduction of risk through design change, procedural control, protective measure, training, or other intervention.

**Example.** Risk mitigation included relocation of the interface, clearer labelling, and a revised inspection step.

**Usage note.** Use this term in safety notes, design reviews, and incident follow-up actions.

**Contrast / learner note.** Mitigation reduces risk but may not eliminate the hazard completely.

**Related terms.** control measure, protective action, residual risk, prevention

### exposure

**Definition.** Exposure is the state of being subjected to a hazard, environmental condition, or harmful influence.

**Example.** Prolonged exposure to contamination increased the probability of connector degradation.

**Usage note.** The term is useful in both safety and reliability discussions, especially when environment matters.

**Contrast / learner note.** Exposure describes contact or presence in relation to a hazard; it does not by itself describe the final consequence.

**Related terms.** hazard, duration, susceptibility, operating environment

### severity

**Definition.** Severity is the measure of how serious the consequences of a hazardous event or failure could be.

**Example.** Although the likelihood was low, the severity of uncontrolled thermal escalation justified immediate design review.

**Usage note.** Usually appears with likelihood when discussing risk assessment.

**Contrast / learner note.** Severity concerns consequence magnitude, not frequency.

**Related terms.** likelihood, consequence, risk rating, criticality

### likelihood

**Definition.** Likelihood is the probability or relative chance that a hazardous event, failure, or unwanted condition will occur.

**Example.** Improved cable retention reduced the likelihood of accidental disconnection during maintenance handling.

**Usage note.** Useful in qualitative and quantitative risk language.

**Contrast / learner note.** Likelihood is not the same as exposure duration, although exposure can influence likelihood.

**Related terms.** probability, frequency, severity, occurrence

### safe state

**Definition.** A safe state is the condition into which a system moves or is placed to minimise harm following a fault, abnormal condition, or emergency action.

**Example.** On loss of communication, the controller transitions to a predefined safe state and inhibits further motion commands.

**Usage note.** Use this term in control logic, safety functions, hazard analyses, and emergency procedures.

**Contrast / learner note.** A safe state is not always a full shutdown. It is the condition judged safest for the specific system and context.

**Related terms.** fail-safe behaviour, emergency stop, inhibition, protective logic

### protective measure

**Definition.** A protective measure is any design feature, device, barrier, warning, or procedural control intended to reduce exposure or consequence.

**Example.** The protective measure selected for the interface zone combined physical shielding with access restrictions.

**Usage note.** Useful in formal safety writing because it stays neutral and technically broad.

**Contrast / learner note.** Prefer *protective measure* to vague wording such as *something was added for safety*.

**Related terms.** mitigation, barrier, control, safeguard

### incident

**Definition.** An incident is an unplanned event that resulted in, or had the potential to result in, harm, damage, interruption, or reportable abnormality.

**Example.** The incident caused temporary system unavailability but no damage to adjacent equipment.

**Usage note.** This term is common in safety reporting, operational summaries, and investigation notes.

**Contrast / learner note.** An incident may involve consequences; a near miss is usually an event that could have led to harm but did not.

**Related terms.** event, near miss, nonconformity, occurrence

### near miss

**Definition.** A near miss is an event that did not result in harm or damage but had the potential to do so under slightly different circumstances.

**Example.** The dropped fastener was classified as a near miss because no component damage occurred and the foreign object was recovered immediately.

**Usage note.** Near-miss reporting is important because it reveals vulnerabilities before more serious outcomes occur.

**Contrast / learner note.** Do not downplay near misses. They often provide high-value learning with low-cost consequences.

**Related terms.** incident, hazard, learning action, prevention

### emergency shutdown

**Definition.** Emergency shutdown is the rapid and deliberate stopping of a system or process to reduce danger or prevent escalation during an unsafe condition.

**Example.** Emergency shutdown was initiated after abnormal temperature rise exceeded the defined intervention threshold.

**Usage note.** Use this phrase in procedures, safety analyses, and event descriptions where controlled stopping is part of the safety strategy.

**Contrast / learner note.** Not every stop is an emergency shutdown. The term implies a defined protective response to a hazardous or abnormal condition.

**Related terms.** safe state, protective logic, emergency procedure, isolation

### residual risk

**Definition.** Residual risk is the remaining level of risk after planned control measures and mitigations have been applied.

**Example.** Residual risk remained acceptable provided that the inspection interval was respected and trained personnel performed the task.

**Usage note.** This term is useful when explaining why design and procedural controls do not eliminate all risk but reduce it to an acceptable level.

**Contrast / learner note.** Residual risk should be explicitly acknowledged rather than hidden by overconfident language.

**Related terms.** mitigation, acceptance, control measure, safety case

## Tone guidance for safety writing

Safety writing should remain factual, controlled, and evidence-based. Strong safety communication does not rely on dramatic vocabulary. Instead, it uses structured statements such as *the hazard was identified*, *the risk was reduced*, *exposure was limited*, and *the residual risk was accepted subject to defined controls*.


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

