---
authors: A. B. Author, C. D. Author, E. F. Author
affiliations: 1 Institute of Molecular Systems, Example University; 2 Department of Biology, Example Institute
---

# A measured atlas of protein-language-model geometry that survives held-out families

## Abstract
Pooled protein-language-model embeddings collapse a protein to one point. We asked whether residue-level fields carry information that a pooled mean cannot, across four models and 29,400 domains. A residue-field readout reaches 0.91 accuracy on held-out families against 0.78 for a composition-matched baseline; removing the alignment step drops it to 0.74. The contrast reproduces in 400 independent domains, with a mean absolute coordinate difference of 0.013. A boundary endpoint falls within ten residues for 62 of 84 predictions, and the misses concentrate in low-complexity regions. The atlas, the fitted readout and the exact code that produced every panel are released, so the claim can be re-measured rather than trusted, and the boundary result can be tested on new families.

## Introduction
Pooled embeddings collapse a protein to one point [1].

## Results
The readout reaches 0.91 accuracy on held-out families against 0.78 for the baseline [2]. Removing the alignment step drops accuracy to 0.74.

## Discussion
The effect is local to the alignment step and does not require a larger model.

## Methods
Domains were selected by CATH and SCOP annotation.

## References and Notes
1. A. B. Author, C. D. Author, A pooled baseline for protein representations. Nature 555, 1 (2018).
2. G. H. Author, Alignment steps in protein language models. Science 370, 123 (2020).

## Acknowledgments
We thank the reviewers of an earlier version.

## Author contributions
A.B.A. designed the study; C.D.A. ran the analyses.

## Competing interests
The authors declare no competing interests.

## Data and materials availability
Coordinates and code are available at the recorded repository.

## Figure legends
Fig. 1. A residue-level readout beats the pooled baseline.
