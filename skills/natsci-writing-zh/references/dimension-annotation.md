# Dimension-based protein annotation: direction, reference sets and evidence

Updated: 2026-11-11. This reference records the author's confirmed scientific emphasis and the inspected SEAL implementation. New verified data supersede historical numbers. Read the actual scoring/library code before changing a statistical claim.

## 1. Preserve the direction of the scientific argument

The central insight is that embedding dimensions can be used to annotate protein function. Constructing functional annotations for dimensions is an intermediate step, not the final purpose of module IV.

Organize the argument as:

Annotations of characterized proteins → term-associated signed dimension sets → statistical scoring or enrichment for a query protein or defined protein collection → recovery of known annotations and candidate annotations for uncharacterized proteins.

Prefer a heading such as “DimSEA enables protein functional annotation from embedding dimensions.” Do not reduce the section to “investigating the functions associated with dimensions selected in group comparisons.” Keep the endpoint explicit in the opening paragraph, validation and concluding inference, consistent with the approved abstract.

The signed-dimension reference is analogous in organization to a gene-set library used to investigate cellular functions. Here each biological term corresponds to dimension identities and the direction of their association. Explain the analogy once. The analogy does not mean that a dimension is a gene or that the implementation is identical to GSEA.

## 2. What signed-DimORA means

DimSEA is the umbrella for module IV. Define the two-stage idea concretely:

1. Reference construction: investigate GO/Pfam annotation enrichment among reference proteins with high or low values in each dimension; reorganize the results by annotation term to obtain signed dimension sets.
2. Query use: compare the query's high- and low-valued dimensions with the matching directions in each term's reference set; use statistical overlap scores to rank candidate functions.

“Signed” refers to a term's association with higher or lower dimension values relative to a stated background. It does not imply activation versus repression, positive versus negative functional effect, or experimentally measured causality.

The archived single-protein signed-DimORA script selects the 200 dimensions with largest absolute standardized values, then separates them by sign. There are 200 selected dimensions in total, not 200 per direction. Positive query dimensions are compared with positive reference dimensions, and negative query dimensions with negative reference dimensions. Each directional overlap is tested with a one-sided hypergeometric upper tail over the 1,024-dimension universe.

The archived scorer takes the smaller directional P value and computes -log10(P) for ranking. It does not combine the directions by Fisher's method, correct the choice of direction, or perform term-level BH in that scorer. The Peptidein annotation script additionally adjusts across terms but retains the directional-minimum step. Describe these values as statistical scores unless the complete null and multiplicity calibration is verified. They are not probabilities that a functional annotation is correct.

## 3. Individual proteins and user-defined protein groups

The author wants the framework to support both:
- An individual query protein, using its standardized dimension values to rank candidate functional annotations.
- Any specified protein collection, including a previously defined class or atlas cluster, using the group's HVDims as input for functional analysis.

Explain what was actually executed. The inspected DSEA implementation receives precomputed group-specific HVDims, selects proteins with extreme absolute standardized values for each dimension in the relevant target/background collection and tests GO enrichment. It does not itself discover the HVDims, and the 214/93 summary is not an ORA of the query dimension set against the signed-DimORA reference library.

It is legitimate to describe both as connected capabilities of SEAL, with module II providing HVDims and module IV supplying annotation analyses. Do not silently replace one algorithm with the other's description or imply that every group result used the same term–dimension library.

Use clear language: “For a specified protein group, DSEA uses its HVDims to investigate enriched functional annotations under the defined protein background.” Include enough method detail to identify the tested objects without filling Results with implementation steps.

## 4. Reference-library construction and composition

Inspected source chain:
- `AI-files/_p1_go_pfam_scan.R`: full 205,228-entry human ProstT5 embedding matrix; top 200 and bottom 200 proteins for each dimension. Eligible terms have 5 to N/20 members. One-sided hypergeometric enrichment; BH within each ontology × dimension × direction.
- `AI-files/_p1_top_hits.R`: expands each scan's 20 best-ranked terms, copying scan-level `n_sig` and minimum adjusted P to every row.
- `AI-files/_build_dim_annotation_dataset.py`: retains the expanded top-20 lists from scans containing at least one BH-significant term.
- `AI-files/_dim_annotation/DimAnnotation_term2dims.csv`: the resulting library.

Historical library counts:

| Category | Terms with reference links | Terms with at least five signed links | Signed links |
|---|---:|---:|---:|
| GO biological process | 4,129 | 1,088 | 23,400 |
| GO molecular function | 1,608 | 655 | 21,540 |
| GO cellular component | 1,114 | 678 | 23,860 |
| Pfam | 788 | 308 | 19,060 |
| Total | 7,639 | 2,729 | 87,860 |

Each `(category, term, dimension, sign)` is unique. Opposite directions for the same term/dimension are distinct signed links. Do not count signed links as unique dimensions.

Important correction: 87,860 records are enrichment-ranked reference links. Only 40,634 of the retained links satisfy the original scan's term-level BH criterion; 47,226 are other top-ranked terms carried along with the passing scan. The library's `padj` field inherited a scan-minimum statistic and cannot establish that every stored link is significant.

Safe resource wording: “a GO/Pfam-based signed dimension reference library” or “reference sets constructed from enrichment-ranked term–dimension links.” A reusable resource is not automatically a community-endorsed standard or a term-level FDR-filtered library. If the library is rebuilt using only significant links, recompute its composition and all downstream performance before reporting revised results. Do not transfer the old performance to a new library.

## 5. Validation evidence and metrics

### RING recognition is a separate signed-score demonstration

Do not label the RING classifier as a completed GO/Pfam signed-DimORA library or hypergeometric classifier. It selects 30 dimensions by absolute effect size and averages direction-weighted background-standardized values.

Historical cohorts: 550 RING domains from 227 parent proteins. Splitting by parent protein gives 367 reference domains from 159 proteins and 183 query domains from 68 proteins. The score uses 17 positive and 13 negative dimensions.

At a threshold exceeded by 1% of 5,000 random reference domains, 180/183 query RING domains are recognized: 98.36%, normally reported as 98.4%. At the 5% threshold, 181/183 are recognized: 98.91%. For the 1% reference threshold, 500 random 30-dimension sets have mean recognition 74.58%; empirical P = 0.006. The 5% random-set comparison has P = 0.1377.

Use actual counts and plain definitions. “Reference false-positive threshold” is clearer than an unexplained “operating point.” This is positive-domain recognition/sensitivity under the evaluated procedure, not overall classification accuracy or protein-function annotation accuracy.

The archived feature selection used reference positives against the remaining domain collection, which included query RING domains. Parent-protein separation therefore does not ensure independent feature selection. Retain the tested scope and disclose/correct this issue; do not call the result a strict independent test.

The stored 24 tested designed RING sequences were all recognized, but deleted/control and other designs also passed. This supports RING-like recognition, not discrimination of catalytic activity or successful engineering.

### Functional annotation recovery

The scoring matrix has 20,420 proteins, different from the full reference scan. Actual category-specific evaluation requires at least one scorable existing annotation:

| Category | Proteins contributing to recovery |
|---|---:|
| GO biological process | 14,707 |
| GO molecular function | 14,572 |
| GO cellular component | 15,335 |
| Pfam | 7,656 |

The `n_proteins` column in the archived all-axis result includes some proteins skipped for having no scorable truth. Use the actual denominator when reporting sample size.

Mean signed-dimension scoring in the historical within-library analysis gives recall@10 values of 5.559%, 7.219%, 2.900% and 39.773% for GO BP/MF/CC/Pfam. Relative to the matched random-term expectation in that comparison, the fold values are 6.17, 4.68, 1.95 and 12.21. These are category-specific annotation-recovery comparisons, not signed-DimORA performance for every category or held-out accuracy. State which scoring method produced them.

In the GO BP comparison, signed-DimORA gives macro-averaged recall@10/50/100 of 0.0907/0.1963/0.2752. Mean signed-dimension scoring gives 0.0556/0.1330/0.2080. Recall is calculated per protein as the fraction of its known scorable terms found among the top candidates, then averaged across proteins. It is not top-k precision, the fraction of proteins with any correct hit, or an annotation-correctness percentage.

The 63.2% relative increase at top10 is mathematically valid for that comparison, with an absolute change from 5.56% to 9.07%. Do not substitute it for absolute performance to create a misleading impression. The author prefers a concise statement that the statistical scorer recovered more existing annotations across evaluated cut-offs when the detailed recall series distracts from the central result. Keep absolute results and null definitions available in the figure/supplement. Different files use different random-term draws; do not mix their fold values.

### Secondary evidence and placement

The 22-dimension panel's selection provenance is incomplete; recurring term counts alone do not establish cross-species conservation or annotation transfer. Remove it from the main annotation argument unless there is a clear, verified conclusion.

The 214 human-RING and 93 mouse-RING DSEA values count dimension–term occurrences across 30 dimensions, not unique functions or prediction accuracy. These tests characterize functional associations under their own backgrounds and nulls; retain them in the supplement or a dedicated analysis when relevant. They need not interrupt the main reference-library/annotation narrative.

E3 atlas organization and 351 HVDims demonstrate the earlier modules' application. Keep them in the atlas/HVD section or supplementary context if no additional annotation result is being reported.

## 6. Peptidein application

Use Peptideins as the application to poorly characterized sequences and explain why the lack of existing annotations makes the case informative.

Historical collection: 7,264 unique ORFs. Five separately computed atlas clusters contain 432, 1,580, 1,965, 1,669 and 1,618 sequences. Distinguish cluster-associated functional terms from individual candidate annotations; do not assign a cluster term to every member without supporting individual scores.

Candidate dimension-based annotations: 2,336/7,264 = 32.2%. This is inferred coverage under the specified rule, not 32.2% proven function or independent correctness. The source rule applies term-level BH after the direction-minimum P step; its calibration is subject to the scoring issue above.

Other channels in the same ORF collection: literature/source curation 136, any InterProScan signature 101, independent Pfam scan 30, InterProScan domain-type signature 3. Channels overlap and use different evidence criteria. Do not sum their counts or call the coverage ratios accuracy advantages.

Length/composition controls remain relevant: broad dimension significance is also observed in control comparisons; the archived length matching is incomplete. Keep the controls in the study record and discuss their implication for annotation specificity. They can be placed in supplementary Results and Discussion when they would otherwise dominate the annotation Results paragraph.

## 7. Resource availability

The author wants a closing resource sentence stating that the signed dimension library is available with SEAL for custom datasets. Before writing that it is public on GitHub, verify the exact repository, release and reference files. An earlier check of the known author profile and repository list did not locate an accessible SEAL/reference-library release; that is a dated access result, not proof that no other repository exists.

If still unverified, write the resource's intended/reusable capability in the manuscript and place a conditional availability sentence in an author note. Once verified, name the URL and clarify model/checkpoint, compatible preprocessing, library version and licence. “Any custom dataset” means a suitable dataset generated with the corresponding representation and protocol, not arbitrary dimensions from unrelated models.

Do not publish files as part of language editing. Do not invent a GitHub URL or assert that a transfer package is publicly downloadable.

## 8. Preferred section architecture

1. Annotation purpose, signed-set idea and gene-set analogy.
2. How single queries are statistically scored and how defined groups use HVDims.
3. Compact RING-domain recognition demonstration with reference/query numbers and clear threshold meaning.
4. Reusable GO BP/MF/CC/Pfam library: composition, justified annotation-recovery evidence and resource use/availability.
5. Peptidein group and individual candidate annotations.
6. A short final inference stating how dimensions support functional annotation of proteins with limited prior knowledge.

Follow actual figure order where possible; if extensive reordering improves the argument, synchronize figure labels and citations deliberately. Keep the main prose discovery-focused, the method descriptions sufficient and the metrics correctly named. Strong writing does not require declaring uncertain performance to be high accuracy.

Relevant local deliverable: `SEAL1Article/DimSEA-功能注释主线-核查后中英文稿.md`. Source scripts and result files are listed there. New verified implementations supersede these notes.
