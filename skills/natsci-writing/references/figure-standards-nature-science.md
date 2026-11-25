# Figure standards for Nature and Science

Version 1.2.5; updated 2026-11-24. Read with the parent SKILL.md and with figure-design-and-audit.md (the author's project geometry and colour overlay). Journal specifications below were checked against Nature author guidance in November 2026; confirm the current target-journal instructions at submission because production rules change.

## 1. A figure is one claim

Write the figure's claim as a single declarative sentence before opening a drawing program. If the sentence needs "and", the material is probably two figures or one figure plus supplementary panels.

Anatomy of a top-journal figure:
1. **Context panel** — the biological object, system or design, only as much as needed to read the rest.
2. **Primary comparison** — the measurement that establishes the claim, with the comparison group visible.
3. **Mechanistic or structural evidence** — where the effect acts, if the claim is mechanistic.
4. **Robustness or independent validation** — an orthogonal measurement, held-out set or perturbation.
5. **Model or summary** — a compact conceptual panel, only if it adds information the data panels cannot.

Not every figure needs all five. Every figure needs panels that are ordered by the reader's reasoning, not by the order of the experiments.

## 2. Journal specifications

### Nature
- Widths: 89 mm (single column), 183 mm (double column), 120–136 mm (1.5 column). Page depth 247 mm.
- Typeface: sans-serif, Helvetica or Arial, identical across all figures. Greek letters in Symbol font; amino-acid sequences in one-letter code, Courier.
- Text: panel letters 8 pt bold, upright, lowercase a, b, c. All other text maximum 7 pt, minimum 5 pt.
- Lines: 0.25–1 pt at final printed size. Do not rasterise or outline line art or text.
- Raster: 300–600 dpi at final size; TIFF or layered PSD preferred; JPEG only at maximum quality. RGB.
- Vector: EPS, PDF or AI preferred; editable, unflattened layers where possible.
- Colour: RGB, distinct colours with comparable visibility; avoid red–green contrast; recolour fluorescence images to accessible combinations (for example green–magenta).
- Figure length: 4–6 main display items for a typical Article; each with a short title and a legend.

### Science
- Widths: 55 mm (single column), 120 mm (1.5 column), 183 mm (double column).
- Typeface: Helvetica or Arial; consistent within the figure.
- Text: 5–7 pt at final size; panel letters uppercase bold A, B, C.
- Raster: at least 300 dpi for photographs and 600 dpi for line art and combination art; TIFF, EPS or PDF; RGB.
- Vector: PDF, EPS or AI preferred; keep text editable.
- Colour: RGB; colour-blind-safe; avoid red–green encoding; use redundant shape/line encoding for essential categories.
- Figure length: typically 4–6 main figures for a Research Article, 3–4 for a Review.

### Practical consequence
A 55 mm Science column cannot hold a 12-panel composite; use 120 mm or 183 mm and design the panel grid before plotting. A Nature double-column figure is 183 mm wide at 300 dpi = 2,161 pixels; at 600 dpi = 4,323 pixels. Set canvas sizes in millimetres, not arbitrary inches.

## 3. Panel construction

**Data panels**
- One message per panel; the panel title (when used) states the comparison, not the method.
- Axes labelled with quantity and unit; shared axes only with a clear note; identify any panel with a changed scale.
- Show distributions: points, box plots, violin plots or intervals. A summary bar without points needs a reason in the caption.
- Direct labels on the compared groups; a legend should not force the reader to scan back and forth.
- For small n, show every point. For large n, show the distribution and the summary statistic.
- For dose, time and perturbation series, show the full series in one panel rather than several near-identical panels.
- For model comparisons, show baseline and proposed model on the same scale, with uncertainty and the evaluation unit.

**Structural panels**
- Whole view for orientation, crop for mechanism; label the residues, states or interfaces referred to in the text.
- State whether the structure is experimental, predicted or schematic; give PDB/EMDB identifier and resolution in the caption.
- Use a restrained colour scheme: one colour per state or chain, neutral context; avoid rainbow colouring of continuous variables unless the scale is meaningful.
- Pair the structural panel with the quantitative panel that measures the same object; keep numbering and colour consistent.

**Imaging panels**
- Scale bar in every micrograph; state modality, channel colour map, exposure/brightness adjustments and the representative-image criterion.
- Show the number of independent experiments and the quantification in a paired panel, not only the representative image.
- Crop honestly: show enough surrounding context to identify the structure; disclose any non-linear adjustment.

**Sequence and alignment panels**
- Monospace one-letter code; highlight positions referenced in the text; include a consensus or conservation track where relevant.
- Do not encode essential categories by colour alone; use labels or symbols.
- For long tracks, a wide panel is appropriate; register the exception.

**Model and workflow panels**
- A workflow panel earns its space only if it explains a design decision or a data dependency; otherwise move the workflow to Methods.
- Model diagrams should show inputs, outputs and the evaluated quantity, not the software stack.

## 4. Caption grammar

A Nature/Science caption is a small argument with five parts:

1. **Title sentence.** Declarative claim, one line, no method inventory.
   Example shape: "Fig. 2 | Family-specific embedding dimensions separate GPCR subfamilies."
2. **Panel walkthrough.** "a, ... b, ... c, ..." Each panel: what is shown, the comparison, the condition. Do not repeat the title.
3. **Statistics.** n, definition of n, centre and dispersion, test, P value, correction. State "two-sided" where relevant.
4. **Symbols and abbreviations.** Define only non-obvious encodings; colours that are already meaningful need no definition.
5. **Credits, permissions and scale bars.** "Created with BioRender.com", "Adapted from ref. 12", scale-bar length.

Working example (schematic, not from a paper):

"**Fig. 3 | A sequence-only model recovers family-specific structural constraints.** **a,** Overview of the evaluation: proteins from 34 Pfam families were split by family into training and held-out sets. **b,** Per-family accuracy of the model (blue) and the profile baseline (grey) on held-out proteins. Each point is one family; bars show median and interquartile range; n = 34 families. **c,** Difference in accuracy between the model and the baseline, ordered by family size; the dashed line marks zero. **d,** Residues with the largest predicted effect for family PF00001 mapped onto the experimental structure (PDB 1ABC); colour indicates effect size. **e,** Agreement between predicted and measured effects across 128 mutations (Pearson r = 0.61, two-sided P = 2 × 10⁻⁴)."

Rules:
- The title is a claim, not a label ("Model performance" is a label).
- The caption defines the evaluation unit before any percentage.
- Panel letters match the figure exactly; do not use letters that are not present.
- The caption states the statistical test once, not in every panel.
- Captions for Reviews are shorter (80–150 words) and may omit statistics when the figure is conceptual.

## 5. Statistical display

- Error bars: define as s.d., s.e.m., 95% CI or IQR in the caption. "Error bars" alone is incomplete.
- Report the test, the test statistic where space allows, the degrees of freedom for small samples, and whether the test was one- or two-sided.
- For multiple comparisons, name the correction family (for example, Benjamini–Hochberg across 34 families) and report adjusted values.
- For model comparisons, report effect size with uncertainty, not only P; a small P value with a negligible effect is not a result.
- Do not use significance stars as the only encoding; show the distribution and effect size.
- For benchmark panels, keep the metric definition and the evaluation unit constant across panels; a leaderboard without uncertainty is not evidence.
- For representative images, state the number of independent experiments and how the representative image was chosen.

## 6. Typography, colour and accessibility

- Type hierarchy: panel letters 8–10 pt bold; axis labels 7–8 pt; tick labels 6–7 pt; annotations 6–7 pt; nothing essential below 5 pt.
- One typeface across the figure; consistent line weights; consistent panel margins.
- Colour: one colour per biological role, stable across panels, figures and text. Use a colour-blind-safe palette; avoid red–green contrast; add shape or line-style encoding for essential categories.
- Greyscale check: convert the figure to greyscale; if a category disappears, add redundant encoding.
- Small-size check: print at final size (89 mm or 55 mm) and read every label; if a label fails, change the panel layout rather than shrinking the font below 5 pt.
- White space is part of the design: align panels on a grid, keep axis labels outside the data area, and do not fill empty space with decoration.

## 7. Export and production checklist

- Canvas set in millimetres at final size; fonts embedded; text editable (no outlines) unless the journal requires raster.
- Vector formats for line art; 300–600 dpi raster for photographs; RGB; no CMYK conversion unless requested.
- Line weights 0.25–1 pt at final size; no hairlines that disappear in print.
- Panel letters and titles outside the data area; no overlap with ticks, labels or data.
- File naming consistent with the manuscript; each figure as a separate file; supplementary figures separate.
- Source data and plotting code deposited or archived; figure numbers and legends match the manuscript and the submission system.
- Permissions for reused panels; credit line in the caption; BioRender licence where applicable.

## 8. Audit sequence

1. Claim: write the figure's claim sentence; does every panel contribute?
2. Order: does the panel sequence follow the reader's reasoning?
3. Evidence: for each quantitative panel, are comparison, n, statistic and uncertainty present?
4. Structure: are residue/state/colour mappings identical between structural and quantitative panels?
5. Caption: does it state the claim, define n, name the test and explain non-obvious symbols?
6. Typography: at final size, is the smallest text ≥5 pt, and do panel letters follow the journal convention?
7. Accessibility: greyscale and colour-blind checks; no colour-only essential information.
8. Production: vector/raster choice, dpi, RGB, fonts embedded, line weights, file naming.
9. Consistency: figure numbers, panel letters, text references and legends agree.

Record the audit result. A figure that fails the 5-pt test, the greyscale test or the n/test statement is not ready, regardless of how attractive it looks on screen.

## 9. Relationship to the project overlay

figure-design-and-audit.md defines the author's project conventions: near-square data boxes (0.9–1.1 aspect), blue-led Okabe–Ito palette, wide-panel exceptions, larger type for HTML (essential text ≥6 pt, panel letters 9.5–10 pt) and audit records. Those conventions refine, and do not replace, the journal rules above. The larger HTML type is for screens and embedded documents; for journal submission, follow the target journal's 5–7 pt range at final printed size. When a project convention conflicts with a journal requirement (for example, a wide panel that would not fit a single column), follow the journal for final artwork and record the project exception.

## 12. AI image policy and image integrity

AI-generated or AI-altered research images are not acceptable data. Nature Portfolio requires AI use to be documented and AI-generated images must not misrepresent data; some Nature journals prohibit AI-generated images and videos. Science requires explicit editor permission for AI-generated text, images and graphics and treats undisclosed AI visual content as an editorial-integrity issue. Elsevier (June 2026) requires image-level caption disclosure of the tool, version and use, plus the general AI declaration. Verify the target journal before generation.

For a conceptual AI-assisted figure: label it conceptual, disclose tool/version/use in the caption, verify all labels and relationships, keep the prompt/output/manual-edit provenance, and obtain editor permission for covers or graphical abstracts. Data figures come from real data and code. Full policy, provenance and negative checklist: ai-figures-and-visual-integrity.md.

## 13. v1.2.6.3 layout and statistical marks

Legends must not cover points, lines, intervals, bars, matrices or structures. Prefer a
horizontal legend below the panel title; use a reserved right corridor when the title band
cannot accommodate it. Direct labels are limited to at most four short series. Never remove
an axis title to resolve tick collisions. Abbreviate category labels and retain two to four
evenly spaced ticks; every axis keeps at least two.

Observed values must not touch a linear upper limit. Non-negative proportions retain the
zero baseline and add about 10% headroom. Significance brackets correspond to real
comparisons and report adjusted q values; forest q values occupy a separate outside column.
Combined distributions keep observations, violin and box transparent enough to remain
simultaneously visible.

## 14. v1.2.6.4 stars and legend order

Use stars inside figures: `*` q<0.05, `**` q<0.01, `***` q<0.001, `****` q<0.0001 and
`n.s.` otherwise. Exact q values belong in caption and source table. The default legend is
a horizontal multi-column band below the panel title and above the data; a right column is
the last fallback. Use first/middle/last representative stars for a continuous significant
run, retaining state changes and the last point so adjacent stars cannot collide.
