# NatSci-Writing-skills changelog

## 1.2.2 — 2026-11-23

Perspective and theory-manuscript upgrade derived from the mirror-world project: added nature-perspective-production and mirror-world-case-study references; Perspective outline, editing scope/change log and conceptual-figure brief templates; SKILL sections on editing fidelity, Perspective production, conceptual figures and final gates; expanded style checker; updated README/docs/manifest.

## 1.2.1 — 2026-11-23

Publication-system upgrade: added AI-use and disclosure policy, literature search/citation integrity, five-pass proofreading, Perspective/insight writing and Nature section craft references; extended reviewer/response and data/code/materials guidance; added AI-disclosure, literature-search and data/materials templates; re-polished README; integrated content from independent skills (insight-led-scientific-perspective, literature-review, grammar-checker, polish, writing-beats) and current journal AI policies.

## 1.2.0 — 2026-11-23

Package metadata update: author credited as Chuanyang Liu; provenance states that the system was built from the author's own research projects and long-term conversations and integrates Nature-skills by Yuan Yizhe (Apache-2.0); citation metadata added; license moved to source-available non-commercial terms with Apache-2.0 retained for adapted portions. Skill content unchanged.

## 1.0.0 — 2026-11-23

First public release of NatSci-Writing-skills: a complete, portable English production skill for Nature/Science-level manuscripts and figures. Consolidates the author's v2.1.0 manuscript/figure standards, the NatSci corpus analysis and nature-skills-derived production workflows. Includes references, manuscript/figure/caption/response/statement templates and tested Python/R figure starters.

## 2.1.0 — 2026-11-23

Merged the author's v1.18.0 project system and the nature-skills production system into the corpus-calibrated v2.0.0 skill, so the skill can produce complete manuscripts and complete figure sets as well as revise and format them.

End-to-end production: new manuscript-production.md covers deliverable modes, the confirmation gate, the terminology ledger, the ten-step full-manuscript pipeline, section playbooks (title, abstract including the Nature summary paragraph, introduction, results, discussion, conclusion, methods, related work), five paper-type playbooks (research, methods, algorithmic, hypothesis, review), journal format tables, the complete-manuscript package (title page, abstract, main text, methods, references, legends, statements, change log), Word/LaTeX/HTML formatting, data/code availability statements, citation management and an adversarial self-review checklist.

Figures: new figure-production.md adds the figure contract, four page archetypes, the Python/R backend gate, typography/colour/density system, chart selection, statistical display, caption conventions, export and QA. figure-standards-nature-science.md remains the journal-spec reference. The author's full 1.18.0 figure system is now bundled: figure-design-and-audit.md (42 KB), panel-layout-and-letter-placement.md, figure-colour-audit-contract.md, structural-figures-baker-standard.md, and the updated html-and-data-verification.md; v2.1.0 SKILL.md summarises the mandatory release gates (one data plot per panel, fixed axes grid, 0.38–0.42 pane-width gutters, panel-letter anchors, semantic colour audit, structure-raster packing, collision audits, evidence density).

Revision and review: new revision-and-response.md covers reasoning-first polishing, revision mechanics, section moves, phrasebank by evidence strength, style guardrails, response-letter package and action mapping, disagreement tone, reviewer simulation and journal-format checks.

Writing: SKILL.md restructured around deliverable modes, corpus-measured genre targets, writing diagnostics, claim calibration and a final quality gate; description extended to trigger on full-manuscript drafting, formatting and figure production. Existing author preferences (bilingual delivery, bolded replacements, citation placement, project geometry and colour roles) are preserved.

## 2.0.0 — 2026-11-23

Rebuilt the skill around a measured Nature/Science corpus (868 records: 489 long-form Perspective/Review papers, 379 research Articles, plus 28 Nature Methods/Biotechnology methods papers; 317 full texts and 2,320 parsed figure captions) in life science, biotechnology, protein language models and AI.

Added genre architecture grounded in journal guidance and corpus statistics: Nature summary paragraph (≤200 words, 7–8 sentences, "Here we show"), Science abstract (~125 words, 6 sentences), Nature Review preface (≤200 words, 4 display items, <7,000 words) and Perspective (personal, forward-looking, argument-led), Science Review and one-sentence Science Perspective teaser. Added paragraph and sentence targets from the corpus (research 120–140-word paragraphs; Review 150–260; Perspective 200–320; sentence median 24–27 words; hedge and connective rates).

Added writing-diagnostics.md: AI-tell lexicon with measured density, seven failure modes with before/after rewrites, sentence-level drills and a paragraph revision protocol. New SKILL.md sections cover claim calibration, numerals in prose, transition logic and a final quality gate.

Added figure-standards-nature-science.md: official Nature sizes (89/183 mm; 8 pt lowercase panel letters; 5–7 pt text; 0.25–1 pt lines; 300–600 dpi) and Science sizes (55/120/183 mm; uppercase panel letters), panel construction by evidence type, five-part caption grammar, statistical display, accessibility, export and an audit sequence. figure-design-and-audit.md updated to v2 and linked to the journal standard.

Added journal-style-evidence.md documenting corpus construction, coverage, measured statistics, genre definitions, exemplar DOIs and limitations. Version bumped to 2.0.0; existing author preferences (bilingual delivery, bolding, citation placement, project geometry and Okabe–Ito colour roles) are preserved.

## 1.4.0 — 2026-11-13

Clarified that a square panel means equal visual x- and y-axis lengths inside the data plotting box, with an aspect ratio of 0.9–1.1. The whole composite, PNG and HTML card can remain rectangular.

Added a journal type hierarchy and crowding rules: essential text is normally at least 6 pt, axis labels about 7.5–8 pt and panel letters about 9.5–10 pt. Resolve crowding through canvas, grid, title, tick-density and adjacent-residue adjustments rather than reducing key text to 4–5 pt. The audit now records typography, geometry, wide exceptions and text collisions.

## 1.3.1 — 2026-11-13

Added a worked figure-audit example to `references/figure-design-and-audit.md`. Regular data axes use a 0.9–1.1 near-square plotting box; Figure 4a/4e, CDS tracks, 384-well layouts and full-length residue tracks are registered as purposeful wide exceptions.

Defined project colour roles for the Science-style accents: PA, Per-OH and S-Lim use navy, teal and amber; LMSF and DAMP reporter channels use teal and reddish purple; positive and negative model-comparison directions use blue and vermillion. The audit record now requires before/after panel-geometry tables, an exception ledger, collision checks, image exports, HTML browser checks and caption colour verification.

## 1.3.0 — 2026-11-13

Added `references/figure-design-and-audit.md` with a unified workflow for scientific purpose, panel geometry, colour roles, structural-plus-statistical composition, export and review.

Analytical panels default to a near-square box aspect of 0.9–1.1. Long sequence, operon, timeline, plate-map and explicitly longitudinal panels can use wide geometry, with every exception recorded.

Blue remains the primary project identity, with restrained Science-style Okabe–Ito accents in teal, amber, vermillion and reddish purple. Structure and statistical panels share residues, states and colour mapping, with essential values visible and traceable to source data.

## 1.2.0 — 2026-11-13

扩展课题构思与研究框架设计，要求通过中心假设、区分性预测、干预、对照和独立证据发展原创科学洞见。前沿调研保留检索日期、原始文献和逐项证据来源。

强化完整阅读、逐句润色及自然学术表达，覆盖正文、图注、表格、附录和动态科学文字；改写模板化否定转折、防御性语气及含义不清的抽象表达。保留影响结论的真实对照、阴性结果、条件及不确定性。

新增数据真实性与计算核验流程，追溯输入、代码、统计口径和图文结果，区分报告值算术核对与原始数据重现。

新增 research-and-language.md、html-and-data-verification.md 和可直接复用的 academic-prompt-zh.md。保留独立中文论文技能 nature-biology-manuscript-writing-zh，配齐全部参考文件，并同步项目便携副本。

保留原有 SEAL、维度回译与功能注释专题资料。备份和维护脚本位于项目 AI-files 独立工作目录。

## 1.1.0 — 2026-11-11

本次依据 SEAL 稿件后续讨论更新原有技能，保留名称 `nature-biology-manuscript-writing`。

### 通用写作规范

强化 Results 的主要发现及研究目的，说明每个案例的选择缘由；保留会影响结论的必要信息，将算法细节、次要比较和局限分别安排到 Methods、补充材料及 Discussion。避免正文被审计细节淹没，也避免通过省略对照或更换指标夸大结果。

要求图文修改先完整读图并检查清晰局部，核对坐标轴、阈值、点色、维度集合、聚合方式及残基编号。明确区分原始值、归一化值、排名和百分位，以及结构映射与实际构象条件化输入。

保留作者原意及已定稿术语优先、句间逻辑递进、具体生物学表达、引文位于句点前、中英逐段对应、全部新增和替换文字加粗、完整复读及原始文件保护等要求。

### 维度回译专题

新增 `references/translation-validation.md`，以“HVDim/选定维度—残基响应矩阵—确定的选点规则—独立结构与功能证据”为论证主线。记录生成熵与 KL 响应四种组合的准确含义，区分最大构象位移、运动控制、催化贡献及模型敏感性。说明 ADK 与 CarH 各自的案例价值，并区分原始候选、独立文献位点和本轮新增复算。

### 功能注释专题

新增 `references/dimension-annotation.md`，明确模块 IV 的目标是基于维度给蛋白质或指定蛋白质集合注释功能；维度–功能参照库的建立服务于这一目标。解释 signed 的关联方向、与基因集合的类比、超几何评分和用户定义群体的 HVDim 分析，保留不同实现之间的区别。

更新四类注释库的规模、RING 参考/查询队列、注释恢复与候选覆盖的统计口径。记录逐条目显著性、特征选择隔离及资源公开状态的核查结果，要求使用新数据时重新确认，避免将历史问题视为永久结论。

### 资源与维护

公开可用声明需要真实仓库、可访问文件及相应模型/版本依据。未核实的 GitHub 地址不写成已经发布。原技能保留备份，管理目录与项目便携副本保持一致。

### 检查范围

完成技能元数据与结构校验、专题引用和写作规则覆盖检查，并进行独立只读内容复核。未进行生成质量的对照实验，也未将这些检查表述为论文录用或模型性能保证。