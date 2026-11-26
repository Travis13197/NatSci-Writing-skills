---
name: natsci-writing
description: >-
  NatSci-Writing-skills production system. Write, draft and revise complete biology, biotechnology, bioinformatics and
  AI-for-science manuscripts to Nature/Science standard, and produce the figures that
  carry them. Use for full manuscripts, abstracts, introductions, results, discussions,
  methods, reviews, perspectives, figure sets, figure legends, journal formatting,
  response-to-reviewers letters, Chinese scientific prose, complete HTML revision,
  literature-grounded research design, data or calculation verification, bracketed
  annotations, bilingual revision and continuation of the SEAL project. Encodes
  corpus-calibrated argument architecture, diction, hedging, figure conventions,
  editorial fit, statistics and reporting integrity, information architecture and
  end-to-end production workflows measured from 800+ Nature/Science papers. Includes
  defensive-writing control (press-release principle, argument selection, experiment duties)
  and measurable anti-AI-prose gates for English and Chinese drafts.
metadata:
  version: "1.2.8.0"
  updated: "2026-11-26"
  author: "Chuanyang Liu"
  system: "NatSci-Writing-skills"
  language: "en"
  companion: natsci-writing-zh
---

# NatSci-Writing-skills — Nature/Science manuscript production (English)

## Purpose and scope

Produce or revise complete scientific manuscripts, sections, figures and submission packages at Nature/Science standard: a specific question, an early claim, evidence that earns it, a consequence the reader can use, and figures that carry the same argument visually. The skill covers research Articles, Reviews, Perspectives, methods and algorithmic papers in life science, biotechnology, bioinformatics, protein language models and AI-for-science, in English and Chinese.

Four habits govern every task:

1. **Claim before catalogue.** Each paragraph opens with the relationship it establishes, then earns it with evidence.
2. **Concrete before abstract.** Name the molecule, dataset, comparison, measurement or model quantity; abstractions are earned by definition, not used as scaffolding.
3. **Calibrated confidence.** Verbs match evidence; uncertainty is stated once, concretely, where it matters.
4. **Reader economy.** Delete anything that does not change what the reader knows or can do.

Resources:
- references/manuscript-production.md — complete drafts, section playbooks, paper types, journal formats, full-manuscript package, formatting, statements, self-review. Read for any full-manuscript or formatting task.
- references/revision-and-response.md — polishing workflow, phrasebank, style guardrails, response letters, reviewer simulation. Read for revisions and rebuttals.
- references/journal-style-evidence.md — corpus coverage, measured statistics, genre definitions, exemplars, limitations.
- references/writing-diagnostics.md — AI-tell lexicon, failure modes, rewrite drills.
- references/editorial-and-submission.md — Nature/Science editorial criteria, journal fit, article limits, cover letter, presubmission and submission package.
- references/innovation-and-broad-interest.md — contribution types, contribution ladder, gap engineering, discriminating predictions, broad-interest and why-this/why-now/why-broad tests.
- references/main-text-and-information-architecture.md — result classification, shortest evidence chain, main-text/caption/SI split, revision-accretion control, claim repetition, display budgets.
- references/statistics-and-reporting-integrity.md — independent unit and replication, Nature statistical requirements, figure statistics, image integrity, data/code/materials reporting, severity labels.
- references/language-and-taste.md — prose rhythm, voice, house style, taste diagnostics, model shapes, Chinese-specific checks.
- references/ai-use-and-writing-integrity.md — AI authorship ban, disclosure, permitted/prohibited uses, 2026 policy updates, AI-writing negative list, confidentiality, AI-tone control, audit.
- references/ai-figures-and-visual-integrity.md — AI-generated/AI-assisted figure policy, data vs conceptual figures, publisher positions, disclosure, provenance, copyright, QC and negative checklist.
- references/literature-search-and-citation.md — search strategy, source hierarchy, screening, evidence synthesis, citation verification and reference management.
- references/proofreading-and-polish.md — five-pass proofreading, sentence polish, grounding/rhythm, number/reference consistency.
- references/perspective-and-insight.md — Perspective intellectual centre, sequence of discoveries, speculation and accountability, formal content, audit.
- references/nature-section-craft.md — Nature abstract/Introduction/Results/Discussion move sequences, claim escalation and section audits.
- references/nature-perspective-production.md — Nature Perspective/theory-paper production: format, six-section architecture, full-paragraph rule, evidence hierarchy, conceptual figures, bilingual workflow, editing modes, three-discipline review.
- references/mirror-world-case-study.md — worked case: mirror-world hypothesis Perspective, six sections, Box/figures, mathematical objects, production lessons and reusable checklist.
- references/figure-craft-and-information-density.md — multi-panel evidence architecture, inferential roles, figure order escalation, information density, vector schematics, graphical abstracts.
- references/figure-production.md — figure contract, archetypes, Python/R backends, design system, chart selection, QA. Read for any figure task.
- references/figure-standards-nature-science.md — journal specifications, caption grammar, statistical display.
- references/figure-design-and-audit.md — the author's project geometry, colour hierarchy, structure rendering and release audits.
- references/panel-layout-and-letter-placement.md, figure-colour-audit-contract.md, structural-figures-baker-standard.md, seal-supplementary-figure-standard.md — mandatory project figure gates, including per-panel delivery and the SEAL 28-figure release audit.
- references/research-and-language.md — research-topic design, hypothesis development, literature synthesis, conceptual revision.
- references/html-and-data-verification.md — complete HTML revision, data authenticity and calculation checks.
- references/academic-prompt-zh.md — reusable Chinese task prompt.
- Project references (seal-project.md, translation-validation.md, dimension-annotation.md) — only for that project.
- assets/templates/ — manuscript outline, figure contract, caption, response letter, data statements, terminology ledger, cover letter/submission package, innovation canvas, editorial audit, reporting/statistics checklist, figure evidence map, AI-disclosure record, literature-search plan, data/code/materials checklist, Perspective outline (perspective-manuscript-outline.md), editing-scope/change log (editing-scope-and-change-log.md), conceptual-figure brief (conceptual-figure-brief.md), AI-image provenance record (ai-image-provenance-record.md), AI-use negative checklist (ai-negative-checklist.md).

Project-specific values are dated evidence records, not universal facts; the latest author decision and verified analyses supersede them. Skill use does not authorize external publication or source-data changes.

## 0. Deliverable modes and routing

Separate skill maintenance, research design, manuscript drafting, local polishing, figure production, complete HTML revision, formatting conversion and response letters. Perform the underlying task when it is the requested deliverable; treat a quoted reusable prompt as instruction to incorporate.

| Mode | Input | Output |
|---|---|---|
| Complete draft | idea, data, figures, notes, Chinese draft | Full manuscript in target structure, with assumptions and missing-input list |
| Section draft | section request plus claim/evidence | Complete sections ready to paste |
| Rebuild | draft with structural problems | New architecture plus rewritten sections |
| Polish | finished or near-finished prose | Sentence/paragraph revision with change log |
| Formatting | manuscript plus target journal | Journal-compliant layout, references, statements, legends |
| Figure set | data plus claim | Publication-grade figures, captions, source-data map |
| Response | reviewer comments plus revision facts | Point-by-point letter, tracker, change checklist |
| Pre-submission review | manuscript | Three reviewer reports plus synthesis |
| Editorial audit | manuscript plus target journal | Fit assessment, readiness state, missing-fact list |
| Submission package | manuscript plus author facts | Cover letter, title page, declarations, reviewer suggestions, deliverable matrix |
| Statistics audit | methods/results/legends | P0/P1/P2 issues, ready-to-paste revisions, AUTHOR_INPUT_NEEDED list |

Before a full draft or major rewrite, run the confirmation gate (manuscript-production.md §2): echo the one-sentence argument, paper type, plan, terminology ledger, reader lead question and assumptions; ask at most 2–3 high-leverage questions only if the framing is ambiguous. If the author supplies a complete claim/evidence/boundary, state the argument in one line and proceed.

For a new research project, read research-and-language.md in full, identify the unresolved biological relationship, and develop a central hypothesis with distinguishable predictions. Record search dates and compare with the closest primary studies.

## 1. Preserve the author's scientific intent

- Treat the latest explicit author decision, supplied text and annotations as the editing baseline; older versions provide context only. A changed file is a reason to inspect, not permission to restore.
- Keep approved titles, abstracts, definitions and names consistent. Change approved text only when requested or when correcting a substantive error; explain the correction separately.
- Read the full supplied section and all annotations; read adjacent sections when they affect the edit. Say accurately what was read.
- Interpret 【】 and inline comments as instructions about the preceding sentences; resolve every comment and remove editing instructions from the prose.
- When the structure is largely satisfactory, preserve it; polish sentences, repair connections, add only evidence-grounded insight.
- Preserve numbers, units, cohort definitions, thresholds, figure identities and statistical directions. Correct verified discrepancies transparently. Never manufacture experiments, effects, citations, benchmarks or mechanisms.
- Treat the intended novelty as a scientific argument to develop, not a label to repeat. Distinguish a conceptual proposal, a demonstrated capability and a future opportunity.

## 2. Argument, top-journal standard and genre

Build an internal map: question → unresolved issue → approach → evidence → interpretation → next question. For each paragraph identify its purpose, object/comparison, claim, evidence, inference, and its link to the previous and next paragraphs. Reordering alone does not repair a missing relationship.

Measured targets (median values from the corpus; per 1,000 words for rates):

| Dimension | Research Articles | Reviews | Perspectives |
|---|---|---|---|
| Abstract | Nature ~200 words/7–8 sentences; Science ~125/6 | 120–200 words/5–6 sentences | Nature ~185-word preface; Science one-sentence teaser (~11 words) |
| Sentence | 24–25 words; p90 42–45 | 25 words | 26–27 words |
| Paragraph | 120–140 words/4–5 sentences | 150–260/6–9 | 200–320, essayistic |
| First person | 10–13 | 1–2 | ~5 |
| Hedges | 3–6 | 6 | 5 |
| Connectives | 4 | 6 | 5 |
| Not X but Y | <1 | <1 | <1 |
| Em dash/semicolon | <1 / 3–4 | 1–4 / 1–2 | 1–3 / 1–2 |
| Numerals | 50–60 | 40–65 | 30–40 |

Qualitative rules: claim-first openings; specific subjects and strong verbs; evidence adjacent to claim; one move per paragraph; calibrated verbs (show/demonstrate/reveal for direct evidence; indicate/suggest/consistent with for inference; may/could/propose for speculation); quantified prose with unit, comparison and denominator; restrained connectives; journal-specific signatures (Nature summary paragraph ≤200 words with "Here we show"; Nature Review preface ≤200 words, <7,000 words, 4 display items; Nature Perspective personal and forward-looking; Science abstract ~125 words; Science Perspective one-sentence teaser; Nature lowercase bold panel letters, Science uppercase).

**Genre architecture.**
- Research Article: abstract 5–6 moves; introduction funnel; Results subsections as question → design → observation → inference; Discussion 4–6 paragraphs ending on a concrete opportunity.
- Review: argued thesis, organizing framework, synthesis by mechanism, evidence-quality judgement, specific outlook; one conceptual figure; not author-centred.
- Perspective: tension → thesis → 3–5 evidenced propositions → serious counterposition → consequences → agenda; personal voice, labelled speculation.
- Short formats: one claim, minimal context, one decisive comparison, ≤2 display items.

### 2.4 Innovation, broad interest and editorial fit

Classify the primary contribution (phenomenon, mechanism, measurement/capability, resource, theory, clinical/translational) and place it on the contribution ladder (incremental → discriminating → explanatory → enabling → field-changing). Most Nature/Science papers need rung 2–4 in a broad frame; do not claim rung 5 without evidence.

A publishable gap is a scientific unknown, not the absence of your method. State the exact unknown, the competing explanations, the observation that discriminates them, and what resolving the gap changes. Write three sentences: why this, why now, why broad — each answerable with nouns and evidence, not adjectives.

Editorial fit is judged on originality, outstanding scientific importance, interdisciplinary interest, technical soundness and readability. Name the audience beyond the specialty and the concrete change for them. If the fit is weak, say so and propose how to strengthen the contribution or choose a better venue; never inflate significance language.

Detail: editorial-and-submission.md and innovation-and-broad-interest.md.

## 3. Language and writing diagnostics

Define a term at first relevant use through its measurable object or action; then use the established term. Replace unexplained abstraction with the actual comparison or result. Prefer exact verbs and concrete nouns; remove unsupported evaluative adjectives (sophisticated, revolutionary, unprecedented, universal, powerful, highly accurate, comprehensive, robust, seamless, pivotal, crucial, state-of-the-art).

Avoid promotional summaries and generic promises ("provides a foundation", "opens a new paradigm"). Each closing sentence names a capability, inference or consequence. Rewrite formulaic opposition and concession ("not X, but Y", "rather than", "X, but Y", 不是……而是……, 并非……而是……) as direct statements; keep contrast only when two scientific alternatives genuinely compete. Remove defensive framing, generic rigor assurances, self-evaluation and repeated limitation language; state the actual object, comparison, evidence and condition. Preserve substantive controls, negative findings, uncertainty and conditions that determine the conclusion.

Apply the same direct style inside figures: panel titles, legends, direct labels and captions name the measured observation, comparison, count or interval. Avoid defensive or self-limiting boilerplate in figure text; preserve genuine negative results in positive descriptive form (for example "the adjusted 95% interval includes zero", "62 of 84 shifts were negative") while keeping denominators, units, intervals, thresholds and sample hierarchy.

Avoid opaque phrases (for example 高加性读出中仍可识别连通响应, 物理与 AI 保持不同的可观测扇区, 全局软方向是一个真实的中介对象); read the source to find the actual perturbation, response, spatial relationship or mechanism; never invent one to repair a sentence. Avoid conversational instructions, audit language and editorial workflow descriptions inside manuscript paragraphs; keep them in short author notes. Avoid em dashes or hyphens linking independent clauses; standard compound modifiers are acceptable.

Seven diagnostics (detail in writing-diagnostics.md): abstraction stacking; template contrast; connective inflation; evaluative adjectives; defensive/self-limiting prose; list-paragraphs and module catalogues; meta-commentary. Corpus watchlist density is 2–4 per 1,000 words, mostly statistical/technical; more than ~5 per 1,000 or two in one paragraph signals generated-sounding prose. Run the delete-20%, actor, so-what and read-aloud tests.

**Zero-tolerance patterns.** Do not use template contrast ("not X but Y", "not only X but also Y", "not just X, it is Y", "rather than", "far from"), defensive disclaimers ("it is important to note", "to some extent", "further research is needed", "the findings should be interpreted with caution"), self-limiting framing, outline-like transitions ("In summary", "In conclusion", "Overall"), or their Chinese equivalents (不是……而是……, 并非……而是……, 不仅……而且……, 值得注意的是, 在一定程度上, 有待进一步研究, 综上所述). State claims affirmatively. When two explanations genuinely compete, write two affirmative sentences and let the discriminating evidence separate them. The same ban applies to READMEs, cover letters, figure text and author notes that will be read by others. Check deliverables with python tools/check_prose_style.py; ERROR hits are must-fix. Full pattern tables, rewrites, structural tells and sources: writing-diagnostics.md sections 3A and 4A. For argument-level selection - what the paper claims, which experiments survive, and how to separate a necessary caveat from a defensive one - read defensive-writing-and-argument-selection.md and run the gates in section 17.

### 3.1 AI assistance boundary

AI tools may help with language editing, structure, literature triage, formatting, code and figure layout, but AI cannot be an author and authors remain fully responsible. Disclose AI use where the target journal requires it; never upload unpublished, confidential, peer-review or patient material to public models; never use AI to generate data, research images, references, statistics or approvals. Treat AI-suggested references as unverified leads and verify every citation and number. The final text must still read as the authors' argument: specific, evidence-linked and free of AI-tone clusters. Policy table, disclosure template, 2026 updates, AI-writing negative list and audit: ai-use-and-writing-integrity.md; record template in assets/templates/ai-disclosure.md.

AI figures follow a separate gate. Data figures come from real data and code; generative models must not create or alter microscopy, gels, blots, imaging, plots or structures. Conceptual schematics, graphical abstracts and covers follow the target journal's AI-image policy, with disclosure, human verification, a conceptual label and a provenance record. Never use generative fill, object removal, synthetic research images, fake scale bars or undisclosed AI cover art. Read ai-figures-and-visual-integrity.md before any image generation; record with assets/templates/ai-image-provenance-record.md; audit with assets/templates/ai-negative-checklist.md.

### 3.2 Proofreading and final language pass

Run the five passes in proofreading-and-polish.md: spelling/terms; grammar; inappropriate words; awkward expression; academic style/consistency. Then check grounding, paragraph rhythm, numbers/units, citations and markup. Preserve correct technical terms and the author's voice; do not manufacture pedantic edits.

### 3.3 Editing modes and author-text fidelity

Agree on the mode before touching a manuscript: light polish, author-faithful expansion, structural rewrite, translation, tracked revision or audit. Light polish preserves claim order, scope and wording and adds no claims, experiments or methods. Author-faithful expansion keeps the author's terms and order, adding explanation only where marked. Tracked revision copies the source first and edits the copy with tracked changes and yellow highlights; the source file stays untouched. For every mode, keep a change log, list residual questions and run the fidelity checks in assets/templates/editing-scope-and-change-log.md. Preserve theoretical status: a proposed comparison stays a proposal; a model-derived relation stays distinct from an observed result.

## 4. Section playbooks (summary)

- **Title**: system/object + capability/action + application/consequence; 8–12 words; searchable, specific, defensible; no grant-style aims or unverified "first".
- **Abstract**: context/problem → gap → approach → strongest result with number/comparison → consequence → bounded implication. Nature: staged summary paragraph, "Here we show" after sufficient context, ≤200 words. Science: ~125 words. Draft last; every sentence must survive deletion of the others.
- **Introduction**: field stake → bottleneck → prior work (what it has and has not solved) → remaining gap → present study. Three to five paragraphs; no results in detail; explicit transition from known to this paper.
- **Results**: evidence ladder (system validation → main result → fair baseline → mechanism/ablation → application/generalization → stress test). Subsection openings state the question; observations with statistics; inference last. Every claim has comparison/ablation/stress-test evidence or is marked for follow-up.
- **Discussion**: central advance → meaning → rival explanations → relation to closest work → specific limits → now-testable opportunity. Interpret, do not repeat Results; hedge only where needed; limitations name the actual condition.
- **Conclusion**: contribution → decisive evidence → implication → boundary; no new data.
- **Methods**: reproducible inputs, design, procedure, outcomes, analysis/statistics, ethics; no "standard conditions", "routine methods" or undefined randomisation.
- **Review/Perspective**: see genre architecture; argument first, literature as evidence.

Full playbooks, paper-type variants (research, methods, algorithmic, hypothesis, review), journal formats and the complete-manuscript package are in manuscript-production.md.

### 4.2 Nature section craft

The four core sections are different compressions of one claim. Abstract: shortest claim-evidence-implication chain, one main discovery, no method inventory. Introduction: converge on the exact unknown, not the absence of your method; let the answer emerge after the question is motivated. Results: escalating evidence chain, one new inference per subsection, robustness visible where it bounds the claim. Discussion: synthesis against rival explanations and specific boundaries, ending on a concrete opportunity. Use the reverse outline, claim ladder, claim-location map and deletion tests in nature-section-craft.md.

### 4.3 Perspective and conceptual writing

A Perspective must change how the reader thinks. State one private editorial sentence, find the intellectual centre in a concrete tension, and design the argument as a sequence of discoveries rather than a topic tour. Mark established facts, interpretations, hypotheses and proposed experiments locally; use mathematics, analogies and speculation only where they do explanatory work. Detail: perspective-and-insight.md.

### 4.4 Perspective production and theory manuscripts

A full Perspective needs a production architecture, not only an insight. Use nature-perspective-production.md for the Nature format, the six-section archetype (tension, definitions, conceptual move, method, return, horizon), the evidence hierarchy, the full-paragraph rule, conceptual figure design, bilingual workflow, editing modes and the three-discipline review. Manuscript prose uses connected paragraphs; bullet lists stay out of the argument. Bold two or three single-sentence insights per subsection where the journal permits. Put boundaries in one dedicated paragraph, not in every paragraph. The mirror-world case study in mirror-world-case-study.md shows a worked six-section Perspective with a Box, three conceptual figures, mathematical objects and production lessons.

### 4.1 Main-text discipline and information architecture

Evidence completeness is not main-text completeness. Classify every result before placement: core discovery, necessary support, qualification, robustness, heterogeneity, provenance detail, alternative inference or edge case. Build the shortest sufficient evidence chain; route reassurance, provenance and secondary analyses to Extended Data/Supplementary Information; never hide conclusion-changing or contradictory evidence in SI.

Use the main text for what was found and what it means; captions for what is shown and how to read it; SI for why the conclusion survives deeper scrutiny. Report full statistics once in a defined location. Run the paragraph necessity test and claim-repetition map; every requested addition triggers a deletion check to prevent revision accretion. Respect the display-item and word budget (Nature Article ~2,500 or ~4,300 words with 4–6 modest display items).

Detail: main-text-and-information-architecture.md.

## 5. Scientific claims and statistics

- Distinguish association, model-output response, molecular mechanism and biological causality. Decoder sensitivity identifies a computational effect; functional assays test a biological role.
- When a project continues an earlier model generation, build a cross-generation comparison register: objective, source population and analysis cohort, model/layer scope, dimensionality reduction and atlas, clustering, visualization, group-level dimensions, compact programs, cross-model/species analysis, translation, annotation, experimental endpoints, statistical validation and delivered artifacts. Compare source counts, anchors and shared objects only when denominators, coordinate systems and evidence status align. Preserve ARI, effect size, KL, AP, recall, odds ratio as separate estimands; do not collapse them into a composite score. Report mapped rank, derived-axis loading and effect change with corrected cohort and background. State what the earlier generation supplies, what the current adds, and which predecessor analyses have not been rebuilt.
- Do not describe residue identities or domains as intrinsically qualitative; dimensions add quantitative variables learned from sequence context. "Underlying/deeper" refers to the model's numerical representation, not a physical layer below amino acids.
- Treat raw coordinates as model/layer-specific components; same-numbered coordinates from different models have no assumed biological equivalence.
- Distinguish raw embedding coordinates, PCA components and sparse-autoencoder features; do not attribute an SAE result to original coordinates.
- Keep FDR-only counts separate from effect-size-filtered selections. Distinguish unique GO terms from dimension–term associations summed over dimensions.
- Distinguish annotation call, inferred coverage, recovery of existing annotations, independent predictive accuracy and experimentally established function. Report numerator, denominator, unit and overlap for coverage.
- Distinguish in-library recovery from held-out testing; a held-out label alone does not ensure independent feature selection, library construction or calibration.
- Distinguish a decoy-calibrated operating point from an independently measured false-positive rate; state the operating point.
- Report means with correct dispersion, n, test, correction family and null model; never reuse a P value from a different null.
- Keep residue indexing and sequence-to-PDB mappings explicit; separate a decoded structural alphabet from a measured conformation.
- Use "some control comparisons also showed widespread significance" when that is what was observed; such results alone do not quantify the fraction from length/composition.
- Avoid family specificity, conservation or general applicability beyond the comparison. "Across the 34 families analysed" is stronger and safer than "generally".
- Trace annotation statistics through reference construction, feature selection, scoring, calibration and evaluation; a column named padj is not proof of term-level correction. Expanding a top-ranked list from a scan with one significant term does not make every link significant.
- Describe signed sets as dimension identities plus the direction relative to a stated reference; the sign is not an activating/inhibiting biological effect. State whether a quantity is a score, unadjusted test, adjusted result or calibrated probability; check how positive/negative tests are combined.
- Preserve provenance of selected variables (decoder KL, family dimensions, signed top-effect, all-model); do not substitute a favourable all-dimension result for a variable-specific validation.
- Separate largest structural displacement, model sensitivity, hinge motion, catalytic contribution, binding and mutational necessity. A candidate near an experimentally studied residue inherits regional context, not that residue's proof. Use fixed site-selection and aggregation rules before claiming recovery of important residues.
- Apply cohort splitting at every stage: a protein excluded from positive training may still sit in the selection background. Name the evaluation scope.

### 5.1 Statistics and reporting integrity

Define the independent experimental unit for every central claim; separate biological from technical replicates; do not treat cells, fields, reads, wells or model runs as independent samples. Report exact n, error-bar/interval definitions, number of repeated experiments, exact P values, and F/t statistics with degrees of freedom where required. State the comparison, test family, tail and multiple-comparison correction.

For flagship Nature, the Methods statistics section must cover tests, sidedness, independent unit, replicate definitions, pairing/repeated measures, inclusion/exclusion, randomisation/blinding and correction strategy; a Reporting Summary applies to life/behavioural/social/ecology/evolution/environmental fields and covered physical sciences. Audit image integrity (raw files, crop, contrast, pseudocolour, stitching, reuse) and data/code/materials statements.

Use P0/P1/P2 severity; never invent sample sizes, tests, software versions, approvals or accession numbers. Detail: statistics-and-reporting-integrity.md.

## 6. Literature, citations and statements

For simple polishing of supplied text, use its evidence and do not browse unnecessarily. When asked to discuss studies, assess novelty or meet current journal requirements, consult primary literature and official guidance.

- Form targeted questions; prioritise primary papers, author repositories and official guidance over secondary summaries.
- Verify title, authors, year, publication status and DOI before adding a reference; distinguish preprint from peer-reviewed version.
- Read the sections that support the statement; report access limitations accurately.
- Synthesise around a scientific question or methodological distinction, not paper summaries.
- Explain what the new work adds, complements or makes practical. Avoid "first", "universal", "new class" without a defined search scope.
- Place manuscript citation markers before sentence punctuation (author preference) unless a platform rule overrides; format references consistently for the venue.
- Never invent identifiers or convert database coverage into external validation.
- Verify resource availability (repository, release, licence, checkpoint compatibility) before writing that code or data are public; a local package or intended upload is not a public resource.
- Data availability, code availability, author contributions, competing interests and ethics statements must be specific, durable and verifiable; never "available upon request" without reason, route, eligibility and metadata. Details in manuscript-production.md §10.

### 6.1 Literature search, synthesis and citation integrity

Search to answer a question, not to accumulate references. Use a source hierarchy (primary research > systematic reviews/guidelines > reviews > preprints), at least three complementary databases when comprehensiveness matters, and a documented search/screening record. Synthesise by question, mechanism or assumption, not paper by paper. Verify every DOI/title/author, distinguish preprint from peer-reviewed and check retractions; cite where the claim is made and within the journal's reference budget. Detail: literature-search-and-citation.md; planning template in assets/templates/literature-search-plan.md.

## 7. Deliverables

Unless the request specifies otherwise:
1. One short Chinese paragraph explaining the revision logic.
2. The complete English revision in manuscript paragraphs.
3. A fully corresponding Chinese version in the same paragraph order.
4. Bold every replaced or added span relative to the author's latest text, including grammar and word choice; keep unchanged text unbolded. A fully rewritten sentence may be bolded in full.
5. A short prose note for significant scientific corrections, unresolved figure/source issues or editorial choices.

For a final clean version or complete HTML, remove revision bolding unless tracked changes are requested. When only one language is requested, deliver that language. For Chinese academic tasks, write native Chinese paragraphs directly (companion: natsci-writing-zh). Keep checklists and evidence ledgers outside manuscript prose.

Complete-manuscript deliverables additionally include: title page, abstract (and Chinese version when bilingual), main text with headings, methods, verified references, figure legends, extended data/supplementary list, statements, assumptions/missing-input list, and a change log. Output Markdown for review, DOCX for co-authors, LaTeX or HTML when required; keep one source of truth for numbers.

Match evidence strength across languages: candidate = 候选; associated = 相关/关联; predicted = 预测; demonstrated only for the tested capability.

## 8. Files and long-form work

Read the entire original and all annotations; preserve the source unless in-place editing is requested. For Word, create a new version and preserve images, sections, styles, references, fields and review anchors. Keep code outside document text.

Maintain an ordered coverage record for long files; continue through truncated tool output; include captions, tables, footnotes, references, appendices and dynamic scientific text. Review in two complete passes: (1) scientific logic, evidence, paragraph links, consistency; (2) every sentence, terminology, figures, statistics and annotation. For a section task, apply both passes to that section and adjacent context.

When data authenticity or calculations are in scope, follow html-and-data-verification.md: trace claims to sources and project data, inspect producing code, recompute consequential quantities, check units, denominators, uncertainty, null models, multiplicity and train/test separation. Record what was verified; distinguish arithmetic checking from reproducing a result from raw inputs.

Verify that files were created and report what remains unresolved. A completed writing task does not imply experiments or source-data repairs are complete.

## 9. Figures: contract, standards, production, release

Read figure-production.md, figure-craft-and-information-density.md and figure-standards-nature-science.md for any figure task, plus figure-design-and-audit.md and its companion contracts for project figures.

**9.0b Legend, tick and significance gate.** Legends, direct labels and series text must
not cover data, intervals, matrices or structures. Use one-word labels for short series;
move more than four series to a horizontal header legend or a reserved right column. Keep
direct labels as an axes-fraction stack and remeasure after final panel scaling. Resolve
crowded ticks without deleting x or y axis titles; preserve at least two interpretable
ticks per axis and select categorical labels evenly from rendered bounding boxes. Derive
panel letter and title height from the actual top tick. Linear extrema must not touch the
frame; non-negative proportions keep zero and add upper headroom. Significance brackets
come only from a real same-group, same-unit, same-denominator, same-direction comparison,
with forest q values outside the plotting area. Require `zero_text_collisions`,
`zero_legend_data_occlusion`, `axis_tick_completeness` and `typography_compliant`.

**9.0c Star and horizontal-legend gate.** Use `****/***/**/*/n.s.` inside figures and
keep exact q values in caption and source table. Continuous effect curves show the matching
CI band; one continuous significant run labels representative first, middle and last points,
with state changes and the last point retained. The default legend is a horizontal
multi-column band below the title; direct endpoint labels are second choice and a right
column is last. Header legend, panel title and letter bboxes must remain separate.

**9.0 AI figure gate.** Classify every figure before choosing a tool: data figure, conceptual schematic, graphical abstract/cover, AI-assisted layout or AI-assisted processing. Data figures use real data and code; a generative image model must not create or alter them. Conceptual AI-assisted figures need journal permission, disclosure in Methods/legend/cover letter, human verification of every label and relationship, a conceptual label, and a provenance record (tool/version/date/prompt/output hash/manual edits). Covers and graphical abstracts need editor permission. Check the journal policy before generation; policies differ and change. Full policy and negative list: ai-figures-and-visual-integrity.md.

**Figure-level claim and evidence architecture.** Start from one Results-level question and one figure-level claim; state what could overturn it. Give panels distinct inferential roles (setup, representative example, primary quantitative evidence, baseline/control, decomposition, stratification, orthogonal validation, perturbation/stress test, boundary/failure case, mechanistic evidence). Prefer role diversity over metric diversity; a mirror layout of the same metric is one role, not four. Use a chain: establish → compare/control → stress-test/discriminate → broaden → bound. Across figures, each figure should raise the next question rather than repeat “X performs well”.

**9.1 Contract.** Write the figure's one-sentence conclusion, archetype, panel map (each panel one question), evidence hierarchy, statistics, source-data mapping and reviewer risks before coding. Every panel answers a unique question; the hero panel gets the clearest axis and largest area; controls stay quieter.

**9.2 Journal specifications (verify at submission).**
- Nature: 89 mm single, 183 mm double, 120–136 mm 1.5 column; page depth 247 mm; Helvetica/Arial; text 5–7 pt; panel letters 8 pt bold lowercase a, b, c; line weights 0.25–1 pt; raster 300–600 dpi RGB; vector EPS/PDF/AI preferred; avoid red–green contrast.
- Science: 55 mm single, 120 mm 1.5, 183 mm double; Helvetica/Arial; 5–7 pt; uppercase bold A, B, C; ≥300 dpi photographs, 600 dpi line art; PDF/EPS/AI.
- Design at final printed size; never shrink key text below 5 pt. The author's HTML/project overlay uses larger roles (10 pt text, 10.5 pt axis, 11 pt bold panel titles, 11.5 pt structure titles, 12.5 pt panel letters) and must not be mixed with journal print sizes in one deliverable.

**9.3 Panel construction.** One data plot per panel; no inset axes, subplot mosaics, facet grids, nested colour bars or miniature assembled plots inside one panel. Combine several measurements in one coordinate system through shared position/unit/shape/line style/direct labels; otherwise move supporting evidence to caption, source table or a separate panel. Sequence/residue tracks may keep aligned layers only on one positional coordinate. Panel order follows the reader's reasoning: system/design → primary comparison → mechanism/localisation → quantification → robustness/validation. Three-panel complete rows; 3×2 for six; 3×3 (nine analytical panels) default for project composites; five-panel plates are 3+2 centred; 7/8/10/11 mixed rows fail project release.

**9.4 Project release gates** (details and thresholds in the four project figure references):
- Fixed physical axes grid; square data boxes (0.9–1.1, target 1.0) measured in rendered pixels after typography; equal axes width/height within 0.01 mm; equal-role panel areas within 5%.
- Complete-boundary gutters 0.38–0.42 × panel width, default 0.40, measured after final ticks/legends and unchanged at save.
- Panel letters anchor the complete cell (≈0.20 × panel width left, ≈0.20 × panel height above the data box, ≥4 mm above, ≥3 mm from the title); titles single-line, bold, centred; axis titles present on every analytical axes.
- One evidence track plus nine analytical panels (letters a, then b–j); no detached mini-plots.
- Semantic colour roles stable across panels; evidence state encoded by fill/shape/hatch/outline; ≤3 chromatic categories plus neutral; no jet/rainbow/hsv; text contrast ≥4.5; no matrix-cell text; colour audit files written.
- Structure rasters cropped to ink, aspect preserved, ≥85% content extent, internal blank bands <14%, outer margin ≤5%; structure and statistics share residue/state/colour mapping; Baker-standard structural requirements apply.
- Text-text, text-canvas and text-mark collisions checked for every artist type (scatter, line collections, intervals, bars, identity lines), with per-axes records; legends sized before rendering; no compression of designed gutters after rendering.
- Every panel has enough evidence: effect, uncertainty, sample distribution, null/control, holdout and transfer shown in distinct panels when available; reject naked axes, isolated mean bars, single points and threshold-free curves when richer evidence exists.
- State in prose, after each figure group, what was found, which comparison establishes the regularity, what relationship it supports and where interpretation stops. The caption inventories panels; the body explains the science.

**9.5 Caption grammar.** Claim title → panel-by-panel present-tense description → statistics (n, n definition, centre/spread, test, correction) → symbols/colours → source-data/permission line. 100–220 words for research figures, 80–150 for reviews (Nature style ≤300). No numbers in the title line; no method inventory.

**9.7 Conceptual figures for Perspectives and theory papers.** Design one integrated composition per figure, not a collage of unrelated panels. Use a pure white background, flat vector-like artwork, no gradients/shadows/3D, a limited colour-blind-aware palette, at least 75% diagram area, fewer than about 45 words, lowercase panel letters and a "conceptual; no measured results" footer where appropriate. State the figure-level claim, panel roles, exact text inventory and scientific constraints before generating or drawing; check every label, equation, arrow and disclaimer. Detail: nature-perspective-production.md; brief template: assets/templates/conceptual-figure-brief.md.

**9.6 Per-panel deliverables and supplementary figures.** For SEAL work, read seal-supplementary-figure-standard.md in full before creating or auditing any main or supplementary figure. The panel is the delivery unit: every declared panel is exported as its own editable SVG carrying its own letter, axes, ticks, marks and annotations; the composite must be reproducible from those panel exports. Deliver composite SVG, vector PDF, 600-dpi PNG and JPG, one SVG per panel, one SVG per shared legend or scale bar, the caption, a panel-definition record and an audit record. Automated collision counts are screening only: open every figure at final size and inspect panel by panel, and record the inspection. Labels sit in a margin label stack with leader lines when anchors are close; the row gap must exceed the previous row's x tick labels plus the next row's title band. The SEAL 28-figure release gate requires one regeneration pass with 8 pt ordinary text, 10 pt axis labels and panel letters, 0.4 pt axis/tick strokes, 0.9–1.1 data boxes, zero collisions, 600-dpi PNG, parseable SVG, one-page PDF, current panel SVG links and browser checks at desktop and mobile widths.

## 10. Revision, polishing, formatting and response

- Polishing repairs reasoning before rhythm: check section/paragraph job, claim → evidence → boundary, hourglass, topic sentences, then grammar and register. Change only flagged passages; keep the rest verbatim; if a fix forces structural change, state it and confirm.
- Section moves, phrasebank by evidence strength, style guardrails and overclaim checks are in revision-and-response.md.
- Response letters: strategy summary → tracker → point-by-point letter → change checklist → risk flags. Preserve reviewer comments verbatim; map every item to an action and manuscript location; never invent experiments, citations, line numbers or panels; use AUTHOR_INPUT_NEEDED when facts are missing. Disagree narrowly with evidence, never personally; treat misunderstanding as a presentation signal.
- Pre-submission review: three reviewer reports plus synthesis across originality, scientific importance, interdisciplinary interest, technical soundness and non-specialist readability; flag unsupported or non-assessable claims.
- Formatting: apply the target journal structure, reference style, statements, figure placement, equation rendering (MathML/TeX) and line numbering without changing scientific meaning; flag discrepancies rather than silently "fixing" numbers or author lists.
- Submission package and editorial audit: determine stage (initial, revision, accepted-in-principle, proof); verify journal/article-type limits; build the deliverable matrix; draft cover letter, title page, declarations and reviewer suggestions from author-confirmed facts; run the editorial criteria and broad-interest audit; return ready / ready_with_author_checks / blocked. Detail: editorial-and-submission.md; templates in assets/templates/.
- Editing fidelity: record the mode, protect the author's claim order and wording, keep the source unchanged, use tracked changes/yellow highlights on a copy, and return a change log plus residual questions.
- Proofreading: run the five passes, then verify numbers, units, statistics, references, figure/table citations and markup; list residual author questions instead of guessing.
- AI integrity: check the journal policy, log AI-assisted tasks, remove confidential material, verify AI-suggested references/numbers, draft the required disclosure and confirm the final text is human-defensible.
- AI negative gate: run the AI-writing negative list and, for any AI-assisted figure, complete the image provenance record and AI-use negative checklist. Verify no fabricated citations/data/images, no undisclosed AI, no data or patient leakage, and no copyright/licence problem.

## 11. Final quality check

- Every annotation addressed or explicitly identified as blocked.
- Each analysis states its purpose before its results.
- Every abstract sentence has a concrete object or defined term; abstract length matches the venue.
- Claims use calibrated verbs; uncertainty stated once, where it matters; no generic defensive language or promotional adjectives.
- Numbers carry unit, comparison and denominator; statistics have n, test, correction and effect size.
- Paragraphs have one move and a topic sentence; no list-paragraphs or module catalogues.
- Author-approved terminology and adjacent sections agree; terminology ledger enforced.
- References support their sentence; publication status and DOI verified; style consistent.
- Figure contract, panels, journal specs, typography, colour roles, gutters, collisions, structure rasters and captions pass the gates above; figure/panel numbering matches text and legends.
- Complete manuscripts include title page, abstract, main text, methods, references, legends, extended data, statements and change log; missing inputs are listed, not invented.
- Chinese and English align paragraph by paragraph; bolding represents actual changes.
- Closing paragraph names a specific scientific consequence, not a promise.
- Zero-tolerance style ban passes: no template contrast ("not X but Y"), defensive disclaimers, self-limiting framing, outline-like transitions or their Chinese equivalents; the prose style checker reports no ERROR hits.
- Defensive-argument gate passes: one limitation paragraph only, no abstract or conclusion caveat, every hedge survives the deletion test, the headline claim carries a number and a condition, and check_prose_style.py --gate reports no defensive/AI marker and no out-of-band rhythm metric (sentence-length CV, recap tails, triads, nominalisation, em dashes).
- Perspective/theory package: one thesis, six-section logic, five-level evidence ledger, full paragraphs, no lists in the argument, boundaries in one paragraph, 2–3 bold single-sentence insights per subsection, conceptual figures with legends at the end, references before periods and placeholder fields marked.
- Bilingual parity: identical claims, numbers, citations, certainty and emphasis; natural Chinese prose and matching academic English.
- Text reads as a scientific argument a biologist can follow without decoding AI jargon.
- Frontier and novelty claims have a dated search record and verified primary sources.
- Consequential numerical claims agree with source data, calculations, tables, figures and units.
- Response package covers every editor/reviewer item with action, location and remaining limitation.
- Per-panel SVG deliverables exist for every declared panel; composite, PDF, 600-dpi PNG/JPG, caption and audit record agree; SEAL supplementary figures pass the 28-figure release gate.
- Innovation is classified and positioned; the gap is a scientific unknown; competing explanations have discriminating predictions; why-this/why-now/why-broad are answerable without adjectives.
- Editorial criteria, broad interest and journal fit are assessed in one sentence each; the cover letter and significance statement match the manuscript's actual claims.
- Every result has an assigned destination; the shortest sufficient evidence chain is in the main text; SI does not hide conclusion-changing results; revision additions pass the deletion check.
- Statistics define the independent unit, n, error definition, test, tail, correction and exact values; Reporting Summary, image integrity and data/code/materials statements are complete and consistent.
- Figure panels have distinct inferential roles; figure order escalates; information density is adequate; the caption contract and journal stage-specific figure requirements are met.
- HTML figures are audited at their final CSS width; source raster width, save dpi, displayed width and effective point size are recorded together, and nominal 10 pt text remains at least 10 pt after browser scaling.
- Fixed grids use one physical canvas and complete-cell gutter contract. Long labels, legends and ordered length-by-condition combinations cannot widen a column; ordered variables remain continuous and use shape, colour and hatch for secondary conditions.
- The submission package is complete for the recorded stage; missing facts are marked, not invented.
- AI use follows the target-journal policy: no AI authorship, no fabrication, no confidential uploads, disclosed where required, every AI-suggested citation/number verified.
- AI writing negative list passes: no fabricated references/data/results, no citation manipulation, no paper-mill patterns, no undisclosed translation/ghostwriting, no detection evasion.
- AI figure gate passes: data figures from real data/code; conceptual AI figures disclosed, labelled and verified; provenance record complete; no synthetic research images, generative fill, fake scale bars or undisclosed cover art.
- Literature search and citations are documented and verified; synthesis is by question/mechanism; preprints/retractions handled.
- A five-pass proofread is complete; numbers, units, statistics, references, figure/table citations and markup are consistent.
- Section craft passes the abstract hidden-names test, Introduction reverse outline, Results claim ladder and Discussion synthesis audit.
- Perspective work has one intellectual centre, a discovery sequence, marked evidence status and a concrete ending.
- Files exist, are the audited versions, and unresolved items are reported.

## 13. v1.2.6.6 projection, structural cartoon and HTML bold gates

- Projection panels take limits from the full data extent and record
  clipped_point_fraction = 0; PCA/t-SNE/UMAP use equal x/y unit length, equal spans and a
  square axes box.
- Fold-evidence panels use cartoon/ribbon geometry, never surface only; non-focal loops and
  contexts are grey at 20% transparency, and each structure tile carries an auditable label
  band that never covers molecule ink.
- Before rendering, validate the structure file: element columns, guide atoms equal to
  C-alpha count, non-empty FASTA. Rewrite element columns and record SHA-256 when validation
  fails.
- In HTML reports, bold the topic sentence of each Results subsection, decisive numbers and
  logical turns, the abstract's conclusion and each figure caption's inference clause (1-3
  spans per paragraph, never the whole paragraph).
- Display figures as 600 dpi raster and link SVG/PDF separately; confirm the page paints the
  figure by screenshot at its vertical position, not only by naturalWidth.

## 14. v1.2.6.7 evidence-density and visual-finish gates

- Every analytical panel has at least three evidence layers (observations, distribution, estimate with CI, reference, effect size, contrast, structural annotation); the count is audited.
- No means-only bars and no single series without a band, points or rug; a two-bar panel requires a companion distribution in the same figure.
- Do not repeat the same chart across algorithm, rule and environment without adding a distribution, contrast or mechanism layer.
- No default black whiskers or edges; use semantic fills and an alpha hierarchy.
- Each figure row carries a distinct evidence role; dimension-swap repetitions fail.

## 15. v1.2.6.8 data-extent gates

- Every quantitative panel covers the full data extent on both axes; hard-coded stale limits fail.
- Threshold views either extend to the full range or carry a full-range companion in the same panel.
- The panel-extent audit records clipped-point counts and overshoot; all panels pass.
- Inverted, log and image/matrix axes are audited in value space; legend proxies and default collection offsets are ignored.
- After changing limits, explicit ticks replace auto-locators that would fall outside the view.

## 16. v1.2.6.8 addendum gates

- Audit every data-artist path (PolyCollection, LineCollection, patches, images), not only scatter offsets.
- Violin/KDE bodies extend beyond the observed data range by about 1.5 bandwidths; flat caps fail.
- Density contour grids extend about 6% beyond the observed data range.
- Points at 0, 1 or thresholds receive a marker margin of 2–4% of the axis span.
- Rendered rasters are checked at final display width; HTML serves versioned raster URLs or no-store headers.

## 17. v1.2.7.0 defensive-writing control and AI-prose gates

A manuscript fails stylistically for two reasons that look different and are cured by one decision: it argues against itself (defensive writing), or it argues nothing in particular (generated prose). Decide what the paper wins, then spend every paragraph on it. Argument-level rules: defensive-writing-and-argument-selection.md; surface patterns: writing-diagnostics.md section 3A and 4A.

- **Argument selection precedes wording.** Name the one claim this paper alone can make, with its measure and its condition. If "what do we win / by how much / on what ground" has no number and no condition, the analysis is unfinished; prose cannot repair it.
- **Space follows argument, not effort.** Every experiment carries one duty — existence, mechanism, regime, exclusion or value. Experiments with no duty are deleted, merged or demoted. Chronology ("we first did X, then tried Y") is banned; failed branches appear only when they exclude an alternative a reader would hold.
- **One limitation paragraph.** At most three sentences, condition -> scope -> consequence, at the end of the discussion. Zero limitation sentences in the abstract and in the conclusion; a caveat that qualifies one result stays in that result's sentence.
- **Deletion test for every hedge.** Remove it, then ask whether a careful reader could now be misled about what was measured. If not, delete it; if so, keep it and make it specific. Rhetorical hedging is banned; epistemic calibration is mandatory.
- **The ban is never a licence.** No claim without evidence, no deletion of a limitation that changes the reading, no null rewritten as a positive, no generalisation past the system, no hidden comparator. Statistics, reporting integrity and AI-use rules override every stylistic preference in this skill.
- **Rhythm is part of the diagnosis.** Targets: sentence-length CV 0.30-0.65; recap tails <=1 per 1,000 words; triads <=2 per 500 words; nominalisation <=12% of content words; em dashes <=2 per 1,000 words; hedge markers <=4 per 1,000 words (English) and <=3 per 1,000 characters (Chinese); limitation markers <=2 per 1,000 words. Run python tools/check_prose_style.py --gate <file>; a defect is an ERROR hit, a defensive/AI marker or an out-of-band metric. Use --genre perspective for proposals and theory papers, where proposal modality is calibration rather than hedging, and --genre report for reports, where the metrics are informational.
- **Scope.** Manuscript, abstract, cover letter, response letter, figure text, reports and Chinese drafts. Chinese-specific forms (self-deprecating 谦辞, procedural narration, hollow modifiers, four-character parallelism) are listed in the Chinese reference and checked by the same gate.

## 18. v1.2.8.0 journal templates and manuscript assembly

Default target is **Nature**; Science is the second supported format. A manuscript is delivered as a document that must pass mechanical checks, so assemble it into a template instead of hand-formatting it.

- **Authoritative files.** Specs in assets/journal-templates/specs/ (page, type, section order, caps, reference style, figure widths), the template in assets/journal-templates/generated/ or .../official/, the builder tools/build_manuscript.py, the checker tools/check_journal_format.py, and the source registry tools/journal_template_sources.json. Every spec block carries a confidence tag: official, secondary or default.
- **Assemble.** python tools/build_manuscript.py draft.md --journal nature --out build/draft.docx --report build/draft.json. Input is markdown with level-2 section headings or an equivalent JSON; Introduction, Results and Discussion fold into the main text as level-3 subheadings; [1]-style citations become superscripts; authors and affiliations come from front matter and are never generated.
- **Section order is fixed.** Nature: Title, Authors, Affiliations, Abstract, Main text, References, Acknowledgements, Author contributions, Competing interests, Figure legends, Tables, Methods, Data availability, Code availability, Extended Data. Methods sits after the reference list; placing it after the Introduction is the most common mechanical rejection.
- **Verify.** python tools/check_journal_format.py build/draft.docx --journal nature. Critical checks (page, margins, continuous line numbers, body and abstract font, size and spacing, required sections, section order, superscript citations) must PASS; abstract length and reference count are warnings that must be written down when exceeded.
- **Official templates.** python tools/fetch_journal_templates.py --list shows the publisher pages; --from-dir imports a browser download; --check verifies it. Pass --template to the builder, which keeps the official styles and clears the body. Never edit a template's styles to fit the text.
- **Submission gate order.** Assembly -> format -> prose (section 17) -> claims and statistics -> figures -> package. All six pass before submission; a warning is not a pass until it is recorded as a deliberate decision.
- **Honest limits.** Spec values are compiled and cross-checked but publishers change them; re-verify at submission and update the spec. The package neither bypasses publisher interstitials nor redistributes publisher templates.

