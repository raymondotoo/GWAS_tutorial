# GWAS QC and Analysis Checklists

Use these checklists as teaching aids and project sign-off gates.

## 1. Study Design Checklist

- Primary phenotype is clearly defined.
- Study population or panel is clearly defined.
- Inclusion and exclusion rules are written before association testing.
- Case-control definitions or quantitative trait processing are documented.
- Sample size and power expectations are discussed.
- Covariates are justified by design or confounding logic.
- Data-use permissions allow the planned analysis.
- Replication or validation strategy is identified early.

## 2. Phenotype Checklist

- Units are documented.
- Missing phenotype codes are unambiguous.
- Outliers were checked.
- Transformations are documented.
- Batch, site, field, treatment, season, or measurement platform effects were assessed.
- Case-control balance is reported for binary traits.
- For repeated measures, the aggregation or mixed-model plan is documented.
- For plant traits, field design and environmental conditions are documented.

## 3. Sample QC Checklist

- Initial sample count recorded.
- Genotype missingness per sample checked.
- Heterozygosity outliers checked.
- Duplicates checked.
- Relatedness checked.
- Sex checks performed where applicable.
- Ancestry or population structure visualized with PCA.
- Batch effects assessed.
- Final sample count recorded.
- Every exclusion threshold is justified.

## 4. Variant QC Checklist

- Initial variant count recorded.
- Genome build documented.
- Chromosome naming convention documented.
- Duplicate variants checked.
- Multiallelic handling documented.
- Variant missingness checked.
- MAF or MAC threshold selected.
- HWE checked in an appropriate subset or intentionally omitted with justification.
- Differential missingness checked when appropriate.
- Strand ambiguous variants handled.
- Final variant count recorded.

## 5. Imputation Checklist

- Pre-imputation QC completed.
- Build matches reference panel.
- Alleles harmonized.
- Strand flips checked.
- Phasing method documented.
- Reference panel documented.
- Imputation software and version documented.
- Imputation quality threshold documented.
- Post-imputation allele frequency checked.
- Dosage versus hard-call analysis documented.

## 6. Model Selection Checklist

Use this quick guide:

| Situation | Reasonable starting model |
| --- | --- |
| Quantitative trait, unrelated samples | Linear regression with covariates |
| Binary trait, unrelated samples | Logistic regression with covariates |
| Related or structured samples | Mixed model |
| Large biobank quantitative trait | REGENIE, BOLT-LMM, GEMMA, or similar |
| Large imbalanced binary trait | SAIGE or REGENIE |
| Plant diversity or breeding panel | GLM/MLM with PCs and kinship |
| Rare variants | Burden tests, SKAT, SKAT-O, or gene-based models |
| Multiple correlated traits | Multivariate GWAS or MTAG-like summary methods with caution |

Document:

- Trait model.
- SNP coding.
- Covariates.
- Relatedness handling.
- Software.
- Version.
- Genome build.
- Analysis population.

## 7. Plot Interpretation Checklist

### Manhattan Plot

- Genome-wide threshold is shown.
- Suggestive threshold is explained if used.
- Top peaks are labeled.
- Single-SNP spikes are treated cautiously.
- Known problematic regions are considered.
- Locus boundaries are based on LD or distance rules.

### QQ Plot

- Bulk distribution reviewed.
- Tail behavior reviewed.
- Lambda GC or equivalent reported when appropriate.
- Inflation interpreted in light of sample size and polygenicity.
- Results compared across covariate or mixed-model choices if needed.

## 8. Top Loci Checklist

For each lead locus:

- Lead SNP ID.
- Chromosome and position.
- Effect allele and other allele.
- Effect estimate.
- Standard error.
- p-value.
- Allele frequency.
- Imputation quality if imputed.
- Nearest gene.
- Regional LD context.
- Prior GWAS evidence.
- Functional annotation.
- Replication status.

## 9. Reporting Checklist

- Abstract distinguishes association from causation.
- Methods include all QC thresholds.
- Methods include covariates and model.
- Results include sample and variant counts before and after QC.
- Results include effect sizes, not only p-values.
- Plots include Manhattan and QQ plots.
- Discussion includes limitations.
- Data availability is clear.
- Code or workflow availability is clear where permitted.
- Ethical and diversity considerations are addressed.

## 10. Red Flags

- Strong Manhattan peaks but poor QQ plot.
- Cases and controls separated by ancestry PCs.
- Top SNPs have high missingness or low imputation quality.
- Reported effect allele is unclear.
- Mixed genome builds.
- Allele frequencies differ wildly from reference without explanation.
- No replication or validation plan.
- Biological story built only from nearest gene.
- Polygenic score reported without independent validation.

