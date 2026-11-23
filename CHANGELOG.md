# Changelog

All notable changes to NatSci-Writing-skills are documented here. The system follows semantic versioning.

## 1.2.2 — 2026-11-23

Perspective and theory-manuscript release, derived from the complete mirror-world hypothesis project, its design documents, final bilingual manuscript, audits, figure prompts and author conversation.

- Added references/nature-perspective-production.md and references/mirror-world-case-study.md (plus Chinese editions): Nature Perspective format, six-section architecture, full-paragraph rule, five-level evidence hierarchy, conceptual figure production, bilingual workflow, editing modes, three-discipline review, and a worked mirror-world case.
- Added templates: Perspective outline, editing scope/change log, conceptual-figure brief (17 templates per language).
- Added SKILL sections 3.3 (editing modes and author-text fidelity), 4.4 (Perspective production and theory manuscripts), 9.7 (conceptual figures), plus final gates for full paragraphs, 2–3 bold key sentences per subsection, one boundaries paragraph, references before periods, placeholder integrity and bilingual parity.
- Expanded the prose-style checker with exact Chinese/English constructions for "not X but Y", "not ... rather than", "并不……而是", "不……，而是".
- Captured project lessons: author Chinese is authoritative; light polish preserves claim order; tracked changes/yellow highlights on a copy; no caveat creep or noun stacking; mathematics must carry biological meaning; figures are one integrated argument; AI disclosure states the real scope.
- Updated README, docs, architecture, usage, coverage audit, versions, manifest and release package.

## 1.2.1 — 2026-11-23

Publication-system upgrade after syncing the published GitHub version and auditing latest sources.

- Added AI-use and writing-integrity policy: authorship ban, disclosure, permitted/prohibited uses, confidentiality, AI-tone control, journal policy table and audit.
- Added literature search and citation integrity: source hierarchy, search/screening record, synthesis, reference verification and management.
- Added five-pass proofreading and sentence polish: spelling/terms, grammar, inappropriate words, awkward expression, academic style; numbers/citations/markup.
- Added Perspective/insight writing and Nature section craft: intellectual centre, discovery sequence, abstract/Introduction/Results/Discussion moves and audits.
- Extended reviewer/response guidance with technical-concern taxonomy, severity, forensic consistency and package consistency; extended data/code/materials with mandatory deposition, FAIR, RRIDs and reporting guidelines.
- Added templates: AI disclosure, literature search plan, data/code/materials checklist (14 templates per language).
- Re-polished README (English and Chinese) in a direct human voice with bilingual one-line summaries, new capabilities, AI section and v1.2.1 notes; synchronized the author-published README.
- Integrated independent skills: insight-led-scientific-perspective, literature-review, grammar-checker, polish, writing-beats, plus current Nature/Science/ICMJE/COPE/Elsevier/Springer Nature AI policies and the latest nature-skills upstream (commit c6701db).
- Updated coverage audit, docs, versions, manifest and release package.
- README.md and README.zh-CN.md fully rewritten in natural language following the skill's own rules: human voice, concrete claims, no translationese or AI-tone, and a one-line Chinese summary after each key point.
- Hardened the style ban: template contrast, defensive/self-limiting phrases, AI vocabulary and structural tells are now zero-tolerance. Expanded English/Chinese diagnostics with pattern tables, rewrites and sources; added tools/check_prose_style.py and a CI check; fixed all README hits.

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
