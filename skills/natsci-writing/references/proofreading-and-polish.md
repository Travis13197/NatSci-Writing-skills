# Proofreading and sentence polish

Version 1.2.1; updated 2026-11-23. Read for the final language pass, non-native English polishing, post-revision cleanup, or a systematic proofread before submission. Pair with language-and-taste.md and writing-diagnostics.md.

## 1. Five passes

Run them in order; complete one before the next.

### Pass 1 — Typo and spelling
Misspellings; technical-term spelling; inconsistent capitalisation; hyphenation variants; duplicated words; missing/extra spaces; wrong gene/protein/species names; unit symbols; Greek letters.

### Pass 2 — Grammar
Subject–verb agreement; tense; articles; prepositions; pronoun–antecedent agreement; fragments; run-ons; comma splices; misplaced/dangling modifiers; parallel structure.

### Pass 3 — Inappropriate words
Informal language; contractions; vague quantifiers ("very", "quite", "a lot of"); unnecessary hedges; emotional/subjective language; anthropomorphism ("the system thinks", "the paper argues"); unsupported evaluative adjectives; AI-tone markers.

### Pass 4 — Awkward expression
Over-complex sentences; passive where active is clearer; wordy phrases; redundancy; unclear pronoun reference; non-idiomatic phrasing; noun chains; stacked modifiers; overlong parentheticals.

### Pass 5 — Academic style and consistency
Terminology across sections; abbreviations defined once; tense conventions; citation style; equation/unit symbols; number formatting; figure/table references; heading style; British/American spelling; reference and caption consistency.

## 2. Sentence-level rules

- Prefer active voice for author actions; passive when the object is the point.
- Present tense for the paper's established claims and model behaviour; past tense for experiments performed and prior work.
- Define acronyms at first use; use the short form thereafter; do not re-define in every section.
- Avoid hyphens joining independent clauses; compound modifiers are fine.
- Cut "in order to" → "to"; "due to the fact that" → "because"; "at this point in time" → "now"; "make use of" → "use".
- One proposition per sentence; keep dependent clauses attached to a main clause.
- Replace nominalisations with verbs: "activation of X by Y leads to..." → "Y activates X, which...".
- Keep technical terms, gene/protein nomenclature and LaTeX/markup intact; never "correct" domain jargon.
- Do not over-correct correct but unusual constructions; preserve the author's voice and argument.

## 3. Grounding and rhythm

A reader can only follow a sentence that uses concepts already grounded. Before a paragraph leans on a term or idea, either the audience already knows it or an earlier sentence/paragraph introduced it. If a term appears before its idea is grounded, add the definition or move it later.

Paragraph rhythm:
- one move per paragraph;
- a topic sentence that states the claim or question;
- evidence and explanation in the middle;
- an ending that states the inference or motivates the next paragraph;
- vary sentence length; avoid three long sentences in a row and avoid a chain of short declaratives that reads like a list.

## 4. AI-tone cleanup

Watch for: generic transitions ("Moreover", "Furthermore", "Additionally", "Notably", "Importantly"), triads, "not only ... but also", "in the realm of", "plays a crucial role", "paves the way", "underscores the importance", "delve into", vague "robust/comprehensive/powerful", and summary sentences that repeat the paragraph. Replace with a specific relation, comparison, number or consequence. Check the corpus watchlist in writing-diagnostics.md.

## 5. Numbers, units, references

- Recompute or verify every number; check that abstract, Results, legend and supplement agree.
- Units: space between value and unit; consistent symbols; SI where appropriate.
- Statistical symbols italic/consistent; P value format per journal.
- Figure/table citations consistent ("Fig. 1a", "Extended Data Fig. 2", "Supplementary Table 1").
- References: numbering/order, author formatting, DOI, title, journal abbreviation; no broken field codes.
- Equations: variables defined, units preserved, subscripts/superscripts render correctly.

## 6. Output contract

For a proofreading task, return:
1. **Pass summaries**: issues found/fixed by category.
2. **Issue log**: location, original, corrected, reason, severity (critical/major/minor).
3. **Corrected text** in full.
4. **Residual questions**: items needing author verification (numbers, terminology, citation).
5. **No-change note** when the text is already sound; do not manufacture pedantic edits.

For a revision task, preserve unchanged passages, mark changes, and keep the author's voice. Do not silently rewrite the argument.

## 7. Final proofreading audit

- All five passes completed.
- Every number checked against source data; units and statistics consistent.
- Terminology, abbreviations and nomenclature consistent.
- References verified and style consistent.
- Figures/tables cited and numbered correctly.
- LaTeX/markup/math intact.
- No AI-tone clusters; no generic transitions; no unsupported adjectives.
- Paragraphs have one move, a topic sentence and a grounded vocabulary.
- Read aloud once; any sentence requiring a second parse is rewritten.
- Residual questions listed for the author, not silently guessed.
