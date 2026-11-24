# 覆盖审计：已整合与未整合的内容

版本 1.2.5；更新日期 2026-11-24。本文回答：作者此前的写作/图件要求、nature-skills 最新内容、当前期刊 AI 政策与独立写作 skill，是否已有机整合进 NatSci-Writing-skills。

## 一、审计范围

1. 作者标准：v2.1.0 论文/图件规则、项目图件几何、颜色审计、Baker 结构图标准、SEAL 补充图规范、R50 清单、HTML/数据核验。
2. 已发布仓库：the published GitHub working copy（v1.2.0）；其 README 已同步为基线并在 1.2.1 重润色；1.2.2 增加镜像世界 Perspective 项目经验。
3. nature-skills 上游：main 最新提交 c6701db（2026-11-22）；审计模块：nature-writing、nature-figure、nature-polishing、nature-statistics、nature-data、nature-reviewer、nature-response、nature-shared、nature-academic-search、nature-citation。
4. 独立 skill：insight-led-scientific-perspective、literature-review、grammar-checker、polish、writing-beats、nature-reader。
5. 期刊 AI 政策：Nature Portfolio、Science/AAAS、ICMJE、COPE、Elsevier、Springer Nature（截至 2026-11；投稿前核对当期政策）。
6. NatSci 语料：868 篇 Nature/Science 记录、317 篇全文、1,504 条图注。
7. 镜像世界项目：design.md/design-ref1–4、最终中英 Perspective、修订/审读记录、图件 prompt、完整作者对话与前期写作 skill 评估。可复用经验见 nature-perspective-production-zh.md 与 mirror-world-case-study-zh.md。
8. AI 写作与图像政策来源：Nature Portfolio、Nature Methods（2026）、Nature Materials（2026）、Nature Geoscience、Science/AAAS 封面图政策、Elsevier（2026 年 6 月）、Cell Press、Springer Nature、PLOS、ICMJE（2026）、COPE，以及 2026 年 arXiv AI 图件调查。汇总规则见 ai-use-and-writing-integrity-zh.md 与 ai-figures-and-visual-integrity-zh.md。
7. AI 文风来源：Wikipedia Signs of AI writing、AI Smells 指南、中文 zh-cues、意得辑 AIGC 风格词、中国社科院"AI 味"分析；汇总的零容忍句式表见 writing-diagnostics-zh.md 第 3A 节。

## 二、覆盖矩阵

| 要求层 | 当前覆盖位置 | 状态 |
|---|---|---|
| 学术论证与文体 | SKILL 第二至五节；manuscript-production；nature-section-craft；research-and-language | 已整合 |
| 创新与创造性 | innovation-and-broad-interest；SKILL 2.4；创新画布 | 已整合 |
| 广泛受众与编辑契合 | editorial-and-submission；SKILL 2.4；编辑审核模板 | 已整合 |
| 语言与学术品味 | language-and-taste；writing-diagnostics；proofreading-and-polish | 1.2.1 强化 |
| Perspective 生产 | nature-perspective-production；mirror-world-case-study；SKILL 4.4；Perspective 提纲 | 1.2.2 新增 |
| 编辑保真 | SKILL 3.3；editing-scope-and-change-log；案例 | 1.2.2 新增 |
| 概念图与理论文章封装 | nature-perspective-production 第 7 节；conceptual-figure-brief；SKILL 9.7 | 1.2.2 新增 |
| 项目经验 | mirror-world-case-study；生产文件第 12 节；writing-diagnostics 3A | 1.2.2 新增 |
| AI 写作负面清单 | ai-use-and-writing-integrity 第 10–15 节；SKILL 3.1/10/11；ai-negative-checklist | 1.2.5 新增 |
| AI 图件政策与溯源 | ai-figures-and-visual-integrity；SKILL 9.0；ai-image-provenance-record | 1.2.5 新增 |
| AI 图像版权与可复现 | ai-figures-and-visual-integrity 第 6/9 节；图件参考 | 1.2.5 新增 |
| Perspective 与概念写作 | perspective-and-insight；SKILL 4.3；manuscript-production | 1.2.1 强化 |
| Nature 章节技艺 | nature-section-craft；SKILL 4.2；journal-style-evidence | 1.2.1 强化 |
| 图件与视觉质量 | figure-craft-and-information-density；figure-production；figure-standards；项目叠加 | 已整合 |
| 信息密度与正文纪律 | main-text-and-information-architecture；SKILL 4.1；图件证据地图 | 已整合 |
| 统计与诚信 | statistics-and-reporting-integrity；Reporting Summary；图像诚信 | 已整合 |
| 文献检索与引用 | literature-search-and-citation；SKILL 6.2；文献检索计划模板 | 1.2.1 强化 |
| AI 使用与披露 | ai-use-and-writing-integrity；SKILL 3.1；AI 披露模板 | 1.2.1 新增 |
| 文风诚信 | writing-diagnostics 3A；SKILL 3.0；tools/check_prose_style.py | 1.2.1 强化 |
| 校对与润色 | proofreading-and-polish；SKILL 3.2；grammar-checker/polish 整合 | 1.2.1 强化 |
| 审稿与回复 | revision-and-response（新增分类/严重度/取证一致性）；manuscript-production | 1.2.1 强化 |
| 数据、代码与材料 | statistics-and-reporting-integrity（新增存缴/FAIR/RRID）；数据/材料模板 | 1.2.1 强化 |
| 投稿与编辑流程 | editorial-and-submission；manuscript-production；cover letter/投稿包模板 | 已整合 |
| 中英双语与中文特性 | natsci-writing-zh SKILL 与参考 | 已整合 |
| 生产与 QA | tools、docs、examples、CI、manifest、zip | 已整合 |

## 三、nature-skills 模块映射

| 上游模块 | 整合到 | 状态 |
|---|---|---|
| nature-writing | manuscript-production；nature-section-craft；editorial-and-submission；期刊格式 | 已整合 |
| nature-figure | figure-production；figure-craft-and-information-density；figure standards；项目叠加 | 已整合（规则；上游审计脚本未打包） |
| nature-polishing | language-and-taste；proofreading-and-polish；revision-and-response | 已整合 |
| nature-statistics | statistics-and-reporting-integrity；报告模板 | 已整合 |
| nature-data | statistics-and-reporting-integrity（数据/代码/材料）；数据声明模板 | 已整合 |
| nature-reviewer | revision-and-response（审稿侧审计/分类/严重度）；编辑审核 | 已整合 |
| nature-response | revision-and-response；回复信模板；包一致性 | 已整合 |
| nature-shared | manuscript-production；nature-section-craft；术语表；正文纪律 | 已整合 |
| nature-academic-search | literature-search-and-citation；文献检索计划 | 已整合 |
| nature-citation | literature-search-and-citation；引用核实/管理 | 已整合 |
| 外围模块（专利、PPT、reader、paper card、translation、x-ray、引用核验器、文献流水线、实验日志、image-to-PPT、proposal writer、下载器、医学） | 有意不整合 | 范围外 |

## 四、独立 skill 映射

| Skill | 有用内容 | 整合到 |
|---|---|---|
| insight-led-scientific-perspective | 智识中心、发现序列、问责、形式内容 | perspective-and-insight |
| literature-review | 系统检索、PRISMA 式筛选、提取、质量评估、综合 | literature-search-and-citation |
| grammar-checker | 五轮校对与问题日志 | proofreading-and-polish |
| polish | 句级清晰度/声音/时态/缩写/简洁规则 | proofreading-and-polish；language-and-taste |
| writing-beats | 概念落地、段落节奏、结尾落在"beat"上 | proofreading-and-polish；language-and-taste |
| nature-reader | 来源锚定的阅读与验证纪律 | literature-search-and-citation（阅读/核实） |

## 五、AI 政策来源

比较 Nature Portfolio、Science/AAAS、ICMJE、COPE、Elsevier、Springer Nature。共同底线：AI 不能作作者；作者负责；实质使用按要求披露；机密稿件与审稿材料不得上传公共模型；AI 生成研究图像不能作为数据。详细政策表与披露模板见 ai-use-and-writing-integrity-zh.md。政策会变，投稿前核对目标期刊。

## 六、有意不整合

上游领域/工作流专用模块（专利、PPT、reader/card、翻译、paper x-ray、引用核验器、文献流水线、实验日志、image-to-PPT、proposal writer、下载器、医学）不整合；它们不是 Nature/Science 论文生产核心。需要时单独安装。

## 七、已知局限

- 期刊限制、图件规格、报告规则与 AI 政策会变；包内每个数字都标"投稿前核对"。
- 本包不自动从原始数据计算新统计或生成图件；它产出分析计划、报告检查、绘图代码和稿件文字，仍需作者数据与决策。
- 上游图件审计脚本（Python/R）未打包；规则已整合，项目模板提供检查表。
- 语料是本地分析集；只记录汇总统计，不分发全文。
- 通过检查不保证接收；它降低可避免的编辑、统计、风格、诚信与制作风险。

## 八、1.2.5 已执行验证

- 包与已安装副本校验通过。
- YAML frontmatter、作者元数据、companion 链接有效。
- SKILL.md 引用的参考文件全部存在；相对链接无断链。
- 无绝对路径、个人信息、密钥或旧私有名称。
- Python 与 R 图件脚本运行并导出 SVG/PDF/600 dpi。
- 安装器复制两个技能；zip 解压后校验通过。
- manifest 当前；版本 1.2.5。

## 九、结论

包现已覆盖完整发表栈：论证与创新、广泛受众与编辑契合、语言与品味、Perspective 与章节技艺、图件质量与信息密度、统计与诚信、文献/引用、AI 使用诚信、校对、审稿回复、数据/代码/材料、投稿与 QA。剩余问题是被明确记录的局限，而不是缺失的核心层。
