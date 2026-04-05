# System Description Template

## Purpose

This template is intended for concise but professional description of a system, subsystem, assembly, or technical unit. It is especially useful in technical English training because it teaches the learner how to describe function, composition, interfaces, operating context, and constraints in a controlled way.

A system description should not read like marketing material. Its tone should be neutral, explanatory, and technically grounded.

---

## Recommended Content

A robust system description usually addresses the following:

- what the system is;
- what it is designed to do;
- what major elements it includes;
- how it interacts with other parts of the platform or architecture;
- under which conditions it operates;
- what limitations or assumptions apply.

---

## Template

```md
# [System / Subsystem Name]

## 1. Overview
[Provide a concise description of the system and its purpose.]

## 2. Primary Function
[State the main function or mission of the system.]

## 3. Main Components
- [Component / module 1]
- [Component / module 2]
- [Component / module 3]

## 4. Operating Principle
[Explain, in a clear sequence, how the system performs its function.]

## 5. Interfaces
[Describe relevant mechanical, electrical, digital, operational, or human-machine interfaces.]

## 6. Operating Conditions / Constraints
[Summarize environmental, installation, performance, or procedural constraints.]

## 7. Notes on Maintenance / Safety / Compliance
[Add relevant professional notes if required.]
```

---

## Model Example

# Remote Monitoring Unit

## 1. Overview
The remote monitoring unit is a compact electronic subsystem intended to collect, process, and transmit equipment condition data from a protected installation area to the supervisory interface.

## 2. Primary Function
Its primary function is to detect predefined status conditions, record relevant events, and provide timely information to the operator or control system.

## 3. Main Components
- sensor interface module  
- processing board  
- communication interface  
- power conditioning stage  
- protective enclosure

## 4. Operating Principle
The unit receives status inputs from connected sensors, processes the incoming signals against predefined logic conditions, and transmits the resulting status information to the receiving interface. When threshold conditions are exceeded, the unit generates an alert and records an event entry for later analysis.

## 5. Interfaces
The unit includes an electrical power interface, a communication interface to the supervisory system, and physical mounting points for installation on a vertical support structure.

## 6. Operating Conditions / Constraints
The system is intended for installation in controlled industrial environments. It shall be powered by a regulated DC source and should not be installed in high-vibration conditions unless additional mitigation measures are implemented.

## 7. Notes on Maintenance / Safety / Compliance
Routine inspection should include connector retention, enclosure integrity, and verification of indicator function. Any maintenance activity should be carried out with the power supply disconnected.

---

## Writing Notes

- Begin with purpose, not with excessive detail.
- Use present simple for stable technical facts.
- Separate description from evaluation.
- Do not overload the overview with every component detail.
- Add constraints explicitly if they affect use or interpretation.

## Cross-Links

- [Describing Systems and Architectures](../modules/06-describing-systems-and-architectures.md)
- [Phrasebank for Description](../language-tools/phrasebank-for-description.md)
- [Technical Description Exercises](../exercises/technical-description-exercises.md)
