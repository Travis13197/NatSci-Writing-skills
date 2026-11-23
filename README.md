# NatSci-Writing-skills  |  Nature/Science 顶级学术论文写作和作图skill（生命科学+AI版本）

**Author:** Chuanyang Liu  |  作者：Chuanyang Liu  
**Citation:** a related paper is in preparation and will be updated; if you use these skills, please cite it and this repository.  |  引用：相关论文准备中并会更新；使用本 skills 请引用论文与本仓库。

Most writing advice tells you to "be clearer" and "tell a story". That is not enough when a real editor is deciding whether your paper is worth review. This package is the opposite of that advice: a working system of rules, templates, checks and figure code that turns data, figures and rough notes into a manuscript you can actually submit.  |  结合AI Coder，能够使用skills直接把数据、Manuscript推进到Nature Science期刊可直接投稿的稿件状态，也会润色、会作图。

It is built for one job: produce complete manuscripts and complete figure sets at Nature/Science standard, then revise, format and defend them.  |  目标只有一个:按照 Nature/Science 标准写出完整论文和整套图件，并能修订、排版、回复审稿。

## Where it comes from  |  它从哪里来

This is not a generic prompt collection. I built the rules, section playbooks, figure contracts, statistics checks and revision workflows from my own research projects and long-term conversations with AI coding agents — from real manuscripts, figures, reviews and rewrites.  |  中文：不是通用提示词合集，而是从作者自己的科研课题、长期与 AI 编程助手的对话、真实稿件/图件/审稿/返修中沉淀出的规则、章节 playbook、图件合同、统计检查和修订流程。

It also integrates and adapts the open-source **Nature-skills** project by **Yuan Yizhe (袁一哲)** — https://github.com/Yuan1z0825/nature-skills — under Apache-2.0, with attribution kept in NOTICE.md and LICENSES/.  |  中文：同时整合并改编了袁一哲的开源项目 Nature-skills（地址：https://github.com/Yuan1z0825/nature-skills，Apache-2.0），署名保留在 NOTICE.md 与 LICENSES/。

## What this is  |  这是什么

Two self-contained agent skills, one English and one Chinese. Each contains a SKILL.md operating manual, a reference library, working templates and tested Python/R figure starters.  |  中英文各一个自包含技能，每个都带操作手册、参考库、模板和已测试的绘图脚本。

No absolute paths. No network calls. No external corpus needed at run time. Copy the folder, load SKILL.md, and work.  |  没有绝对路径、不联网、运行时不依赖外部语料；直接复制文件夹、加载 SKILL.md 即可使用。

| Skill | Language | Version | Folder | 中文说明 |
|---|---|---|---|---|
| natsci-writing | English | 1.2.0 | skills/natsci-writing/ | 英文写作与作图 |
| natsci-writing-zh | 中文 | 1.2.0 | skills/natsci-writing-zh/ | 写作与作图 |

## What you can actually do with it  |  你能用它做什么：Anything about Nature、Science

- **Write a complete manuscript.** Title, summary paragraph, introduction, results, discussion, methods, references, legends, statements, supplementary list and change log, in one pass.  |  一次性写出Nature、Science级别的标题、摘要、引言、结果、讨论、方法、参考文献、图注、声明和补充材料清单。
- **Build a submission-grade figure set.** Start from one claim, get a figure contract, panel map, publication styling, statistical display, SVG/PDF/600-dpi files and captions.  |  从一个论断出发，得到图件合同、面板地图、投稿级样式、统计呈现、SVG/PDF/600 dpi 文件和图注。
- **Revise and polish.** Repair the reasoning before the sentences; remove AI tone and translationese; deliver tracked bilingual changes.  |  先修论证再修文字；去 AI 味和翻译腔；交付中英对照的加粗修订。
- **Format for a target journal.** Nature, Science or Nature Communications structure, references, statements, equations and line numbers, without changing the science.  |  按目标期刊调整结构、参考文献、声明、公式和行号，不改变科学内容。
- **Respond to reviewers.** Point-by-point letter, comment tracker, action mapping, tone control and change checklist.  |  逐点回复信、意见跟踪表、动作映射、语气控制和修改清单。
- **Audit editorial fit.** Test originality, importance, broad interest, soundness and readability before you submit.  |  投稿前用编辑标准检查原创性、重要性、广泛兴趣、可靠性和可读性。
- **Audit statistics and integrity.** Independent unit, replication, exact n and P values, Reporting Summary, image integrity, data/code/materials statements.  |  审计独立实验单位、重复、精确 n 与 P 值、Reporting Summary、图像诚信和数据/代码/材料声明。
- **Control information density.** Decide what belongs in the main text, captions and SI; stop revision bloat.  |  决定什么进正文、图注和补充材料，控制返修导致的篇幅膨胀。

## The idea behind it  |  背后的思路

Top-journal writing fails in three places: the argument is thin, the evidence is badly placed, or the prose and figures do not let a busy reader see why it matters.  |  解决顶刊写作通常出现三种问题：论证单薄、放错位置，以及 **文字和图让读者无法直接看出重要性。**

So the system enforces gates. Before drafting: innovation canvas and editorial fit. During drafting: main-text discipline and evidence chains. Before submission: statistics, reporting integrity and figure audits. After review: point-by-point response and claim calibration.  |  因此系统设置流程：写作前查创新与编辑契合；写作中控制正文纪律与证据链；投稿前查统计、报告诚信和图件；返修时做逐点回复和断言校准。

None of this guarantees acceptance. It removes the avoidable reasons a good paper gets rejected or delayed. 

## Quality bar  |  质量门槛

- **Argument:** one sentence, one claim, one evidence chain.  |  一句话论证、一个核心断言、一条证据链。
- **Innovation:** name the contribution type and rung; the gap must be a scientific unknown, not a missing method.  |  写清贡献类型和层级；缺口必须是科学未知，不是"没人用我们的方法"。
- **Broad interest:** name who outside the field cares and what changes for them.  |  写清领域外谁关心、对他们改变什么。
- **Language:** concrete subjects, calibrated verbs, no hype, no defensive padding, no AI-tone clusters.  |  ** 主语具体、动词与证据匹配、不吹嘘、不防御、不堆 AI 味词。**
- **Figures:** one figure-level claim, distinct inferential roles per panel, adequate information density, journal-compliant specs.  |  一幅图一个图级断言，面板承担不同推断角色，信息密度足够，符合期刊规格。
- **Statistics:** independent unit, exact n, error definitions, tests, correction, exact P values.  |  独立单位、精确 n、误差定义、检验、校正、精确 P 值。
- **Submission:** stage-specific package, real declarations, verified limits and access routes.  |  按投稿阶段准备材料，声明真实，限制与获取途径已核实。

## Quick start  |  快速开始

1. Copy one or both skill folders into your agent's skills directory.  |  把一个或两个技能目录复制到 agent 的 skills 目录。
2. Refresh the catalog.  |  刷新技能目录。
3. Ask for the outcome, not the steps.  |  直接说你要的结果，而不用给操作步骤。

~~~bash
python tools/install.py --target ~/.agents/skills --skills both --dry-run
python tools/install.py --target ~/.agents/skills --skills both
~~~

Then try one of these:

- "Use natsci-writing. Turn these data and figures into a complete Nature Article."  |  中文："用 natsci-writing，把这些数据和图写成完整 Nature 论文。"
- "使用 natsci-writing-zh。为这个结论做一套投稿级图件，先问我用 Python 还是 R。"  |  中文："可以先问后端，再出整套投稿图。"
- "Use natsci-writing. Audit this manuscript against Nature editorial criteria before I submit."  |  中文："投稿前按 Nature 编辑标准审一遍。"

## What is inside  |  包里有什么

- **SKILL.md** — the operating manual: modes, standards, routing, release gates.  |  操作手册，含交付模式、标准和发布。
- **references/** — the depth: editorial fit, innovation, main-text discipline, statistics, language taste, figure craft, journal rules, writing diagnostics, project figure standards.  |  参考库，覆盖编辑契合、创新、正文纪律、统计、语言品味、图件技艺、期刊规则、写作诊断和项目图件规范。
- **assets/templates/** — eleven working documents: manuscript outline, figure contract, caption, response letter, data statements, terminology ledger, cover letter/submission, innovation canvas, editorial audit, reporting checklist, figure evidence map.  |  11 个工作模板，覆盖提纲、图件合同、图注、回复信、数据声明、术语表、投稿包、创新画布、编辑审核、报告检查、图件证据地图。
- **assets/code/** — tested Python and R starters that produce a three-panel figure and export SVG/PDF/600-dpi raster.  |  已测试的 Python 与 R 起步脚本，生成三联图并导出 SVG/PDF/600 dpi。
- **tools/** — validator, installer, manifest builder and CI workflow.  |  校验器、安装器、manifest 生成器和 CI。
- **docs/** — architecture, usage, migration, publishing and a bilingual coverage audit.  |  架构、使用、迁移、发布和中英双语覆盖审计。

## Repository layout  |  目录结构

~~~
NatSci-Writing-skills/
├── README.md / README.zh-CN.md
├── CHANGELOG.md / VERSION / LICENSE / NOTICE.md / AUTHORS.md / CITATION.cff
├── manifest.json
├── docs/            architecture, usage, migration, publishing, coverage audit
├── examples/        ready-to-use prompts (EN/ZH)
├── tools/           validate_package.py, install.py, build_manifest.py
├── .github/         CI validation workflow
└── skills/
    ├── natsci-writing/       SKILL.md, references/, assets/
    └── natsci-writing-zh/    same structure in Chinese
~~~

Each skill is self-contained. Keep references/ and assets/ next to SKILL.md.  |  每个技能自包含；复制时务必带上 references/ 和 assets/。

## Verify  |  校验

~~~bash
python tools/validate_package.py
python tools/validate_package.py --installed ~/.agents/skills
python tools/build_manifest.py
~~~

The validator checks frontmatter, names, versions, companion links, reference links, absolute paths, stale names, assets and package documents. It needs no third-party library.  |  校验 frontmatter、名称、版本、companion、参考链接、绝对路径、旧名称、资产和包文档；不依赖第三方库。

## Coverage and limits  |  覆盖与边界

A layer-by-layer audit against the author's standards, the latest nature-skills upstream and Nature/Science requirements is in docs/COVERAGE-AUDIT.md.  |  逐层对照作者标准、nature-skills 最新上游与 Nature/Science 要求，见覆盖审计。

What is deliberately not included: upstream field- or workflow-specific modules such as paper-to-patent, paper-to-PPT, paper reader, experiment log and downloader. Install them separately if you need them.  |  有意不包含论文转专利、转 PPT、reader、实验日志、下载器等外围技能，需要时单独安装。

Journal limits, figure specifications and reporting rules change. The package marks them "verify at submission" and expects you to check the current guide.  |  期刊限制、图件规格和报告规则会变；包内标注"投稿前核对"，请以当期指南为准。

## Version, license, provenance and citation  |  版本、许可、来源与引用

Current version: 1.2.0 (2026-11-23).  |  当前版本 1.2.0（2026-11-23）。

**License:** source-available and free for non-commercial academic, research and teaching use; you may copy, modify and redistribute with attribution. Commercial or profit-generating use is not permitted without a separate written license. See LICENSE.  |  许可：源码可用，非商业学术/科研/教学免费；可复制、修改、再分发，但需署名。未经单独书面许可，不得用于商业或盈利性用途。详见 LICENSE。

**Author and origin:** Chuanyang Liu; built from the author's own research projects and long-term conversations with AI coding agents.  |  作者与来源：Chuanyang Liu；由作者自己的科研课题和长期与 AI 编程助手的对话完整建立。

**Third-party:** integrates and adapts Nature-skills by Yuan Yizhe (袁一哲), https://github.com/Yuan1z0825/nature-skills, Apache-2.0; adapted portions retain their Apache-2.0 terms. See NOTICE.md and LICENSES/Apache-2.0.txt.  |  第三方：整合并改编袁一哲的 Nature-skills（地址同上，Apache-2.0）；改编部分保留 Apache-2.0 条款，详见 NOTICE.md 与 LICENSES/。

## Citation  |  引用

A related paper is in preparation and will be updated here when published. If you use these skills in your research, teaching or software, please cite the related paper and this repository.  |  相关论文正在准备，发表后会在此更新；如使用本 skills，请引用相关论文与本仓库。

Citation metadata is in CITATION.cff; update the GitHub URL before publishing.  |  引用元数据见 CITATION.cff；发布前请替换 GitHub 地址。

## Contributing  |  贡献

Run python tools/validate_package.py --strict, update CHANGELOG.md and manifest.json, keep relative links, and do not add paywalled full text, private project data or fabricated citations.  |  提交前跑严格校验，更新 CHANGELOG 和 manifest，保持相对链接，不加入付费全文、私有项目数据或编造引文。
