# NatSci-Writing-skills v1.2.6.3

This release turns the CellAuto figure audit into reusable publication rules
for legends, ticks, panel headers, axis headroom and significance display.

## Release gates

- Legends, direct labels and series text cannot cover data.
- Direct labels are limited to four short series and retain stable
  axes-fraction spacing after final panel scaling.
- Axis titles survive tick collision handling.
- Every axis retains at least two interpretable ticks.
- Panel titles and letters clear the rendered top tick.
- Linear extrema receive range headroom; non-negative proportions keep zero.
- Significance marks use only real comparisons and adjusted q values.
- Forest q values occupy a separate outside column.
- Combined distributions keep violin, box and observations visible.

## Audit fields

`legend_data_occlusions`, `zero_legend_data_occlusion`,
`axis_tick_completeness`, `all_axes_have_visible_ticks`,
`sparsified_tick_labels`, `zero_text_collisions`,
`zero_text_data_occlusion`, `typography_compliant` and
`all_panels_evidence_dense`.

The bilingual SKILL documents, figure references, R50 checklist, HTML/data
verification guide and prompt library contain the full implementation and
regression guidance.
