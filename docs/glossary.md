# GWAS Glossary

## Allele

One version of a genetic variant. In a GWAS table, always identify the effect allele before interpreting direction of effect.

## Association

A statistical relationship between genotype and phenotype. Association does not by itself prove causation.

## Base Pair Position

The coordinate of a variant on a reference genome build. Positions are build-specific, so mixing builds creates errors.

## Beta

The estimated change in a quantitative trait per copy of the effect allele under an additive model.

## Case-Control GWAS

A GWAS where the phenotype is binary, usually coded as affected versus unaffected.

## Covariate

A variable included in the model to account for design, confounding, or precision. Examples include age, sex, batch, site, PCs, treatment, or field block.

## Dosage

Expected allele count from imputed genotype data. Dosage can take fractional values between 0 and 2.

## Effect Allele

The allele for which the effect estimate is reported. A positive beta means the trait increases per copy of this allele.

## Fine Mapping

Post-GWAS analysis that prioritizes likely causal variants within an associated locus, often using LD and association strength.

## Genomic Inflation

A pattern where association statistics are larger than expected under the null. It can arise from confounding, relatedness, technical artifacts, or true polygenicity.

## Genotype

The pair of alleles an individual carries at a variant. In GWAS, often coded as 0, 1, or 2 copies of the effect allele.

## Genome Build

The reference genome coordinate system, such as GRCh37, GRCh38, or a crop-specific reference assembly.

## GWAS Catalog

A curated database of published human GWAS associations.

## Hardy-Weinberg Equilibrium

Expected genotype frequencies under random mating and no evolutionary pressures. HWE checks can detect genotyping problems, but assumptions may not hold in structured or selected populations.

## Haplotype

A combination of alleles inherited together on the same chromosome segment.

## Imputation

Prediction of untyped genotypes using observed genotypes and a reference panel.

## Kinship Matrix

A matrix describing genetic relatedness among individuals. Mixed models use kinship to control relatedness.

## Lambda GC

A summary of genomic inflation based on the median test statistic. It is useful but can be misleading in very large or highly polygenic studies.

## Linkage Disequilibrium

Correlation between variants. LD makes a SNP useful as a marker for nearby variants, but it also complicates causal interpretation.

## Manhattan Plot

A genome-wide plot of variant position versus `-log10(p-value)`. Peaks highlight associated loci.

## Minor Allele Frequency

The frequency of the less common allele in the analyzed sample.

## Mixed Model

A model that includes fixed effects, such as SNP and covariates, plus random effects, often to account for relatedness.

## Odds Ratio

The multiplicative change in disease odds per copy of the effect allele in logistic regression.

## Phenotype

The measured trait or outcome used in association testing.

## Polygenic Score

A weighted sum of trait-associated alleles. It estimates genetic liability or trait propensity under a model and requires independent validation.

## Population Structure

Systematic genetic differences among subgroups. If correlated with phenotype, population structure can create false associations.

## Principal Components

Axes of genetic variation used to summarize ancestry or structure.

## QQ Plot

A plot comparing observed p-values to expected p-values under the null.

## Regional Association Plot

A plot showing association strength near a lead SNP, often colored by LD.

## SNP

A single-nucleotide polymorphism, or one-base genetic variant.

## Summary Statistics

GWAS results released without individual-level genotype data. Usually include SNP, alleles, effect estimate, standard error, p-value, frequency, and sample size.

## Variant Call Rate

The proportion of samples with a called genotype at a variant.

