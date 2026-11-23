# NatSci-Writing-skills v1.0.0

Initial public release.

## Highlights

- Two self-contained skills: natsci-writing (English) and natsci-writing-zh (Chinese).
- Complete-manuscript production: modes, confirmation gate, terminology ledger, section and paper-type playbooks, journal formats, submission package, statements, adversarial self-review.
- Figure production: figure contract, archetypes, Python/R backend gate, design system, chart selection, statistics, caption grammar, export and QA; project figure standards including geometry, gutters, colour audit, structural-figure (Baker) standard, SEAL per-panel delivery and R50 checklist.
- Revision, formatting and reviewer response: reasoning-first polishing, phrasebank, style guardrails, journal-format conversion, point-by-point response and pre-submission review.
- Corpus evidence: 868 Nature/Science records, 317 full texts, 1,504 parsed figure captions; measured style and caption targets.
- Package infrastructure: bilingual documentation, architecture/usage/migration/publishing guides, template assets, tested Python/R figure starters, validator, installer, manifest and CI.

## Installation

~~~bash
python tools/install.py --target ~/.agents/skills --skills both
python tools/validate_package.py --installed ~/.agents/skills
~~~

## Compatibility

- Agents that load SKILL.md plus relative references and optional assets.
- Optional Python (matplotlib, pandas, numpy) or R (ggplot2, patchwork) for figure starter code.
- No network access, external corpus or absolute paths required at run time.

## License and attribution

Apache-2.0. See LICENSE and NOTICE.md; adapted open-source material is attributed to nature-skills (Apache-2.0).
