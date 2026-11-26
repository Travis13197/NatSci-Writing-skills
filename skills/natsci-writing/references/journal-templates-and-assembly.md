# Journal templates and manuscript assembly

A manuscript is delivered twice: as an argument (sections, claims, evidence) and as a document that must pass a journal's mechanical checks before an editor reads a word. This file owns the second: it turns a drafted manuscript into a format-correct file, and it verifies the result. **Default journal: Nature.** Science is the second supported target.

## 0. What is authoritative here

| Layer | File | Role |
|---|---|---|
| Spec (single source of truth) | assets/journal-templates/specs/nature-article.json, science-research-article.json | page, type, section order, limits, reference style, figure widths |
| Template | assets/journal-templates/generated/ or .../official/ | the .docx the manuscript is assembled into |
| Builder | tools/build_manuscript.py | fills the template from markdown or JSON |
| Checker | tools/check_journal_format.py | verifies the produced document against the spec |
| Source registry | tools/journal_template_sources.json | where the publisher's own templates live |

The spec carries a confidence tag per block: official (stated by the publisher), secondary (third-party summary), default (our safe fallback). The checker fails only on critical structural and typographic items; limits such as abstract length and reference caps are reported as warnings, so a deliberate deviation is visible rather than fatal.

## 1. Templates: generated vs official

Publisher pages sit behind interactive interstitials. This skill therefore ships two routes.

1. **Generated template** (default, always available): tools/make_journal_template.py builds a .docx that encodes the spec exactly - page size, 1-inch margins, 12 pt Times New Roman, double spacing, continuous line numbers, page numbers, and one style per element (NSC Title, NSC Body, NSC Abstract, NSC Reference, ...). It is our own artefact, so it travels with the package.
2. **Official template** (preferred when present): download it in a browser from the page listed by the tool below, then import it.

~~~bash
python tools/fetch_journal_templates.py --list
python tools/fetch_journal_templates.py --from-dir ~/Downloads
python tools/fetch_journal_templates.py --check
~~~

The builder then opens the official file, clears its body and keeps its styles:

~~~bash
python tools/build_manuscript.py draft.md --journal nature \
  --template assets/journal-templates/official/nature-template.docx
~~~

Never edit an imported template's styles to fit the manuscript; change the manuscript or the spec, and record why.

## 2. Nature (default)

| Parameter | Value | Confidence |
|---|---|---|
| Page | A4, 1-inch margins, page numbers | secondary |
| Body | Times New Roman 12 pt, double-spaced (2.0), left-aligned, no space before/after | secondary |
| Title | Arial 14 pt bold | secondary |
| Headings | Arial 12 pt bold | secondary |
| Captions / tables | Arial 10 pt | secondary |
| Line numbers | continuous, page 1 to the last page | secondary |
| Abstract | 150-200 words, unreferenced, one paragraph | secondary |
| References | numbered by first citation, superscript in text, cap 50 (Article) | secondary |
| Display items | up to 8; single column 89 mm, double 183 mm, at least 300 dpi | secondary |

**Section order** (must not be rearranged): Title, Authors, Affiliations, Abstract, Main text, References, Acknowledgements, Author contributions (optional), Competing interests, Figure legends, Tables (optional), Methods, Data availability, Code availability (optional), Extended Data (optional). Methods sits after the reference list, not after the Introduction: this inverted order is the most common mechanical rejection cause.

## 3. Science (second target)

| Parameter | Value | Confidence |
|---|---|---|
| Page | Letter, 1-inch margins | secondary |
| Body | Times New Roman 12 pt, double-spaced | secondary |
| Abstract | 100-125 words, unreferenced | secondary |
| References | numbered, superscript in text, cap 80, section titled References and Notes | secondary |
| Display items | up to 7; 55 / 121 / 183 mm widths, at least 300 dpi | secondary |
| Letters on panels | uppercase bold, 8 pt, top-left | secondary |

**Section order**: Title, Authors, Affiliations, Abstract, Main text, References and Notes, Acknowledgments, Funding (optional), Author contributions, Competing interests, Data and materials availability, Supplementary Materials (optional), Figure legends.

## 4. Assembly

The input is markdown whose level-2 headings name sections, or a JSON file with the same structure:

~~~markdown
---
authors: A. B. Author, C. D. Author
affiliations: 1 Institute of Molecular Systems, Example University
---

# Title sentence carrying the claim

## Abstract
150-200 words (Nature) or 100-125 (Science), no citations.

## Introduction
## Results
### A residue-level readout beats the pooled baseline
## Discussion

## References
1. Author, A. B. et al. Title. Nature 555, 1-9 (2018).

## Methods
## Acknowledgements
## Author contributions
## Competing interests
## Data availability
## Figure legends
~~~

Introduction, Results and Discussion all fold into the main text and become level-3 subheadings; nothing is emitted twice.

Rules the builder enforces: sections are emitted in spec order; [1]-style citations become superscripts; repeated main-text headings become subheadings instead of duplicate blocks; missing required sections are reported, never invented; front matter supplies authors and affiliations (never auto-generated).

~~~bash
python tools/build_manuscript.py draft.md --journal nature \
  --out build/draft-nature.docx --report build/draft-nature.json
python tools/check_journal_format.py build/draft-nature.docx --journal nature
~~~

## 5. The submission gate order

Run the gates in this order and fix the first failure before the next gate:

1. **Assembly** - build_manuscript.py; missing= must be none, or every missing item listed and justified.
2. **Format** - check_journal_format.py; all critical checks PASS, warnings acknowledged.
3. **Prose** - check_prose_style.py --gate (section 17): no ERROR, no defensive/AI marker, no out-of-band metric.
4. **Claims and statistics** - the claim ledger and the reporting checklist: every number has n, test, correction and effect size.
5. **Figures** - figure contract, panel roles, widths and dpi from the spec, captions matching the legends.
6. **Package** - statements, reporting summary, cover letter and a change log; nothing marked verify-at-submission left unresolved.

A manuscript is submitted only when all six gates pass. A warning is not a pass until it is written down as a deliberate decision with its justification.

## 6. Honest limits

- The spec values are compiled from the published requirements and cross-checked against a 2026 secondary summary; publishers change them. Re-verify at submission and update the spec, not the manuscript.
- The official Word/LaTeX templates are downloaded by the author in a browser; this package does not bypass publisher interstitials and does not redistribute publisher files.
- LaTeX output is a skeleton that mirrors the spec's page setup and section order; for LaTeX-heavy venues, assemble in LaTeX and check the PDF against section 5.
- The checker verifies what a .docx exposes (page, styles, spacing, headings, counts). It cannot judge whether the argument is right; sections 2-5 of this skill do that.
