# NatSci-Writing-skills v1.2.6.4

This release standardises statistical marks and legend placement across
multi-panel publication figures.

## Statistical notation

- `*`: q<0.05
- `**`: q<0.01
- `***`: q<0.001
- `****`: q<0.0001
- `n.s.`: q≥0.05

Exact q values, adjustment methods and comparison keys remain in captions and
source tables. Continuous effect curves pair a 95% CI band with representative
first/middle/last stars; significance-state changes and the last observation
remain labelled.

## Legend order

1. Horizontal multi-column legend below the panel title.
2. Direct endpoint labels in a real right-side corridor.
3. One-column legend on the right as the final fallback.

State transitions use compact `C→C`, `T→C`, `T→T` and `B→B` codes. Dynamic
panel titles and letters sit above the rendered horizontal legend.

## Regression focus

The release adds explicit checks for Main Fig. 12 g/h, Main Fig. 14e and Main
Fig. 15b, plus all-panel checks for star collisions, q text, legend mode, axis
titles, final font size, data occlusion and browser rendering.
