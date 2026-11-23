# Statistics, reporting and research integrity

Version 1.1.0; updated 2026-11-23. Read when drafting the Statistical analysis section, auditing Results and figure legends, responding to statistical reviewer comments, or preparing a Nature Portfolio reporting summary. This is a reporting and review skill, not a substitute for a statistician reanalysing raw data.

## 1. Design transparency before statistical language

Separate three questions: what was measured, what unit was analysed, and what inference is claimed.

For every analysis identify:
- endpoint/response and groups/conditions;
- independent experimental unit;
- biological versus technical replicates;
- repeated measures, pairing, blocking, batches, donors, animals, patients, plots, model runs;
- inclusion/exclusion, missing-data handling;
- randomisation and blinding where applicable;
- transformation/normalisation;
- test or model, assumptions, and correction family;
- estimate, uncertainty, exact P, sample size;
- software/package/version.

Treat the independent experimental unit as the default n. Do not silently treat cells, fields, spectra, reads, wells, repeated readings, model runs or technical replicates as independent biological samples.

## 2. Nature statistical requirements (flagship)

At initial submission, statistical information must already be complete enough for editors and referees. Required Methods content:
- every test used and the comparison/model it addresses;
- one-tailed versus two-tailed;
- independent experimental unit;
- definitions of biological/technical replicates;
- paired/unpaired or repeated-measures structure;
- inclusion/exclusion, randomisation, blinding where applicable;
- multiple-comparison correction strategy.

Required numerical reporting:
- exact n; individual values if n varies;
- definition of every error bar/interval;
- number of repeated experiments;
- exact P values for significant and non-significant results where relevant;
- ANOVA: F statistic and degrees of freedom;
- t-test: t statistic and degrees of freedom;
- exact comparison, test family and tail near the result.

A Reporting Summary is required for life sciences, behavioural/social sciences, ecology/evolution/environmental sciences, and covered physical-science areas. Cross-check the completed form against Methods, Results, legends and Source Data; flag contradictions in sample sizes, exclusions, randomisation, blinding or software.

## 3. Statistical analysis paragraph

Order: software/environment → data-summary convention → sample-size and replication definition → test/model choice → multiplicity strategy → thresholds/exact reporting → exclusions/robustness.

Prefer exact values:
- "Treatment A was associated with a higher response than control (mean difference ..., 95% CI ..., P = ...)."
- "The analysis used animals as the independent unit; cell-level measurements show within-animal variability."
- "The evidence is consistent with an increase, although the small sample limits precision."

Avoid:
- proved, demonstrated conclusively, confirmed the mechanism, based only on a P value;
- highly significant without effect size or uncertainty;
- n = 300 cells when the experiment has three animals or three cultures;
- ns as the only result;
- data were normally distributed without a basis, especially for small samples.

## 4. Common failure modes

**P0 — may undermine a central claim**
- Pseudoreplication: n is cells/images/fields/reads while the independent unit is animal/patient/culture/batch/experiment.
- Uncorrected multiple comparisons with an undefined or selective family.
- Wrong interaction inference: one comparison significant and another not is not evidence that the effects differ.
- Analysis-unit mismatch: paired, matched, blocked, longitudinal, nested or repeated-measures design analysed as independent.

**P1 — important reporting risk**
- Significance-only conclusions without effect size or interval.
- Small-sample overclaim.
- Unsupported normality/equal-variance assumptions.
- Missing software/version, exact n or error-bar definition.
- Stars without correction status or exact P values.

**P2 — clarity**
- Inconsistent replicate terminology.
- Legends omit panel-specific n.
- ns labels unclear.
- Statistics scattered across Methods, legends and SI without a map.

## 5. Figure statistics

Each quantitative panel legend should state:
- what points/bars/boxes/lines/shaded regions represent;
- exact n and what n counts;
- summary convention (mean ± s.d./s.e.m., median with IQR, 95% CI, model estimate);
- test/model, paired/unpaired or repeated-measures;
- multiple-comparison correction;
- exact P values or star thresholds;
- whether source data include raw independent values.

Plot-type rules:
- Bar plots: prefer individual points; if bars remain, define error and n.
- Box plots: state median, box bounds, whisker rule, outlier rule, n.
- Violin plots: define points, density caveat and independent unit; do not let dense cell-level violins imply many independent experiments.
- Time courses: state whether the same units are followed; use repeated-measures/mixed models when inference uses all time points.
- Heat maps/omics: state normalisation, scaling, clustering distance/linkage, multiplicity/FDR and whether rows/columns were selected post hoc.
- Regression/correlation: report coefficient or correlation, uncertainty, n, independence and whether descriptive or inferential.

Star notation should state the test, correction and comparison family; exact P values and sample sizes belong in Source Data.

## 6. Image integrity

For microscopy, gels, blots and processed images record:
- raw file and processed file;
- crop;
- brightness/contrast/gamma adjustments and whether global or local;
- pseudocolour;
- scale calibration and scale-bar length;
- stitching, lane rearrangement, reuse in other figures;
- quantification link;
- processing software.

Global adjustments are generally safer than local selective edits. If an adjustment changes the visibility of relevant background or bands, flag it rather than normalising it away.

## 7. Data, code and materials reporting

- Data Availability: map each dataset to a repository, accession/DOI or exact Source Data file; state restrictions and access route; cite deposited datasets.
- Code Availability: separate headed statement for central custom code; repository/DOI, version, licence, environment, entry point; reviewer access when central to claims.
- Materials: persistent identifiers (RRIDs) for key antibodies, cell lines and organisms; authentication, source and distribution restrictions; protocols deposited and cited.
- Never invent repository names, DOIs, accession numbers, licences, software versions, approvals or reviewer identities.

## 8. Severity labels and reviewer-risk phrasing

Use P0/P1/P2 as in Section 4. Neutral phrasing:
- "A reviewer may challenge whether the analysis treats the correct independent unit as n."
- "The legend does not make clear whether points are biological replicates or technical subsamples."
- "The claim is stronger than the statistical evidence currently reported."
- "The comparison family is not defined, so correction status is unclear."

Unless raw data and the full design are supplied, prefer "not assessable from the supplied material", "potential risk", "requires author confirmation".

## 9. Statistics audit table

| Analysis/panel | Test and tail | Exact n and replicate unit | Error/interval | Exact P | Test statistic and df | Repeat count | Status |
|---|---|---|---|---|---|---|---|

Status: pass / AUTHOR_INPUT_NEEDED / not applicable with reason / blocked.

## 10. Reporting-integrity gate

- Is the independent unit defined for every central claim?
- Are biological and technical replicates separated?
- Is every central result mapped to a test/model or a clear descriptive statement?
- Is multiplicity either corrected or explicitly limited/prespecified?
- Are exact n, error definitions, P values and test statistics available?
- Are figure statistics aligned with Methods and Source Data?
- Are image adjustments and raw-file provenance documented?
- Are data/code/materials statements real, durable and consistent?
- Is the Reporting Summary complete and consistent with the manuscript?
- Are missing facts labelled rather than invented?

## 11. Data, code and materials: mandatory deposition and access

For flagship Nature and most Nature Portfolio journals:

- Every original research Article needs a headed Data Availability statement; place it with Methods/end-of-Methods per the current sequence.
- Map primary and reused datasets to repositories, accession numbers or exact Source Data/Supplementary files; cite deposited datasets in the reference list.
- Use community repositories for sequences, structures/EM maps, gene expression, proteomics, crystallography, and field-specific data; personal sites, mutable cloud folders and unarchived GitHub branches are not durable records.
- Code central to the claims needs a separate Code Availability statement, reviewer access, a versioned DOI-minting archive and a licence; state restrictions precisely.
- Materials: persistent identifiers (RRIDs) for key antibodies, cell lines and organisms; authentication, source and distribution restrictions; deposit protocols and cite the DOI.
- Controlled, clinical or third-party data: state why access is restricted, the responsible committee/route, eligibility, application procedure, expected timeframe, data-use agreement and what metadata remain public. "Undecided" is not a sharing plan.
- Check mandatory deposition gates and structure validation files before submission; verify accessions resolve.

Reporting guidelines: use the study-type standard where applicable (CONSORT for randomised trials, STROBE for observational studies, PRISMA for systematic reviews, ARRIVE for animal research, field-specific standards). The Reporting Summary must agree with Methods, Results, legends and Source Data.

**Data-integrity audit**: every claim-critical dataset has a durable route; every accession resolves; no "available on request" without reason/route/eligibility/metadata; code can be run by a reviewer; materials requests have a named route; statements are consistent across files.
