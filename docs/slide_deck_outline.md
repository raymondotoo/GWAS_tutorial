# GWAS Slide Deck Outline

This is a slide-by-slide outline. It can be converted into PowerPoint, Keynote, Quarto, Marp, or Reveal.js.

## Module 1: Why GWAS?

### Slide 1: Title

Excellent GWAS Tutorial: From Raw Genotypes to Defensible Biological Interpretation

### Slide 2: The Core Question

Which genomic variants are associated with variation in a trait?

Use figure: GWAS analysis workflow.

### Slide 3: What GWAS Can Discover

- Trait-associated loci.
- Candidate biological pathways.
- Shared genetic architecture.
- Targets for follow-up experiments.
- Inputs for fine mapping and polygenic scores.

### Slide 4: What GWAS Cannot Prove Alone

- Causality.
- The causal gene by nearest distance.
- Complete heritability.
- Clinical actionability without validation.

## Module 2: GWAS Vocabulary

### Slide 5: SNPs and Alleles

Define SNP, genotype, effect allele, other allele, reference allele.

Use figure: Single-SNP association model.

### Slide 6: MAF and Power

Lower frequency means fewer carriers and less stable estimates.

### Slide 7: Linkage Disequilibrium

Variants travel together through inheritance; markers tag regions.

Use figure: Linkage disequilibrium heatmap.

### Slide 8: Manhattan Plot

Each point is a variant; peaks are loci to investigate.

Use figure: Manhattan and QQ diagnostic plots.

### Slide 9: QQ Plot

Observed versus expected p-values diagnose inflation, deflation, and signal.

## Module 3: Study Design

### Slide 10: Start With the Question

Trait, population, design, primary analysis.

### Slide 11: Phenotype Quality

No model rescues an incoherent phenotype.

### Slide 12: Human Study Designs

Case-control, cohort, EHR, biobank, family.

### Slide 13: Plant Study Designs

Diversity panels, breeding lines, field trials, treatment contrasts.

### Slide 14: Power

Sample size, MAF, effect size, phenotype quality, LD, multiple testing.

## Module 4: Data and File Formats

### Slide 15: Genotype Inputs

VCF, PLINK, PGEN, BGEN.

### Slide 16: Phenotype and Covariate Files

Sample IDs must match exactly.

### Slide 17: Genome Builds and Alleles

Build mismatches and strand errors can invalidate results.

## Module 5: Quality Control

### Slide 18: QC Is an Argument

Show the data are suitable for the claim.

### Slide 19: Sample QC

Missingness, heterozygosity, duplicates, relatedness, sex checks, ancestry.

### Slide 20: Variant QC

Missingness, MAF/MAC, HWE, differential missingness, strand, build.

### Slide 21: HWE With Care

HWE assumptions depend on the population and study design.

### Slide 22: Before and After Counts

Every filter needs a count and justification.

## Module 6: Structure and Relatedness

### Slide 23: Population Structure

Ancestry can confound genotype-trait association.

### Slide 24: PCA

Visualize structure and choose covariates.

Use figure: PCA population structure plot.

### Slide 25: Kinship

Related samples can inflate test statistics.

### Slide 26: Mixed Models

Model relatedness instead of pretending it is absent.

## Module 7: Association Testing

### Slide 27: Linear Regression

Quantitative trait model.

### Slide 28: Logistic Regression

Binary trait model.

### Slide 29: Covariates

Age, sex, batch, PCs, field block, treatment, site.

### Slide 30: Model Choice

PLINK, GEMMA, REGENIE, SAIGE, BOLT-LMM, TASSEL.

### Slide 31: Multiple Testing

Genome-wide significance and FDR.

Use figure: Multiple-testing schematic.

## Module 8: Interpreting Results

### Slide 32: Reading Manhattan Peaks

Peak shape, LD support, artifacts, known loci.

### Slide 33: Reading QQ Plots

Null bulk, lifted tail, inflation, deflation.

### Slide 34: Top Loci Table

SNP, position, effect allele, beta/OR, SE, p-value, MAF, imputation quality.

### Slide 35: Common Overclaims

Association is not causation; nearest gene is not proof.

## Module 9: Imputation and Meta-Analysis

### Slide 36: Why Impute?

Increase coverage and harmonize across arrays.

### Slide 37: Imputation Workflow

QC, harmonization, phasing, imputation, post-QC.

Use figure: Genotype imputation flow.

### Slide 38: Meta-Analysis

Combine cohorts after allele and phenotype harmonization.

### Slide 39: Heterogeneity

Differences can be biological or technical.

## Module 10: Post-GWAS

### Slide 40: From Variant to Locus

LD clumping and regional association.

Use figure: Regional association plot.

### Slide 41: Functional Annotation

Coding consequence, regulatory elements, eQTLs, pQTLs.

### Slide 42: Fine Mapping

Credible sets prioritize plausible causal variants.

### Slide 43: Colocalization

Do two association signals share a causal variant?

### Slide 44: Pathway and Gene Tests

Useful, but sensitive to annotation and assumptions.

## Module 11: Polygenic Scores

### Slide 45: What a PGS Is

Weighted sum of trait-associated alleles.

### Slide 46: Validation

Independent target dataset, calibration, discrimination, uncertainty.

### Slide 47: Transferability

Performance often drops across ancestry groups.

## Module 12: Reporting and Reproducibility

### Slide 48: Reproducible Project Structure

Data, scripts, results, logs, reports, environments.

### Slide 49: Reporting Checklist

Study design, QC, model, build, software, plots, limitations.

### Slide 50: Final Mental Model

Question -> phenotype -> genotype QC -> structure -> model -> plots -> locus -> replication -> report.
