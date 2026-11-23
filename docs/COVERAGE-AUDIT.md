# Coverage audit: what is integrated and what is not

Version 1.2.0; updated 2026-11-23. Package 1.2.0 adds author, citation and license metadata; coverage is unchanged. This document answers whether the earlier writing and figure requirements, the latest nature-skills content, and Nature/Science publication-level requirements are organically integrated into NatSci-Writing-skills.

## 1. Audit scope

Sources compared:

1. Author standards — v2.1.0 manuscript/figure rules, project figure geometry, colour audit, Baker structural standard, SEAL supplementary-figure standard, R50 checklist, HTML/data verification.
2. nature-skills upstream — local clone plus upstream main at commit c6701db (2026-11-22), covering nature-writing, nature-figure, nature-polishing, nature-statistics, nature-data, nature-reviewer, nature-response, nature-citation, nature-academic-search, nature-shared and related modules.
3. Nature/Science official requirements — article types, editorial criteria, word/display/reference limits, statistical reporting, reporting summary, data/code/materials statements, figure production contracts, image integrity.
4. NatSci corpus — 868 Nature/Science records, 317 full texts, 1,504 parsed figure captions.

## 2. Coverage matrix

| Requirement layer | What "complete" means | Where it is covered now | Status |
|---|---|---|---|
| Academic argument and genre | Question, claim, evidence chain, competing explanations, genre architecture | SKILL.md sections 2–4; manuscript-production.md; section playbooks; research-and-language.md | integrated |
| Innovation and creativity | Contribution type, contribution ladder, gap engineering, discriminating predictions, positioning | innovation-and-broad-interest.md (new); SKILL.md 2.4; innovation-canvas template | strengthened in 1.1.0 |
| Broad audience and editorial fit | Editorial criteria, why-this/why-now/why-broad, significance, journal fit | editorial-and-submission.md (new); SKILL.md 2.4; editorial-audit template | strengthened in 1.1.0 |
| Language and academic taste | Rhythm, voice, restraint, house style, AI-tone, phrasebank | language-and-taste.md (new); writing-diagnostics.md; revision-and-response.md; corpus evidence | strengthened in 1.1.0 |
| Figures and visual quality | Figure-level claim, inferential roles, visual hierarchy, journal specs, schematics, QA | figure-craft-and-information-density.md (new); figure-production.md; figure-standards; project overlay; Python/R starters | strengthened in 1.1.0 |
| Information density | Result classification, main-text/SI split, display budgets, revision accretion, claim repetition | main-text-and-information-architecture.md (new); SKILL.md 4.1; figure-evidence-map template | strengthened in 1.1.0 |
| Statistics and integrity | Independent unit, replication, exact reporting, figure stats, Reporting Summary, image/data/code integrity | statistics-and-reporting-integrity.md (new); SKILL.md 5.1; reporting checklist template | strengthened in 1.1.0 |
| Submission and editorial process | Stage gate, limits, cover letter, title page, declarations, reviewer suggestions, readiness | editorial-and-submission.md; manuscript-production.md sections 7–10; cover-letter template | strengthened in 1.1.0 |
| Literature, citation and data | Search strategy, verification, citation formats, data/code/materials statements | SKILL.md sections 6–7; manuscript-production.md; html-and-data-verification.md; statement templates | integrated |
| Bilingual and Chinese-specific | Native Chinese guidance, translationese, evidence-strength alignment | natsci-writing-zh SKILL.md; Chinese references and templates | integrated |
| Production and QA | Complete draft, figure files, formatting, response, validator, installer, manifest, CI | SKILL.md sections 7–11; assets; tools; docs; GitHub workflow | integrated |

## 3. Latest nature-skills delta: what was integrated

- nature-writing: initial submission package (cover letter, title page, highlights, declarations, reviewer suggestions, stage-aware limits); Nature-family and NMI journal fragments; main-text discipline; Nature abstract/introduction/results-discussion corpus guidance; revised workflow emphasis on deletion checks and scoped alignment.
- nature-statistics (new upstream skill): independent unit and replication, Nature Article statistical requirements, reporting summary gate, figure statistics, common failure modes, P0/P1/P2 reviewer-risk labels.
- nature-figure: multipanel evidence architecture, flagship Nature figure requirements, vector schematic style rules, template catalogue, updated design/QA guidance.
- nature-data: flagship Nature data/code/materials requirements and mandatory deposition gate.
- nature-polishing: updated section moves, phrasebank, failure modes and Nature/NMI style fragments.
- nature-reviewer / nature-response: technical-concern taxonomy, severity tiering, package-consistency audit, response structure and tone updates — folded into review, response and editorial audit rather than duplicated as separate skills.
- nature-shared: reader workflow, terminology ledger, paper-type taxonomy, ethics, consistency sweep, journal formats.

## 4. Deliberately out of scope

The upstream repository also contains field- or workflow-specific modules that are not core to a Nature/Science manuscript production system: social-science writing, paper-to-patent, paper-to-PPT, paper reader, paper cards, paper translation, paper x-ray, reference verifier, literature pipeline, experiment log, image-to-PPT, proposal writer, downloader and medical skills. They are not integrated because they would dilute the writing/figure production focus; users who need them can install the upstream skills separately.

## 5. Known limits

- Journal limits and production rules change; every number is marked "verify at submission" and must be checked against the current guide.
- Project-specific SEAL content is included and should be reviewed before public release (see PUBLISHING.md section 6).
- The package does not compute new statistics or generate figures from raw data automatically; it produces the analysis plan, reporting checks, figure code and manuscript text, and requires author data and decisions.
- The corpus is a local analysis set; aggregate statistics are documented, but full texts are not redistributed.
- Passing these checks does not guarantee acceptance; it reduces avoidable editorial, statistical, stylistic and production risk.

## 6. Verification performed for 1.1.0

- Validator passes for the package and for installed copies.
- YAML frontmatter and companion links valid.
- All references named in SKILL.md exist; no broken relative links.
- No absolute paths, personal data, secrets or stale private names.
- Python and R figure starters run on demo data and export SVG/PDF/600-dpi raster.
- Installer copies both skills; zip extraction passes validation.
- Manifest is current; version 1.1.0.

## 7. Conclusion

The package now covers the full publication stack: argument and innovation, broad-audience editorial fit, language and taste, figure quality and information density, statistics and integrity, submission and editorial process, bilingual production, and QA. Remaining gaps are explicit limits, not missing core layers.
