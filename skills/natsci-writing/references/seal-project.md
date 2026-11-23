# SEAL manuscript: terminology, reasoning and evidence conventions

Updated: 2026-11-11, skill version 1.1.0. This reference records decisions established during the author's SEAL manuscript revisions. It is a project-specific guide, not a substitute for the latest author text or verified source data. New author revisions and corrected analyses supersede older values. Do not copy historical audit details into polished prose without checking their relevance.

For module III, also read `translation-validation.md`: dimension-to-residue translation, actual figure reading, confidence × sensitivity, case selection and independent biological evidence. For module IV, also read `dimension-annotation.md`: the protein-annotation objective, signed reference sets, statistical scoring, group HVD analysis, library composition, validation metrics and resource availability.

## Conceptual priorities

Keep these three contributions connected throughout the manuscript:
1. Embedding dimensions as elementary quantitative variables: each is a numerical component of a learned vector. They extend descriptions based on residue identity, motifs and domains by incorporating information learned from sequence context. “Underlying/deeper” describes the model's numerical representation, not a more fundamental physical substance or an assertion that classical biology is exclusively qualitative.
2. SEAL as a unified, extensible methodology and technical framework for dimension-based proteomics, integrative biology and bioinformatics. Explain practical extensibility through user-defined protein collections, model-specific embeddings, annotations and optional expression/interaction measurements. Do not imply completed mass-spectrometry or multi-omics validation when only supported input types are being described.
3. Embedding-level AI interpretability: examine how learned numerical components relate to protein-group differences, specific residue-level prediction responses and functional associations. Explain the scientific questions this makes accessible. Prior work already includes feature interpretation, annotation enrichment and feature interventions, so novelty is the specified method and connected workflow.

## Approved language and standard terms

- Title: SEAL decodes protein language model representation spaces at the dimension level.
- Abstract wording anchor: “a standardized framework for embedding-level analysis of pLM representation spaces”; preserve the author's capitalization when explicitly used to explain SEAL's acronym.
- protein language models (pLMs); use the same case throughout.
- protein–dimension–annotation (PDA) data structure/dataset.
- protein-by-dimension matrix: rows are protein sequence entries, columns are embedding dimensions.
- protein-level embeddings may be pooled from residue-level hidden representations; distinguish the two whenever describing perturbations.
- highly variable dimensions (HVDims), not highly-variables dimensions, high variation dimensions or inconsistent HVD abbreviations.
- dimension-level enrichment analyses (DimSEA): module IV umbrella term.
- signed dimension over-representation analysis (signed-DimORA): signed dimension–annotation links and annotation scoring.
- dimension set enrichment analysis (DSEA): selected dimension-set functional analyses with explicit backgrounds and nulls. Preserve implementation differences. Do not treat every DSEA comparison as testing a ranked gene list or automatically against the exact same signed-DimORA library.
- G protein-coupled receptor (GPCR); really interesting new gene (RING) domain; E3 ubiquitin ligase.
- Peptideins: the project's noncanonical open reading frame (ncORF)-derived microprotein collection. Use the author's capitalization. Explain “dark proteins” if retained; it is not a measured functional category.
- ProstT5 sequence-to-3Di decoder; 3Di structural-alphabet states are predictions, not experimentally measured conformational states.
- Prefer dimension values, protein groups, background proteins, annotated terms, residue positions, predicted structural-state probabilities and candidate functional annotations to vague references to coordinates, context, molecular readouts or signatures.
- Define dimension signature if used: the selected dimensions and their directions/effect magnitudes in a specified comparison. This is a descriptive result, not a certified family-exclusive classifier.

## The four modules

Module I of SEAL: dimensionality reduction, neighbourhood-graph construction, clustering and annotation-guided visualization. Explain its purpose before comparing models or parameters. Connect full collection, independently computed family subatlas and representative predicted structures.

Module II of SEAL: compare target dimension distributions with a defined background. HVDims require Benjamini–Hochberg-adjusted P < 0.05 and |Cohen's d| > 0.5 in the established analysis. FDR-only counts have a different meaning. Explain positive/negative effects as higher/lower target values. Volcano plots show significance and magnitude, heatmaps compare selected dimension values across proteins, and feature plots show values over atlas coordinates.

Module III of SEAL: translate selected dimensions, ideally independently established HVDims, back to sequence positions and structural regions, then test whether those positions have independent biological relevance. Perturb the ProstT5 residue/token hidden-state matrix and compare decoder outputs, preserving coordinate identity and accurate residue mapping. Explain case selection: ADK tests correspondence to conformational motion and catalytic studies; CarH tests cofactor-dependent assembly and DNA-binding regulation. Entropy/KL and their four response classes are tools for site selection. The scientific endpoint is residue-level interpretation supported by structural or functional evidence. See `translation-validation.md` for input provenance, aggregation and evidence distinctions.

Module IV of SEAL: use embedding dimensions to annotate the functions of proteins or specified protein collections. Organizing GO/Pfam terms into signed dimension reference sets is the intermediate step that makes query annotation possible. Explain signed direction, the gene-set analogy, hypergeometric query scores and the use of group-specific HVDims before presenting applications. Distinguish the signed-score RING demonstration, individual-protein signed-DimORA and the executed group DSEA procedure. Lead with reusable library composition, relevant recognition/annotation results and Peptidein candidate annotations. See `dimension-annotation.md` for the exact implementation and statistical scope.

## Established cohort and figure distinctions

The following are historical verified examples, subject to newer corrected data:
- Primary full-human collection: 205,228 sequence entries (20,420 Swiss-Prot and 184,808 TrEMBL). Sequence entries can include isoforms; do not label them canonical genes.
- Matched three-model benchmark: 1,418 proteins; balanced geometry subset 63 per class; 20 seeded splits. ProtT5 classification and ProstT5 cosine-silhouette rankings differ. ESMC annotation analyses were a different comparison. No universal winner.
- At the evaluated common k=29 setting, Louvain mean ARI/NMI exceeded Leiden. Do not restore the author's initial suggested superiority without new data.
- Fig. 2 GPCR_orphan_7tm_4 region: 1,232 members, including members without that family annotation. Full-human Pfam-defined GPCR HVDim comparison: 789 target and 204,439 background, 466 HVDims; these are distinct cohorts.
- GPCR effects: dim_419 d=2.0302; dim_478 d=1.9372 in the full-human DE table. Separate Swiss-Prot tables have other effects.
- Human RING HVDims384, mouse RING132, human E3 351; count reflects the specified target and background.
- Human-domain collection: 42,537 domains, 17,976 parent proteins, 6,698 Pfam entries. Domain-region membership and a pure Pfam-defined family are different units.
- Fig. 2 has no a/b/c panels. Central 3D map, inner flanking subatlases, outer representative structure overlays. Most regions show5 structures; cadherin4; ion-channel display is residues1–1,200.
- Current family model source was ESMFold2 per the generation manifest. OpenDDE was a later proposed stage. Verify the exact current software from source, not the naming of a better-known older model.
- Fig. 3: a workflow, b human reference atlas, c GPCR volcano, d heatmap, e featureplot, f translation, g–i ADK responses/structures. The reference atlas and full-human HVDim analysis need not be the same cohort.
- Fig. 4: a DimSEA workflow; b domain atlas; c RING comparison; d dimension library; e/f within-library scoring; g Peptidein atlas; h cluster annotation; i annotation coverage.
- Numbering established during revisions: Supplementary Figs1 cross-model,2 atlas algorithms/settings,3 2D atlas/family subatlases,4 structural representatives,5 HVDims,6 domain atlas,7 RING recognition,8 ADK,9 CarH/family-dimension application,10 cross-dataset panel,11 DimORA validation,12 DSEA nulls,13 E3,14 Peptideins. Confirm against the current manuscript before using.

## Evidence distinctions for the final Results

- The archived22-dimension comparison panel was explicitly supplied by source code; its GO table contains dim_754 counts68/36/36. Original selection lists did not reproduce a22-way intersection in earlier checks. Describe the selected panel; do not claim established conserved intersection or call dim754 the broadest term coverage.
- In the30-dimension DSEA example,214 human RING and93 mouse RING values are sums of significant dimension–GO-BP associations. A term contributes repeatedly across dimensions. Random-dimension100-set means±SD are53.5±38.342 and89.87±43.725. Domain union-statistic results count unique terms and are different.
- RING sensitivity0.9836 vs random0.7458±0.1966 at a threshold calibrated to1% FPR; at5%,0.9891 vs0.9524±0.0409. Random dimension sets n500; empirical P=.006/.1377 respectively. Calibration uses5000 decoys. Held-out positive domains183; selection backgrounds formerly included some held-out positives, so do not call it strictly independent validation.
- The archived dimension library contains 87,860 enrichment-ranked signed links covering 7,639 terms. GO BP/MF/CC/Pfam term counts are 4,129/1,608/1,114/788; requiring at least five signed links retains 1,088/655/678/308. Only 40,634 retained links pass the original term-level BH criterion; the other 47,226 were carried with the top-ranked lists from passing scans. Do not call the entire library term-level FDR significant. Actual GO-BP recovery uses 14,707 proteins with scorable truth. Recall@10/50/100 = 0.0907/0.1963/0.2752 is within-library macro-averaged recall, not annotation accuracy. See `dimension-annotation.md` before choosing performance wording.
- Human/mouse E3 collection386/805, RING subset227/537. Do not confuse proteins with domains.
- Peptideins7264 unique ORFs; five clusters432/1580/1965/1669/1618 sum7264. Annotation channels3/30/101/136/2336 use the same ORF collection but different evidence rules and overlap. They represent InterProScan domain-type calls, independent Pfam scan, any InterProScan call, source curation and dimension-based candidate calls. The2336 rule was top_q<.05. Candidate coverage is not correctness.
- FDR-only Peptidein count1008/1024; length-control958; composition-control992. Existing control median199aa, peptide sequence median34aa; ORF nt/3 median35 includes a different length convention. These results motivate better matching; they do not establish a quantified causal contribution or prove microprotein-specific function.

## Known issues to recheck before asserting corrected results

These are source-check reminders, not generic manuscript language:
- Old GPCR display code used dim-1 against dim_0-based columns; verify named columns before interpreting featureplots. Old volcano log-P summaries also mixed raw/adjusted statistics.
- ADK open response ranks V1174/214 and D51149/214 were supported by the matrix. Closed confidence summaries134/1 disagreed with matrix mean ranks95/110. H_gen identical across214 positions in stored open/closed tables. Do not infer independently conditioned physical states without input provenance.
- CarH model0-based107/158/226 maps to PDB88/139/207; plotting code previously mixed numbering.
- RING-dimension switching panels used the CarH decoder input. An analysed RING-associated coordinate does not make the input sequence a RING protein. Independently rendered RING structures do not by themselves verify residue-level perturbation provenance.
- Old70:30 DimORA validation had reverse hypergeometric-P ranking, inconsistent training scaling and training-universe errors. Archived below-null numbers are not a reliable negative validation. They require a corrected rerun.
- Fig4c design Signed-HVD cells previously read a different annotation source; mouse UniProt fractions and domain denominators mixed units. Even when independent score tables support a percentage, correct the source linkage.

## Literature context already considered

Reverify publication status and content if quoting or updating:
- Rives et al., Biological structure and function emerge from scaling unsupervised learning to250 million protein sequences. PNAS2021. DOI10.1073/pnas.2016239118.
- Simon & Zou, InterPLM: discovering interpretable features in protein language models via sparse autoencoders. Nature Methods2025. DOI10.1038/s41592-025-02836-7. SAE features and targeted generation steering already exist.
- Gujral, Bafna, Alm & Berger, Sparse autoencoders uncover biologically interpretable features in protein language model representations. PNAS2025. DOI10.1073/pnas.2506316122. Protein-level and residue-level SAE analyses and GO enrichment already exist.
- Heinzinger et al., Bilingual language model for protein sequence and structure. NAR Genomics and Bioinformatics2024. DOI10.1093/nargab/lqae150.
- ProtGenesis: Universal physical principles govern the deterministic genesis of protein structure. Liu et al., bioRxiv2026, DOI10.64898/2026.02.20.706798. Public author repository links the preprint; direct bioRxiv access was previously blocked. Safe brief comparison: quantifies embedding changes during stepwise assembly/mutation and complements dimension-centred analysis. Do not present its physical-law claims as independently proven by SEAL.

## Closing principle

Keep the author’s conceptual ambition and make it explicit through concrete scientific relationships. Preserve strong, accurate prose. Use brief author notes for unresolved source issues instead of filling the scientific text with repetitive disclaimers or turning exploratory associations into established mechanisms.
