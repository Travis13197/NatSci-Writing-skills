# r50 图件回归清单：结构空带、拼图拥挤与低信息密度的根因检查

版本：1.2.6.8；更新日期：2026-11-24。本清单用于作者已指出“某图看起来仍不合格”的
回归场景。既往几何 PASS、单图 aspect PASS 或整图最小值 PASS 都不能覆盖这里的检查。

## 1. 结构 panel 上方大面积空白

结构行被压成窄条、上方留白很大、同行定量 panel 明显更大时，按以下顺序定位：

1. 检查 `imshow`、`Image` 或结构图是否先被放进宽矩形，再通过 `set_box_aspect(1)`
   居中；该组合会把较小维度缩成窄条。修复必须在放置前重算 axes 宽高和 row height，
   不能用事后 aspect 设置伪装方形。
2. 测量源 raster 的非白墨迹外接框。若 whole source 外缘空白超过 5%，先只裁除完全
   空白的外缘，保留 1–2% 呼吸区；不得裁除分子、标签、比例尺或位点标记。
3. 测量 panel 内结构内容外接框。保留上下文的单一结构视图允许主要方向 ≥0.85、
   次要方向 ≥0.72；这是为了保留约 20% 的周边三级结构。四周透明 context 用约 50%
   透明度并启用白色景深，不能淡到几乎不可见。禁止拉伸结构，也禁止在同一 panel 放
   全景与局部 inset 的“一大一小”组合。
4. 每个结构 panel 与同行定量 panel 使用同一 82 mm × 82 mm 数据框或登记等效 footprint；
   等权 panel 面积差不超过 5%。结构图不是宽幅例外，除非它本身是连续残基轨道。
5. 结构 panel letter、结构标题、图像、轴说明和图例分别占位。letter 定义完整 cell
   左上空白，位于数据框左侧约 `0.20w`、高于数据框至少 `4 mm`；标题在数据框上方
   水平居中并加粗，标题顶线与 panel letter 顶线在行内统一；结构 raster 的纵横比变化后
   重新检查标题、letter 和残基标签。
6. 输出 `structure_raster_audit.tsv`：源尺寸、非白 bbox、外缘 margin、crop box、
   whole/detail/composite 内容占比、最大内部空白行带与最终 panel bbox。

Figure 3b 一类问题通常同时包含“源图宽而短”和“固定方形 cell 放置宽图”两个原因。
只修切边或只改间距都不能通过最终验收。

## 2. 同行 panel 靠得过近、上下行又留白过多

完整 panel 边界是 axes、letter、单行标题、刻度、offset text、x/y 轴标题、直接标注和
外部图例的并集。验收必须逐对同时记录：

- 横向净空 / axes 宽度；
- 纵向净空 / axes 宽度；
- 每个 panel 的完整 bbox；
- 每行 panel 数和列 left/bottom 对齐；
- 保存前后 axes 矩形是否一致。

BioNoether 目标固定为 `0.28w`，允许 `0.27–0.29w`，即相对早期 `0.40w` 缩小约 30%。横向达标不能掩盖纵向偏大；轴间距达标不能
掩盖标题或图例相碰。发现相邻 panel 视觉相碰时，扩大物理画布或统一 footer/title 带，
禁止缩小 10 pt 或 10.5 pt 的角色字号。

## 3. Fig. 5/6 一类“内容少”与视觉粗糙

先审查证据密度，再审查装饰：

1. 逐一列出每个 panel 的 source table、可恢复的个体值、区间、paired unit、matched
   null、阈值、失败状态和留出层级。
2. 每个 panel 只承担一个主要比较；相邻 panel 不得重复同一估计量，只换点形、颜色或
   图型。
3. 低行数、多字段的源表使用能承载比较方向的专门几何：paired dot/线、forest interval、
   volcano、matrix symbol、slope、calibration、threshold curve 或结构 context。
4. 高密度源表保留个体或分布，并使用分档、中位、密度或直接标注承担聚合；禁止用均值柱
   替代完整分布。
5. 每个图组至少出现两类独立证据，例如样本分布 + matched null、paired change + 阈值、
   结构 context + 定量 endpoint、holdout + uncertainty。
6. 图标、点形和轮廓只在存在对应语义时使用。装饰图标不计入证据维度。

Figure 5 的 geometry distance 与物理 operation Gram 必须保留独立 panel、独立标题、
独立源表和独立判决。Figure 6 的 overlap、slow-mode capture、memory integral、
replicate slope、hold-trajectory prediction 和 time-window transfer 是不同估计量，
不能用单一“记忆分数”或均值柱概括。

## 4. 字号、配色和语义角色

最终发布使用固定角色字号：普通文字、刻度、图例与直接标注 10 pt；轴标签 10.5 pt；
常规标题 11 pt；结构标题 11.5 pt；panel letter 12.5 pt。所有可见分析 axes 同时具有
非空 x/y 轴标题。文字统一 `#132B36`，字体统一 DejaVu Sans。需要放大才能阅读时扩大
画布或减少次要文字，禁止缩到角色字号以下。

颜色使用项目固定语义板。对象身份与证据状态分开编码：颜色承担模型、蛋白或证据来源，
点形、空心、线型、hatch、轮廓和直接标签承担条件、严重度与通过状态。结构图颜色在
统计图、正文、图注和结构增强页保持一致。未注册颜色、禁用色图和矩阵格内文字均阻断发布。

## 5. 结构增强页最低验收

每个结构原图之后提供一个独立 `结构增强版：Cartoon + Cylinder` 链接。增强页至少包含：

- 原图不变；
- 每个结构实体一个方形画布；
- Cartoon 与 Cylinder 两个独立按钮；
- 同一 Cα 坐标、固定正交相机、缩放、残基编号和关键位点；
- Cartoon 来自 PyMOL `cartoon_fancy_helices=1` 或同类真实 molecular viewer；
- Cylinder 来自 PyMOL `cartoon_cylindrical_helices=1` 或 3D viewer 的真实 helix run；
- 可选 8 Å network，并明确 cutoff；
- 源结构 SHA、DSSP 赋值、相机、半径、端盖、高光、线条和导出哈希。

增强页按结构实体分组，桌面至少两列；53 个报告图位以紧凑 anchor 或折叠小图组列出。
同一结构只显示一组 Cartoon/Cylinder 主图。固定宽度手绘 helix、正弦偏移线、椭圆端帽
和手工 β 带均阻断发布。细长结构先优化 camera 和裁切；局部视图在命中位点两侧保留
至少 6 个残基。

桌面 1440 px、移动 390 px 与 320 px 都要满足无横向溢出、console error 为 0、
控制高度至少 44 px。切换表示前后，对结构 canvas 截图并计算哈希；哈希必须不同。

## 6. 发布顺序

1. 重建每个 panel；
2. 检查单一数据轴、角色字号、轴标题和证据密度；
3. 检查 panel 内文字—文字与文字—数据遮挡；
4. 按最终 HTML CSS 宽复算有效字号，拒绝仅靠页面放大可读的 raster；
5. 重建固定物理 canvas 并逐对测量完整视觉边界，记录列 cell 宽与长标签扩展；
6. 检查最终 raster 内容占空率与内部空白带；
7. 检查每个 panel 的证据编码，拒绝重复均值和单一估计量的镜像 panel；
8. 检查语义色和矩阵符号编码；
9. 在完整 HTML 中核对全部图像加载；
10. 在桌面与窄屏浏览器检查图片、公式、宽表和交互；
11. 保存所有哈希并把当前 skill 版本写入图件审计。

浏览器检查必须展开全部 `<details>` 并走完整个页面。lazy image 的图像卡片要有
`aspect-ratio` 和最小高度；全部声明图像达到 `complete && naturalWidth > 0` 后才算
加载完成。多面板完整图允许最大内部全白行列带 `0.18`，单结构 raster 仍为 `0.14`。

以上任一环节失败，回到对应 panel 的真实布局或证据组织修复。颜色、字重和边距的局部
美化不能替代结构空带、证据不足或拼图错误的根因修复。

## 7. v1.2.6.3 逐 panel 回归样例

- line/scatter legend 压住点或线：转为不超过四系列的 short direct label；整组在 axes fraction 中保持间距；超过四系列改标题带或右侧列。
- 分类刻度相互重叠：先改写为一个词，再按 rendered bbox 均匀保留 2–4 个并显式设置 ticks；不得重新出现，也不得导致 x/y 轴标题消失。
- panel letter 与顶部 y 刻度相撞：根据顶部 tick 的完整 bbox 动态抬高 header，不能隐藏刻度。
- 数据贴近坐标上限：检查差值/恢复量是否更合适；保留原估计量时加入约 10% 上侧余量。
- forest 无显著性：将 adjusted q 放在 axes 外独立列；没有真实检验的 bar/violin/box 不画括号。
- 分布叠加：点 alpha 约 0.50、violin 约 0.28、box 约 0.38，避免结构互相覆盖。
- 每个图完成后逐 panel 检查图层顺序、图例是否在预留空间、轴标题是否存在、显著性与比较是否一一对应。

## 8. v1.2.6.4 星号—图例全量回归

- 每张统计图只出现 `****/***/**/*/n.s.`，图内没有 `q=` 或 `p=` 文本。
- 连续效应图同时有同点 CI 带；一个连续显著区段标首、中、末，状态变化和末点保留。
- 森林图外置星号列逐行对齐，不覆盖点与区间。
- 图例优先标题下水平多列；宽度能放进完整 axes 时不得出现在右侧。
- 顶部 legend、标题和 letter 从下到上依次分离，最终缩放后重新测量。
- 代表性版式逐图回归，任何重复星号碰撞或右侧多余图例均重新绘制。

## 9. v1.2.6.6 投影范围与结构可见度

- PCA/t-SNE/UMAP 使用当前完整数据范围，x/y 等长跨度、等单位、方形数据框，越界点数为 0。
- 旧的极端自动刻度或上一轮 limits 必须删除；刻度显式设置。
- 折叠证据使用 cartoon/ribbon；非重点结构为灰色 20% 透明度（约 80% 可见）。
- 结构标签占用独立标签带，不压分子墨迹。
- HTML 图件按图位置截图，不能只用 naturalWidth 判定可见。
