# Usage

## 1. Choose the mode

| Mode | Ask for | Typical artifact |
|---|---|---|
| Complete draft | a full manuscript from data, figures, notes or a Chinese draft | complete manuscript + assumptions + missing-input list |
| Section draft | abstract, introduction, results, discussion, methods, review or perspective section | ready-to-paste section |
| Rebuild | restructure an existing draft | new architecture + rewritten sections |
| Polish | sentence/paragraph revision | revised text + change log |
| Format | convert to a target journal | compliant layout, references, statements, legends |
| Figure set | publication figures for a claim | figure contract, files, captions, audit |
| Response | reviewer comments + revision facts | letter + tracker + change checklist |
| Editorial audit | manuscript + target journal | fit assessment, readiness state, missing-fact list |
| Submission package | manuscript + author facts | cover letter, title page, declarations, reviewer suggestions |
| Statistics audit | methods/results/legends | P0/P1/P2 issues, revised text, AUTHOR_INPUT_NEEDED list |
| AI integrity audit | AI-assisted manuscript + target journal | disclosure statement, prohibited-use check, citation/number verification |
| Literature audit | manuscript/review + claims | search record, evidence table, verified references |
| Proofread | full or section text | five-pass issue log + corrected text |
| Perspective development | topic/notes/exemplars | intellectual centre, discovery sequence, draft |
| Perspective production | design docs/author text | six-section manuscript, Box/figures, bilingual package, template |
| Author-faithful edit | source file + mode | revised copy, change log, residual questions |
| Theory-paper audit | manuscript + claims | evidence ledger, three-discipline review, figure/format audit |
| AI writing audit | manuscript + AI log | policy check, AI negative list, disclosure and verification record |
| AI figure audit | figure + generation record | figure class, provenance record, disclosure, image negative checklist |
| Pre-submission review | manuscript | three reviewer reports + synthesis |

## 2. What to supply

The agent produces a strong draft when it receives:

- the core claim, even one sentence;
- evidence: figures, tables, analyses, statistics, datasets;
- boundary: where the claim stops;
- target journal or article type;
- terminology that must not change;
- language: English, Chinese or bilingual.

If claim, evidence or boundary is missing, the skill returns a scaffold with visible placeholders instead of inventing content.

## 3. Complete-manuscript flow

1. Agent echoes the one-sentence argument, paper type, outline and terminology ledger.
2. Agent maps each claim to evidence and marks gaps.
3. Agent drafts Results first, then Introduction/Conclusion, Discussion, Methods, Abstract, Title.
4. Agent runs consistency checks (numbers, units, figure/panel references, citation order, tense, claim strength).
5. Agent runs the adversarial self-review.
6. Agent delivers the manuscript package: title page, abstract, main text, methods, references, legends, extended data list, statements, assumptions, change log.

## 4. Figure flow

1. Write the figure contract: core conclusion, archetype, panel map, evidence hierarchy, statistics, source data, reviewer risks.
2. Choose Python or R; the backend is exclusive for plotting, preview and export.
3. Select panels by reading order: system/design → primary comparison → mechanism/localisation → quantification → robustness.
4. Apply journal specifications and project gates (type size, width, colour roles, gutters, panel letters, caption statistics).
5. Export SVG/PDF plus 300–600-dpi raster; for SEAL, export each panel as an editable SVG with its own letter and labels, and record the audit.
6. Deliver figure files, captions, source-data map and release checks.

Starter scripts:

~~~bash
python skills/natsci-writing/assets/code/figure_python.py --demo --out ./figures
Rscript skills/natsci-writing/assets/code/figure_r.R --demo --out ./figures
~~~

## 5. Editorial audit and submission

1. Record stage (initial, revision, accepted-in-principle, proof) and verify journal/article-type limits.
2. Score originality, importance, interdisciplinary interest, soundness and readability in one sentence each.
3. Run the why-this / why-now / why-broad test and name the audience outside the specialty.
4. Build the deliverable matrix; draft cover letter, title page, declarations and reviewer suggestions only from author-confirmed facts.
5. Return ready / ready_with_author_checks / blocked with missing facts listed.

## 6. Innovation and positioning

Classify contribution type and rung; state the exact scientific unknown; list competing explanations and discriminating predictions; test broad interest; position against closest prior work without flattening it. Use the innovation canvas template.

## 7. Statistics audit

Define the independent unit and replicate hierarchy; check exact n, error definitions, tests, tails, correction and exact P values; align figure legends and Source Data; check Reporting Summary, image integrity and data/code/materials statements. Return P0/P1/P2 issues and AUTHOR_INPUT_NEEDED facts.

## 8. Revision flow

Repair reasoning first: section job, claim → evidence → boundary, hourglass, topic sentences; then grammar and register. Change only flagged passages unless a structural change is confirmed. Return tracked changes, bilingual alignment when requested, and a change log.

## 9. Response flow

Preserve reviewer comments verbatim; classify each item; map to an action and a manuscript location; flag missing facts as AUTHOR_INPUT_NEEDED; keep the tone cooperative, evidence-forward and non-defensive. Deliver strategy summary, tracker, letter, change checklist and risk flags.

## 10. Bilingual delivery

- For an English manuscript with Chinese notes, deliver English prose plus a corresponding Chinese version when asked.
- Bold replaced or added spans relative to the author's latest text.
- Keep evidence strength matched across languages: candidate, associated, predicted, demonstrated.
- For a standalone Chinese paper, use natsci-writing-zh and write native Chinese, not a translation of English scaffolding.

## 11. Prompt patterns

- "Here are my claim, figures and notes. Write the complete Nature Article; mark anything missing."
- "Draft the Discussion only; preserve my Results and terminology."
- "Turn this manuscript into Nature format; do not change scientific meaning."
- "Build the figure set; ask Python or R; give the contract and panel map first."
- "Draft the response letter; here are the reviewer comments and my revision notes."

## 12. Perspective and author-fidelity gates

- Perspective: one thesis, six sections, five-level evidence ledger, full paragraphs, no lists inside the argument, boundaries in one paragraph, 2–3 bold single-sentence insights per subsection, conceptual figures with legends at the end.
- Editing: agree on light polish / author-faithful expansion / structural rewrite / translation / tracked revision; protect the author's claim order and wording; copy the source; keep a change log.
- Bilingual: identical claims, numbers, citations, certainty and emphasis; natural Chinese and matching academic English.

## 13. AI writing and AI figure gates

- AI writing: check the journal policy, log tools/tasks, verify references/numbers/methods, run the AI negative list, and confirm no fabricated data, paper-mill patterns or detection evasion.
- AI figures: classify data vs conceptual; data figures use real data and code; conceptual AI figures need permission, disclosure, human verification and a provenance record; no synthetic research images, generative fill, fake scale bars or undisclosed cover art.
- Final: complete ai-negative-checklist.md and, for each AI-assisted figure, ai-image-provenance-record.md.

## 14. AI, literature and proofreading gates

- AI integrity: check the target journal policy; log tools/tasks; remove confidential material; verify every AI-suggested reference/number; draft the required disclosure; confirm a human can defend every sentence.
- Literature: document databases, strings and dates; screen and extract; synthesize by question/mechanism; verify every DOI/title/author and preprint/retraction status; keep the library.
- Proofreading: run five passes, then numbers, units, statistics, references, figure/table citations and markup; list residual author questions.

## 15. Common failure modes to avoid

- Asking for prose before the claim and evidence are fixed.
- Supplying figures without source data or statistics; captions cannot be completed honestly.
- Mixing journal figure print sizes with the larger HTML/project type roles in one deliverable.
- Requesting a full rewrite when only local repair is needed.
- Expecting the skill to invent experiments, citations, line numbers or reviewer identities.
