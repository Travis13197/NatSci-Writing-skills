# NatSci-Writing-skills  |  面向 Nature/Science 的论文写作与作图系统

**作者：Chuanyang Liu**  
**引用：相关论文正在准备并会更新；使用本 skills 请引用论文与本仓库。**

你手里有数据、图件和一个结论。稿子还需要能过审的论证、放在正确位置的证据、能承担论证的图、符合目标期刊的格式，以及经得起追问的审稿回复。这个包把这些工作组织成一套面向 Nature/Science 的生产系统，覆盖生命科学、生物技术、生物信息学和 AI-for-science。

它面向完整交付物：整篇论文、整套图件、完整 Perspective、返修包，或者可直接投稿的文件。

## 适合谁

写新稿、重搭旧稿、准备图件、写 Nature 风格 Perspective、返修，或把草稿变成可投稿文件时使用。科学、数据和判断由你提供，包提供结构、检查和成稿流程。

它面向生命科学、生物技术、生物信息学和 AI-for-science 的研究组，也面向需要完整草稿、并希望保留推理过程的作者。

## 你会得到什么

中英文各一个自包含技能。每个技能都带操作手册、参考库、工作模板和已测试的 Python/R 绘图脚本。

所有内容都在文件夹里：参考、模板和脚本放在本地，链接使用相对路径，离线即可运行。复制文件夹、加载 SKILL.md 就能用。

| 技能 | 语言 | 版本 | 目录 | 说明 |
|---|---|---|---|---|
| natsci-writing | English | 1.2.5 | skills/natsci-writing/ | 英文写作与作图 |
| natsci-writing-zh | 中文 | 1.2.5 | skills/natsci-writing-zh/ | 中文写作与作图 |

## 能做什么

### 起草

- **写完整论文**：一次交付整篇，含标题、摘要、引言、结果、讨论、方法、参考文献、图注、声明和补充材料清单。
- **做整套投稿图**：从一句结论出发，先定图件合同和面板地图，再出投稿级样式、统计呈现、SVG/PDF/600 dpi 文件和图注。
- **完成整篇 Nature Perspective**：六节结构、证据台账、整段正文、关键句加粗、三幅概念图加一个 Box、中英双语，以及符合期刊模板的完整稿件。
- **写理论或假说文章**：把概念主张写成定义、可检验关系、图件和边界段。

### 审查

- **判断编辑契合度**：投稿前检查原创性、重要性、跨领域兴趣、技术可靠性和可读性，再回答为什么做这个、为什么现在做、为什么领域外也关心。
- **检查统计与诚信**：检查独立实验单位、重复、精确 n 和 P、Reporting Summary、图像诚信、数据/代码/材料声明。
- **控制信息量**：决定什么进正文、图注和补充材料；返修时控制篇幅，让信息更集中。
- **系统检索和引用**：写检索计划，按 PRISMA 式流程筛选，逐条核对文献，管理 RIS/BibTeX/Zotero。
- **审查 AI 写作与 AI 图件**：投稿前检查 AI 披露、图像溯源、合成图像禁令、许可和 AI 负面清单。

### 修改与投稿

- **改稿润色**：先修论证，再修语言；去掉 AI 腔和翻译腔；中英对照标出改动。
- **按作者原文编辑**：轻度润色、作者忠实扩写、翻译或修订模式；保留断言顺序和措辞，标出改动，源文件保持不动。
- **按期刊排版**：按 Nature、Science、Nature Communications 的结构、参考文献、声明、公式和行号排版，科学内容保持原样。
- **回复审稿**：逐条回复、意见跟踪表、动作映射、语气控制和修改清单。
- **合规使用 AI**：按期刊要求披露，检查禁止用途，核实 AI 提到的文献和数字，清掉 AI 腔。

## 它和普通写作提示有什么不同

- **论证先行**：每个任务先定主张、证据链和图级结论，再动句子。
- **证据台账**：每条断言标明状态，例如已确立、定义性、模型依赖、假说或前瞻实验。
- **整段正文**：正文用连贯段落，列表留在论证之外，洞见用单句加粗。
- **文风检查器**：扫描模板对立、防御性表达和高频 AI 词，CI 会检查 README。
- **AI 负面清单**：文字、引文、数据和图像都有明确禁用项，终检查行为，不只查语气。
- **作者保真**：轻度润色保留断言顺序和措辞；修订模式在副本上操作，源文件不动。

## 背后的做法

顶刊稿子常见三类问题：论证单薄、证据放错位置、文字和图让忙碌的读者看不出重点。

流程设四道关口：动笔前查创新和编辑契合；写作中管正文纪律和证据链；投稿前查统计、报告诚信和图件；返修时做逐点回复和断言校准。

每道关口都有具体产出：创新画布、断言表、图件合同、报告检查表或回复跟踪表。每一步都让下一个决定变得可见。

## AI 使用底线

AI 可以辅助语言编辑、结构梳理、文献初筛、格式处理、写代码和调图件布局。署名作者必须是人，每条结论、引文、数字、图像和许可由作者负责。

未发表、机密、审稿中的材料和患者数据留在受控环境。数据、研究图像、参考文献、统计和批件都由作者核实。AI 推荐的文献逐条核对。

目标期刊要求披露时，写清工具、任务、涉及章节和核验过程。

完整政策表、2026 更新、AI 写作负面清单和审计见 references/ai-use-and-writing-integrity-zh.md；记录模板见 assets/templates/ai-disclosure.md。政策会变，投稿前按目标期刊核对。

AI 辅助图件走独立政策。数据图用真实数据和代码；概念示意图、图形摘要和封面需要期刊许可、披露、人工核验和溯源记录。生成式填充、合成研究图像、假比例尺和未披露的 AI 封面都不允许。

图件政策、溯源和负面清单见 references/ai-figures-and-visual-integrity-zh.md；模板见 ai-image-provenance-record.md 和 ai-negative-checklist.md。

## 快速开始

1. 把一个或两个技能目录复制到 agent 的 skills 目录，references/ 和 assets/ 一起带上。
2. 刷新技能目录。
3. 直接说结果，例如"写完整论文""做整套投稿图"。

~~~bash
python tools/install.py --target ~/.agents/skills --skills both --dry-run
python tools/install.py --target ~/.agents/skills --skills both
~~~

可以这样开口：

- "使用 natsci-writing-zh。把这些数据和图写成完整 Nature 论文，缺什么列出来。"
- "使用 natsci-writing-zh。为这个结论做一套投稿级图件，先问我用 Python 还是 R。"
- "使用 natsci-writing-zh。把这份设计文档写成完整 Nature Perspective，带图和一个 Box。"
- "Use natsci-writing. Verify every citation and the AI disclosure before I submit."

## 包里有什么

- **SKILL.md**：操作手册，写清交付模式、标准、路由和发布门槛。
- **references/**：31 个英文、32 个中文参考文件，覆盖编辑契合、创新、正文纪律、统计、语言品味、AI 诚信、文献与引用、校对、Nature 章节写法、Perspective 生产、镜像世界案例、AI 图件政策与溯源、图件技艺、期刊规则、写作诊断和项目图件规范。
- **assets/templates/**：19 个工作模板，覆盖论文提纲、图件合同、图注、回复信、数据声明、术语表、投稿包、创新画布、编辑审核、报告检查、图件证据地图、AI 披露、文献检索计划、数据/代码/材料检查、Perspective 提纲、编辑范围与修改记录、概念图设计单、AI 图像溯源记录、AI 使用负面清单。
- **assets/code/**：已测试的 Python 和 R 脚本，能画三联图并导出 SVG/PDF/600 dpi 图。
- **tools/**：校验器、文风检查器、安装器、manifest 生成器和 CI。
- **docs/**：架构、使用、迁移、发布和覆盖审计，包含已整合与未整合清单。

## 目录结构

~~~
NatSci-Writing-skills/
├── README.md / README.zh-CN.md
├── CHANGELOG.md / VERSION / LICENSE / NOTICE.md / AUTHORS.md / CITATION.cff
├── manifest.json
├── docs/            architecture, usage, migration, publishing, coverage audit
├── examples/        ready-to-use prompts (EN/ZH)
├── tools/           validate_package.py, check_prose_style.py, install.py, build_manifest.py
├── .github/         CI validation workflow
└── skills/
    ├── natsci-writing/       SKILL.md, references/, assets/
    └── natsci-writing-zh/    same structure in Chinese
~~~

每个技能自包含；复制时带上 references/ 和 assets/。

## 校验

~~~bash
python tools/validate_package.py
python tools/check_prose_style.py README.md README.zh-CN.md
python tools/validate_package.py --installed ~/.agents/skills
python tools/build_manifest.py
~~~

校验器检查 frontmatter、名称、版本、companion、参考链接、绝对路径、旧名称、资产和包文档；只用 Python 标准库。文风检查器扫描模板对立、防御性表达和高频 AI 词。

## 覆盖与边界

逐层对照作者标准、nature-skills 最新上游（提交 c6701db）、Nature/Science 要求、期刊 AI 政策和独立写作 skill，结果在 docs/COVERAGE-AUDIT.zh-CN.md。

论文转专利、转 PPT、reader、实验日志、下载器这类外围模块单独安装，写作和图件主线保持集中。

期刊限制、图件规格、报告规则和 AI 政策会变；包内标了"投稿前核对"，以当期指南为准。

## 版本、许可、来源与引用

当前版本：**1.2.5**（2026-11-24），版本记录见 CHANGELOG.md。

**许可**：源码可用，非商业的学术、科研和教学用途免费；可以复制、修改、再分发，需要署名。商业或盈利性用途需要单独书面许可，详见 LICENSE。

**作者与来源**：Chuanyang Liu；系统由作者自己的科研课题和长期与 AI 编程助手的对话建立。

**第三方**：整合并改编袁一哲（Yuan Yizhe）的 Nature-skills（https://github.com/Yuan1z0825/nature-skills，Apache-2.0）；改编部分保留 Apache-2.0 条款，详见 NOTICE.md 和 LICENSES/Apache-2.0.txt。

## 引用

相关论文正在准备，发表后会更新；如果这些 skills 帮到了你的研究、教学或软件，请引用相关论文和本仓库。

引用元数据在 CITATION.cff；发布前换成实际 GitHub 地址，论文有 DOI 后补入。

## 贡献

提交前跑 python tools/validate_package.py --strict 和 python tools/check_prose_style.py，更新 CHANGELOG.md 和 manifest.json，保持相对链接，只加入公开数据和已核实引文。
