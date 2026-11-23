# r50 图件回归清单：结构空带、拼图拥挤与低信息密度的根因检查

版本：1.18.0；更新日期：2026-11-22。本清单用于作者已指出“某图看起来仍不合格”的
回归场景。既往几何 PASS、单图 aspect PASS 或整图最小值 PASS 都不能覆盖这里的检查。

## 1. 结构 panel 上方大面积空白

结构行被压成窄条、上方留白很大、同行定量 panel 明显更大时，按以下顺序定位：

1. 检查 `imshow`、`Image` 或结构图是否先被放进宽矩形，再通过 `set_box_aspect(1)`
   居中；该组合会把较小维度缩成窄条。修复必须在放置前重算 axes 宽高和 row height，
   不能用事后 aspect 设置伪装方形。
2. 测量源 raster 的非白墨迹外接框。若 whole source 外缘空白超过 5%，先只裁除完全
   空白的外缘，保留 1–2% 呼吸区；不得裁除分子、标签、比例尺或位点标记。
3. 测量 panel 内结构内容外接框。whole、detail 与 composite 在宽、高方向的内容占比
   均应达到约 0.85 以上。一个维度的占比偏低时，重选相机、调整 zoom、改变 detail
   布局或重新组合 context 与 inset，禁止拉伸结构。
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

目标固定为 `0.40w`，允许 `0.38–0.42w`，即相邻面板各自保留约 `0.20w` 空白。横向达标不能掩盖纵向偏大；轴间距达标不能
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
和手工 β 带均阻断发布。细长结构无法在方形内达到 0.85 内容占空率时，增加同
representation 的正交 inset。

桌面 1440 px、移动 390 px 与 320 px 都要满足无横向溢出、console error 为 0、
控制高度至少 44 px。切换表示前后，对结构 canvas 截图并计算哈希；哈希必须不同。

## 6. 发布顺序

1. 重建每个 panel；
2. 检查单一数据轴、角色字号、轴标题和证据密度；
3. 检查 panel 内文字—文字与文字—数据遮挡；
4. 重建整图并逐对测量完整视觉边界；
5. 检查最终 raster 内容占空率与内部空白带；
6. 检查语义色和矩阵符号编码；
7. 在完整 HTML 中核对 14/14 图加载；
8. 在桌面与窄屏浏览器检查图片、公式、宽表和交互；
9. 保存所有哈希并把当前 skill 版本写入图件审计。

以上任一环节失败，回到对应 panel 的真实布局或证据组织修复。颜色、字重和边距的局部
美化不能替代结构空带、证据不足或拼图错误的根因修复。
