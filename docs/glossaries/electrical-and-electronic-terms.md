# Electrical and Electronic Terms

!!! abstract "Scope of this glossary"
    This glossary supports technical communication involving electrical power, signal transmission, electronic assemblies, instrumentation, and control hardware. The selected terms are broad enough for B2 learners but specific enough to improve the quality of engineering descriptions, troubleshooting notes, and test documentation.

## How to read and reuse the entries

Each entry is written for **active professional use**. The definition gives conceptual precision, the example shows sentence-level application, and the usage note explains where the term is especially valuable in engineering communication. Where helpful, a contrast note is added to prevent common learner mistakes.

## Best fit inside this course

- Best aligned with `modules/06-describing-systems-and-architectures.md`, `modules/08-performance-testing-and-evaluation.md`, `modules/14-troubleshooting-and-fault-analysis.md`, and `templates/test-report-template.md`.

## Glossary entries

### voltage

**Definition.** Voltage is the electrical potential difference between two points and is the driving condition that enables current to flow in a circuit.

**Example.** Input voltage remained within the specified limits throughout the endurance test.

**Usage note.** Use voltage when documenting electrical limits, power conditions, test setup, and interface behaviour.

**Contrast / learner note.** Do not confuse voltage with current. Voltage is the potential difference; current is the flow of electric charge.

**Related terms.** current, power supply, overvoltage, input range

### current

**Definition.** Current is the flow of electric charge through a conductor or circuit path, usually measured in amperes.

**Example.** Current draw increased significantly during startup but stabilised once the control loop reached nominal operation.

**Usage note.** Useful in performance reports, troubleshooting, power budgeting, and safety notes.

**Contrast / learner note.** Learners sometimes write *consumption* where *current draw* is needed. Consumption is broader and less precise.

**Related terms.** voltage, load, power, protection

### resistance

**Definition.** Resistance is the opposition that a material or circuit element presents to the flow of electric current.

**Example.** Connector resistance rose after repeated environmental exposure, indicating possible contact degradation.

**Usage note.** Use this term when discussing electrical integrity, continuity checks, sensor elements, and fault diagnosis.

**Contrast / learner note.** In mechanical contexts, *resistance* may refer to opposition more generally, but in electrical documents it should be used with discipline and usually with measurable context.

**Related terms.** continuity, impedance, conductor, contact quality

### power supply

**Definition.** A power supply is the source or subsystem that provides electrical energy at the required voltage and current for a device or assembly.

**Example.** The power supply shall maintain stable output during transient load conditions.

**Usage note.** Essential in hardware descriptions, system architecture pages, and troubleshooting records.

**Contrast / learner note.** A power supply can be an external source or an internal subsystem; the document should clarify the architecture.

**Related terms.** input voltage, output regulation, load, protection

### signal

**Definition.** A signal is an electrical, electronic, or digital representation of information used for control, communication, monitoring, or measurement.

**Example.** The diagnostic signal remained intermittent until the connector interface was cleaned and re-seated.

**Usage note.** The term is highly flexible but should be qualified where useful: analogue signal, digital signal, control signal, feedback signal, or status signal.

**Contrast / learner note.** Avoid writing *data* when the text is really about the physical or logical signal path.

**Related terms.** interface, transmission, bandwidth, interference

### circuit

**Definition.** A circuit is the complete path or functional arrangement through which electric current flows or through which an electronic function is implemented.

**Example.** The protection circuit isolated the affected branch before the fault propagated to the main controller.

**Usage note.** Appropriate in design notes, fault analysis, electrical schematics, and hardware descriptions.

**Contrast / learner note.** A circuit is not the same as a system. It is usually one electrical or electronic part of a broader architecture.

**Related terms.** board, branch, connector, protection

### connector

**Definition.** A connector is a device that enables electrical, signal, or combined connections between cables, modules, boards, or external equipment.

**Example.** Inspection showed minor contamination on the connector contacts, which likely contributed to intermittent communication loss.

**Usage note.** Very common in assembly descriptions, maintenance findings, and interface control discussions.

**Contrast / learner note.** Connector issues are often described too vaguely. Where possible, state whether the problem concerns pin damage, retention, contamination, corrosion, or seating.

**Related terms.** interface, cable, contact resistance, continuity

### sensor

**Definition.** A sensor is a device that detects a physical condition or parameter and converts it into a signal suitable for monitoring or control.

**Example.** The temperature sensor shall provide stable output across the specified operating range.

**Usage note.** Use this term when describing instrumentation, feedback loops, monitoring systems, and test setups.

**Contrast / learner note.** A sensor detects; an actuator causes or controls action. Learners should keep the distinction clear.

**Related terms.** actuator, signal, calibration, monitoring

### actuator

**Definition.** An actuator is a device that converts electrical, hydraulic, pneumatic, or other input into physical motion or controlled action.

**Example.** The actuator response time exceeded the specified threshold during low-temperature testing.

**Usage note.** Common in mechanical-electrical integration, control systems, and functional testing.

**Contrast / learner note.** Do not describe an actuator only as a motor unless the system architecture actually reduces to that element. The actuator may include transmission and control functions.

**Related terms.** motor, control signal, response time, mechanism

### grounding

**Definition.** Grounding is the intentional electrical connection to a reference potential or protective earth for safety, stability, or signal integrity purposes.

**Example.** Improper grounding increased susceptibility to noise on the measurement channel.

**Usage note.** Important in safety discussions, EMC considerations, test setup descriptions, and installation instructions.

**Contrast / learner note.** Grounding problems may appear as signal instability, communication errors, or unexplained measurement drift.

**Related terms.** shielding, interference, protective earth, reference potential

### bandwidth

**Definition.** Bandwidth is the range of frequencies or data transfer capacity that a system, channel, or signal path can support effectively.

**Example.** The interface bandwidth was sufficient for nominal operation but became a limiting factor during high-rate data capture.

**Usage note.** Useful in communication, instrumentation, and performance discussions.

**Contrast / learner note.** In some documents bandwidth refers to data throughput in a broad sense; in others it has a more specific frequency-domain meaning. Context matters.

**Related terms.** throughput, signal quality, latency, communication channel

### interference

**Definition.** Interference is the unwanted effect of one electrical, electromagnetic, or signal source on another, causing degradation, noise, or instability.

**Example.** Electromagnetic interference was suspected after the sensor output showed repeatable disturbances near the transmitter housing.

**Usage note.** Use this term in test reports, troubleshooting notes, installation guidance, and compatibility discussions.

**Contrast / learner note.** Interference should be distinguished from random noise when the disturbance has a traceable source or coupling mechanism.

**Related terms.** noise, shielding, grounding, compatibility

## Typical electrical reporting patterns

- Input voltage remained within the specified range throughout the test.
- The signal path was interrupted at the connector interface.
- The sensor output showed increased noise under high-interference conditions.
- Corrective action focused on grounding, shielding, and connector integrity.


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
