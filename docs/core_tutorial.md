# Core GWAS Tutorial

## 1. What GWAS Is

A genome-wide association study tests many genetic variants across the genome for statistical association with a trait. The trait can be binary, such as disease status, or quantitative, such as height, expression level, flowering time, yield, metabolite level, or drug response.

The basic unit is usually a SNP. For each SNP, learners should imagine a small regression model:

```text
phenotype = baseline + genotype_effect + covariate_effects + error
```

The genotype is commonly coded as 0, 1, or 2 copies of the effect allele. The estimated genotype coefficient is the effect estimate. The p-value asks whether the observed association is surprising under a null model of no SNP-trait association.

GWAS is powerful because it is agnostic: it does not require choosing candidate genes in advance. That same strength creates a central burden: a significant result must be interpreted through quality control, LD, ancestry, study design, replication, and biology.

## 2. What GWAS Is Not

GWAS does not directly prove causation. A significant SNP may be:

- The causal variant.
- In LD with a causal variant.
- A proxy for ancestry or technical batch.
- A false positive from chance, structure, relatedness, phenotype artifact, or unmodeled confounding.

GWAS also does not fully explain complex traits. Common SNP GWAS usually captures a portion of heritable variation, especially for polygenic traits influenced by many variants of small effect, rare variants, structural variants, epigenetic regulation, gene-environment interaction, and measurement noise.

## 3. Core Vocabulary

### SNP

A single-nucleotide polymorphism is a genomic position where individuals differ by base. GWAS usually treats SNPs as markers that tag nearby haplotypes.

### Allele

An allele is a version of a genetic variant. In GWAS result files, pay careful attention to:

- Effect allele: the allele for which the reported effect is estimated.
- Other allele or non-effect allele.
- Reference allele: allele in a reference genome, which is not always the same as the non-effect allele.

### Minor Allele Frequency

Minor allele frequency, or MAF, is the frequency of the less common allele in the analyzed sample. Low-MAF variants are harder to test because fewer individuals carry them, so estimates are less stable.

Common teaching rule:

- `MAF >= 0.05`: common variant.
- `0.01 <= MAF < 0.05`: low-frequency variant.
- `MAF < 0.01`: rare variant.

These boundaries are conventions, not laws.

### Linkage Disequilibrium

Linkage disequilibrium, or LD, is non-random association between alleles at different loci. If two SNPs are in high LD, knowing one genotype gives information about the other.

LD matters because:

- A genotyped SNP can tag an unobserved causal variant.
- Nearby significant SNPs may represent one association signal.
- LD patterns differ across ancestries and species.
- Fine mapping needs accurate LD from a relevant population.

### Population Structure

Population structure is systematic allele-frequency difference among subgroups due to ancestry, geography, breeding history, selection, or demographic history. If a trait also differs across those subgroups, GWAS can detect ancestry-associated markers rather than trait-causing loci.

Common controls:

- Principal components as covariates.
- Stratified analysis.
- Linear or generalized mixed models.
- Careful phenotype and cohort design.

### Kinship and Relatedness

Related individuals share long chromosome segments. If relatedness is not modeled, association statistics can be inflated. Mixed models use a genetic relationship matrix or kinship matrix to account for this.

### Manhattan Plot

A Manhattan plot shows genomic position on the x-axis and `-log10(p-value)` on the y-axis. Peaks suggest associated regions. The plot is a discovery map, not proof of causality.

### QQ Plot

A QQ plot compares observed p-values with expected p-values under the null. It helps detect inflation, deflation, technical artifacts, population structure, and strong polygenic signal.

## 4. Study Design Before Software

A good GWAS begins before the command line.

### Question

Define one primary question:

```text
Which genomic loci are associated with trait X in population Y under design Z?
```

Avoid vague goals such as "find genes for disease" or "run GWAS on yield." Better:

```text
Identify common SNP associations with drought-stress yield in replicated maize field trials after accounting for population structure and field block.
```

### Phenotype

Phenotype quality is often the limiting factor.

Ask:

- Is the trait biologically coherent?
- Is measurement repeatable?
- Is the phenotype measured before or after treatment?
- Are case and control definitions consistent?
- Are outliers biological or data errors?
- Are environmental covariates recorded?
- Is the phenotype transformed or residualized?

For plant GWAS, field design matters:

- Location.
- Season.
- Replication.
- Field block.
- Treatment.
- Environmental exposure.
- Genotype-by-environment interaction.

For human GWAS, phenotype definition matters:

- Diagnosis source.
- Age at onset.
- Medication effects.
- Ascertainment.
- Controls.
- Comorbidities.
- Electronic health record artifacts.

### Genotype

Genotype sources include:

- SNP arrays.
- Whole-genome sequencing.
- Exome sequencing.
- Genotyping-by-sequencing in plant studies.

Common formats:

- VCF: flexible variant call format.
- PLINK BED/BIM/FAM: classic binary PLINK format.
- PLINK PGEN/PVAR/PSAM: newer PLINK 2 format.
- BGEN: common in large imputed datasets.

### Power

Power depends on:

- Sample size.
- Allele frequency.
- Effect size.
- Phenotype quality.
- Case-control balance.
- Genotype quality.
- LD between tested and causal variants.
- Multiple-testing burden.
- Model fit.

Small GWAS can be useful for teaching, pilot analysis, or large-effect loci, but common complex-trait discovery usually needs large sample sizes or strong experimental design.

## 5. Quality Control

Quality control is not a checklist to execute blindly. It is an argument that the data are suitable for the scientific question.

### Sample QC

Common sample checks:

- Missing genotype rate.
- Heterozygosity outliers.
- Sex checks where biological sex is relevant and available.
- Duplicates.
- Close relatives.
- Ancestry outliers or population clusters.
- Batch effects.
- Phenotype missingness.
- Consent and data-use restrictions.

### Variant QC

Common variant checks:

- Missingness or call rate.
- MAF.
- Hardy-Weinberg equilibrium in appropriate control groups.
- Differential missingness by case-control status or batch.
- Strand ambiguity.
- Multiallelic handling.
- Duplicate variant IDs.
- Reference build consistency.
- Allele frequency comparison with reference panels.

### Hardy-Weinberg Equilibrium

HWE filtering can detect genotyping errors, but it must be used carefully.

In human case-control GWAS, HWE is often checked in controls. In structured plant populations, inbred panels, selected breeding material, or non-random mating systems, HWE assumptions may not hold. A mechanical HWE filter can remove real biology.

### Missingness

Missingness can create false associations when missing genotype calls correlate with phenotype, ancestry, batch, or DNA quality.

Check:

- Per-sample missingness.
- Per-variant missingness.
- Missingness by case/control group.
- Missingness by batch or genotyping array.

## 6. Population Structure and Relatedness

Population structure is one of the central GWAS hazards. If ancestry correlates with both genotype and phenotype, naive association tests can produce false positives.

### PCA

Principal component analysis summarizes genetic variation. In GWAS, PCs are commonly included as covariates:

```text
phenotype ~ SNP + age + sex + PC1 + PC2 + ... + PCN
```

PCA is also a visual diagnostic:

- Do samples cluster as expected?
- Are there outliers?
- Are cases and controls uneven across ancestry clusters?
- Are study sites or batches aligned with PCs?

### Mixed Models

Mixed models include a random effect that captures genetic relatedness:

```text
phenotype = fixed effects + random genetic effect + error
```

Use them when relatedness, cryptic relatedness, family structure, breeding design, or population structure is substantial.

## 7. Association Models

### Quantitative Trait

For a continuous trait:

```text
trait ~ SNP + covariates
```

Use linear regression for unrelated samples with manageable structure. Use a linear mixed model for related or structured samples.

### Binary Trait

For a case-control trait:

```text
case_status ~ SNP + covariates
```

Use logistic regression for unrelated samples. Use methods such as SAIGE or REGENIE for large, imbalanced, or related biobank data.

### Plant and Crop GWAS

Common models include:

- GLM when structure is minimal.
- GLM plus PCs or Q matrix for population structure.
- MLM with kinship for relatedness.
- MLM plus PCs or structure matrix plus kinship.

Because plant panels often reflect breeding history, selection, inbreeding, and field design, modeling population structure and environment is central.

### Covariates

A covariate should be included because it addresses design, confounding, or precision.

Typical human GWAS covariates:

- Age.
- Sex.
- Genotyping batch.
- Recruitment site.
- Ancestry PCs.

Typical plant GWAS covariates:

- Field location.
- Season.
- Block.
- Treatment.
- Kinship.
- Population PCs.

Avoid conditioning on variables that are consequences of the genotype-trait pathway unless the estimand requires it.

## 8. Multiple Testing

GWAS tests hundreds of thousands to millions of variants. A nominal p-value threshold such as `0.05` is not meaningful on its own.

Common thresholds:

- Human common-variant GWAS often uses `5e-8`.
- Exome-wide or array-specific studies may use a threshold based on the number of effective tests.
- Plant GWAS may use Bonferroni, FDR, permutation, or LD-aware thresholds depending on marker density and design.

Teach this principle:

```text
The threshold should match the number of independent hypotheses and the study purpose.
```

Discovery, screening, and replication do not need identical thresholds.

## 9. Reading GWAS Plots

### Manhattan Plot Interpretation

Ask:

- Which loci cross the significance threshold?
- Are neighboring SNPs also associated?
- Is there a single-point spike with no LD support?
- Are peaks concentrated in regions of poor genotype quality?
- Are there known nearby genes or previous GWAS hits?
- Does the signal replicate?

### QQ Plot Interpretation

Ask:

- Does the bulk follow the null line?
- Is the tail lifted, suggesting true associations?
- Is the whole distribution inflated?
- Is there deflation from overcorrection or low power?
- Do results change after adding PCs or using a mixed model?

Inflation can reflect confounding, but in highly polygenic traits it can also reflect widespread true signal. LDSC can help separate polygenicity from confounding in human summary statistics when assumptions are met.

## 10. Imputation

Imputation predicts untyped genotypes using observed genotypes and a reference panel. It increases genomic coverage and helps harmonize datasets across genotyping platforms.

Typical steps:

1. Pre-imputation QC.
2. Coordinate and allele harmonization.
3. Phasing.
4. Imputation against a reference panel.
5. Post-imputation QC using imputation quality metrics.
6. Association testing using dosage or best-guess genotypes.

Important cautions:

- Imputation quality varies by ancestry.
- Rare variants impute poorly unless reference panels are well matched.
- Strand and build mismatches can corrupt results.
- Post-imputation filters should use imputation quality and allele frequency.

## 11. Meta-Analysis

Meta-analysis combines results across cohorts. It can increase power, but only if studies are harmonized.

Check:

- Genome build.
- Effect allele.
- Other allele.
- Allele frequency.
- Effect scale.
- Standard error.
- Sample size.
- Phenotype definition.
- Covariates.
- Ancestry composition.
- Imputation quality.

Fixed-effect meta-analysis estimates one shared effect. Random-effect meta-analysis allows heterogeneity. Heterogeneity can be biological, technical, or phenotype-driven.

## 12. From Locus to Biology

A GWAS hit is a starting point.

Post-GWAS interpretation can include:

- LD clumping to identify independent loci.
- Regional plots.
- Annotation of variants and nearby genes.
- Coding consequence lookup.
- eQTL and molecular QTL colocalization.
- Fine mapping.
- Gene-based tests.
- Pathway analysis.
- Literature review and GWAS Catalog lookup.
- Replication in independent cohorts.
- Functional validation.

For plant and crop studies, validation may include:

- Expression analysis.
- Near-isogenic lines.
- Gene editing.
- Candidate gene resequencing.
- Multi-environment trials.
- Marker-assisted selection tests.

For human biomedical studies, validation may include:

- Independent ancestry-matched replication.
- Phenome-wide association.
- Functional assays.
- Colocalization with eQTL, pQTL, or chromatin data.
- Mendelian randomization where assumptions are credible.

## 13. Polygenic Scores

A polygenic score sums trait-associated alleles weighted by effect estimates from a discovery GWAS.

Core workflow:

1. Choose discovery GWAS summary statistics.
2. Harmonize alleles to target genotypes.
3. Select or shrink variants.
4. Compute scores in an independent target dataset.
5. Evaluate prediction.
6. Report calibration, discrimination, uncertainty, and limitations.

Key cautions:

- Scores are not deterministic.
- Scores often transfer poorly across ancestry groups.
- Prediction does not imply mechanism.
- Clinical deployment requires independent validation and careful communication.

## 14. Reporting a GWAS

A strong GWAS report includes:

- Scientific question.
- Cohort or panel description.
- Inclusion and exclusion rules.
- Phenotype definition.
- Genotyping or sequencing method.
- Reference genome build.
- Sample and variant QC.
- Population structure and relatedness analysis.
- Association model and covariates.
- Multiple-testing correction.
- Software versions.
- Manhattan and QQ plots.
- Top loci table.
- Replication or validation.
- Limitations.
- Data and code availability where permitted.

## 15. Common Mistakes

- Treating the top SNP as the causal gene.
- Ignoring ancestry or relatedness.
- Using HWE filters where assumptions do not apply.
- Removing data without documenting why.
- Mixing genome builds.
- Forgetting allele harmonization.
- Reporting p-values without effect sizes.
- Interpreting Manhattan peaks without LD context.
- Treating polygenic scores as diagnostic certainty.
- Using public databases without checking ancestry, phenotype, and build compatibility.

## 16. Mental Model

Teach learners to move through GWAS as a chain of evidence:

```text
study question
-> phenotype quality
-> genotype quality
-> population structure and relatedness
-> association model
-> diagnostic plots
-> locus interpretation
-> replication
-> biological validation
-> transparent reporting
```

Weakness at any step weakens the final claim.

