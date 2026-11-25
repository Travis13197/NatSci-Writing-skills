# Scientific figure design and audit

Version 1.1.0; updated 2026-11-23 (merged from the author's 1.18.0 figure system). Use for paper figures, extended-data figures, structural evidence displays, HTML figure groups and figure legends.

Journal specifications, caption grammar and statistical-display standards are in figure-standards-nature-science.md. The end-to-end production workflow (figure contract, archetypes, Python/R backends, export and QA) is in figure-production.md. This file remains the author's project overlay: panel geometry, gutters, colour hierarchy, structural rendering and release audits.

When panel gutters or panel letters are revised, also read
`references/panel-layout-and-letter-placement.md` in full. It defines the current
cell-anchor coordinates, retired layout thresholds and the measurements required to
prevent false-positive geometry checks.

For molecular structure figures, protein interfaces, ligand pockets, protein–DNA/RNA complexes
and oligomeric assemblies, also read `references/structural-figures-baker-standard.md` in full.
That standard distils ten David Baker laboratory papers into concrete rules for whole-complex
orientation, orthographic cameras, homologous-chain colour, design/prediction/experiment
overlays, retained parent context, side-chain sticks, ligand-pocket presentation, external
labels, occlusion control and editable PyMOL/ChimeraX sessions.

## 1. Define the scientific task

Each figure group answers one biological question. State the question, comparison, principal evidence and inference before selecting a chart type. The figure title names the relationship supported by the complete panel set. The legend explains how the panels form one argument.

The body text after each figure must state the principal finding, the comparison or numerical
pattern that establishes the regularity, the relationship supported by the phenomenon and the
interpretation boundary. Captions inventory panels; prose explains what the figure means.
Multi-branch reports add a branch-by-branch result index preserving each estimand, denominator,
threshold and failure condition.

Figure language follows the same direct scientific standard as the manuscript. Panel titles,
internal annotations, legends and captions name the measured effect, count, interval, comparison
or condition. Use `the adjusted 95% interval includes zero` for a zero-crossing estimate,
`10/16 contrasts met the Holm threshold` for a supported subset, and `62/84 shifts were negative`
for a directional count. Avoid defensive boilerplate (`not supported`, `only`, `cannot`,
`bounded`, `limited to`, `not a`) when the underlying result can be stated positively and
quantitatively. Preserve negative findings, denominators, sample hierarchy, uncertainty and
measured conditions. Do not hide an inconvenient result to make the wording sound stronger.

Structural evidence figures contain a concrete structure and a paired distance, response, effect-size, model comparison or statistical test. Structure panels locate residues, interfaces and states; statistical panels quantify the relationship. Use the same residue numbering, state names and colour mapping across both.

Panels generally follow this order: structural context, measurement design, primary comparison, robustness or independent validation, mechanistic inference. Panel order follows the reader's reasoning path, and panel letters match manuscript references.

## 2. Panel geometry

"Near-square" refers to the physical x-axis length and y-axis length inside the data coordinate box. Regular analytical panels target `plot_box_width / plot_box_height = 1.0` and must remain within `0.9–1.1` after final typography, single-line title placement, tick thinning and legend placement. The composite figure, the exported PNG and the HTML figure card can remain rectangular. Panel letters, titles, legends, tick labels and colour bars sit outside the plotting box and do not count toward this ratio.

### Mandatory three-panel rows

For this author's composite biology figures, arrange regular panels three per row. Six-panel
plates use `3 × 2`; five-panel plates use three panels in the first row and two centred panels
in the second. Do not retain a two-panel row from an earlier layout. Use one physical
three-column axes grid across all rows. When an 11-pt single-line title or the final legend
requires more room, enlarge the regular data box and the physical plate rather than wrapping
the title or reducing type. Fixed panel cells contain the complete visual envelope; their
neighboring boundaries retain `0.40 × panel width`, with acceptance from `0.38` to `0.42`.
This represents approximately one fifth blank separation at each panel side. The earlier
`0.20–0.25` and `0.28–0.32` ranges are retired because a full plate can pass while remaining
visibly compressed.

Current BioGeo-ID figures default to nine analytical panels in a complete `3×3` grid.
Six-panel `3×2` plates are valid only when a ninth independent evidence dimension would
duplicate an estimand or add decoration. The top evidence track is a registered wide
exception and does not count toward the nine. Each ninth panel must answer a new question
from a named source table, including matched background, interval, sample distribution,
threshold sensitivity, holdout calibration, coverage composition or support/completeness.
Do not use simplified mean bars, isolated points or threshold-free curves when source-level
distributions, intervals, pairing, background or controls are available.

Use a fixed physical axes grid. Within a figure, axes in one column share the same left
boundary across rows and axes in one row share the same bottom boundary, with deviations
at most `0.01 mm`. All regular axes have equal width and height within `0.01 mm` and stay
square. Do not centre rows independently. When label or legend extents differ, define fixed
panel cells from the maximum left extension, axes width and maximum right extension; a
subtle `0.6 pt` `#CAD7DC` cell frame can mark the complete boundary without covering data
or acting as another plot.

Regular panel titles remain single-line, fit within the axes width, are horizontally centred
over the data box and bold, and share one title top line with the panel letter. Use 10 pt for
ordinary text, ticks, legends and direct labels; 10.5 pt for axis labels; 11 pt bold for
regular titles; 11.5 pt bold for structure titles; and
12.5 pt for panel letters. Use DejaVu Sans and `#132B36` for text. Validate exact role
sizes and colors rather than figure-level minima.

Every visible analytical axes requires non-empty x- and y-axis titles. Matrix panels name
row and column classes; categorical panels label class and count/proportion axes; continuous
panels include variable and unit. Axis labels are fixed at 10.5 pt. Structure image panels
without a data coordinate system are registered exceptions.

Use letter `a` for the evidence track and `b–j` for the nine analytical panels. The letter
defines the complete panel cell’s outer upper-left blank. Its box begins approximately
`0.20 × panel width` left of the data-box left edge (`7–12 mm` for a 50.8-mm panel), extends
at least `4 mm` above the data-box top, and shares a title top line about
`0.20 × panel height` above the data-box top within `0.5 mm`. The title is centred over the
data box and remains at least `3 mm` right of the letter. Letter and title remain
separate text objects. Detect them with character, weight, size and header-band position;
`[a-z]` alone misclassifies a track stage such as `h`.

Reject naked coordinate boxes, isolated summary bars, single points and threshold-free
curves. Each figure needs at least two evidence encodings and must show available sample
observations, intervals, pairing, matched background, controls, thresholds or holdouts.

### Complete panel-boundary gutters

Audit horizontal and vertical gaps from complete visual panel boundaries. The boundary is the
union of the data box, panel letter, wrapped title, every tick and offset text, axis labels,
direct annotations and external legend. Both dimensions require a clear gap of
`0.38–0.42 × regular panel data-box width`, with `0.40` as the default. Axes-only and
cell-only gaps are insufficient.

Measure after the last tick suppression, typography change and legend placement. Suppressing
edge ticks can shrink a panel's visual extent, so a row placed before that pass will have a
stale gap. Iterate in the order `final tick suppression → complete-boundary measurement →
reflow → remeasure`. Keep titles single-line within a row, with one shared title top line
and title-band height; otherwise a short title creates unexplained extra clearance. Freeze
the resulting positions before export. A save function that repeats `subplots_adjust`,
`tight_layout` or automatic title placement invalidates the audit. Record boundaries,
millimetre gaps and `gap / panel_width` in `panel_visual_gutter_audit.tsv`, and reject
negative gaps, intersecting boundaries or values outside `0.38–0.42`.

Measure adjacent pairs independently in both directions. A current regression produced
horizontal complete-boundary gaps near `0.225w` while some vertical pairs reached `0.45w`
because one panel had a one-row legend and another had none. Equalize the footer band by
rebuilding short legends as one row, adding a short key for the principal mark of a
quantitative panel without a legend, and adding a readable structure-identity, colour and
residue/line-width note to a structure panel. Keep the axes in one row on a common top line.
Do not shift one axes or insert invisible spacing to manufacture a passing value.
Composite exports may crop only fully blank outer margins. Never compact designed internal
gutters after rendering, because the PNG then differs from PDF, SVG and the audited layout.
Size and centre a standalone panel canvas around its widest final legend and label bounds
before export.

### Mandatory one-panel-one-plot rule

Each panel must contain exactly one data plotting area. Do not use `inset_axes`, nested subplots, facet grids, miniature panels, secondary colour-bar axes or several plots assembled inside one panel. Multiple quantities can share a panel only when they are layered into one meaningful coordinate system with a common position axis or unit. Express additional dimensions through point shape, line style, transparency, size, ordered tracks and direct labels. If quantities cannot share one interpretable frame, retain the panel's primary evidence plot and move supporting evidence to the caption, source table or a separate panel.

The renderer must fail closed if a panel creates any new Axes during rendering. A panel record must explicitly state that it uses one data axis. Aligned long-sequence or residue tracks are allowed only when all layers share the same positional coordinate and remain one continuous plot.

If dimensionality reduction is part of the scientific design, show the coordinate plot and the metadata or features projected onto it. A coverage census, one density map and a retention curve are not a complete atlas layer. Separate the source population, fitted sample, annotation or reference-cohort map, at least one continuous feature map and its feature distribution. A 40,000-record projection sampled from a 210,709-record census remains a 40k projection; exact overlap with a 20,000-record reference is not an independently fitted 20k atlas. Name the annotation system and do not infer global non-annotation from a blank selected-category field. If the complete raw store is absent, plot the available coordinates and exact overlap, record the missing full-atlas gate, and do not synthesize the missing cloud.

A previous geometry PASS does not establish visual acceptance. When an author reports remaining crowding, replace the panel's evidence composition instead of merely changing colours or line widths. Repeated records should be summarized only when the summary preserves the estimand and the source table retains the full distribution. A panel should normally carry one primary comparison, not every available source column.

Apply `Axes.set_box_aspect(1)` to regular analytical panels. When a panel occupies an unequal grid cell, adjust the grid, canvas height or label arrangement so the data box has equal x- and y-axis lengths. Cropping the whole card into a square does not satisfy this check.

Do not allow axes centring to create false whitespace. If a rectangular allocation is wider than its square data box, choose an explicit anchor, reduce the allocation or redistribute the row. Audit the final axes rectangles in millimetres. Regular panels in the same row must share one data-box side length within 1 mm, and a registered wide track must share the row height. Compute adjacent-axis gutters rather than only cell boundaries. Reject overlaps, unused central bands that dominate the composition, and horizontal gaps that are not explained by axis labels plus a small gutter.

Do not solve a square panel by stacking a multi-entry legend in one column below it. For two to three short legend entries, use one horizontal row; for four to six, normally use two compact rows. Explicitly set limits and ticks when an automatic locator creates labels outside the displayed range or corner-label collisions. A detached top miniature, secondary fragment or visual sub-panel violates the one-data-axis rule even when it is not created with `inset_axes`.

Run the geometry audit twice. The first pass records the pre-layout data box. The second pass records the final rendered axes box after fonts, labels, titles and legends have reached release size. Read the rendered width and height in pixels, not the grid-cell allocation and not the exported composite dimensions. Read centered, left-aligned and right-aligned titles as separate title objects. A regular panel with a box ratio of 1.000 at both passes passes directly; a ratio within 0.9–1.1 passes with its measured value retained; a ratio outside this range requires a registered wide-exception purpose.

Wide panels are appropriate for:

- long sequence, gene, operon, domain or residue tracks;
- timelines, workflows and experimental schedules;
- 384-well plates and other spatial layouts;
- matrices with many horizontal labels that lose legibility when compressed;
- specialized panels where horizontal span and position must remain directly comparable.

Record wide exceptions in the source-data table or author verification note. Set `Axes.set_box_aspect(1)` or an equivalent control for other panels. Keep labels, legends and colour bars outside the data area rather than stretching the plot to create room.

## 3. Colour system

Blue carries the project's primary identity and neutral structural context. Okabe–Ito supplies
the colour-blind-safe hue separation; publication figures use controlled, lower-saturation
project colours with fixed semantic roles:

| Role | Colour | Value |
|---|---|---|
| Primary model/structure | Deep blue | `#0D5673` |
| Secondary model/prediction | Muted blue | `#4E8EAD` |
| Robust support/confirmation | Teal green | `#16786F` |
| Conditional/caution | Muted amber | `#C77A24` |
| Negative/stopped/failure | Brick red | `#B8453E` |
| Orthogonal validation | Muted purple | `#6C5079` |
| Neutral/context | Grey | `#586B75` |
| Text/annotation | Navy black | `#132B36` |

Most panels use one primary colour, one comparison colour and one neutral context colour.
A qualitative panel normally contains at most three chromatic categories plus neutral context.
Above three categories, add marker shape, line style, grouping, outlines or direct labels.
Continuous variables use a monotone blue ramp; signed deviations use brick-red–neutral–deep-blue.
Forbid `jet`, `rainbow`, `hsv`, `gist_rainbow` and decorative colour cycling. Text and axis labels
on white must reach at least 4.5:1 contrast. Matrix panels must not put numbers, letters or
`yes / ~ / x` inside cells; encode support with geometry or outlines and retain exact values in source data.

Reserve accents for biological roles such as the target mutation, positive control, independent validation, ligand-selective response or exceptional state. Keep those colour roles consistent across prose, structure, statistics, legends and captions. Information-dense blue figures receive one or two restrained accents when a real categorical comparison, signed effect, control or evidence tier needs immediate visual separation; decorative colour cycling remains prohibited.

Read `references/figure-colour-audit-contract.md` before assigning the palette. Object identity and evidence state are separate channels. The same model, system, state or residue keeps one colour throughout the group; pass/fail, condition or uncertainty uses marker fill, shape, hatch, outline, line style or a direct label. A summary bar panel that recolours the same objects to represent a gate result conflicts with the corresponding trajectories or matrices and must be redrawn.

Every redraw writes `figure_color_audit.tsv` and `figure_palette_roles.csv`. The per-panel
audit records semantic role, explicit colours, colormap name, forbidden-colormap use,
unregistered colours, chromatic category count, minimum text contrast against white and the
number of text annotations inside matrix cells. Release fails if any forbidden colormap is
used, any colour is unregistered, minimum text contrast is below 4.5, matrix-cell text is
nonzero, or the structure image and statistical panels use different versions of the palette.

Common failures observed in real revisions include assigning a saturated hue to every model,
inconsistent saturation across blue, purple and pink, writing correlation values or support
letters inside heatmap cells, colour-only encoding of supported/conditional/negative states,
pale text on white, redrawing statistical panels without rerendering the structure image,
retaining a retired 6 pt audit after the release floor moved to 10 pt, enlarging type without
enlarging the physical canvas, and substituting a figure-level typography PASS for per-axis
records.

## 4. Structure plus measurement

Choose structural views that expose the relevant pocket, DNA interface, domain connection, assembly interface or perturbation field. A whole-structure view supplies orientation; a crop or second view supplies residue-level context. Define colour, sphere size and labels in the legend.

The paired statistical panel uses the same residues, pairs or classes. Direct labels should identify the comparison and include the relevant effect or uncertainty. When feasible, label key residues in the structural panel and key comparisons in the statistical panel.

Figure legends describe object, comparison, key value and biological inference for each panel. Identify experimental structures, predicted structures and proposed relationships separately. Keep method inventories out of the legend.

## 5. Layout and readability

- Use a consistent type system, line weight and margin.
- Review type at the final print and 100% HTML display size. This project's release floor is 10 pt for the smallest annotation or tick label, 10.5 pt for axis labels, 11 pt for panel titles, 12.5 pt for panel letters and 10 pt for legends. A lower journal minimum is not permission to use unreadable text. If the complete comparison cannot be read without zooming, redraw the panel rather than shrinking typography.
- Solve crowding by enlarging the canvas, changing the grid, shortening titles, wrapping labels, thinning category ticks or combining adjacent residue labels. Do not compress key text to 4–5 pt to preserve every label.
- Separate panel letters from titles. Place regular panel letters at the upper left without covering ticks, axis labels, legends or the principal data.
- Label variables and units; state test type, sample size, error representation and correction.
- Pair categorical colours with marker shape, line style, hatch, direct labels or ordered position so meaning survives greyscale and colour-vision differences. Do not increase icon variety with decorative or semantically undefined symbols.
- Keep essential values visible without hover.
- Wrap or abbreviate long labels and define abbreviations.
- Place colour bars without compressing data areas.
- Use shared axes for common scales and identify panels with changed scales.
- Export PNG for web preview, PDF for submission and SVG for editable panels.
- Preserve image aspect ratio in HTML and control size through the container.

### Equal panel territory, gutters and evidence density

Equal evidence roles should receive equal visual territory. In a multi-panel comparison, structural context, measurement, primary comparison and validation panels normally use the same physical square footprint. Measure the rendered axes rather than the grid-cell allocation: equivalent panels should differ in area by no more than 5% and should not mix one small square with another nominally square box whose surrounding allocation is much larger.

A wide native raster is not a reason to make a short horizontal strip. If a whole-structure render is naturally elongated, compose the structural axes as a square using a sufficiently large global-context view plus a legible local inset or second view. The inset must preserve state and residue identity, remain secondary to the parent context and be described in the legend. Analytical one-plot panels continue to follow the one-data-axis rule; a molecular parent-and-detail composition is treated as structural evidence rather than a hidden facet grid.

Gutters are designed parts of the grid. Record complete panel boundaries rather than only
axes. Horizontal and vertical complete-boundary clearances each target
`0.38–0.42 × panel width`, default `0.40 × panel width`, after final typography, tick
suppression and legend placement. Panels should not visually touch. Empty space outside that
interval is a failure unless a registered scientific layout explains it. Freeze the converged
positions so the exported raster corresponds to the measured layout.

Panel count follows scientific breadth, not a decorative target. When two or more orthogonal frozen comparisons, controls or sample-level distributions exist, a two-panel summary is often under-informative for a top-tier figure. Use the additional comparisons to expose effect, null, repetition level and a registered condition or validation. Do not fill a grid with duplicated metrics, unlabeled subsets or decorative infographics. Every panel should answer a distinct part of the figure's argument.

Apply the same test to four-panel plates. Four summary panels can also be under-informative when source tables contain trajectory-, protein-, family- or mutation-level observations and an outer predictive holdout. The plate should show the smallest chain that preserves the result: effect, uncertainty, sample distribution, matched null or control, predictive holdout, and independent transfer or registered condition. Six equal-role panels commonly follow from that chain. Use a 3×2 square lattice when collapsing to four panels would move orthogonal evidence into prose. Do not add panels whose estimates duplicate one another.

### Structure-raster packing and blank-band release rule

Treat white space around a molecular render as allocated layout, not as part of the molecule. Measure the non-white molecular-ink bounding box in every whole-structure and close-up raster before composing a panel. Crop away source-canvas margins, retain only a controlled 2-4% breathing margin, and record the source dimensions, ink box, crop box and retained content fraction. An unexamined PyMOL/ChimeraX canvas must not set the height of a structural row.

Pack whole-structure and local views by object extent while preserving each image's native aspect ratio. Resize both to a common object height, keep their proportional widths and use one small, fixed gap. Do not stretch a structure horizontally or vertically, and do not enlarge a molecule merely to hide whitespace left by an incorrect row allocation.

Compute each structural axes height from its actual raster dimensions:

`height_fraction = width_fraction x (figure_width / figure_height) / (image_width / image_height)`

Use the reciprocal form only when deriving width from an explicitly fixed height. When an image is added to an axes with `aspect="equal"`, read the final axes position after `fig.canvas.draw()`; the axes must keep its intended top or bottom anchor and must not be silently moved outside the nominal figure box. Anchor a structural row by its top edge when images have different aspect ratios, then place the next row from the tallest or lowest rendered object edge plus one designed gutter. Avoid oversized fixed GridSpec rows that reserve blank space above or below short structural images.

Audit the final exported raster rather than only the nominal axes. Threshold near-white background consistently, locate the internal run of empty rows crossing the main content flow, and record its fraction of image height alongside the overall content bounding box. A structure composite should retain at least 0.85 of its width and height as content extent. The largest internal blank row band should be at most 0.14 of the exported figure height; a larger band fails release unless a specific wide-layout or isolated-column purpose is registered with its measured value. Check panel letters and titles against the final canvas at the same time: out-of-canvas text, text collisions and text placed outside its image axes fail release.

### Mandatory zero-text-collision rule

Headings, panel letters, axis labels, tick labels, legends and direct annotations must not overlap each other or cover data marks. Do not rely on opaque annotation boxes to hide collisions. Numerical sample sizes, intervals and secondary qualifications normally belong in the caption or source table; retain only short anchors needed to read the panel.

After minimum fonts are applied at final size, calculate the window bounding box of every visible text object. Reject the panel when two text boxes intersect, when text extends beyond the canvas, or when an exported raster contains ink at an unauthorized panel edge. Write the per-panel overlap count, out-of-bounds count, collision examples and final font limits to text and geometry ledgers.

For text-data occlusion, map artists with their own transforms, count only text whose centre is
inside the axes as a possible overlay, and keep legends in a dedicated band. Wide HTML tables
belong in local overflow containers and require a mobile page-width regression test.

Font changes are layout changes. Derive renderer and validator thresholds from one release
constant, enlarge the canvas and recompute gutters, and reduce log ticks or wrap categories
where needed. Write one `axis_index` row per panel with text count, minimum font, in-panel
collision count and canvas-overflow count. An old 6 pt PASS is invalid, and a figure-level
minimum does not establish panel-local acceptance.

Matrix panels use colour plus an external legend and source table instead of text over cells. Supported cells can receive a corner mark, outline or another non-occluding symbol. Legends count as text during collision and canvas checks; an out-of-canvas legend fails release even when the axes remain square.

## 6. Information density and restraint

A high-level figure keeps the principal comparison, effect size, sample size, uncertainty and structural location in one reading path. Each analytical panel should expose at least one direct form of evidence: observations, distributions, effect intervals, thresholds, key values or a structural location. Summary bars should normally include point-level values, distributions or intervals; a summary-only bar chart needs a scientific reason why individual values would reduce clarity.

A visually weak `n ≈ 4–6` summary figure is usually under-informative rather than merely under-styled. Add an orthogonal comparison, matched null, repetition level, interval, threshold or sample-level distribution. Do not repair it with extra icons or a saturated palette.

Use short panel titles for the comparison and avoid repeating the figure title in every panel. Let axis labels, direct annotations and legends carry interpretation without restating one another. Colour should retain one stable role, while grids, frames and backgrounds remain low contrast.

When reducing labels, preserve the anchors needed for interpretation: significance thresholds, key residues, principal comparison groups, extremes, sample sizes and structural classes. Source data, the legend and the main text can carry secondary labels.

### 6.4 Sparse sources, coarse rendering and duplicate panels

Sparse source rows and coarse figure design are separate failures. A source with three to
ten substantive rows needs a bespoke geometry that carries the full relationship: a protein
topology track, protocol change from a named baseline, effect-uncertainty lattice, status
matrix, source-to-matched-to-holdout funnel, or short forest with denominators and intervals.
Do not respond to sparse data with a default bar chart, a bare line through a few means or
isolated points. Every small category should expose its comparator, total or denominator,
interval or threshold, and the decisive direct value.

For a field-rich source, inventory the principal numeric columns, category levels, intervals,
controls, thresholds and sample units before choosing a plot. A panel that uses one column
while relegating the rest to the caption is a registered visual simplification. Dense scatter
keeps all individuals and adds hierarchy through transparency, density, split structure,
median, threshold or extreme labels. Forests show intervals, support state and denominators.
Matrices add CI width, support outlines or failure symbols. Sparse protocols show change
from the complete baseline.

One source can support several panels only through a different estimand, transformation,
control or scientific question. A panel that keeps the same columns, transformation and
reading path while changing colour, marker or title duplicates evidence. Record source-reuse
groups, usable numeric fields, implemented evidence encodings, direct labels, fields omitted
from the chosen visual simplification, and separate sparse-source/coarse-rendering decisions
in `panel_information_density_audit.tsv`.

Audit evidence completeness separately from visual completion. Evidence completeness means
the samples, comparator, interval, threshold and denominator are visible. Visual completion
means the primary geometry, reference lines, hierarchy, direct labels and redundant state
encoding serve the reading path. Decorative icons, meaningless gradients, extra hues and
random jitter do not count.

## 7. Audit sequence

First inspect the figure group: title, panel order, scientific question, structural panel, quantitative evidence, legend, alternative text and source-data links.

Then inspect each panel: box aspect, axes, units, sample size, thresholds, legends, colour roles, direct labels and source values.

Finally inspect exports: PNG resolution, PDF availability, SVG parsing, embedded panel letters, browser loading and desktop/mobile layout. Record figure-group typography, panel geometry, wide exceptions and text collisions. Recompute consequential numbers from source tables; colour and typography do not replace statistical review.

The audit record lists figure groups, exports, source tables, panel-aspect exceptions, colour roles, browser results and unresolved items. Release the figure only when manuscript references, legends, HTML headings and source-data links agree.

## 8. Worked acceptance example

The RemoteEffect figure system provides a reusable acceptance check. Figure 4a and 4e remain wide to preserve direct horizontal correspondence between the TetR residue track and three cross-site endpoints. Figure 15, the CDS tracks in Extended Data Figure 4, the 384-well layouts in Extended Data Figures 8 and 9, and the long pLDDT track in Extended Data Figure 13 also use registered wide geometry. Bar, scatter, curve, heatmap, forest, power and model-comparison panels use a near-square plotting box. Extended Data Figure 19 tests the same rule in a 2×2 component-inference figure: the VanR structural map, seven-endpoint component signatures, compound-component detection and sample-depth recovery each occupy one data axis with a 1.0 target box ratio. Extended Data Figure 20 applies the rule to structural component context, a weighted correlation matrix, independent threshold calibration and n=5/8/12 confirmation depth. Extended Data Figure 21 links a structural readout location to selectivity-dependent correlation, component F1 and n=5/8 recovery.

Blue and navy carry the project identity. Comparisons use a restrained set of colour-blind-safe Science-style accents: teal `#009E73`, amber `#E69F00`, vermillion `#D55E00`, reddish purple `#CC79A7` and neutral grey `#7F7F7F`. Ligand comparisons map PA, Per-OH and S-Lim to navy, teal and amber; negative ΔAIC directions use vermillion; LMSF and DAMP reporter channels use teal and reddish purple. Figure legends define these roles.

Each redraw retains `panel_geometry_pre.tsv` and `panel_geometry_post.tsv` and writes separate `panel_aspect_exceptions.tsv` and `figure_typography_audit.tsv` records. Every regular data axis targets 1.0 and remains within 0.9–1.1 after final layout, every wide axis has a written purpose, and colour bars or decorative axes are marked as utility axes. Typography records the smallest, median and largest font sizes, the number of thinned category ticks and all title objects for each figure group. The release check covers text bounds and collisions, 600-dpi PNG, parseable SVG, PDF, embedded panel letters, HTML image loading, desktop and mobile viewports, and the colour descriptions in captions.

## 9. Panel-local regression protocol

Use this section when a figure has already failed visual review or when an earlier audit called a crowded panel acceptable. Audit each panel separately before auditing the assembled plate.

### 9.1 One panel, one data plot, one visible evidence path

Count `Figure.axes` and child axes after rendering. Each panel must contain exactly one data plotting area. A detached strip above the main plot, a visual inset, a second mini-histogram or a small matrix embedded inside a larger panel is a second plot even when it is drawn without `inset_axes`. Share one coordinate system when multiple measurements are scientifically layered; otherwise move secondary evidence to a separate panel, caption or source table.

A panel may contain several aligned tracks only when all tracks use the same positional coordinate and read as one continuous evidence object. P1D and P4D/P4F may contain aligned residue-position layers, but they must not contain a separate miniature chart. P1A must remain one horizontal cohort-coverage chart; do not add a detached top strip to show a second cohort summary.

### 9.2 Reserve title, data, label and legend bands

Allocate four independent vertical regions inside each panel cell:

1. panel letter and title band;
2. square data box;
3. x-axis label and tick band;
4. external legend/direct-label band.

Do not solve a collision by shrinking type. At the 10 pt project floor, long y-category labels, legends and titles require more physical space. Wrap long labels, shorten condition codes, move sample counts and exact values to the caption/source table, or enlarge the cell. A legend from row 1 must not enter the title band of row 2. A top y tick must not touch a title. A lower-left y tick must not touch the x-axis title.

Short legend entries should use one compact row when possible. A multi-row single-column legend is not a valid default for a square panel because it creates a tall footer and can overlap the next row. Direct annotations are not a place for sample sizes, exact intervals and secondary qualifications that belong in the caption.

### 9.3 Use one physical axes lattice for equal-role panels

For regular three-column figures, define one final axis side length for all three columns. Position axes by explicit millimetre coordinates or an equivalent layout unit. Measure the final axes boxes after `fig.canvas.draw()`, not the cell rectangles. Equal-role panels must differ in rendered area by no more than 5%; normally every regular panel in one figure has the same side length. Record row counts and require `[3, 3]`, or `[3, 2]` for a five-panel plate.

A wide track is registered only for a continuous long coordinate that would lose position correspondence in a square view. A wide track must share the row height with its square neighbour. A missing property or an automatic `set_box_aspect(1)` centred in a much wider cell is not a wide exception. Audit both minimum and maximum gutters. A horizontal gap should contain at most the longest neighbouring y labels, axis label and a designed gutter; an unexplained central band larger than this is a failure even when axes do not overlap.

### 9.4 Parse panel identifiers exactly

Do not dispatch panel-specific layout with broad prefix tests. `panel_id.startswith("P1")` matches `P10` and `P11`, and `startswith("P1")` style routing can silently assign P1 geometry to P10/P11. Use an exact regex such as `^P1[A-F]$`, a parsed figure number, or an explicit mapping. Regression-test the largest numbered panels in the same run as the short identifiers.

### 9.5 Audit final text geometry and data occlusion

For every visible text object, compute its final window bound after fonts, legends and axis limits are set. Record:

- text-to-text overlap count;
- text-to-canvas overflow count;
- text-to-mark occlusion count;
- collision examples with both boxes;
- final minimum font and font role.

An empty-text list is not evidence of a clean panel. Legends count as text; tick labels and offset text count as text. A text box that intersects an unexplained data mark is a collision even when an opaque background would visually hide it. If a corner tick and axis label are close, increase the label band or wrap the label; do not shrink either object.

Audit every artist type present in the panel. Scatter offsets are insufficient when intervals are drawn as `LineCollection` objects, paired observations as connector collections, gates as bar patches or identity relations as individual lines. Test each complete line segment against the text box rather than checking endpoints only. A title placed over the middle of a zero line or connector can be missed by a vertex-only audit. A collision helper that omits line collections, bar patches or error-bar artists has not established zero occlusion. Unsupported collection types must stop release and trigger an audit extension.

### 9.6 Verify the actual HTML and raster artifact

Inspect the current HTML `img` source or embedded data URI and confirm that it corresponds to the latest renderer output hash. A stale PNG or SVG is treated as a failed revision even when the working renderer is correct. Rerender each panel as PNG/PDF/SVG and each plate after the final layout change.

Measure the final raster, not only nominal axes:

- content width and height extent at least 0.95;
- largest internal blank row/column band no more than 0.14;
- 1-2% outer padding after cropping;
- no ink at an unauthorized edge;
- visually check the contact sheet and desktop/mobile HTML.

When an internal empty band exceeds the limit, delete only pixel rows or columns containing no ink. Never move, rescale or crop data, text, legends or structures. Re-run text, aspect and occlusion checks after compaction. A P6 structural panel may use a registered square composition, but the molecular-ink content extent and blank-band gates still apply.

Audit the outer content box independently from the largest internal gap. `bbox_inches="tight"` does not guarantee a compact raster when its save padding is oversized, and the internal blank-band metric can pass while a figure retains more than 5% unused border. Inspect both width and height fractions, reduce fixed save padding to the registered 1-2% margin, or remove only fully blank outer rows and columns. Do not shrink an axes or relabel a crop as a wide-layout exception to satisfy this gate.

### 9.7 Release checklist for every panel

Before accepting a plate, confirm all of the following:

- exactly one data plot and no detached mini-plot;
- panel letter/title separate from axes and ticks;
- panel letter occupies the upper-left blank, at least `4 mm` above and approximately
  `0.20 × panel width` left of the data box;
- panel title is horizontally centred over the data box, single-line and bold;
- first row contains exactly three panels and the assembled plate records `[3, 3]`, or `[3, 2]` for a five-panel figure;
- axis labels, tick labels, legends and direct labels inside the canvas;
- zero text overlap and zero text-mark occlusion;
- regular axes square within 0.9–1.1 and equal-role areas within 5%;
- gutters justified by label space, not phantom whitespace;
- horizontal and vertical complete panel-boundary gaps both fall within `0.38–0.42 × panel
  width`, are measured after final tick suppression, and remain unchanged during save;
- adjacent boundary pairs are checked independently in both directions; a normalized
  one-row legend/footer band prevents row alignment from masking a larger vertical gap;
- composite export preserves designed internal gutters and crops only blank outer margins;
- legends sized before final export and not stacked into the next row;
- long category/condition labels wrapped or abbreviated with definitions in caption/source data;
- alternating categorical labels checked as one plate-level text field, not only inside their own axes;
- two-line row abbreviations rejected when their bbox enters the adjacent row, and diagonal category labels replaced with full vertical labels or a short horizontal legend when 10 pt spacing cannot separate them;
- effect, uncertainty, sample distribution, null/control, predictive holdout and transfer/registered-condition evidence use distinct panels when those layers exist;
- scatter, line collections, interval artists, bar patches and identity lines all enter the text-mark occlusion audit;
- final PNG compact under the 0.95/0.14 rules;
- HTML references the current artifact and both viewport checks use that artifact.

## 10. Final HTML typography and fixed-cell regression

Validate source point size and rendered point size together. Compute effective pt as
`raw_pt × save_dpi / 72 × css_width / raster_width ÷ (96 / 72)`. Record every role
in `effective_font_size_audit.tsv`; a nominal 10 pt label that falls below 10 pt in
the rendered report fails.

Use one physical canvas family for each grid. Keep axes width and height identical,
freeze complete panel cells, and measure the union of axes, letter, title, ticks,
axis labels, direct annotations and legends. Never use absolute
`set_label_coords(-0.55/1.55)` placement to push long labels into a gutter. Abbreviate
comparison names in the tick rail, with the full estimand in the axis title, caption
and source table. Write `column_cell_width_audit.tsv` and `panel_role_audit.tsv`.

Reject duplicate estimands. A panel that only changes plot type, threshold, seed or
colour has the same inference role. Replace it with sample-level pairing, denominator
anatomy, independent validation, matched background or a failure-state decomposition.

For multi-panel figures with designed 0.38–0.42 w complete-cell gutters, allow a
full-image internal blank row or column band up to 0.18; isolated structure rasters
remain at 0.14 because title and label bands are not part of their declared gutter.

## 11. v1.2.6.3 legend, tick and significance regression

**Legends never cover data.** Legends, direct labels and series labels all enter the
final data-occlusion audit. Prefer one-word abbreviations; keep the full estimand in the
caption and source table. Use direct endpoint labels only for at most four series and only
when a true right-side corridor exists. For more series, or when values crowd the edge,
place a horizontal legend below the title or a one-column legend in a reserved right
corridor. Store direct-label positions as axes fractions and translate the whole label
stack together to preserve minimum spacing. Per-label clipping reintroduces collisions at
the frame boundary. Record `legend_data_occlusions` and `zero_legend_data_occlusion`.

**Never remove an axis title to solve a collision.** Resolve crowding through ticks,
abbreviations, wrapping and label padding. Numeric axes normally retain four to six ticks.
Write categorical ticks as one word or a short two-word phrase. Rotate at 45° only when
labels are genuinely long or multiline and at most four labels remain visible. For denser
category axes, use short registered abbreviations and retain two to four evenly spaced
labels selected from rendered bounding boxes. Do not use the unstable pattern “every other
tick plus the forced last tick”. Preserve at least two interpretable ticks per axis and
record `axis_tick_completeness` and `all_axes_have_visible_ticks`.

**Derive the panel header from the rendered top tick.** Anchor the title and letter above
the full bbox of the top y tick, then add text height and at least 4 mm clearance from the
axes top. A fixed header ratio is insufficient. Re-measure after final panel scaling.
Keep the title centred, bold and single-line; keep the letter in the outer upper-left of
the complete panel cell. Axis titles must never appear in `sparsified_tick_labels`.

**Reserve range headroom.** Linear-axis extrema must not touch the frame. For non-negative
data, keep the zero baseline and add about 10% headroom above the observed maximum; add
about 4% below when required. Expand log axes multiplicatively. For near-saturated
proportions, show baseline-relative change, recovery gain or completion gain while retaining
the denominator, direction and zero reference.

**Use significance only for real comparisons.** Bars, boxes and violins receive effect
markers only for the same grouping, independent unit, denominator and contrast direction;
the bracket height derives from the data span, and the label reports adjusted q or a
predefined P value. Forest plots place q values in a separate column outside the plotting
area. When no formal comparison or paired unit exists, keep the panel descriptive. Scatter
points use about 0.50 alpha; violin fill uses about 0.28 and box fill about 0.38 so that
distribution shape, summary and observations remain simultaneously visible.

## 12. v1.2.6.4 star notation and legend layout

**Use conventional stars inside figures.** `*` marks q<0.05, `**` q<0.01, `***`
q<0.001, `****` q<0.0001 and `n.s.` marks q≥0.05. Do not print `q=0.349` inside a plot;
keep the exact q value, adjustment method and comparison key in the caption and source
table. Forest plots use an outside star column.

**Pair continuous effects with intervals and stars.** Draw the real 95% CI as a
semi-transparent band and place stars on the matching adjusted test. Repeating a 20 px-wide
star label at every adjacent point causes collisions. For one continuous significant run,
label the first, middle and last representative point; always add state changes and the
last point. Never solve crowding by deleting tests or moving stars into the tick rail.

**Prefer a horizontal legend above the data.** After registered abbreviation, try a
multi-column horizontal legend below the title and outside the data rectangle. Use direct
labels only when the header really exceeds the complete panel width, and a right-side
column last. Encode state transitions as `C→C`, `T→C`, `T→T` and `B→B`, with full names in
the caption. Dynamic title and letter anchors sit above this header legend.

**Audit every panel after a full redraw.** Check legend mode, abbreviated labels, axis
titles, star thresholds, CI bands, header/tick clearance, significance columns, data
occlusion and final CSS font size. A right legend that could fit above is a failure; q text
inside a plot is a failure; colliding repeated stars are a failure.

## 13. v1.2.6.6 projection extent, equal units and structural cartoons

**Show the complete projection.** Limits for an embedding or projection panel come from the
full current data extent with at most 6% padding, never from a previous round's values. Any
point outside the axes is a failure; record clipped_point_fraction = 0 together with the
data minimum and maximum. If a legend or annotation forces a narrower view, split the panel
instead of hiding points.

**Use equal x/y unit length for projections.** PCA, t-SNE and UMAP panels set equal aspect
and pad the shorter range so both spans match. The axes box remains square
(height/width 0.98-1.02) and a unit in PC1 equals a unit in PC2 on the page. Ticks are
declared explicitly for each projection instead of relying on an automatic locator that can
leave stale labels after a limit change.

**Cartoon first for fold evidence.** Panels that claim a fold class use ribbon/cartoon
geometry, not a surface-only render. Helices use rounded ribbon style; sheets keep arrow
ends. Non-focal chains, loops or contexts are grey and 20% transparent (about 80% visible);
the focal fold stays opaque and saturated. Surface renders remain acceptable only when the
panel's claim is about shape or pocket, and the caption must say so.

**Annotate inside a reserved label band.** Each structural tile reserves a white band for a
short class label or TM bucket at 10 pt equivalent; labels never sit on molecule ink. The
caption expands the abbreviation into architecture name, TM value and source identifier.
Bake labels only when the renderer cannot produce auditable text, and record the font size in
source pixels.

**Validate the structure file before any cartoon render.** Predicted-structure writers may
left-justify element symbols and treat atom-name prefixes as elements, so CA is read as
calcium. Check that columns 77-78 hold a right-justified element, that the number of guide
atoms equals the number of C-alpha atoms, and that loading the file returns a non-empty FASTA
sequence. If any check fails, rewrite the element columns from the atom name, record source
and corrected SHA-256, and rerender. A cartoon that renders blank or as a thin line is a data
problem before it is a style problem.

## 14. v1.2.6.7 evidence density and visual finish

**Every analytical panel carries at least three evidence layers.** Choose from individual
observations (strip or jitter), a distribution (violin, box, hexbin, density contour), a
central estimate with interval (median/mean plus CI), a reference or threshold line, an
effect size, a cross-condition contrast, and a structural annotation. A panel with only
mean bars, or one line without a band or observations, fails. Record the layer count in the
panel audit; three is the floor, four is the target for main figures.

**Two-category panels need a companion distribution.** A two-bar comparison is allowed only
as a control or validation panel when the same figure already shows the distribution of the
same variable; otherwise add the observations and an interval. A single-series curve must
add a confidence band, individual points, or an event rug.

**Use the third dimension instead of repeating the same chart.** With n >= 30 and at least
two categorical variables, encode one variable on the position axis, one on colour or marker,
and the response on size, coverage or a second summary inside the same panel. Three stacked
bars that differ only by algorithm, rule and environment are a failure; at least one of them
must show a distribution, a contrast or a mechanism layer.

**Reference and uncertainty are part of the panel.** Add threshold, zero, identity or
baseline lines; define the interval in the caption; do not leave a floating mean without a
dispersion estimate. Forest plots keep the null line and exact intervals.

**Visual finish is auditable.** Use semantic fills with an alpha hierarchy (about 0.15 for
bands, 0.55 for observations, 1.0 for estimates), never matplotlib default black whiskers or
edges (#000000 is an unregistered colour), keep tick lengths and frame weights consistent,
and remove panels that are mostly empty. A panel that survives only when enlarged is a
failure at the final CSS width.

**Figure-level rhythm.** Each row has a distinct evidence role (occupancy, composition,
structure, outcome, mechanism, control). Repeating the same bar chart with only the dimension
swapped is a failure even when every individual panel is technically valid.

## 16. v1.2.6.8 universal data-extent gate

**Every quantitative panel displays the complete data extent on both axes.** Limits are
computed from the current data with a small margin; hard-coded limits copied from an earlier
dataset version fail. This applies to all marks that carry data: scatter points, bars, error
bars, CI bands, violin bodies, rugs, regression lines and density bands.

**Threshold views need a full-range companion.** A panel that deliberately starts at a
threshold (for example TM >= 0.2) must either extend to the full data range or show the full
range in the same panel. A zoomed view without a full-range companion fails.

**Audit in value space, not by eye.** Compare data minima and maxima with axis limits on
sorted limits (inverted axes) and on the original scale (log axes); check raster images and
matrices with their half-pixel extent. Ignore legend proxies and default collection offsets;
count explicit scatter offsets and line vertices. Record clipped-point counts and relative
overshoot per axis in a panel-extent audit table, and require all panels to pass.

**After extending a range, reset tick locators.** Extending a limit can leave auto-locator
ticks outside the visible view; those labels still enter text-collision checks. Set explicit
ticks inside the new range.

**Lessons from the PGv3 audit.** The common causes were stale hard-coded y-limits, threshold
views that hid zero-valued endpoints, long tails in control distributions, CI upper bounds
outside the mean range, natural-sequence composition reaching 1.0, and KDE bodies clipped at
the frame. Inverted and log axes plus default collection offsets generated false positives,
so the audit must be geometry-aware rather than a visual check.

## 17. v1.2.6.8 addendum: visible bodies, markers and raster completeness

**A data-extent check that reads only scatter offsets is insufficient.** Distribution
bodies (violins, KDE contours, CI bands, box whiskers) are drawn by PolyCollection and
LineCollection paths, not by PathCollection offsets. Audit every data artist path after the
data transform, or the plate can pass while the visible bodies are cut.

**Violin bodies must not be flat-cut at the data minimum or maximum.** The default
matplotlib violin evaluates the KDE only inside the observed range, producing a flat cap at
the extreme observation. Extend the kernel grid beyond the data by about 1.5 bandwidths,
draw the extended body, then set the axis range from the body extent plus a margin. A flat
violin cap is a failure even when every observation is inside the frame.

**Contours and CI bands need a kernel margin.** Density contours evaluated only between the
data minima and maxima terminate at the data boundary. Extend the grid by about 6% beyond
the observed range and expand the axis to the resulting contour extent.

**Markers centred on a limit are half-clipped.** Points at exactly 0, 1 or a threshold touch
the spine. Add a marker margin of about 2–4% of the axis span so the full symbol is visible.
Apply the same rule to category labels and bars touching the frame.

**Audit the raster, not only the vector geometry.** After export, inspect the rendered panel
image at the HTML display width for ink that touches or is cut by the axes frame. The final
HTML must serve versioned raster URLs or no-store headers; a regenerated PNG with an
unchanged URL can be hidden by the browser cache and read as a stale, truncated plate.

**Case study (PGv3, 2026-11-25).** A first geometry pass reported zero clipped panels while
readers still saw: (i) Fig. 2b violins flat at +-0.006; (ii) Fig. 2c contours ending near
-0.1; (iii) Fig. 2d/g markers on 0 and 1; (iv) Fig. 4b violins flat at the 50% data maximum;
(v) Fig. 4h contours and points on 0/1; (vi) Fig. 4i points too small. The causes were
data-only audit logic, default violin truncation, contour grids limited to the data range,
no marker margin, and unversioned raster URLs. The fixes were extended KDE bodies, extended
contour grids, marker margins, a full artist-geometry audit, and versioned image URLs.

**Rule.** The extent gate passes only when the union of all data-artist paths, including
distribution bodies and CI bands, lies inside the visible axes box with a small margin, and
when the rendered raster confirms the same at final display width.

## 18. v1.2.6.8 reflow addendum

- Reflow addendum: a log-scaled axis can inflate the measured row pitch and leave a large internal blank band even when every artist is inside the axes. If a plate develops an unexplained blank band, test the log axis; for a narrow dynamic range use a linear axis, or reserve enough explicit vertical space and recheck the content-extent audit.
