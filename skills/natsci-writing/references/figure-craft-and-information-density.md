# Figure craft, evidence architecture and information density

Version 1.2.5; updated 2026-11-24. Read when planning or auditing a multi-panel figure, deciding what belongs in a main figure versus Extended Data/Supplementary Information, judging visual hierarchy and information density, or designing a schematic/graphical abstract. Pair with figure-production.md, figure-standards-nature-science.md and the project figure overlay.

## 1. Start from the figure-level claim

Write before plotting:

~~~
Results-level question:
Figure-level claim (one sentence with a verb):
What could overturn that claim?
Decisive evidence:
Panel sequence: a — role; b — role; c — role
Destination of displaced material: main figure / another figure / Extended Data / SI
~~~

One figure normally answers one Results-level question. A figure may contain subordinate findings when all are needed to establish, qualify or bound the same claim. If a panel establishes a separate major claim, give it another figure.

Panel letters mark reading order; they do not assign fixed functions. Panel a need not be a schematic; panel d need not be a stress test.

## 2. Give panels different inferential roles

| Role | Question answered |
|---|---|
| Setup/schematic | What system, intervention or contrast is tested? |
| Representative example | What does the phenomenon look like in a concrete case? |
| Primary quantitative evidence | Does the central effect or capability exist? |
| Baseline/control | Does it exceed a credible alternative or survive the control? |
| Decomposition | Which components or variables account for the effect? |
| Stratification | Does it hold across meaningful conditions? |
| Orthogonal validation | Is it recovered with another assay or evidence type? |
| Perturbation/stress test | Does it survive an attack or fail as predicted? |
| Boundary/failure case | Where does it weaken, reverse or stop generalising? |
| Mechanistic evidence | What bounded explanation is supported? |

Panels should be independently necessary, not independent stories. Covering one must remove a distinct inferential step the others cannot recover. Prefer role diversity over metric diversity.

Weak mirror layout: a: R2 → b: R2 pairwise tests → c: MAPE → d: MAPE pairwise tests. This is often two roles, not four.

Stronger chain: a: perturbation design → b: decisive comparison → c: full distribution/residual → d: decomposition or boundary.

## 3. Evidence-chain archetypes

- **Validation envelope** (is a system/intervention/model credible?): define capability → establish it → test distinct failure modes (consistency, leakage, safety, bias, robustness) → attack → bound.
- **Scale-to-instance** (population pattern needs interpretation): global map/distribution → quantity → spatial relation/scale → internal structure → informative exception.
- **Discovery sequence**: hypothesis → decisive experiment → analysis → refined hypothesis → next test → mechanism validation.
- **Capability ladder** (method papers): what it is → what behaviour it learned → whether it outperforms alternatives → whether the gain survives harder conditions → what broader ability follows.

Across archetypes the reusable figure-level chain is: establish → compare/control → stress-test/discriminate → broaden → bound. Use only the moves the claim needs.

## 4. Align figure order with claim escalation

Across figures, each figure should make a stronger or different claim that creates the next question. Example archetype:

Fig. 1: What is it? → Fig. 2: Is the evaluation/resource credible? → Fig. 3: Does the phenomenon exist? → Fig. 4: Does it beat alternatives? → Fig. 5: Does the claim survive harder conditions? → Fig. 6: What mechanism, generality or boundary follows?

If two figures can both be summarised as "X performs well", merge them, demote the weaker evidence, or make the later figure ask a deeper question.

## 5. Visual hierarchy from evidence hierarchy

- Give the decisive evidence the hero position or largest area.
- Keep controls and robustness quieter but large enough to judge.
- Use one condition/cohort/method mapping across panels.
- Do not force equal panel sizes when importance differs; do not decorate panel a by habit.
- Make the attack, negative result or failure boundary visible when it changes the claim.
- Keep axes, uncertainty, n and comparator labels consistent wherever panels invite comparison; disclose any change.

## 6. Panel necessity and destination

1. What unique inference disappears if this panel is removed?
2. Does that inference establish, advance, qualify or bound the figure-level claim?
3. Is it a distinct role, or the same result under another metric/seed/threshold/encoding?

Route:
- **Main figure**: decisive evidence, necessary control, central falsification, conclusion-changing boundary.
- **Extended Data/SI**: reassurance, provenance, secondary metrics, alternative estimators, expanded subgroup views.
- **Another figure**: a genuinely separate major claim or the next rung.
- **Delete/merge**: a repeated view with no independent inference gain.

Never hide a conclusion-changing negative result because it complicates layout.

## 7. Information density

- One data plot per panel; no inset axes, subplot mosaics, facet grids, nested colour bars or miniature assembled plots inside one panel.
- Evidence density means role diversity, not more metrics. A panel with a mean bar and no n or distribution is under-informative when source data exist.
- Show distributions (points, box, violin, interval) rather than summary-only bars unless there is a reason.
- Use direct labels for decisive comparisons; avoid legend scavenger hunts.
- Keep colour roles stable and limited; encode evidence state by fill/shape/hatch/outline as well as colour.
- Remove chartjunk: 3D, gradients, shadows, decorative icons, heavy grids, coloured text, unexplained axes.
- Do not let a composite become unreadable: enlarge the canvas, split the figure, or move panels to Extended Data rather than shrinking type below the journal floor.
- A large dataset does not require a large number of panels; a few decisive comparisons plus source data often carry more information.

## 8. Flagship Nature figure requirements (verify at submission)

- Initial submission: figures may be embedded in the manuscript; production-quality artwork is not required; legends go on the same page as the figure; data must be assessable.
- Legends: complete legend <250 words at initial submission; begin with a title sentence; describe what is shown; state n, replicate definition, centre/spread, error bars, test, correction and P-value display; do not narrate results or Methods.
- Production main figures: 89 mm single or 183 mm double column; height ≤170 mm; text 5–7 pt at final size; panel letters 8 pt bold upright lowercase a, b, c; Arial/Helvetica; Courier for amino-acid sequences; editable text; vector formats (.ai, .eps, editable .pdf; layered PSD, PDF-converted PowerPoint, SVG, Excel, PS where accepted); no flattened JPEG/TIFF/PNG as final main-figure production file; aim <50 MB per file.
- Extended Data production: RGB, ≤300 dpi, ≤10 MB per file, JPEG preferred or TIFF/EPS, one page per item, required filename pattern.
- Accessibility: axis lines/ticks, labelled axes with units, accessible palette (no red/green or rainbow reliance), no gridlines/shadows/decorative patterns/coloured text, scale bars editable and calibrated, RGB, photographs ≥300 dpi (450 dpi preferred).
- Image integrity: raw file, crop, contrast/gamma, pseudocolour, stitching, lane rearrangement, processing software, reuse; follow the journal image-integrity policy.
- Extended Data: up to ten multi-panel items; SI for essential large/specialised material; every item cited in the manuscript.

Do not confuse initial-submission and accepted-in-principle requirements.

## 9. Vector schematics and graphical abstracts

- Use a vector schematic when the reader must understand a system, workflow, mechanism or agent loop before reading the data.
- Type: one family, at most three sizes; 5–7 pt ordinary text at final Nature size; one dark ink; bold only top-level group names; labels use the manuscript's own terms.
- Colour: white canvas; at most two saturated fills and exactly one accent for the paper's new component; pale/grey for existing parts; red only for errors/bottlenecks; no rainbow, gradients, 3D or shadows; do not rely on colour alone.
- Lines: every directed edge has an arrowhead; main path heaviest; one meaning per dashed style; orthogonal routes for structure, curves only for feedback; connectors attach mid-side; avoid crossing labels; keep visible gaps between lines and box edges.
- Structure: ≤3 nesting levels; align boxes to a grid; equal gaps; repeat container order; show repetition with ×N, not N copies.
- Legend: only when more than four encodings need decoding; place within one box-width; number main-path edges and match the caption walkthrough.
- Agent/tool diagrams: draw the agent as an iterating loop (reason → call tool → observe), tools as callees grouped by module, retrieval as a tool call, not a pipeline stage; name the model when compared.
- Graphical abstract: a schematic, not fabricated data or a decorative illustration; no invented structures, results or quantitative claims; use the vector workflow and keep labels/colour roles consistent with the figures and abstract. AI-generated images are acceptable only as illustration when disclosed and when they do not imply data; never use them to represent experimental results.

## 10. Chart catalogue (quick selection)

| Chart | Use when | Avoid when |
|---|---|---|
| Horizontal bars | Ranking/comparison of methods or groups, with uncertainty | Continuous trend; hiding distributions |
| Line/trend | Time, dose, ordered condition | Nominal categories; few timepoints with large uncertainty |
| Scatter | Relationship between two measured variables | Overplotting with no density/alpha strategy |
| Box/violin + points | Distribution across groups | n so small that only individual points are honest |
| Heatmap | Matrix of many conditions/features | Arbitrary ordering; rainbow scales; cell text |
| Forest/interval | Effect sizes with CIs across subgroups | No reference line or scale interpretation |
| Stacked area/bar | Composition over time/group | Exact comparisons; more than ~5 categories |
| Radar | Multi-benchmark profile with independently normalised axes | General comparison; hides magnitudes |
| Network | Relationships/architecture | Dense hairball without layout purpose |
| Image plate | Microscopy/imaging evidence | Without scale bars, controls and quantification |
| Schematic | System/mechanism/workflow | Decorative panel with no informational role |

## 11. Figure audit

- Can the figure-level claim be stated in one sentence with a verb?
- Does every panel have a distinct inferential role and a necessary comparison?
- Does panel order form a chain rather than a dashboard?
- Is the decisive evidence visually dominant, with controls quieter but legible?
- Are central attacks, negative results and boundaries visible?
- Is the information density appropriate (distributions, n, uncertainty, direct labels) rather than summary-only?
- Are the journal width, type size, panel letters, file format and legend limits met at the recorded stage?
- Do figure order, Results claims and Discussion synthesis escalate rather than repeat?
- Can the caption explain what is shown without replaying the Results?
- At final physical size, are all labels, ticks and annotations legible and collision-free?

## 12. AI-generated visual content

An AI-generated image is not evidence. Conceptual schematics and graphical abstracts may use AI when the journal permits it, the figure is labelled conceptual, the authors verify every label and relationship, and the provenance record is archived. Data figures remain code-generated from real data. AI-assisted layout, colour or typography is acceptable with disclosure; AI-generated text labels must be rebuilt and checked. Bans: synthetic data images, generative fill/object removal, AI upscaling that invents detail, fabricated structures, fake scale bars or significance marks, undisclosed AI in covers/graphical abstracts, and copyrighted or patient material in prompts. Read ai-figures-and-visual-integrity.md.
