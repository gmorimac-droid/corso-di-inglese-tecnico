from pathlib import Path
import textwrap

base = Path('/mnt/data/work_v2')
docs = base / 'docs'

def md_list(items):
    return '\n'.join(f'- {x}' for x in items)

course_pages = {
'index.md': """
# Technical English for Engineering B2

Welcome to **Technical English for Engineering B2 — Civil, Industrial and Defence-Oriented Contexts**. This site is designed as both a learning environment and a structured documentary repository. It is not intended to function as a traditional textbook alone. Instead, it combines language training, document analysis, controlled writing practice, and editorial discipline so that the learner progressively develops a professional command of technical English and transforms that competence into publishable documentation.

The course has been designed for learners who already possess an intermediate command of English and need to move toward a more reliable, more precise, and more professionally usable level. In engineering environments, language is rarely neutral or decorative. It supports design communication, documentation, verification, troubleshooting, safety, maintenance, procurement, and coordination between stakeholders. For this reason, the course treats English as an operational tool.

## What this site contains

This MkDocs site is organised as a technical learning portal. It includes:

- course framing pages, including methodology, learning outcomes, and assessment logic;
- eighteen structured modules covering core technical English, engineering communication, documentation, maintenance, safety, and defence-oriented terminology;
- glossaries organised by disciplinary domain and documentary function;
- phrasebanks and grammar references designed for professional writing and controlled oral communication;
- exercises, models, and templates suitable for classroom, self-study, or blended delivery;
- a final-project section supporting the production of a professional documentation website.

## Learning philosophy

The central principle of this course is that **language production should generate reusable documentation**. Each module is therefore expected to produce not only understanding, but also an output that can be revised, standardised, and published. A glossary entry, a short system description, a troubleshooting note, a safety warning, or a report summary can all become part of the final project if drafted with sufficient care.

## Intended learner profile

The site is suitable for:

- engineering students preparing for technical or industrial contexts;
- junior engineers who need stronger documentary English;
- maintenance and support personnel working with English-language documentation;
- systems, quality, or safety staff who must read and write formal technical content;
- professionals operating in civil, industrial, dual-use, or defence-related sectors where English is the working language of documents and coordination.

## Expected result

By the end of the course, the learner should be able to read, analyse, produce, revise, and organise technical English documentation at a solid B2 level. The final deliverable is not a single isolated assignment, but a coherent site containing evidence of technical reading, structured writing, terminological control, and editorial consistency.

## How to use the site

A recommended workflow is the following:

1. read the module overview and identify the communicative purpose of the topic;
2. study the key vocabulary and language patterns;
3. analyse the model examples critically;
4. complete the proposed reading, writing, and speaking tasks;
5. revise the output for clarity, consistency, and documentary suitability;
6. integrate the revised material into the final project section or into a thematic subpage.

The site may be used progressively during a course, or as a reference portal during independent study and revision.
""",
'course-overview.md': """
# Course Overview

## Course title

**Technical English for Engineering B2 — Civil, Industrial and Defence-Oriented Contexts**

## General description

This course develops the learner's ability to use English effectively in professional engineering environments. The focus is not limited to vocabulary acquisition. Equal importance is given to documentary structure, grammatical accuracy, phraseological control, communicative intent, and editorial discipline. The course therefore addresses both language competence and documentation competence.

The programme has been designed around a simple premise: in engineering, language has consequences. A requirement statement must not be ambiguous. A maintenance note must not omit the relevant conditions. A report summary must distinguish observation from interpretation. A safety warning must use the correct degree of obligation and risk indication. A system overview must allow the reader to understand architecture, interfaces, and operational purpose without unnecessary digression. These are precisely the communicative habits this course seeks to develop.

## Main thematic domains

The course covers six broad areas:

1. **Core Technical English**, including vocabulary, grammar, and text interpretation.
2. **Engineering Communication**, with emphasis on systems, processes, and performance.
3. **Documentation and Technical Writing**, including reports, emails, requirements, and controlled style.
4. **Maintenance, Troubleshooting, and Safety English**, with language for operational and support contexts.
5. **Defence-Oriented and Dual-Use Terminology**, treated from a documentary and professional perspective.
6. **Digital Documentation Project**, using Markdown, MkDocs, and GitHub as the publication framework.

## Pedagogical logic

The course moves from input to output in a structured way. Learners first analyse models and terminology, then practise controlled production, and finally refine their texts so that they can be published as documentation. This means that language learning and content management proceed in parallel.

## Course outputs

Typical outputs include:

- glossary entries;
- controlled technical descriptions;
- short procedural texts;
- requirement statements;
- safety notes and incident summaries;
- maintenance and troubleshooting records;
- meeting summaries and technical emails;
- architecture overviews and test summaries;
- documentation pages ready for inclusion in the final MkDocs site.

## Why MkDocs and GitHub are part of the course

In many professional environments, technical language is inseparable from technical documentation practice. Engineers and technical specialists are increasingly expected to write in structured formats, manage versions, and maintain shared repositories. By using Markdown, MkDocs, and GitHub, the course connects language competence to a realistic documentation workflow.
""",
'learning-outcomes.md': """
# Learning Outcomes

At the end of the course, the learner is expected to demonstrate a solid B2-level command of technical English suitable for professional engineering communication. The outcomes below are organised by competence area.

## 1. Lexical and terminological control

The learner should be able to:

- recognise and use recurring engineering vocabulary with appropriate precision;
- distinguish general words from discipline-specific technical terms;
- select accurate nouns, verbs, and adjectives for component description, process explanation, and issue reporting;
- understand and apply frequent collocations such as *power distribution unit*, *scheduled maintenance interval*, *compliance requirement*, *fault isolation procedure*, and *design constraint*.

## 2. Reading and interpretation of technical documents

The learner should be able to:

- read and interpret short and medium-length technical texts with confidence;
- extract relevant information from specifications, manuals, procedural documents, data sheets, and reports;
- identify purpose, audience, scope, assumptions, and constraints in a technical text;
- distinguish measured data, inferred conclusions, recommendations, and mandatory instructions.

## 3. Technical writing

The learner should be able to:

- produce structured texts such as technical emails, short reports, summaries, requirement statements, and explanatory descriptions;
- apply a style that is concise, clear, and appropriate to engineering communication;
- use modal verbs and passive structures accurately when expressing requirements, procedures, compliance conditions, or observations;
- revise a draft to reduce ambiguity, inconsistency, redundancy, or excessive informality.

## 4. Oral professional communication

The learner should be able to:

- explain systems, functions, and procedures in a clear and logically organised way;
- take part in technical discussions, reviews, and briefings using controlled professional language;
- ask for clarification, confirm understanding, and report issues or constraints appropriately;
- summarise findings and recommendations for colleagues, supervisors, or stakeholders.

## 5. Documentary and editorial competence

The learner should be able to:

- structure information into reusable documentation units;
- organise pages, headings, examples, and reference material coherently in Markdown;
- maintain terminological consistency across multiple pages;
- contribute to a documentation repository using a rational information architecture.

## 6. Sector-specific awareness

The learner should be able to:

- adapt language to civil, industrial, and defence-oriented settings while maintaining a professional and neutral tone;
- recognise differences in terminology, register, and documentary expectations across sectors;
- produce language that is suitable for dual-use and institutional contexts without losing clarity or precision.
""",
'target-audience.md': """
# Target Audience

This course is intended for learners who need technical English as a working tool rather than as an abstract academic subject.

## Primary audience

The main target groups are:

- engineering students at upper-intermediate level who are preparing for internships, thesis work, or entry-level technical roles;
- junior engineers who must interact with English-language documentation on a daily basis;
- maintenance, support, testing, or quality personnel who need to read and write in a controlled technical style;
- learners in civil or industrial sectors who work with international suppliers, clients, or standards;
- personnel in dual-use or defence-related environments who need professional documentary English.

## Entry profile

A typical learner should already be able to:

- understand general English at approximately B1+/B2 level;
- read simplified technical passages with support;
- write basic work-related messages;
- discuss familiar technical topics with some hesitation but reasonable control.

## Needs addressed by the course

Learners often report one or more of the following needs:

- they know the technical subject in Italian but struggle to express it accurately in English;
- they can recognise many technical words when reading, but have difficulty using them actively in writing;
- they can write understandable texts, but the register is inconsistent or too informal;
- they need more confidence in technical meetings, briefings, and documentation reviews;
- they need a structured method for building a technical glossary and organising knowledge into a reusable repository.

## Suitable delivery modes

The course can be used in several ways:

- instructor-led classroom teaching;
- blended delivery with self-study and revision tasks;
- guided independent study;
- corporate or institutional language training;
- documentation-oriented technical English workshops.

## Not the intended focus

The course is not primarily designed for advanced literary study, general conversation, or academic essay writing. Its orientation is professional, technical, and documentary.
""",
'methodology.md': """
# Methodology

## General approach

The course follows a **document-driven technical English methodology**. This means that language is learned in connection with realistic texts, realistic purposes, and realistic output formats. The learner is not asked simply to memorise vocabulary or complete isolated grammar drills. Instead, the course trains the learner to analyse how technical meaning is constructed and then to reproduce that meaning in a controlled, professional way.

## Core methodological principles

### 1. Purpose before form

A sentence in technical English should be evaluated not only for grammatical correctness but also for communicative function. Before producing a text, the learner should ask:

- What is the purpose of this document?
- Who is expected to read it?
- What decision or action should it support?
- What degree of precision is required?

This focus helps the learner avoid generic phrasing and select language that is appropriate to the documentary context.

### 2. Controlled language rather than stylistic ornament

Technical English often benefits from lexical and structural repetition when repetition improves clarity. The learner is therefore encouraged to value consistency, explicitness, and stable patterns over stylistic variation for its own sake.

### 3. Progressive refinement

Most professional texts are improved through revision. Drafting and revising are both part of the learning process. Learners are expected to:

- produce a first version;
- verify terminology and structure;
- reduce ambiguity;
- improve sentence economy;
- re-check consistency of headings, references, and examples.

### 4. Output with documentary value

Each module should ideally end with an output that can be integrated into the final site. This transforms the course into a cumulative project and gives language practice a clear practical destination.

## Typical learning cycle

A standard module follows this cycle:

1. **Input** — reading a model, extracting terminology, observing phraseology.
2. **Analysis** — identifying communicative purpose, structure, and grammar patterns.
3. **Controlled practice** — completing targeted tasks on vocabulary, grammar, and sentence design.
4. **Production** — writing or presenting a short technical output.
5. **Revision** — improving the output according to documentary criteria.
6. **Publication** — adapting the revised text to Markdown and integrating it into the site.

## Role of translation

Translation is used selectively as a contrastive tool. It helps learners notice interference from Italian, false friends, and overly literal structures. However, the goal is not word-for-word conversion. The goal is professionally acceptable English.

## Role of oral communication

Speaking tasks are designed as briefings, explanations, updates, and review discussions. They are deliberately functional. Learners should practise concise, structured oral delivery rather than informal conversation alone.
""",
'assessment-framework.md': """
# Assessment Framework

Assessment in this course is intended to measure functional ability in technical English, not merely passive recognition. For this reason, evaluation combines diagnostic, formative, and summative elements.

## 1. Diagnostic assessment

At the beginning of the course, the learner's profile should be established through tasks such as:

- recognition of technical vocabulary;
- comprehension of a short technical extract;
- production of a brief system description;
- correction of typical grammar and style errors;
- discussion of a familiar engineering topic.

The objective is not to assign a rigid label but to identify strengths, weaknesses, and priority areas for development.

## 2. Formative assessment

Throughout the course, continuous evaluation should focus on the quality of intermediate outputs. Typical criteria include:

- accuracy of terminology;
- clarity of sentence structure;
- correctness of grammar and phraseology;
- relevance to communicative purpose;
- documentary suitability of the output;
- consistency across pages or assignments.

Feedback should be specific. Comments such as *too informal*, *insufficiently explicit*, *good terminology but weak paragraph structure*, or *requirement language not strong enough* are more useful than generic judgments.

## 3. Summative assessment

The final evaluation may combine several components:

- a portfolio of revised technical writing tasks;
- a selected oral performance, such as a briefing or system presentation;
- a reading-based analysis task;
- the final MkDocs project or a defined section of it.

## Suggested weighting model

A possible weighting model is:

- 20% diagnostic and early baseline tasks;
- 40% continuous production and revision tasks;
- 15% oral technical communication;
- 25% final project quality and documentary coherence.

This model can be adapted according to institutional needs.

## Suggested evaluation criteria for writing

A technical writing task may be evaluated on the basis of:

1. **Terminological precision**
2. **Grammatical reliability**
3. **Clarity and coherence**
4. **Register and tone**
5. **Document structure**
6. **Revision quality**

## Suggested evaluation criteria for the final site

The final project should be assessed not only as a language artefact but also as a documentation artefact. Relevant criteria include:

- coherence of navigation and file organisation;
- consistency of style across pages;
- quality of headings, examples, and cross-references;
- practical value of templates, glossaries, and worked examples;
- technical credibility of the language used.
""",
'study-plan.md': """
# Study Plan

This site supports a modular study plan that may be adapted to intensive, semester-based, or annual delivery. The structure below provides a recommended sequence.

## Phase 1 — Foundations

**Modules 01–04**

This phase establishes the conceptual and linguistic base of the course. Learners focus on:

- understanding what technical English is and how it differs from general English;
- building a foundational engineering vocabulary;
- revising grammar through a technical lens;
- learning to read technical texts strategically.

### Expected outputs

- introductory glossary entries;
- short descriptive paragraphs;
- reading-analysis notes;
- grammar and phraseology examples.

## Phase 2 — Core Engineering Communication

**Modules 05–08**

This phase develops the language required to describe parts, systems, processes, and performance. Learners begin to produce more substantial outputs and to organise information in a professional structure.

### Expected outputs

- component descriptions;
- system architecture summaries;
- process and workflow texts;
- test and performance summaries.

## Phase 3 — Documentation and Technical Writing

**Modules 09–12**

This phase focuses on professional written communication. Learners practise:

- concise technical style;
- technical emails;
- structured reports and meeting notes;
- requirements and compliance language.

### Expected outputs

- email models;
- report summaries;
- requirements lists;
- specification-style statements.

## Phase 4 — Operational and Support Communication

**Modules 13–15**

This phase addresses maintenance, troubleshooting, and safety communication. It is particularly relevant for real-world technical operations and support environments.

### Expected outputs

- maintenance records;
- fault reports;
- incident and safety notes;
- corrective-action summaries.

## Phase 5 — Sector-Specific Extension

**Modules 16–17**

This phase introduces defence-oriented and procurement-related terminology from a documentation perspective. The purpose is to widen sector awareness without losing linguistic control.

### Expected outputs

- sector comparison notes;
- terminology maps;
- document-control and programme-language examples.

## Phase 6 — Final Project and Publication

**Module 18 plus final-project section**

This final phase consolidates all previous work into a coherent MkDocs site.

### Expected outputs

- repository structure;
- refined page set;
- consistent navigation;
- polished portfolio;
- publishable documentation site.

## Recommended rhythm

A practical rhythm for each module is:

- session 1: input, reading, terminology;
- session 2: grammar and controlled practice;
- session 3: production, revision, and documentary output.

This structure allows the learner to move steadily from understanding to publication.
"""
}

for fname, content in course_pages.items():
    (docs / fname).write_text(textwrap.dedent(content).strip() + "\n", encoding='utf-8')

module_data = [
    ("01-introduction-to-technical-english","Introduction to Technical English",
     "introduce the learner to the logic, purpose, and documentary discipline of technical English in engineering contexts",
     ["technical communication","controlled language","documentary purpose","clarity","consistency","traceability","requirement","specification","procedure","verification"],
     ["use definitions, functional descriptions, and documentary formulations with improved control",
      "distinguish informal wording from professional engineering wording",
      "identify the purpose, audience, and expected action associated with a technical text",
      "produce a concise introductory page suitable for a documentation site"],
     "Technical English is best understood as a professional variety of English used to support engineering work. It does not exist merely to sound specialised. Its function is to transmit information accurately enough for design, operation, inspection, maintenance, verification, and coordination. In engineering, the quality of language is linked to the quality of action. If the wording is vague, incomplete, or poorly structured, the resulting interpretation may also be weak.",
     """In technical environments, the same topic can be expressed in very different ways depending on purpose. Compare the following examples:\n\n- *This part helps the machine work better.*  \n- *This component provides structural support to the actuator housing and reduces vibration under nominal operating conditions.*\n\nThe second sentence is more precise because it identifies function, scope, and conditions. Precision does not necessarily require longer sentences, but it does require more disciplined choices.""",
     ["present simple for facts and general functions",
      "passive voice for process and document neutrality",
      "modal verbs such as shall, must, should, and may for requirement strength",
      "relative clauses for definitions and technical identification",
      "noun clusters such as power supply module, signal conditioning board, or maintenance access panel"],
     "Read a short extract from a data sheet, system overview, or introductory technical note. Identify the purpose of the document, the type of reader, the main terms, and the degree of precision expected. Then rewrite one generic sentence so that it sounds more professional.",
     "Write a 220–300 word introductory text explaining what technical English is and why it matters in engineering documentation. The text should include at least five technical terms and at least three examples of professional wording.",
     "Prepare a two-minute explanation for a new team member who has strong technical knowledge but limited experience with English-language documentation.",
     "Translate a short Italian paragraph about the importance of clear technical documentation, then revise it to reduce literal translation and improve professional tone.",
     ["course home introduction","technical-English primer","mini style note on clarity and precision"]),
    ("02-engineering-vocabulary-foundations","Engineering Vocabulary Foundations",
     "build a disciplined technical vocabulary base that supports description, analysis, and documentation across multiple engineering domains",
     ["component","assembly","subsystem","housing","bracket","shaft","sensor","actuator","reliability","constraint","enhance","monitor","withstand","compliant","serviceable"],
     ["organise vocabulary by function, physical category, and documentary use",
      "differentiate near-synonyms and frequent collocations",
      "use compound nouns and technical adjectives more accurately",
      "create glossary entries with definitions, usage notes, and examples"],
     "Technical vocabulary is most useful when it is organised, not memorised in isolation. A learner who knows fifty unconnected words may still struggle to write a coherent paragraph, whereas a learner who understands the relationships between terms can build more accurate sentences. For example, *component*, *assembly*, *subsystem*, and *system* are not interchangeable. They describe different levels of technical organisation.",
     """Engineering vocabulary should be recorded in clusters. For example:\n\n- **Parts and structure**: housing, enclosure, bracket, fastener, support frame\n- **Function and behaviour**: detect, transmit, regulate, withstand, isolate\n- **Performance and condition**: reliable, stable, degraded, nominal, serviceable\n- **Documentary use**: requirement, interface, limitation, revision, verification\n\nThis clustered approach makes the vocabulary operational rather than decorative.""",
     ["compound nouns and technical naming conventions",
      "adjective order in technical descriptions",
      "verb patterns in function description: is designed to, is used to, enables, allows",
      "countable and uncountable nouns in technical prose"],
     "Analyse a short list of terms from a manual or system description. Group them by category, define them briefly, and identify two frequent collocations for each group.",
     "Create a glossary page with at least fifteen entries. Each entry should include a concise definition, one example sentence, and one note on typical misuse by Italian-speaking learners.",
     "Present five terms orally and explain how they relate to one another within a simple system or procedure.",
     "Translate a list of Italian technical terms and then comment on which equivalents are context-dependent rather than fixed.",
     ["core engineering glossary","useful technical verbs note","terminology-learning guide"]),
    ("03-grammar-for-technical-communication","Grammar for Technical Communication",
     "reframe grammar as a tool for precision, obligation, sequence, and documentary neutrality in engineering texts",
     ["passive voice","modal verb","requirement language","conditional statement","relative clause","sequence marker","tolerance","obligation","recommendation","constraint"],
     ["use modal verbs accurately in requirements and procedures",
      "apply passive constructions when the process or result is more relevant than the actor",
      "express cause, sequence, condition, and limitation clearly",
      "revise informal or ambiguous structures into professional formulations"],
     "Grammar in technical English should never be studied as a separate decorative layer. It directly shapes meaning. The difference between *can*, *should*, *must*, and *shall* is not merely grammatical. It affects obligation, acceptability, and sometimes compliance. Similarly, the choice between active and passive voice changes the focus of a sentence. Technical writing therefore requires grammatical control in the service of communicative accuracy.",
     """Consider the difference between these formulations:\n\n- *You have to inspect the connector before using the unit.*\n- *The connector shall be inspected before the unit is operated.*\n\nThe second version is more suitable for a formal procedure because it removes conversational tone and foregrounds the required action.""",
     ["modal verbs for requirement strength",
      "passive voice in procedure, testing, and reporting",
      "zero and first conditionals in operational logic",
      "relative clauses for defining components, interfaces, and constraints",
      "sequencing expressions for procedural clarity"],
     "Read a short procedure and underline all modal verbs. Decide whether each one expresses obligation, recommendation, permission, or capability. Then justify whether the wording is strong enough for the documentary purpose.",
     "Rewrite ten informal engineering sentences in a more controlled technical style, using passive voice, requirement language, and improved sequencing where appropriate.",
     "Explain orally why *shall* is not interchangeable with *should* in specifications and what problems may arise if requirement strength is poorly controlled.",
     "Translate an Italian procedural paragraph containing implicit obligations. Make the obligations explicit in English using appropriate modal forms.",
     ["grammar reference for technical English","requirement-language mini guide","rewriting examples page"]),
    ("04-reading-technical-texts","Reading Technical Texts",
     "develop strategic reading skills for manuals, specifications, reports, procedures, and data-focused engineering documents",
     ["scope","assumption","constraint","warning","caution","nominal","parameter","acceptance criteria","appendix","reference"],
     ["identify purpose, structure, and audience in technical documents",
      "extract key data from dense prose, lists, and tables",
      "distinguish fact, interpretation, and recommendation",
      "annotate texts for vocabulary, structure, and possible revision"],
     "Reading technical English efficiently requires a method. Unlike general reading, the objective is often highly selective. The reader may need to locate a limit value, verify an installation condition, identify a maintenance interval, or confirm whether a requirement is mandatory or advisory. Strategic reading is therefore as important as vocabulary.",
     """A good technical reader does not always proceed line by line. Instead, the reader asks:\n\n- What kind of document is this?\n- Which part of the text contains the information I need?\n- Which signals indicate risk, limitation, or exception?\n- Which terms are repeated because they are functionally important?\n\nThis analytical reading behaviour supports both comprehension and later writing.""",
     ["skimming for structure and document purpose",
      "scanning for values, warnings, conditions, and references",
      "recognising document signals such as note, warning, limitation, and acceptance criteria",
      "paraphrasing without distorting technical meaning"],
     "Read a two-page technical extract and create a structured note containing purpose, main sections, critical values, and any warnings or limitations found in the text.",
     "Write a short reading-analysis summary explaining what the document is for, which information it prioritises, and how a user should navigate it.",
     "Give a brief oral explanation of how you located the key information and why certain sections were more relevant than others.",
     "Translate selected sentences from a manual into Italian, then explain which parts are difficult because of condensed wording or sector-specific terminology.",
     ["reading-strategy page","annotation example","manual-analysis note"]),
    ("05-describing-components-and-assemblies","Describing Components and Assemblies",
     "train the learner to describe parts, physical arrangements, materials, and functional roles with technical precision",
     ["component","assembly","fastener","enclosure","connector","mounting bracket","housing","bearing","interface","alignment","tolerance","fitment"],
     ["identify parts and their relationships within an assembly",
      "describe geometry, position, and material choice",
      "use functional language to explain what a component does",
      "write concise yet sufficiently explicit component descriptions"],
     "Component description is a core engineering skill. A reader must be able to identify what the part is, where it is located, what it is made of, how it is connected, and what function it performs. The difficulty for many learners is that informal descriptions often omit one or more of these dimensions. Technical English encourages the writer to include the information that matters for operation, maintenance, or understanding of the assembly.",
     """A strong component description often answers five practical questions:\n\n1. What is the component called?\n2. Where is it located or mounted?\n3. What is its function?\n4. What is it made of or how is it protected?\n5. Which interfaces or constraints are relevant?\n\nFor example, a connector is not simply 'on the panel'. It may be *mounted on the rear access panel, protected by a sealing cap, and used to provide a temporary diagnostic interface during maintenance operations*.""",
     ["prepositions and patterns for position and mounting",
      "material and finish language: made of, coated with, protected against",
      "functional description: provides, supports, transfers, isolates, secures",
      "relative clauses for identifying part variants or installation conditions"],
     "Read a short assembly description and map each sentence to one of the five questions above. Identify any missing information that would be useful for a technician or reviewer.",
     "Write a 250–350 word description of a component or small assembly, including naming, location, function, interfaces, and relevant operational considerations.",
     "Present a simple part or assembly orally using an exploded-view logic: overall purpose first, then main elements, then functional relationships.",
     "Translate an Italian description of a mechanical or electromechanical part. Improve noun clusters, prepositions, and functional verbs in the English version.",
     ["component description page","assembly note","illustrated terminology section"]),
    ("06-describing-systems-and-architectures","Describing Systems and Architectures",
     "develop the language required to explain system hierarchy, subsystem roles, interfaces, signal flow, and operational logic",
     ["system architecture","subsystem","interface","input","output","data flow","power distribution","processing unit","communication link","redundancy","integration","dependency"],
     ["describe a system from high-level overview to subsystem detail",
      "explain interactions between mechanical, electrical, and software elements",
      "use architecture language to clarify hierarchy and interfaces",
      "produce system overview pages suitable for design, training, or documentation"],
     "System description requires more than a list of parts. It requires the writer to show how technical elements are organised and why they are organised in that way. A well-written system overview helps readers understand hierarchy, interfaces, dependencies, and operational purpose. It also helps non-specialist stakeholders follow the logic of the design without needing full design documentation.",
     """A strong architecture description usually progresses through distinct layers:\n\n- overall mission or purpose of the system;\n- major subsystems and their responsibilities;\n- main interfaces between those subsystems;\n- flow of energy, signal, or data;\n- critical constraints, dependencies, or redundancy features.\n\nWhen these layers are omitted, the reader may know the names of the elements but not understand the system as an integrated whole.""",
     ["overview-to-detail paragraph organisation",
      "interface language: exchanges data with, receives input from, provides output to",
      "cause-and-effect language in system behaviour",
      "use of present simple and passive voice in architecture summaries"],
     "Analyse a short system overview and identify which sentences describe purpose, which describe structure, which describe interfaces, and which describe constraints.",
     "Write a 300–400 word description of a notional system made up of sensing, processing, communication, and power-management subsystems. Use clear paragraphing and at least eight relevant collocations.",
     "Deliver a three-minute oral system briefing aimed at a mixed audience of engineers and technical managers. Focus on architecture, function, and interfaces rather than low-level design detail.",
     "Translate an Italian architecture overview and revise it to improve hierarchy, interface language, and paragraph logic.",
     ["system-overview page","architecture-summary example","subsystem interaction note"]),
    ("07-describing-processes-and-workflows","Describing Processes and Workflows",
     "teach the learner to explain sequences, procedures, decision points, and task dependencies in clear operational English",
     ["workflow","procedure","sequence","verification step","handover","inspection stage","decision point","precondition","post-condition","parallel activity"],
     ["use sequence markers and conditional language effectively",
      "distinguish process description from instruction writing",
      "explain dependencies, prerequisites, and outcomes",
      "produce clear process notes for technical and operational readers"],
     "Processes and workflows are central to engineering communication because they connect technical knowledge to action. A process description explains how work or system behaviour unfolds. A procedure instructs the reader on what to do. These are related but not identical genres, and technical English benefits from recognising the difference.",
     """In process writing, sequencing alone is not enough. The writer should also indicate:\n\n- prerequisites;\n- responsible role or function, where relevant;\n- expected outcome of each stage;\n- possible branches or exceptions;\n- verification points before closure or handover.\n\nWithout these elements, the text risks becoming a list of actions without operational logic.""",
     ["sequence markers and temporal linking",
      "conditional language for branches and exceptions",
      "purpose clauses and result clauses",
      "impersonal instruction style and role-based process language"],
     "Read a workflow description and convert it into a process map showing main stages, inputs, checks, and outputs.",
     "Write a 250–350 word process description for a technical activity such as inspection, data review, installation handover, or anomaly management.",
     "Explain a workflow orally as if you were briefing a new team member on how work moves from initial input to verified completion.",
     "Translate an Italian process description and revise it to improve sequence clarity and consistency of subject reference.",
     ["workflow description page","procedure comparison note","process phrasebank contribution"]),
    ("08-performance-testing-and-evaluation","Performance, Testing and Evaluation",
     "provide the language needed to describe performance criteria, test setups, observations, measured results, and engineering conclusions",
     ["test setup","performance metric","accuracy","reliability","repeatability","acceptance threshold","deviation","measured value","benchmark","verification"],
     ["describe tests with clear distinction between configuration, method, result, and conclusion",
      "use quantitative and comparative language appropriately",
      "summarise performance findings without overstatement",
      "write test-related texts that remain objective and traceable"],
     "Testing language must support evidence-based communication. This means that claims should be tied to conditions, measurements, references, or acceptance criteria. Learners often write conclusions too early or use imprecise evaluative language. A more professional approach distinguishes between what was tested, under which conditions, what was measured, and what can reasonably be concluded from the evidence available.",
     """A robust performance summary usually includes:\n\n- purpose of the test;\n- configuration or setup;\n- relevant operating conditions;\n- measured outcomes;\n- comparison with specified thresholds or expected behaviour;\n- residual limitations or recommendations.\n\nThis structure improves traceability and supports review or later reuse.""",
     ["comparative and quantitative language",
      "past simple and passive voice in test reporting",
      "hedging and caution in technical conclusions",
      "reporting deviations, tolerance bands, and acceptance criteria"],
     "Read a short test summary and separate the statements into configuration, observation, measurement, interpretation, and recommendation.",
     "Write a 300-word performance summary for a notional subsystem tested under nominal operating conditions, including at least three measured results and one limitation.",
     "Present the outcome of a test campaign orally in two minutes, focusing on what was verified, what was observed, and what remains to be addressed.",
     "Translate an Italian test-result paragraph and revise it to improve objectivity, quantification, and relation to criteria.",
     ["test summary page","performance comparison note","evidence-based conclusion guide"]),
    ("09-principles-of-technical-writing","Principles of Technical Writing",
     "establish a disciplined writing style based on clarity, consistency, conciseness, and documentary usefulness",
     ["clarity","conciseness","consistency","traceability","ambiguity","redundancy","controlled language","heading structure","cross-reference","document revision"],
     ["identify typical weaknesses in technical prose",
      "revise sentences to improve structure and meaning",
      "apply controlled style principles to longer passages",
      "produce writing that is reusable across documentation contexts"],
     "Technical writing is not defined by difficulty or density. Its quality depends on whether readers can understand and use the information without unnecessary effort or misinterpretation. Good technical writing is economical but not cryptic, explicit but not repetitive without purpose, and consistent across terms, headings, and document logic.",
     """Typical weaknesses in learner writing include:\n\n- undefined pronouns such as *it* or *they* with unclear reference;\n- long sentences containing several actions and no clear hierarchy;\n- inconsistent terminology, for example alternating between *device*, *unit*, and *system* without reason;\n- evaluative wording unsupported by technical evidence;\n- abrupt changes between formal and informal register.\n\nEach of these issues can be improved through controlled revision.""",
     ["sentence economy and information hierarchy",
      "noun phrase density and readability balance",
      "active vs passive voice according to communicative purpose",
      "signposting, cross-reference, and consistent heading design"],
     "Analyse a short technical paragraph and identify all points where clarity, consistency, or sentence economy could be improved.",
     "Revise a poorly structured text into a professional technical note of 250–300 words. Add headings or bullet structure where useful.",
     "Explain orally how you decide whether a sentence is too vague, too long, or too informal for technical documentation.",
     "Translate a loosely written Italian note into English, then revise it a second time to make it documentation-ready.",
     ["technical style guide","before-and-after revision page","writing checklist"]),
    ("10-technical-emails-and-professional-messages","Technical Emails and Professional Messages",
     "develop the ability to write professional emails that are clear, efficient, courteous, and technically usable",
     ["subject line","clarification","attachment","revision","status update","action item","follow-up","outstanding issue","confirmation","circulation"],
     ["structure technical emails logically",
      "write concise messages for requests, updates, and issue reporting",
      "maintain formal yet efficient register",
      "refer to documents, revisions, and actions precisely"],
     "Technical emails are often underestimated, yet they play a major role in coordination. A good technical email is not simply polite. It should allow the reader to understand what the issue is, why the message has been sent, what document or item is concerned, and what action is expected. Poor email structure generates delay, repetition, and documentary confusion.",
     """A strong professional email usually contains:\n\n- a subject line that supports later retrieval;\n- a brief contextual opening;\n- a clearly defined main point;\n- any required action, deadline, or requested clarification;\n- references to attachments, revision status, or previous correspondence;\n- a concise closing line.\n\nThis structure helps the message function both as communication and as a traceable project record.""",
     ["email openings and controlled courtesy",
      "clear requests and action-oriented phrasing",
      "referencing attachments, revisions, and meetings",
      "avoiding spoken-English interference in written messages"],
     "Review two model emails and compare them in terms of subject quality, structure, tone, and clarity of requested action.",
     "Write two emails: one requesting technical clarification on a document revision and one reporting a minor issue discovered during review.",
     "Role-play a short oral briefing that summarises the content of an email thread and the next required action.",
     "Translate an Italian work email into English, then improve concision, tone, and documentary precision.",
     ["email template page","subject-line guide","follow-up phrasebank note"]),
    ("11-reports-summaries-and-meeting-notes","Reports, Summaries and Meeting Notes",
     "train the learner to condense technical information into structured documentary formats for review, coordination, and traceability",
     ["executive summary","meeting minutes","action item","observation","finding","recommendation","open point","status","summary table","owner"],
     ["distinguish summary, report, and meeting-note genres",
      "organise information into headings and action-oriented sections",
      "record observations and decisions accurately",
      "produce concise documentation that remains useful over time"],
     "Reports and notes are central to technical communication because they preserve institutional memory. A meeting without clear minutes often produces uncertainty. A report without a disciplined summary forces the reader to reconstruct the main findings. This module therefore focuses on compression without loss of technical meaning.",
     """A useful summary is selective rather than merely shorter. It answers the questions a busy reader is likely to ask:\n\n- What was reviewed, tested, or discussed?\n- What were the main findings?\n- Which points remain open?\n- What action is required and by whom?\n- What is the current status or recommendation?\n\nIf these points are missing, the text may be grammatically correct but operationally weak.""",
     ["summary language and high-value sentence design",
      "past simple and passive voice in reporting completed activities",
      "action-item phrasing and owner assignment",
      "difference between neutral observation and recommendation"],
     "Read a meeting record and identify which lines are factual notes, which record decisions, and which define actions.",
     "Write a one-page meeting summary or short technical report using headings, bullet points, and a brief executive summary.",
     "Present orally the content of a technical review meeting as if reporting back to a supervisor who did not attend.",
     "Translate an Italian meeting note into English and improve the consistency of tense, style, and action-item wording.",
     ["meeting-notes model","executive-summary page","action-item language note"]),
    ("12-requirements-specifications-and-compliance","Requirements, Specifications and Compliance",
     "introduce the formal language of requirements, specifications, conditions, and compliance-oriented documentation",
     ["requirement","shall","acceptance criterion","compliance","tolerance","environmental condition","interface requirement","unless otherwise specified","reference standard","verification method"],
     ["write requirement statements with appropriate strength",
      "differentiate mandatory, advisory, and descriptive formulations",
      "refer to standards and conditions accurately",
      "support compliance-oriented reading and writing"],
     "Requirements language is one of the most sensitive areas of technical English because imprecision can have contractual, safety, or verification consequences. The learner must understand that descriptive prose and prescriptive prose are not interchangeable. A specification tells the reader what is required or permitted, under which conditions, and sometimes how compliance will be assessed.",
     """Three distinctions are especially important:\n\n- **Description vs requirement**: *The unit is fitted with a filter* is not the same as *The unit shall be fitted with a filter*.\n- **Requirement vs recommendation**: *should* is weaker than *shall* and may be unsuitable in a formal specification.\n- **Requirement vs verification**: *The system shall operate within the specified range* is different from *Compliance shall be verified through functional testing*.\n\nThe writer must control these distinctions consistently.""",
     ["shall, must, should, may and their documentary implications",
      "condition clauses and exceptions",
      "reference to standards and governing documents",
      "structured requirement statements and acceptance criteria"],
     "Analyse a short list of requirements and identify whether each statement is testable, ambiguous, or incomplete.",
     "Write ten requirement statements for a notional subsystem, ensuring that each statement is clear, testable, and limited to one main requirement.",
     "Explain orally why certain requirements are difficult to verify and how wording may be improved to support validation.",
     "Translate Italian specification statements into English and revise them to remove ambiguity, hidden assumptions, and weak modality.",
     ["requirement template","compliance-language guide","testable-requirements checklist"]),
    ("13-maintenance-english","Maintenance English",
     "develop the language required for maintenance planning, execution records, serviceability assessments, and support documentation",
     ["preventive maintenance","corrective maintenance","scheduled inspection","unscheduled intervention","serviceability","overhaul","replacement interval","maintenance record","consumable","spare"],
     ["describe maintenance activities, intervals, and findings clearly",
      "record actions performed and parts affected",
      "express serviceability judgments in an appropriately neutral tone",
      "write maintenance-oriented texts suitable for logs and procedures"],
     "Maintenance English must support planning, execution, and traceability. A maintenance note should indicate what was done, why it was done, which item was affected, and what the resulting condition is. Learners often focus on the action alone, but the maintenance record is stronger when it also captures context and outcome.",
     """Maintenance language is closely related to operational reality. Terms such as *preventive*, *corrective*, *serviceable*, *replacement interval*, and *inspection criteria* are not simply vocabulary items. They indicate how organisations manage reliability and supportability over time.""",
     ["past simple and passive voice in maintenance logs",
      "serviceability assessments and condition statements",
      "time and interval language",
      "concise action recording for traceability"],
     "Read a maintenance log extract and identify the trigger for the action, the task performed, the part involved, and the resulting status.",
     "Write a maintenance entry set for a notional unit covering routine inspection, part replacement, and return-to-service statement.",
     "Explain orally the difference between preventive and corrective maintenance, with examples drawn from a simple system.",
     "Translate an Italian maintenance note and revise it to improve terminology, traceability, and consistency of recorded actions.",
     ["maintenance-log example","serviceability note","scheduled-maintenance page"]),
    ("14-troubleshooting-and-fault-analysis","Troubleshooting and Fault Analysis",
     "teach the language of symptoms, diagnostic reasoning, fault isolation, temporary mitigation, and corrective action",
     ["fault","failure mode","symptom","root cause","fault isolation","diagnostic step","workaround","corrective action","recurrence","anomaly"],
     ["describe technical issues in a disciplined sequence",
      "distinguish observed symptom from inferred cause",
      "record diagnostic steps and outcomes clearly",
      "produce troubleshooting notes that support later reuse and escalation"],
     "Troubleshooting requires disciplined language because premature conclusions are common. A strong fault-analysis text separates what was observed from what was inferred. It also preserves the sequence of diagnostic actions so that another technician or engineer can follow the reasoning. The aim is not merely to say that a problem occurred, but to document how the problem was characterised, isolated, and addressed.",
     """A useful troubleshooting structure often includes:\n\n- initial symptom or reported issue;\n- operating conditions at the time of detection;\n- checks performed and their outcomes;\n- suspected and confirmed causes;\n- corrective action and follow-up recommendation.\n\nThis structure supports traceability and prevents overly narrative reporting.""",
     ["symptom vs cause language",
      "diagnostic sequencing and evidence-based inference",
      "reporting temporary mitigation and permanent correction",
      "careful use of appears, indicates, was traced to, could not be reproduced"],
     "Review a short fault report and classify each sentence as symptom, diagnostic action, finding, cause, or recommendation.",
     "Write a troubleshooting report for a notional fault affecting a communication or sensing subsystem. Include symptom, diagnostic sequence, root cause, and corrective action.",
     "Present orally a fault-analysis update during a technical review meeting, making clear what is known, what remains under investigation, and what action has been taken.",
     "Translate an Italian anomaly report into English and revise it to improve structure, evidence linkage, and technical neutrality.",
     ["troubleshooting-report model","fault-language phrasebank","root-cause analysis note"]),
    ("15-safety-risk-and-incident-communication","Safety, Risk and Incident Communication",
     "develop precise language for hazards, protective measures, incident reporting, and risk-related documentation",
     ["hazard","risk","exposure","mitigation","protective measure","unsafe condition","incident","near miss","warning","caution","consequence"],
     ["distinguish hazard, risk, consequence, and mitigation clearly",
      "write warnings and safety notes with appropriate strength",
      "report incidents factually and responsibly",
      "support safety culture through disciplined technical language"],
     "Safety communication must be precise, proportionate, and unambiguous. An unclear warning is not merely a language problem; it can create operational risk. For this reason, technical English in safety contexts uses a combination of controlled wording, explicit consequence language, and clear identification of required protective measures.",
     """A professional safety text should normally answer several practical questions:\n\n- What is the hazard?\n- Under what conditions does it arise?\n- What consequence may follow?\n- What protective measure is required or recommended?\n- What should the user avoid doing?\n\nThis structure helps the reader understand not only the instruction, but also the logic behind it.""",
     ["warning and caution language",
      "cause-consequence structures",
      "modal verbs for required protective actions",
      "incident-report phrasing and neutral factual style"],
     "Read a safety notice and identify hazard, condition, consequence, and protective measure. Then evaluate whether the warning is sufficiently explicit.",
     "Write a safety note and a short incident summary related to a technical activity involving inspection, power isolation, or access to moving parts.",
     "Explain orally how you would brief a team on a recurring safety issue while maintaining a calm and professional tone.",
     "Translate an Italian safety instruction into English and revise it to improve risk language and instructional precision.",
     ["safety-note page","incident-summary example","warning-vs-caution guide"]),
    ("16-defence-oriented-technical-english","Defence-Oriented Technical English",
     "introduce defence-related terminology in a neutral, documentary, and professionally controlled manner",
     ["platform","mission profile","payload","readiness","interoperability","supportability","deployment","surveillance","command and control","logistics","sustainment","availability"],
     ["recognise sector-specific terminology without losing documentary clarity",
      "compare defence-oriented and civil engineering phrasing",
      "maintain neutral professional tone in sensitive institutional contexts",
      "produce descriptive language suitable for documentation, training, or programme communication"],
     "Defence-oriented technical English often shares a large portion of its grammar and documentary logic with civil and industrial engineering English. The main difference lies in terminology, institutional context, and the type of systems being described. This module treats defence-related language as a professional communication domain and focuses on descriptive, documentary, and support-oriented uses of language rather than on tactical or operational instruction.",
     """Many terms have broader scope in defence contexts. For example:\n\n- *platform* may refer to a vehicle, vessel, aircraft, or integrated host system;\n- *payload* often refers to mission-related equipment carried by the platform;\n- *readiness* and *availability* concern operational and support condition;\n- *interoperability* refers to the ability of systems or organisations to function effectively together.\n\nThe learner should therefore pay attention to institutional usage, not just dictionary definitions.""",
     ["neutral professional register in institutional documentation",
      "difference between descriptive and operational wording",
      "comparison of civil, industrial, and defence-oriented terminology",
      "use of support, integration, and sustainment language"],
     "Read a descriptive text about a notional dual-use system and identify terminology that would sound unusual in a purely civilian industrial context. Explain why.",
     "Write a 300-word neutral overview of a platform-based system used in a defence or security-related environment, focusing on architecture, supportability, and documentation needs rather than sensitive operational detail.",
     "Present orally the difference between *mission profile*, *payload*, *availability*, and *supportability* to an audience familiar with civilian engineering language.",
     "Translate an Italian defence-sector descriptive paragraph into English and revise it to ensure neutral tone, terminological precision, and documentary appropriateness.",
     ["defence terminology note","civil-vs-defence comparison page","neutral-register example"]),
    ("17-procurement-and-programme-language","Procurement and Programme Language",
     "familiarise the learner with formal language used in procurement, programme coordination, deliverables, and document control",
     ["deliverable","milestone","revision status","statement of work","bidder","evaluation criterion","compliance matrix","interface control","baseline","stakeholder"],
     ["understand formal documentary language used in programme and procurement contexts",
      "write concise messages and notes related to deliverables, reviews, and revisions",
      "use document-control terminology accurately",
      "produce professionally toned texts for coordination and governance contexts"],
     "Engineering work does not take place only in laboratories or workshops. It also unfolds through programmes, contracts, reviews, and coordinated documentary exchanges. Procurement and programme language is therefore important even for learners whose main identity is technical rather than administrative. Many key project decisions depend on clear documentation of scope, deliverables, compliance, and revision status.",
     """Procurement language tends to prioritise formality, traceability, and explicit reference. Typical documentary elements include:\n\n- stated scope and applicable references;\n- deliverable identification;\n- milestones and review points;\n- responsibility allocation;\n- compliance statements;\n- revision and baseline control.\n\nA learner who understands this language can navigate programme documentation more effectively.""",
     ["formal coordination language",
      "document control and revision terminology",
      "milestone and deliverable phrasing",
      "careful distinction between scope, requirement, and offer"],
     "Read a short procurement or programme note and identify the terms that define scope, responsibility, deliverables, and status.",
     "Write a formal update on the status of a document package, including revision references, outstanding comments, and next milestone.",
     "Explain orally how document control supports engineering quality and why revision clarity matters in multi-stakeholder projects.",
     "Translate an Italian programme-management note into English and revise it to improve formality, structure, and term consistency.",
     ["programme-language guide","document-control note","deliverables status page"]),
    ("18-mkdocs-and-github-documentation-project","MkDocs and GitHub Documentation Project",
     "connect technical English production to structured documentation authoring, version control, and publication workflow",
     ["Markdown","navigation","repository","commit","branch","documentation site","information architecture","front matter","cross-linking","version history"],
     ["organise content into a coherent MkDocs structure",
      "apply documentation principles to headings, pages, and navigation",
      "understand the role of GitHub in versioned collaborative writing",
      "prepare a final site that demonstrates both language and documentary competence"],
     "The final value of technical language increases when it is organised, versioned, and made reusable. MkDocs and GitHub are included in this course because they provide a realistic framework for technical documentation work. Markdown encourages concise and structured writing. MkDocs encourages information architecture. GitHub supports version control and collaborative discipline. Together, they create a suitable environment for a course that aims to produce documentation rather than isolated exercises.",
     """A good documentation site is not a folder of unrelated pages. It should have:\n\n- a clear navigation structure;\n- stable naming conventions;\n- predictable page templates;\n- consistent terminology;\n- internal links that help the user move between theory, examples, templates, and outputs.\n\nIn this sense, the final project is an editorial task as well as a language task.""",
     ["heading hierarchy and page structure in Markdown",
      "navigation design for technical learning content",
      "version control concepts relevant to documentation authors",
      "revision workflow from draft to published page"],
     "Review the site structure and evaluate whether pages are organised in a way that supports study, revision, and later reuse.",
     "Create or revise one full module page, one glossary page, and one template page so that they are publication-ready and consistent with the rest of the site.",
     "Present orally how the repository is structured and how a learner or reviewer should navigate the site.",
     "Translate or adapt an existing Italian teaching note into a Markdown page that fits the site style and navigation logic.",
     ["documentation authoring guide","site-structure note","final project page set"]),
]

module_template = """
# Module {num} — {title}

## Module overview

{overview}

{detail}

## Learning objectives

By the end of this module, the learner should be able to:

{objectives}

## Why this module matters in professional practice

In engineering contexts, this topic is not merely academic. It supports actual work. A reader, reviewer, technician, engineer, or coordinator may rely on the language associated with this module to understand a situation, document a decision, reduce ambiguity, or verify whether a task has been completed correctly. For this reason, the learner is encouraged to approach the module not as isolated language study, but as preparation for credible professional communication.

## Key vocabulary

The following terms should be learned actively. Each one should ideally be recorded in a personal glossary with a concise definition, an example sentence, and a note on usage.

{vocab}

### Vocabulary development note

Vocabulary should not be memorised as isolated bilingual pairs. A more effective approach is to record terms with three layers of information:

1. **core meaning** — what the term refers to in a technical context;
2. **documentary use** — the kinds of texts in which the term commonly appears;
3. **phraseological pattern** — the collocations or structures that typically accompany the term.

For example, *interface* may appear in a system overview, a requirement statement, or an integration note, but its function changes depending on whether the text concerns design, installation, communication, or verification.

## Grammar and language focus

This module uses grammar to support technical meaning. The following areas deserve particular attention:

{language_focus}

### Model language patterns

Below are sample formulations that illustrate the expected register:

- The component is designed to provide...
- The subsystem receives input from...
- The procedure shall be completed before...
- No abnormal behaviour was observed during...
- The issue was traced to...
- Additional verification is recommended where...

The learner should adapt these patterns to the module topic and expand them through guided practice.

## Worked example

{example}

### Commentary on the example

When analysing examples, the learner should ask:

- Which information has been prioritised?
- Which terminology is repeated on purpose?
- Which structures make the sentence more precise?
- Which elements define scope, condition, or limitation?
- How could the sentence become weaker if simplified excessively?

This reflective analysis is one of the fastest ways to internalise professional technical style.

## Recommended reading task

{reading_task}

### Reading strategy

While reading, the learner should annotate the text actively. Useful annotation tags include:

- **purpose**
- **definition**
- **requirement**
- **warning**
- **observation**
- **result**
- **recommendation**
- **limitation**

This creates a bridge between comprehension and later writing.

## Recommended writing task

{writing_task}

### Writing guidance

A strong technical paragraph should usually contain:

1. a clear opening sentence stating topic or purpose;
2. logically ordered supporting sentences;
3. accurate terminology rather than generic wording;
4. explicit links between function, condition, and result where relevant;
5. a controlled conclusion or status statement.

The learner should revise the output at least once, with specific attention to ambiguity, overlong sentences, inconsistent terminology, and unnecessary conversational tone.

## Speaking task

{speaking_task}

### Oral performance guidance

In oral tasks, clarity should take priority over speed. The learner should aim for:

- concise signalling of structure;
- stable terminology;
- explicit transitions between points;
- limited but accurate explanation of technical relationships;
- appropriate professional tone.

A well-organised two-minute explanation is more valuable than a longer but poorly controlled performance.

## Translation focus

{translation_task}

### Contrastive note for Italian-speaking learners

Italian technical writing often tolerates longer sentences and more implicit links between ideas. English technical writing more often requires the writer to make relationships explicit through structure, sequencing, and repeated reference to the relevant item or function. During translation, learners should therefore not only convert words, but also re-organise information where necessary.

## Mini quality checklist

Before finalising the module output, verify the following:

- Is the terminology sufficiently precise?
- Are the sentences too long or difficult to parse?
- Is obligation expressed with the right modal verb?
- Is the tone professional and consistent?
- Could another reader understand the text without extra explanation?
- Is the text suitable for publication in a documentation site?

## Documentation output

This module should generate one or more of the following site elements:

{doc_outputs}

## Suggested extension activity

For additional practice, the learner may compare a civil/industrial example and a defence-oriented example related to the same broad topic. The objective is not to make the writing more dramatic or more confidential, but to observe how terminology, scope, and institutional tone may change while the underlying documentary logic remains similar.
"""

for idx, (slug,title,purpose,vocab,objectives,overview,example,language_focus,reading,writing,speaking,translation,outputs) in enumerate(module_data, start=1):
    num = f"{idx:02d}"
    content = module_template.format(
        num=num,
        title=title,
        overview=overview,
        detail=f"The purpose of this module is to {purpose}. The learner should gradually move from recognition to controlled production and finally to documentation-quality output.",
        objectives=md_list(objectives),
        vocab=md_list([f"**{t}** — term to be defined, contextualised, and reused in writing." for t in vocab]),
        language_focus=md_list(language_focus),
        example=example,
        reading_task=reading,
        writing_task=writing,
        speaking_task=speaking,
        translation_task=translation,
        doc_outputs=md_list(outputs),
    ).strip()+"\n"
    (docs/'modules'/f'{slug}.md').write_text(content, encoding='utf-8')

# language tools
language_tools = {
'grammar-reference.md': """
# Grammar Reference for Technical English

This reference does not aim to cover all English grammar. Its purpose is to highlight the structures most relevant to technical communication and to explain why they matter in professional engineering texts.

## 1. Present simple for facts, functions, and stable descriptions

The present simple is widely used to describe how a component or system works, what a document states, and what a process normally involves.

**Examples**

- The control unit receives input from three sensors.
- The enclosure provides environmental protection.
- The procedure includes a final verification step.

This tense is particularly useful for system overviews, component descriptions, and stable documentary statements.

## 2. Passive voice for process focus and documentary neutrality

The passive voice is common in technical English because the focus is often on the action, result, or item affected rather than on the person who performed the action.

**Examples**

- The unit was inspected before installation.
- The connector shall be protected during transport.
- The test was conducted under nominal operating conditions.

Use passive voice when the actor is unknown, irrelevant, or less important than the procedure or outcome. Avoid using it automatically in every sentence, as excessive passive voice can make a text heavy.

## 3. Modal verbs and degree of obligation

Technical English relies heavily on modal verbs. Their meaning must be controlled carefully.

### Shall
Used in specifications and requirements to indicate mandatory provisions.

- The system shall operate within the specified temperature range.

### Must
Used for strong obligation, often in instructions, safety statements, or policy contexts.

- Protective gloves must be worn during the procedure.

### Should
Used for recommendation, good practice, or non-mandatory preference.

- The wiring should be checked before the panel is closed.

### May
Used for permission, possibility, or authorised option.

- The cover may be removed for inspection purposes.

### Can
Used for capability or general possibility.

- The interface can support remote diagnostics.

## 4. Conditionals in technical logic

Conditionals are useful in procedures, fault analysis, and safety communication.

- If the measured value exceeds the limit, the test shall be repeated.
- If the fault persists, the unit should be removed from service.

The key issue is not grammatical complexity but clarity of operational consequence.

## 5. Relative clauses for definition

Relative clauses allow the writer to define an item without breaking the flow.

- The connector that links the sensor module to the control unit is located on the rear panel.
- The procedure, which is described in Appendix B, shall be followed in full.

## 6. Sequencing and procedural logic

Clear sequence markers reduce ambiguity.

- first
- then
- subsequently
- after verification
- prior to installation
- once completed
- in the event of failure

These markers are especially useful in workflow descriptions and maintenance tasks.

## 7. Quantification and limits

Technical writing often requires precise expression of values, ranges, tolerances, and limits.

- within the specified range
- not less than
- up to
- no greater than
- approximately
- nominal value

The learner should avoid vague alternatives such as *more or less* in formal technical texts.

## 8. Common grammar risks for technical writers

Frequent problems include:

- mixing present and past without a clear reason;
- using *should* where *shall* is required;
- overusing pronouns such as *it* without a clear reference;
- writing one sentence for too many actions or conditions;
- using conversational structures in formal documents.

The best remedy is revision with purpose in mind.
""",
'functional-language.md': """
# Functional Language for Engineering Communication

Functional language refers to the recurring expressions used to perform specific communicative tasks. In technical English, these tasks are highly stable. Engineers and technical personnel repeatedly need to describe function, state requirements, report findings, request clarification, explain limitations, and recommend actions.

## Describing function

Useful patterns include:

- is designed to...
- is intended to...
- provides...
- enables...
- supports...
- is responsible for...

**Example**  
The power distribution unit is designed to supply regulated power to the main subsystems.

## Describing structure and relationship

Useful patterns include:

- consists of...
- is composed of...
- is mounted on...
- is connected to...
- interfaces with...
- is housed within...

## Reporting observations

Useful patterns include:

- no abnormal behaviour was observed;
- the measured value exceeded the specified threshold;
- minor wear was detected on the contact surface;
- no evidence of leakage was found.

## Expressing requirements

Useful patterns include:

- shall be...
- shall not exceed...
- must be verified before...
- should be reviewed periodically.

## Expressing limitation and condition

Useful patterns include:

- under nominal operating conditions;
- within the specified range;
- subject to the following constraints;
- unless otherwise specified;
- provided that...

## Recommending action

Useful patterns include:

- additional verification is recommended;
- the unit should be removed from service;
- corrective action is required prior to release;
- further analysis may be necessary.

## Asking for clarification

Useful patterns include:

- please confirm whether...
- kindly clarify if...
- could you specify...
- please advise whether the following interpretation is correct...

These functions appear across many document types. The learner should therefore collect them systematically and reuse them in context.
""",
'linking-words-for-technical-writing.md': """
# Linking Words for Technical Writing

Linking words in technical writing are not decorative. They reveal structure, logic, cause, sequence, exception, and contrast. Good use of linking words helps the reader follow reasoning without unnecessary effort.

## Addition

- in addition
- furthermore
- also
- moreover

## Sequence

- first
- then
- subsequently
- finally
- prior to
- after completion of

## Cause and effect

- because
- therefore
- as a result
- consequently
- due to

## Contrast and limitation

- however
- although
- whereas
- by contrast
- nevertheless

## Condition

- if
- provided that
- unless
- in the event that

## Clarification and example

- for example
- in particular
- namely
- specifically

## Practical note

In technical writing, fewer but better chosen linking words usually work better than excessive variety. The priority is not stylistic elegance but logical transparency.
""",
'phrasebank-for-description.md': """
# Phrasebank for Description

## Describing components

- The component is mounted on the rear section of the assembly.
- The housing is made of corrosion-resistant aluminium alloy.
- The connector provides a temporary interface for diagnostic access.
- The bracket secures the module and maintains alignment during operation.

## Describing systems

- The system consists of four main subsystems.
- The sensing module provides real-time input to the processing unit.
- The communication subsystem transfers status data to the control interface.
- Power is distributed through a dedicated regulation stage.

## Describing function

- The primary function of the unit is to...
- The device is intended to...
- This mechanism enables...
- The assembly is responsible for...

## Describing condition and limitation

- Under nominal operating conditions, the unit...
- The device remains operational within the specified range.
- The following limitations shall be taken into account...
- Access is restricted when the unit is energised.
""",
'phrasebank-for-reporting.md': """
# Phrasebank for Reporting

## Reporting observations

- The test was conducted under nominal operating conditions.
- No abnormal behaviour was observed during the inspection.
- The measured value exceeded the specified limit.
- Minor surface wear was detected on the contact area.
- The observed deviation remained within the allowable tolerance band.

## Reporting diagnostic activity

- Initial checks were performed to verify power continuity.
- Further analysis focused on the communication interface.
- The issue could not be reproduced during the first verification cycle.
- Additional measurements were taken to confirm the initial finding.
- The fault was isolated by replacing the suspect module.

## Explaining findings

- The deviation appears to be associated with...
- Further analysis indicates that...
- The issue was traced to...
- Available evidence suggests that the malfunction originated in...
- The observed instability was consistent with intermittent signal loss.

## Recording outcomes

- Corrective action was implemented successfully.
- The unit was returned to serviceable condition.
- Additional monitoring is recommended.
- No further anomalies were observed after replacement of the affected component.
- A follow-up inspection is recommended after the next operating cycle.

## Stating limitations

- The result should be interpreted in light of the limited test duration.
- The current assessment does not include environmental stress conditions.
- The available data is sufficient for preliminary evaluation only.
- A definitive conclusion cannot be issued until full verification is completed.
""",
'phrasebank-for-meetings.md': """
# Phrasebank for Meetings

## Opening a technical point

- I would like to draw attention to the following issue.
- The main point for review is the interface between...
- Before moving on, it may be useful to clarify...

## Asking for clarification

- Could you confirm whether the latest revision includes...?
- Do we have agreement on the acceptance criteria?
- Can you clarify the basis for that assumption?

## Reporting status

- The activity is currently on schedule.
- The document has been updated and is under internal review.
- Two open points remain and are being addressed.

## Defining actions

- We will update the note accordingly.
- The systems team will provide the revised data set.
- This point should be closed after verification of...

## Closing a discussion item

- From a documentation perspective, the issue appears closed.
- Unless there are further comments, we can proceed to the next item.
- The remaining action is limited to confirmation of the final value.
""",
'phrasebank-for-safety.md': """
# Phrasebank for Safety

## Identifying hazards

- Exposure to moving parts may result in injury.
- Uncontrolled energisation presents a significant hazard.
- Contact with the heated surface may cause burns.

## Expressing protective measures

- Appropriate protective equipment must be worn.
- The power source shall be isolated before access is permitted.
- The area should be secured prior to maintenance activity.

## Stating consequences

- Failure to follow this instruction may result in equipment damage.
- Incorrect handling may lead to loss of containment.
- Non-compliance may compromise operator safety.

## Incident reporting

- The event occurred during routine inspection.
- No injuries were reported.
- The incident was contained and the area was made safe.
- Preliminary analysis indicates that...
""",
'phrasebank-for-email-writing.md': """
# Phrasebank for Email Writing

## Opening the message

- Please find attached the revised document for your review.
- I am writing to request clarification regarding...
- Following today's meeting, please see below a summary of the agreed actions.

## Requesting information or confirmation

- Could you please confirm whether...
- Kindly advise if the following interpretation is correct.
- Please let us know whether the attached revision is acceptable for release.

## Reporting status or issue

- During the latest review, we identified the following point.
- The document has been updated accordingly.
- One outstanding issue remains regarding...

## Closing professionally

- Your feedback would be appreciated.
- Please do not hesitate to contact me if further clarification is required.
- Thank you in advance for your support.
""",
'common-mistakes-for-italian-speakers.md': """
# Common Mistakes for Italian-Speaking Learners

## 1. Overusing generic words

Words such as *thing*, *part*, *piece*, or *problem* are often used where more precise terminology is required. In technical English, replacing generic language with specific nouns improves credibility and clarity.

## 2. Translating sentence structure too literally

Italian technical prose may tolerate longer periods and more implicit logical links. In English, readers usually benefit from shorter, more clearly segmented structures.

## 3. Confusing requirement strength

Italian speakers may use *should* when a real requirement is intended. In specifications, *shall* is often the more appropriate form.

## 4. Inconsistent terminology

Alternating between *system*, *device*, *unit*, and *equipment* without reason may confuse the reader. Choose the appropriate term and maintain it consistently.

## 5. Misusing false friends

Terms such as *eventually*, *actual*, *sensible*, and *fabric* can cause problems if interpreted through Italian.

## 6. Underusing explicit reference

English technical writing often repeats the relevant noun where Italian might use an implicit subject or a pronoun. This repetition may feel heavy to the learner but often improves clarity.
""",
'false-friends-in-technical-english.md': """
# False Friends in Technical English

## Actual
In English, *actual* means real or existing, not current.  
**Correct:** The actual measured value was lower than expected.

## Eventually
In English, *eventually* means in the end, not possibly.  
**Correct:** The system eventually returned to nominal performance.

## Sensible
In English, *sensible* means reasonable, not sensitive.  
**Correct:** A sensible mitigation strategy was adopted.

## Comprehensive
In English, *comprehensive* means complete or wide-ranging, not understandable.  
**Correct:** The report provides a comprehensive overview.

## Control
In technical contexts, *control* may refer to regulation or command, but not always to simple checking.  
**Correct:** The module controls power distribution.

Learners should maintain a dedicated page or personal list of problematic items and revisit them regularly.
"""
}
for fname, content in language_tools.items():
    (docs/'language-tools'/fname).write_text(textwrap.dedent(content).strip()+"\n", encoding='utf-8')

# glossaries

glossaries = {
'general-engineering-glossary.md': [("component","A discrete technical item that performs a function within an assembly or system.","The component shall be replaced if visible cracking is detected."),("assembly","A group of connected components that operate as a functional unit.","The assembly includes a mounting bracket, fasteners, and a protective cover."),("subsystem","A major part of a larger system with a defined role.","The communication subsystem transfers status data to the control station."),("interface","A point or mechanism of connection between systems, subsystems, or users.","The maintenance connector provides a temporary diagnostic interface."),("constraint","A design, operational, or environmental limit that must be respected.","Thermal dissipation is a key design constraint."),("reliability","The ability of an item to perform its required function over time.","Reliability improved after the connector redesign."),("verification","The process of confirming that a requirement has been met.","Verification shall be conducted before release."),("nominal","Referring to normal, expected, or declared operating condition.","The unit operated correctly under nominal load."),("deviation","A difference between observed and expected condition or value.","The deviation remained within the allowable range."),("serviceable","In acceptable condition for continued use.","The assembly was found to be serviceable after inspection."),("traceability","The ability to reconstruct the history, status, or use of an item or decision.","Clear revision control improves document traceability."),("mitigation","An action taken to reduce risk or consequence.","A shielding panel was added as a mitigation measure."),("baseline","An approved reference configuration or document version.","The drawing was compared against the current baseline."),("compliance","Conformity with a requirement, standard, or rule.","Compliance shall be demonstrated through testing."),("integration","The process of combining elements into a functioning whole.","System integration revealed a minor interface conflict.")],
'mechanical-terms.md': [("housing","The external body that contains or protects internal parts.","The housing is made of anodised aluminium."),("shaft","A rotating mechanical element used to transmit motion or torque.","The shaft showed signs of surface wear."),("bearing","A component that supports relative motion and reduces friction.","The bearing shall be lubricated at the specified interval."),("fastener","A device such as a bolt or screw used to join parts.","All fasteners shall be torqued according to the procedure."),("bracket","A support element used for mounting or alignment.","The bracket secures the sensor module to the frame."),("torque","The rotational force applied to a component.","Excessive torque may damage the thread."),("clearance","The designed gap between parts to allow movement or prevent interference.","Insufficient clearance caused contact during operation."),("fatigue","Progressive material damage due to repeated loading.","The crack pattern was consistent with fatigue."),("stiffness","Resistance to deformation under load.","Higher stiffness reduced misalignment under vibration."),("corrosion","Material degradation caused by chemical or environmental action.","Corrosion was observed near the lower fixing point.")],
'electrical-and-electronic-terms.md': [("power supply","A source or module providing electrical energy to a device.","The power supply remained stable during the test."),("voltage","Electrical potential difference.","The measured voltage exceeded the nominal value."),("current","Flow of electric charge.","Current draw increased during peak load."),("ground","Reference potential or protective electrical connection.","Ground continuity shall be verified before energisation."),("connector","A device used to establish an electrical or signal connection.","The connector was replaced due to contact damage."),("sensor","A device that detects a physical condition and generates a signal.","The sensor provides temperature feedback to the controller."),("actuator","A device that converts energy into motion or controlled action.","The actuator did not respond to the command signal."),("signal integrity","The quality and reliability of an electrical signal.","Routing changes improved signal integrity."),("short circuit","An unintended low-resistance path in an electrical circuit.","The unit was isolated following detection of a short circuit."),("insulation","Material or design preventing undesired electrical conduction.","Insulation damage was found near the cable entry point.")],
'systems-engineering-terms.md': [("architecture","The high-level structure and organisation of a system.","The architecture includes sensing, processing, and communication layers."),("requirement allocation","Assignment of system requirements to lower-level elements.","Requirement allocation was updated after the design review."),("stakeholder","A person or organisation with an interest in the system.","Stakeholder expectations influenced the interface design."),("verification method","The means by which compliance with a requirement is demonstrated.","Inspection was selected as the verification method."),("interface control","Management of boundaries and interactions between elements.","Interface control is critical during integration."),("redundancy","Duplication of functions or elements to improve reliability.","The architecture uses redundancy for critical signals."),("lifecycle","The sequence of stages from concept to disposal.","Lifecycle considerations affected maintainability requirements."),("configuration","The defined set of characteristics of a system or item.","Configuration changes shall be documented formally."),("dependency","A relationship in which one function or activity relies on another.","System startup depends on correct power sequencing."),("trade-off","A design choice balancing competing objectives.","A trade-off was required between weight and thermal protection.")],
'maintenance-terms.md': [("preventive maintenance","Planned action intended to reduce the likelihood of failure.","Preventive maintenance was completed at the scheduled interval."),("corrective maintenance","Action taken to restore an item after a fault or failure.","Corrective maintenance included replacement of the damaged seal."),("inspection","A planned examination to determine condition or compliance.","A visual inspection revealed minor contamination."),("overhaul","A major maintenance action involving detailed examination and restoration.","The pump underwent a complete overhaul."),("spare part","A replacement item kept available for maintenance use.","A spare part was installed to restore functionality."),("downtime","Period during which a system is unavailable for use.","Downtime was reduced through improved spare management."),("serviceability","Condition determining whether an item is fit for continued use.","The unit was declared fully serviceable."),("replacement interval","The specified time or usage after which an item should be replaced.","The filter replacement interval is six months."),("maintenance log","A record of performed maintenance actions.","All interventions shall be recorded in the maintenance log."),("wear limit","The maximum acceptable level of wear before action is required.","The measured wear exceeded the approved wear limit.")],
'safety-and-risk-terms.md': [("hazard","A source of potential harm.","The rotating assembly presents a hazard during inspection."),("risk","The combination of likelihood and consequence of harm.","Residual risk remains low after mitigation."),("mitigation","Action taken to reduce risk or consequence.","Lock-out procedures are a key mitigation measure."),("exposure","The condition of being subject to a hazard.","Exposure to heat should be minimised."),("protective equipment","Equipment used to reduce injury risk.","Protective equipment must be worn at all times."),("unsafe condition","A state of the environment or equipment that can cause harm.","The damaged guard created an unsafe condition."),("near miss","An event that could have caused harm but did not.","The near miss was reported for review."),("incident","An event involving actual or potential harm, damage, or disruption.","The incident occurred during routine servicing."),("warning","A statement indicating a serious hazard or required caution.","The warning label shall remain clearly visible."),("caution","A statement indicating a less severe but still important risk or risk of equipment damage.","A caution note was added to the procedure.")],
'compliance-and-standards-terms.md': [("standard","A formal reference defining requirements or accepted practices.","The design was reviewed against the applicable standard."),("applicable document","A document formally referenced as governing or supporting material.","All applicable documents shall be listed in the specification."),("acceptance criterion","A measurable condition used to determine acceptability.","The acceptance criterion is defined in Section 4."),("conformity","State of meeting a defined requirement.","Conformity was demonstrated through inspection."),("non-conformance","Failure to satisfy a requirement.","A non-conformance report was issued."),("waiver","Authorised acceptance of a departure from a requirement.","A waiver request was submitted for review."),("deviation permit","Formal approval to depart from an approved baseline or process.","The deviation permit is valid for this production batch only."),("audit trail","Documented history of actions and decisions.","The repository provides a clear audit trail."),("validation","Confirmation that the final product meets intended use.","Validation will follow laboratory verification."),("governing requirement","A requirement that has controlling authority over design or process.","The governing requirement is defined in the customer specification.")],
'defence-and-dual-use-terms.md': [("platform","The host vehicle, vessel, aircraft, or main system that carries equipment or performs a mission-related role.","The sensor payload is integrated on the host platform."),("payload","Mission-related equipment carried by a platform.","The payload includes observation and communication modules."),("readiness","State of preparedness for intended use or deployment.","Maintenance status directly affects readiness."),("availability","Degree to which a system is ready for use when required.","Availability improved after spare provisioning was revised."),("supportability","Ease and effectiveness of maintaining and supporting a system.","Supportability is a major lifecycle consideration."),("interoperability","Ability of systems or organisations to work together effectively.","Interoperability requirements drove interface standardisation."),("sustainment","Long-term support of a system throughout its service life.","Sustainment planning was addressed during programme review."),("surveillance","Systematic observation or monitoring activity.","The surveillance subsystem provides persistent area observation."),("command and control","Functions related to directing, coordinating, and managing resources or operations.","The communication link supports command and control functions."),("deployment","Movement or placement of resources for operational use.","Environmental protection is important during deployment.")],
'procurement-and-document-control-terms.md': [("deliverable","A defined item or document to be provided under a project or contract.","The updated interface note is a contract deliverable."),("milestone","A scheduled project point used to monitor progress.","The design review is the next programme milestone."),("statement of work","A document describing required tasks or scope.","The statement of work defines the documentation package."),("compliance matrix","A structured record showing how requirements are addressed.","The compliance matrix was updated after review."),("baseline","Approved reference version of a document or configuration.","All comments shall refer to the current baseline."),("revision status","The current issue or update level of a document.","Please confirm the revision status before circulation."),("redline comment","A marked-up document comment proposing changes.","Redline comments were incorporated into Revision B."),("approval authority","Person or role authorised to approve a document or decision.","Final release requires approval authority."),("distribution list","The set of recipients who must receive a document or message.","The distribution list was expanded to include the quality team."),("comment resolution","Process of addressing and closing review comments.","Comment resolution is in progress.")],
'useful-technical-verbs.md': [("withstand","To remain effective or intact under stress or adverse condition.","The enclosure shall withstand vibration during transport."),("monitor","To observe or measure over time.","The system monitors temperature continuously."),("regulate","To control within desired limits.","The module regulates output voltage."),("detect","To identify the presence of a condition or signal.","The sensor detects abnormal pressure increase."),("transmit","To send data, signal, or power from one point to another.","The interface transmits status information."),("isolate","To separate for protection, testing, or fault finding.","The faulty circuit was isolated for inspection."),("secure","To fasten or protect against movement or unauthorised change.","The unit shall be secured before transport."),("verify","To confirm that a condition or requirement has been met.","The installation shall be verified before use."),("degrade","To decline in performance or condition.","Performance may degrade under extreme heat."),("restore","To return to a previous functional condition.","Corrective action restored normal operation.")],
'technical-adjectives-and-descriptors.md': [("nominal","Corresponding to expected or declared normal condition.","Nominal current was recorded during the first test."),("serviceable","Fit for intended use.","The equipment remained serviceable after inspection."),("redundant","Provided in duplication to improve reliability or continuity.","A redundant channel is used for critical data."),("integrated","Combined into a unified system or arrangement.","The integrated module reduces cabling complexity."),("portable","Able to be moved and used easily in different locations.","The portable unit supports field maintenance."),("sealed","Closed in a way that protects against ingress or leakage.","The enclosure is sealed against dust ingress."),("degraded","Operating below nominal performance.","The system remained functional in a degraded mode."),("critical","Highly important to safety, function, or mission success.","This connector is critical to system availability."),("compliant","In conformity with a requirement or standard.","The design is compliant with the applicable reference."),("robust","Able to remain effective under demanding conditions.","The mounting solution is mechanically robust.")],
}
for fname, entries in glossaries.items():
    content = [f"# {fname.replace('-', ' ').replace('.md','').title()}\n", "This glossary page is intended for active study. Learners should not only memorise terms, but also observe how each term behaves in context, which documents commonly use it, and which nearby collocations reinforce its technical meaning.\n"]
    for term, definition, example in entries:
        content.append(f"## {term}\n")
        content.append(f"**Definition**  \n{definition}\n")
        content.append(f"**Example**  \n{example}\n")
        content.append("**Usage note**  \nWhere possible, reuse this term in system descriptions, reports, or glossary-linked module outputs so that terminology becomes active rather than passive.\n")
    (docs/'glossaries'/fname).write_text('\n'.join(content), encoding='utf-8')

exercise_pages = {
'reading-exercises.md': """
# Reading Exercises

## Purpose

These exercises train the learner to read technical texts strategically rather than passively. The objective is not to translate every word, but to identify document purpose, critical information, and documentary logic.

## Exercise 1 — Document purpose and audience

Read a short technical passage provided by the instructor or selected from the course materials. Then answer the following:

1. What type of document is this?
2. Who is expected to read it?
3. What practical action or decision does it support?
4. Which terms appear central to the text's purpose?

## Exercise 2 — Critical information extraction

From the same text, extract and organise:

- one requirement;
- one limitation or condition;
- one warning or note, if present;
- one key value, parameter, or performance statement;
- one sentence that summarises the main purpose of the document.

## Exercise 3 — Sentence improvement

Select one sentence that is grammatically correct but documentary weak. Rewrite it so that it is clearer, more explicit, or more professional.

## Instructor note

These tasks are especially effective when applied repeatedly to different genres: manuals, requirements, meeting notes, reports, and maintenance records.
""",
'vocabulary-exercises.md': """
# Vocabulary Exercises

## Exercise 1 — Term classification

Sort a list of technical terms into the following categories:

- components and structure;
- function and operation;
- performance and condition;
- documentation and compliance;
- maintenance and troubleshooting.

## Exercise 2 — Definition writing

Write concise definitions for ten terms. Each definition should be one sentence long and avoid circular wording.

## Exercise 3 — Collocation building

For each of the following nouns, write three suitable collocations:

- interface
- requirement
- maintenance
- fault
- verification

## Exercise 4 — Context sentence

Use each term in one sentence that sounds suitable for a professional technical document.

## Exercise 5 — Glossary refinement

Select five entries from your glossary and improve them by adding one usage note and one warning about a common mistake.
""",
'grammar-exercises.md': """
# Grammar Exercises

## Exercise 1 — Requirement strength

Rewrite the following statements using an appropriate modal verb:

- It is necessary to check the connector before installation.
- It is a good idea to review the cable routing regularly.
- It is permitted to remove the cover for inspection.
- The system is able to operate in standby mode.

## Exercise 2 — Passive transformation

Transform active procedural sentences into a more formal technical register when appropriate.

## Exercise 3 — Conditional logic

Complete the sentences using a suitable conditional structure:

- If the measured value exceeds the specified limit, ...
- If no fault is detected during the initial check, ...
- Unless otherwise specified, ...

## Exercise 4 — Relative clauses for definition

Join the sentences into more precise technical formulations using relative clauses.
""",
'technical-description-exercises.md': """
# Technical Description Exercises

## Task 1 — Component description

Write a description of a component including:

- name;
- location;
- material or protection;
- function;
- interface with surrounding elements.

## Task 2 — System overview

Describe a notional system with at least three subsystems. Include architecture, main functions, and key interfaces.

## Task 3 — Comparison task

Compare two configurations or two components. Focus on function, limitation, and expected application.

## Quality reminder

Avoid generic language such as *thing*, *part*, or *works well*. Use technical nouns and explicit function statements.
""",
'writing-exercises.md': """
# Writing Exercises

## Task 1 — Controlled paragraph

Write a 180–250 word paragraph on a technical topic using a clear topic sentence, stable terminology, and at least one condition statement.

## Task 2 — Revision task

Take a draft paragraph and improve it according to the following criteria:

- clarity;
- consistency;
- technical tone;
- sentence economy;
- documentary usefulness.

## Task 3 — Documentation adaptation

Transform a classroom answer into a Markdown-ready page section with heading hierarchy and improved readability.
""",
'email-writing-exercises.md': """
# Email Writing Exercises

## Task 1 — Request for clarification

Write an email asking for clarification on a document revision. Mention the exact section or issue and state the required response clearly.

## Task 2 — Status update

Write a concise technical status email summarising:

- what has been completed;
- what remains open;
- what action is expected from the recipient.

## Task 3 — Issue notification

Write an email reporting a minor issue identified during review or testing. Keep the tone factual and constructive.

## Review criteria

Check subject line quality, action clarity, and reference to documents or revisions.
""",
'report-writing-exercises.md': """
# Report Writing Exercises

## Task 1 — Executive summary

Prepare a summary of a notional test or technical review in no more than 180 words.

## Task 2 — Finding and recommendation

Write a short section containing:

- one observation;
- one finding;
- one recommendation;
- one residual limitation.

## Task 3 — Structured mini-report

Produce a one-page report using the following headings:

- Purpose
- Method
- Findings
- Conclusion
- Recommended action
""",
'maintenance-and-troubleshooting-exercises.md': """
# Maintenance and Troubleshooting Exercises

## Task 1 — Maintenance log entry

Write a log entry describing a routine inspection and the resulting status.

## Task 2 — Fault report

Prepare a short fault report including:

- symptom;
- operating condition;
- checks performed;
- root cause, if known;
- corrective action.

## Task 3 — Root cause discussion

Write a paragraph explaining why the observed symptom does not automatically prove the suspected cause.
""",
'safety-exercises.md': """
# Safety Exercises

## Task 1 — Warning and consequence

Write a warning statement that includes:

- the hazard;
- the condition of exposure;
- the possible consequence;
- the required protective measure.

## Task 2 — Incident summary

Draft a short incident summary in a neutral, factual style.

## Task 3 — Safety review

Revise a weak safety instruction so that it is more explicit and professionally credible.
""",
'translation-exercises.md': """
# Translation Exercises

## Objective

These tasks are designed to help Italian-speaking learners move from literal translation to professional technical English.

## Task 1 — Short paragraph translation

Translate a short Italian technical paragraph and then revise it to improve:

- terminology;
- sentence structure;
- explicit logic;
- professional tone.

## Task 2 — Requirement reformulation

Translate five Italian requirement statements and decide whether the best English form uses *shall*, *must*, *should*, or descriptive present simple.

## Task 3 — Commentary

After translating, add a short commentary explaining which choices were difficult and why.
""",
'oral-communication-tasks.md': """
# Oral Communication Tasks

## Task 1 — System briefing

Explain the architecture and purpose of a simple system in two to three minutes.

## Task 2 — Maintenance update

Report the outcome of a maintenance intervention to a supervisor or technical lead.

## Task 3 — Issue escalation

Present a fault or unresolved concern during a review meeting. Distinguish what is known from what remains uncertain.

## Performance criteria

The speaker should demonstrate:

- structure;
- terminology;
- clarity;
- professional tone;
- controlled pace.
"""
}
for fname, content in exercise_pages.items():
    (docs/'exercises'/fname).write_text(textwrap.dedent(content).strip()+"\n", encoding='utf-8')

templates = {
'technical-email-template.md': """
# Technical Email Template

## Purpose

This template supports concise, traceable communication in professional technical contexts.

## Recommended structure

**Subject:** Clear reference to topic, document, or action required

**Opening context**  
State why you are writing and what the message concerns.

**Main point**  
Describe the issue, update, request, or clarification in one focused paragraph.

**Action required**  
State clearly what the recipient is expected to do and, if relevant, by when.

**Attachments or references**  
Mention attached documents, revision identifiers, or meeting references.

**Closing**  
Use a professional, concise closing line.

## Example skeleton

Dear [Name],

Please find attached Revision B of the interface note for your review.

During final verification, we identified one outstanding point concerning the connector reference in Section 3.2. The current wording may be interpreted in two different ways and should therefore be clarified before release.

Could you please confirm the intended reference by [date], so that the document package can be finalised?

Thank you in advance for your support.

Best regards,  
[Name]
""",
'meeting-notes-template.md': """
# Meeting Notes Template

## Heading information

- Meeting title
- Date
- Participants
- Purpose

## Executive summary

Provide a brief overview of the meeting outcome in three to five lines.

## Main discussion points

Use numbered items or headings to record the main technical or documentary topics discussed.

## Decisions taken

Record only confirmed decisions, not assumptions or informal opinions.

## Action items

For each action, record:

- action description;
- owner;
- due date;
- related document or reference.

## Open points

List unresolved items requiring follow-up.
""",
'technical-report-template.md': """
# Technical Report Template

## 1. Purpose

State why the report has been written and what scope it covers.

## 2. Configuration or background

Describe the item, setup, or context relevant to the report.

## 3. Method or activity performed

Explain what was done, under which conditions, and with which references.

## 4. Findings

Report observations and measurements clearly. Distinguish fact from interpretation.

## 5. Conclusion

Summarise the main outcome and its significance.

## 6. Recommended action

State any corrective action, follow-up, or further verification required.
""",
'incident-report-template.md': """
# Incident Report Template

## 1. Incident identification

- date and time;
- location;
- affected item or activity.

## 2. Event description

Describe what happened in a factual and neutral way.

## 3. Immediate response

Record actions taken to secure the area, isolate the hazard, or restore control.

## 4. Consequences

State whether there was injury, damage, interruption, or only potential consequence.

## 5. Preliminary analysis

Provide initial observations without claiming a definitive cause unless confirmed.

## 6. Follow-up actions

Record recommendations, corrective actions, or further investigation needs.
""",
'maintenance-log-template.md': """
# Maintenance Log Template

## Required fields

- date;
- item identification;
- maintenance type;
- trigger or reason;
- actions performed;
- parts replaced, if any;
- resulting condition;
- technician or responsible role.

## Example format

**Date:**  
**Item:**  
**Maintenance type:**  
**Reason for action:**  
**Work performed:**  
**Resulting condition:**  
**Remarks:**
""",
'troubleshooting-report-template.md': """
# Troubleshooting Report Template

## 1. Initial symptom

Describe the issue as first observed or reported.

## 2. Operating conditions

State the context in which the issue occurred.

## 3. Diagnostic actions

List the checks performed in logical order.

## 4. Findings

Indicate what was discovered through testing or inspection.

## 5. Suspected or confirmed cause

Differentiate clearly between inference and confirmation.

## 6. Corrective action

Record the action taken to restore function or contain the issue.

## 7. Follow-up recommendation

State whether monitoring, re-test, or further investigation is required.
""",
'system-description-template.md': """
# System Description Template

## 1. Purpose

State what the system is intended to do.

## 2. Architecture overview

Identify the main subsystems and their roles.

## 3. Interfaces

Explain how the subsystems exchange data, power, or control signals.

## 4. Operational logic

Describe the sequence or principle of operation at a high level.

## 5. Constraints and limitations

Record any relevant environmental, interface, or performance limitations.
""",
'test-report-template.md': """
# Test Report Template

## 1. Objective

State what was to be verified.

## 2. Test configuration

Describe setup, items involved, and operating conditions.

## 3. Method

Summarise the procedure followed.

## 4. Results

Provide measured outcomes and observations.

## 5. Assessment

Compare results with expected values or acceptance criteria.

## 6. Conclusion and recommendation

State whether the objective was met and what follow-up is needed.
""",
'requirement-template.md': """
# Requirement Template

## Requirement identifier

Assign a unique identifier where appropriate.

## Requirement statement

Write one clear and testable requirement using controlled language.

**Example**  
The unit shall remain operational within the specified temperature range of -20°C to +50°C.

## Verification method

Indicate how compliance will be checked, for example by test, inspection, analysis, or demonstration.

## Rationale or note

Optional explanatory note if needed for learning or traceability.
""",
'briefing-template.md': """
# Briefing Template

## 1. Topic and purpose

Open by stating the subject and purpose of the briefing.

## 2. Background

Provide only the background needed to understand the point.

## 3. Main technical points

Present the system, issue, status, or proposal in logical order.

## 4. Risks, limitations, or open points

State what remains uncertain or constrained.

## 5. Requested decision or next action

Conclude with the action required from the audience.
"""
}
for fname, content in templates.items():
    (docs/'templates'/fname).write_text(textwrap.dedent(content).strip()+"\n", encoding='utf-8')

cvd = {
'terminology-comparison.md': """
# Terminology Comparison: Civil, Industrial, and Defence-Oriented Contexts

A large portion of technical English remains stable across sectors. Terms such as *interface*, *requirement*, *verification*, *maintenance*, and *performance* appear in civil, industrial, and defence-related documents alike. However, some sectors use additional terminology or different preferred framing.

## Examples of broad comparison

- **System** is common in all sectors, but defence contexts may more often use **platform**, **payload**, or **mission subsystem**.
- **Availability** exists in all domains, but in defence-oriented writing it may be closely linked to readiness and sustainment.
- **Supportability** is also found in industrial lifecycle discourse, yet it appears especially prominently in programme and defence-related documentation.

The objective for the learner is not to memorise separate languages, but to recognise how context influences preferred wording.
""",
'register-and-tone.md': """
# Register and Tone

Professional register in technical English should remain clear, neutral, and disciplined regardless of sector. In defence-oriented contexts, this often means even greater emphasis on institutional tone, traceability, and careful scope definition.

## Good practice

- prefer precise description over dramatic wording;
- avoid unnecessary confidentiality markers unless formally required;
- maintain documentary neutrality;
- distinguish clearly between capability description, support information, and operational use.

The course therefore promotes a stable professional tone rather than stylistic imitation of any particular organisation.
""",
'documentation-differences.md': """
# Documentation Differences

Civil and industrial documentation often prioritises usability, compliance, maintenance, and product support. Defence-oriented documentation may include additional concerns such as readiness, interoperability, sustainment, or institutional review processes. Nevertheless, the same documentary principles still apply:

- clarity;
- consistency;
- traceability;
- controlled requirement language;
- appropriate version control.

The learner should therefore focus on continuity first and difference second.
""",
'examples-of-neutral-professional-language.md': """
# Examples of Neutral Professional Language

## Less suitable

- This system is extremely advanced and highly effective.
- The platform performs excellently in all scenarios.

## More suitable

- The system is intended to provide...
- The platform supports the following functions under the specified operating conditions...
- Performance remains within the defined range during the evaluated configuration.

Neutral professional language supports credibility and reduces unsupported evaluation.
""",
'dual-use-technology-language.md': """
# Dual-Use Technology Language

Dual-use contexts often require language that is technically precise but institutionally careful. The same subsystem may be described in terms suitable for civil infrastructure monitoring, industrial inspection, or security-related integration. The learner should therefore favour descriptive formulations linked to architecture, function, supportability, interface logic, and documentation requirements.

A useful principle is this: describe what the system is, how it is structured, what it interfaces with, and what documentary constraints matter, without drifting into unnecessary operational sensitivity.
"""
}
for fname, content in cvd.items():
    (docs/'civil-vs-defence'/fname).write_text(textwrap.dedent(content).strip()+"\n", encoding='utf-8')

final_project = {
'project-overview.md': """
# Project Overview

The final project is a structured MkDocs site that demonstrates the learner's ability to organise technical English content in a professional and coherent way. The project is not a decorative website. It is a curated documentation repository showing that the learner can move from language exercise to documentation-grade output.

## Core objective

The learner must produce a site that shows:

- reliable technical English at B2 level;
- control of terminology and phraseology;
- coherent information architecture;
- documentary discipline in headings, cross-references, and page consistency;
- practical value for study, revision, or professional consultation.

## Minimum expected elements

The final site should include at least:

- a clear homepage and course or portfolio overview;
- a defined set of module pages or thematic pages;
- one or more glossary sections;
- at least three template pages;
- evidence of revised writing, not raw notes;
- logically structured navigation.

## Recommended philosophy

The best final projects are cumulative. Learners should revise and publish selected outputs progressively rather than waiting until the end. This approach improves both quality and confidence.
""",
'project-guidelines.md': """
# Project Guidelines

## 1. Define scope

Decide whether the final site will represent:

- the entire course;
- a selected thematic strand;
- a learner portfolio based on chosen outputs.

## 2. Apply a stable page model

Pages should be structured consistently. Use predictable heading levels and repeated section logic where appropriate.

## 3. Revise before publishing

Do not upload first drafts unchanged. Each page should be checked for:

- clarity;
- terminology;
- grammar;
- tone;
- consistency with related pages.

## 4. Use internal linking intelligently

When a term or concept appears repeatedly, consider linking to a glossary or related module page.

## 5. Maintain a coherent naming convention

File names should be stable, readable, and informative. Avoid inconsistent mixtures of styles.

## 6. Prefer documentary usefulness

A short, well-structured page is better than a long but diffuse page. The purpose is to create a usable technical learning resource.
""",
'student-portfolio.md': """
# Student Portfolio

The portfolio section may be used to highlight the learner's best revised outputs. This is especially useful when the site is intended to demonstrate progress or capability to an instructor, institution, or employer.

## Recommended portfolio items

- one system description;
- one technical email model;
- one report or summary;
- one troubleshooting or maintenance note;
- one safety-related text;
- one glossary subsection developed in a mature way.

## Portfolio note

Each portfolio item should ideally include a short note explaining:

- the communicative purpose of the text;
- the main language challenge addressed;
- the reason the item was selected.
""",
'evaluation-rubric.md': """
# Evaluation Rubric

## Criterion 1 — Language accuracy

- grammar is reliable;
- terminology is appropriate;
- sentence structure supports clarity.

## Criterion 2 — Technical credibility

- wording sounds plausible in engineering documentation;
- statements are sufficiently explicit;
- conclusions are proportionate to available evidence.

## Criterion 3 — Documentary structure

- headings are coherent;
- pages are well organised;
- navigation supports understanding and reuse.

## Criterion 4 — Consistency

- terminology remains stable across pages;
- tone is professional;
- formatting and style are controlled.

## Criterion 5 — Revision quality

- evidence of editing and improvement is visible;
- raw classroom language has been refined into publishable text.

## Suggested scale

A four-level scale may be used:

- Excellent
- Good
- Developing
- Needs substantial revision
""",
'revision-checklist.md': """
# Revision Checklist

Before considering a page complete, verify the following:

- Is the title specific and informative?
- Does the opening paragraph define the purpose clearly?
- Is the terminology consistent with the rest of the site?
- Are long sentences justified or should they be divided?
- Are requirements, observations, and recommendations clearly distinguished?
- Does the page provide value to a future reader?
- Is Markdown structure clear and readable?
- Are there useful internal links where appropriate?
""",
'publishing-guide.md': """
# Publishing Guide

## 1. Prepare the repository

Ensure that the folder structure is complete and that `mkdocs.yml` reflects the navigation logic of the site.

## 2. Review page readiness

Check for incomplete placeholders, inconsistent headings, or notes that should not appear in a published version.

## 3. Build locally

Run the local MkDocs preview and inspect page structure, navigation, and formatting.

## 4. Commit carefully

Use informative commit messages that reflect documentary changes, not only generic updates.

## 5. Publish

Publish the site through the chosen GitHub workflow and verify that links, navigation, and page rendering behave as expected.

## 6. Maintain

A documentation site remains useful only if it is maintained. Continue to refine terminology, examples, and internal structure as the course grows.
"""
}
for fname, content in final_project.items():
    (docs/'final-project'/fname).write_text(textwrap.dedent(content).strip()+"\n", encoding='utf-8')

readme = """
# Technical English for Engineering B2 — MkDocs Project

This repository contains a documentation-oriented course site for **Technical English for Engineering B2**, with emphasis on civil, industrial, dual-use, and defence-oriented professional communication.

## Contents

- structured MkDocs site;
- extended module pages;
- glossaries and phrasebanks;
- exercises and templates;
- final-project guidance.

## Local use

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open the local preview in your browser.

## Editorial principle

This project is intended to function as both a learning resource and a documentation model. Pages are therefore written in a controlled technical style and organised for reuse.
"""
(base/'README.md').write_text(textwrap.dedent(readme).strip()+"\n", encoding='utf-8')

print('Generation complete')
