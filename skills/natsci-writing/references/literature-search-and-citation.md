# Literature search, synthesis and citation integrity

Version 1.2.1; updated 2026-11-23. Read when scoping a literature search, writing a Review/Introduction, verifying references, or building a reference library. Pair with manuscript-production.md, journal-style-evidence.md and ai-use-and-writing-integrity.md.

## 1. Search as an argument, not a dump

Start from the scientific question and the claim the literature must support. For each claim, decide what kind of source is required: primary experiment, systematic review/meta-analysis, method paper, resource/database, official guidance or preprint. Search to answer a question, not to accumulate citations.

- Define the question and scope: system, mechanism, intervention, outcome, time window, language, publication types.
- For clinical/biomedical questions, use PICO (Population, Intervention, Comparison, Outcome) and note study designs.
- Keep a search log: database, date, query string, filters, result count, screening decision.

## 2. Source hierarchy

1. Primary research articles, registered reports and deposited datasets.
2. Systematic reviews/meta-analyses and authoritative community guidelines.
3. Narrative reviews and Perspectives for orientation only.
4. Preprints labelled as such; check whether a peer-reviewed version exists.
5. Official journal/publisher/repository documentation for reporting and data rules.

Do not use a review as evidence for a primary result when the primary paper can be read. Do not cite a paper you have only seen summarised elsewhere as if you read it.

## 3. Databases and search strategy

Use at least three complementary sources when comprehensiveness matters: PubMed/PMC, Web of Science/Scopus, Semantic Scholar/OpenAlex, bioRxiv/medRxiv, arXiv, Crossref, and domain repositories (PDB, GEO, UniProt, ChEMBL, etc.). For Nature/Science-level work, search both the primary literature and the closest competing studies.

Build search blocks from 2–4 concepts, with synonyms, abbreviations, spelling variants and field tags. Combine with AND/OR; use NOT sparingly and document it. Run pilot searches, inspect false positives/negatives, refine. Document exact strings and dates.

Search techniques:
- backward citation chasing from key papers;
- forward citation chasing (papers citing the key work);
- author/lab tracking for the closest groups;
- preprint and conference-version checks;
- retraction/correction checks for relied-upon citations.

## 4. Screening and documentation

For a systematic review, follow PRISMA-style reporting:
- records identified per database;
- duplicates removed;
- title/abstract screened and excluded with reasons;
- full texts assessed and excluded with reasons;
- final included set.

For a manuscript Introduction/Review, keep a lighter but auditable record: source, why included, which claim it supports, and what it does not establish. Record whether you read the abstract, sections or full text.

## 5. Data extraction and quality assessment

For each included study record: design, system/population, intervention/comparison, sample size, key result with effect size/uncertainty, conditions, limitations, funding/conflicts, and relevance to the claim.

Quality tools by design:
- randomised trials: Cochrane risk-of-bias;
- observational studies: Newcastle–Ottawa or equivalent;
- systematic reviews: AMSTAR 2;
- computational/benchmark studies: leakage controls, baseline parity, external test, ablations, uncertainty, reproducibility.

Do not treat all evidence as equal; state where evidence is strong, weak, contradictory or absent.

## 6. Synthesis

Organise by question, mechanism, method or assumption, not by paper. For each theme: what is established, where studies disagree, which design differences explain disagreement, and what remains untested. Use a comparison table when many studies share dimensions. Explain the strength of evidence and the gap that motivates the present work.

Avoid "Author A found X. Author B found Y." lists. Avoid flattening prior work into a weak baseline to manufacture novelty. State what the closest studies established and what they could not.

## 7. Citation verification

Every reference must be verified against the actual record:

- title, authors, year, journal/venue, volume/pages or article number, DOI;
- publication status: peer-reviewed, accepted, preprint, conference version, retracted, corrected;
- that the cited source actually supports the sentence;
- that the reference is not a duplicate or a predatory/mismatched record.

Use Crossref/PubMed/DOI resolution to check metadata. For preprints, check for a published version. For datasets/code, cite the repository record with DOI/accession and version. Never invent identifiers or "fill in" missing metadata.

Reference management:
- export RIS/BibTeX/Zotero RDF from verified records; one record per work;
- deduplicate by DOI then by title;
- keep a library file next to the manuscript;
- apply the target journal's style consistently (Nature: numbered, superscript, titles included; Science: journal style; check current guide);
- remove field codes/links before submission if required.

## 8. Citation placement and density

Cite where the claim is made, close to the sentence it supports. Prefer primary sources; cite reviews for synthesis or definitions. Avoid citation stacks that do not distinguish what each source established. For Nature/Science, keep the reference list within the journal budget (Nature Article typically ≤50 main-text references) and move method/external details to Methods/SI references.

Never cite:
- a paper you have not verified;
- a retracted paper without disclosure;
- a preprint as peer-reviewed;
- a dataset without its identifier;
- your own unpublished work as if published.

## 9. AI-assisted search

AI can help build queries, deduplicate and triage abstracts, but:
- treat AI-suggested references as unverified leads;
- verify every DOI/title/author against the source;
- do not let AI write the synthesis without reading the papers;
- disclose AI use if the journal requires it;
- keep confidential manuscripts out of public tools.

## 10. Literature audit

- Is the question and search scope explicit?
- Are the databases, strings and dates documented?
- Is there a source hierarchy and a screening record?
- Are the closest competing studies included and treated fairly?
- Is the synthesis organised by question/mechanism, not paper?
- Is evidence quality assessed and disagreement explained?
- Is every reference verified and actually supporting its sentence?
- Are preprints, retractions and versions handled correctly?
- Is the reference style consistent and within budget?
- Is the gap that motivates the study explicit and not manufactured?
