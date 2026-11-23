# Changelog

All notable changes to NatSci-Writing-skills are documented here. The system follows semantic versioning.

## 1.2.0 — 2026-11-23

Authorship, provenance, citation and license update.

- Author credited as **Chuanyang Liu**. Provenance now states that the system was built from the author's own research projects and long-term conversations with AI coding agents.
- Third-party credit made explicit: integrates and adapts **Nature-skills** by **Yuan Yizhe (袁一哲)**, https://github.com/Yuan1z0825/nature-skills, Apache-2.0; adapted portions retain Apache-2.0 terms.
- Added AUTHORS.md and CITATION.cff. Related paper is in preparation and will be updated; users are asked to cite the paper (when published) and the repository.
- License changed to the NatSci-Writing-skills Non-Commercial License: free to copy, modify and redistribute for non-commercial academic/research/teaching use with attribution; commercial or profit-generating use requires a separate written license. Apache-2.0 portions remain under Apache-2.0 (LICENSES/Apache-2.0.txt).
- README integrated the author-edited version, with bilingual one-line summaries and new author/origin/license/citation sections.
- Skill content is unchanged; versions bumped to 1.2.0 for package consistency.

## 1.1.0 — 2026-11-23

Publication-level coverage upgrade after a full audit against author standards, the latest nature-skills upstream (commit c6701db, 2026-11-22) and Nature/Science requirements.

- New references: editorial-and-submission.md, innovation-and-broad-interest.md, main-text-and-information-architecture.md, statistics-and-reporting-integrity.md, language-and-taste.md, figure-craft-and-information-density.md, plus Chinese editions.
- New templates: cover letter/submission package, innovation canvas, editorial audit, reporting/statistics checklist, figure evidence map.
- SKILL.md now integrates innovation and broad interest, editorial fit, main-text discipline, statistics/reporting integrity, figure evidence architecture, submission package and editorial audit, with expanded final gates.
- Integrated latest nature-skills content: initial submission package and journal fragments; main-text discipline and Nature abstract/introduction/results-discussion guidance; nature-statistics requirements and failure modes; multipanel evidence architecture, Nature figure requirements and vector-schematic rules; Nature data/code/materials requirements; reviewer/response and polishing updates.
- Added bilingual coverage audit (docs/COVERAGE-AUDIT.md and .zh-CN.md), documenting what is integrated, deliberately out of scope and remaining limits.
- Validator now reads VERSION dynamically; docs and manifest updated.
- README rewritten in a direct, human voice with a one-line Chinese summary after each key point and heading, so the core capabilities are visible at a glance.

## 1.0.0 — 2026-11-23

Initial public release of NatSci-Writing-skills.

- Two self-contained skills: natsci-writing (English) and natsci-writing-zh (Chinese), each with SKILL.md, references, templates and tested figure starter code.
- Complete-manuscript production: deliverable modes, confirmation gate, terminology ledger, section playbooks, paper-type playbooks, journal formats, manuscript package, statements and adversarial self-review.
- Figure production: figure contract, archetypes, Python/R backend gate, design system, chart selection, statistics, caption grammar, export and QA, plus the author project figure standards (geometry, gutters, colour audit, structural-figure standard, SEAL per-panel delivery, R50 checklist).
- Revision, formatting and response: reasoning-first polishing, phrasebank, style guardrails, journal-format conversion, point-by-point reviewer response and pre-submission reviewer simulation.
- Corpus-evidence layer: 868 Nature/Science records, 317 full texts, 1,504 parsed figure captions, measured style and caption statistics.
- Package infrastructure: bilingual READMEs, architecture/usage/migration/publishing docs, validator, installer, manifest builder, CI workflow and release checklist.
- License: Apache-2.0, with attribution to adapted open-source nature-skills material in NOTICE.md.
