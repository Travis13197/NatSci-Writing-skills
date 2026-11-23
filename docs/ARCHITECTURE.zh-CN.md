# 架构说明

## 一、系统模型

NatSci-Writing-skills 由两个技能组成：

- natsci-writing（英文）
- natsci-writing-zh（中文）

二者是平级技能，不是"主技能 + 翻译层"。每个技能自包含：SKILL.md、references/、assets/templates/、assets/code/ 和独立 changelog。唯一的跨技能连接是 metadata 中的 companion 字段，用于需要另一种语言的场景。

## 二、加载模型

agent 先读 SKILL.md。SKILL.md 是操作手册而非百科：

1. 说明交付模式与路由；
2. 给出不可妥协的标准（论证、证据、语言、图件）；
3. 列出参考文件及阅读时机；
4. 定义最终质量门槛。

随后只加载当前模式需要的参考文件，使普通任务保持轻量，同时保留论文、图件、修订、格式和回复所需的深度。

## 三、内容分层

| 层 | 文件 | 作用 |
|---|---|---|
| 操作手册 | SKILL.md | 模式、标准、路由、发布门槛 |
| 语料证据 | references/journal-style-evidence.md | 实测风格目标、文体定义、范例与局限 |
| 写作诊断 | references/writing-diagnostics.md | AI 味与翻译腔词表、七类问题、改写练习 |
| 编辑与创新 | references/editorial-and-submission-zh.md；innovation-and-broad-interest-zh.md | 编辑标准、期刊契合、投稿包、贡献阶梯、缺口工程、广泛兴趣 |
| 正文纪律 | references/main-text-and-information-architecture-zh.md | 结果分类、证据链、正文/SI 分工、返修控制 |
| 统计与诚信 | references/statistics-and-reporting-integrity-zh.md | 独立单位、重复、Nature 统计、Reporting Summary、图像/数据诚信 |
| 语言与品味 | references/language-and-taste-zh.md | 节奏、声音、house style、品味诊断 |
| 图件技艺 | references/figure-craft-and-information-density-zh.md | 多面板证据架构、图序、信息密度、矢量示意图 |
| Nature 章节技艺 | references/nature-section-craft-zh.md | 摘要/引言/结果/讨论动作、断言升级、审核 |
| Perspective | references/perspective-and-insight-zh.md | 智识中心、发现序列、推测、形式内容 |
| Perspective 生产 | references/nature-perspective-production-zh.md | Nature 格式、六节结构、整段正文、证据层级、概念图、编辑模式 |
| 理论文章案例 | references/mirror-world-case-study-zh.md | 镜像世界假说：六节、Box/图、数学对象、生产经验 |
| 文献与引用 | references/literature-search-and-citation-zh.md | 检索策略、来源层级、筛选、综合、引用核对 |
| AI 诚信 | references/ai-use-and-writing-integrity-zh.md | 作者禁令、披露、允许/禁止用途、期刊政策表 |
| 校对 | references/proofreading-and-polish-zh.md | 五轮校对、句子润色、概念落地/节奏、一致性 |
| 生产 | references/manuscript-production.md | 完整论文流水线、章节/论文类型 playbook、期刊格式、稿件包、声明 |
| 修订 | references/revision-and-response.md | 润色、句式库、审稿回复、审稿模拟 |
| 图件生产 | references/figure-production.md | 图件合同、原型、后端、设计系统、图型选择、QA |
| 图件标准 | references/figure-standards-nature-science.md | 期刊规格、图注语法、统计呈现 |
| 项目图件叠加 | figure-design-and-audit.md + panel-layout + colour audit + Baker standard + SEAL standard + R50 | 作者项目的几何、颜色、结构与发布门槛 |
| 课题设计 | references/research-and-language.md | 课题设计、假设、文献综合 |
| 数据与 HTML | references/html-and-data-verification.md | 全文修订、数据真实性、计算核验 |
| 专题 | seal-project.md、translation-validation.md、dimension-annotation.md | SEAL 术语、回译、注释 |
| 提示词 | references/academic-prompt-zh.md | 可复用中文任务提示词 |
| 资产 | assets/templates、assets/code | 17 个工作模板（论文、图件、cover letter、创新画布、编辑审核、报告检查、回复、声明、AI 披露、文献检索、数据/材料）与已测试的 Python/R 图件脚本 |

## 四、为什么是两个语言技能

- 中文和英文的失败模式不同（翻译腔、的-字链 vs 冠词、名词化），词表和交付规范也不同。
- 单一双语技能要么在同一文件里重复两遍，要么强制一种语言加载另一种语言的参考。
- 两个平级技能让每种语言保持原生指令，同时在中英对照任务中通过 companion 互查。

## 五、为什么 SKILL.md 保持单体而不是 fragment router

前身 nature-skills 采用 router + 多个 fragment。NatSci-Writing-skills 保留单一操作手册，因为：

- 编辑和作者需要一次读完全部标准；
- 单文件更易审计、diff 和版本化；
- 深度材料仍在 references 中，SKILL.md 只保留核心标准与路由。

## 六、资产

- 模板是 Markdown 工作文档：论文提纲与证据地图、图件合同、图注骨架、回复包、数据/代码声明、术语表。
- 代码脚本是可直接运行的 Python 与 R 起点：从 demo 数据生成三联图并导出 SVG/PDF/600 dpi 位图，内置图件合同、一面板一图规则和导出设置。用户替换为自己的 CSV 即可。

## 七、项目专用标准

SEAL 项目规范、R50 回归清单、逐 panel 交付和项目颜色契约是作者生产环境的一部分，因此打包在内，并明确标注为"项目门槛"而非普适期刊规则。其他用户可忽略或替换这些文件，不影响通用写作、生产和期刊图件层。

## 八、校验与发布

- docs/COVERAGE-AUDIT.md 记录逐层来源审计。
- tools/validate_package.py：检查结构、frontmatter、技能名、版本、companion、参考链接、绝对路径、旧名称、资产和必要文档。
- tools/build_manifest.py：生成带大小和 SHA-256 的 manifest.json。
- tools/check_prose_style.py：扫描模板对立、防御性/自限性表达和高频 AI 词。
- tools/install.py：把技能复制到目标 skills 目录并校验。
- CI 工作流 .github/workflows/validate.yml 在每次 push/PR 时校验。
- 版本遵循语义化版本；系统版本在 VERSION 与 CHANGELOG.md，技能各自也有版本和 changelog。

## 九、扩展方式

新增参考文件：

1. 放入技能的 references/；
2. 在 SKILL.md 资源列表中加入"何时阅读"；
3. 运行 python tools/validate_package.py --strict；
4. 更新 CHANGELOG.md 并运行 tools/build_manifest.py。

新增语言：

1. 复制英文技能目录；
2. 翻译 SKILL.md 与 references，保持同样的相对结构；
3. 设置 metadata 的 language 与 companion；
4. 更新 README、install.py 和校验器。

## 十、非目标

- 不自动投稿；
- 不编造数据、引文或审稿人；
- 不再分发付费全文或私有项目数据；
- 不做交互界面；产品是技能及其产物。
