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
