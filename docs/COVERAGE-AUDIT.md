# Coverage audit: what is integrated and what is not

Version 1.2.8.3; updated 2026-11-27. This document answers whether the author's earlier writing/figure requirements, the latest nature-skills content, current journal AI policies and independent writing skills are organically integrated into NatSci-Writing-skills.

## 1. Audit scope

1. Author standards: v2.1.0 manuscript/figure rules, project figure geometry, colour audit, Baker structural standard, SEAL supplementary-figure standard, R50 checklist, HTML/data verification.
2. Published repository: the published GitHub working copy at v1.2.0; its README was synchronized as the base and re-polished for 1.2.1; the 1.2.2 release adds the mirror-world Perspective project lessons.
3. nature-skills upstream: latest main at commit c6701db (2026-11-22); modules audited: nature-writing, nature-figure, nature-polishing, nature-statistics, nature-data, nature-reviewer, nature-response, nature-shared, nature-academic-search, nature-citation.
4. Independent skills: insight-led-scientific-perspective, literature-review, grammar-checker, polish, writing-beats, nature-reader.
5. Journal AI policies: Nature Portfolio, Science/AAAS, ICMJE, COPE, Elsevier, Springer Nature (positions as of November 2026; verify current policy at submission).
6. NatSci corpus: 868 Nature/Science records, 317 full texts, 1,504 parsed figure captions.
7. Mirror-world project: design.md/design-ref1–4, final bilingual Perspective, revision/audit records, figure prompts, full author conversation and prior writing-skill evaluations. The reusable lessons are in nature-perspective-production.md and mirror-world-case-study.md.
8. AI writing and image policy sources: Nature Portfolio, Nature Methods (2026), Nature Materials (2026), Nature Geoscience, Science/AAAS cover-image policy, Elsevier (June 2026), Cell Press, Springer Nature, PLOS, ICMJE (2026), COPE, and the 2026 arXiv survey on AI-generated figures. The consolidated rules are in ai-use-and-writing-integrity.md and ai-figures-and-visual-integrity.md.
7. AI style sources: Wikipedia Signs of AI writing; AI Smells field guide; Chinese zh-cues; Editage AIGC style words; CASS AI-tone analysis. The consolidated zero-tolerance tables are in writing-diagnostics section 3A.

## 2. Coverage matrix

| Requirement layer | Where it is covered now | Status |
|---|---|---|
| Academic argument and genre | SKILL.md sections 2–5; manuscript-production; nature-section-craft; research-and-language | integrated |
| Innovation and creativity | innovation-and-broad-interest; SKILL 2.4; innovation canvas | integrated |
| Broad audience and editorial fit | editorial-and-submission; SKILL 2.4; editorial audit | integrated |
| Language and academic taste | language-and-taste; writing-diagnostics; proofreading-and-polish | strengthened in 1.2.1 |
| Perspective production | nature-perspective-production; mirror-world-case-study; SKILL 4.4; Perspective outline | new in 1.2.2 |
| Editing fidelity | SKILL 3.3; editing-scope-and-change-log; case study | new in 1.2.2 |
| Conceptual figures and theory packaging | nature-perspective-production §7; conceptual-figure-brief; SKILL 9.7 | new in 1.2.2 |
| Project-derived lessons | mirror-world-case-study; production §12; writing-diagnostics 3A | new in 1.2.2 |
| AI writing negative list | ai-use-and-writing-integrity §10–15; SKILL 3.1/10/11; ai-negative-checklist | new in 1.2.5 |
| AI figure policy and provenance | ai-figures-and-visual-integrity; SKILL 9.0; ai-image-provenance-record | new in 1.2.5 |
| AI image copyright and reproducibility | ai-figures-and-visual-integrity §6/§9; figure refs | new in 1.2.5 |
| Perspective and conceptual writing | perspective-and-insight; SKILL 4.3; manuscript-production | strengthened in 1.2.1 |
| Nature section craft | nature-section-craft; SKILL 4.2; journal-style-evidence | strengthened in 1.2.1 |
| Figures and visual quality | figure-craft-and-information-density; figure-production; figure-standards; project overlay | integrated |
| Information density and main-text discipline | main-text-and-information-architecture; SKILL 4.1; figure evidence map | integrated |
| Statistics and integrity | statistics-and-reporting-integrity; Reporting Summary; image integrity | integrated |
| Literature search and citation | literature-search-and-citation; SKILL 6.1; literature-search-plan template | strengthened in 1.2.1 |
| AI use and disclosure | ai-use-and-writing-integrity; SKILL 3.1; ai-disclosure template | new in 1.2.1 |
| Style integrity | writing-diagnostics 3A; SKILL 3.0; tools/check_prose_style.py | hardened in 1.2.1 |
| Structural AI tells and metrics | writing-diagnostics 4A; check_prose_style --metrics/--gate/--genre | new in 1.2.7.0 |
| Defensive writing and argument selection | defensive-writing-and-argument-selection; SKILL 17; check_prose_style --gate | new in 1.2.7.0 |
| Journal templates and assembly | journal-templates-and-assembly; SKILL 18; specs, generated/official templates, builder and checker | new in 1.2.8.0 |
| Results heading language | results-heading-language; SKILL 19; heading audit | new in 1.2.8.1 |
| Results as a discovery narrative | results-architecture; SKILL 20; paragraph contract | new in 1.2.8.2 |
| Proofreading and polish | proofreading-and-polish; SKILL 3.2; grammar-checker/polish integration | strengthened in 1.2.1 |
| Reviewer response and peer review | revision-and-response (extended with taxonomy/severity/forensic consistency); manuscript-production | strengthened in 1.2.1 |
| Data, code and materials | statistics-and-reporting-integrity (extended deposition/FAIR/RRID); data/code/materials template | strengthened in 1.2.1 |
| Submission and editorial process | editorial-and-submission; manuscript-production; cover letter/submission template | integrated |
| Bilingual and Chinese-specific | natsci-writing-zh SKILL and references | integrated |
| Production and QA | tools, docs, examples, CI, manifest, zip | integrated |

## 3. nature-skills module mapping

| Upstream module | Integrated into | Status |
|---|---|---|
| nature-writing | manuscript-production; nature-section-craft; editorial-and-submission; journal formats | integrated |
| nature-figure | figure-production; figure-craft-and-information-density; figure standards; project overlay | integrated (rules; upstream audit scripts not shipped) |
| nature-polishing | language-and-taste; proofreading-and-polish; revision-and-response | integrated |
| nature-statistics | statistics-and-reporting-integrity; reporting template | integrated |
| nature-data | statistics-and-reporting-integrity (data/code/materials section); data statement template | integrated |
| nature-reviewer | revision-and-response (reviewer-side audit; taxonomy/severity); editorial audit | integrated |
| nature-response | revision-and-response; response-letter template; package consistency | integrated |
| nature-shared | manuscript-production; nature-section-craft; terminology ledger; main-text discipline | integrated |
| nature-academic-search | literature-search-and-citation; literature search plan | integrated |
| nature-citation | literature-search-and-citation; reference verification/management | integrated |
| nature-statistics reporting summary | statistics-and-reporting-integrity | integrated |
| Peripheral modules (patent, PPT, reader, paper cards, translation, x-ray, reference verifier, literature pipeline, experiment log, image-to-PPT, proposal writer, downloader, medical) | not integrated by design | out of scope |

## 4. Independent-skill mapping

| Skill | Useful content | Integrated into |
|---|---|---|
| insight-led-scientific-perspective | intellectual centre, discovery sequence, accountability, formal content | perspective-and-insight |
| literature-review | systematic search, PRISMA-style screening, extraction, quality assessment, synthesis | literature-search-and-citation |
| grammar-checker | five-pass proofreading and issue log | proofreading-and-polish |
| polish | sentence-level clarity/voice/tense/acronym/concision rules | proofreading-and-polish; language-and-taste |
| writing-beats | grounding concepts, paragraph rhythm, ending on a beat | proofreading-and-polish; language-and-taste |
| nature-reader | source-grounded reading and anchor discipline | literature-search-and-citation (reading/verification) |

## 5. AI policy sources

Nature Portfolio, Science/AAAS, ICMJE, COPE, Elsevier and Springer Nature positions were compared. Common ground: AI cannot be an author; authors remain responsible; substantive use must be disclosed where required; confidential manuscripts and review material must not be uploaded to public models; AI-generated research images are not acceptable as data. Details and disclosure templates are in ai-use-and-writing-integrity.md. Policies change; verify the target journal at submission.

## 6. Deliberately out of scope

Field- or workflow-specific upstream modules (patent drafting, PPT generation, paper reader/cards, translation, paper x-ray, reference verifier, literature pipeline, experiment log, image-to-PPT, proposal writer, downloader, medical skills) are not integrated; they are not core to a Nature/Science manuscript production system. Install them separately if needed.

## 7. Known limits

- Journal limits, figure specifications, reporting rules and AI policies change; every number is marked "verify at submission".
- The package does not compute new statistics or generate figures from raw data automatically; it produces analysis plans, reporting checks, figure code and manuscript text, and requires author data and decisions.
- Upstream figure audit scripts (Python/R) are not shipped; their rules are integrated and the project file templates provide the checklist.
- The corpus is a local analysis set; aggregate statistics are documented, full texts are not redistributed.
- Passing these checks does not guarantee acceptance; it reduces avoidable editorial, statistical, stylistic, integrity and production risk.

## 8. Verification performed for 1.2.5

- Package and installed-copy validator pass.
- YAML frontmatter, author metadata, companion links valid.
- All references named in SKILL.md exist; no broken relative links.
- No absolute paths, personal data, secrets or stale private names.
- Python and R figure starters run and export SVG/PDF/600-dpi raster.
- Installer copies both skills; zip extraction passes validation.
- Manifest current; version 1.2.5.

## 9. Conclusion

The package now covers the full publication stack: argument and innovation, broad-audience editorial fit, language and taste, Perspective and section craft, figure quality and information density, statistics and integrity, literature/citation, AI-use integrity, proofreading, reviewer response, data/code/materials, submission and QA. Remaining gaps are explicit limits, not missing core layers.
