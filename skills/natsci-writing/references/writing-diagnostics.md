# Writing diagnostics: removing generated-sounding prose

Version 1.1.0; updated 2026-11-23. Read with the parent SKILL.md when drafting, revising or auditing prose for Nature/Science style. The corpus basis is in journal-style-evidence.md.

## 1. The target is specificity, not decoration

Generated academic prose fails in a characteristic way: it is grammatically clean, lexically inflated and semantically thin. The corrections are not stylistic preferences; each removes a sentence that fails to transfer information. Apply the tests in order: meaning, structure, lexicon, mechanics.

Baseline for comparison (median rates per 1,000 words in the Nature/Science corpus):

| Signal | Research | Review | Perspective |
|---|---|---|---|
| Logical connectives (however, moreover, therefore, ...) | 4–5 | 7 | 5 |
| Hedges (may, suggest, likely, indicate, ...) | 5–6 | 7 | 7 |
| First person (we, our) | 11–13 | 2 | 5 |
| "Not X but Y" and "rather than" | <0.5 | <0.5 | 1 |
| Em dash | <0.5 | <0.8 | 1–2 |
| Semicolon | 3 | 1.4 | <1 |
| Numerals | 40–55 | 20–40 | 5–12 |
| AI-marker watchlist (Section 3) | 2–4 | 3–4 | 4 |

The important number is not the exact value; it is that top-journal text stays in single digits per 1,000 words for markers that generated text repeats several times per paragraph.

## 2. Seven failure modes, with rewrites

### 2.1 Abstraction stacking
Symptom: a subject that is an abstraction, a verb that is empty, a predicate that restates the subject.

- Before: "The proposed framework enables a comprehensive and robust characterization of the functional landscape of protein representations."
- After: "The framework assigns each protein a vector and tests whether individual dimensions track Pfam family membership."
- Test: name the object, the operation and the output. If one is missing, the sentence is not yet written.

### 2.2 Template contrast
Symptom: "not X, but Y", "rather than", "X is not merely A; it is B" used to create emphasis without a scientific alternative.

- Before: "This is not merely a benchmark; it is a fundamental rethinking of how models are evaluated."
- After: "The benchmark measures residue-level accuracy on held-out families; earlier evaluations measured whole-chain similarity."
- Keep contrast only when X and Y are competing hypotheses or real alternatives. One or two substantive contrasts per paper are enough.

### 2.3 Connective inflation
Symptom: moreover, furthermore, additionally, notably, importantly, ultimately at the head of successive sentences.

- Before: "Moreover, the model is robust. Furthermore, it generalises. Additionally, it is efficient."
- After: "The model is robust to sequencing depth, generalises to held-out families and runs in under a minute per proteome."
- Merge list-like claims into one comparative sentence, or delete the connectives and let juxtaposition carry the relation. When a relation really is causal or contrastive, use because, therefore, in contrast, under this condition.

### 2.4 Evaluative and promotional adjectives
Symptom: groundbreaking, unprecedented, revolutionary, powerful, comprehensive, robust, seamless, pivotal, crucial, state-of-the-art, cutting-edge, novel.

- Before: "We introduce a powerful and comprehensive model that achieves state-of-the-art performance."
- After: "The model improves recall@10 by 12 points over the previous best method on the held-out benchmark."
- If the adjective is load-bearing, replace it with the property that makes it true ("robust to missing residues", "comprehensive across 34 families"). If no property can be named, delete the adjective.

### 2.5 Defensive and self-limiting prose
Symptom: generic caveats, ritual humility, repeated limitation sentences, "it is important to note", "although preliminary", "to some extent", "cannot be overstated".

- Before: "Although our method has some limitations, it provides a promising foundation for future work, and further studies are needed to fully validate its generality."
- After: "The evaluation covers 34 families; performance on families with fewer than ten members remains untested. The same representation supports annotation transfer, which we test in the next section."
- State the condition where it changes interpretation, once. Move unresolved source or data problems to an author-facing note. Do not colonise the Discussion with a limitations list.

### 2.6 List-paragraphs and module catalogues
Symptom: "First, we ... Second, we ... Third, we ..."; paragraphs that walk through modules in the order they were implemented.

- Before: "First, we constructed the dataset. Second, we trained the model. Third, we evaluated it. Fourth, we analysed the representations."
- After: "To ask whether sequence context alone determines family-specific representations, we trained the model on Pfam families and tested it on held-out families that share no detectable homology."
- Organise Results by question and evidence, not by implementation order. A reader should be able to state each subsection's claim after its first two sentences.

### 2.7 Meta-commentary
Symptom: "This paper aims to", "In this section, we will", "The following analysis demonstrates", "It is worth noting that this figure shows".

- Before: "In this section, we present an analysis that demonstrates the model's ability to capture structural information."
- After: "The model's internal representations recover secondary-structure content that was not supplied during training."
- Delete references to the document; report the science.

## 3. Watchlist lexicon

Count occurrences per 1,000 words. More than five total, or two in one paragraph, usually indicates generated-sounding prose. Most legitimate uses are statistical ("significantly" with a test) or technical ("robust optimisation").

**Promotional / evaluative:** groundbreaking, unprecedented, revolutionary, transformative, powerful, comprehensive, robust (when unqualified), seamless, holistic, pivotal, crucial, vital, cutting-edge, state-of-the-art, game-changing, paradigm-shifting, landmark, seminal.

**Empty intensifiers and hedges:** significantly (without test), substantially (without magnitude), considerably, remarkably, notably, importantly, crucially, ultimately, essentially, fundamentally, inherently, arguably, seemingly, potentially (stacked), to some extent, in some sense.

**Formulaic connectives:** moreover, furthermore, additionally, in addition, notably, importantly, overall, taken together, in conclusion, it is worth noting, it is important to note, needless to say.

**Abstraction nouns (when undefined):** landscape, realm, tapestry, framework, paradigm, ecosystem, synergy, interplay, nuance, multifaceted, intricate, holistic, dimension (undefined), geometry (undefined), representation (undefined), signature (undefined), context (undefined).

**Promissory closures:** paves the way, opens new avenues, sheds light, provides a foundation, lays the groundwork, holds promise, offers a promising direction, bridges the gap, unlocks.

**Contrast templates:** not only ... but also, not merely ... but, rather than, far from, at the intersection of, beyond the scope of.

The list is not a ban. "Robust" is fine when followed by the perturbation it resists; "framework" is fine when the components are named; "significantly" is fine when a test is reported. The rule is: every flagged word must be paid for by a specific object, comparison or number in the same sentence or the next.

## 4. Sentence-level drills

Apply to every paragraph that feels generated.

1. **Verb rescue.** Circle every noun ending in -tion, -ment, -ity, -ness, -ance. Convert half to verbs with explicit subjects.
2. **Actor check.** Underline the grammatical subject of each sentence. If the subject is "this", "it", "the results" or a nominalisation, replace it with the scientific object.
3. **Claim locality.** Ensure each claim is followed within one sentence by its evidence (number, comparison, citation or experiment).
4. **One qualifier.** Remove all but one hedge per sentence; keep the one that states the actual uncertainty.
5. **Delete the first clause.** If a sentence opens with a scene-setting clause ("In recent years, ...", "With the rapid development of ..."), delete it and start with the science.
6. **Compress triads.** Three parallel adjectives or three parallel clauses are usually one idea plus filler. Keep the informative member.
7. **Replace the transition.** Delete every moreover/furthermore/additionally; if the paragraph stops making sense, add a content link (because, therefore, in contrast, after).
8. **Read aloud.** A sentence that needs a second pass is rewritten, not re-punctuated.
9. **Twenty-percent cut.** Remove 20% of words; if no information is lost, keep the cut.
10. **So-what check.** After each paragraph, write the one thing the reader now knows. If it duplicates the topic sentence, the paragraph is circular.

## 5. Paragraph-level revision protocol

1. Write the paragraph's claim in one sentence outside the manuscript.
2. Mark the sentences that provide evidence for that claim. Everything else is context, transition or filler.
3. Reorder: claim first, evidence next, qualification last (or where it changes interpretation).
4. Merge context sentences into one; delete transitions that do not encode a relation.
5. Check that the paragraph's last sentence either states the inference or motivates the next paragraph.
6. Read the section's topic sentences in sequence: they should form a coherent argument on their own.

## 6. Genre voice

| Feature | Research Article | Review | Perspective |
|---|---|---|---|
| Person | "we" for work; "the data/model" for results | "we" sparing; field as subject | "I"/"we" for argument |
| Tense | past for experiments, present for established facts and model behaviour | present | present, with future for agenda |
| Claims | measured, with statistics | synthesised, with evidence quality | argued, with selected evidence |
| Speculation | confined to Discussion, labelled | allowed in Outlook | expected, labelled and grounded |
| Citation density | moderate; primary sources | high; primary sources | selective; strongest evidence |

## 7. Pre-submission checklist

- No paragraph opens with a scene-setting clause or a connective.
- No sentence contains two stacked hedges.
- Every "significant" has a test; every "robust" has a perturbation; every "comprehensive" has a scope.
- Watchlist density is single-digit per 1,000 words.
- At least one number appears in every Results paragraph that makes a quantitative claim.
- The Discussion's final sentence names a measurement or capability, not a hope.
- Reading the topic sentences alone reproduces the paper's argument.
- The abstract contains no sentence that could be moved to another paper unchanged.

## 3A. Defensive, self-limiting and template-contrast language (zero tolerance)

These patterns are banned from manuscript prose, READMEs, cover letters and figure text. They make the writer sound uncertain, evasive or machine-generated. State the claim directly; if a contrast is real, write two affirmative sentences.

### A. Template contrast (the strongest AI tell)

| Banned pattern | Example | Rewrite |
|---|---|---|
| not X but Y | "The gain is not from scale but from data quality." | "Data quality produces the gain; scale contributes little." |
| not only X but also Y | "The model is not only accurate but also fast." | "The model reaches 0.91 accuracy and runs in 40 s." |
| not just X, it is Y | "This is not just a benchmark; it is a new evaluation paradigm." | "The benchmark measures held-out family accuracy." |
| rather than | "We measure calibration rather than accuracy." | "We measure calibration. Accuracy appears in Extended Data Fig. 2." |
| far from X, Y | "Far from settled, the mechanism remains unclear." | "The mechanism remains unresolved." |
| it is not that X; it is that Y | "It is not that the model fails; it is that the data leak." | "The data leak explains the apparent gain." |
| X, not Y (comma negation) | "The result reflects biology, not batch effects." | "The result persists after batch correction." |

Chinese equivalents: 不是……而是……；并非……而是……；不是……，是……；不仅……而且……；不只是……更是……；与其说……不如说……；看似……实则……；表面上……实际上……；所谓……并不是……；X，而不是 Y；X，不 Y。Rewrite as two affirmative statements.

### B. Defensive and self-limiting phrases

Delete these unless a specific condition requires a precise limitation. When a limitation matters, state the condition, the scope and the consequence in one sentence.

- it is important/worth/crucial/necessary to note/mention/emphasize
- it should be noted; it must be acknowledged; it cannot be overstated
- to some extent; to a certain extent; in some sense; arguably; presumably; seemingly
- further research/work/studies is/are needed/required/warranted
- the findings/results should be interpreted with caution
- based on the available information/data/sources
- this does not by itself establish/prove/imply
- while the data/evidence/sample are limited
- may potentially; could possibly; might possibly; may vary
- 值得注意的是；需要指出的是；需要强调的是；必须承认；不可否认；毋庸置疑；毋庸讳言；众所周知；诚然；固然
- 在一定程度上；在某种意义上；某种意义上；或许；也许；有望；尚需；有待；仅供参考；不成熟；浅析；抛砖引玉；难免；限于篇幅；不再赘述；以期；试图；旨在
- 本研究的不足之处；由于条件限制；有待进一步研究；希望本文能够；仅供参考

Replace with the measured condition: "In the 34 held-out families, ..." / "The single-centre cohort limits generalisation to ...". Then state what follows.

### C. AI vocabulary and density

Tier 1 (avoid by default): delve, underscore, intricate/intricacies, realm, tapestry, testament, nuanced, multifaceted, meticulous, commendable, garner, boast, leverage, robust, pivotal, crucial, vital, foster, navigate (figurative), landscape (figurative), showcase, underpin, notably, comprehensive, seamless, holistic, paradigm, transformative, groundbreaking, unprecedented, state-of-the-art, cutting-edge.
Tier 2 (use only when the technical meaning is exact): significant (with a test), substantial (with a magnitude), robust (with the perturbation it resists), comprehensive (with its scope), novel (with the specific new relation).
Chinese: 赋能、助力、闭环、抓手、生态、范式、图景、底层逻辑、组合拳、破局、重塑、颠覆、革命性、里程碑、新篇章、注入新动能、按下加速键、提供新思路、奠定基础、开辟新方向、具有广阔前景、具有重要意义、发挥关键作用、至关重要、全面、深度、高度、系统性地、有效地、显著地（无检验时）。

Density: more than five watchlist hits per 1,000 words, or two in one paragraph, signals generated prose. Most legitimate uses are statistical or technical.

### D. Structural tells

- Rule of three: three adjectives, three parallel clauses or three examples used as a default rhythm. Keep the informative item; cut the other two.
- Section summaries and outline-like endings: "In summary", "In conclusion", "Overall", "Taken together"; Chinese 首先/其次/最后、总而言之、综上所述、由此可见、不难看出、总的来说、总之.
- Didactic disclaimers and meta-commentary: "It is worth noting that this figure shows ...", "In this section, we will ...", "This paper aims to ...".
- Information repetition: "in other words", "that is to say"; Chinese 换句话说、也就是说.
- Symbol inflation: "witnessed", "carries", "marks", "is a microcosm of"; Chinese 见证了、承载着、彰显了、标志着、意味着.
- Overuse of em dashes and definition-style colons; keep punctuation plain.
- Avoidance of simple "is/are": do not turn every sentence into "serves as", "represents", "constitutes".
- Emoji-decorated headings, canned lists and placeholder text in serious prose.

### E. Rewrite protocol

1. Find the sentence that carries the actual claim.
2. Delete the negation setup, disclaimer or contrast frame.
3. State the claim with its object, comparison, number or condition.
4. If two alternatives genuinely compete, write two affirmative sentences and let the evidence separate them.
5. Read the paragraph aloud; if the only rhetorical energy came from the banned frame, rewrite the science.
6. Run the checker: python tools/check_prose_style.py <file>. ERROR hits are must-fix.

### F. Overcorrection is also a tell

Do not scrub the text into telegraphic fragments, remove every qualification, or replace precise hedges with false certainty. Fix robotic prose with specificity: the condition, the comparison, the number, the mechanism. A precise "in the 34 held-out families" is better than either "generally" or a stack of disclaimers.

### G. Sources consulted (November 2026)

- Wikipedia, Signs of AI writing: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- AI Smells field guide (AI-Smells-Agents-Avoid): https://github.com/williamsmithedward/pyvbaanalysis/blob/main/docs/AI-Smells-Agents-Avoid.md
- Chinese AI cues (zh-cues): https://github.com/prism-shadow/penguin-harness/blob/main/plugins/humanizer/skills/humanizer/reference/zh-cues.md
- Editage, AIGC style words: https://www.editage.cn/sci-writing/6791/
- CASS, 智能写作的"AI味"问题: http://ling.cass.cn/news/xuejie/202607/t20260703_6057568.html


## 4A. Rhythm and paragraph shape (structure-level AI tells)

Lexicon checks catch words; generation shows up first in **rhythm**. Three structural signatures, all measurable:

1. **Uniform sentence length.** Generated prose clusters at 18–26 words with low variance. Human scientific prose mixes a 6-word verdict with a 40-word mechanism sentence.
2. **The template paragraph.** Topic sentence → three supports → recap. Every paragraph the same shape, every section the same length, every subsection ending in a summary.
3. **Glue instead of content.** Transition sentences ("Building on this, we next examine …") that carry no object, number or mechanism.

Repair by rebuilding the paragraph, not by swapping synonyms:

| Before (template) | After (argued) |
|---|---|
| "Our method achieves strong performance across multiple benchmarks. First, it improves accuracy. Second, it reduces cost. Third, it generalises well. Overall, these results demonstrate its effectiveness." | "The gain is 0.08 in held-out families (Fig. 2a) and disappears when the alignment step is removed, so the step, not the extra parameters, carries the effect." |

Measured gates (`python tools/check_prose_style.py --metrics <file>`):

| Metric | Target | Reading |
|---|---|---|
| Sentence-length CV | 0.30–0.65 | <0.30 machine rhythm; >0.65 choppy |
| Paragraphs whose first sentence states the claim | ≥80% | lower means the paragraph warms up before saying anything |
| Recap tails per 1,000 words | ≤1 | "Overall/In summary/Taken together" |
| Triad density | ≤1 per 500 words | three-item lists used as default rhythm |
| Nominalisation ratio | ≤12% of content words | -tion/-ment/-ance/-ity chains |
| Em dashes per 1,000 words | ≤2 | definition-colon and dash habits |

The argument-level counterpart — which claims to keep, which experiments to drop, and how to tell a necessary caveat from a defensive one — is `defensive-writing-and-argument-selection.md`.
