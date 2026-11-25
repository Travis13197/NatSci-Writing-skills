# Changelog

All notable changes to NatSci-Writing-skills are documented here. The system follows semantic versioning.

## 1.2.6.8 — 2026-11-25

- Reflow addendum: a log-scaled axis can inflate the measured row pitch and leave a large internal blank band even when every artist is inside the axes. If a plate develops an unexplained blank band, test the log axis; for a narrow dynamic range use a linear axis, or reserve enough explicit vertical space and recheck the content-extent audit.

- Visible-body addendum: audit PolyCollection/LineCollection paths, not only scatter offsets; extend violin KDE grids by about 1.5 bandwidths (flat caps fail); extend density-contour grids by about 6%; give points on 0/1/thresholds a 2-4% marker margin; check rendered rasters at final display width; serve versioned raster URLs or no-store headers.


Universal data-extent release, derived from a full panel audit of the PGv3
six-figure plate set where several axes still truncated real observations,
confidence intervals or long-tailed controls.

- Every quantitative panel must display the full data extent on both axes;
  limits are computed from the current data, not copied from earlier versions.
- Threshold views require a full-range companion; hidden zero-valued endpoints
  fail.
- The audit compares data extrema with sorted limits in value space, handles
  inverted and log axes, and records clipped-point counts and overshoot per
  panel.
- Default collection offsets and legend proxies are excluded from the count.
- After extending limits, explicit ticks replace auto-locators outside view.

## 1.2.6.7 — 2026-11-25

Evidence-density and visual-finish release, derived from the PGv3 six-figure
review where technically valid plates still read as sparse and rough.

- Every analytical panel must carry at least three evidence layers
  (observations, distribution, estimate with interval, reference line, effect
  size, cross-condition contrast, structural annotation); the layer count is
  audited.
- Means-only bars and single series without band, points or rug fail; a
  two-category bar panel requires a companion distribution in the same figure.
- Repeated dimension-swap charts (algorithm, rule, environment with the same
  encoding) fail unless one variant adds a distribution, contrast or mechanism
  layer.
- Visual finish: semantic fills with an alpha hierarchy, registered colours for
  every whisker and edge, no default #000000, no mostly empty panels.
- Figure-level rhythm: each row carries a distinct evidence role.
- Implementation recipes added for layered distributions, regression bands and
  dose-response ribbons.

## 1.2.6.6 — 2026-11-24

Projection-extent, structural-cartoon and HTML-claim release, derived from a
full redraw of the PGv3 exploratory growth plates.

- Projection panels must cover the complete data extent: zero clipped points,
  limits recomputed from the current data, explicit ticks instead of a stale
  automatic locator.
- PCA/t-SNE/UMAP panels require equal x/y unit length with equal spans and a
  square axes box.
- Fold-evidence panels must use cartoon/ribbon geometry; surface-only renders
  are no longer acceptable as fold evidence.
- Non-focal loops and background chains use grey at 20% transparency (about
  80% visible); focal folds stay opaque.
- Structure tiles reserve an auditable label band at 10 pt equivalent; labels
  never cover molecule ink.
- Added a pre-render structure-file gate: element columns 77-78 right
  justified, guide atoms equal to C-alpha count, non-empty FASTA. Predicted
  PDB writers that left-justify elements turn CA into calcium and produce
  blank cartoons; the rule records source and corrected SHA-256.
- HTML reports must bold Results topic sentences, decisive numbers, logical
  turns, abstract conclusions and caption inference clauses (1-3 spans per
  paragraph).
- HTML figure elements must display a 600 dpi raster and link SVG/PDF
  separately; rendered-page screenshots at the figure position replace the
  naturalWidth check alone.

## 1.2.6.4 — 2026-11-24

Star-notation and horizontal-legend release, derived from a second
panel-by-panel audit of the CellAuto figures.

- Replaced in-plot q text with conventional `****/***/**/*/n.s.` markers.
- Kept exact q values, adjustment methods and comparison keys in captions
  and source tables.
- Added CI bands and representative significance markers to continuous
  effect curves so adjacent star labels cannot collide.
- Changed legend priority to horizontal header first, direct labels second
  and right-side columns last.
- Added compact state-transition labels (`C→C`, `T→C`, `T→T`, `B→B`).
- Made panel title and letter anchors rise above the rendered header legend.
- Added full-panel regressions for Fig. 12 g/h, Fig. 14e and Fig. 15b.
- BioNoether structure regression: context cartoons use ChimeraX
  `transparency 20` (about 80% visible) with a white depth cue beginning at
  0.75; opaque key cartoons and side-chain sticks remain the foreground.
- A structure panel contains one molecular object. Complete and local views are
  separate panels, and local views retain six residues on each side of the hit.
- BioNoether complete-cell gutters use the author-confirmed `0.27–0.29 w`
  range, default `0.28 w`, replacing the earlier `0.40 w` spacing.
- Structure raster labels use 52 px source type, audited at 5–7 pt in the final
  HTML; the ordinary 10 pt screen rule is not applied mechanically to raster
  residue labels.
- Biological terminology and reader-facing language rules now cover GB1,
  1PGA, Olson data, q/Q scores, forbidden AI-style labels and per-panel
  semantics.

## 1.2.6.3 — 2026-11-24

Legend, tick, headroom and significance regression release, derived from a
panel-by-panel audit of the CellAuto report.

- Added a hard legend–data separation gate. Short series use one-word labels;
  direct labels are limited to four series and preserve spacing as an
  axes-fraction stack; denser series move to a horizontal header legend or a
  reserved right-side column.
- Added `legend_data_occlusions` and `zero_legend_data_occlusion` to the release
  contract. A plate fails when any legend, direct label or series text covers a
  point, line, interval, bar, matrix or structure.
- Protected x/y axis titles during tick-collision handling. Numeric axes retain
  four to six major ticks. Categorical labels are abbreviated, rotated only
  when genuinely long, and reduced to two to four evenly spaced ticks selected
  from rendered bounding boxes rather than every-other-plus-last sampling.
- Added `axis_tick_completeness` and `all_axes_have_visible_ticks`; every axis
  keeps at least two interpretable ticks, and `sparsified_tick_labels` cannot
  contain an axis title.
- Made panel header height depend on the top y-tick bbox, text height and a
  minimum clearance above the axes. Fixed header ratios remain only a lower
  bound and are remeasured after final panel scaling.
- Added linear and log range headroom. Non-negative proportions keep zero and
  add upper space; near-saturated variables may use baseline-relative change,
  recovery gain or completion gain with the denominator retained.
- Added real-comparison significance rules. Bar, box and violin brackets use
  the same grouping, independent unit, denominator and direction; forest plots
  place adjusted q values outside the plotting area; panels without a formal
  comparison remain descriptive.
- Added distribution transparency guidance: observations about 0.50 alpha,
  violin fill about 0.28 and box fill about 0.38.
- Updated bilingual figure design, production, craft, journal-standard, panel
  layout, R50, HTML/data verification, academic-prompt and SKILL gates.

## 1.2.6.2 — 2026-11-24

Final-footprint and evidence-density regression release, derived from a full
audit of the CellAuto report's main, supplementary and generation figures.

- Added the HTML effective-font rule: native Matplotlib point sizes are not accepted unless the final PNG width, browser CSS width and downsampling ratio are recorded together. A nominally 10 pt label in a 6,500–9,700 px raster displayed at about 1,384 CSS px failed because its effective size fell to roughly 2–7 pt.
- Added fixed physical canvas families for regular grids. A 3×3 plate now starts from a 72 mm data-box target, 28.8 mm complete-cell gutters and a fixed outer label band; a single long legend, y tick or comparison name cannot expand one column into a central blank corridor.
- Prohibited absolute `set_label_coords(-0.55/1.55)` positioning for long y labels. Comparison names are abbreviated in the tick rail, exact estimands remain in axis titles, captions and source tables, and axes use fixed label padding.
- Added a release gate that reports `effective_font_size_audit.tsv`, `column_cell_width_audit.tsv` and `panel_role_audit.tsv` for every quantitative figure; the last table records points, intervals, bars, matrices, thresholds and direct annotations per panel.
- Added the duplicate-estimand rejection: Main Fig. 7 g/h previously repeated the completion and recovery-defined summaries in e. They now show damage-matched before/after recovery tracks and damage-denominator anatomy.
- Added numeric-length layouts for distance-response figures, avoiding 12–24 long categorical bars whose labels widened columns and removed readable axes area.
- Added the ordered-dimension rule: length, time, dose and information levels stay on continuous axes; action arms and conditions use colour/shape/hatch instead of one categorical tick per length-by-condition combination.
- Added rendered-page lazy-image verification: supplement cards must reserve an aspect ratio/minimum height, every collapsed `<details>` is opened, and all images must reach `complete && naturalWidth > 0`.
- Calibrated internal blank-band acceptance: multi-panel figures with 0.38–0.42 w complete-cell gutters use a 0.18 full-image limit; isolated structure rasters keep 0.14.
- Updated the prompt library, figure production, information-density, journal standards, panel layout and R50 regression references with these checks.

## 1.2.5 — 2026-11-24

AI writing and AI figure integrity release, based on a broad policy review of Nature Portfolio, Science/AAAS, Cell Press, Elsevier, Springer Nature, PLOS, ICMJE, COPE and current surveys.

- Added references/ai-figures-and-visual-integrity.md (plus Chinese edition): data vs conceptual figures, publisher AI-image policies, absolute prohibitions, disclosure framework, provenance record, prompt/data hygiene, copyright/licensing, reviewer boundaries and a negative checklist.
- Expanded ai-use-and-writing-integrity.md (EN/ZH): 2026 policy clarifications, AI-writing negative list, image-policy pointer, reviewer/editor boundaries, detection/translation/licensing, and additional audit gates.
- Added templates: ai-image-provenance-record.md and ai-negative-checklist.md (19 templates per language).
- Extended figure-production, figure-craft and figure-standards references with AI-image gates; added SKILL 9.0 AI figure gate, AI negative gate in revision, and final gates for AI writing and figures.
- Updated README, docs, architecture, usage, coverage audit, versions, manifest and release package.
- Sources include Nature Methods 2026, Nature Materials 2026, Nature Geoscience, Science cover-image policy, Elsevier June 2026, Cell Press, Springer Nature, PLOS, ICMJE 2026, COPE, and arXiv 2603.16159.

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
