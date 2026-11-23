# SEAL supplementary-figure production standard

Version 1.1.0; updated 2026-11-18. Read this file in full before creating, redrawing or auditing any SEAL main or supplementary figure.

## 1. Scope

This profile applies to all 28 SEAL Supplementary Figures and every subsequently regenerated panel. It also records the author-approved decisions for main Figures 1–4. The later author instruction overrides generic figure defaults when they conflict.

## 2. Mandatory typography and axes for every supplementary figure

- Ordinary text: 8 pt. No essential annotation may remain at 4–6 pt.
- x/y-axis labels and panel titles: 10 pt.
- Panel letters: 10 pt bold, with no overlap with data, ticks, legends or captions.
- Legends and direct labels: normally 8 pt; essential values must remain legible without hover.
- Axis and major-tick strokes: 0.4 pt. Use rounded line caps and joins.
- Major grid lines: no heavier than 0.35 pt and visually subordinate to the data.
- Regular analytical data boxes: near-square with `plot_box_width / plot_box_height = 0.9–1.1`; use `set_box_aspect(1)`.
- Resolve crowding by changing the canvas, grid, wrapping, direct-label placement or tick density. Do not shrink text to preserve an overcrowded layout.
- Place annotation text outside the point field, in a margin or ordered label stack; do not cover data points with category or cluster names.
- Every SVG must retain editable text; no text may be converted to outlines.

Apply these rules to all supplementary figures, not only the figures being actively redesigned.

## 3. Colour and point-visibility rules

- Use the project colour identity and the exact rendered colours in legends. A legend swatch must not look substantially paler than the plotted marks.
- Core annotated observations use full-saturation marks with `alpha = 1` unless transparency is necessary to resolve overplotting. Context or unannotated observations use a documented neutral grey.
- Earlier project base tokens remain reference colours: red `#9B4B4B`, light blue-grey `#6C839C`, blue `#3E7A9E`, dark blue `#4A5E87`, green `#5A9199` and grey `#939393`.
- The current main figures use the measured final palette: slate `#536F89`, coral `#B96359`, teal `#438E7B`, purple `#8179A8`, ochre `#A97936`, supplementary blues/greens and neutral greys. When matching the final main figures is the explicit requirement, these measured colours take precedence over the historical base tokens; record any mapping.
- Do not silently alter category colours across figures. Keep biological classes consistent across the main figure, subatlas, structure overlay, legend, caption and HTML.
- Data points must be large enough to read at the final publication size. For the 600-dpi SEAL supplement profile, benchmark seed points use `s >= 12`; family subatlas points `s >= 8`; structure-summary points `s >= 16`; coloured 20,420-protein overlays `s >= 10`.
- When a family subatlas was judged too small in review, enlarge its point areas approximately fourfold relative to the preceding draft or adjust the layout so visibility is equivalent; do not preserve microscopic marks merely because the source code already had a point size.
- Marker shape and direct labels provide redundant identity in addition to colour.

## 4. Distribution figures

- When seed-level or observation-level distributions exist, show a violin distribution together with all observations and a central mean/median and interval where appropriate.
- Do not replace a distribution with a summary-only bar or a mean point.
- For the SEAL cross-model benchmark, show the 20 split-seed distributions for every displayed metric.
- For class precision, recall and F1, recompute per-seed per-class values from the same predictions used for the confusion matrices; display all 20 values as points and summarize them with violins and means.
- Name the evaluation unit: split seed, protein, ORF or independently trained model. Repeated seeds quantify resampling, not independent biological replication.

## 5. Cross-model benchmark and ESMC

- Do not omit ESMC when evaluating the five-family protein benchmark.
- ESMC-6B is a current-input 2,560-dimensional extension. Evaluate it on the same frozen 1,418 labels, row-wise L2 normalization, cosine distance, 20 stratified splits, 10-NN rule, balanced K-means sampling and bootstrap procedure.
- Never imply that ESMC dimensions align one-to-one with the 1,024 ProstT5, ProtT5 or ProTrek dimensions.
- Distinguish the historical three-model benchmark from the current-input ESMC extension in captions and source notes.
- Keep the exact input hashes, accession matching, split seeds, predictions, per-seed metrics and bootstrap intervals in Source Data.

## 6. Human proteome projection figures

- Where the figure is described as a 2w human-proteome projection, fit and show all 20,420 current-input Swiss-Prot proteins, not only the 1,418 labelled benchmark cohort.
- Plot the 19,002 proteins outside the five benchmark labels as a light-grey context layer. This dense layer may be rasterized in SVG/PDF at 600 dpi to control file size.
- Overlay all 1,418 labelled proteins as editable vector marks using saturated category colours and distinct markers.
- Directly label the categories and report their counts. Use the same categories and colours in every t-SNE/UMAP panel.
- Keep the grey context in a separate raster layer; axes, labels, legends and coloured observations remain editable vectors.
- For parameter sensitivity, display all prespecified values without selecting the visually most separated result.

## 7. Main Figures 1–4 and Figure 2 atlas/subatlas requirements

- Preserve the four author-approved main figures. Do not silently redraw or replace them when the request concerns supplementary figures.
- Main Figure 1 is the approved conceptual/application design. If the complete author-approved version is restored from an earlier manuscript, use the exact embedded artwork and its original crop rather than a reconstructed approximation.
- Preserve the approved central composition of Figure 2: a full 205,228-entry 3D t-SNE atlas, eight clearly separated colour-coded regions, inner family-specific subatlases and outer representative structures.
- Main atlas deliverables include both t-SNE and UMAP, with t-SNE as the primary view; provide 2D and 3D versions, axes-on and axes-off exports, multiple camera views, and a 3D view in which all eight clear categories are near the visible outer edge.
- Show all points without clipping. Do not use an auto-crop that removes extreme observations.
- Unassigned proteins are light grey. The dense grey layer may be rasterized; coloured annotations and editable text remain vector.
- When the same family occurs in several peripheral islands, label a representative exterior instance and avoid repeating the family name across the whole map. Split duplicated families into separate, clearly identified subatlas groups where required. Preserve multiple GPCR-related regions when the approved design uses them.
- The eight highlighted families must be clear, spatially coherent groups. Do not include a family label that spans many unrelated islands or include significant isolated outliers as one of the eight primary groups.
- Use a reproducible clustering/selection procedure and documented criteria; do not tune the selection standard merely to produce a preferred visible result.
- Use true protein-family/Pfam annotations for subatlas legends and colouring, not generic local cluster IDs as biological labels.
- Within a family subatlas, annotated proteins take the family hue (or a documented deeper shade); proteins in the regional subset without a retained annotation stay light grey. Do not assign biological meaning to a generic cluster colour.
- Each subatlas is independently computed from its own protein subset and uses a strictly equal x/y visual scale. Make all subatlas points large enough to distinguish at print size.
- For every selected family, export the ten structures nearest the family centre as FASTA for structure prediction. In addition, the project has used ten predicted structures per family; confirm the exact cohort before making new predictions.

Main-figure evaluation must also provide a clearly separated main-family atlas and independent family-level analyses; broad umbrella annotations such as protein kinase cannot substitute for a visually coherent family when the kinase label spans multiple distant subfamilies.

## 8. Structural-overlay figures

- Start from a representative reference structure and align four to five representatives on a defined shared core.
- The project may provide ten predicted structures per family; analyze all available structures, then select the four or five with the most convincing shared-core alignment for display.
- The primary “all five, whole chains – front” view shows whole-chain cartoons.
- Display one saturated reference cartoon plus other representatives as aligned semi-transparent cartoons that remain visible.
- Hiding irrelevant flexible loops, disordered regions and very low-pLDDT segments is allowed and must be recorded; the core structural region is the object of comparison.
- Show cartoons only. Do not show atoms.
- Confirm that the displayed content is the intended protein core, that at least four aligned cores are visible and that the same family colour identity used in the atlas is retained.
- Do not use stacked transparent surfaces when transparency accumulation would make overlap darker or ambiguous.
- Maintain the exact atlas family colour in the reference cartoon and structural panel. Structure overlays are matched to the corresponding subatlas rather than treated as standalone decoration.

## 9. Export, rasterization and editability

- Deliver SVG, PDF and 600-dpi PNG for each final figure; all requested JPG/HTML deliverables must also be generated.
- Main Figure 2 must additionally include t-SNE and UMAP, 2D and 3D, multiple camera views, and axes-on/axes-off variants in JPG/SVG/HTML as applicable.
- Every supplementary figure must have JPG plus SVG and an HTML-ready preview/link in addition to PDF/PNG where the release requires it.
- Every analytical panel and panel letter must exist as an independent editable SVG export where the source artwork permits it.
- Only dense, unannotated grey background layers may be rasterized. Point distributions, highlighted observations, axes, labels, legends and statistical marks remain vector.
- Remove stale shared/panel SVG files before publication so that every HTML link points to an existing current panel.
- Check that all page images load and that no pane is empty or clipped.
- Do not upscale a raster image and describe it as newly recovered resolution. State native dpi, crop and interpolation provenance.

## 10. Mandatory audit before release

For every one of the 28 supplementary figures:

- minimum text ≥8 pt;
- axis labels/titles =10 pt;
- panel letters =10 pt;
- axis/tick line width =0.4 pt with rounded caps/joins;
- regular data-box ratio 0.9–1.1;
- zero text collisions and zero text outside the canvas/page;
- 600-dpi PNG, parseable SVG and one-page openable PDF;
- caption number, panel letters, sample size/denominator and source records agree;
- every declared panel has a current independent SVG;
- no stale, hollow or empty HTML image/panel links;
- browser rendering checked at desktop and mobile widths.

Run figure-by-figure, SVG/PDF and source-data audits after the final regeneration. Record image-loading, panel coverage, source hashes and any unresolved exception. Do not report a figure as final from visual inspection alone.

## 11. Per-panel deliverable, label placement and release gate (1.1.0)

### 11.1 The panel is the unit of delivery

Every declared panel must be exported as its own editable SVG that opens standalone and carries its own panel letter, axis labels, tick labels, marks and annotations. A composite assembled from panels must be reproducible from those panel exports. A crop of the composite raster, a flattened image, or a panel that only exists inside the composite is not a deliverable.

For each figure deliver: composite SVG, vector PDF, 600-dpi PNG, 600-dpi JPG, one SVG per panel, one SVG per shared legend or scale bar, the caption, a panel-definition record and an audit record.

### 11.2 Automated checks are screening only

Bounding-box collision counters miss real defects: a panel title can sit on the previous row's tick labels, and a category label can sit inside the point cloud without tripping a text-to-text test. A reported collision count of zero is not evidence of a clean figure. Every figure must be opened as an image at final size and inspected panel by panel, and the inspection must be recorded.

### 11.3 Label placement

- Category, cluster, region and site labels are placed in a margin label stack with leader lines when anchors are close.
- No label may cover a data point, an axis, a tick label, a panel title, a panel letter, a colour bar or another label.
- Offsets are computed from each panel's own anchor geometry. A single hard-coded offset applied to every panel is a defect when anchors differ.
- When two anchors are closer than the label height, fan the labels vertically and draw a short leader to each anchor.
- Direct labels may be omitted for a category that the legend already identifies unambiguously, provided no essential value becomes hidden.

### 11.4 Row and column budgets

- Reserve a separate band for the panel title and panel letter above each data box, and a separate band for x tick labels and the axis label below it.
- The vertical gap between rows must exceed the height of the previous row's x tick labels plus the next row's title band. Setting equal axes alone does not prevent collisions.
- Wide exceptions, colour bars and legends occupy reserved margins, never data area.
- Use one numeric notation per axis; do not mix decimal and scientific forms, and keep shared exponent text at 8 pt or above.
- When a row would collide, increase canvas height rather than shrinking text or dropping axis labels.

### 11.5 Release gate for the 28-figure set

The set is released only when, in one regeneration pass:

- all 28 composites and every panel SVG are regenerated from current source data;
- every panel SVG opens, contains live text, and matches the composite;
- 8 pt / 10 pt / 10 pt / 0.4 pt typography and 0.9-1.1 regular data boxes are verified on the regenerated files;
- the visual inspection of every figure is recorded with the defects found and fixed;
- no stale panel, caption or HTML link remains;
- the manuscript citations, captions, counts and source records agree with the delivered figures.
