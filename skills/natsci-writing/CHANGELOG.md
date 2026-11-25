# Changelog

## 1.2.6.8 — 2026-11-25

- Reflow addendum: a log-scaled axis can inflate the measured row pitch and leave a large internal blank band even when every artist is inside the axes. If a plate develops an unexplained blank band, test the log axis; for a narrow dynamic range use a linear axis, or reserve enough explicit vertical space and recheck the content-extent audit.

- Visible-body addendum: audit PolyCollection/LineCollection paths, not only scatter offsets; extend violin KDE grids by about 1.5 bandwidths (flat caps fail); extend density-contour grids by about 6%; give points on 0/1/thresholds a 2-4% marker margin; check rendered rasters at final display width; serve versioned raster URLs or no-store headers.


Universal data-extent release, derived from a full panel audit of the PGv3
six-figure plate set where several axes still truncated real observations,
confidence intervals or long-tailed controls.

- Every quantitative panel must display the full data extent on both axes;
  limits are computed from the current data, not copied from earlier versions.
- Threshold views require a full-range companion; hidden zero-valued endpoints
  fail.
- The audit compares data extrema with sorted limits in value space, handles
  inverted and log axes, and records clipped-point counts and overshoot per
  panel.
- Default collection offsets and legend proxies are excluded from the count.
- After extending limits, explicit ticks replace auto-locators outside view.

## 1.2.6.7 — 2026-11-25

Evidence-density and visual-finish release, derived from the PGv3 six-figure
review where valid plates still read as sparse.

- Every analytical panel must carry at least three evidence layers
  (observations, distribution, estimate with interval, reference line, effect
  size, cross-condition contrast, structural annotation); the layer count is
  audited.
- Means-only bars and single series without band, points or rug fail; a
  two-category bar panel requires a companion distribution in the same figure.
- Repeated dimension-swap charts (algorithm, rule, environment with the same
  encoding) fail unless one variant adds a distribution, contrast or mechanism
  layer.
- Visual finish: semantic fills with an alpha hierarchy, registered colours for
  every whisker and edge, no default #000000, no mostly empty panels.
- Figure-level rhythm: each row carries a distinct evidence role.

## 1.2.6.6 — 2026-11-24

- Projection panels cover the full data extent with zero clipped points.
- Equal x/y unit length for PCA/t-SNE/UMAP projections.
- Cartoon/ribbon required for fold evidence; 20% background transparency.
- Structure label bands at 10 pt equivalent, never over molecule ink.
- Pre-render structure-file gate for element columns, guide atoms and FASTA.
- Bold argument-carrying claims in HTML reports.
- Raster figure display with separate SVG/PDF links and rendered-page check.

## 1.2.6.4 — 2026-11-24

- Use standard stars inside figures and exact q values in captions/source tables.
- Prefer horizontal header legends and compact state-transition labels.
- Add CI bands and representative significance markers on effect curves.

## 1.2.6.3 — 2026-11-24

- Added hard legend–data separation and compact direct-label fallbacks.
- Protected axis titles during tick thinning and added tick-completeness audits.
- Added dynamic panel headers, range headroom and real-comparison significance
  rules for bars, boxes, violins and forest plots.
- Added release regressions for `legend_data_occlusions`,
  `axis_tick_completeness`, final panel scaling and significance provenance.

## 1.2.6.2 — 2026-11-24

- Added final HTML effective-font and fixed physical-canvas regressions.

