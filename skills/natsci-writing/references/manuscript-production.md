# Manuscript production: complete drafts, revisions and formatting

Version 1.1.0; updated 2026-11-23. Read when the task is to produce a complete manuscript or section, rebuild a paper's architecture, convert/format a manuscript, or prepare a submission package. This file integrates the nature-skills writing system with the corpus-calibrated standards in SKILL.md.

## 1. Deliverable modes and routing

| Mode | Input | Output |
|---|---|---|
| Complete draft | idea, data, figures, notes, or Chinese draft | Full manuscript in target journal structure, with assumptions and missing-input list |
| Section draft | section request plus claims/evidence | One or more complete sections, ready to paste |
| Rebuild | existing draft with structural problems | New architecture plus rewritten sections, tracked |
| Polish/revise | finished or near-finished prose | Sentence- and paragraph-level revision with change log |
| Format conversion | manuscript plus target journal | Journal-compliant layout, references, statements, figure legends |
| Figure set | data plus claim | Publication-grade figure files plus captions and source-data map |
| Response package | reviewer comments plus revision facts | Point-by-point response, tracker, change checklist |
| Pre-submission review | manuscript | Three reviewer reports plus cross-review synthesis |

Ask for missing essentials only when the answer changes the deliverable: core claim, evidence, boundary, target journal, section scope. If essential input is absent, produce a scaffold with explicit placeholders rather than inventing content.

## 2. Intake and confirmation gate

Before drafting a full section, extract and echo back:
- **One-sentence argument**: In [system/problem], we show [advance] using [approach], supported by [evidence], with [boundary].
- **Paper type**: research / methods / algorithmic / hypothesis / review.
- **Plan**: target journal, word limit, sections to draft, paragraph map (one job per paragraph).
- **Terminology ledger**: canonical forms for methods, models, datasets, metrics, abbreviations; flag collisions.
- **Reader lead question**: relevance, novelty, trust, reuse or meaning — the abstract/introduction should answer them in that order.
- **Assumptions and at most 2–3 high-leverage questions**.

Then stop for confirmation when the claim, evidence or framing is ambiguous. If the user supplies complete claim/evidence/framing, state the argument in one line and proceed. For a long manuscript, offer the outline first; reacting to an outline is cheaper than reacting to full prose.

## 3. Terminology ledger

One name for one thing across title, abstract, main text, figures, tables, supplement and response letter. Record canonical term, first-use expansion, variants in the source, decision. Do not coin names for the author's methods; ask or flag. Reuse the ledger on every later section; if a term changes, change every occurrence.

## 4. Full-manuscript pipeline

1. **Brief and scope**: target journal, article type, audience, length, deadline, existing materials.
2. **Argument**: one-sentence argument; contribution type (mechanism, capability, measurement, resource, theory); nearest prior work.
3. **Evidence map**: each claim → figure/table/analysis → strength → boundary. Mark unsupported claims as gaps.
4. **Architecture**: choose the paper-type playbook and section word budget; write the paragraph map (each paragraph one job).
5. **Abstract and title drafts**: draft early as orientation, finalize last.
6. **Draft in evidence order**: Results first, then Introduction/Conclusion, Discussion, Methods, Abstract, Title. This prevents the Introduction from promising results the paper does not deliver.
7. **Section pass**: apply the section playbooks (Section 6).
8. **Consistency pass**: terminology, numbers, units, figure/panel references, citation numbering, tense, claim strength.
9. **Adversarial self-review**: rejection-risk checklist (Section 11); fix claims, evidence presentation, or scope.
10. **Package**: manuscript, figures, legends, statements, references, supplement, cover letter if requested.

Drafting order for a research paper: Results → Introduction and Conclusion → Title → Discussion → Methods → Abstract. For a methods/algorithmic paper: Methods → Results/benchmarks → Introduction → Discussion → Abstract.

## 5. Section playbooks

### Title
Concrete and searchable: system/object + capability/action + application/consequence. 8–12 words is typical; Nature titles are compact noun phrases. Avoid grant-style aims ("Toward…", "A study of…"), unverified "first", slogans and unexplained jargon. Generate 3–5 alternatives spanning declarative, finding-led and (rarely) question forms; mark the most defensible; verify any quantitative claim.

### Abstract
Nature research: ~200 words, 7–8 sentences, staged as broad field → sharper background → exact problem → "Here we show" main result → what the result changes (2–3 sentences) → bounded broader context. Science research: ~125 words, 5–6 sentences, ending on consequence. Never begin with "Here we show" before enough context; never end with a generic promise.

Nature summary paragraph internal logic (use when drafting or rebuilding a Nature abstract):
1. 1–2 sentences field context understandable to a non-specialist.
2. 2–3 sentences specific background and the minimum concepts needed.
3. One unmistakable gap sentence.
4. One main-result sentence with "Here we show" or equivalent.
5. 2–3 sentences interpreting what the result changes, not listing more results.
6. 1–2 sentences broader context, anchored in the evidence.
7. Optional 2–3 sentences wider perspective; total may reach ~250–300 words only when the journal allows.

Default abstract movement for other venues: context/problem → why current routes fall short → what this paper introduces → strongest result with number/comparison → mechanism or consequence → bounded implication. The abstract is a mini-paper, drafted last and revised most.

### Introduction
Controlled funnel: field stake → bottleneck in existing practice → prior work and what it has/has not solved → remaining capability gap → present study as the direct response. Four paragraphs is typical. Explain the transition from "what is known" to "what this paper does" explicitly. Cite to position, not to demonstrate breadth. Do not summarize results or numbers in detail; the final paragraph previews the contribution and approach.

Common variants (state which you use): task-then-application; application-first; general-to-specific; open-with-challenge; novel-task-challenge-decomposition; technical-challenge; pipeline/module framing.

### Results / Experiments
Evidence ladder: system/workflow validation → main result → fair baseline comparison → mechanism/ablation → application/generalization → stress tests/failure modes. Each subsection opens with the question, then the design, then the observation with quantitative support, then the inference. Use past tense for what was observed; keep interpretation short unless deliberately transitioning to Discussion. Every major claim needs comparison, ablation or stress-test evidence; mark unsupported claims as follow-up needs rather than drafting around them. Do not hide a main-text result in supplementary material; do not repeat every visual detail from the figure.

### Discussion
Interpret, do not re-summarize: central advance → what the evidence means → rival explanations → relation to prior work (support/revise/complicate) → specific limitations and where the claim stops → what is now testable or usable. Hedge where interpretation requires it; do not promote "consistent with" to "demonstrates". Limitations must name the actual condition/dataset, not generic modesty. End on a concrete opportunity or open measurement, not praise.

### Conclusion
Four-part close: central contribution → decisive evidence → implication → boundary. No new data, citations or mechanisms. The implication must be narrower than or equal to the evidence scope.

### Methods
Reproducibility test: could another group repeat the work from this description plus cited protocols? Structure: design/cohort → materials or data source → procedure → outcome measures → analysis and statistics → ethics. State inputs, transformations, test definitions, controls, software/resource versions and parameters actually verified; do not fill unknown settings with defaults. Never leave vague phrases such as "under standard conditions", "using routine methods", "data were analysed statistically", "samples were randomly assigned" without the mechanism.

### Related work (where the venue requires it)
Group prior work by approach or assumption, not paper by paper; state what each line achieves and where it fails for the present problem; end at the gap the paper addresses. Do not use related work to postpone stating the contribution.

## 6. Paper-type playbooks

| Type | Argument chain | Drafting order | Key evidence requirement |
|---|---|---|---|
| Research | field need → bottleneck → move → decisive evidence → implication → boundary | Results first | each claim has comparison/ablation/stress test |
| Methods | task → limits of existing methods → proposed method → fair evaluation → reproducibility → boundary | Methods first | baseline, protocol, failure modes |
| Algorithmic | problem → limitations → model/system → fair comparison → ablations → generalization → boundary | Methods/architecture first | split discipline, seeds, metric definitions |
| Hypothesis | observation → competing explanations → discriminating prediction → targeted test → mechanism decision | Results/testing first | a test that separates explanations |
| Review | field state → framework → synthesis by mechanism → disagreement/evidence quality → open questions | Framework first | synthesis, not paper-by-paper summary |

## 7. Journal formats (verify current author guidelines at submission)

| Venue | Abstract | Main text | Display items | References |
|---|---|---|---|---|
| Nature Article | ≤200 words, staged summary paragraph | ~2,500 words (6 pages) or ~4,300 (8 pages); subheadings ≤40 characters | 4–6 main figures | ≤50 |
| Nature Review | ≤200-word preface ending in summary sentence | <7,000 words; one topical aspect | 4 display items; boxes welcome | ≤150 |
| Nature Perspective | Same as Review; personal, forward-looking, narrower | Argued essay | 1–4 | Selective |
| Science Research Article | ~125 words, 5–6 sentences | Results-led; no strict page model | 4–6 main figures | Journal style |
| Science Review | ~120 words | Synthesis with framework | 3–4 figures | Journal style |
| Science Perspective | One-sentence teaser (~11 words) | Short argumentative essay | 0–2 | Selective |
| Nature Communications | ~150 words, broad readership | Flexible | 4–8 | Journal style |

Use the target journal's current guide, not a remembered limit, when compliance is requested.

## 8. Complete-manuscript package

For a complete draft, deliver:
1. **Title page**: title, authors and affiliations (placeholders if unknown), corresponding author, keywords if required.
2. **Abstract** in journal structure, plus a Chinese version when the workflow is bilingual.
3. **Main text** with section headings and paragraph-level argument.
4. **Methods** with reproducibility detail and statistics.
5. **References** verified and formatted, with in-text numbering before punctuation (author preference) unless the venue requires otherwise.
6. **Figure legends** matching the actual panels; figures as separate files.
7. **Extended Data / Supplementary** list with legends.
8. **Statements**: data availability, code availability, author contributions, competing interests, acknowledgements, ethics/consent where relevant.
9. **Assumptions and missing-input list**: what the author must supply, marked visibly.
10. **Change log** for revisions: location, old text, new text, reason.

Output formats: Markdown for review, DOCX for co-authors, LaTeX when the venue requires it, HTML for interactive review. Keep a single source of truth for numbers; generate tables from source data rather than retyping.

## 9. Formatting conversion

- Preserve content and scientific meaning; change layout, not claims.
- Apply the target journal's structure: title page fields, abstract heading, section order, figure/table placement, reference style, line numbering, page size and font.
- Nature-style references: numbered, authors surname + initials, article titles included; Science style follows its current guide. Do not mix styles within one manuscript.
- Equations: MathML or a real TeX renderer for display equations; Unicode pseudo-subscripts are not equations. Verify fractions, subscripts, superscripts, norms and Greek symbols in the rendered output.
- In HTML, wrap measured comparisons in strong emphasis while keeping the full sentence and denominator; keep tables in local overflow containers; verify desktop and mobile widths.
- Figure files: vector for line art, 300–600 dpi raster for photographs, RGB, embedded fonts, file names matching figure numbers.
- Do not silently "fix" numbers, author lists, affiliations or funding during formatting; flag discrepancies in a change log.

## 10. Statements and metadata

Data availability: name the repository, accession/DOI, contents, version/date, and restriction route if controlled. Never write "available upon request" without a reason, durable route, eligibility and metadata. Distinguish generated, reused, licensed and controlled-access data. Code availability: repository, release/tag, licence, environment and entry point. Author contributions: use the venue's CRediT-like categories and verify with authors. Competing interests: state actual financial/non-financial interests or "The authors declare no competing interests". Ethics: approval body, approval number, consent procedure. For detailed statement patterns, follow the journal's current policy and the principle that each statement must be durable, specific and verifiable.

Citation management: verify title, authors, year, venue, DOI and publication status before adding; export RIS/BibTeX/Zotero RDF from verified metadata; one record per work; deduplicate; never invent fields. Keep the reference library next to the manuscript.

## 11. Adversarial self-review before submission

Answer with explicit evidence from the manuscript; mark pass / needs revision / needs new data:
- **Contribution**: what new knowledge? Is the failure case meaningful? Is the idea non-obvious? Is the gain surprising rather than predictable? Which novelty type applies?
- **Writing clarity**: could a knowledgeable reader reproduce the method? Is every module's motivation explicit? Are terms and notation consistent? Does each paragraph carry one message?
- **Empirical strength**: are gains meaningful against strong baselines, consistent across datasets/settings, and honestly bounded by failure cases?
- **Evaluation completeness**: ablations for all key choices; recent strong baselines under fair settings; standard and sufficient metrics; challenging datasets; documented protocols.
- **Method soundness**: realistic setting; hidden defects; robustness without per-case tuning; benefits outweigh complexity and new limitations.
- **Journal fit**: broad-interest case, immediate implications, readability for non-specialists.

Revise claims, evidence presentation or scope until no major rejection risk remains.
