# 覆盖审计：已整合与未整合的内容

版本 1.2.0；更新日期 2026-11-23。1.2.0 增加作者、引用与许可元数据；覆盖范围不变。本文回答：此前的写作与图件要求、nature-skills 最新内容、Nature/Science 发表级要求，是否已有机整合进 NatSci-Writing-skills。

## 一、审计范围

1. 作者标准：v2.1.0 论文/图件规则、项目图件几何、颜色审计、Baker 结构图标准、SEAL 补充图规范、R50 清单、HTML/数据核验。
2. nature-skills 上游：本地仓库及 upstream main（提交 c6701db，2026-11-22），覆盖 nature-writing、nature-figure、nature-polishing、nature-statistics、nature-data、nature-reviewer、nature-response、nature-citation、nature-academic-search、nature-shared 等。
3. Nature/Science 官方要求：文章类型、编辑标准、字数/展示项/参考文献限制、统计报告、Reporting Summary、数据/代码/材料声明、图件制作合同、图像诚信。
4. NatSci 语料：868 篇 Nature/Science 记录、317 篇全文、1,504 条图注。

## 二、覆盖矩阵

| 要求层 | "完整"的含义 | 当前覆盖位置 | 状态 |
|---|---|---|---|
| 学术论证与文体 | 问题、断言、证据链、竞争解释、文体架构 | SKILL.md 第二至四节；manuscript-production-zh；章节 playbook；research-and-language | 已整合 |
| 创新性与创造性 | 贡献类型、贡献阶梯、缺口工程、区分性预测、定位 | innovation-and-broad-interest-zh（新）；SKILL.md 2.4；创新画布模板 | 1.1.0 强化 |
| 广泛受众与编辑契合 | 编辑标准、为什么是这个/现在/广泛、意义、期刊契合 | editorial-and-submission-zh（新）；SKILL.md 2.4；编辑审核模板 | 1.1.0 强化 |
| 语言与学术品味 | 节奏、声音、克制、house style、AI 味、句式库 | language-and-taste-zh（新）；writing-diagnostics-zh；revision-and-response-zh；语料证据 | 1.1.0 强化 |
| 图件与视觉质量 | 图级断言、推断角色、视觉层级、期刊规格、示意图、QA | figure-craft-and-information-density-zh（新）；figure-production-zh；figure-standards；项目叠加；Python/R 脚本 | 1.1.0 强化 |
| 信息密度 | 结果分类、正文/SI 分工、展示预算、返修膨胀、断言重复 | main-text-and-information-architecture-zh（新）；SKILL.md 4.1；图件证据地图模板 | 1.1.0 强化 |
| 统计与诚信 | 独立单位、重复、精确报告、图件统计、Reporting Summary、图像/数据/代码诚信 | statistics-and-reporting-integrity-zh（新）；SKILL.md 6.1；报告检查模板 | 1.1.0 强化 |
| 投稿与编辑流程 | 阶段门、限制、cover letter、标题页、声明、审稿人建议、就绪状态 | editorial-and-submission-zh；manuscript-production-zh 第七至十节；cover letter 模板 | 1.1.0 强化 |
| 文献、引用与数据 | 检索策略、核实、引用格式、数据/代码/材料声明 | SKILL.md 第七节；manuscript-production-zh；html-and-data-verification；声明模板 | 已整合 |
| 中英双语与中文特性 | 原生中文指导、翻译腔、证据强度对齐 | natsci-writing-zh SKILL.md；中文参考与模板 | 已整合 |
| 生产与 QA | 完整初稿、图件文件、格式、回复、校验器、安装器、manifest、CI | SKILL.md 第八至十二节；assets；tools；docs；GitHub workflow | 已整合 |

## 三、nature-skills 最新增量的整合情况

- nature-writing：首次投稿包（cover letter、标题页、highlights、声明、审稿人建议、阶段化限制）；Nature 系列与 NMI 期刊片段；正文纪律；Nature 摘要/引言/结果-讨论语料指南；修订工作流的删除检查与范围确认。
- nature-statistics（上游新技能）：独立单位与重复、Nature Article 统计要求、Reporting Summary、图件统计、常见失败模式、P0/P1/P2 审稿风险分级。
- nature-figure：多面板证据架构、Nature 正刊图件要求、矢量示意图规则、模板目录、更新后的设计与 QA。
- nature-data：Nature 正刊数据/代码/材料要求与强制存缴门。
- nature-polishing：更新的章节动作、句式库、失败模式和 Nature/NMI 风格片段。
- nature-reviewer / nature-response：技术关切分类、严重度分级、投稿包一致性审计、回复结构与语气更新，融入评审、回复与编辑审核。
- nature-shared：读者工作流、术语表、论文类型、伦理、一致性扫描、期刊格式。

## 四、有意不整合的内容

上游还有社会科学习作、论文转专利、论文转 PPT、论文 reader、paper card、paper translation、paper x-ray、引用核验器、文献流水线、实验日志、image-to-PPT、proposal writer、下载器、医学技能等。它们不是 Nature/Science 论文生产系统的核心，整合会稀释写作与图件焦点；需要时可单独安装上游技能。

## 五、已知局限

- 期刊限制与制作规则会变化；包内每个数字都标"投稿前核对"，必须对照当期指南。
- 项目专用 SEAL 内容已包含，公开前需审核（见 PUBLISHING 第六节）。
- 本包不自动从原始数据计算新统计或生成图件；它产出分析计划、报告检查、绘图代码和稿件文字，仍需作者数据与决策。
- 语料是本地分析集；只记录汇总统计，不分发全文。
- 通过本包检查不保证接收；它降低可避免的编辑、统计、风格与制作风险。

## 六、1.1.0 已执行验证

- 包与已安装副本校验通过。
- YAML frontmatter 与 companion 链接有效。
- SKILL.md 引用的参考文件全部存在；相对链接无断链。
- 无绝对路径、个人信息、密钥或旧私有名称。
- Python 与 R 图件脚本在 demo 数据上运行并导出 SVG/PDF/600 dpi 位图。
- 安装器复制两个技能；zip 解压后校验通过。
- manifest 当前；版本 1.1.0。

## 七、结论

包现已覆盖完整发表栈：论证与创新、广泛受众与编辑契合、语言与品味、图件质量与信息密度、统计与诚信、投稿与编辑流程、双语生产与 QA。剩余问题是被明确记录的局限，而不是缺失的核心层。
