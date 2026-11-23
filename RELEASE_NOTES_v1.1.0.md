# NatSci-Writing-skills v1.1.0

Publication-level coverage upgrade, based on a full audit against the author's standards, the latest nature-skills upstream (commit c6701db, 2026-11-22) and Nature/Science requirements.

## New capabilities

- **Editorial fit and submission**: Nature/Science editorial criteria, article limits and stage gate, initial submission package, cover letter, title page, declarations, reviewer suggestions, presubmission enquiry and journal choice.
- **Innovation and broad interest**: contribution types and ladder, gap engineering, competing explanations and discriminating predictions, why-this/why-now/why-broad, broad-interest test, positioning against prior work.
- **Language and academic taste**: rhythm, voice, restraint, Nature house style, taste diagnostics, model shapes, Chinese-specific checks.
- **Main-text discipline and information architecture**: result classification, shortest evidence chain, main-text/caption/SI split, display budgets, revision-accretion control, claim-repetition audit, auditable compression record.
- **Statistics and reporting integrity**: independent unit and replication, Nature statistical requirements, Reporting Summary, common failure modes, figure statistics, image integrity, data/code/materials statements, P0/P1/P2 audit.
- **Figure evidence architecture**: multipanel inferential roles, evidence-chain archetypes, figure-order escalation, visual hierarchy, panel necessity, information density, vector schematic rules, graphical-abstract guidance.

## New files

- Six English and six Chinese references, plus five bilingual templates (cover letter/submission, innovation canvas, editorial audit, reporting/statistics checklist, figure evidence map).
- Bilingual coverage audit: docs/COVERAGE-AUDIT.md and docs/COVERAGE-AUDIT.zh-CN.md.
- Integrated latest upstream: nature-writing submission package and journal fragments; main-text discipline and Nature section corpus guidance; nature-statistics; nature-figure multipanel/Nature requirements/vector schematics; nature-data requirements; reviewer/response and polishing updates.

## Verification

- Package and installed-copy validator pass.
- Python and R figure starters run and export SVG/PDF/600-dpi raster.
- Installer and zip extraction validated; manifest current.
- No private data, absolute paths or secrets.

## Upgrade notes

- SKILL.md versions are now 1.1.0 in both languages.
- If you installed v1.0.0, copy the new skill folders over the old ones or run tools/install.py --force.
