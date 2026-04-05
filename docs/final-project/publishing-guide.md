# Publishing Guide

## Purpose

This page explains how to turn the final project into a publishable MkDocs site managed through GitHub.

The focus is on a workflow that is:
- clear;
- reliable;
- easy to maintain;
- suitable for an educational technical documentation repository.

## At a Glance

Before publishing, make sure the project is:

- complete enough to be credible;
- readable in local preview;
- structured correctly under `docs/`;
- configured properly in `mkdocs.yml`;
- ready for version control and release through GitHub.

## Recommended Repository Structure

A typical repository should contain at least:

```text
project-root/
├── docs/
│   ├── index.md
│   ├── modules/
│   ├── glossaries/
│   ├── language-tools/
│   ├── exercises/
│   ├── templates/
│   └── final-project/
├── mkdocs.yml
├── README.md
├── requirements.txt
└── .gitignore