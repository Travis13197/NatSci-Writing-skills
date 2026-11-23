# NatSci-Writing-skills 更新记录

## 1.2.2 — 2026-11-23

基于镜像世界项目的 Perspective/理论文章升级：新增 nature-perspective-production 与 mirror-world-case-study 参考；新增 Perspective 提纲、编辑范围与修改记录、概念图设计单模板；SKILL 增加编辑保真、Perspective 生产、概念图与终检条款；扩展文风检查器；更新 README/文档/manifest。

## 1.2.1 — 2026-11-23

发表系统升级：新增 AI 使用与披露政策、文献检索与引用诚信、五轮校对、Perspective/洞见写作、Nature 章节技艺参考；扩展审稿/回复与数据/代码/材料指导；新增 AI 披露、文献检索、数据/材料模板；重润色 README；整合独立 skill（insight-led-scientific-perspective、literature-review、grammar-checker、polish、writing-beats）与当前期刊 AI 政策。

## 1.2.0 — 2026-11-23

包元数据更新：作者署名为 Chuanyang Liu；来源说明为作者自己的科研课题与长期对话经验，并整合袁一哲的 Nature-skills（Apache-2.0）；新增引用元数据；许可改为源码可用、非商业条款，改编部分保留 Apache-2.0。技能内容不变。

## 1.0.0 — 2026-11-23

NatSci-Writing-skills 首个公开版本：完整、可迁移的中文 Nature/Science 论文与图件生产技能。整合作者 v2.1.0 论文/图件规范、NatSci 语料分析与 nature-skills 生产流程，含参考文件、论文/图件/图注/回复/声明模板，以及已测试的 Python/R 图件脚本。

## 2.1.0 — 2026-11-23

把作者的 v1.18.0 项目体系与 nature-skills 生产体系合并进语料校准的 v2.0.0 技能，使技能能够直接产出完整论文与整套图件，也能修订、润色和调整格式。

端到端生产：新增 manuscript-production-zh.md，覆盖交付模式、确认门、术语表、十步完整论文流水线、章节 playbook（标题、摘要含 Nature summary paragraph、引言、结果、讨论、结论、方法、相关工作）、五类论文 playbook（research、methods、algorithmic、hypothesis、review）、期刊格式表、完整稿件包（标题页、摘要、正文、方法、参考文献、图注、声明、修改记录）、Word/LaTeX/HTML 格式、数据/代码声明、引文管理和对抗性自审清单。

图件：新增 figure-production-zh.md，加入图件合同、四类页面原型、Python/R 后端门、字体/颜色/密度系统、图型选择、统计呈现、图注规范、导出与 QA；figure-standards-nature-science-zh.md 保留期刊规格。作者 1.18.0 的完整图件体系随技能打包：figure-design-and-audit.md（54 KB）、panel-layout-and-letter-placement.md、figure-colour-audit-contract.md、structural-figures-baker-standard.md、figure-r50-regression-checklist.md，并更新 html-and-data-verification.md；v2.1.0 的 SKILL.md 汇总强制发布门槛（一面板一图、固定坐标网格、0.38–0.42 面板宽间距、面板字母锚点、语义颜色审计、结构 raster 排布、遮挡审计、证据密度）。

修订与审稿：新增 revision-and-response-zh.md，覆盖先修推理的润色、修订机制、章节动作、按证据强度的句式库、风格红线、审稿回复包与动作映射、分歧语气、审稿模拟和期刊格式检查。

写作：SKILL.md 按交付模式、语料实测文体目标、写作诊断、断言校准和终检重构；description 扩展到完整论文起草、格式调整和图件生产。保留作者既有偏好（中英对照、加粗修订、引文位置、项目几何与颜色角色）。

## 2.0.0 — 2026-11-23

围绕实测的 Nature/Science 语料重建技能（868 条记录：489 篇 Perspective/Review 长文、379 篇研究论文，另有 28 篇 Nature Methods/Biotechnology 方法学论文；317 篇全文、2,320 条图注），覆盖生命科学、生物技术、蛋白质语言模型与 AI。

新增有期刊依据的文体结构：Nature 摘要（不超过 200 词、7–8 句、"Here we show"）、Science 摘要（约 125 词、6 句）、Nature 综述前言（不超过 200 词、4 个展示项、少于 7,000 词）、Nature Perspective（个人视角、前瞻、论证驱动）、Science 综述与一句提要领的 Science Perspective。新增语料实测的段落与句长目标（研究论文段落 120–140 词，综述 150–260 词，Perspective 200–320 词；句长中位数 24–27 词；限定语与连接词频率）。

新增 writing-diagnostics-zh.md：带实测密度的 AI 标记词表、七类问题及中文改写示例、逐句练习与段落修改流程。SKILL.md 新增断言校准、数字入文、连接逻辑和终检清单。

新增 figure-standards-nature-science-zh.md：Nature 官方规格（89/183 mm；8 pt 小写面板字母；5–7 pt 文字；0.25–1 pt 线宽；300–600 dpi）与 Science 规格（55/120/183 mm；大写面板字母）、按证据类型构建面板、五段式图注语法、统计呈现、可及性、导出与审核流程。figure-design-and-audit.md 升级到 v2 并与期刊标准衔接。

新增 journal-style-evidence-zh.md，记录语料构建、覆盖范围、实测统计、文体定义、范例 DOI 与局限。版本升至 2.0.0；保留作者既有偏好（中英对照、加粗修订、引文位置、项目图件几何与 Okabe–Ito 配色）。

## 1.4.0 — 2026-11-13

明确“正方面板”指内部数据坐标框的 x 轴与 y 轴视觉长度相等，比例为 0.9–1.1；整张多面板图、PNG 和 HTML 卡片不受正方形约束。

新增期刊字号层级与拥挤处理规则：关键文字通常不低于 6 pt，轴标签约 7.5–8 pt，面板字母约 9.5–10 pt；通过调整画布、网格、标题、刻度密度和相邻残基标签解决排版，不压缩字号。审核流程增加字号表、几何表、宽幅例外表和文字碰撞记录。

## 1.3.1 — 2026-11-13

将图件审核实例写入 `references/figure-design-and-audit.md`。常规数据轴采用 0.9–1.1 的近方形绘图区，Figure 4a/4e、CDS 轨道、384 孔布局和全长残基轨道按用途登记为宽幅例外。

补充 Science 常用强调色的项目角色：PA、Per-OH、S-Lim 分别使用深蓝、青绿和琥珀，LMSF 与 DAMP 报告通道使用青绿和紫红，正负模型比较方向使用蓝色和朱红。审核记录要求同时保存面板几何前后表、例外清单、文字碰撞检查、图像导出、HTML 浏览器检查及图注颜色核对。

## 1.3.0 — 2026-11-13

新增 `references/figure-design-and-audit.md`，统一论文图件的科学任务、面板比例、色彩、结构证据、统计证据、导出和审核流程。

分析面板默认采用 0.9–1.1 的近方形 box aspect。长序列、基因/操作子、时间轴、孔位图和需要保持横向对应关系的面板允许宽幅布局，并要求登记例外。

蓝色继续作为项目主识别色；新增 Science 常用 Okabe–Ito 强调色，包括青绿、琥珀、朱红和紫红。规范同时要求结构与统计面板共享残基、状态和颜色映射，关键结果保留直接标注和源数据链接。

## 1.2.0 — 2026-11-13

建立可独立使用的中文学术论文写作技能，采用自然中文学术段落组织研究构想、摘要、引言、结果、讨论、方法和图注。同步课题创新、网络调研、逐句润色、完整 HTML 修订、数据与计算核验规则。

随附完整研究与语言规范、HTML 核验规范、可复用中文提示词，以及 SEAL、维度回译和功能注释专题参考资料。根据中文论文目标选择输出语言，保留真实数据、作者决定、标准术语和证据身份。