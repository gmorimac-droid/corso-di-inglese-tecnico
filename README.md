# Technical English for Engineering B2 — MkDocs Repository

This repository contains a full MkDocs-based course on Technical English at B2 level, with a professional engineering orientation spanning civil, industrial, dual-use, and defence-related documentation contexts.

## Repository character

The project is designed to function on three levels at once:

1. **course** — a structured instructional programme;
2. **documentation system** — a reusable technical knowledge base;
3. **publication scaffold** — a GitHub-ready MkDocs site.

## What is included

- 18 main instructional modules;
- multi-layer glossaries;
- language-tool pages and phrasebanks;
- exercise sets;
- templates and models;
- model answers;
- teacher notes;
- review playbooks;
- quality-assurance guidance;
- appendices for document-control and editorial consistency;
- final-project guidance for publication workflow.

## V5 focus

Version 5 is editorially refined. The emphasis is on repository maturity, not only content volume. This version adds:

- section landing pages for improved navigation;
- a quality-assurance layer;
- appendices for repository governance;
- improved MkDocs Material configuration;
- custom stylesheet support;
- more explicit editorial control over page behaviour.

## Quick start

```bash
pip install -r requirements.txt
mkdocs serve
```

## Build for publication

```bash
mkdocs build
```

## Suggested GitHub workflow

1. create a repository on GitHub;
2. push the project;
3. enable GitHub Pages or deploy through your preferred MkDocs pipeline;
4. maintain revisions through pull requests and review cycles;
5. use the release and quality pages as repository-governance tools.

## Recommended first reading path

- `docs/index.md`
- `docs/release-notes-v5.md`
- `docs/modules/index.md`
- `docs/quality-assurance/index.md`
- `docs/final-project/project-overview.md`

## Maintenance note

This repository is intentionally written as a high-density instructional and documentation environment. Contributors should review the editorial guidance before changing terminology, page architecture, or template logic.
