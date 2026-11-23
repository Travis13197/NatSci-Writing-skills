# Semantic colour and release-audit contract

Version 1.1.0; updated 2026-11-22.

Use this contract for manuscript figures, extended-data figures, structure/statistics composites and any HTML figure group that will be presented as a release candidate.

## 1. Stable semantic roles

| Role | Colour | Release rule |
|---|---|---|
| primary model, structure or system | `#0D5673` | primary identity and direct comparison |
| secondary model or structural context | `#4E8EAD` | comparison fill and near-site context; use dark text |
| support, confirmation or independent success | `#16786F` | evidence meeting a frozen rule |
| conditional, cautionary or condition-dependent category | `#C77A24` | marks and fills; do not use for small text on white |
| negative, failed or disruptive category | `#B8453E` | failure, stopping or destructive substitution |
| orthogonal validation or second state | `#6C5079` | independent or orthogonal evidence |
| neutral comparison or control | `#586B75` | nulls, controls and context |
| text and axes | `#132B36` | text, panel letters, spines and tick labels |

The project may map named objects to these roles, but one object must keep one role throughout the figure group. For example, if ESM2 is primary blue in one panel, it remains primary blue in every panel. If ProstT5 fails a rule, show the failure with hatch, an outline, a cross marker or a direct label while retaining ProstT5's object colour. Do not silently change its colour to grey in one summary panel.

## 2. Redundant categorical encoding

Use at most three chromatic categories plus one neutral role in a typical qualitative panel. Above three categories, add a non-colour channel: marker shape, line style, fill state, hatch, ordered position, grouping or direct labels. Non-colour icons must carry a defined scientific meaning. Decorative icon variety does not increase information density.

Continuous variables use a monotone blue ramp. Signed deviations use brick-red to neutral to deep blue. Do not use `jet`, `rainbow`, `hsv` or `gist_rainbow`.

## 3. Matrix panels

Do not place numbers, coefficients, letters or `yes / ~ / x` inside matrix cells. Use cell fill plus an outline, corner marker or external legend, and retain exact values in source data.

## 4. Structure and statistics

Structure context, mutation sites, ligands, statistical categories and captions use the same palette. When the statistical palette changes, rerender structure PNG, PDF, SVG and editable sessions. Save `STRUCTURE_RENDER.json` with source PDB/CIF and hash, camera, lighting, object and site colours, molecular-ink box, crop box, content occupancy, exports and session hashes.

## 5. Required release files

`figure_color_audit.tsv` has one row per panel:

`figure, axis_index, role, cmap_names, forbidden_cmap, matrix_texts_inside_cells, chromatic_colors, n_chromatic_colors, unregistered_colors, minimum_text_contrast_to_white, text_colors, non_colour_encodings`

`figure_palette_roles.csv` records every approved role, colour, contrast against white and permitted usage. `STRUCTURE_RENDER.json` records every structure composition.

## 6. Fail-closed conditions

Reject release when any panel contains an unregistered colour, a forbidden colormap, text below 4.5:1 contrast on white, text inside matrix cells, a categorical comparison that relies on colour alone, or a structure/statistics colour mismatch. Also reject a figure when the same object changes colour semantics between panels, or when a sparse summary panel substitutes recolouring and decorative icons for evidence.
