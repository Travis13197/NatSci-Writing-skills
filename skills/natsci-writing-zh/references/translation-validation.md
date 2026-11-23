# Dimension translation: scientific objective and validation

Updated: 2026-11-11. Project-specific evidence recorded during SEAL revisions. Recheck against new data before use. These notes preserve the reasoning and source distinctions; they do not establish completed experimental validation.

## 1. Keep the purpose of translation explicit

The central question is whether a selected embedding dimension, especially an independently identified HVDim, can be translated back to specific sequence positions and structural regions with biological meaning. The argument should connect:

HVDim selection and direction → dimension-by-residue perturbation matrix → fixed site-selection rule incorporating prediction uncertainty and response → independent structural/functional evidence → new experimentally testable sites.

A description of entropy, KL and four quadrants alone does not demonstrate successful biological translation. State why the case is informative and what the external comparison tests. The intended scientific claim and the result actually generated must remain distinguishable.

Do not refer to a residue as an HVDim. The dimension is a model variable; the residue is a position implicated by translating or perturbing that variable. Preserve the identity of the selected dimensions across pooled protein vectors and residue-level analysis.

Before describing an HVDim-specific result, verify that the matrix rows are the HVDims selected by the group comparison. A heatmap of dimensions selected by high mean KL, a score using signed top-effect coordinates and an average over all model dimensions are different analyses. Correctly labelled demonstrations of the translation method can be retained when HVDim provenance is incomplete.

## 2. Read and interpret the actual figure

Read the complete image and legible crops, including g/h/i, supplementary schematics and labels. Check axis direction, units, percentile calculation, region boundaries, threshold lines, colours, selected-site labels, residue numbering, structural state and source matrix.

For the archived ADK figure:
- A row of the response matrix is an embedding dimension; a column is an output/residue position after verified token mapping.
- The displayed 50 dimensions are selected by mean KL response across the sequence. The archived residue-level mean profile averages all 1,024 tested dimensions. Those summaries cannot be substituted for one another.
- `kl_max` is the maximum response over the positive and negative perturbation, not automatically the maximum across dimensions.
- Some figures use a 0–99 min–max-normalized KL summary. This is neither raw KL nor a response percentile.
- The combined scatter uses `100 * (N - descending_rank + 1) / N`, with N = 214. Larger displayed percentiles represent stronger relative responses. Other scripts use empirical rank percentages and handle ties differently.
- Within-protein rank changes do not establish absolute KL differences between states or batches.
- An older scatter labels an axis as percentile while showing values up to 214. Reconcile the actual calculation and label.

## 3. Generation entropy and perturbation sensitivity

Generation entropy H_gen describes uncertainty of the decoder's baseline autoregressive output distribution. In the methodological definition, H_gen(t) = -sum_k P_AR(t,k) log P_AR(t,k). Lower entropy means a more concentrated predictive distribution. Inspect the producing code before asserting token vocabulary, normalization, log base or units.

KL compares baseline and perturbed output distributions under specified decoding conditions. Inspect whether these are teacher-forced from generated tokens, all-ones dummy decoder inputs, or another baseline. Different versions are different interventions; do not combine them into one claimed experiment.

The archived implementations softmax over the full output logits. This alone does not establish a 20-state 3Di-only probability distribution. Keep H_gen and H_base separate unless their producing computation confirms equivalence. A baseline entropy column cannot automatically substitute for the generation entropy used in another figure.

The joint analysis has two numerical axes and four operational classes:

| Class | Generation entropy | KL response | Direct interpretation |
|---|---|---|---|
| Q1, lower left | Lower | Lower | Concentrated prediction with relatively low sensitivity to the tested interventions |
| Q2, upper left | Lower | Higher | Concentrated prediction with relatively high intervention sensitivity |
| Q3, lower right | Higher | Lower | Diffuse prediction with relatively low intervention sensitivity |
| Q4, upper right | Higher | Higher | Diffuse prediction with relatively high intervention sensitivity |

These are four response classes, not four embedding dimensions. Q2 can prioritize sites at which a confident model output depends on the perturbed representation. Higher entropy is not an experimental disorder measurement; low entropy is not a probability of correctness or pLDDT. Low KL is not proof of conservation, canonical structure or lack of functional importance. High KL is not proof of a functional hinge, intrinsic conformational ambiguity or global-versus-local information dependence.

Labels such as state-encoding site, functional polymorphism, disorder and canonical conserved site require evidence beyond quadrant membership. A Q4 label of KL-independent is inconsistent with the high-response axis.

Thresholds are part of the analysis. Define them in Methods and keep the point classification, plot lines and explanatory text consistent. The archived open ADK labels match H_gen median 0.15726236 and the normalized-response median; the combined plot draws H_gen = 0.5. Closed labels have additional inconsistencies. Do not adjust thresholds after inspecting known sites to improve apparent recovery.

## 4. Explain why each case was chosen

ADK: an enzyme with experimentally characterized NMP/LID opening and closing, catalytic residues, crystal structures and mutational/dynamical literature. It tests correspondence to conformationally relevant regions and independently studied functional positions.

CarH: a cobalamin-dependent photoreceptor whose dark-state oligomerization and light response regulate DNA binding, with cofactor contacts, subunit interfaces and published site-directed mutants. It tests a different functional mechanism from ADK domain movement.

Explain this selection in one short sentence per case. Do not present both cases as generic examples of a large KL peak.

## 5. ADK evidence and state provenance

Identity: E. coli ADK, UniProt P69441, 214 residues. PDB 4AKE is the apo open reference; 1AKE is the Ap5A-bound closed reference. Some supplied figures reverse these names. Check structure identity rather than copying a title.

The inspected encoder inputs use the same amino-acid sequence in the <AA2fold> direction. They do not contain measured PDB coordinates or an identified state condition. Mapping a response to two structures does not establish state-resolved predictions. Archived open and closed H_gen values are identical at all 214 positions. Closed response tables and current per-dimension matrices disagree. Do not claim successful open/closed discrimination until final inputs, decoder contexts, perturbation settings and aggregation are aligned.

Useful archived open-associated results:
- Val117: H_gen 0.0084; mean response rank 4/214.
- Gly122: H_gen 0.0073; rank 5/214.
- Arg123: H_gen 0.0126; rank 29/214.
- Gly100: H_gen 0.0258; rank 6/214.
- Asn102: H_gen 0.7163; rank 3/214, so high response alone does not imply low entropy.
- Asp51: H_gen 0.0060; rank 149/214.
- Lys13 and Arg36: lower mean responses despite established catalytic/binding relevance.

These observations support selected model-response correspondences; they do not define a complete ranking of biological importance.

Independent literature already examined:
- Brokaw & Chu, Biophys J 2010, DOI 10.1016/j.bpj.2010.09.040. Artificial unfolding of residues 169–175 produces alternative contacts including Val117–Leu168, Arg36–Ser129 and Arg167–Thr175. This is context-dependent MD evidence, not single-site proof of Val117 being the principal hinge.
- Beckstein et al., J Mol Biol 2009, DOI 10.1016/j.jmb.2009.09.009. Local rearrangements include regions 50–54 and 114–116; salt-bridge networks provide mechanistic hypotheses. Regional overlap is not a direct mutation result at Asp51 or Val117.
- Dulko-Smith et al., J Chem Inf Model 2023, DOI 10.1021/acs.jcim.2c01629. Functional mutant set includes K13Q, R36A, R88A, R123A, R156K, R167A and D158A. Only specified variants/conditions show enhanced opening; do not equate all activity changes with the same motion effect. Arg123 is a useful independent functional comparison, not part of the original five manually highlighted sites.
- Mattsson et al., Biochemistry 2025, DOI 10.1021/acs.biochem.5c00306. E114-helix 113–122 includes Val117; experiments target Glu114. K47-helix 44–56 includes Asp51; experiments target Lys47. Describe the exact residue tested and the regional relevance separately.

The original Arg2/Asp51/Val117/Ser129/Thr175 highlights are manually specified in plotting code, not a demonstrated automatic top-five or predeclared experimental site set.

## 6. Structural displacement is a separate comparison

A new local comparison of deposited 4AKE and 1AKE C-alpha coordinates was performed during the revision. Primary fit: chain A to A, Kabsch alignment on specified CORE residues 1–29, 68–117 and 161–214. Cross-checks used all C-alpha atoms and all A/B chain pairings. Thr149 had the largest displacement in all eight comparisons.

Primary CORE-fit displacements: Thr149 23.95 Å, Val117 2.39 Å, Asp51 16.46 Å, Ser129 19.25 Å. The largest coordinate displacement, hinge role, energetic control, catalytic necessity and decoder sensitivity are different biological or computational quantities. A hinge can move less than the domain it enables to move, but that principle does not prove a particular residue is causal.

These are new retrospective analyses, not original figure results. Add their methods and source tables if used in the manuscript. Do not quietly use them as completed HVDim-specific or experimental validation.

## 7. CarH evidence, selection and mapping

5C8E is Thermus thermophilus CarH bound to AdoCbl and DNA in the dark state, resolution 3.89 Å. Model zero-based positions 107, 158 and 226 map to chain-A Leu88, Ala139 and Leu207; the construct includes a tag. The KL matrix has 306 output positions, while mapping covers 305 construct positions and 285 native residues. Exclude or explicitly account for tag, special and unmapped positions in native-site rankings.

Dim72, dim356 and dim748 appear among the top dimensions ranked by mean decoder KL. Their HVDim status was not established in the inspected source. The old Leu88/Ala139/Leu207 highlights are manually specified. Their peaks also come from different dimensions; do not attribute all three to dim748 or claim automatic quadrant selection.

Independent evidence:
- Jost et al., Nature 2015, DOI 10.1038/nature14950. His142 and Asp201 mutants disrupt dark-state tetramer formation; compensatory Asp201/Arg176 substitutions partly rescue assembly and DNA binding. Trp131, Glu141, Gly160, Gly192, His177 and DNA-binding residues have distinct functional evidence.
- Poddar et al., Nat Commun 2023, DOI 10.1038/s41467-023-40817-6. His132 involvement in light response depends on conditions and construct; its photodissociation phenotype differs from the earlier report. Avoid an unconditional necessity claim.

Retrospective native-residue rankings depend on aggregation:
- Among the 285 mapped native residues, averaging the 50 displayed dimensions ranks His142 sixth and Asp201 twenty-seventh.
- Averaging all 1,024 dimensions ranks His142 43rd and Asp201 second.
- Important sites including His177 and His132 are not uniformly high; include them in an unbiased assessment.
- New 5C8E coordinate inspection finds reciprocal chain-A/chain-B Ala139–Leu207 contacts around 4.0–4.1 Å. This supports interface candidates, not established energetic importance or a direct mutant phenotype.

## 8. Validation design and writing

Before claiming recovery of critical sites, fix the HVDim set, background, perturbation scale, response aggregation, entropy definition, selection threshold, residue mapping and independent functional-site set. Compare recovery/ranking against matched random-dimension or background-site controls. Evaluate catalytic, moving-domain, cofactor-binding and interface roles separately where appropriate.

Use the chain: why this case → selected dimensions → matrix-based candidate rule → recovered positions → independent evidence and biological inference. Keep low-level implementation conflicts in author notes and Methods; retain any qualification needed to prevent the manuscript from claiming state discrimination, HVDim specificity or experimental causality that was not demonstrated.

Relevant local deliverables, if available in the current workspace:
- `SEAL1Article/Figure3-Translation-双指标解释与修订.md`
- `SEAL1Article/Translation-关键位点文献与独立结构验证.md`
- `AI-files/_translation_fig3_review/ADK_structure_vs_translation_response.csv`
- `AI-files/_translation_fig3_review/ADK_independent_literature_sites_vs_response.csv`
- `AI-files/_translation_fig3_review/CarH_literature_sites_vs_translation_response.csv`

Reopen actual sources when numbers or definitions change. Do not rerun broad literature searches merely to repeat a conclusion already adequately verified.
