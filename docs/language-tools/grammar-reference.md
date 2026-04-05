?# Grammar Reference for Technical English

## Why grammar matters in engineering writing

Grammar in technical English is not a decorative element and should never be treated as one. In engineering documentation, grammar determines whether the reader interprets a sentence as a verified fact, a design characteristic, a requirement, a recommendation, a possibility, a limitation, or a tentative conclusion. Vocabulary alone is not sufficient. Two sentences may contain the same technical terms and still communicate very different levels of certainty, obligation, or operational consequence.

For that reason, this page does not present grammar as a general-language subject detached from context. Instead, it focuses on the grammatical structures that most directly affect technical meaning, reviewability, and professional clarity.

## 1. Sentence architecture in technical prose

Technical sentences should normally be built around a clear relationship between **subject**, **action**, and **technical meaning**. Writers frequently lose clarity when they overload the sentence with subordinate clauses, vague connectors, and delayed reference.

### Weak pattern
*The component, which has been installed in the upper section of the frame and which is connected with the external connector and that has the purpose to support the whole system, was checked.*

### Stronger pattern
*The component is installed in the upper section of the frame and interfaces with the external connector. Its primary function is to support the assembly. The item was checked during the inspection.*

### Practical rule
When a sentence performs more than one function, consider splitting it. A reviewer should not have to decide whether the sentence is describing, evaluating, or recommending.

## 2. Articles and technical reference

Italian learners often underuse or misuse articles because Italian and English package technical reference differently.

### Definite article: **the**
Use **the** when the item is already known, defined by context, or identified by a specific function.

- *The connector on the lower panel shall remain accessible.*
- *The current configuration does not include the optional bracket.*

### Indefinite article: **a / an**
Use **a** or **an** when introducing one item as a non-specific member of a category.

- *A temporary bracket was installed for alignment verification.*
- *An additional inspection is recommended after transport.*

### Zero article
Do not add an article automatically before all technical nouns.

- *Surface contamination was observed.*
- *Continuity testing was repeated after reassembly.*
- *Damage was not detected during visual inspection.*

### Frequent learner issue
Italian writers often produce forms such as *the maintenance*, *the contamination*, or *the verification* when the noun is being used in a general or process sense. In English technical writing, many abstract and process nouns appear without an article unless they are specifically bounded by context.

## 3. Noun clusters and compound terminology

Engineering English relies heavily on compound noun structures such as:

- *power distribution unit*
- *signal integrity issue*
- *maintenance access panel*
- *configuration control record*
- *interface verification procedure*

These clusters are efficient but can become unreadable if they are overextended. When the cluster is too dense, convert part of it into a prepositional structure.

### Dense version
*external interface connector retention force verification requirement*

### Improved version
*requirement for verification of external interface connector retention force*

### Practical rule
Use compound nouns to increase efficiency, but not at the cost of readability. A good test is whether a first-time reviewer can parse the phrase without re-reading.

## 4. Present simple for stable technical meaning

The present simple is the default tense for facts, permanent characteristics, defined functions, and general process descriptions.

- *The enclosure protects the electronics from dust ingress.*
- *The sensor detects pressure variation and transmits status data to the controller.*
- *The procedure applies to the baseline configuration only.*

This tense is appropriate when the information is true as a design statement, not just as a historical event.

## 5. Past simple for completed actions and observations

Use the past simple when reporting actions performed, results observed, and events that occurred during a specific test, inspection, review, or incident.

- *The unit completed the full cycle without interruption.*
- *Minor wear was observed on the contact surface.*
- *The team reviewed the updated drawing during the design meeting.*

### Frequent learner issue
Do not use the present simple when reporting what happened in a defined completed event.

- weak: *During the test, the unit stops after 40 seconds.*
- correct: *During the test, the unit stopped after 40 seconds.*

## 6. Present perfect in technical review context

Use the present perfect when the past action is relevant to the current document state, current configuration, or current review cycle.

- *The document has been updated to reflect the revised torque values.*
- *Three non-conformities have been identified during the current review phase.*
- *The supplier has provided revised material data.*

This tense is useful when the result matters now, even if the exact time is secondary.

## 7. Passive voice: use and control

Passive voice is common and often useful in engineering communication because the action, result, or affected item may matter more than the actor.

### Typical valid uses
- *The connector shall be inspected before installation.*
- *Minor surface wear was observed during the inspection.*
- *Verification shall be performed by continuity testing.*
- *The issue was traced to intermittent signal loss at the interface.*

### Benefits of passive voice
- keeps focus on the equipment, condition, or procedure;
- supports neutral reporting tone;
- aligns with requirement and procedural language;
- reduces unnecessary emphasis on the actor when responsibility is already clear.

### Risks of passive voice
Passive voice becomes weak when it hides agency that actually matters.

- weak: *A decision was made to defer the update.*
- stronger: *The review board decided to defer the update.*

### Practical rule
Use passive voice when the actor is irrelevant, obvious, or secondary. Use active voice when responsibility, ownership, or decision authority matters.

## 8. Modal verbs in technical English

Modal verbs are critical because they directly encode obligation, capability, recommendation, and possibility.

### **shall**
Use **shall** for formal requirements, especially in specifications, acceptance criteria, and controlled documentation.

- *The enclosure shall maintain integrity under nominal vibration conditions.*
- *The connector shall remain accessible for inspection.*

### **should**
Use **should** for recommendations, preferred practice, or non-mandatory guidance.

- *A follow-up inspection should be performed after transport.*
- *The revision history should include a short description of each major change.*

### **may**
Use **may** for permission or possibility depending on context.

- *The module may be removed after electrical isolation has been confirmed.*
- *The observed deviation may be associated with local contamination.*

### **can**
Use **can** mainly for capability or general possibility, not formal permission in specifications.

- *The interface can support remote diagnostics.*
- *This configuration can reduce maintenance time under normal conditions.*

### **must**
Use **must** with care. In some organisations it expresses strong obligation; in others, **shall** is preferred in formal requirements and **must** is reserved for procedural urgency or safety-critical instruction.

- *Operators must not energise the unit before closure is verified.*

### Frequent learner issue
Italian writers often overuse **must** because it feels direct and strong. In controlled requirement writing, **shall** is often more appropriate and more standard.

## 9. Conditionals in procedures and diagnostics

Conditional structures are essential in troubleshooting, maintenance, and risk communication.

### First conditional for operational logic
- *If contamination is detected, the surface shall be cleaned before energisation.*
- *If the issue persists after replacement, further analysis is required.*

### Zero conditional for stable procedural truth
- *If the connector is not fully seated, continuity cannot be guaranteed.*
- *If the seal is damaged, moisture ingress becomes more likely.*

### Practical rule
Use conditionals to express controlled decision logic, not to add vagueness. A strong conditional sentence identifies the condition, the response, and the consequence clearly.

## 10. Relative clauses for technical precision

Relative clauses allow the writer to define exactly which component, signal, requirement, or event is being referred to.

- *The connector that interfaces with the external power unit shall remain accessible.*
- *Any item which shows evidence of deformation shall be quarantined for review.*
- *The version that was released on 12 March has now been withdrawn.*

Relative clauses are useful, but overuse can overload the sentence. If a clause becomes too long, convert it into a separate sentence.

## 11. Non-finite structures for concise technical style

Technical writing often uses non-finite verb forms to compress information efficiently.

### Infinitive of purpose
- *The support bracket is designed to reduce vibration transfer.*
- *The update was introduced to improve traceability.*

### -ing form in process descriptions
- *After completing the inspection, the operator shall record the results.*
- *Repeated startup cycling was performed to assess recurrence.*

### Past participle in condensed description
- *The revised drawing attached to this message supersedes the previous issue.*
- *The data collected during the retest confirmed the original trend.*

These structures are useful, but they must remain unambiguous. A condensed sentence is only better if it remains easy to interpret.

## 12. Comparatives and qualification

Engineering communication often requires comparison, but comparison must be controlled and evidence-based.

- *The revised configuration is more accessible during maintenance.*
- *This option is less vulnerable to connector strain during transport.*
- *The measured deviation was slightly higher than the specified threshold.*

### Avoid vague comparison
- weak: *This solution is better.*
- stronger: *This solution provides better maintenance access and reduces removal time by approximately 15 percent.*

## 13. Quantifiers and approximation language

Technical writers must distinguish between exact, bounded, and approximate statements.

### Exact or bounded language
- *three fasteners*
- *within the specified range*
- *less than 2 mm*
- *no measurable deformation*

### Approximation language
- *approximately*
- *about*
- *in the order of*
- *slightly above*
- *roughly equivalent*

Approximation is not a weakness when it is justified. It becomes a weakness only when it is used instead of available data.

## 14. Cause, evidence, and conclusion

A technically mature sentence distinguishes between:

- what was observed;
- what was inferred;
- what was demonstrated.

### Examples
- *Surface residue was observed near the connector interface.* → observation
- *The residue appears to be associated with seal degradation.* → interpretation
- *Laboratory analysis confirmed seal material breakdown.* → verified conclusion

### Practical rule
Do not present an interpretation as a fact unless the evidence supports it.

## 15. Negation and limitation

Technical writing often needs to state not only what is true, but also what is **not** included, **not** observed, or **not** yet confirmed.

- *No abnormal behaviour was detected during the test.*
- *The current assessment does not include environmental stress conditions.*
- *This conclusion cannot be extended to long-duration field use.*

Negation should be precise. Avoid broad, casual phrases such as *there was no problem* when a narrower technical statement is possible.

## 16. Punctuation for readability and control

Punctuation strongly affects readability in technical English.

### Commas
Use commas to separate introductory clauses and prevent misreading.

- *After reassembly, the unit shall undergo continuity verification.*

### Semicolons
Useful when linking two closely related clauses without overusing conjunctions.

- *The enclosure remained intact; however, local contamination was observed near the access port.*

### Colons
Useful for introducing lists, explanations, or formal categories.

- *The inspection covered three areas: external damage, interface cleanliness, and fastener condition.*

### Practical rule
Do not use punctuation to imitate spoken rhythm. Use it to clarify structure.

## 17. Typical grammar risk areas for Italian-speaking engineers

### Prepositions
Italian-English transfer often produces incorrect prepositions.

- correct: *compliant with*
- not: *compliant to*
- correct: *related to*
- not: *related with* in many technical contexts
- correct: *responsible for*
- not: *responsible of*

### Verb choice after nouns
- correct: *perform a check*
- not: *make a control*
- correct: *carry out an inspection*
- not: *execute a control* unless the context is very specific

### Word order
English technical prose usually prefers a more linear and explicit order than Italian.

- weaker: *Regarding the issue that during the test has been found...*
- stronger: *During the test, the issue was identified...*

## 18. Grammar review checklist

Before releasing a technical text, verify the following:

- Is each sentence performing one clear function?
- Are observations clearly separated from interpretation?
- Are modal verbs used consistently?
- Is passive voice used where appropriate, but not to hide responsibility?
- Are time references consistent across the paragraph?
- Are conditionals explicit and operationally clear?
- Are limitations stated precisely?
- Are articles and prepositions natural in English, not transferred from Italian?

## 19. Mini practice: revising sentence function

### Example 1
*The system may fail because the connector is damaged and it must be replaced and checked.*

### Improved version
*The connector shows evidence of damage. The condition may affect system reliability. The connector shall be replaced and the interface shall be checked before the next operating cycle.*

### Example 2
*The document has many changes and should be approved because it is updated.*

### Improved version
*The current revision incorporates the agreed interface changes. Subject to final review of Section 6, the document is ready for approval.*

## Final note

!!! tip "Grammar is an engineering control, not only a language topic"
    In professional technical communication, grammar is one of the mechanisms that control interpretation. Good grammar reduces ambiguity, improves review efficiency, and protects the writer from making claims that the evidence does not support.

