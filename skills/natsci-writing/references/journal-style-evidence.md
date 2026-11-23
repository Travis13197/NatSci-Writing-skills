# Journal style evidence: the Nature/Science corpus

Version 1.1.0; updated 2026-11-23. This file documents the corpus behind the writing and figure rules in SKILL.md. Read it when calibrating genre length, claim strength or figure conventions, or when a user asks why a rule exists. It is evidence, not a template: the corpus is a local analysis set, and no full texts are redistributed.

## 1. What was collected

Sources: Nature (flagship) article pages, Europe PMC/PubMed records, PubMed Central full-text XML, and Nature Methods/Nature Biotechnology open-access methods papers. Search and download date: 23 November 2026.

Selection: life science, biotechnology, bioinformatics, protein language models and AI-for-science. Nature records were discovered from journal article-type listings (Perspective, Review Article, Article) and filtered by biological/AI title terms; Science records were discovered from PubMed metadata (2019–2026), classified by publication type, abstract length and page span, then filtered by the same topic terms. Science type labels are therefore format-based estimates for Perspectives (see limitations).

| Source | Perspective / Review | Research Articles | Records | Full text | Figure captions |
|---|---|---|---|---|---|
| Nature | 115 Perspective; 104 Review | 169 Article | 388 | 141 | 1,401 |
| Science | 126 Perspective; 144 Review | 182 Research | 452 | 148 | 716 |
| Nature Methods/Biotechnology (supplement) | — | 28 methods/AI papers | 28 | 28 | 203 |
| Total | 489 long-form | 379 research | 868 | 317 | 2,320 |

Full text means at least 2,000 words of parsed body text. Nature full texts are open-access Articles and Perspectives; Reviews are mostly paywalled, so Review statistics rest on abstracts, captions and eight full texts. Science full texts are PubMed Central deposits. Years: Nature 2020–2026; Science 2019–2026. Topic tiers: AI/protein-language-model, biotechnology/genomics, general life science.

## 2. Measured statistics

Medians unless stated. Rates are per 1,000 words of body text.

| Metric | Nature Article | Nature Perspective | Nature Review | Science Research | Science Review | Science Perspective |
|---|---|---|---|---|---|---|
| Records | 169 | 115 | 104 | 182 | 144 | 126 |
| Abstract words | 208 | 184 | 180 | 125 | 123 | 11 (teaser) |
| Abstract sentences | 8 | 7 | 6 | 6 | 5 | 1 |
| Title words | 9 | 8 | 8 | 10 | 8 | 5.5 |
| Title colon rate | 1% | 10% | 4% | 3% | 31% | 6% |
| Sentence words | 25 | 27 | 27 | 24 | 25 | 26 |
| Sentence p90 words | 45 | 46 | 44 | 42 | 41 | 39 |
| Sentences >40 words | 15% | 17% | 15% | 11% | 10% | 8% |
| Paragraph words | 121 | 320 | 259 | 133 | 136 | 128 |
| First person ("we/our") | 11.1 | 5.1 | 1.3 | 12.7 | 1.8 | 5.5 |
| Passive constructions | 16.5 | 11.5 | 14.7 | 14.3 | 11.0 | 10.1 |
| Hedges | 3.4 | 5.2 | 5.8 | 5.6 | 7.3 | 7.2 |
| Boosters | 4.7 | 2.8 | 4.0 | 5.3 | 4.2 | 1.7 |
| Logical connectives | 3.9 | 4.7 | 6.2 | 4.4 | 6.9 | 5.2 |
| "Not X but Y" / rather than | 0.34 | 0.67 | 0.32 | 0.40 | 0.49 | 1.22 |
| Em dash | 0.8 | 2.8 | 3.7 | 0.5 | 0.8 | 2.0 |
| Semicolon | 4.1 | 2.1 | 1.7 | 3.3 | 1.4 | 0.8 |
| Numerals | 62 | 37 | 65 | 53 | 39 | 12 |
| Figure captions, words | 189 | 85 | 143 | 198 | 114 | 79 |
| Captions stating n | 39% | 2% | 0% | 25% | 1% | 0% |
| Captions stating P value | 14% | 0% | 0% | 11% | 2% | 0% |
| Captions defining error | 53% | 12% | 14% | 44% | 12% | 6% |
| Captions with scale bar | 16% | 2% | 0% | 9% | 0% | 0% |
| Captured figures per paper | 3.0 | 0.5 | 0.2 | 2.8 | 1.3 | 0.1 |

Caption statistics are computed only over captions that were parsed; Review and Perspective figures are under-represented because those articles are largely paywalled. Treat them as lower bounds.

## 3. Findings that shaped the skill

1. **Nature and Science abstracts differ in length, not in structure.** Nature Articles run ~200 words and 7–8 sentences; Science Research Articles ~125 words and 6 sentences. Both move from context to gap to approach to result to consequence; Nature marks the pivot with "Here we show".
2. **Abstracts are longer than the informal "150-word" rule.** Nature's own guidance is ≤200 words, and the measured median is 208 (including the author summary and structured phrasing). Do not compress a Nature abstract to 150 words without an editorial reason.
3. **Paragraph length depends on genre.** Research Articles: 120–140 words, 4–5 sentences. Reviews: 150–260 words, 6–9 sentences. Nature Perspectives: ~300 words, essayistic. A single "paragraph = 100 words" rule would flatten Reviews and Perspectives.
4. **First person is normal in research, rare in Reviews.** Nature and Science research text uses we/our 11–13 times per 1,000 words; Reviews 1–2. Perspectives use it for argument.
5. **Hedges are less frequent than expected.** Research Articles hedge 3–6 times per 1,000 words; Reviews 6–7. Generated text often hedges 15–30 times per 1,000. Over-hedging is a stronger AI marker than under-hedging.
6. **Evaluative and connective markers sit in single digits.** The full watchlist (Section 3 of writing-diagnostics.md) fires 2–4 times per 1,000 words in top-journal text, and most hits are statistical or technical. A paragraph with three "moreover/furthermore/additionally" is far outside the corpus distribution.
7. **"Not X but Y" is rare.** 0.3–0.7 per 1,000 words in research and Reviews, ~1.2 in Science Perspectives. It is a real rhetorical move but not a default sentence pattern.
8. **Em dashes are genre-dependent.** Research text uses <1 per 1,000 words; Reviews and Perspectives 1–4. Semicolons are more common in research (3–4) than in Perspectives (<1).
9. **Numerals carry the argument.** Research Articles contain 50–65 numerals per 1,000 words. A Results paragraph without a number is usually an interpretation paragraph misplaced in Results.
10. **Figure captions are substantial and statistical.** Median 190–200 words in both journals; 39% (Nature) and 25% (Science) state n; 53% and 44% define error representation. A 40-word caption is an outlier, not a model.
11. **Title grammar differs by journal and genre.** Nature titles are compact noun phrases (9 words, 1% colon). Science Research titles are slightly longer (10 words, 3% colon). Science Review titles use a "Topic: thesis" colon in 31% of cases; Nature Reviews rarely do (4%).
12. **Science Perspectives are a different format.** Their "abstract" is a one-sentence teaser (median 11 words); the essay carries the argument. Do not write a Science Perspective like a short Review.

## 4. Genre definitions from the journals

Nature (author guidance, checked 23 November 2026):
- Article: original report whose conclusions represent a substantial advance with immediate, far-reaching implications; summary paragraph ideally ≤200 words; 2–3 sentences of field introduction, background and rationale, main conclusions introduced by "Here we show" or equivalent, then 2–3 sentences of context; typical 2,500 words (6 pages) or 4,300 words (8 pages); ≤50 references; subheadings ≤40 characters.
- Review: focuses on one topical aspect, not a comprehensive survey; may be controversial but should indicate opposing viewpoints; not centred on the authors' own work; accessible language; 200-word maximum preface ending with a summary sentence; generally <7,000 words; 4 moderate display items; ≤150 references; boxes welcome; highlight 5–10% of references with a one-sentence explanation.
- Perspective: a forum for models and ideas from a personal viewpoint; more forward-looking and speculative than a Review; may be narrower; opinionated but balanced; intended to stimulate discussion and new experimental approaches; same formatting guidelines as Reviews.

Science (format observed in the corpus; verify current instructions at submission):
- Research Article: ~125-word, 5–6 sentence abstract; results organised around claims and experiments; first person common.
- Review: ~120-word abstract; explicit synthesis and framework; often closes with a forward statement or "We review...".
- Perspective: one-sentence teaser (median 11 words) and a short argumentative essay; no methods.

## 5. Exemplars used for qualitative reading

These papers were read in full or in substantial part for structure and voice; DOIs are given for verification.

Nature Articles:
- 10.1038/s41586-021-03819-2 (AlphaFold2)
- 10.1038/s41586-024-07487-w (AlphaFold3)
- 10.1038/s41586-023-06291-2 (clinical LLM evaluation)
- 10.1038/s41586-021-04008-x (ethics of DNA research on human remains)
- 10.1038/s41586-020-2649-2 (NumPy)

Nature Perspectives:
- 10.1038/s41586-021-03694-x (social aspects of infectious disease transmission)
- 10.1038/s41586-020-2913-5 (organized crime in fisheries)
- 10.1038/s41586-021-03792-w (after the pandemic)
- 10.1038/s41586-021-03191-1 (NIH Somatic Cell Genome Editing program)

Science Research Articles:
- 10.1126/science.ade2574 (ESMFold)
- 10.1126/science.abj8754 (RoseTTAFold)
- 10.1126/science.abf4063 (immunological memory to SARS-CoV-2)
- 10.1126/science.aaz1776 (GTEx atlas)
- 10.1126/science.abb2507 (SARS-CoV-2 spike structure)

Science Reviews:
- 10.1126/science.aau6977 (exosomes)
- 10.1126/science.aat5314 (integrated stress response)
- 10.1126/science.abq4964 (spatial omics)
- 10.1126/science.abc4552 (microbiome and cancer)
- 10.1126/science.aax3769 (ubiquitin-proteasome system and autophagy)

Science Perspectives (title and teaser structure):
- 10.1126/science.abk3436 (oncolytic virotherapy)
- 10.1126/science.abm7530 (genetic ancestry)
- 10.1126/science.adn4128 (GLP-1 drugs beyond obesity)
- 10.1126/science.adh3073 (drug-delivering microrobots)

## 6. Limitations

- Paywalled full text: Nature Reviews and most Perspectives are not open access, so their body-text statistics are based on 8 and 21 full texts respectively; abstract, title and caption statistics use the full sets. Science Perspectives are represented by 3 full texts.
- Science type classification is heuristic. Perspectives were identified as Journal Articles with a 6–30-word abstract and a 2–4-page span; the set may include adjacent Insight formats (Policy Forum, Viewpoint) and may exclude atypical Perspectives. This affects genre labels, not the writing statistics materially.
- Figure-caption parsing captured main-text figures, not Extended Data figures; per-paper figure counts are lower bounds. Caption statistics describe what authors write, not how figures look; the visual rules come from journal production specifications and from reading exemplar figures.
- Topic filtering was title/abstract based and favours papers with explicit bio/AI vocabulary; it does not represent all of Nature or Science.
- No Chinese journal corpus was collected. The Chinese skill uses these statistics as a cross-language reference for argument structure and evidence strength, and applies Chinese-specific diagnostics separately.
- Statistics describe the corpus, not a target for every paper. A Review may legitimately use long paragraphs; a short Brief Communication may have no numeral. Use the numbers to detect outliers, not to fill quotas.

## 7. Reproducing the analysis

Local scripts and manifests are kept outside the skill package under the author's corpus workspace: page harvesting and parsing, Europe PMC/PMC acquisition, style metrics, figure-caption statistics and report generation. The corpus is not redistributed with the skill. Re-running the analysis requires network access to Nature, Europe PMC and PubMed Central, and respect for their terms of use.
