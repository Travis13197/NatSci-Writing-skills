# Language, style and academic taste

Version 1.1.0; updated 2026-11-23. Read when polishing English prose, calibrating voice, preparing journal house style, or judging whether a passage reads like a working scientist rather than generated text. Pair with writing-diagnostics.md (AI-tone lexicon and drills) and revision-and-response.md (section moves and phrasebank).

## 1. What "taste" means operationally

Academic taste is not decoration. It is a set of decisions that make a paper readable, credible and memorable:

1. **Restraint** — say the strongest defensible thing with the fewest words; no adjective that the evidence does not pay for.
2. **Precision** — every abstraction resolves to an object, comparison, measurement or mechanism.
3. **Proportion** — space follows evidence: the decisive result gets the clearest paragraph and figure, not the most familiar method.
4. **Rhythm** — sentence length varies with the argument; long sentences carry qualified claims, short ones land them.
5. **Voice** — authority without hype, humility without defensiveness, first person where the discipline allows.
6. **Ending** — paragraphs and sections close on an inference, a consequence or a question, not on praise or a promise.

A passage has taste when a reader can see the author deciding what matters.

## 2. Journal house style (verify current guide)

Nature initial-submission style:
- English with Oxford English Dictionary spelling conventions.
- Double spacing; standard font, preferably 12 pt Times New Roman; Word without style tags preferred.
- Line numbers.
- Title ≤75 characters including spaces, normally ≤2 printed lines; avoid numbers, acronyms, abbreviations and punctuation where possible.
- Summary paragraph ≤~200 words, written for readers outside the discipline, avoiding numbers and abbreviations unless essential.
- Main text: ~2,500 words with four modest display items (6 pages) or ~4,300 words with five or six (8 pages); subheadings ≤40 characters; ≤~50 references.
- Methods typically ≤3,000 words; no figures/tables in Methods; separate Data and Code Availability; Methods references continue numbering.
- Figure legends <250 words at initial submission; begin with a title sentence.
- References: sequential numbering across text, tables, legends, Methods and Extended Data; superscript citations; one publication per number; list all authors up to five, then first author et al.; include article titles; remove EndNote link fields.
- Acknowledgements brief; no thanking anonymous referees or editors.

Science and Nature subjournals have their own guides. Do not import flagship numbers; record the source and date.

## 3. English prose craft

**Sentences**
- Prefer actor–verb–object. Convert nominalisations: "activation of the kinase by phosphorylation leads to..." → "phosphorylation activates the kinase, which...".
- Median 24–25 words is a corpus norm, not a quota; vary deliberately. Two consecutive 40-word sentences tire the reader.
- One qualification per sentence. Delete stacked hedges ("may potentially suggest").
- Put old information at the start and the new claim at the end (given–new).
- Use concrete subjects: the model, the assay, the 34 families, the 128 mutations — not "this", "it" or "the results" when the referent matters.
- Avoid triads and ornamental parallelism; three adjectives usually hide one property.
- Prefer direct statements to "not X, but Y" unless X and Y are competing scientific explanations.

**Paragraphs**
- One job per paragraph: context, gap, approach, result, comparison, mechanism, implication or limitation.
- Open with a topic sentence that states the relationship; close with the inference or the next question.
- Keep research paragraphs ~120–140 words (4–5 sentences), reviews 150–260, Perspectives up to ~300 when the argument needs continuity.
- A paragraph that can be reversed without loss of meaning is probably a list, not an argument.

**Hedging and claim strength**
- show/demonstrate/reveal/establish: direct evidence.
- indicate/suggest/are consistent with: inference.
- may/could/propose: speculation.
- "Significant" only with a statistical test; "substantial" only with a magnitude.
- Remove "novel", "unprecedented", "groundbreaking", "powerful", "comprehensive", "robust", "seamless", "pivotal", "crucial" unless replaced by the property that makes them true.

**Punctuation and mechanics**
- Em dashes sparingly; avoid joining independent clauses with them. Semicolons for genuinely parallel clauses. No contractions, rhetorical questions or direct address in research prose.
- Numerals for measurements; space between value and unit; en dash for ranges; consistent statistical symbols.
- Define abbreviations at first use; one canonical term per object; British spelling for Nature-style prose.
- Figure citations: "Fig. 1a", "Extended Data Fig. 2", "Supplementary Table 1" per journal style.

## 4. Voice and register

- Research Articles: "we" for work, data/model for results; past tense for experiments, present for established facts and model behaviour.
- Reviews: field as subject; "we argue/propose" sparingly; synthesis rather than author-centred narrative.
- Perspectives: first person acceptable; speculation labelled and motivated.
- Never conversational, never promotional, never defensive. Authority comes from specific evidence, not from adverbs.

## 5. Taste diagnostics

Read each paragraph and ask:
1. What is the one thing the reader now knows?
2. Which sentence carries the evidence, and is it adjacent to the claim?
3. Can any sentence be deleted without loss? Delete it.
4. Does any adjective do work that a number or comparison should do?
5. Is the opening a scene-setter ("In recent years...") that can be replaced by the science?
6. Is the ending a promise ("opens new avenues") that can be replaced by a consequence?
7. Would a biologist outside the subfield need to reread any sentence? Rewrite it.
8. Does the prose sound like the author has a view, or like a summary of everything?

## 6. Model shapes (not text to copy)

- Opening: "Proteins from the same family share sequence features, yet models trained on individual families do not transfer to held-out families." (known → tension)
- Result: "Across 34 held-out families, the model recovered family-specific structural constraints (median accuracy 0.71 versus 0.58 for the profile baseline; n = 34 families)." (claim → comparison → number → unit)
- Interpretation: "The gain persists when sequence similarity is removed, which is consistent with the model learning structural rather than taxonomic cues." (inference → condition → alternative)
- Discussion close: "The same representation may make annotation transfer testable in families that currently lack structural coverage." (bounded opportunity, not praise)

## 7. Chinese prose notes

- 中文科学写作以动词句为主，避免"对……进行……"式名词化；一句话一个论断。
- 控制"的"字链（连续三个"的"通常可拆句）和长定语（80 字以上应拆分）。
- 少用"此外、同时、值得注意的是、综上所述"；段间关系用内容承接。
- 删除评价性四字词与空泛展望（"具有广阔前景""提供新思路"）；保留具体条件与数字。
- 中英对照时保持证据强度一致：候选、相关、预测、已证明（限测试范围）。

## 8. Final language gate

- Title, abstract and opening are intelligible outside the subfield.
- No paragraph opens with a scene-setting clause or a decorative connective.
- Every central claim has evidence within the same or next sentence.
- No unsupported adjective, priority claim or universal claim.
- Terminology, abbreviations, units and figure citations are consistent.
- The text reads as an argument with a view, not as a summary of everything.
