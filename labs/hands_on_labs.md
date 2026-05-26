# Hands-On GWAS Labs

These labs are designed for a small teaching dataset. Replace file names with the actual dataset used in class.

The commands are examples, not a universal pipeline. Learners should understand why each command is run.

## Suggested Folder Layout

```text
project/
  data_raw/
  data_interim/
  data_processed/
  results/
  plots/
  logs/
  scripts/
  docs/
```

## Lab 1: Inspect Genotype and Phenotype Data

### Goal

Understand the data before filtering it.

### Inputs

- `data_raw/study.pgen`
- `data_raw/study.pvar`
- `data_raw/study.psam`
- `data_raw/phenotypes.tsv`

### Example Commands

```bash
plink2 \
  --pfile data_raw/study \
  --freq \
  --missing sample-only \
  --missing variant-only \
  --out results/01_initial
```

### Questions

- How many samples and variants are present?
- How many samples have phenotype data?
- Are there obvious missingness problems?
- What does the allele-frequency distribution look like?
- Are chromosome names and positions consistent?

### Deliverable

Write a short data-readiness note:

```text
The starting dataset contains N samples and M variants. The phenotype file contains K measured samples. Initial checks suggest...
```

## Lab 2: Sample and Variant QC

### Goal

Create a clean analysis dataset while documenting every exclusion.

### Example Commands

```bash
plink2 \
  --pfile data_raw/study \
  --mind 0.02 \
  --geno 0.02 \
  --maf 0.01 \
  --hwe 1e-6 \
  --make-pgen \
  --out data_processed/study_qc
```

For case-control data, apply HWE filters to controls where appropriate:

```bash
plink2 \
  --pfile data_raw/study \
  --keep controls.txt \
  --hwe 1e-6 \
  --write-snplist \
  --out data_interim/hwe_controls
```

### Questions

- How many samples were removed?
- How many variants were removed?
- Do thresholds make sense for this study design?
- Would HWE assumptions be appropriate for this population?

### Deliverable

Before/after table:

| Stage | Samples | Variants | Main reason |
| --- | ---: | ---: | --- |
| Raw |  |  |  |
| After sample missingness |  |  |  |
| After variant missingness |  |  |  |
| After MAF/MAC |  |  |  |
| Final |  |  |  |

## Lab 3: PCA and Population Structure

### Goal

Detect population structure and decide how to account for it.

### Example Commands

Prune variants for LD:

```bash
plink2 \
  --pfile data_processed/study_qc \
  --indep-pairwise 200 50 0.2 \
  --out results/03_prune
```

Run PCA:

```bash
plink2 \
  --pfile data_processed/study_qc \
  --extract results/03_prune.prune.in \
  --pca 20 approx \
  --out results/03_pca
```

### Questions

- Do samples cluster?
- Are phenotype groups unevenly distributed across PCs?
- Are batch or site labels aligned with PCs?
- How many PCs should enter the model?

### Deliverable

PCA plot and covariate plan.

## Lab 4: Relatedness and Kinship

### Goal

Identify duplicates, close relatives, and the need for mixed models.

### Example Commands

```bash
plink2 \
  --pfile data_processed/study_qc \
  --extract results/03_prune.prune.in \
  --king-cutoff 0.0884 \
  --make-pgen \
  --out data_processed/study_unrelated
```

### Questions

- Are close relatives expected in this study?
- Should related samples be removed or modeled?
- How would this decision differ in a plant breeding panel?

### Deliverable

Relatedness decision memo.

## Lab 5: Association Testing

### Goal

Run a basic association model and interpret the output.

### Quantitative Trait Example

```bash
plink2 \
  --pfile data_processed/study_unrelated \
  --pheno data_raw/phenotypes.tsv \
  --pheno-name trait_value \
  --covar results/03_pca.eigenvec \
  --covar-name PC1-PC10 \
  --glm hide-covar cols=+a1freq,+beta,+se,+ci,+tstat,+p \
  --out results/05_gwas_trait
```

### Binary Trait Example

```bash
plink2 \
  --pfile data_processed/study_unrelated \
  --pheno data_raw/phenotypes.tsv \
  --pheno-name case_status \
  --covar results/03_pca.eigenvec \
  --covar-name PC1-PC10 \
  --glm hide-covar firth-fallback cols=+a1freq,+orbeta,+se,+ci,+p \
  --out results/05_gwas_case_control
```

### Questions

- What is the effect allele?
- Is the reported effect a beta or odds ratio?
- Which covariates were included?
- How many variants were tested?
- What significance threshold will you use?

### Deliverable

Association results summary with top 10 variants.

## Lab 6: Manhattan and QQ Plots

### Goal

Diagnose association results visually.

### R Example

```r
library(data.table)
library(qqman)

gwas <- fread("results/05_gwas_trait.trait_value.glm.linear")

manhattan(
  gwas,
  chr = "CHROM",
  bp = "POS",
  snp = "ID",
  p = "P",
  genomewideline = -log10(5e-8),
  suggestiveline = -log10(1e-5)
)

qq(gwas$P)
```

### Questions

- Is there evidence of global inflation?
- Are top signals isolated or supported by neighboring variants?
- What additional QC checks would you run before trusting the result?

### Deliverable

One Manhattan plot, one QQ plot, and a short interpretation.

## Lab 7: Imputation Concept Lab

### Goal

Understand imputation without requiring a long production run.

### Discussion Workflow

```text
raw genotypes
-> pre-imputation QC
-> build and allele harmonization
-> phasing
-> imputation
-> post-imputation QC
-> association testing with dosage
```

### Questions

- Why is reference-panel matching important?
- What happens if genome builds are mixed?
- Why are palindromic A/T and C/G SNPs difficult?
- What imputation quality threshold will you use?

### Deliverable

Imputation readiness checklist for the teaching dataset.

## Lab 8: Locus Interpretation

### Goal

Turn a GWAS signal into a cautious biological hypothesis.

### Steps

1. Choose a lead SNP.
2. Define an LD window.
3. Identify nearby variants and genes.
4. Look up previous associations.
5. Check functional annotations.
6. Write a replication plan.

### Questions

- Is the nearest gene necessarily the causal gene?
- Is there evidence from expression, coding consequence, or previous GWAS?
- Is LD consistent with one signal or multiple signals?
- What experiment or independent dataset would validate this locus?

### Deliverable

Candidate-locus table:

| Item | Evidence |
| --- | --- |
| Lead SNP |  |
| Position |  |
| Effect allele |  |
| p-value |  |
| Nearby genes |  |
| LD support |  |
| Prior evidence |  |
| Proposed follow-up |  |

## Lab 9: Capstone Mini-Project

### Goal

Produce a complete GWAS report.

### Required Sections

- Scientific question.
- Data description.
- QC plan and results.
- PCA and relatedness assessment.
- Association model.
- Manhattan and QQ plots.
- Top loci table.
- Biological interpretation.
- Limitations.
- Next steps.

Use `templates/gwas_project_report.md`.

