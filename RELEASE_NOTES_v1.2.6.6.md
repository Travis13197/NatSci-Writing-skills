# NatSci-Writing-skills 1.2.6.6

Date: 2026-11-24

This release consolidates the PGv3 exploratory-growth figure rewrite. It adds
four hard gates, each derived from a failure that survived an earlier audit.

## 1. Projection panels must show the complete data

The PGv3 embedding panels had been drawn with limits inherited from an older
dataset; 1,532 of 10,520 states fell outside PC1. The redraw recomputes limits
from the current data, records the number of clipped points (must be zero),
and stores data minima and maxima next to the axes.

## 2. Equal x/y unit length for projections

PCA/t-SNE/UMAP panels now require equal spans, equal aspect and a square axes
box so that one unit of PC1 equals one unit of PC2 on the printed page.

## 3. Cartoon, not surface, for fold evidence

Fold-evidence panels use ribbon/cartoon geometry; surface-only renders are no
longer accepted as fold evidence. Non-focal loops and background chains are
grey at 20% transparency, and each tile reserves a white label band at 10 pt
equivalent.

## 4. Structure files must pass a chemistry gate

Predicted PDB writers may left-justify element symbols and treat atom-name
prefixes as elements; CA then reads as calcium. PyMOL then sets zero guide
atoms, builds no cartoon geometry and renders a blank or hairline object. The
gate checks element columns 77-78, guide atoms against C-alpha count and FASTA
recovery, rewrites the element columns when needed and records source and
corrected SHA-256.

## 5. HTML claims and figure display

- Bold the topic sentence of each Results subsection, decisive numbers and
  logical turns, the abstract's conclusion and each caption's inference clause
  (1-3 spans per paragraph).
- Display figures as 600 dpi raster and link SVG/PDF separately; verify the
  rendered page by screenshot at the figure position, not only by
  naturalWidth.

All gates are reflected in both natsci-writing and natsci-writing-zh
references and in manifest.json.
