# 期刊模板与稿件组装

稿件要交付两次：一次作为论证（章节、主张、证据），一次作为一份必须先通过期刊机械检查的文件。这份文件管后者：把写好的稿件装进格式正确的文档，并验证结果。**默认期刊：Nature**，第二目标是 Science。

## 〇、什么是权威

| 层 | 文件 | 作用 |
|---|---|---|
| 规格（唯一真源） | assets/journal-templates/specs/nature-article.json、science-research-article.json | 页面、字号、章节顺序、上限、参考文献风格、图幅 |
| 模板 | assets/journal-templates/generated/ 或 .../official/ | 稿件装入的 .docx |
| 组装器 | tools/build_manuscript.py | 从 markdown 或 JSON 填充模板 |
| 检查器 | tools/check_journal_format.py | 按规格验证产物 |
| 来源登记 | tools/journal_template_sources.json | 出版社官方模板地址 |

规格中每个块都带 confidence：official（出版社明文）、secondary（第三方汇总）、default（我们的保守回退）。检查器只对关键结构与排版项判失败；摘要字数、参考文献上限等报为 WARN，让刻意偏离可见而不是直接判死。

## 一、两种模板路线

出版社页面有交互式中转页，本技能因此提供两条路线：

1. **生成模板**（默认，永远可用）：tools/make_journal_template.py 按规格生成 .docx——页面、1 英寸边距、12 pt Times New Roman、双倍行距、连续行号、页码，以及每个元素一个样式（NSC Title、NSC Body、NSC Abstract、NSC Reference 等）。它是我们自己的产物，可随包分发。
2. **官方模板**（有则优先）：在浏览器里从清单页下载，再导入。

~~~bash
python tools/fetch_journal_templates.py --list
python tools/fetch_journal_templates.py --from-dir ~/Downloads
python tools/fetch_journal_templates.py --check
~~~

组装时指定官方文件，组装器会清空正文、保留其样式：

~~~bash
python tools/build_manuscript.py draft.md --journal nature \
  --template assets/journal-templates/official/nature-template.docx
~~~

不要为了让稿件好看而改导入模板的样式；改稿件或改规格，并记录原因。

## 二、Nature（默认）

| 项 | 取值 | 置信度 |
|---|---|---|
| 页面 | A4，1 英寸边距，带页码 | secondary |
| 正文 | Times New Roman 12 pt，双倍行距 2.0，左对齐，段前段后 0 | secondary |
| 标题 | Arial 14 pt 粗体 | secondary |
| 各级标题 | Arial 12 pt 粗体 | secondary |
| 图注/表格 | Arial 10 pt | secondary |
| 行号 | 连续，第 1 页到末页 | secondary |
| 摘要 | 150–200 词，不带引用，单段 | secondary |
| 参考文献 | 按首次引用编号，正文上标，上限 50（Article） | secondary |
| 显示项 | 至多 8 个；单栏 89 mm，双栏 183 mm，≥300 dpi | secondary |

**章节顺序**（不得重排）：题目 → 作者 → 单位 → 摘要 → 正文 → 参考文献 → 致谢 → 作者贡献（可选）→ 利益冲突 → 图注 → 表格（可选）→ 方法 → 数据可用性 → 代码可用性（可选）→ 扩展数据（可选）。方法放在参考文献之后而不是引言之后，这个倒置顺序是最常见的机械退稿原因。

## 三、Science（第二目标）

| 项 | 取值 | 置信度 |
|---|---|---|
| 页面 | Letter，1 英寸边距 | secondary |
| 正文 | Times New Roman 12 pt，双倍行距 | secondary |
| 摘要 | 100–125 词，不带引用 | secondary |
| 参考文献 | 编号、正文上标，上限 80，章节名为 References and Notes | secondary |
| 显示项 | 至多 7 个；55 / 121 / 183 mm，≥300 dpi | secondary |
| 图内字母 | 大写粗体 8 pt，左上角 | secondary |

**章节顺序**：题目 → 作者 → 单位 → 摘要 → 正文 → References and Notes → 致谢 → 资助（可选）→ 作者贡献 → 利益冲突 → 数据与材料可用性 → 补充材料（可选）→ 图注。

## 四、组装

输入是二级标题命名章节的 markdown，或同结构的 JSON：

~~~markdown
---
authors: 张三, 李四
affiliations: 1 示例大学分子系统研究所
---

# 承载主张的题目

## 摘要
150–200 词（Nature）或 100–125 词（Science），无引用。

## 引言
## 结果
### 残基级读出优于池化基线
## 讨论

## 参考文献
1. 作者. 题目. Nature 555, 1-9 (2018).

## 方法
## 致谢
## 作者贡献
## 利益冲突
## 数据可用性
## 图注
~~~

引言、结果、讨论都并入正文，并降为三级小标题，不会重复输出。

组装器强制：章节按规格顺序输出；[1] 式引用转为上标；重复的正文标题降级为小标题而非重复块；缺失的必需章节只报告、不编造；作者与单位来自 front matter，绝不自动生成。

~~~bash
python tools/build_manuscript.py draft.md --journal nature \
  --out build/draft-nature.docx --report build/draft-nature.json
python tools/check_journal_format.py build/draft-nature.docx --journal nature
~~~

## 五、投稿门顺序

按顺序跑，前一道不通过不进入下一道：

1. **组装**：build_manuscript.py，missing= 必须为 none，或逐条列出并说明理由。
2. **格式**：check_journal_format.py，关键项全 PASS，WARN 逐条确认。
3. **文字**：check_prose_style.py --gate（第十七节），无 ERROR、无防御性/AI 标记、无度量越界。
4. **主张与统计**：claim ledger 与报告清单，每个数字带 n、检验、校正与效应量。
5. **图件**：图件合同、panel 角色、规格中的图幅与 dpi、图注与正文一致。
6. **投稿包**：声明、reporting summary、cover letter、change log；不留下“投稿前核对”的悬置项。

六道全通过才提交。WARN 在写下理由之前不算通过。

## 六、诚实边界

- 规格值来自已公布的投稿要求，并与 2026 年的一份第三方汇总交叉核对；出版社随时会改。投稿前重新核对，改规格而不是改稿件。
- 官方 Word/LaTeX 模板由作者在浏览器中下载；本包不绕过出版社的中转页，也不重新分发出版社文件。
- LaTeX 产物是镜像规格页面与章节顺序的骨架；以 LaTeX 为主的期刊，请在 LaTeX 中组装并对 PDF 执行第五节检查。
- 检查器验证的是 .docx 能暴露的东西（页面、样式、行距、标题、计数），它无法判断论证是否正确——那由本技能第二至五节负责。
