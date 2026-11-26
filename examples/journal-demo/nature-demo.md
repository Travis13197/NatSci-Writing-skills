---
authors: A. B. Author, C. D. Author, E. F. Author
affiliations: 1 Institute of Molecular Systems, Example University; 2 Department of Biology, Example Institute
---

# A measured atlas of protein-language-model geometry that survives held-out families

## Abstract
Protein language models map sequences to vectors, but whether the geometry of those vectors carries information beyond a pooled mean remains unresolved. We assembled a cohort of 29,400 domains across four models and asked whether residue-level fields predict family membership on held-out families. A pooled baseline reaches 0.78 accuracy; a residue-field readout reaches 0.91, and the gain disappears when the alignment step is removed, which localises the effect to alignment rather than model size. The same contrast reproduces in an independent panel of 400 domains with a mean absolute difference of 0.013. We then tested the atlas against a domain-boundary endpoint and found that 62 of 84 predicted boundaries fall within ten residues of the annotation, with the remainder concentrated in low-complexity regions. The atlas is released with per-domain coordinates, the fitted readout, and the exact code needed to reproduce every panel, so that the claim can be re-measured rather than trusted. Together these measurements turn a representation claim into a reproducible procedure that other groups can run on their own families.

## Introduction
Pooled embeddings collapse a protein to one point. That collapse is convenient and lossy.

## Results
### A residue-level readout beats the pooled baseline
On 34 held-out families the readout reaches 0.91 accuracy against 0.78 for a composition-matched baseline [1]. Removing the alignment step drops accuracy to 0.74, so the step carries the gain [2].

### The gain reproduces in an independent panel
In 400 independent domains the mean absolute difference between predicted and observed coordinates is 0.013 [3].

## Discussion
The effect is local to an alignment step and does not require a larger model. The remaining error sits in low-complexity regions, which the current representation does not resolve.

## Methods
Domains were selected by CATH and SCOP annotation. Embeddings were extracted from four models. The readout was trained on 80 percent of families and evaluated on the rest.

## References
1. Author, A. B., Author, C. D. & Author, E. F. A pooled baseline for protein representations. Nature 555, 1-9 (2018).
2. Author, G. H. Alignment steps in protein language models. Science 370, 123-128 (2020).
3. Author, I. J. et al. Domain boundaries from residue fields. Nat. Methods 18, 45-53 (2021).

## Acknowledgements
We thank the reviewers of an earlier version.

## Author contributions
A.B.A. designed the study; C.D.A. ran the analyses.

## Competing interests
The authors declare no competing interests.

## Data availability
Coordinates and code are available at the repository recorded in the reporting summary.

## Figure legends
Fig. 1 | A residue-level readout beats the pooled baseline. a, Accuracy across held-out families. b, Ablation of the alignment step.
