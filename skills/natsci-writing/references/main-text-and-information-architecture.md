# Main-text discipline and information architecture

Version 1.1.0; updated 2026-11-23. Read when drafting or compressing Results, deciding what belongs in the main text versus Extended Data/Supplementary Information, auditing whether the manuscript is over-long, or mapping the evidence chain onto figures and sections.

## 1. Evidence completeness is not main-text completeness

Preserve the complete evidential record across the manuscript, figures, tables, Methods, source data and Supplementary Information. Reserve main-text space for evidence that establishes, advances or materially bounds the central claim.

Compression must never hide inconvenient evidence. If an observation changes the direction, magnitude, scope or credibility of the central conclusion, keep it visible in the main text even if it is nominally a robustness or subgroup analysis.

## 2. Classify every result before placement

| Class | Test | Default destination |
|---|---|---|
| Core discovery | Advances the central conclusion | Main text with adequate evidence |
| Necessary support | Reader must see it to accept the core discovery | Main text, briefly |
| Qualification | Materially bounds or alters interpretation | Main text if yes, else SI |
| Robustness | Survives alternative specification, seed, threshold or estimator | SI with a pointer |
| Heterogeneity | Variation across groups/settings is part of the claim | Main text if central, else SI |
| Provenance detail | Traceability, preprocessing, implementation | Methods/Source Data/repository/SI |
| Alternative inference | Secondary route to the same claim | SI unless it changes acceptance |
| Edge case | Failure boundary that changes how the claim is read | Main text if interpretation changes |

Classify by function in this paper, not by analysis name. An ablation can be a core discovery in a mechanism paper; heterogeneity can be the headline; a confidence interval can be primary evidence.

## 3. Shortest sufficient evidence chain

Write the minimum ordered chain that lets the reader:
1. understand the central observation;
2. see the decisive comparison or mechanism evidence;
3. judge the primary uncertainty or inference;
4. understand any boundary that changes the conclusion.

Do not reproduce the chronological record of analyses. Draft Results only after the analysis and result-allocation table are stable.

## 4. Main text, caption and SI split

- **Main text**: what was found, the decisive support, and what it means for the central claim.
- **Caption**: what is shown and how to read it, including definitions needed for interpretation.
- **SI**: why the conclusion survives deeper scrutiny (secondary analyses, robustness, implementation detail, extended diagnostics, non-central edge cases).

Do not repeat a full set of effect sizes, intervals and P values in both main text and caption. Choose one authoritative location for the full numeric report and use the other for the minimum narrative or reading cue, while preserving journal-mandated caption content.

## 5. Display-item budget and information density

Nature Article budgets: a six-page Article is ~2,500 words with four modest display items; an eight-page Article is ~4,300 words with five or six. A modest display item plus legend occupies about a quarter page (~270 words equivalent). A large composite requires a corresponding text reduction. Main references are typically ≤50.

Rules:
- Every figure/table must earn its space by carrying a claim, comparison, mechanism or boundary not better expressed in text.
- Do not crowd multiple independent claims into one figure to save budget; split or move to Extended Data.
- Do not use tables as data dumps; a table should support a comparison the reader needs.
- Extended Data should carry integral supporting data (Nature allows up to ten multi-panel items); SI is for essential material too large or specialised for print.
- Keep caption statistics and methods minimal; put full protocols in Methods/SI.
- Prefer one strong panel over three decorative variants of the same result.

## 6. Prevent revision accretion

Every requested addition triggers a deletion check:
1. State the new function the sentence serves.
2. Find existing sentences that already serve it.
3. Prefer replacement, combination or compression before appending.
4. Re-read the paragraph and delete what the edit made redundant.
5. Re-run the paragraph necessity test and claim-repetition audit.

For reviewer-driven edits ask: does this sentence tell the reader what was discovered, or mainly tell a reviewer why an objection fails? Keep the first in the main text when necessary; route the second to SI or the response letter unless it is essential to the central inference. Answer every reviewer fully in the response letter even when the manuscript change is short.

## 7. Paragraph necessity and explanatory recursion

For every Results paragraph: if removed, would the reader still understand and have adequate evidence for the central claim?
- No: keep it.
- Yes, but a reviewer might ask: route to SI or the response letter.
- Yes, and the point appears elsewhere: delete it.

Do not explain an explanation in the main text. If a statistical or graphical detail needs several sentences to reconcile with the main result, state the result and any conclusion-changing boundary simply, then move the extended reconciliation to SI. Keep the longer explanation only when the reconciliation itself is part of the discovery.

## 8. Claim-repetition map

A major claim may be introduced, demonstrated and synthesized, but each appearance must perform a different function. Map every occurrence across the heading, transition, figure/table caption, Results paragraph, Discussion and closing sentence; mark it introduce, demonstrate, interpret, synthesize, shorten or delete. Remove restatements that add no new evidence, boundary or interpretation.

## 9. Statistics location discipline

Compute and retain every analysis required by the design, protocol, reporting standard and integrity audit. In the main text normally report the descriptive quantity needed to understand the effect and the primary inferential statistic or interval needed to support the claim. Route secondary intervals, alternative estimators, multiplicity checks, sensitivity analyses and model-level heterogeneity to SI unless they change the conclusion or are required in the main text. Never select only the most favourable statistic; record the full analysis family and the reason for each reporting location.

## 10. Auditable compression record

For a Results or full-manuscript restructuring task, maintain:
1. Result-allocation table (result, class, effect on interpretation, destination, pointer).
2. Shortest evidence chain (ordered claims and decisive evidence).
3. Deletion log (appended, replaced, compressed, relocated, deleted, with reason).
4. Statistics-location record (primary main-text report, secondary SI analyses).
5. Claim-repetition map (function retained at each location).
6. Word-count delta per revised subsection.

Keep the record compact unless the user asks for the full table; the prose remains the deliverable.

## 11. Non-negotiable exceptions

- Do not move reproducibility, integrity, safety, ethics or mandatory reporting information to save words.
- Do not bury contradictory or conclusion-changing evidence in SI.
- Do not strip a qualification that prevents a misleading causal, clinical, societal or generalisation claim.
- Do not remove statistics required by the target journal, study design or field standard.
- When an editor requires a point in the main text, comply but still replace or compress neighbouring redundancy.

## 12. Information-architecture audit

- Is every Results paragraph necessary for the central claim?
- Does each figure/table have a distinct role and an appropriate destination?
- Is the main text carrying evidence, not implementation inventory?
- Are full statistics reported once, in a defined location?
- Does the SI contain robustness and provenance without hiding conclusion-changing results?
- Does the revised text avoid duplicated claims across abstract, Results, Discussion and caption?
- Is the word count inside the target journal's budget after all additions?
