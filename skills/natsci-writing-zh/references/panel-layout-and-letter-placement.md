# Panel cell 版式与 panel letter 锚点

版本：1.2.6.8；更新：2026-11-24。修改 panel 间距、panel letter 或完整 cell 边界时，
与 `figure-design-and-audit.md` 一并完整执行。

## 1. 旧检查为何会接受压缩拼图

早期实现把 letter 放在 axes 左上角外侧约 5.8 mm，并允许完整边界净空为
`0.20–0.25w`。该版式即使没有文字碰撞，也可能让 letter 看起来附着在数据框角上，
无法建立清楚的 cell 层级。新版把 letter 定义为 panel cell 的左上锚点，并单独测量
letter 与 axes、标题的关系。

## 2. 当前完整边界间距

- BioNoether 横向与纵向相邻完整边界的净空均为 `0.27–0.29` 倍 panel 数据框宽度。
- 默认值为 `0.28w`，由作者要求把早期 `0.40w` 缩小约 30% 后确定；该覆盖需与实现、
  `panel_visual_gutter_audit.tsv` 和 HTML 说明同步。
- 完整边界包含数据框、letter、单行标题、刻度、offset text、轴标题、直接标注与外部图例。
- 在最终刻度稀疏化和图例定位后，逐对测量相邻 panel；不得用 axes 间距、grid cell
  间距或某一行最小值代替。
- 增大 gutter 时扩大物理画布，不缩小方形数据框、角色字号或标签带。
- 布局收敛后冻结；保存阶段再次执行自动布局会使审计失效。

## 3. Panel letter 锚点

- letter 位于数据框外，并定义完整 panel cell 的左上角。
- letter 左边界位于数据框左边界左侧约 `0.20w`（82 mm panel 约 16.4 mm）。
- letter 底边高于数据框顶边至少 `4 mm`。
- 标题单行、粗体并在数据框上方水平居中。
- letter 和标题共享同一标题顶线，垂直偏差不超过 `0.5 mm`。
- letter 与标题水平净空至少 `3 mm`；标题中心与数据框中心偏差不超过 `0.5 mm`。
- letter 和标题是两个独立文字对象。不得把 letter 嵌入标题、放入数据框、
  与第一个刻度对齐或悬在 axes 内。
- 结构 panel 即使隐藏 image spines，也执行同一规则。

## 4. 必须记录

`panel_visual_gutter_audit.tsv` 记录方向、相邻 panel、完整边界净空毫米值、数据框宽度
和 `gap / panel_width`。

`panel_text_collision_audit.tsv` 逐 panel 记录：

- `letter_left_to_axis_mm`；
- `letter_bottom_to_axis_top_mm`；
- `letter_title_gap_mm`；
- `letter_title_top_delta_mm`；
- `letter_is_cell_left`；
- `letter_is_cell_top`；
- `title_center_offset_px`；
- `title_is_centered`；
- `title_is_bold`；
- `letter_anchor_ok`。

`figure_geometry_audit.json` 汇总 letter 锚点错误、letter–axes 左距最小值和最大值、
letter–axes 纵向净空最小值、letter–标题净空最小值、标题中心偏差错误、标题字重错误、
完整边界 gap ratio 的最小值和最大值。

## 5. 拒绝发布

- BioNoether 任一完整边界净空超出 `0.27–0.29w`；
- letter 从 axes 顶边或更低处开始；
- letter 偏离 axes 左侧约 `0.20w`、距 axes 顶边不足 4 mm，或距标题不足 3 mm；
- 标题未在数据框上方居中，或未使用粗体；
- letter 没有定义 cell 的外侧左上边界；
- 标题带重排后没有重新测量 gutter；
- PNG、PDF、SVG 与已审计布局不一致；
- 没有碰撞但视觉仍显压缩，或 letter 仍像数据框角标。

## 6. 视觉粗糙与证据密度的分界

更宽的 gutter 和更清楚的标题层级解决拥挤，不替代证据密度。panel 仍显简单或粗糙时，
应加入源表已有的样本、区间、匹配、阈值、对照、直接测量或独立验证。不得加入装饰性
边框、饱和色循环、无含义图标或虚构云图。

## 7. 最终显示字号与列 cell 回归

panel 间距、字母和标题在源 raster 中通过，仍可能因 HTML 缩小而失效。每张图同时记录
`effective_font_size_audit.tsv`、`column_cell_width_audit.tsv` 和
`panel_role_audit.tsv`。有效字号按最终 CSS 图像宽复算；任何普通文字低于 10 pt、轴标签
低于 10.5 pt，或列 cell 宽度因单个 panel 的长刻度翻倍，均拒绝发布。

固定网格先生成物理 canvas，再测量完整 cell。不得用
`yaxis.set_label_coords(-0.55, 0.5)`、外置单列图例或 50–80 字符的比较名把标签推入
gutter。y 刻度比较名限为可识别的短标签，统一最多两行；完整变量、单位、比较方向和
样本分母保留在图注与源表。保存时禁止 `bbox_inches="tight"` 二次重排，只裁完全空白的
外缘像素。

## 8. v1.2.6.3 动态标题带

letter 与标题的纵向锚点由顶部 y 刻度文字的完整 bbox、letter/title 实际字高和至少
4 mm 轴顶净空共同决定。固定比例只能在尚未生成刻度文字时作为下限。最终 panel 缩放
后必须重新测量并重放锚点；若标题带高度改变，所有行间距和完整 cell 边界都要重新计算。
标题顶部对齐、单行粗体居中，字母位于 cell 外侧左上区域。

刻度过密时修改刻度和标签，不修改轴标题。类别标签先缩写，再按 rendered bbox 均匀保留
2–4 个；每个轴至少保留两个可解释刻度。

## 9. v1.2.6.4 水平图例与标题顺序

legend 先放标题下的水平多列带，再考虑 axes 端点直接标签，右侧单列是最后回退。顶部
legend 的 y1 进入 panel header 计算；标题与 letter 必须整体高于 legend，不能和 legend
共享基线。状态转移缩成 `C→C/T→T/B→B`，全部全称在 caption。若顶部 legend 宽度不超过
完整 axes，右侧图例即布局失败。

## 10. v1.2.6.6 投影面板的等单位范围

PCA、t-SNE 和 UMAP 面板先取当前 x/y 数据范围中的最长跨度，增加最多 6% 边距，再以各自
数据中心设置等长的 x/y limits。等比例单位与方形数据框分别验收；一个轴不能把另一个轴
压缩成细线。显式设置刻度并保存数据极值、axes limits 与越界点数，越界点数必须为 0。
