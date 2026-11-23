# Panel-cell layout and letter placement

Version 1.1.0; updated 2026-11-22. Read in full with
`references/figure-design-and-audit.md` whenever panel gutters or panel letters are changed.

## 1. Why the older checks passed compressed plates

A prior implementation placed each panel letter at approximately
`(-0.115 × axes width, 1.045 × axes height)` in axes coordinates. The letter therefore
started at the axes top and only 5.8 mm to the left of the data box. The complete visual
boundary moved by that small distance, while the audit accepted complete-boundary gaps from
`0.20` to `0.25 × panel width`. The plate could therefore pass with:

- the letter visually attached to the upper-left data-box corner;
- approximately 11 mm complete-boundary gaps around a 51 mm data box;
- no text collision and no canvas overflow;
- no measurement of whether the letter actually occupied the cell corner.

Those conditions establish separation and readability, but they do not establish a
publication-grade panel hierarchy. A later `0.28–0.32w` revision still left the header band
shallow and the titles left-aligned. The 1.18 standard reserves approximately one fifth of
the panel dimension as blank separation at each side, treats the letter as the panel-cell
anchor and centres a bold title over the data box.

## 2. Current gutter contract

- Horizontal and vertical complete-boundary gaps must each be `0.38–0.42 × panel data-box
  width`.
- The default is `0.40 × panel width`, representing approximately `0.20 × panel width` of
  blank separation at each adjacent panel side.
- `0.225`, the former `0.20–0.25` range and the `0.28–0.32` range are retired.
- A complete boundary is the union of the data box, panel letter, single-line title, tick
  labels, axis labels, direct labels and external legend.
- Measure every adjacent pair after final tick suppression and legend placement. Do not use
  only axes rectangles, cell allocations or the minimum of one favourable row.
- Increase the physical canvas when the larger gutter is required. Do not reduce the square
  data box, type floor or label bands.
- Save only after the grid has converged. A repeated `subplots_adjust`, `tight_layout` or
  automatic title pass invalidates the measurement.

## 3. Panel-letter contract

- The panel letter is outside the data box and defines the outer upper-left blank of its
  complete panel cell.
- The letter box begins approximately `0.20 × panel width` left of the data-box left edge
  (`7–12 mm` for a 50.8-mm panel).
- The bottom of the letter remains at least `4 mm` above the data-box top.
- The title is horizontally centred over the data box and bold.
- Letter and title share one title top line within `0.5 mm`.
- The shared title top line is about `0.20 × panel height` above the data-box top.
- The horizontal gap between the letter box and title box is at least `3 mm`.
- The letter and title are separate text objects. The letter cannot be embedded in the title
  string, placed inside the data box, aligned with the first tick or centred over the axes.
- A structure panel follows the same anchor rule even when image spines are hidden.

## 4. Required measurements

`panel_visual_gutter_audit.tsv` records:

- orientation;
- adjacent panel identifiers;
- complete-boundary gap in millimetres;
- panel data-box width in millimetres;
- `gap / panel_width`.

`panel_text_collision_audit.tsv` records per panel:

- `letter_left_to_axis_mm`;
- `letter_bottom_to_axis_top_mm`;
- `letter_title_gap_mm`;
- `letter_title_top_delta_mm`;
- `letter_is_cell_left`;
- `letter_is_cell_top`;
- `title_center_offset_px`;
- `title_is_centered`;
- `title_is_bold`;
- `letter_anchor_ok`.

`figure_geometry_audit.json` aggregates:

- `panel_letter_anchor_errors`;
- `minimum_letter_left_to_axis_mm`;
- `maximum_letter_left_to_axis_mm`;
- `minimum_letter_axis_clearance_mm`;
- `minimum_letter_title_gap_mm`;
- `title_center_errors`;
- `title_weight_errors`;
- `minimum_complete_boundary_gap_ratio`;
- `maximum_complete_boundary_gap_ratio`.

## 5. Fail-closed conditions

Reject the plate when:

- any complete-boundary gap is outside `0.38–0.42 × panel width`;
- the letter begins at or below the axes top;
- the letter is closer than 7 mm to the axes left, closer than 4 mm vertically, or closer
  than 3 mm to the title;
- a title is not centred within `0.5 mm`, is not bold or exceeds the data-box width;
- the letter, rather than the title boundary, fails to define the cell's outer upper-left
  extent;
- a header-band reflow changes gutters without remeasurement;
- the PNG, PDF and SVG do not match the audited layout;
- the plate passes collision checks but remains visually compressed or visually attached
  to the axes.

## 6. Improvement without decorative inflation

Larger whitespace and a clear title hierarchy address visual crowding. They do not replace
evidence density. When a panel still reads as simple or coarse, use available samples,
uncertainty, matching, thresholds, controls, direct measurements or independent validation.
Do not add decorative frames, saturated colour cycling, arbitrary icons or synthetic sample
clouds. A low-emphasis reading grid may use the registered pale neutral role; it must remain
behind the data and does not count as an additional evidence encoding.
