# Complete HTML revision and scientific verification

Updated: 2026-11-24; NatSci-Writing-skills 1.2.6.8. Read this reference in full when the user requests a complete HTML or long-document revision, verification of data authenticity, or inspection of scientific calculations. Combine it with SKILL.md and research-and-language.md.

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

Use standard mathematics markup for every displayed relationship. A standalone equation
belongs in MathML `<math display="block">` or an equivalent offline TeX/MathJax renderer;
inline variables use `<math>` or the same renderer. Do not leave formulas as ordinary
paragraph text, Unicode pseudo-subscripts or spacing-based approximations. Verify the
browser renders fractions, subscripts, superscripts, norms, Greek symbols and identity
relations as mathematical structure, and define every variable next to its first use.

Within each scientific section, wrap the comparison, count, interval, threshold or effect
that changes the interpretation in `<strong>`. Preserve the complete sentence and its
denominator or condition. The emphasis should identify the key result without bolding the
whole paragraph or isolating a number from its evidence.

### Figure and panel system

Read `figure-design-and-audit.md` for figure redesign or figure-dependent HTML revision. Square means that the plotting box inside each panel has equal visual x- and y-axis lengths; it does not mean that the whole figure card is square. Keep regular analytical plotting boxes within 0.9–1.1 and reserve wide layouts for longitudinal structures, sequence maps, plate maps and panels whose labels or comparisons require horizontal correspondence. Use the established semantic Nature/Science palette: primary `#0D5673`, secondary `#4E8EAD`, support `#16786F`, conditional `#C77A24`, negative `#B8453E`, orthogonal `#6C5079`, neutral `#586B75`, text `#132B36`. Check each panel's internal box aspect, axes, units, type sizes, labels, legends, colour roles and source-data links. Matrix panels must use symbols or outlines rather than in-cell numeric, letter or `yes / ~ / x` annotations. Verify `figure_color_audit.tsv` and `figure_palette_roles.csv`: no forbidden colormaps, no unregistered colours, minimum text contrast to white ≥4.5, no matrix-cell text, and shape/line redundancy for every categorical comparison. Check each figure group's title, panel sequence, alternative text, PNG/PDF/SVG exports, embedded panel letters and browser rendering. Verify typography, geometry, wide exceptions, semantic colour and zero out-of-bounds or overlapping text before release.

Use fixed type roles: 10 pt for ordinary text, ticks, legends and direct labels; 10.5 pt
for axis labels; 11 pt for regular panel titles; 11.5 pt for structure titles; and
12.5 pt for panel letters. Use DejaVu Sans and `#132B36` for ordinary text. Validate
equality, not a figure-level minimum. After any layout change, audit each axis separately
for role font sizes, text colour, in-panel collisions and canvas overflow. Measure final
raster content extent (at least 0.95 in both directions) and the largest internal blank
row and column bands (at most 0.14), in addition to edge-ink checks.

Regular composite figures default to nine analytical panels in a complete `3×3` grid;
six-panel `3×2` plates require an evidence-based reason. A separate horizontal evidence
track can sit above the grid and is registered as a wide exception. The ninth panel must
add an independent evidence dimension from a named source table rather than repeat a mean
or pass rate. No seven-, eight-, ten- or eleven-panel mixed layout passes.

Use one fixed physical grid: axes in each column share the same left boundary and axes in
each row share the same bottom boundary, with deviations at most `0.01 mm`. All regular
axes have equal width and height within `0.01 mm` and remain square. Use fixed panel cells
when labels or legends differ in width; a subtle `0.6 pt` `#D4E0E8` cell frame may mark the
complete boundary but cannot obscure data or act as a second plot. Panel titles must remain
single-line, fit inside the axes width, be horizontally centred and bold, and share one
title top line with the panel letter. Reject wrapped titles, mixed font roles/colors,
misaligned axes columns and any cell frame that changes the data area.

Every visible analytical axes requires non-empty x- and y-axis titles, including matrix and
categorical panels; a descriptive title does not replace either axis label. Axis-label
font size must equal 10.5 pt. Use letter `a` for the evidence track and `b–j` for the nine
analytical panels. The b–j letters align to the complete panel cell’s left edge within
`0.5 mm` and to the single-line title top within `0.5 mm`; letter and title remain separate
text objects. A plain `[a-z]` panel-letter test is insufficient because a track stage label
such as `h` would be misclassified.

Reject a figure when its panels are only naked coordinate boxes, isolated summary bars,
single points or threshold-free curves. Each figure must use at least two evidence
encodings and represent available samples, intervals, pairing, matched background, controls,
thresholds or holdouts. Pass the geometry and collision gates first, then perform this
evidence-density and publication-quality review.

Measure the complete visual gap between neighboring panels after the final typography, tick
suppression and legend placement. The panel boundary is the union of the data box, panel
letter, single-line centred title, all ticks and offset text, axis labels, direct
annotations and external legend. Reserve approximately one fifth of the panel width as
blank separation at each side. For BioNoether, horizontal and vertical gaps are
`0.27–0.29` of the regular panel data-box width, with `0.28` as the author-required
default after a 30% reduction from the earlier `0.40`. Audit axes-only or grid-cell-only
gaps do not establish this condition. Write the measured millimetre gaps and
`gap / panel_width` values to `panel_visual_gutter_audit.tsv`, then freeze the layout. If
the save routine repeats `subplots_adjust` or automatic title placement, the exported PNG
no longer corresponds to the audited layout and the figure fails release.

Each figure group needs a prose block stating what was found, which comparison or numerical
pattern establishes the regularity, what relationship the phenomenon supports, and where
interpretation must stop. For multiple result branches, add a row-by-row result index that
preserves each estimand, denominator, threshold and failure condition. Wrap every wide table
in a local overflow container and rerun desktop/mobile page-width checks after any table edit.

The figure should state one anatomical or mechanistic claim through a structural view and a quantitative comparison on the same residue, state and colour mapping. Data-only panels remain valid when the figure also contains a concrete structural panel that locates the measured relationship. Essential numerical values remain visible in the graphic or caption and traceable to source data.

Every structural HTML supplies visible Cartoon and Cylinder controls backed by a real
molecular viewer. PyMOL Cartoon uses `cartoon_fancy_helices=1`; PyMOL Cylinder uses
`cartoon_cylindrical_helices=1`. An interactive 3D viewer renders cylinders along real
helix runs. Hand-drawn fixed-width helix strokes and elliptical end caps cannot serve as
Cartoon or Cylinder. Both modes retain the active state, frame, camera, zoom, residue
numbering, domain colours, key sites and network. For a complete report, preserve every
original figure asset and add one independent `结构增强版：Cartoon + Cylinder` link at
each figure card. The companion page groups figures by structural entity, uses at least
two columns on desktop, and presents repeated report figures as compact anchors rather
than full-width repeated cards. The companion page displays the unchanged original image
together with both structural representations, source structure, key sites and
PNG/PDF/SVG links. Two-dimensional canvases reserved for network or motion schematics are
labelled as trace and use thin lines, nodes, edges and arrows.

Browser verification covers 1440, 390 and 320 px viewports. Verify that changing the
representation changes a screenshot hash of the structure canvas, that frozen-network
mode retains mode and camera, that controls keep a 44 px effective height, and that
`documentElement.scrollWidth <= clientWidth`. Store source-structure SHA-256, camera,
secondary-structure assignment, cylinder parameters, export hashes, raster occupancy
and maximum internal blank bands in the structural render record.

Lazy image galleries need a reserved intrinsic aspect ratio before browser QA. An image
inside a closed or zero-height card can remain at `naturalWidth = 0` even when its file
exists, so `document.images` reports it as missing during scrolling. Give gallery images
explicit `aspect-ratio` and `min-height`, open every `<details>` during the test, scroll
through the expanded page, and require all declared images to reach
`complete && naturalWidth > 0`. File-existence audits do not replace this rendered-page
check.

## 8. Verify coverage and delivery

Re-read all revised scientific text in reading order. Reconcile the coverage ledger against the original inventory: each original content block has a reviewed counterpart or a documented, justified removal. Added sections require the same language and evidence checks.

Check document-wide terminology, repeated numbers, units, methods descriptions, figure/table references, citations and conclusions. Inspect images and relevant panels when the task depends on them. Use an available browser to review the final rendered HTML, including navigation, figures, tables, collapsed content and equations. Distinguish a structural HTML check from visual inspection.

Run text searches for risky wording as a final aid, then inspect each match in context. Exact phrase matching can miss paraphrases and can flag legitimate scientific wording. Human-readable meaning remains the criterion.

Verify that the final file exists and contains the intended revised content. Report the output path, actual scope completed and any substantive unresolved items concisely. Keep a detailed verification record separate when needed. Declare final deliverables through the host artifact tool when available; exclude backups, working scripts and temporary files.

## 9. v1.2.6.3 全图件发布回归

HTML 中每幅定量图必须读取同名审计 JSON，并同时要求
`zero_text_collisions`、`zero_out_of_canvas`、`layout_spacing_compliant`、
`typography_compliant`、`all_panels_evidence_dense`、
`zero_text_data_occlusion` 和 `zero_legend_data_occlusion` 为真。另查
`axis_tick_completeness` 中每个轴至少两个可见刻度、
`sparsified_tick_labels` 不含轴标题，以及最终 CSS 宽下的 effective font size 不低于
项目阈值。

图例与直接标签必须在最终面板缩放后再次检查。报告中的图不可只凭文件存在就通过；需要
核对当前 HTML 引用的哈希等于本轮生成文件，并确保旧版图不再被引用。所有显著性括号和
q 值来自源 summary 的真实比较，审计记录中保留比较键、独立单位、分母和校正字段。

## 10. v1.2.6.4 星号与图例模式审计

HTML 图注统一声明 `*` q<0.05、`**` q<0.01、`***` q<0.001、`****` q<0.0001、
`n.s.` q≥0.05。图内不得存在 q 文本。定量图审计同时核对 legend mode：顶部可容纳却出现
右侧图例为失败；水平图例 y1、panel title 和 letter 的 bbox 必须分离；连续星号只能出
现在代表点或显著状态变化处。最终报告重新跑全部图、视觉资产和 1440/390/320 浏览器
回归。

## 11. v1.2.6.6 HTML 强调、raster 展示与范围审计

每个 Results 小节的主题句、决定性数字和结论转折加粗；摘要结论句与每条图注的推断句也
加粗。每段使用 1–3 个 `<strong>`，禁止整段加粗；浏览器中必须显示为 700 字重和标题色，
只在写作计划里“强调”而页面未呈现视为未完成。

图件以 600 dpi PNG/JPG 显示，SVG/PDF 单独链接；嵌入式浏览器对超大 SVG 的支持不稳定。
在图的纵向位置截图核验实际绘出，`complete && naturalWidth>0` 只能说明文件加载。每个
投影面板同时记录数据最小/最大值、axes limits 和 `clipped_point_fraction=0`；每个结构
面板记录 cartoon 表示、20% 背景透明度和标签带位置。
