# NatSci-Writing-skills

> 面向 Nature/Science 级论文与图件的完整、可迁移生产体系。
> A complete, portable production system for Nature/Science-level manuscripts and figures.

**作者：Chuanyang Liu**  
**引用：相关论文正在准备并会更新；使用本 skills 请引用论文与本仓库。**

NatSci-Writing-skills 包含两个自包含的 agent skill（一英文、一中文），把科研项目从想法和数据推进到可投稿的完整稿件与整套图件。

## 它从哪里来

这不是通用提示词合集。整套规则、章节 playbook、图件合同、统计检查和修订流程，来自作者自己的科研课题、长期与 AI 编程助手的对话，以及真实稿件、图件、审稿和返修。

同时整合并改编了**袁一哲（Yuan Yizhe）**的开源项目 **Nature-skills**（https://github.com/Yuan1z0825/nature-skills，Apache-2.0），署名保留在 NOTICE.md 与 LICENSES/。

| 技能 | 语言 | 版本 | 目录 |
|---|---|---|---|
| natsci-writing | English | 1.2.0 | skills/natsci-writing/ |
| natsci-writing-zh | 中文 | 1.2.0 | skills/natsci-writing-zh/ |

每个技能自带 SKILL.md、参考文件、模板和图件起步代码，不含绝对路径、不依赖网络，运行时不需要外部语料库。

## 为什么需要它

顶刊写作不是词汇问题，而是论证问题、证据问题和生产问题。NatSci-Writing-skills 同时编码这三层：

- **论证结构**：来自 868 篇 Nature/Science 记录（317 篇全文、1,504 条图注）的实测统计。
- **证据纪律**：论断、证据、边界、统计与图内文字按期刊标准校准。
- **生产流程**：完整论文流水线、章节/论文类型 playbook、期刊格式、图件合同、Python/R 后端、图注语法、发布审核与审稿回复包。
- **项目级图件规范**：几何、间距、颜色层级、结构图标准、逐 panel SVG 交付与发布门槛。

## 能做什么

- 写出**完整论文**：标题、摘要（含 Nature summary paragraph）、引言、结果、讨论、结论、方法、参考文献、图注、声明、补充材料清单、修改记录；中英文皆可。
- 从论断和数据产出**整套图件**：图件合同、面板地图、投稿级样式、统计呈现、SVG/PDF/600 dpi 导出与审核记录。
- **修订润色**：先修推理再修文字，诊断 AI 味与翻译腔，中英对照加粗修订。
- **格式调整**：Nature、Science、Nature Communications 的结构、参考文献、Word/LaTeX/HTML、公式、行号和声明。
- **审稿回复**：逐点回复信、意见跟踪表、动作映射、语气控制、修改清单。
- **投稿前评审**：三份审稿报告加综合意见。
- **编辑契合评估**：原创性、重要性、跨学科兴趣、技术可靠性与可读性，附"为什么是这个/现在/广泛"测试和 cover letter/投稿包。
- **统计与诚信审计**：独立单位、重复、精确报告、Reporting Summary、图件统计、图像诚信和数据/代码/材料声明。
- **信息密度控制**：结果分类、正文与 Extended Data/SI 分工、展示预算、返修膨胀控制和断言重复审计。

## 仓库结构

~~~
NatSci-Writing-skills/
├── README.md                 英文说明
├── README.zh-CN.md           中文说明
├── CHANGELOG.md              版本记录
├── VERSION                   当前系统版本
├── LICENSE                   非商业许可（NatSci Non-Commercial License）
├── NOTICE.md                 来源与署名
├── AUTHORS.md                作者与致谢
├── CITATION.cff              引用元数据
├── manifest.json             文件清单与校验和
├── docs/
│   ├── ARCHITECTURE.md       技能设计与扩展
│   ├── ARCHITECTURE.zh-CN.md
│   ├── USAGE.md              工作流与提示词模式
│   ├── USAGE.zh-CN.md
│   ├── MIGRATION.md          迁移到其他 agent 包
│   ├── MIGRATION.zh-CN.md
│   ├── PUBLISHING.md         GitHub 发布清单
│   ├── COVERAGE-AUDIT.md     覆盖审计：已整合、未整合与局限
│   └── COVERAGE-AUDIT.zh-CN.md
├── examples/
│   ├── prompts-en.md
│   └── prompts-zh.md
├── tools/
│   ├── validate_package.py   结构、元数据与链接校验
│   ├── install.py            安装到目标 skills 目录
│   └── build_manifest.py     重建 manifest.json
└── skills/
    ├── natsci-writing/
    │   ├── SKILL.md
    │   ├── CHANGELOG.md
    │   ├── references/       规则、证据、诊断、生产指南
    │   └── assets/
    │       ├── templates/    论文、图件、图注、回复、声明模板
    │       └── code/         Python 与 R 图件起步脚本
    └── natsci-writing-zh/
        └── ... 结构相同，内容为中文
~~~

## 快速开始

1. 把一个或两个技能目录复制到目标 agent 包的 skills 目录（见 docs/MIGRATION.zh-CN.md）。
2. 刷新 agent 的技能目录。
3. 直接描述目标，而不是步骤，例如：
   - "使用 natsci-writing-zh。把这些数据和图写成完整的中文 Nature 风格论文，并给出图注和缺失输入清单。"
   - "Use natsci-writing. Turn these data and figures into a complete Nature Article."
   - "使用 natsci-writing-zh。为这个结论做一套投稿级图件，先问我用 Python 还是 R。"
4. 技能只加载当前模式需要的参考文件，返回完整成果、假设与缺失输入。

## 安装

~~~bash
python tools/install.py --target ~/.agents/skills --skills both --dry-run
python tools/install.py --target ~/.agents/skills --skills both
~~~

也支持手动复制；每个 SKILL.md 必须与 references/、assets/ 一起保留。

## 校验

~~~bash
python tools/validate_package.py
python tools/validate_package.py --installed ~/.agents/skills
python tools/build_manifest.py
~~~

校验 frontmatter、技能名、版本、companion、参考链接、绝对路径、旧名称、必要资产和包文档；不依赖第三方库。

## 覆盖审计

逐层对照作者标准、nature-skills 最新上游与 Nature/Science 要求，说明已整合、有意不整合与剩余局限，见 [docs/COVERAGE-AUDIT.zh-CN.md](docs/COVERAGE-AUDIT.zh-CN.md)。

## 设计原则

1. **一手来源优先**：规则追溯到期刊官方指南、实测 Nature/Science 语料或作者确认的项目规范。
2. **证据先于文字**：先查论断、证据和边界，再改措辞。
3. **显式规则**：每条规则说明理由和发布检验。
4. **输出优先**：每个模式都返回可直接使用的成果。
5. **可迁移**：只用相对链接；Python/R 仅用于图件代码；无隐藏运行时依赖。

## 质量基础

- 868 篇 Nature/Science 记录，覆盖生命科学、生物技术、蛋白质语言模型与 AI；317 篇全文；1,504 条图注。
- 摘要、句长、段长、限定语、连接词、数字密度与图注的实测目标。
- Nature 与 Science 的图件规格，以及作者项目的几何、颜色与发布契约。
- research、methods、algorithmic、hypothesis、review 五类论文 playbook。

## 版本

当前版本：**1.2.0**（2026-11-23）。见 CHANGELOG.md。

## 许可、来源与引用

**作者：** Chuanyang Liu。系统由作者自己的科研课题和长期与 AI 编程助手的对话完整建立。

**许可：** 源码可用，非商业学术、科研、教学免费；可复制、修改和再分发，但需署名。未经单独书面许可，不得用于商业或盈利性用途；详见 LICENSE。

**第三方：** 整合并改编袁一哲（Yuan Yizhe）的 Nature-skills（https://github.com/Yuan1z0825/nature-skills，Apache-2.0）；改编部分保留 Apache-2.0 条款，详见 NOTICE.md 与 LICENSES/Apache-2.0.txt。

**引用：** 相关论文正在准备，发表后会在此更新；如使用本 skills，请引用相关论文与本仓库。引用元数据见 CITATION.cff（发布前替换 GitHub 地址）。

## 贡献

欢迎 issue 和 pull request。提交前运行 python tools/validate_package.py --strict，更新 CHANGELOG.md 和 manifest.json；保持相对链接，不加入付费全文或私有项目数据。
