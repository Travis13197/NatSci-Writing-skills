# Baker-style structural figure standard

Version: 1.8.0; updated 2026-11-22.

## Evidence base

This standard is derived from twelve representative structural figures in ten original
David Baker laboratory papers. The complete record is
`B:/2026_Exploration/writing/structural-figure-research-2026-11-14/BAKER_STRUCTURAL_FIGURE_EVIDENCE.md`.

## Core grammar

1. Establish the whole assembly, symmetry axis and binding location before any close-up.
2. Use a neutral grey/surface context and one saturated foreground object.
3. Use brightness differences within one hue for homologous chains.
4. Reserve separate hues for model, prediction, experiment, ligand and a second state.
5. Keep the parent context visible in every interface close-up.
6. Show only the three to six side chains needed to support the mechanistic claim.
7. Use orthographic views and a fixed camera for all members of a comparison.
8. Pair every structural panel with a quantitative contact, distance, BSA, RMSD or response panel.
9. Put the full residue list in the legend or source table, not in the image.
10. Export PNG, PDF, SVG and an editable PyMOL/ChimeraX session.

## Palette

| Role | Colour |
|---|---|
| neutral context | `#CAD7DC`, `#B7C1C7`, `#586B75` |
| primary structure | `#0D5673` |
| second homologous chain | `#4E8EAD` |
| interface / validation | `#16786F` |
| functional site | `#C77A24` |
| ligand / active centre | `#B8453E` |
| prediction / orthogonal state | `#6C5079` |
| text / annotation | `#132B36` |

Use `specular <= 0.10`, no cast shadows, and one restrained key light. Save a separate
`STRUCTURE_RENDER.json` containing source PDB/CIF hash, protein and site colours, camera,
lighting, ink bounding box, crop box, content occupancy, exports and editable-session hashes.

Common failures include saturated rainbow chains, different colour versions between the
structure image and statistical panels, stale `.pse` sessions after recolouring, high-specular
rendering, and assigning row height from an uncropped PyMOL canvas.

## Ligand pockets

Show transparent cartoon or surface context, ligand as ball-and-stick, three to six pocket
side chains as sticks, heteroatom colouring, and only evidence-supported interactions.

## Protein interfaces

Keep both sides of the interface visible. Use muted grey-blue context, brighter blue/teal
for focus residues, external labels with short leader lines, and no more than six direct
labels per close-up.

## Protein–DNA/RNA interfaces

Use pale blue or pale grey DNA/RNA, a blue/teal HTH or DBD, and a whole-complex panel that
shows whether the other protein chain remains in the assembly. Keep operator orientation
constant across comparisons.

## Assemblies

Use a monomer → interface → oligomer → assembly sequence with one hue family and brightness
changes between subunits. Overlay design and experimental models with a stable grey-versus-
colour convention.

## Typography and export

Minimum direct label size is 10 pt, axis labels are at least 10.5 pt and panel letters are 12.5 pt. Reserve image space for readable labels instead of scaling text down.
Use orthographic projection, flat cartoon rendering, weak shadows and white background.
Output 600 dpi PNG, PDF, editable SVG and `.pse`/`.cxs` sessions.

## Whitespace and raster packing

Structural whitespace failures usually arise from two independent causes: the renderer writes a full camera canvas around a small molecule, and the figure layout allocates a row from that source canvas rather than from molecular extent. Correct both.

1. Measure the bounding box of non-white molecular ink separately for the whole-structure and close-up renders. Crop outer margins and retain a small, consistent 2-4% padding that protects labels and sticks.
2. Use a square axes for equal-role structural comparisons. If the global render is elongated, keep it as the parent view and place a sufficiently large local side-chain inset or second view inside the square. Do not turn the panel into a 2:1 or 3:1 strip merely because the molecule is elongated. Never use non-uniform scaling or decorative fill.
3. Derive the structural axes height from `width_fraction x (figure_width / figure_height) / (image_width / image_height)`. Check the post-draw axes bounds when using an equal image aspect; an axes box that moves outside its intended row indicates an inverted aspect calculation or conflicting fixed geometry.
4. Top-align structural views with different aspect ratios, place the following row from the deepest rendered content edge, and keep gutters smaller than the 14% blank-band release limit.
5. Save source-ink, crop, composite, final-axes and exported-raster measurements. Reject a composite whose ink bounding box covers less than 85% of either panel dimension, or whose exported figure contains an internal blank row band above 14% of the figure height without a registered scientific layout exception.
6. Re-run panel-letter and title bounds after the structural layout. A title placed relative to the page rather than inside the image axes can appear to fit in code while being clipped after tight export.
7. Compare rendered structural panels with neighboring quantitative panels. Equivalent panels should have equal square footprints, similar visual area and deliberate gutters. A tiny structure band above a large square plot fails release even when its own raster has little white border.
8. Measure the assembled plate from complete panel boundaries that include the raster, panel
   letter, wrapped structure title, ticks, axis labels and external legend. Horizontal and
   vertical clearances must each be `0.38–0.42 × panel data-box width`, default `0.40`.
   Measure after final tick suppression, freeze the converged layout, and prevent the save
   step from repeating `subplots_adjust` or automatic title placement. The panel letter
   defines the cell's outer upper-left blank and remains approximately `0.20 × panel width`
   left of and at least `4 mm` above the structure data box. The structure title is centred
   over the data box and bold.

## Release checklist

- whole assembly and close-up agree on object identity;
- only one colour role per mark;
- ligand is unobstructed;
- essential side chains are visible;
- labels have no overlap or clipping;
- quantitative panel uses the same states and residue numbering;
- whole and local rasters are ink-cropped and packed by object extent without stretching;
- final exported figure passes the structure-content and blank-row-band thresholds;
- structural panels have the same square footprint and visual weight as neighboring equal-role panels;
- complete horizontal and vertical structural-panel boundaries retain `0.38–0.42 × panel
  width` clearance and the exported layout matches the measured layout;
- editable session and source structure are present.
