# Defensive writing and argument selection

Read this file before polishing any sentence: it decides **what the paper dares to claim and what it dares to drop**. Sentence-surface problems belong to `writing-diagnostics.md`; this file owns the argument.

## 0. Two failure families that read the same

| Failure | What the reviewer sees | Root cause |
|---|---|---|
| **Defensive writing** | The manuscript argues against itself: every claim arrives with its own rebuttal, limitations precede contributions, the conclusion withdraws what the abstract promised. | Writing for an imagined hostile reviewer instead of a reader who wants the result. |
| **Generated prose** | The manuscript argues nothing in particular: balanced paragraphs, symmetrical sections, informative-sounding sentences with no object, number or mechanism. | Producing text that satisfies the shape of a paragraph rather than its content. |

Both are cured by the same move: **decide what the paper wins, then spend every paragraph on it.** A defensive draft and an AI-flavoured draft are the same paper before and after that decision.

## 1. The press-release principle

A paper is a press conference, not a project summary, a lab log or a self-audit. The task is not to present every aspect of the work evenly, but to identify the most publishable value and build the most favourable *complete* narrative around it. "Complete" is load-bearing: completeness means every required element is present, not that every element that could be computed is reported.

## 2. Argument selection (do this before any wording)

**2.1 Find the one thing only this paper has.** Candidate advantages: a new capability; a new problem; a new mechanism; a new regime or scale; a stricter test that existing claims fail; a cost, speed or data advantage; a trade-off that is now quantified rather than asserted. If two candidates tie, the paper has no headline — choose the one the evidence can carry alone.

**2.2 The three-question test.** Answer all three in one sentence each, without adjectives:
1. What do we win — the specific relation, not the topic.
2. By how much, on what measure, against what comparator.
3. On what ground does it hold — the condition, system or regime where the claim is earned.
If question 2 has no number and question 3 has no condition, the paper is not ready to be written; it is ready to be run.

**2.3 Choose the battlefield.** You are not obliged to enter a contest you cannot win. A metric where you lose is not automatically the main metric: re-choose the task definition, the evaluation dimension, the operating regime, the constraint set or the comparison frame that reflects what the work actually establishes — **then say which game you won.** This is selection, not spin: the new frame must be defensible on its own terms, and the old frame must not be hidden if a reader would reasonably apply it.

**2.4 Space must follow argument, not effort.** The most common structural tell of a lab-log paper: every figure receives one section, every experiment one paragraph, because every experiment cost the same. Allocate text by evidential weight. A 3-month negative control is one sentence; the decisive experiment is half a page.

**2.5 Ban chronology.** Never "we first did X, then tried Y, and Z failed". Keep only the standing logic: why the problem matters → why existing approaches fall short → what this paper provides → how the evidence supports it. Failed branches appear only if they rule out an alternative explanation a reader would otherwise hold.

**2.6 Restructuring is permitted and sometimes mandatory.** When the results cannot carry the original story, do not defend the story. Re-pick the headline result, re-order contributions, rewrite title, abstract, introduction and figure set, and record the change in the claim ledger. Loyalty is owed to the evidence, not to the first plan.

## 3. Every experiment carries one duty

An experiment is an instrument of argument, not a warehouse entry. Assign each one exactly one duty and write it down before drafting:

| Duty | Question it answers | Where it belongs |
|---|---|---|
| **Existence** | Does the effect occur at all? | First main figure |
| **Mechanism** | Is the stated cause the cause? | Ablation, perturbation, rescue |
| **Regime** | Where does it hold, and where does it stop? | Held-out systems, stress conditions |
| **Exclusion** | Which competing explanation is ruled out? | Matched controls, null models |
| **Value** | Does it matter for the claimed use? | Prospective or applied panel |

An experiment with no duty is deleted, demoted to Extended Data, or merged. An experiment with two duties is usually one experiment and one claim too many.

## 4. Section-level defensive audit

| Section | Defensive failure | Control |
|---|---|---|
| Title / abstract | Caveat creep: "a preliminary exploration of …" | Zero limitation sentences. First five sentences carry problem, gap, approach, headline number. |
| Introduction | Pre-emptive concession paragraph ("although our approach has limitations …") before the contribution is established | No caveat before the first statement of what this paper does. |
| Results | Claims without number, condition or comparator; "it is interesting to note that …" | Every subsection opens with the claim it establishes; each claim carries its measure. |
| Discussion | Limitation wall: 8–12 sentences of self-audit scattered across three paragraphs | **One** limitation paragraph, ≤3 sentences, each in the form condition → scope → consequence. Other caveats are folded into the results sentence they qualify. |
| Conclusion | Fresh self-negation in the final paragraph | Last sentence is the takeaway. No new limitation, no "future work" paragraph as the final beat. |
| Cover letter | Apologising for the study's scope | State the claim and why it matters now; scope is a sentence, not a confession. |
| Response letter | Conceding every point to seem agreeable | Concede what the data concede; answer the rest with the evidence. |

## 5. Rhetorical hedging vs epistemic calibration

This is the boundary that keeps anti-defensive rules from becoming overclaiming.

**The deletion test.** Remove the hedge and ask: *could a careful reader now be misled about what was measured?*
- **No** → rhetorical hedge. Delete it. ("It is worth noting that", "to some extent", "we merely", "arguably")
- **Yes** → calibration. Keep it, but make it *specific*: condition → scope → consequence, in the same sentence as the claim it qualifies. ("In the 34 held-out families — not in the 12 low-homology ones — the gain is 0.08.")

| Hedge | Diagnosis | Action |
|---|---|---|
| "may potentially" | redundant modality | delete |
| "to some extent" | unfalsifiable degree | replace with the measured degree |
| "further work is needed" | universal disclaimer | delete or state the specific open question |
| "only in E. coli" | scope calibration | keep — attach it to the claim, do not banish it to the discussion |
| "n = 3, single site" | power/coverage calibration | keep — with the consequence for interpretation |
| "the assay cannot distinguish X from Y" | measurement limitation | keep — it bounds the claim |

**Absolute prohibitions — the anti-defensive rules never license these:**
1. No claim without evidence; no number without its measurement.
2. Never delete a limitation that changes how a result must be read — relocate and compress it, do not remove it.
3. Never convert a negative result into a positive one by rewording; "we did not detect X" stays "we did not detect X".
4. Never generalise from one system, one site or one condition to a class without a stated bridge.
5. Never hide the comparator, the null model or the failed baseline that a reader would ask for.
6. Statistics, reporting-integrity and AI-use rules in this skill override every stylistic preference here. Style may not buy what data cannot pay for.

## 6. Where defensiveness hides

- Caveat in the first two sentences of the abstract.
- Stacked concessive openers: "Although …", "While …", "Despite …" as the default sentence shape.
- Limitation scattering: a small apology in every section, so no section can be quoted alone.
- Double claims: "we show X, though only in Y" written as one sentence, so the grant and the withdrawal cannot be separated.
- Reviewer anticipation: "one might argue that …", "it could be objected that …" — answering an objection nobody raised.
- False modesty: "we merely", "a first step towards", "preliminary".
- Supplemental dumping: putting the awkward result in Extended Data without acknowledging it in the main text.
- Symmetric comparison tables that invite a contest the paper loses, placed in the main figures.
- Conclusion that reopens the question the abstract closed.

## 7. Revision protocol (argument level)

1. **Claim inventory** — list every claim the manuscript asserts, with its measure and condition; mark unsupported ones.
2. **Duty assignment** — map each experiment to one duty; delete or demote the unassigned.
3. **Battlefield** — name the game; check that the main figures argue it.
4. **Caveat consolidation** — collect every apology in the document into one place; keep what qualifies a specific claim, delete the rest.
5. **Hedge triage** — apply the deletion test sentence by sentence.
6. **Opening and closing** — rewrite the first five abstract sentences and the last conclusion sentence as a pair; they must state the same claim.
7. **Reader test** — give the abstract to someone who has not seen the paper; ask them to state the claim, the measure and the condition. If they cannot, the argument is still defensive.

## 8. Measured gates

Run `python tools/check_prose_style.py --gate <file>`; the structural metrics are reported per document. `--genre perspective` widens the hedge and limitation caps for proposals and theory papers, where modality is calibration; `--genre report` reports metrics without gating them.

| Metric | Target | Note |
|---|---|---|
| Limitation sentences in abstract | 0 | manual + `defensive.*` hits |
| Limitation paragraphs per manuscript | ≤1 | manual |
| Paragraphs with a claim in the first sentence | ≥80% | `--metrics` |
| Hedge density | ≤4 per 1,000 words (EN), ≤3 per 1,000 characters (ZH) | `--metrics` |
| Recap tails ("Overall, …", "综上所述") | ≤1 per 1,000 words | `--metrics` |
| Sentence-length CV | 0.30–0.65 | below 0.30 is machine rhythm |
| Triad density | ≤1 per 500 words | `--metrics` |
| Nominalisation ratio (EN) | ≤12% of content words | `--metrics` |
| Em dashes | ≤2 per 1,000 words | `--metrics` |

## 9. Applying it to letters

- **Cover letter**: one paragraph on the claim and its measure, one on why it matters now, one on fit. No scope apology.
- **Response letter**: restate each reviewer point in the reviewer's terms; answer with the new evidence; where you decline, say what you did instead and why it is sufficient. Never open with an apology for the manuscript.

## 10. Chinese manuscripts

The same rules, with Chinese-specific surface forms:

- **谦辞与自贬**：不揣浅陋、抛砖引玉、浅析、初探、以期、仅供参考、难免有疏漏 — delete; state the scope instead.
- **程序性叙述**："我们先……随后……最后……"、"本文首先回顾……" — delete; keep the standing logic.
- **空转定语**："具有一定的理论意义和实践价值"、"为……提供了新思路"、"在……背景下" — replace with the specific relation or delete.
- **对称让步**："虽然……但是……" 作为段落默认骨架；改写为两个肯定句，让步只在必要处出现一次。
- **局限集中**：全文只保留一段局限，位置在讨论末尾，三句以内，每句写明条件→范围→后果。

## 11. Sources and attribution

- Anti-defensive-writing skill by **Adkid-Zephyr** (MIT License, 2026): https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill — the press-release principle, narrative rules, experiment duties, decision priority order and the pre-submission "no knife for the reviewer" checklist are adapted from it, rewritten for manuscript production and bounded by the calibration rules in §5.
- Signs of AI writing (Wikipedia): https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- AI Smells field guide: https://github.com/williamsmithedward/pyvbaanalysis/blob/main/docs/AI-Smells-Agents-Avoid.md
