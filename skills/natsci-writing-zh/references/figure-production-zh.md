# 图件生产：从论断到投稿级成图

版本 1.2.6.8；更新日期 2026-11-24。与 figure-standards-nature-science-zh.md（期刊规格、图注语法、统计呈现）和 figure-design-and-audit.md（作者项目的几何、颜色与发布门槛）配合使用。本文件整合 nature-skills 图件体系与语料证据，给出端到端流程。

## 一、图件合同（写代码之前）

先在笔记中写九行：
~~~
核心结论：一句带动词的话，例如"模型通过保守维度 12 区分留出家族"。
图件原型：定量网格 / 示意主导拼图 / 图像板+定量 / 非对称混合模态。
期刊与输出：目标期刊、栏宽、最终尺寸、格式。
后端：Python 或 R（阻塞项，见第三节）。
面板地图：a、b、c……每个面板回答的问题。
证据层级：hero 证据、验证、对照/稳健性。
统计：n、中心、离散度、检验、校正。
源数据：每个定量面板对应的文件与连接键。
审稿风险：审稿人最可能挑战的两三件事。
~~~

规则：
- 结论是关系不是主题（"处理通过恢复 Z 使 Y 下降"，不是"处理结果"）。
- 每个面板回答独立问题；删掉它不削弱论证就删除或合并。
- 主证据与支撑证据分开；hero 面板获得最清晰坐标轴和最大面积，对照视觉更安静。
- 有数据但无论断时，先提出暂定论断并确认，再定样式。
- 数据不支持的面板删除，不用装饰填充或编造。

## 二、原型与面板逻辑

| 原型 | 适用 | hero 面板 | 支撑面板 |
|---|---|---|---|
| 定量网格 | 论断主要是数值比较 | 汇总指标或森林图 | 共享坐标、对齐尺度、紧凑图例 |
| 示意主导拼图 | 流程、机制或设计需先读懂 | 示意图占 35–60% 面积 | 2–4 个定量验证面板 |
| 图像板+定量 | 显微、组织、成像、印迹主导 | 图像板或代表性图像 | 比例尺、叠加、裁剪、配对定量 |
| 非对称混合模态 | 示意、位图与统计图并存 | 一个面板跨行/列 | 按证据价值排序的小面板 |

默认阅读顺序：体系与设计 → 主要比较 → 机制/定位 → 代表性观察的量化 → 稳健性/对照/独立验证。Fig. 1 的首个面板定义整图（以及全文）复用的视觉词汇：颜色、符号、流程方向、样本类别与尺度。

面板数量纪律：完整行三个分析面板；五面板用 3+2 居中；六面板 3×2；项目完整拼图默认九个分析面板 3×3；独立的证据轨道（如序列轨道）可置于上方，不计入分析网格。7/8/10/11 混合行不得发布；精确几何按项目规范执行。

## 三、后端门：Python 或 R

用户未明确选择后端、也未提供语言特定文件时，只问一句"Python 还是 R？"然后停止。不默认、不猜测、不先生成示意图。选定后，该后端独占绘图、预览、导出和视觉 QA。选定运行时缺失时停止并报告阻塞，提供该后端脚本与安装命令，不换另一种语言替代。

- Python：matplotlib、seaborn、subplot_mosaic/GridSpec、pandas/numpy/statsmodels、matplotlib.imshow/skimage/tifffile；导出 SVG（svg.fonttype='none'）、PDF（pdf.fonttype=42）、TIFF 600 dpi。
- R：ggplot2、patchwork、ComplexHeatmap/circlize、ggrepel、survival/survminer、Seurat/ggtree；导出 svglite、cairo_pdf、ragg::agg_tiff。
- 混合流程仅允许非可视的数据准备；最终拼装与所有视觉输出使用选定后端。

## 四、设计系统

**字体。** Arial/Helvetica（回退 DejaVu Sans），全图一致；SVG/PDF 文字可编辑；仅在渲染器支持时使用数学字体。期刊印刷字号 5–7 pt；作者 HTML/项目叠加使用较大角色（10 pt 正文、10.5 pt 轴标签、11 pt 粗体面板标题、11.5 pt 结构标题、12.5 pt 面板字母），同一交付物中不得混用。不得为缓解拥挤把字号压到发布下限以下；应扩大画布、稀疏刻度、缩短标签或把精确数值移入图注/源表。

嵌入 3×3 HTML 综合图的结构 raster 标签使用最终显示大小计算，目标 5–7 pt；1600 px
结构画布以 48–56 px source label 为起始值，并在最终截图复核。结构标题仍为 11.5 pt，
panel letter 为 12.5 pt。残基标签过大会遮住侧链和 Cartoon，不得用正文 10 pt 的规则
机械放大 raster 标签。

**坐标与边框。** 只保留左、下边框；上/右边框关闭；图例无框；默认无网格。每个分析面板（含矩阵和类别面板）都必须有轴标题；自动定位器产生超出数据范围的刻度时手动设定范围。

**颜色。** 每图一个中性族、一个信号族、一个强调族。语义稳定优先于色相多样：同一对象/方法/状态在面板、图和正文中保持同一颜色；通过填充、形状、网纹、线型或直接标签编码证据状态，不通过重新着色对象。使用色盲友好色（Okabe–Ito 作为色相来源）；定性面板最多三种彩色类别，超过则加形状/线型/直接标签；连续量用单调色阶；双向偏离用砖红—中性—深蓝发散色阶。禁用 jet/rainbow/hsv、装饰性循环和低于 4.5:1 的文字对比；矩阵单元不写文字，支持信息用标记或轮廓编码；项目语义色板（navy #0D5673、secondary #4E8EAD、teal #16786F、ochre #C77A24、brick #B8453E、plum #6C5079、neutral #586B75、text #132B36）在 figure-design-and-audit.md 和 figure-colour-audit-contract.md 中定义。

**密度。** 每个面板需要一个数据驱动的视觉锚点、主次分明的标记层级、可见的不确定性或参考线，以及足以回答一个问题的证据。有区间、对照、重复测量、匹配零模型或样本级观察时，拒绝裸坐标框、孤立均值柱、单点和无阈值曲线。密集散点用透明度/密度保留个体；森林图显示区间、支持和分母；矩阵补充不确定性或支持几何；稀疏方案展示相对命名基线的变化。

## 五、图型选择

- 方法比较：横向柱按效应排序，带不确定性；n 小时叠加个体点；直接标注；避免 3D 柱和冗余网格。
- 时间/剂量趋势：线图加不确定性带；相关面板共享一行图例；基线用参考线；连续序列不用柱状图。
- 组间分布：箱线/小提琴加散点；写 n 与中心；不把双峰藏在均值±s.e.m. 柱后。
- 关系：相关性是断言时用散点加边际分布；第三个变量用大小编码时必须有清晰图例；解释依赖象限时加参考线。
- 组成：堆叠柱显示绝对份额；配 z-score 偏离热图说明"哪里异常"，再配散点说明共变；不用两种图型重复同一切片。
- 热图：列间尺度不同时按列标准化；缺失用白色；不写单元文字；记录聚类顺序；色标标注统计量。
- 雷达/极坐标：只在多基准剖面且每轴独立标准化时使用；自定义辐条和圆环，无默认网格，图例在外。
- 成像：灰度背景 + 1–2 个荧光通道；黑色仅用于图像板内部；裁剪、比例尺和视野框一致。
- 结构：全景定位、局部展示机制；几何断言需要两个正交视图；结构与配对定量使用相同残基/状态颜色；Baker 结构规范见 structural-figures-baker-standard.md。

## 六、统计呈现与图注

- 写 n 及 n 计数的是什么（细胞、蛋白质、供者、独立实验）；小 n 展示个体点。
- 定义中心与离散度（mean ± s.d./s.e.m.、median+IQR、95% CI）；不写未定义的"误差棒"。
- 写检验、单双侧、校正族和确切比较；报告效应量与不确定性，不只 P。
- 模型图：训练/验证/测试划分、随机种子/折数、指标定义、基线、变异来源；各面板指标定义保持一致。
- 图像：独立实验次数、代表性图像选择标准、比例尺长度、通道映射、亮度/对比度调整（全局或局部）、原始文件来源。
- 图注骨架："图 N |" 粗体名词短语标题 → 现在时逐面板说明 → 统计 → 符号 → 源数据/许可行。Nature 风格不超过 300 词；数字属于面板和统计，不写进标题行。不照抄他人图注措辞。

## 七、导出与 QA

- 按最终尺寸用毫米设计（Nature 89/183 mm；Science 55/120/183 mm），为标题、刻度、标签和图例带预留边距。
- 线条图用 SVG/PDF 且文字可编辑；位图 300–600 dpi；RGB；嵌入字体；保持纵横比。
- 在 100% 印刷尺寸、灰度和色盲模拟下检查；对所有 artist 类型（散点、线集合、区间、柱、身份线）检查文字—文字、文字—画布、文字—数据遮挡，不只检查点。
- 位图面板检查外边界内容范围和内部空白带；只裁剪完全空白的外边距；保持分子纵横比；结构面板内容范围不低于 85%。
- 记录发布文件：面板几何、间距、逐轴字号、颜色角色、遮挡结果、源数据映射、导出检查。项目审计文件与阈值见 figure-design-and-audit.md、panel-layout-and-letter-placement.md、figure-colour-audit-contract.md、figure-r50-regression-checklist.md。
- 保存后不得压缩设计间距；保存的成图必须是审核过的版式。旧的 PASS 不能证明新的渲染；每次重新测量当前文件。

### 7A. 最终 HTML 有效字号与固定 canvas

Matplotlib 的 10 pt 是源 raster 的点值，不是页面显示值。浏览器把 6,500–9,700 px 的三列图压到约 1,384 px 时，原本 10 pt 的标签只剩约 2–7 pt；即使原图 validator 全部通过，读者仍然无法读图。每张 HTML 图必须记录：

- raster 宽、宽高和保存 dpi；
- 最终内容列和图像 CSS 宽；
- 每类文字角色的有效 CSS pt：`raw_pt × save_dpi / 72 × css_width / raster_width ÷ (96 / 72)`；
- 有效字号是否达到 10 pt、轴标题是否达到 10.5 pt。

三列综合图先固定一个物理 canvas family：72 mm 数据框、28.8 mm 完整 cell 净空、14.4 mm 标题与字母带，并为 y 标签留出独立外侧带。不要先生成任意 `figsize`，再对旧网格追加 `set_box_aspect(1)` 或用 `tight_layout` 压实。`bbox_inches="tight"` 不得在审计后改变 gutter；保存后只允许裁掉完全空白的外边距。

长 y 刻度先缩写，再按固定宽度换行；完整 estimand、单位和比较方向放在轴标题、图注与源表。禁止用 `set_label_coords(-0.55, 0.5)` 或 `set_label_coords(1.55, 0.5)` 把标签推进 gutter。所有图输出 `effective_font_size_audit.tsv`、`column_cell_width_audit.tsv` 和 `panel_role_audit.tsv`。

## 八、与正文的衔接

- 正文解释科学，图注盘点面板。每个图组之后，结果正文说明发现了什么、哪个比较建立规律、解释止于何处。
- 图号、面板字母、图例、正文引用和源数据链接保持一致；任何面板变更后全部更新。
- 多个结果分支时，建立分支索引（估计量、分母、阈值、失败条件）。
- 源数据不能公开时，说明可公开什么（汇总统计、元数据、合成数据）及原因；不暗示不存在的可用性。

## 八B、SEAL 与逐 panel 交付

SEAL 图件必须完整阅读 seal-supplementary-figure-standard.md。每个已声明 panel 是独立可编辑 SVG，自带面板字母、轴标签、刻度、标记与注释；拼图必须可由 panel 导出复现。交付合成 SVG、矢量 PDF、600 dpi PNG/JPG、每 panel 一份 SVG、共享图例/比例尺 SVG、图注、panel 定义记录与审核记录。自动遮挡检查只是筛查；必须在最终尺寸下逐图逐 panel 目检并记录缺陷与修复。标签栈与引导线、行列带宽以及 8/10/10/0.4 pt 发布门槛见该规范。

## 九、最小模板

Python（matplotlib）：
~~~python
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "svg.fonttype": "none", "pdf.fonttype": 42,
    "axes.spines.right": False, "axes.spines.top": False,
    "legend.frameon": False, "font.size": 7,
})
fig, axes = plt.subplots(1, 3, figsize=(183/25.4, 60/25.4), constrained_layout=True)
fig.savefig("fig1.svg"); fig.savefig("fig1.pdf"); fig.savefig("fig1.tiff", dpi=600)
~~~

R（ggplot2 + patchwork）：
~~~r
library(ggplot2); library(patchwork)
p <- ggplot(df, aes(x = method, y = value, colour = family)) +
  geom_point(position = position_jitter(width = 0.12), size = 1.2) +
  stat_summary(fun = median, geom = "crossbar", width = 0.5) +
  theme_classic(base_size = 7, base_family = "Arial") +
  theme(legend.position = "top")
svglite::svglite("fig1.svg", width = 183/25.4, height = 60/25.4); print(p); dev.off()
~~~

模板只是起点；决定面板的是合同、原型和证据逻辑，不是模板。

## 十一、AI 生成与 AI 辅助图件

选工具前先判断图件类型。数据图（显微、凝胶、印迹、成像、光谱、定量图、结构）用真实数据和代码生成；生成式图像模型不得创建或修改数据图。概念示意图、图形摘要和封面按目标期刊 AI 图像政策处理；许多期刊要求编辑许可和披露。AI 辅助排版或字体可以使用，实质协助需披露，最终矢量要核对。

禁用生成式填充、移除物体、合成显微、凭空增加细节的 AI 放大、假比例尺或编造分子结构。保留溯源记录：工具/版本/后端、日期、完整 prompt、seed/参数、输出哈希、人工修改、源数据/代码和核验人。期刊允许时在 Methods、图注和 cover letter 披露。读 ai-figures-and-visual-integrity-zh.md；用 assets/templates/ai-image-provenance-record.md 记录。

## 十二、v1.2.6.3 图例与刻度实现顺序

先完成数据绘制，再移除未定位图例并决定三种布局：不超过四个短系列且有真实右侧空白
时使用 axes-fraction 直接标签；空间不足时在图题下横排；仍不足时放入右侧独立列。
直接标签整组一起平移，保证最小间距；不得在轴框边缘逐标签裁剪。图例、直接标签和
系列文本在最终发布前统一执行数据遮挡检测。

轴标题在碰撞处理前登记为不可删除对象。数值轴设 4–6 个主要刻度；类别轴标签缩短后，
从原 tick positions 中按 rendered bbox 均匀选择 2–4 个，再调用显式 `set_xticks` 或
`set_yticks`。这样刻度不会在下一次 draw 中重新出现。每个轴至少保留两个刻度；轴标题
继续保持可见并增加 label padding。

panel 标题和字母在最终 axes 尺寸已知后重放。锚点高度取顶部 y 刻度文字上界、文字高度
和至少 4 mm 净空的最大值。数据范围在最终 autoscale 后加入 headroom；保存前再次执行
文字—文字、文字—数据、图例—数据和画布边界审计，并同时写出
`axis_tick_completeness` 与 `legend_data_occlusions`。

## 十三、v1.2.6.4 星号与水平图例实现

统计字符串先经统一函数转成 `****/***/**/*/n.s.`，图中不再拼接 q 文本。效应曲线增加
同点 95% CI 带；同一连续显著区段用首、中、末代表点标星，状态变化处和末点始终保留。
森林图的外置显著性列使用同一星号映射。

fig.legend 的布局顺序固定为：标题下水平多列 → axes 端点直接标签 → 右侧单列。顶部图例
使用 `lower center` 放在数据框上缘，标记 `_cellauto_legend_mode="header"`；标题和
panel letter 的动态锚点读取该 legend 的 y1，再整体上移。`target_reached`、`complete`、
`timeout`、`blocked` 的转移缩写为 `C/T/B→C/T/B`。可放上方的图例占右侧列、图内出现
`q=` 文本或相邻星号碰撞，均阻止发布。

## 十四、v1.2.6.6 投影和结构 cartoon 实现

投影面板先计算 `span=1.06 × max(x_range,y_range)`，以各自数据中心设置相同跨度的 x/y
limits，启用等比例坐标并固定方形数据框，再显式设置刻度。保存前逐点断言所有点均在
limits 内，输出越界点数必须为 0。

结构 cartoon 渲染前从原子名重写元素列并保留电荷列为空，记录源文件和修正文件哈希；
检查 guide atom 数为 Cα 数。PyMOL/ChimeraX 中由真实坐标生成 rounded-ribbon cartoon，
非重点链、loop 和上下文使用灰色 20% 透明度（约 80% 可见），焦点折叠不透明。标签带
与分子墨迹分离。

## 十五、v1.2.6.7 密度实现配方

分布 panel 采用分层画法：violin 透明度约 0.18、box 约 0.35、抖动个体点 alpha 约 0.55、
点大小 3–5，中位数/CI 用文字色标记。散点 panel 加回归线与 bootstrap 带，或 hexbin 并在
图注给出边际摘要。剂量–响应 panel 画估计值与 CI 带，同时保留个体终点 rug。禁止使用默认
黑色箱线须线；whiskerprops、capprops、medianprops 必须使用已注册颜色。导出前逐 panel
审计证据层数与未注册颜色。

## 十六、v1.2.6.8 范围实现配方

用统一 helper 计算范围：pad = 0.04 × (max − min) 或 0.02 × |value|；xlim = (min − pad,
max + pad)；必须保持 0/100 的百分比轴不加边距。分布 panel 要包含 violin/KDE 体，而不只是
观测点；对数轴在对数空间加边距。设置范围后显式设置刻度。导出前运行全 panel 范围审计，
任何 panel 出现越界点或相对越界 >0.5% 即判定构建失败。

