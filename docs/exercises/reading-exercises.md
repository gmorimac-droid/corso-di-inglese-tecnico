# Reading Exercises

## Purpose

The objective of this page is to develop the learner's ability to read technical documents efficiently and accurately. In professional engineering contexts, reading rarely means reading everything line by line. It usually means identifying the purpose of the document, extracting key information, detecting constraints, understanding risks, and distinguishing between primary and secondary information.

The tasks below are designed to train this operational reading competence.

## Reading Strategy for Technical English

Before starting the exercises, the learner should apply the following strategy:

1. Identify the probable document type.
2. Detect the communicative purpose.
3. Locate keywords linked to performance, safety, maintenance, or requirements.
4. Separate facts from recommendations.
5. Extract the information that would matter in a real engineering workflow.

---

## Exercise 1 — Identifying Document Purpose

Read the short excerpt below and answer the questions.

> The monitoring unit is intended for indoor installation in controlled industrial environments. The enclosure provides IP54 protection against dust ingress and limited water exposure. The unit shall be mounted on a vertical support surface and connected to a regulated 24 V DC power source. Installation in high-vibration environments is not recommended unless additional damping measures are implemented.

### Tasks
1. What is the main purpose of the text?
2. What type of document is this most likely taken from?
3. Which three installation constraints are explicitly stated?
4. Which requirement is mandatory and which statement is advisory?

### Reviewer Notes
The learner should identify that the paragraph is not a product advertisement. It is a controlled technical description combining environmental constraints, installation requirements, and recommendations.

---

## Exercise 2 — Extracting Technical Constraints

Read the excerpt and complete the table.

> The actuator assembly was tested at ambient temperatures ranging from -20°C to +55°C. Full stroke performance was achieved throughout the range, although response time increased by approximately 8 percent at the upper limit. The unit remained operational after exposure to repeated vibration cycles; however, the cable retention bracket showed visible wear after extended testing.

### Extract the following:
- tested temperature range;
- parameter that changed during testing;
- amount of change;
- subsystem that showed degradation;
- whether the system remained operational.

### Follow-Up
Write a two-sentence summary that distinguishes clearly between **performance variation** and **functional failure**.

---

## Exercise 3 — Warning, Caution, or Note?

Read the three statements and classify each as a **Warning**, **Caution**, or **Note**.

1. Disconnect the power supply before opening the enclosure to avoid the risk of electric shock.
2. Do not exceed the recommended torque value when securing the mounting screws, as thread damage may occur.
3. The status indicator may remain illuminated for up to five seconds after shutdown.

### Tasks
For each statement:
- classify it;
- explain why;
- rewrite it in a more formal technical style if necessary.

### Review Focus
This exercise develops understanding of severity, consequence, and documentation tone.

---

## Exercise 4 — Reading for System Function

Read the excerpt and answer the questions.

> The sensor module detects thermal deviations within the protected compartment and transmits real-time status data to the control interface. If the measured value exceeds the predefined threshold, the system generates an alert and stores an event record for subsequent analysis. Under normal operating conditions, the event log is automatically synchronized with the supervisory workstation at regular intervals.

### Questions
1. What are the main functions of the sensor module?
2. What happens when the threshold is exceeded?
3. Which process occurs under normal operating conditions?
4. Which words indicate automation?

### Follow-Up Task
Write a three-sentence functional summary of the system.

---

## Exercise 5 — Reading a Fault Narrative

Read the fault narrative below.

> During scheduled inspection, maintenance personnel observed intermittent communication loss between the remote terminal and the central processing unit. Initial inspection confirmed that the power supply remained stable and that no abnormal temperature increase was present. Further investigation identified a partially loosened connector at the interface panel. After re-securing the connector and performing a communication check, normal operation was restored.

### Tasks
1. What was the observed symptom?
2. Which possible causes were excluded?
3. What was the root cause?
4. What corrective action was taken?
5. Which sentence confirms recovery?

### Review Focus
The learner should identify the sequence:
**symptom → checks → finding → corrective action → restored condition**

---

## Exercise 6 — Reading a Requirement Statement

Read the statements below.

1. The unit shall operate continuously for a minimum of 12 hours without external recharge.
2. The display should remain readable under direct ambient light.
3. The housing may be manufactured from aluminium alloy or equivalent material.
4. The interface cable must be protected from mechanical abrasion during routine handling.

### Tasks
For each sentence:
- identify whether the statement expresses a requirement, recommendation, permission, or obligation;
- explain the difference between **shall**, **should**, **may**, and **must** in this context;
- rewrite the four statements as part of a formal specification section.

---

## Exercise 7 — Reading for Comparison

Read the short comparison below.

> Compared with the baseline configuration, the revised assembly offers improved sealing performance, reduced cable routing complexity, and lower maintenance time. The revised version, however, requires a more precise alignment procedure during installation.

### Tasks
1. List the three advantages.
2. State the main trade-off.
3. Rewrite the paragraph as a short engineering evaluation note.

---

## Exercise 8 — Critical Reading and Reviewer Mindset

Read the paragraph below and identify weaknesses.

> The device is very good and works well in many situations. It is robust and does not usually fail. The installation is not too difficult if the technician knows what to do. The results were satisfactory.

### Tasks
1. Identify all vague or weak expressions.
2. Explain why the paragraph is unsuitable for professional technical documentation.
3. Rewrite it using more precise engineering language.

### Suggested Review Questions
- What does “very good” mean technically?
- What does “many situations” refer to?
- What measurable evidence supports “robust”?
- What makes the results “satisfactory”?

---

## Exercise 9 — Converting Reading into Documentation

Choose one of the excerpts on this page and transform it into one of the following:
- a system overview paragraph;
- a maintenance note;
- a requirement statement;
- a risk note;
- a short glossary entry.

### Output Requirement
Your text should be:
- technically coherent;
- professionally worded;
- between 80 and 150 words;
- suitable for inclusion in the MkDocs repository.

---

## Exercise 10 — Reading Under Time Pressure

Imagine you have only two minutes to read the following paragraph before a design review meeting.

> The updated power distribution unit incorporates an internal overcurrent protection stage and a revised terminal arrangement intended to simplify field servicing. The revised arrangement reduces cable crossover and improves accessibility; however, it increases the required enclosure depth by 12 mm. Validation testing confirmed nominal operation under standard load conditions, but extended testing under peak load remains pending.

### Tasks
In less than 60 words, prepare a briefing note covering:
- the design improvement;
- the main trade-off;
- the current validation status.

### Reviewer Focus
The learner should prioritize information and avoid full-sentence copying.

---

## Self-Review Checklist

Before finalizing your answers, verify the following:

- I identified the purpose of the text correctly.
- I extracted relevant technical information, not peripheral wording.
- I distinguished between requirement, recommendation, note, and warning.
- I avoided vague reformulation.
- My summary reflects the original technical meaning.
