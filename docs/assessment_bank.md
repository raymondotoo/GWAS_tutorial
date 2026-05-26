# GWAS Assessment Bank

## Quick Quiz: Foundations

1. What does a GWAS test?
2. Why does a significant SNP not automatically identify the causal gene?
3. What is minor allele frequency?
4. Why does LD matter for interpretation?
5. What is the difference between an effect allele and a reference allele?

## Quick Quiz: Quality Control

1. Name two sample-level QC checks.
2. Name two variant-level QC checks.
3. Why can missingness create false associations?
4. When might HWE filtering be inappropriate?
5. Why should QC counts be reported before and after filtering?

## Quick Quiz: Population Structure

1. How can ancestry confound GWAS?
2. What does PCA summarize?
3. What does a kinship matrix capture?
4. When would a mixed model be preferable to ordinary regression?
5. Why can plant breeding panels be especially structured?

## Quick Quiz: Association Testing

1. Which model is commonly used for a quantitative trait in unrelated samples?
2. Which model is commonly used for a binary trait in unrelated samples?
3. Why are covariates included?
4. Why is `p < 0.05` not enough in GWAS?
5. What information should be reported with a top SNP besides the p-value?

## Interpretation Exercise 1: Manhattan Plot

Learners receive a Manhattan plot with one strong peak and several isolated single-SNP spikes.

Ask:

- Which signal would you prioritize and why?
- Which signal worries you and why?
- What QC metric would you check next?
- What LD information do you need?
- How would you describe the result in one cautious sentence?

## Interpretation Exercise 2: QQ Plot

Learners receive three QQ plots:

- Clean null with lifted tail.
- Whole-plot inflation.
- Deflated plot.

Ask:

- Which plot suggests possible true signal?
- Which plot suggests confounding or artifact?
- Which plot suggests overcorrection or low power?
- What follow-up checks would you run?

## Interpretation Exercise 3: PCA

Learners receive a PCA plot where cases cluster mostly in one ancestry group and controls in another.

Ask:

- Why is this dangerous?
- Would adding PCs be enough?
- Would stratification help?
- What would a better study design look like?

## Applied Case Prompt: Plant GWAS

A crop diversity panel has 280 accessions phenotyped for drought tolerance across two locations and two seasons. Genotypes come from sequencing-based SNP calls.

Ask learners to propose:

- Phenotype model or trait summary.
- Sample QC.
- Variant QC.
- Population structure correction.
- Association model.
- Validation plan.

Expected themes:

- Field design and environment matter.
- Kinship and PCs are likely needed.
- HWE assumptions may be questionable.
- Candidate genes require validation across environments.

## Applied Case Prompt: Human GWAS

A biobank case-control study has 12,000 cases and 240,000 controls for a common disease. Samples are genotyped on multiple arrays and imputed.

Ask learners to propose:

- Case/control QC.
- Batch covariates.
- Ancestry handling.
- Association model.
- Imputation quality filters.
- Reporting plan.

Expected themes:

- Array and batch effects matter.
- Case-control imbalance matters.
- Mixed-model or two-step methods may be appropriate.
- Results need independent replication and careful interpretation.

## Capstone Review Questions

A complete capstone should answer:

- What was the scientific question?
- What data were analyzed?
- What phenotype was tested?
- What QC filters were applied and why?
- How were population structure and relatedness handled?
- What association model was used?
- What did the Manhattan plot show?
- What did the QQ plot show?
- Which loci were prioritized?
- What are the limitations?
- What is the replication or validation plan?

## Answer Key Notes

The best answers are not the most complicated answers. They are the ones that connect decisions to the study design, state assumptions clearly, and avoid causal overclaiming.

