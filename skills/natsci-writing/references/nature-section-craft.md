# Nature section craft: abstract, introduction, results and discussion

Version 1.2.1; updated 2026-11-23. Read when drafting or rebuilding the four core sections of a Nature-style research article. This file distils corpus-derived Nature section guidance; journal instructions and the paper's evidence always take precedence. Pair with manuscript-production.md, main-text-and-information-architecture.md and journal-style-evidence.md.

## 1. Abstract: the shortest evidence chain

Do not write the abstract as a compressed Introduction or a catalogue of experiments. Compress the paper into the shortest chain that makes the discovery understandable, credible and consequential:

~~~text
precise problem or gap -> what the study does to resolve it -> main discovery
-> decisive support or boundary -> what the discovery establishes -> why it matters
~~~

Move order (combine when the word limit requires):
1. Known phenomenon or important problem.
2. Precise unresolved question.
3. Study design or conceptual move used to answer it.
4. Main discovery.
5. One or two critical supporting findings or boundaries.
6. Conceptual, technical or field-level implication.

Rules:
- The centre of gravity is "we found X", not "we evaluated many models and datasets" or "we propose a framework".
- Spend only enough background to make the gap intelligible.
- Describe the method only at the level needed to see why the design answers the question; omit learning rates, hardware, routine splits and dataset inventories unless they define the discovery.
- Choose one central claim and at most one or two supports; do not give every Results subsection a sentence.
- Include a number only when it defines, supports or bounds the central claim.
- End with what the finding changes or enables within the tested scope, not with "the method performs well".
- Read the abstract with method and dataset names hidden; if the discovery and its importance disappear, it is organised around implementation rather than insight.

## 2. Introduction: convergence, exact gap, late answer

Build a narrowing argument:

~~~text
important problem -> specific phenomenon or difficulty -> what existing approaches establish
-> unresolved limitation or tension -> exact unknown -> research question or hypothesis -> what this study does
~~~

Rules:
- Move quickly; assume the target journal's readers know why the broad field matters.
- Expose the concrete phenomenon, contradiction, failure condition or bottleneck by the end of the opening paragraph where the material allows.
- State the gap as something genuinely unknown, disputed or untested: what causes an advantage/failure, under what conditions a benefit appears/disappears, which mechanism or information source is necessary, why two credible bodies of evidence disagree, whether a representation adds information beyond the baseline.
- Do not define the gap as the absence of your method ("no one has used our architecture for this task" is not a scientific unknown).
- Organise citations by argumentative function: establish the known capability, show what prior work resolved, expose the unresolved condition/boundary/contradiction, make the present question unavoidable.
- Let the study's answer emerge after the question is motivated; do not force the preferred concept into the opening.
- End with a compact research route: question -> design/conceptual move -> decisive evaluation route -> principal scope of inference. Preview the logic, not every result.
- Align sections: every central Introduction question maps to a Results answer; every central Results claim has a motivated question.

## 3. Results: claim escalation

Results is an escalating evidence chain, not a chronological notebook or a dashboard.

- Each subsection answers a new scientific question and adds an independent inference.
- Open with the question and why the comparison answers it; then design, observation with statistics, and inference.
- Keep a bounded local explanation in Results when it directly resolves the experiment just reported; reserve cross-result, literature and broader implications for Discussion.
- Keep robustness in the main text when it establishes or materially bounds a claim; route reassurance-only checks to Extended Data/SI.
- Do not bury conclusion-changing negative results or boundary conditions in SI.
- Figure order mirrors claim escalation: Fig. 1 what it is -> Fig. 2 is the evaluation/resource credible -> Fig. 3 does the phenomenon exist -> Fig. 4 does it beat alternatives -> Fig. 5 does the claim survive harder conditions -> Fig. 6 what mechanism/generality/boundary follows. This is an archetype, not a fixed six-figure template.
- If two figures can both be summarised as "X performs well", merge them, demote the weaker evidence, or make the later figure ask a deeper question.

## 4. Discussion: synthesis, not replay

- Anchor the central finding briefly, then synthesise what the answers mean together.
- Address rival explanations before generalising. Reviewers look for this.
- Relate to prior work as support, revision or complication; do not flatten prior work into a baseline.
- State limitations as specific conditions where the claim stops holding, not generic modesty.
- Boundaries: dataset scope, model assumptions, assay sensitivity, population/setting, transfer limits.
- End on a concrete opportunity, measurement or capability, not praise or a broad promise.
- Do not introduce new data, citations or mechanisms in the Conclusion.

## 5. Cross-section consistency

Treat the four sections as different compressions of one claim:

- Abstract: shortest claim-evidence-implication chain.
- Introduction: why the exact question must be asked.
- Results: the full escalating evidence chain that answers it.
- Discussion: what the answers mean together.

Build a claim-location map: introduce / demonstrate / interpret / synthesise / shorten / delete. Delete repetitions that add no new evidence, boundary or interpretation. Ensure every abstract claim maps to visible Results evidence, and the final implication matches the Discussion synthesis without exceeding its boundary.

## 6. Section audits

**Abstract audit**
- Gap stated in one sharp sentence?
- Design logic explains why the question is answerable?
- One main discovery, not a list?
- One or two decisive supports/boundaries?
- Payoff specific and scope-calibrated?
- Method/dataset names hidden test passed?

**Introduction reverse outline**
| Unit | Narrowing move | Literature function | Question motivated | Results answer |
|---|---|---|---|---|
| paragraph/sentence block | | | | |

Flag units that add background without narrowing, list studies without constructing known–unknown, introduce the solution too early, claim novelty through adjectives, preview a Result with no question, or motivate a question the Results never answer.

**Results claim ladder**
- Does each subsection answer a new question?
- Is each central claim supported by a comparison, ablation or boundary test?
- Are controls and negative results visible where they matter?
- Does the next subsection follow from the previous inference?

**Discussion audit**
- Is the central advance stated as a claim, not a figure summary?
- Are rival explanations addressed?
- Is the relation to prior work specific?
- Are limitations conditions rather than disclaimers?
- Does the ending name a specific opportunity?

## 7. Deletion tests

- Delete the paragraph: does the reader still understand and have adequate evidence for the central claim? If yes, cut or move it.
- Delete the sentence: does the argument lose a claim, evidence, boundary or link? If not, cut it.
- Delete the adjective: does the claim become weaker? If not, the adjective was decoration.
- Delete the transition: does the logic still hold? If yes, the transition was decoration.
