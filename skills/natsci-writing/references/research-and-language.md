# Research design, evidence synthesis and natural academic language

Compatible with skill v1.1.0; updated 2026-11-13. Sentence- and paragraph-level style diagnostics are in the writing-diagnostics reference of this skill (English or Chinese edition); the measured corpus basis is in the journal-style-evidence reference. Read this entire reference for research-topic design, original hypotheses, literature-grounded frameworks, substantial conceptual revision, or comprehensive language polishing. Apply it with the parent SKILL.md.

## 1. Select the actual task

Treat requests to update a skill as instruction-maintenance tasks. A research topic, manuscript or HTML mentioned inside a reusable prompt describes the skill's future behaviour; it does not by itself authorize a new scientific study or modification of an unrelated manuscript.

For research design, identify the biological system, unresolved question, available observations, proposed mechanism and decisive measurements. For language revision, preserve the supplied scientific object, findings and approved structure. For a complete rewrite, inspect the whole requested document and improve every sentence that needs revision. Preserve scientifically accurate, natural sentences.

Use Nature and Science as aspirations for scientific depth, coherent argument and exact expression. Verify article-type and journal requirements from current official guidance when submission compliance is requested.

## 2. Develop originality through explanatory consequences

Formulate a biological question whose resolution would change a specific explanation, measurement or experimental decision. State the biological object, the process under investigation and the observable consequence in ordinary academic language.

Develop several plausible explanations internally and compare their distinct predictions. Select the research framework with the clearest scientific advance, strongest evidential basis and most informative experiments. An original contribution can reveal a mechanism, explain an unresolved pattern, connect measurements across scales, or enable a previously inaccessible test. Naming several advanced technologies together supplies a tool list; explain the biological relationship each tool helps test.

Construct the reasoning chain: established observation → unresolved relationship → central hypothesis → mechanistic prediction → decisive intervention or analysis → interpretable result → next scientific inference. Explain how each inference follows from the observations and what new prediction it generates.

For each research aim, define the system, intervention, readout, comparison, experimental unit and predicted outcome under the main competing explanations. Include appropriate controls, orthogonal measurements and independent evaluation. Choose models, baselines and ablations according to the question. Explain the additional information obtained from each experiment.

Support causal claims with a design appropriate to the mechanism, such as temporal ordering, targeted perturbation, dose response, rescue, epistasis or independent mechanistic measurements. Select the relevant tests; avoid treating this list as a universal experimental recipe. Separate biological replicates from repeated measurements of the same sample.

Describe proposed work with explicit prospective verbs: “we propose”, “the study will test”, “we hypothesize”, “拟检验”, “计划测定”, “假设”. Describe measured findings with the verbs justified by their evidence. Expected outcomes remain predictions throughout the text, tables and figure captions. Numerical effect sizes and significance values require actual data or a clearly identified simulation.

## 3. Conduct and synthesize online research

When the user requests online research, frontier findings, citation verification or novelty assessment, search the web. Derive queries from the biological mechanism, nearest methods, competing explanations, relevant experimental systems and independent validation. Use English and relevant Chinese terms where they improve retrieval. Cover foundational studies and the most recent work available on the search date.

Prioritize original papers, publisher pages, primary databases, official resource records and author repositories. Use reviews to locate concepts and primary evidence. Follow important references backward and forward, and inspect closely related studies that could change the proposed contribution. Check corrections, retractions and publication updates where relevant.

Keep a compact working evidence record: query and search date; source title and identifier; publication date and status; biological system; experimental design; key result; exact supporting section, figure or table; and the claim it supports. Record whether the abstract, selected sections or full text were actually read. Distinguish a preprint from its later published version and connect both records when appropriate.

Synthesize the evidence by scientific question and mechanism. Explain where studies converge, which differences in systems or methods account for divergent results, and which experiment would resolve the remaining question. A sequence of paper summaries leaves the conceptual synthesis unfinished.

Assess originality against the closest primary studies. Identify the specific advance in explanation, measurement or experimental discrimination. Use a defined search scope and an exact search date for claims about the current state of research. A finite search supports a documented novelty assessment; preserve accurate attribution throughout.

Verify author, title, year, DOI or other identifier and publication status before citing a paper. Check that the cited source supports the accompanying statement. Distinguish database membership, predicted annotation and direct experimental evidence. Maintain evidence links in the final HTML or manuscript reference system. Follow the host platform's citation syntax in chat.

Research the scientific question actually supplied. When this reference is being edited as part of skill maintenance, an external literature search is needed only for scientific assertions or current guidance being added to the skill.

## 4. Write with scientific depth and identifiable biological meaning

Use complete, connected paragraphs for manuscript prose and scientific HTML. Organize each paragraph around one scientific message. Link observations, comparisons, explanation and consequence through explicit relationships. Place the biological purpose before the analysis result. Use headings to organize substantial sections; keep checklists and editorial tables outside the manuscript paragraphs.

For each abstract term, identify its referent: which molecule, residue, cell population, phenotype, dataset, model quantity, intervention or measured relationship does the sentence describe? Define unfamiliar technical terms when they first become necessary. Retain established biological terminology. Explain mathematical and AI concepts through their inputs, operations, outputs and biological interpretation.

Describe an insight by explaining a previously unresolved relationship and the observation or prediction it accounts for. Words such as “profound”, “non-trivial”, “paradigm” and “universal” add no evidence on their own. Show intellectual depth through the reasoning.

Replace strings of abstract nouns with subjects, actions and measurements. Terms such as geometry, representation, sector, direction, mediation and readout require a clear definition and a relationship to the biological question. Keep the same technical term for the same object.

## 5. Remove formulaic contrast and defensive framing

Rewrite formulaic opposition, concession and correction as direct, connected statements. Patterns requiring inspection include “not X, but Y”, “not X; rather, Y”, “rather than”, “X, but Y”, “however”, “yet”, “不是……而是……”, “并非……而是……”, “不……而……”, “……，但……”, “……，而……”, “尽管……但是……”, “不能据此……”, “需要谨慎……”, “必须强调……”, and repetitive “仅仅/只能/尚不能” framing. Inspect the meaning of a sentence; replacing individual conjunctions mechanically can damage the argument.

Write the supported scientific statement directly, together with its biological object, comparison and experimental conditions. Express future experiments as a purposeful research step. Keep routine caveats, self-evaluation, journal-quality assurances and descriptions of the editing process out of the scientific narrative.

Preserve substantive evidence, null findings, contrary controls, uncertainty estimates and conditions that determine the meaning of a result. State them in concrete scientific language. An absent measured effect can be stated with its estimate, interval, assay and comparison. A computational association can be described as a computational association. These formulations preserve the science while keeping the prose focused.

Move unresolved source-file problems and repair requirements to a separate author-facing record. If an issue changes a conclusion, correct that conclusion and retain the necessary experimental definition in the scientific text. Never convert an unverified result into an established fact through stylistic editing.

## 6. Examples of clear revision

These examples demonstrate language repair, not scientific findings. Use them only when the supplied evidence establishes the stated objects and relationships.

Unclear: “程序在函数层稳定，而不需要唯一原子。”
Action: identify what “程序”, “函数层”, “稳定” and “原子” refer to in the source. If the data show several distinct residue combinations with comparable activity, write “多组残基组合在所测条件下表现出相近的酶活性。” If the source supplies no concrete referents, record the ambiguity for the author and retain only the supported statement.

Unclear: “共同几何存在，但生物学不会自动跟着迁移。”
Possible revision with appropriate evidence: “两种模型形成了相似的蛋白质分布。跨模型功能预测可通过独立标注的蛋白质集合进一步评估。” Specify the distribution measure and actual evaluation when available.

Unclear: “高加性读出中仍可识别连通响应。”
Possible revision with appropriate evidence: “联合扰动的预测效应接近各单独扰动效应之和。响应较强的残基在三维结构中形成相邻区域。” Define the additivity measure, response variable and spatial criterion in Methods.

Unclear: “物理与 AI 保持不同的可观测扇区。”
Possible revision with appropriate evidence: “分子实验测量蛋白质的构象变化，模型分析量化指定输入变化引起的预测响应。” Name the actual experiment and model output.

Unclear: “全局软方向是一个真实的中介对象。”
Action: identify the measured movement and the proposed mediation mechanism. If the analyses support the sequence of events, write “该集体运动连接配体结合与催化区域的构象变化。” State causal mediation only when the design supports it.

## 7. Sentence-level completion check

Read each revised sentence aloud internally. Identify its subject, scientific action, object, evidence and connection to its neighbours. Remove unsupported evaluations, overloaded clauses, slogan-like endings and repeated generic transitions. Check that a biologist can explain what happened after reading the sentence once.

For English–Chinese output, compare scientific meaning paragraph by paragraph. Preserve candidate status, prediction status, direction, comparison, units, numbers and statistical meaning. For Chinese-only work, compose natural Chinese academic prose directly and use English only for established technical names and necessary first-use definitions.
