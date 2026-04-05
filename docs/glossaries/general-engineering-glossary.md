# General Engineering Glossary

!!! abstract "Scope of this glossary"
    This page covers cross-disciplinary terms that appear repeatedly in technical descriptions, requirements, reports, design reviews, and engineering discussions. The vocabulary here is deliberately broad: it helps learners describe systems before they specialise into mechanical, electrical, maintenance, compliance, or defence-oriented language.

## How to read and reuse the entries

Each entry is written for **active professional use**. The definition gives conceptual precision, the example shows sentence-level application, and the usage note explains where the term is especially valuable in engineering communication. Where helpful, a contrast note is added to prevent common learner mistakes.

## Best fit inside this course

- Especially useful with `modules/01-introduction-to-technical-english.md`, `modules/02-engineering-vocabulary-foundations.md`, `modules/05-describing-components-and-assemblies.md`, and `modules/06-describing-systems-and-architectures.md`.

## Glossary entries

### component

**Definition.** A component is an individual part of a system or assembly that performs a specific function and can usually be identified, described, replaced, or tested as a distinct element.

**Example.** The power conditioning component was replaced after the inspection revealed unstable output under high thermal load.

**Usage note.** Use this term when you need a precise alternative to generic words such as *part* or *piece*. It is highly appropriate in technical descriptions, maintenance records, and configuration lists.

**Contrast / learner note.** Do not treat *component*, *subsystem*, and *module* as automatic synonyms. A component is usually smaller and more specific than a subsystem.

**Related terms.** assembly, module, subsystem, item

### assembly

**Definition.** An assembly is a set of components joined together to perform a combined function or to form a larger technical unit.

**Example.** The actuator assembly consists of the motor, gearbox, mounting bracket, and electrical connector.

**Usage note.** This term is common in mechanical documentation, installation instructions, illustrated parts lists, and manufacturing notes.

**Contrast / learner note.** An assembly is usually something physically put together. A *system* may include software, interfaces, procedures, and human interaction in addition to physical hardware.

**Related terms.** component, subassembly, integration, installation

### interface

**Definition.** An interface is the defined point or mechanism through which two elements interact, exchange signals, transfer energy, or connect mechanically.

**Example.** The interface between the control unit and the sensor package shall remain stable during continuous operation.

**Usage note.** Use *interface* in systems engineering, electrical descriptions, architecture summaries, and integration discussions.

**Contrast / learner note.** Avoid vague sentences such as *the units are connected somehow*. A good technical sentence identifies the interface and, when necessary, the type of interface.

**Related terms.** connection, connector, protocol, integration

### specification

**Definition.** A specification is a formal statement of technical characteristics, limits, functions, materials, dimensions, or performance expectations that a product, process, or service must satisfy.

**Example.** The environmental specification defines the temperature, vibration, and humidity limits for normal operation and storage.

**Usage note.** This term is central in design, procurement, test planning, compliance work, and customer communication.

**Contrast / learner note.** A specification describes what is required or permitted. A *report* describes what was observed or completed.

**Related terms.** requirement, standard, acceptance criteria, tolerance

### requirement

**Definition.** A requirement is a mandatory statement that defines what a system, subsystem, or process shall do or what condition it shall satisfy.

**Example.** One system requirement states that the monitoring unit shall record event data for a minimum of thirty days.

**Usage note.** Use this word with discipline. In professional writing, a requirement is not just a wish or preference; it implies obligation and traceability.

**Contrast / learner note.** A requirement is mandatory. A recommendation or design preference is not automatically a requirement.

**Related terms.** shall, constraint, compliance, verification

### configuration

**Definition.** Configuration refers to the documented arrangement of functional and physical characteristics of a system or item at a given point in time.

**Example.** The test was performed using the baseline configuration defined in the current integration release.

**Usage note.** This term is important in testing, document control, maintenance, and change management.

**Contrast / learner note.** Do not confuse *configuration* with *setup* in a casual sense. Configuration usually implies controlled and recorded technical status.

**Related terms.** baseline, version, change, configuration item

### integration

**Definition.** Integration is the process of combining components, modules, or subsystems so that they operate together as an intended whole.

**Example.** The integration phase revealed a timing mismatch between the communication unit and the supervisory controller.

**Usage note.** Use this term in programme planning, test reports, system descriptions, and project reviews.

**Contrast / learner note.** Integration is not the same as installation. Installation may be one step within a broader integration activity.

**Related terms.** interface, compatibility, validation, deployment

### reliability

**Definition.** Reliability is the probability or demonstrated ability of a system or item to perform its intended function under stated conditions for a specified period of time.

**Example.** Reliability data showed that the revised connector design reduced intermittent signal loss during vibration exposure.

**Usage note.** This term is essential in performance discussions, qualification evidence, maintenance strategy, and lifecycle planning.

**Contrast / learner note.** Reliability is different from *availability*. A system may be reliable in design but unavailable if logistics or maintenance support are inadequate.

**Related terms.** availability, durability, failure rate, maintainability

### performance

**Definition.** Performance refers to how effectively a system, component, or process achieves its intended function when assessed against defined criteria.

**Example.** The performance of the monitoring software remained within the specified response time across the full operating range.

**Usage note.** The word is common but should be supported by measurable criteria whenever possible.

**Contrast / learner note.** Avoid empty statements such as *good performance*. State what parameter is being discussed: accuracy, efficiency, response time, throughput, endurance, or stability.

**Related terms.** efficiency, capability, accuracy, response time

### operating conditions

**Definition.** Operating conditions are the environmental, electrical, mechanical, and procedural circumstances under which a system is expected to function.

**Example.** The unit was tested under representative operating conditions, including high humidity and continuous duty cycle.

**Usage note.** This phrase is especially useful when linking requirements, test methods, and design constraints.

**Contrast / learner note.** Do not confuse operating conditions with storage conditions or transport conditions unless the document explicitly compares them.

**Related terms.** environmental limits, duty cycle, operating range, service conditions

### verification

**Definition.** Verification is the process of confirming that specified requirements have been met, usually through inspection, analysis, test, or demonstration.

**Example.** Requirement verification was completed through bench testing and document review.

**Usage note.** Use this term in formal project language, especially where evidence must be linked to a requirement.

**Contrast / learner note.** Verification asks whether the item was built correctly against the specification. Validation asks whether the correct solution was chosen for the intended use.

**Related terms.** validation, acceptance, requirement, traceability

### deployment

**Definition.** Deployment is the controlled introduction of a system, software build, capability, or technical solution into operational or field use.

**Example.** Deployment of the updated software package was postponed until the interface issue had been closed.

**Usage note.** This term is common in software, systems, operational planning, and support documentation.

**Contrast / learner note.** Deployment is broader than release or installation. It often includes coordination, configuration control, user readiness, and support arrangements.

**Related terms.** release, installation, rollout, operational use

## Preferred collocations on this page

- meet a requirement
- define an interface
- verify compliance
- control the configuration
- assess performance under representative operating conditions
- complete subsystem integration before deployment


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

