# Five-Day GWAS Course Outline

This outline follows the spirit of the Physalia GWAS course structure while adding explicit beginner scaffolding from the local "Decoding basic GWAS" paper and a stronger practical workflow.

## Course Design Principles

- Move from intuition to implementation: every concept should eventually touch a plot, file, command, or modeling decision.
- Teach QC as scientific reasoning, not button pressing.
- Treat GWAS hits as hypotheses requiring biological interpretation and replication.
- Make ancestry, population structure, diversity, and generalizability central rather than optional.
- Use plant and human examples side by side so learners see which principles transfer and which assumptions change.

## Day 0: Preparation

Learner tasks before the workshop:

- Install software or use a prepared teaching container.
- Read a short GWAS overview.
- Review genotype file formats: VCF, PLINK BED/BIM/FAM, PGEN/PVAR/PSAM.
- Bring one trait example from their own field.
- Skim the visual guide chapter so the main plots and schematics feel familiar before the labs.

Instructor deliverables:

- Confirm compute access.
- Provide a small toy genotype dataset and phenotype file.
- Provide one cleaned GWAS summary statistics file for downstream interpretation labs.

## Day 1: GWAS Foundations

### Learning Goals

- Explain what a GWAS tests.
- Define SNP, allele, genotype, phenotype, MAF, LD, haplotype, effect allele, and p-value.
- Distinguish association from causation.
- Understand why study design matters before statistics.

### Lecture 1: The Core Question

GWAS asks whether genetic variation at many sites across the genome is statistically associated with variation in a trait. The typical single-SNP test asks:

`Does the expected phenotype differ by genotype after accounting for relevant covariates?`

For binary traits:

`Does genotype shift disease odds after accounting for covariates?`

Visuals to use:

- GWAS analysis workflow.
- Single-SNP association model.

### Lecture 2: Genetic Variation and LD

Topics:

- SNPs as markers, not always causal variants.
- LD as correlation among variants.
- Tag SNPs and why genotyping arrays work.
- Why LD patterns differ across populations and species.
- Why a significant SNP points to a genomic region, not automatically a gene.

Visuals to use:

- Linkage disequilibrium heatmap.
- Regional association plot.

### Lecture 3: Study Design

Topics:

- Case-control, quantitative trait, family, cohort, biobank, diversity panel, and breeding panel designs.
- Phenotype definition and measurement error.
- Sample size, effect size, allele frequency, and power.
- Environmental heterogeneity in plant and crop GWAS.
- Ethics, consent, privacy, and responsible communication.

### Lab 1: Inspect GWAS Data

Deliverables:

- Identify sample count, variant count, missingness, allele frequency distribution, and phenotype availability.
- Write a short "data readiness" memo.

## Day 2: Quality Control and Population Structure

### Learning Goals

- Build sample and variant QC rules.
- Interpret PCA, missingness, heterozygosity, relatedness, HWE, MAF, and call-rate metrics.
- Explain false positives from population structure and technical artifacts.

### Lecture 4: Sample QC

Topics:

- Sex checks where applicable.
- Missing genotype rate.
- Heterozygosity outliers.
- Duplicates and close relatives.
- Ancestry inference using PCA.
- Sample exclusions versus stratified analysis.

### Lecture 5: Variant QC

Topics:

- Variant missingness.
- MAF thresholds.
- Hardy-Weinberg equilibrium in appropriate contexts.
- Differential missingness.
- Ambiguous strand alleles.
- Build and reference-genome alignment.
- Filtering for imputation versus filtering for final association.

### Lecture 6: Population Structure and Kinship

Topics:

- PCA covariates.
- Kinship matrices.
- Cryptic relatedness.
- Linear mixed models.
- Structured crop panels and breeding lines.

Visuals to use:

- PCA population structure plot.

### Lab 2: Run QC and PCA

Deliverables:

- A QC flow diagram.
- PCA plot.
- Before/after variant and sample counts.
- Justification for every exclusion threshold.

## Day 3: Association Testing

### Learning Goals

- Choose a GWAS model based on trait type and sample structure.
- Run single-variant association tests.
- Interpret effect estimates, standard errors, p-values, and genomic inflation.
- Understand multiple-testing correction.

### Lecture 7: Regression Models

Topics:

- Linear regression for quantitative traits.
- Logistic regression for binary traits.
- Covariates: age, sex, batch, PCs, environment, field block, treatment, genotyping array.
- Additive genotype coding.
- Dominance and recessive models as secondary analyses.

### Lecture 8: Mixed Models and Large-Scale GWAS

Topics:

- Why relatedness inflates false positives.
- Linear mixed models for quantitative traits.
- Generalized mixed models for binary traits.
- Model choices: PLINK, GEMMA, GCTA, BOLT-LMM, REGENIE, SAIGE.
- Plant GWAS models: GLM, MLM, kinship, PCA correction.

### Lecture 9: Multiple Testing and Diagnostic Plots

Topics:

- Bonferroni and genome-wide significance.
- False discovery rate.
- Manhattan plots.
- QQ plots.
- Lambda GC and LDSC intercept.
- When inflation is signal, confounding, or both.

Visuals to use:

- Manhattan and QQ diagnostic plot.
- Multiple-testing schematic.

### Lab 3: Run Association and Make Plots

Deliverables:

- GWAS result table.
- Manhattan plot.
- QQ plot.
- Brief interpretation of top loci and diagnostics.

## Day 4: Imputation, Meta-Analysis, and Post-GWAS Interpretation

### Learning Goals

- Explain genotype imputation and its assumptions.
- Understand meta-analysis at a practical level.
- Move from associated variants to candidate biology.
- Use external databases responsibly.

### Lecture 10: Imputation

Topics:

- Pre-phasing and imputation.
- Reference panels.
- Imputation quality metrics.
- Allele harmonization.
- Why imputation performance depends on ancestry and reference panels.

Visuals to use:

- Genotype imputation flow.

### Lecture 11: Meta-Analysis and Summary Statistics

Topics:

- Fixed-effect and random-effect meta-analysis.
- Allele harmonization.
- Heterogeneity.
- Genomic control.
- Summary-statistic QC.
- Public summary statistics and reproducibility.

### Lecture 12: Post-GWAS

Topics:

- Regional plots and LD.
- Fine mapping and credible sets.
- Colocalization with eQTL or molecular QTL.
- Gene and pathway tests.
- Functional annotation.
- GWAS Catalog lookup.
- Plant/crop candidate-gene validation.

### Lab 4: Interpret a Locus

Deliverables:

- Regional association interpretation.
- Candidate gene table.
- Replication and validation plan.

## Day 5: Polygenic Scores, Reporting, and Capstone

### Learning Goals

- Explain polygenic scores and their limits.
- Produce a transparent GWAS report.
- Present a coherent analysis from QC through interpretation.

### Lecture 13: Polygenic Scores

Topics:

- Score construction from GWAS summary statistics.
- Clumping and thresholding.
- LD-aware methods.
- Training, tuning, validation, and target datasets.
- Transferability across ancestry groups.
- Clinical and breeding-use caution.

### Lecture 14: Reproducible GWAS

Topics:

- Project organization.
- Versioned software and reference files.
- Workflow systems.
- Containers and environments.
- Reporting checklists.
- Data governance and privacy.

### Capstone

Learners present:

- Study design.
- QC decisions.
- Association model.
- Key plots.
- Top findings.
- Limitations.
- Next-step validation.

## Assessment Rubric

Excellent submissions:

- State a clear scientific question.
- Define phenotype and sample inclusion rules.
- Justify QC thresholds.
- Use covariates that match the study design.
- Diagnose population structure and relatedness.
- Interpret plots without overclaiming.
- Separate marker association from causal inference.
- Propose replication and validation.
- Report software versions and reference builds.
