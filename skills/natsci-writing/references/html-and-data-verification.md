# Complete HTML revision and scientific verification

Updated: 2026-11-18. Read this reference in full when the user requests a complete HTML or long-document revision, verification of data authenticity, or inspection of scientific calculations. Combine it with SKILL.md and research-and-language.md.

## 1. Establish the source and preserve it

Resolve the actual input file and requested output. Inspect the existing document before modifying it. Preserve the source and create a new version unless the author explicitly requests an in-place edit. Read relevant project instructions without extending the task to unrelated projects or files. Keep editing scripts and working records outside the final deliverable.

A request to incorporate an HTML-editing prompt into a skill calls for updating the skill. Execute a manuscript-wide HTML revision when the user supplies or identifies that manuscript as the current editing target.

## 2. Read every scientific content block

Inventory document sections and extract visible text in reading order. Include headings, paragraphs, list items, table headers and cells, figure captions, footnotes, callouts, appendices and references. Inspect collapsed panels, tabs, embedded text and JavaScript-rendered scientific content. Identify text carried inside SVG or raster images separately.

Read all extracted text. Split large documents into explicit, ordered ranges and keep a working coverage ledger with a stable block identifier, section, source location and review status. A search result or excerpt supports inspection of that passage. It does not establish whole-document coverage. Check tool output for truncation and continue from the first unread block.

Preserve document title, scientific argument, section purpose, terminology, figures, equations and citation relationships in a compact internal map. Read original prose before rewriting it. Review the completed revision in full after the edits.

## 3. Revise at sentence level

For every sentence, inspect scientific meaning, grammar, terminology, information order and relation to adjacent sentences. Rewrite vague abstractions, formulaic opposition, defensive framing, noun stacks and unsupported evaluative language using concrete biological objects and observable relationships. Retain clear, accurate sentences.

Keep scientific sections in connected paragraphs. When the author requests conversion of explanatory lists into prose, preserve every substantive point and its evidence. Retain scientific data tables, equations and labels where they communicate the content effectively.

Use the same standard for headings, captions, tables, annotations and conclusion text. A polished introduction and unchanged appendix leave the full-document task unfinished. Track any scientifically meaningful text inside images that requires a separate editable graphic.

Maintain the distinction between an observation, a computed prediction, an interpretation and a proposed experiment in the wording itself. Place the research purpose before the result and explain the biological consequence after the evidence.

## 4. Trace scientific statements to sources

Build a working evidence ledger for consequential claims and numerical quantities. Record the HTML location, statement, source dataset or original paper, version/date, relevant rows or figure, calculation and verification status. Include cohort size, reported rates, statistical tests, effect sizes, thresholds, model comparisons, mechanistic statements and resource-availability claims.

Use local data and producing code to verify project-specific findings. Use primary papers, deposited data and official records for external claims. Verify that the actual source supports the biological system, conditions and outcome stated in the text. Keep experimental data, observational evidence, model predictions, simulations and expected results separately identified.

For proposed research, discuss anticipated observations as predictions and specify the experiment that will test them. An illustrative number stays labelled illustrative everywhere it appears. Never create a completed measurement, citation, effect size or significance value to fill a narrative gap.

## 5. Inspect and reproduce the calculations

Follow the calculation chain from input to transformation, filtering, aggregation, statistical test and plotted or reported quantity. Inspect the producing code before naming a method or interpreting a column. Recompute consequential results from available inputs using an isolated working script, and compare against the displayed text, tables and figures. Record commands, input versions and output locations when useful for reproduction.

Check numerical type, missing-value handling, duplicates, unique identifiers, cohort membership, inclusion/exclusion rules, units, indexing and the analysis unit. Match numerators and denominators. Distinguish proteins, genes, domains, residues, sequence entries, independent samples and repeated measurements.

Check percentage calculations, absolute versus relative change, fold change, weighted versus unweighted averages, transformations, normalization, ranking direction, ties and aggregation across dimensions or samples. Preserve precision in the calculation and round only the final presentation.

For inferential statistics, check experimental independence, replicate structure, pairing, sample size, test assumptions, sidedness, null model, multiplicity correction, testing family, confidence intervals and interpretation of uncertainty. Keep standard deviation, standard error and confidence interval distinct.

For predictive analyses, inspect training/test separation, feature selection, preprocessing, hyperparameter selection, calibration and evaluation. Check overlap, identity or family leakage at the relevant biological unit. Name the metric accurately: recognition/sensitivity, precision, recall, coverage and annotation correctness describe different quantities.

For equations, verify variable definitions, dimensions, normalization, signs, domain of validity and the relationship between mathematical notation and implementation. A spatial, mechanistic or causal interpretation requires the corresponding evidence.

Do not silently change source data or redefine an evaluation to improve a result. Apply verified corrections to the new document and record the original quantity, corrected quantity, reason and source. Re-running a substantial analysis or changing the study design requires the corresponding task scope and permission.

## 6. Resolve evidence gaps through exact writing

Complete all checks supported by the available material. Preserve the distinction between arithmetic checked from reported counts and a result reproduced from raw data. Record an unavailable input or unresolved inconsistency in a separate author-facing verification note. State the affected quantity, missing source and concrete action needed.

Keep routine editing notes and repetitive assurances out of the scientific narrative. Express the actual measurement, comparison and experimental conditions directly. Revise any conclusion whose evidential basis changes. Preserve consequential null findings, contradictory controls and uncertainty values in the scientific account.

A missing source cannot become a verified result through confident language. When it prevents completion of a substantive scientific statement, retain the accurate supported wording and identify the issue explicitly to the author.

## 7. Produce a complete, readable HTML

Write the requested new HTML with semantic headings, complete scientific paragraphs, correct UTF-8 text, a useful document title and an appropriate language attribute. Preserve working navigation, anchors, citation links, tables, equation rendering, figure placement, image descriptions and scientific interactive content.

Maintain the established layout unless redesign is requested. Use readable typography and responsive treatment of wide tables and figures. Embed or package required assets deliberately. Add no external uploads, trackers or unpublished-material transfers. Keep scripts separate from scientific prose.

Preserve figure labels, equation numbering and reference identities through revision. Escape text appropriately and retain valid markup. Check whether dynamic content, local assets and equation libraries work in the intended viewing environment.

Use MathML `<math display="block">` or an equivalent offline TeX/MathJax renderer for
display equations and `<math>` for inline variables. Do not leave equations as ordinary
paragraph text, Unicode pseudo-subscripts or spacing approximations. Verify mathematical
structure in the browser. In every scientific section, use `<strong>` around the measured
comparison, effect, count, interval or threshold that changes the interpretation, while
retaining the complete sentence and denominator.

### Figure and panel system

Read `figure-design-and-audit.md` for figure redesign or figure-dependent HTML revision. Square means that the plotting box inside each panel has equal visual x- and y-axis lengths; it does not mean that the whole figure card is square. Keep regular analytical plotting boxes within 0.9–1.1 and reserve wide layouts for longitudinal structures, sequence maps, plate maps and panels whose labels or comparisons require horizontal correspondence. Use the semantic Nature/Science palette in the figure reference. Check each panel's internal box aspect, axes, units, type sizes, labels, legends, colour roles and source-data links. Matrix panels use symbols or outlines rather than in-cell numeric, letter or `yes / ~ / x` text. Verify `figure_color_audit.tsv` and `figure_palette_roles.csv`: no forbidden colormaps, no unregistered colours, minimum text contrast to white ≥4.5, zero matrix-cell text, and marker/line redundancy for categorical comparisons. Check each figure group's title, panel sequence, alternative text, PNG/PDF/SVG exports, embedded panel letters and browser rendering. Verify typography, geometry, text, wide-exception, semantic-colour and export gates before release.

Use fixed type roles: 10 pt for ordinary text, ticks, legends and direct labels; 10.5 pt
for axis labels; 11 pt for regular panel titles; 11.5 pt for structure titles; and
12.5 pt for panel letters. Use DejaVu Sans and `#132B36` for ordinary text. Validate
equality rather than a figure-level minimum. Record every axis separately for role font,
text colour, in-panel collisions and canvas overflow. Measure final raster content extent
and the largest internal blank row and column bands in addition to edge-ink checks.

Regular composite figures default to nine analytical panels in a complete `3×3` grid.
Use six-panel `3×2` only when a ninth independent evidence dimension would duplicate an
estimand or add decoration. A top evidence track is a registered wide exception. Every
ninth panel needs a named source table and a new evidence role; seven-, eight-, ten- and
eleven-panel mixed layouts fail release.

Use a fixed physical grid: axes in one column share the same left boundary and axes in one
row share the same bottom boundary, with deviations at most `0.01 mm`. Regular axes have
equal width and height within `0.01 mm` and remain square. Fixed panel cells may use a
subtle `0.6 pt` `#CAD7DC` boundary when labels or legends differ in width; the frame must
not cover data or become a second plot. Titles remain single-line, fit within axes width
and share one title top line with the panel letter.

Every visible analytical axes requires non-empty x- and y-axis titles, including matrix and
categorical panels. Axis titles are fixed at 10.5 pt. Use `a` for the evidence track and
`b–j` for the analytical panels; b–j align to the complete cell left edge and title top
within `0.5 mm` as separate text objects. Do not identify letters with `[a-z]` alone.
Reject naked coordinate boxes, isolated summary bars, single points and threshold-free
curves; each figure uses at least two evidence encodings and shows available samples,
intervals, pairing, background, controls, thresholds or holdouts.

Measure complete neighboring-panel gaps after final typography, tick suppression and legend
placement. The boundary includes the data box, panel letter, wrapped title, ticks and offset
text, axis labels, direct annotations and external legend. Horizontal and vertical clearances
must each be `0.38–0.42 × panel data-box width`, default `0.40`. Record millimetre gaps and
`gap / panel_width` in `panel_visual_gutter_audit.tsv`, freeze the converged layout, and ensure
the save call does not repeat `subplots_adjust` or automatic title placement. A panel letter
must anchor the outer upper-left blank of its cell, approximately `0.20 × panel width` left
of and at least `4 mm` above the data box, with a `3 mm` minimum title gap. The title is
centred over the data box, single-line and bold.

Every figure group needs prose that states the finding, the numerical or comparative pattern,
the supported relation and the interpretation boundary. Add a branch-by-branch result index
when several work packages are reported. Wrap all wide tables in local overflow containers;
after adding a table, verify both desktop and mobile `scrollWidth <= clientWidth`.

The figure should state one anatomical or mechanistic claim through a structural view and a quantitative comparison on the same residue, state and colour mapping. Data-only panels remain valid when the figure also contains a concrete structural panel that locates the measured relationship. Essential numerical values remain visible in the graphic or caption and traceable to source data.

## 8. Verify coverage and delivery

Re-read all revised scientific text in reading order. Reconcile the coverage ledger against the original inventory: each original content block has a reviewed counterpart or a documented, justified removal. Added sections require the same language and evidence checks.

Check document-wide terminology, repeated numbers, units, methods descriptions, figure/table references, citations and conclusions. Inspect images and relevant panels when the task depends on them. Use an available browser to review the final rendered HTML, including navigation, figures, tables, collapsed content and equations. Distinguish a structural HTML check from visual inspection.

Run text searches for risky wording as a final aid, then inspect each match in context. Exact phrase matching can miss paraphrases and can flag legitimate scientific wording. Human-readable meaning remains the criterion.

Verify that the final file exists and contains the intended revised content. Report the output path, actual scope completed and any substantive unresolved items concisely. Keep a detailed verification record separate when needed. Declare final deliverables through the host artifact tool when available; exclude backups, working scripts and temporary files.

### Rendered lazy-image galleries

File-existence checks do not prove that a browser loaded an image. Gallery images need
an explicit `aspect-ratio` and minimum height so they retain a nonzero intersection box;
otherwise a lazy image inside a collapsed `<details>` can remain at
`naturalWidth = 0`. During browser QA, open every `<details>`, scroll through the
expanded document, and require every declared image to satisfy
`complete && naturalWidth > 0`. Store these counts with the final screenshots.

## 9. v1.2.6.3 figure-release regression

Every quantitative figure in the HTML reads its same-stem audit JSON and requires all of
`zero_text_collisions`, `zero_out_of_canvas`, `layout_spacing_compliant`,
`typography_compliant`, `all_panels_evidence_dense`,
`zero_text_data_occlusion` and `zero_legend_data_occlusion`. Also require at least two
visible ticks for every axis in `axis_tick_completeness`, no axis title in
`sparsified_tick_labels`, and effective font sizes above the project thresholds at final
CSS width.

Legends and direct labels are checked again after final panel scaling. File existence is
not sufficient: verify that the current HTML references the hashes produced in this build
and no legacy figure remains referenced. Every significance bracket and q value traces to
a real comparison in the source summary, with comparison key, independent unit,
denominator and adjustment recorded.

## 10. v1.2.6.4 star and legend-mode audit

The HTML caption declares `*` q<0.05, `**` q<0.01, `***` q<0.001, `****` q<0.0001 and
`n.s.` otherwise. No q text may remain inside a plot. Quantitative audits also check legend
mode: a right legend is a failure when the header accommodates its width; horizontal
legend y1, panel title and letter bboxes must remain separate; repeated continuous stars
appear only at representative points or significance-state changes. Re-run 38 charts, 128
visual assets and browser checks at 1440/390/320 after the final report build.

## 11. v1.2.6.6 bold claims, raster figure display and extent audit

**Bold the claims that carry the argument.** In a scientific HTML report, bold each Results
subsection's topic sentence, the decisive numbers and the logical turn of the conclusion; the
abstract's conclusion sentence and the inference clause of every figure caption also carry
bold. Use one to three spans per paragraph and never bold a whole paragraph. The rendered
weight must be visibly heavier than body text (700 weight, heading colour), because a claim
that is only emphasised in the prose plan but not on the page does not exist for the reader.

**Display figures as raster and link vector.** Show the 600 dpi PNG (or JPG) as the visible
figure element and link SVG/PDF separately. A very large SVG is not a reliable display path in
embedded viewers even when the browser reports it as loaded. Test by screenshotting the page
at the figure's vertical position; complete and naturalWidth > 0 is necessary but not
sufficient.

**Audit figure geometry against the source.** For every projection panel assert that all
points fall inside the axes and that x/y unit lengths match; for every structure panel assert
cartoon geometry, 20% background transparency and label-band placement. Report the data
minimum and maximum next to the axis limits.

