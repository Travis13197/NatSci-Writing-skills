# Figure contract

Write this before plotting. One contract per figure.

## Core contract

- Core conclusion (one sentence with a verb):
- Figure archetype: quantitative grid / schematic-led composite / image plate + quantification / asymmetric mixed-modality
- Target journal and final output:
- Column width and final size (mm):
- Backend: Python / R (exclusive once chosen)
- Panel count and grid:
- Reading order:

## Panel map

| Panel | Question it answers | Evidence type | Statistic / n | Source data | Reviewer risk |
|---|---|---|---|---|---|
| a | | | | | |
| b | | | | | |

## Evidence hierarchy

- Hero evidence:
- Validation:
- Controls / robustness:
- Boundary or transfer test:

## Statistics

- n definition:
- Centre and dispersion:
- Test, sidedness, correction:
- Effect size / interval:
- Model split / seeds / metric definition:

## Image integrity (if imaging)

- Raw file:
- Crop:
- Brightness/contrast/gamma:
- Pseudo-colour:
- Scale calibration:
- Stitching / reuse:
- Quantification link:

## Release checks

- [ ] One data plot per panel; no inset/mosaic panels
- [ ] Journal width, type size, line weights, raster dpi
- [ ] Panel letters and titles per journal convention
- [ ] Colour-blind and greyscale checks; semantic colour roles stable
- [ ] Text-text, text-canvas, text-mark collisions checked for all artist types
- [ ] Caption states n, error definition, test and correction
- [ ] Composite reproducible from per-panel exports (SEAL/project)
- [ ] Source data and plotting script archived
