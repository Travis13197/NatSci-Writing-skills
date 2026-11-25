# Figure production: from claim to submission-grade artwork

Version 1.2.5; updated 2026-11-24. Read with figure-standards-nature-science.md (journal specifications, caption grammar, statistical display) and figure-design-and-audit.md (the author's project geometry, colour and release gates). This file is the end-to-end production workflow synthesized from the nature-skills figure system and the corpus evidence.

## 1. The figure contract (before any code)

Write these nine lines before opening a plotting tool:

~~~
Core conclusion: one sentence with a verb, e.g. "The model separates held-out families by conserved dimension 12".
Figure archetype: quantitative grid / schematic-led composite / image plate + quantitative / asymmetric mixed-modality.
Journal and output: target, column width, final size, formats.
Backend: Python or R (blocking; Section 3).
Panel map: a, b, c ... each with the question it answers.
Evidence hierarchy: hero evidence, validation, controls/robustness.
Statistics needed: n, centre, dispersion, test, correction.
Source data needed: file and join key for every quantitative panel.
Reviewer risk: the two or three things a referee will challenge.
~~~

Rules:
- The conclusion is a relationship, not a topic ("Treatment reduces X by restoring Y", not "Treatment results").
- Every panel answers a unique question; if covering it would not weaken the argument, delete or merge it.
- Separate primary from supporting evidence: the hero panel gets the clearest axis and largest area; controls stay visually quieter.
- If data exist but the claim is unstated, propose a provisional claim and confirm before styling.
- If the source data cannot support a panel, remove the panel rather than inventing or decorating it.

## 2. Archetypes and panel logic

| Archetype | Use when | Hero panel | Supporting panels |
|---|---|---|---|
| Quantitative grid | Claim is a numerical comparison | Often a summary metric or forest | Shared axes, aligned scales, compact legends |
| Schematic-led composite | Workflow, mechanism or design must be read first | Schematic at 35–60% of area | 2–4 quantitative validation panels |
| Image plate + quantification | Microscopy, histology, imaging, blots lead | Image plate or representative image | Scale bars, overlays, crops, paired quantification |
| Asymmetric mixed-modality | Schematic, raster and plots coexist | One panel spans rows/columns | Smaller panels ranked by evidence value |

Default reading order: system and design → primary comparison → mechanism or localisation → quantification of the representative observation → robustness, controls or independent validation. For Fig. 1, the first panel defines the visual vocabulary (colours, symbols, workflow direction, sample classes, scale) reused throughout the figure and manuscript.

Panel count discipline: three analytical panels per row when the row is complete; a five-panel plate is 3 + 2 centred; a six-panel plate is 3 × 2; the project default for a full composite is nine analytical panels in 3 × 3. A separate evidence track (for example a sequence track) may sit above and does not count toward the analytical grid. Seven-, eight-, ten- and eleven-panel mixed rows fail the project release; use the project overlay for exact geometry.

## 3. Backend gate: Python or R

If the user has not chosen a backend explicitly or through a language-specific file, ask exactly one question — "Python or R?" — and stop. Do not default, guess, or generate mock figures first. Once chosen, the backend is exclusive for plotting, previews, exports and visual QA. If the selected runtime is missing, stop and report the blocker; provide the selected-backend script and install instructions rather than substituting the other language.

- Python stack: matplotlib, seaborn, subplot_mosaic/GridSpec, pandas/numpy/statsmodels, matplotlib.imshow/skimage/tifffile; export SVG (svg.fonttype='none'), PDF (pdf.fonttype=42), TIFF at 600 dpi.
- R stack: ggplot2, patchwork, ComplexHeatmap/circlize, ggrepel, survival/survminer, Seurat/ggtree; export svglite, cairo_pdf, ragg::agg_tiff.
- Mixed workflow is allowed only for non-visual data preparation; final assembly and all visual output use the selected backend.

## 4. Design system

**Typography.** Arial/Helvetica (fallback DejaVu Sans), consistent across all figures; editable text in SVG/PDF; math only when the renderer supports it. Journal print sizes are 5–7 pt (Nature/Science); the author's HTML/project overlay uses larger roles (10 pt ordinary text, 10.5 pt axis labels, 11 pt bold panel titles, 11.5 pt structure titles, 12.5 pt panel letters) and these must not be mixed with journal print sizes in one deliverable. Never shrink type below the release floor to solve crowding; enlarge the canvas, thin ticks, shorten labels, or move exact values to the caption/source table.

**Axes and framing.** Left and bottom spines only; top/right off; frameless legends; no grid by default. Tick labels and axis titles must be present on every analytical axes, including matrices and categorical panels. Set explicit limits when automatic locators create ticks outside the data range.

**Colour.** One neutral family, one signal family, one accent family per figure. Semantic stability beats hue variety: the same object, method or state keeps one colour across panels, figures and text; evidence status (pass/fail, uncertainty, condition) is encoded by fill, shape, hatch, line style or direct label, not by recolouring the object. Use colour-blind-safe hues (Okabe–Ito as the hue source). At most three chromatic categories in a qualitative panel; add shape/line/direct labels beyond that. Sequential variables use a monotone ramp; signed deviations use a diverging ramp (brick-red–neutral–deep-blue). Forbid jet/rainbow/hsv, decorative cycling and text below 4.5:1 contrast. Matrix cells carry no text overlays; encode support with markers or outlines and keep values in the source table. The project semantic palette (navy #0D5673, secondary #4E8EAD, teal #16786F, ochre #C77A24, brick #B8453E, plum #6C5079, neutral #586B75, text #132B36) is defined in figure-design-and-audit.md and figure-colour-audit-contract.md.

**Density.** Each panel needs one data-driven visual anchor, a primary-to-secondary mark hierarchy, visible uncertainty or a reference line, and enough evidence to answer a question. Reject naked coordinate boxes, isolated mean bars, single points and threshold-free curves when intervals, controls, repeated measurements, matched nulls or sample-level observations exist. Dense scatter keeps individuals with transparency/density; forests show intervals, support and denominators; matrices add uncertainty or support geometry; sparse protocols show change against a named baseline.

## 5. Chart selection

- Comparison across methods: horizontal bars ordered by effect, with uncertainty, individual points where n is small, and direct labels; avoid 3D bars and redundant grids.
- Trend over time or dose: line with uncertainty band; one shared legend above a row of related panels; reference line for baseline; do not use a bar for a continuous series.
- Distribution across groups: box/violin with points; show n and centre; do not hide bimodality behind a mean ± s.e.m. bar.
- Relationship: scatter with marginal distributions when correlation is the claim; encode a third variable by size only if the legend makes the mapping legible; add quadrant reference lines when the interpretation depends on them.
- Composition: stacked bar for absolute shares; pair it with a z-score deviation heatmap for what is atypical, and a scatter for co-variation. Do not repeat the same slice in two chart types.
- Heatmap: per-column normalisation when columns are on different scales; white for missing; no cell text; cluster order documented; colour bar labelled with the statistic.
- Radar/polar: only for multi-benchmark profiles where each spoke is independently normalised; custom spokes and ring, no default grid, legend outside.
- Imaging: grayscale context with 1–2 fluorescent channels; black only inside the image plate; consistent crops, scale bars and view boxes.
- Structural: whole view for orientation, crop for mechanism, two orthogonal views when the claim is geometric; identical residue/state colours in paired quantitative panels; Baker-standard structural requirements in structural-figures-baker-standard.md.

## 6. Statistical display and caption

- State n and what n counts (cells, proteins, donors, independent experiments). Show individual points for small n.
- Define centre and dispersion (mean ± s.d./s.e.m., median with IQR, 95% CI); never leave "error bars" undefined.
- Name the test, sidedness, correction family and exact comparison; report effect size and uncertainty, not only P.
- For model figures: train/validation/test split, seeds/folds, metric definition, baseline and variability; keep metric definitions constant across panels.
- For images: independent experiments, representative-image criterion, scale bar length, channel mapping, brightness/contrast adjustments (global vs local), and raw-file provenance.
- Caption skeleton: "Fig. N |" bold noun-phrase title → panel walkthrough in present tense → statistics → symbols → source-data/permission line. Keep ≤300 words for Nature style; numbers belong in panels and statistics, not in the title line. Do not copy source wording from other papers.

## 7. Export and QA

- Design at final size in millimetres (Nature 89/183 mm; Science 55/120/183 mm), with margins for title, ticks, labels and legend bands.
- SVG/PDF for line art with editable text; TIFF/PNG at 300–600 dpi for raster; RGB; embed fonts; preserve aspect ratio.
- Verify at 100% print size, in greyscale and in colour-blind simulation; check text-text, text-canvas and text-mark collisions for every artist type (scatter, line collections, intervals, bars, identity lines), not only points.
- Check outer content extent and internal blank bands for raster panels; crop only fully blank outer margins; keep molecular aspect ratio; structure panels retain ≥85% content extent.
- Record release files: panel geometry, gutter widths, typography per axes, colour roles, collision results, source-data mapping, export checks. The project audit files and thresholds are specified in figure-design-and-audit.md, panel-layout-and-letter-placement.md and figure-colour-audit-contract.md; the Chinese package additionally carries figure-r50-regression-checklist.md.
- Never compact designed gutters after rendering; the saved artifact must be the audited layout. A previous PASS does not certify a new render; re-measure the current file.

## 8. Integration with the manuscript

- The body text explains the science; the caption inventories the panels. After each figure, the Results text states what was found, which comparison establishes it, and where interpretation stops.
- Keep figure numbers, panel letters, legends, text references and source-data links consistent; update all after any panel change.
- For multiple result branches, keep a branch-by-branch index of estimand, denominator, threshold and failure condition.
- If the source data cannot be released, say what can be released (summary statistics, metadata, synthetic data) and why; do not imply availability that does not exist.

## 8b. SEAL and per-panel deliverables

For SEAL figures, read seal-supplementary-figure-standard.md in full. Every declared panel is its own editable SVG with its own panel letter, axis labels, ticks, marks and annotations; the composite must be reproducible from panel exports. Deliver composite SVG, vector PDF, 600-dpi PNG/JPG, one SVG per panel, one SVG per shared legend or scale bar, the caption, a panel-definition record and an audit record. Automated collision checks are screening only; inspect every figure at final size panel by panel and record defects and fixes. Label stacks with leader lines, row/column bands and the 8/10/10/0.4 pt release gate are defined in that reference.

## 9. Minimal working templates

Python (matplotlib) skeleton:

~~~python
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "svg.fonttype": "none", "pdf.fonttype": 42,
    "axes.spines.right": False, "axes.spines.top": False,
    "legend.frameon": False, "font.size": 7,
})
fig, axes = plt.subplots(1, 3, figsize=(183/25.4, 60/25.4), constrained_layout=True)
# one data plot per axes; direct labels; n and uncertainty documented in caption
fig.savefig("fig1.svg"); fig.savefig("fig1.pdf"); fig.savefig("fig1.tiff", dpi=600)
~~~

R (ggplot2 + patchwork) skeleton:

~~~r
library(ggplot2); library(patchwork)
p <- ggplot(df, aes(x = method, y = value, colour = family)) +
  geom_point(position = position_jitter(width = 0.12), size = 1.2) +
  stat_summary(fun = median, geom = "crossbar", width = 0.5) +
  theme_classic(base_size = 7, base_family = "Arial") +
  theme(legend.position = "top")
svglite::svglite("fig1.svg", width = 183/25.4, height = 60/25.4); print(p); dev.off()
~~~

These templates are starting points; the contract, archetype and evidence logic decide the panels, not the template.

## 11. AI-generated and AI-assisted figures

Before choosing a tool, classify the figure. Data figures (microscopy, gels, blots, imaging, spectra, plots, structures) come from real data and code; a generative image model must not create or alter them. Conceptual schematics, graphical abstracts and cover art follow the target journal's AI-image policy; many journals require editor permission and disclosure. AI-assisted layout or typography is allowed, with substantive assistance disclosed and the final vector checked.

Never use generative fill, object removal, synthetic microscopy, AI upscaling that invents detail, fake scale bars or fabricated molecular structures. Keep a provenance record: tool/version/backend, date, full prompt, seed/settings, output hash, manual edits, source data/code and human reviewer. Put the disclosure in Methods, figure legend and cover letter when the journal permits AI-assisted figures. Read ai-figures-and-visual-integrity.md; record with assets/templates/ai-image-provenance-record.md.

## 12. v1.2.6.3 legend and tick implementation order

Draw the data first. Then remove the unplaced legend and choose one of three layouts: direct
axes-fraction labels when at most four short series have a genuine right-side corridor; a
horizontal legend below the title when that band has room; or a one-column legend in a
reserved right corridor. Translate direct labels as one stack and preserve a minimum
separation. Do not clip each label independently at the frame boundary. Audit legends,
direct labels and series text for data occlusion before release.

Register axis titles as protected objects before collision handling. Use four to six major
ticks on numeric axes. For categorical axes, abbreviate first, then choose two to four
evenly spaced labels from the original tick positions using rendered bounding boxes and set
those ticks explicitly with `set_xticks` or `set_yticks`. Explicit selection prevents hidden
labels from reappearing on the next draw. Preserve at least two ticks and keep every axis
title visible with sufficient label padding.

Reapply panel titles and letters after the final axes size is known. Derive the anchor from
the topmost y-tick bbox, text height and at least 4 mm clearance. Add range headroom after
final autoscaling. Before saving, rerun text–text, text–data, legend–data and canvas-boundary
audits and write `axis_tick_completeness` and `legend_data_occlusions`.

## 13. v1.2.6.4 star notation and horizontal legend implementation

Convert every significance string through one function to `****/***/**/*/n.s.`; never
assemble q text inside a plot. Effect curves carry their matching 95% CI band. For one
continuous significant run, label representative first, middle and last points, and always
keep state changes and the last point. Forest outside columns use the same star mapping.

Legend order is fixed: multi-column horizontal header below the title, direct endpoint
labels second, one-column right-side legend last. Place the header with `lower center` just
outside the data rectangle and mark `_cellauto_legend_mode="header"`. The dynamic title and
letter anchor reads that legend's y1 and moves above it. Encode state transitions as
`C/T/B→C/T/B`. A right legend that could fit above, in-plot `q=` text or colliding adjacent
stars blocks release.

## 14. v1.2.6.6 implementation recipe for projections and cartoons

Projection panels: compute span = max(x.max()-x.min(), y.max()-y.min()) * 1.06; set both
limits to the same span around each centre; enable equal aspect with a fixed square box; then
set explicit ticks. Assert every point lies inside the limits and store the count of points
outside (must be zero). Keep the axes box square after saving.

Cartoon panels: before loading, rewrite the element columns of the PDB from atom names
(element = name[0] if name[0].isalpha() else name[1]), keep charge columns blank, and save a
corrected copy with source and corrected hashes. In PyMOL, assign secondary structure, enable
round helices before rebuild, colour helix/sheet/loop by role, set loop transparency to 0.20
only for loop selections, render with the opaque white background and orthographic camera,
and crop to ink before composing. Reserve a 200 px label band per tile at 2,800 px canvas
width for 10 pt labels. Never ship a surface-only panel as fold evidence.

## 15. v1.2.6.7 density implementation recipe

Layer distributions with strip plots: draw a violin at alpha 0.18, a box at alpha 0.35, jittered
observations at alpha 0.55 and size 3-5, and a median/CI marker in the text colour. For
scatter panels add a regression line with a bootstrap band, or a hexbin plus marginal summary
text in the caption. For dose-response panels plot the estimate with a CI band and keep the
individual endpoint rug. Never use default black boxplot whiskers; set whiskerprops,
capprops and medianprops to registered colours. Audit every panel for evidence-layer count
and for unregistered colours before export.

## 16. v1.2.6.8 extent implementation recipe

Compute limits with a helper such as: pad = 0.04 * (max - min) or 0.02 * abs(value); xlim =
(min - pad, max + pad); skip the pad for percentage axes that must stay at 0/100. For
distributions include the violin/KDE body extent, not only the observations. For log axes pad
in log space. Set explicit ticks after setting limits. Run a panel-extent audit over every axis
before export and fail the build if any panel has clipped points or more than 0.5% overshoot.

