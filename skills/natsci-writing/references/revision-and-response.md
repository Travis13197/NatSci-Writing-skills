# Revision, polishing and reviewer response

Version 1.1.0; updated 2026-11-23. Read for sentence- and paragraph-level polishing, journal-format revision, response-to-reviewers packages, or pre-submission reviewer simulation.

## 1. Polishing is reasoning repair first

A polished paragraph that performs the wrong rhetorical job is a failed edit. Before touching rhythm:
1. Identify the section's job and the paragraph's single job.
2. Check claim → evidence → boundary in each important paragraph; repair missing evidence or missing scope before word choice.
3. Check the hourglass: Introduction broad → narrow; Discussion narrow → broad.
4. Check paragraph order and topic sentences; if reverse outlining fails, fix architecture before sentences.
5. Only then correct grammar, diction, rhythm and register.

## 2. Revision mechanics

- Change only the paragraphs or claims the user flagged; keep the rest verbatim. A silent full rewrite breaks correct passages and forces re-checking.
- If a fix forces structural change, state the new structure and confirm before applying.
- Keep the terminology ledger stable; never reintroduce a retired variant.
- Re-run only the checks relevant to what changed.
- If the user's redirection reveals a wrong premise, return to the argument/confirmation step rather than patching prose.
- Track edits: location, old text, new text, reason. For bilingual deliverables, bold replaced/added spans in both languages.

## 3. Section moves (rhetorical functions)

Use these as functions, not templates; the sentence must still contain specific science.

**Introduction**: establish importance → what is known → gap/controversy → aim → value/approach. Avoid historical throat-clearing, detailed results, novelty claims before the gap.

**Methods**: design/cohort → materials/data → procedure → outcomes → analysis/statistics → ethics. Reproducibility is the test.

**Results**: orient to figure/experiment → main observation → quantitative detail → expected/unexpected pattern → comparison only if it clarifies. Avoid mechanism-length interpretation here.

**Discussion**: main finding → plausible explanation → relation to earlier work → limitations → implications → next questions. Do not repeat Results in new words; do not claim mechanism from association.

**Conclusion**: aim → decisive finding → contribution/significance → boundary/forward look. No new experiments.

**Abstract**: context → gap → approach → key result → implication. Selective; if it would not affect editorial triage, it probably does not belong.

**Title**: core entity + mechanism/context, or process + outcome + system; searchable, specific, restrained, defensible.

## 4. Phrasebank by evidence strength

- Strong: show, demonstrate, establish, reveal, identify — only with designs and data that justify them.
- Moderate: suggest, indicate, support the view that, are consistent with, point to.
- Speculative: may reflect, could arise from, appears to, seems likely, might be explained by.

Gap language: remains poorly understood, has not been examined in…, has received limited attention, few studies have addressed…, evidence remains sparse for…. Avoid "no one has ever studied" and "completely unknown".

Comparison: consistent with, accords with, broadly support; divergence: in contrast to earlier reports, differs from, one possible reason for this discrepancy is….

Limitations: pair the limitation with the actual source of uncertainty ("the generalisability is limited by the single-centre cohort"), not vague modesty.

Implication and future work must stay inside the evidence boundary; future work must grow from a real limitation, uncertainty or opportunity.

## 5. Style guardrails

- No contractions, rhetorical questions or conversational fillers in manuscript prose; first person only where the discipline and venue accept it.
- Define abbreviations at first use; one canonical spelling per term; British spelling for Nature-style prose unless the venue specifies otherwise.
- Numerals for measurements; space between value and unit; en dashes for ranges; statistical symbols consistent.
- One proposition per sentence; dependent clauses attach to a main clause; no comma splice; every paragraph has a controlling idea.
- Flag and soften prove, conclusively, unprecedented, best, superior, first. Prefer to our knowledge, among the strongest, in this cohort.
- Figure legends concise (≤300 words for Nature style); title ≤75 characters including spaces unless the journal says otherwise.
- Do not upgrade association to causation or generalisability beyond the study.

## 6. Response-to-reviewers package

Default package: response strategy summary → comment-response tracker → point-by-point letter → manuscript change checklist → missing-information/risk flags → Chinese confirmation notes when the user writes Chinese.

Decision types: minor revision, major revision, revise-and-resubmit, transfer after review, appeal-like (route separately), unclear.

Workflow:
1. Extract editor instructions (E.1, E.2) before reviewer comments (R1.1, R2.1).
2. Preserve each reviewer comment verbatim; do not paraphrase it into something easier to answer.
3. Classify: text, analysis, experiment, figure, clarification, citation, claim softening, partial, disagreement, out of scope, author input needed, blocking.
4. Map each item to a concrete action and a manuscript location; if the location or fact is unknown, mark AUTHOR_INPUT_NEEDED.
5. Draft a direct answer, the action taken, the location, and the remaining limitation. Never answer with thanks or "we revised accordingly" alone.
6. Run QA: every comment addressed; no invented experiments, citations, line numbers or panels; claims match the new evidence; tone cooperative, evidence-forward, non-defensive.

Action labels: ACCEPT_TEXT, ACCEPT_ANALYSIS, ACCEPT_EXPERIMENT, ACCEPT_FIGURE, CLARIFY_EXISTING, ADD_CITATION, SOFTEN_CLAIM, PARTIAL, DISAGREE, OUT_OF_SCOPE, AUTHOR_INPUT_NEEDED, BLOCKING.

Tone:
- Cooperative but not submissive; evidence-forward, not personality-forward; concise enough for editors to audit.
- Disagreement order: acknowledge → state the narrow point → give evidence or scope logic → make a small clarification if the manuscript invited confusion.
- Treat a reviewer misunderstanding as a presentation signal ("the original text did not make this distinction clear"), never as "the reviewer misunderstood".
- For out-of-scope requests: agree on the value, explain the design/scope reason, state the claim restriction, and add the limitation. Do not lead with time, money or convenience.

## 7. Pre-submission reviewer simulation

Return three reviewer reports plus a cross-review synthesis unless asked otherwise. Review axes: originality; scientific importance; interdisciplinary readership interest; technical soundness/technical failings; readability for non-specialists. Reviewer 1 foregrounds technical soundness, Reviewer 2 originality plus importance, Reviewer 3 broad interest plus readability; all cover all axes briefly.

Per report: overall assessment; who would be interested and why; major strengths; major concerns; technical failings that must be addressed; assessment against the five axes; recommendation posture. Synthesis: consensus strengths, consensus technical risks, emphasis differences, broad-interest readout, most important issues to resolve before a strong case is established. Flag unsupported claims and items not assessable from the supplied material; never invent reviewer identities or manuscript details.

## 8. Journal-format revision checks

- Structure and heading order match the target journal; abstract within limit; keywords present if required.
- References: style consistent, numbering/citation order correct, DOIs verified, no duplicates, no retracted papers.
- Figures: numbers and panel letters match legends and text; source data and permissions documented; file formats and sizes compliant.
- Statements: data/code availability, contributions, competing interests, ethics; each specific and durable.
- Equations and symbols render correctly; tables are editable; supplementary files listed and cited in order.
- Tracked changes or clean copy as requested; filename and version clear; original preserved.

## 9. Reviewer-side audit and response-package consistency

When reviewing a manuscript as a referee or preparing a response, use a technical-concern taxonomy rather than generic praise/criticism:

- **Design**: sampling, controls, randomisation, blinding, power, confounding, leakage.
- **Evidence**: unsupported claims, missing comparisons, weak effect size, overgeneralisation, causal overreach.
- **Statistics**: independent unit, pseudoreplication, multiplicity, model assumptions, exact reporting.
- **Reproducibility**: missing parameters, software/version, data/code access, protocol detail.
- **Figures**: evidence density, panel logic, statistical display, image integrity, caption consistency.
- **Claims and novelty**: priority, distance from prior work, incremental framing, mismatch between title/abstract and evidence.
- **Ethics and compliance**: consent, approvals, dual use, conflicts, AI disclosure, permissions.

Severity: P0 issues can invalidate a central claim; P1 issues weaken reviewability or credibility; P2 issues are clarity/consistency. Reviewer 1 foregrounds technical soundness; Reviewer 2 originality and importance; Reviewer 3 broad interest and readability; all cover all axes briefly.

**Forensic consistency audit.** Before finalising a review or response, compare numbers, sample sizes, exclusions, randomisation, software versions, figure/panel counts, accession numbers, reference lists and statements across manuscript, figures, legends, supplement, cover letter and response letter. Flag contradictions; do not silently harmonise them. A response letter must not claim a change that the manuscript does not contain; every claimed change has a location or an explicit AUTHOR_INPUT_NEEDED placeholder.

**Response-package consistency.** Strategy summary -> tracker -> letter -> change checklist -> risk flags. Preserve reviewer comments verbatim; assign each an action and manuscript location; keep readiness state (ready, draft with placeholders, needs author input, blocked). For a local edit requested without a decision letter, do not invent editor instructions; for an unclear decision type, ask or mark it.

**Reviewer visibility and role boundaries.** Do not write as the authors in a reviewer report; do not claim editorial decisions; do not invent reviewer identities or line numbers. AI may help language, but reviewers must not upload manuscripts to public LLMs or substitute model output for independent judgement; disclose AI assistance where the journal requires it.
