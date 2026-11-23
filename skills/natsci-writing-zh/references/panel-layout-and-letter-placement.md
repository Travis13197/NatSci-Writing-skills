# Panel cell 版式与 panel letter 锚点

版本：1.1.0；更新：2026-11-22。修改 panel 间距、panel letter 或完整 cell 边界时，
与 `figure-design-and-audit.md` 一并完整执行。

## 1. 旧检查为何会接受压缩拼图

早期实现把 letter 放在 axes 左上角外侧约 5.8 mm，并允许完整边界净空为
`0.20–0.25w`。该版式即使没有文字碰撞，也可能让 letter 看起来附着在数据框角上，
无法建立清楚的 cell 层级。新版把 letter 定义为 panel cell 的左上锚点，并单独测量
letter 与 axes、标题的关系。

## 2. 当前完整边界间距

- 横向与纵向相邻完整边界的净空均为 `0.38–0.42` 倍 panel 数据框宽度。
- 默认值为 `0.40w`，相当于相邻两张图各自边缘约 `0.20w` 的空白；旧 `0.225`、
  `0.20–0.25` 和 `0.28–0.32` 区间均已退役。
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

- 任一完整边界净空超出 `0.38–0.42w`；
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
