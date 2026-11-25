# David Baker 式结构图规范

版本：1.2.6.8；更新：2026-11-24。

## 1. 证据基础

本规范由 10 篇 David Baker 组原始论文的 12 张代表性结构图归纳，完整记录见
`B:/2026_Exploration/writing/structural-figure-research-2026-11-14/BAKER_STRUCTURAL_FIGURE_EVIDENCE.md`。
论文覆盖 RFdiffusion、ProteinMPNN、SARS-CoV-2 minibinder、target-structure binder、Neo-2/15、
de novo luciferase、protein biosensor、orthogonal heterodimer、60-subunit dodecahedron
和 RNA-encapsulating nucleocapsid。

这些图共同采用一套清楚的视觉语法：整体几何先建立方位，结构比较使用固定的 design/prediction/experiment
颜色，界面近景保留 parent context，侧链和配体只在承担机制证据时显示。

## 2. 每张结构图只回答一个问题

作图前先写四行：

1. 这张图的结构对象是什么：单体、二聚体、完整复合物、装配体还是晶格。
2. 读者先看什么：配体、A–B 界面、DNA 界面、对称轴还是状态转换。
3. 近景从哪里放大：用同色框、引导线或 parent panel 标示边界。
4. 哪 3–6 个残基承担解释作用：只标这些残基，其余进入图注或源表。

图题不写“结构概览”，写可验证的结构关系，例如“VA 口袋与 A–B 界面位于不同耦合层”或
“r210 保持双链 HTH–DNA 接触，r230 形成单头接触”。

## 3. 面板层级

### 3.1 整体 → 比较 → 近景 → 定量

推荐顺序：

- **整体结构**：整体复合物、partner 数、对称轴和结合位置。
- **结构比较**：design vs prediction、design vs experiment、apo vs holo。
- **界面近景**：只显示界面附近的 cartoon/surface、核心侧链与配体。
- **定量对账**：接触、距离、界面面积、氢键、盐桥、响应量或置信度。

整体图不能省。界面近景不能脱离整体。定量面板必须复用整体图中的状态名、残基编号和颜色。

### 3.2 正交视图

对称二聚体、寡聚体、核衣壳和晶格至少使用 side/top 或 front/back 两个正交视图。正交视图使用
orthographic projection，不改变透视、缩放或光源强度。需要比较的构象保持同一相机。

## 4. 颜色系统

### 4.1 默认层级

| 角色 | 推荐颜色 | 用法 |
|---|---|---|
| 中性背景 | `#CAD7DC`, `#B7C1C7`, `#586B75` | 非焦点链、支架、partner surface |
| 主结构蓝 | `#0D5673` | 设计对象、query 链、关键界面 |
| 次结构蓝 | `#4E8EAD` | 同一复合物的第二链、DNA/RNA 背景 |
| 青绿 | `#16786F` | 近景界面侧链、确认性实验 |
| 琥珀 | `#C77A24` | 功能位点、第二比较状态 |
| 砖红 | `#B8453E` | ligand、催化中心、强差异状态 |
| 灰紫 | `#6C5079` | prediction / orthogonal validation |
| 中性灰 | `#586B75` | design model、未聚焦区域、注释线 |
| 正文/注释 | `#132B36` | 标签、注释线和 panel letter |

单面板通常只保留一个主色、一个比较色和一个中性色。颜色不能装饰性地轮流分配。
同一项目和所有统计 panel 使用该语义色表；结构图不得保留旧版高饱和色板。三个
功能位点需要区分时优先使用琥珀、青绿和砖红，同时保留残基文字标签。

### 4.2 同源链

同源 A/B 链优先使用同一蓝色或灰色的明度差：

- Chain A: `#0D5673`
- Chain B: `#8DBED5`
- Context: `#CAD7DC`

不要默认用红/绿表示同源二聚体。红/绿留给明确的正/负或 active/inactive 比较。

### 4.3 设计、预测与实验

同一图组固定以下语义：

- design model: 中性灰或银灰；
- prediction: 蓝色或浅蓝；
- experimental structure: 青绿、紫红或橙色；
- ligand/active center: 红或琥珀；
- targeted patch: 低透明浅黄或浅绿 surface。

叠加图中最少使用两条结构线框。design 与 prediction/experiment 需要可区分但不形成彩虹。

## 5. Camera、光照与渲染

### 5.1 相机

- 使用 orthographic projection。
- 整体图优先沿最高对称轴观察；二聚体选择能同时看见两个 DNA-binding domain 的轴。
- 界面近景旋转到界面法线方向，避免从侧边观察导致一侧被遮挡。
- 同一图组的 comparison 使用同一 camera matrix 和 zoom。
- 不使用夸张 perspective、鱼眼或自动漫游。
- `specular <= 0.10`，关闭 cast shadow，使用 ambient + one key light；避免塑料高光。

### 5.2 光照

- 白背景；轻量 ambient + one key light。
- flat cartoon；关闭或弱化 cast shadows。
- PNG/PDF 不产生高光塑料感。
- surface 使用低透明或 flat shading；不用强 specular。

### 5.3 渲染风格

- protein overall: flat cartoon；
- target/assembly: surface 或 surface + cartoon；
- ligand pocket: transparent cartoon/surface + sticks；
- interface: ribbon context + selected side-chain sticks；
- nucleic acid: flat cartoon with reduced opacity unless it is the focal object；
- solvent/ions: 只在解释配位或静电时显示。

## 6. Ligand pocket

1. 先给整体复合物或 domain context。
2. 放大配体 8–12 Å 范围。
3. 配体使用 ball-and-stick 或 sticks；C 用高对比色，N/O/S 按 heteroatom 颜色。
4. 口袋侧链只保留 3–6 个真正接触残基。
5. 周围 protein 用半透明 cartoon/surface，不遮挡配体。
6. 标出 ligand 与残基名称；如画相互作用，只画有距离或几何依据的 H-bond/salt bridge/π contact。
7. 图注给出 cutoff、配体 ID、构象身份和关键距离/接触数。
8. 不使用“整块蛋白质 sticks”代替口袋图。

## 7. Protein–protein interface

1. 整体图先说明 A/B 链和 assembly axis。
2. 界面近景保留两侧各一小段 secondary structure。
3. 背景链用浅灰或浅蓝透明；核心残基用主蓝/青绿。
4. 同源二聚体不要给两侧不同色相，改用明度差。
5. 侧链 sticks 必须在界面平面内，避免相互重叠。
6. 界面残基标签外移，使用 leader line；近景不超过 6 个标签。
7. 以 contact count、BSA、H-bond、salt bridge 或能量作为并行定量证据。

## 8. Protein–DNA/RNA interface

1. DNA/RNA 使用浅蓝或浅灰表达 scaffold，不要让每个碱基随机换色。
2. HTH/DBD 以蓝或青绿显示；关键碱基/磷酸接触用 sticks 或 spheres。
3. 对于同源二聚体，先给 whole-complex view；再用 side-by-side 比较“双头接触/单头接触”。
4. 不能仅展示一条链接触而省略另一条链是否仍在复合物中；需要把另一条链的 A–B 保留状态画出。
5. operator DNA 的正下方朝向保持一致；同一图组统一 5′→3′方向。
6. 图示接触与定量 contact/cutoff 必须对应。不要用一帧代表性结构替代整个系综分布。

## 9. 寡聚体、装配体与晶格

1. 使用 monomer → interface → oligomer → assembly 的层级。
2. 单体与装配体用同一色相族；亚基之间用明度变化。
3. 对称轴可用细线/中心标记，不加装饰。
4. 实验 EM/cryo-EM 与 design model 叠加时，design 用灰，实验用单一彩色。
5. 整体装配图旁放粒子尺寸、stoichiometry 或质量证据。
6. 对 60-subunit/icosahedral 结构，先展示 whole shell，再展示 asymmetric unit 和关键 interface。

## 10. 标注

- 残基标注格式统一：`R97`、`E210`、`VA`。
- 残基标签与侧链之间使用短 leader line，优先放在空白区。
- 同一面板不超过 3–6 个直接标签；其余进入图注/补充表。
- 标签不得压住 atom、配体、密度、界面或坐标轴。
- 结构 raster 中的残基标签按最终 HTML 显示大小计算有效字号，目标为 5–7 pt；不要在
  1600 px 结构画布上机械使用正文的 10 pt 规则。项目当前用 52 px source label，约为上一版
  60 px 的 87%，并在最终页面宽度下复核有效字号。轴标签仍为 10.5 pt，panel letter 为
  12.5 pt。
- panel letter 固定在左上角，但不覆盖刻度、标题或结构。
- 颜色语义写入图注，不能只依赖颜色。

## 11. 定量结构与统计的组合

结构图旁至少放一项可量化证据：

- ligand–residue distance；
- interface BSA；
- H-bond / salt bridge count；
- model-vs-experiment RMSD；
- contact frequency；
- response/energy effect。

定量面板沿用结构图的状态名与残基编号。均值、区间、样本量和 cutoff 明确写出。

## 12. 版式与交付

- 每个常规分析面板内部坐标框接近正方形（0.9–1.1）；结构 image panel 按原始 aspect。
- 结构图组可以使用宽幅，但只用于 hierarchy、whole assembly 或 side-by-side comparison。
- PNG 至少 300 dpi，正式投稿优先 600 dpi。
- 同时保存 PDF、SVG 和可编辑结构会话（PyMOL `.pse` 或 ChimeraX `.cxs`）。
- SVG 保留文字为 text；结构 raster 若嵌入 SVG，必须另存原始结构会话和源 PDB/CIF。
- 所有颜色、camera、clip plane、label offsets、source PDB/CIF 和 export command 写入脚本。

## 12A. 留白与 raster 紧凑排布

结构图的上下大片空白通常由两个独立问题叠加：渲染器在较小的分子周围输出完整 camera 画布；制图程序又按源画布而不是按分子对象范围分配行高。两者必须同时修正。

1. 分别测量整图与近景中非白色分子墨迹的外接框，裁掉源图外缘并保留约 2-4% 的一致边距，避免截断标签或 sticks。
2. 等权结构比较使用方形 axes。主结构 panel 只保留一个分子对象。整体视图外围保留可见
   上下文；候选区域可另设独立局部视图，局部窗口在命中残基两侧各保留至少 6 个残基，
   比只显示口袋的裁切宽约 20%。不得因为分子细长就把 panel 做成 2:1 或 3:1 横向窄条。
   禁止非等比拉伸，也不要用装饰边框填充无效区域。
3. 按 `width_fraction x (figure_width / figure_height) / (image_width / image_height)` 计算结构 axes 高度。使用等比例图像时，draw 后检查 axes 边界；若它移出目标行，优先排查纵横比取倒数或固定布局冲突。
4. 不同纵横比的结构图按上沿对齐；下一行从最深内容边界加一个小间距开始。结构行与统计行之间的 gutter 小于 14% 空白带发布上限。
5. 保存源墨迹框、裁切框、合成图、最终 axes 和导出 raster 的测量结果。保留上下文的
   单一结构视图允许主要方向 ≥0.85、次要方向 ≥0.72，并登记为 context-preserving
   exception；分子仍应清晰占据画面，禁止用装饰边框填充无效区域。导出图最大内部空白
   行带不得超过图高 14%。
6. 结构排布完成后重新审计面板字母和标题边界。使用相对整页、而非相对图像 axes 的标题定位时，代码中看似可见的文字可能在 tight export 后被裁切或与图像分离。
7. 比较方形结构 panel 与相邻定量 panel 的最终 footprint、视觉面积和 gutter。与等权数据 panel 并排的结构 band 即使自身 raster 空白很低，只要视觉面积明显偏小，仍判失败。
7. 单独保存 `STRUCTURE_RENDER.json`，记录源 PDB/CIF 及 SHA-256、主体色、位点色、
   camera、lighting 参数、原始墨迹框、裁切框、最终内容宽高占比、PNG/PDF/SVG 和
   `.pse/.cxs` 哈希。该文件用于证明结构图与统计 panel 使用同一色板和同一结构身份。

8. 结构 panel 的名义 axes 为方形仍可能显示为窄结构带。必须测量 panel 内部整体
   raster 的内容外接框，确认 parent view、近景 inset、边框和标签共同覆盖方形空间；
   任一方向形成单薄窄条，或内容视觉面积明显小于相邻定量 panel，均拒绝发布。
9. 结构 panel letter 与标题分开创建。letter 固定为 12.5 pt，标题至少 11.5 pt；
   `a  7IE0 · V47` 这种合并 11 pt 标题不能作为 panel letter。最终 SVG 中必须能
   看到两个独立文字对象，并在 PNG 中测量各自未越界、未碰撞。
10. 三结构 panel 与三定量 panel 组成 3×2 网格时，使用同一最终方形边长和同一列
    x 坐标；行间真实 axes gutter 要容纳上行轴标题/刻度与下行标题，通常约 0.075–
    0.12 画布高度。不得把上行结构紧贴下行标题，也不得为拉开距离制造超过 0.14
    图高的内部空白带。
11. 拼接后的完整 panel 边界包含结构 raster、panel letter、结构标题、轴标签、刻度和
    外部图例。BioNoether 相邻完整边界的横向与纵向净空统一为 panel 数据框宽度的
    `0.27–0.29`，默认 `0.28`，即相对早期 `0.40w` 缩小约 30%。结构标题在数据框上方水平居中并加粗，
    letter 位于完整 cell 左上空白。结构 band 自身 content extent 合格不能替代该项。最终刻度稀疏化后
    重新测量，并冻结布局；保存阶段不得再次执行整体重排。

## 13. 发布前结构图核查

- [ ] 整体复合物是否能一眼看出 partner 数、对称关系和 DNA/ligand 位置？
- [ ] 近景是否能回到整图定位？
- [ ] 主色是否只表达一个科学角色？
- [ ] 结构主体、位点、配体和统计 panel 是否使用同一语义色？
- [ ] 是否避免高饱和多链彩虹配色和旧版色板残留？
- [ ] 同源链是否使用同色系明度差？
- [ ] design/prediction/experiment 的颜色是否稳定？
- [ ] ligand 是否没有被 helix/surface 遮挡？
- [ ] 核心侧链是否突出，非核心侧链是否隐藏？
- [ ] 氨基酸标签是否没有重叠、越界或压住原子？
- [ ] 图内接触方向是否与定量面板和图注一致？
- [ ] comparison 是否共用 camera / zoom / cutoff？
- [ ] 是否输出单独 SVG、PDF、600 dpi PNG 和 `.pse/.cxs`？
- [ ] 是否有完整源数据表和结构文件名？
- [ ] 整图与近景是否按分子墨迹裁切、按对象范围紧凑并排且未拉伸？
- [ ] 最终导出图是否通过内容占空率与最大空白行带阈值？
- [ ] 结构 panel 是否与相邻等权 panel 保持相同方形 footprint 和视觉权重？
- [ ] 非重点结构是否采用约 20% ChimeraX 透明度（约 80% 可见），并启用从 0.75 开始的轻微景深提示？
- [ ] 局部视图是否保留命中残基两侧足够的二级/三级结构上下文，并比口袋裁切宽约 20%？
- [ ] 残基标签在最终网页尺寸中是否约为 5–7 pt，且没有压过结构或标题？

## 14. 高频结构配色错误

- 默认把每条链染成不同高饱和色；多链对象应使用同色系明度或中性上下文。
- 三个位点分别使用蓝、紫、粉且饱和度不一致，打印后重要性难以判断。
- 配体、位点 sticks、统计 panel 对同一实体使用不同颜色。
- 结构 PNG 已裁切，但 `.pse` 仍是旧配色或旧 camera，无法编辑复现。
- 使用高 specular 和阴影制造“3D 效果”，损失平面印刷可读性。
- 先按未经裁切的 PyMOL 画布分配行高，再发现结构周围有大片白区。
- 只输出 PNG，没有源 PDB、SHA、结构会话和 render record。
- 重新绘制统计图后未重渲染结构图，造成同一论文两套色板。
- 只测量结构 axes 之间的间距，未把 12.5 pt panel letter、11.5 pt 换行标题、刻度和
  外部图例计入完整边界。

任何一项不满足，结构图不进入最终投稿版本。

## 15. 交互结构视图

交互结构图沿用整体、比较、近景和定量证据的层级，并在 Canvas 或 SVG 中保持固定
相机、缩放、光照与残基编号。作为背景的蛋白质主链使用浅色二级结构，配体、DNA
支架和当前残基网络使用清楚的前后层级。残基网络边、端点和当前选中位点保持深色；
位移箭头使用独立的红色并附 Å 长度。网络密度较高时，用边宽、透明度和持续/新增/
消失状态表达时间关系，减少装饰性节点。

多结构域蛋白采用同一明度层级的浅色域色阶。VanR 的 DBD、hinge 与 LBD/EBD
分别使用浅蓝、浅青绿和浅灰紫，N 端与连接区使用中性浅灰。域色写入图例，并在
主结构、运动图、双状态图和结构冻结网络图中保持一致。代谢物或效应分子使用红橙
球棍、元素相关的原子球和低透明表面，透明表面只辅助定位，原子与化学键保持清晰
边界。

VA 识别壳、二聚界面、hinge、实验替换位点和反向调控对照使用一套稳定的颜色与形状：
识别壳用圆形，界面用菱形，hinge 用三角形，实验替换位点用加深轮廓，反向调控对照
用方形。名称、形状和颜色共同出现。静态截图保留 3–8 个承担解释作用的直接标签；
交互页面可在零碰撞条件下显示完整登记位点，其余读数放在侧栏。

运动视图提供 side 与 orthogonal 两个视角，使用相同尺度和相机中心。两个视角同时
显示二级结构主骨架、显著新增或消失边与红色位移向量，读者能够从侧视和正交方向
辨认整体运动。互作视图与运动视图分开呈现，避免完整网络遮住大尺度结构运动。

二维交互结构使用可辨认的 cartoon 语法。helix 为带纵向曲率的宽 ribbon，并在带内
绘制连续螺旋线；β strand 为具有端部方向箭头的扁平带；loop 为细线。Cα 折线只
作为 trace 或状态系综的浅色辅助层。互作网络叠放在 cartoon 上方，使用更深的边、
加粗节点和白色衬边保持层级。

每个动态状态以真实成员集合显示。状态均值、UMAP 协方差范围和状态内 Cα RMSF
共同描述构象群，邻近成员以浅色细线保留在结构视图中。实验结构状态按实际状态数
显示。双状态差异使用系综平均结构计算逐残基位移与接触重排，分别归一化后联合排序，
并突出最大变化位点与预先登记结构位点。

交互页面另设结构冻结网络视图。骨架固定为当前状态的系综平均结构，时间滑块只
改变网络边、节点和新增/消失状态。实验结构对以 State A 为固定参考。该图与完整
构象互作图并列，分别读取网络重连和大尺度结构运动。

交互结构发布前遍历全部状态，检查时间轴、UMAP、网络、箭头和结构同步；在桌面、
常规移动端和 320 px 窄屏检查零横向溢出、44 px 控制高度与键盘操作；记录控制台、
请求、截图哈希和活动画布变化。截图和 QA 记录必须对应当前 HTML、结构数据与
JavaScript 哈希。

## 16. Cartoon 与 Cylinder 表示契约

每个结构页面和结构增强图同时提供两种可直接比较的骨架表示。两种表示必须由
ChimeraX、PyMOL、Mol*、3Dmol 或同类 molecular viewer 从真实坐标生成。手绘
固定宽度 helix stroke、正弦偏移线、椭圆端帽和手工 β 带不能作为发表级 Cartoon。

### 16.1 Cartoon

- helix 使用分子查看器基于真实主链和 secondary structure 生成的 ribbon；
- β strand 使用扁平方向带，末端箭头沿主链由 N 端指向 C 端；
- loop 使用平滑细线，线宽低于 helix ribbon 与 β 带；
- 结构域使用可区分的浅色，关键残基、配体和网络在骨架前方；
- 不使用单一粗细的 Cα 折线充当 cartoon。

### 16.2 Cylinder

- helix 使用 PyMOL `cartoon_cylindrical_helices=1`，或在 3D molecular viewer 中
  沿真实 helix run 绘制带深色外边界、内层主体、方向高光和端盖的三维圆柱；
- 每个 helix run 的轴、半径和端帽来自真实 Cα 几何；
- β strand 保持扁平方向箭头，避免与 helix 圆柱混淆；
- loop 使用细线，保留真实主链连接；
- 配体使用球棍和透明表面，关键残基使用球、轮廓和文字共同突出；
- 圆柱明暗保持平面印刷可读，关闭夸张高光、阴影和透视。

### 16.3 共享状态与导出

两种表示使用同一真实结构、状态、正交相机、缩放中心、残基编号、结构域颜色与位点
颜色。交互切换保持时间索引、UMAP 当前点、网络边、位移箭头和冻结骨架不变。静态
配对图按相同尺寸和相同视角并排或上下排列，每个结构 axes 内部保持 1:1。

原始结果图保持不变。每个完整报告图位增加独立结构增强版链接；替代版包含原图、
Cartoon、Cylinder、结构来源、关键位点、PNG、PDF、SVG 和渲染记录。发布清单记录
源结构哈希、相机、圆柱半径、端盖、光照、导出哈希、内容占空率和内部空白带。

结构增强 HTML 按结构实体分组。桌面至少使用两列结构卡片，每个结构实体只显示一组
Cartoon/Cylinder 主图；53 个报告图位使用紧凑 anchor 或折叠小图组列出。禁止把同一
结构重复为 53 个整行大卡片。细长结构在自动 Camera 搜索后仍不能同时达到方形画布
有效占空率时，增加同 representation 的正交 inset，并记录 parent 与 inset 的 Camera。
