# Curated Source Map

This file lists the materials pooled into the tutorial and how each one is used. Prefer primary documentation and peer-reviewed methods papers for technical claims.

## Local Source

### Shinde et al. 2024: Decoding Basic GWAS

- Local path: `/Users/raymondotoo/Barrow Neurological Institute Dropbox/Raymond Otoo/GWAS_Tutorial/01_Decoding_Basic_GWAS.pdf`
- DOI: https://doi.org/10.33545/26174693.2024.v8.i10Ss.2783
- Used for: beginner framing, plant/crop GWAS examples, SNP/LD/MAF/Manhattan/QQ/population-structure concepts, QTL versus GWAS comparison, and plant-oriented applications.

## Course Structure

### Physalia GWAS Course

- URL: https://www.physalia-courses.org/courses-workshops/course49/
- Used for: five-day progression covering GWAS foundations, QC, population structure, imputation, association testing, interpretation, and downstream analysis.

## Introductory GWAS Overviews

### NHGRI Genome-Wide Association Studies

- URL: https://www.genome.gov/genetics-glossary/Genome-Wide-Association-Studies
- Used for: accessible conceptual definition of GWAS.

### Uffelmann et al. 2021, Nature Reviews Methods Primers

- Title: Genome-wide association studies.
- URL: https://www.nature.com/articles/s43586-021-00056-9
- Used for: modern overview of GWAS concepts, study design, interpretation, and applications.

## QC and Practical GWAS Tutorials

### Marees et al. 2018

- Title: A tutorial on conducting genome-wide association studies: Quality control and statistical analysis.
- PubMed: https://pubmed.ncbi.nlm.nih.gov/29484742/
- Tutorial repository: https://github.com/MareesAT/GWA_tutorial
- Used for: QC workflow, statistical-analysis teaching structure, and practical beginner-friendly sequencing of steps.

### GWASTutorial

- URL: https://cloufield.github.io/GWASTutorial/
- Used for: practical workflow structure, GWAS file handling, QC, imputation, association analysis, and downstream interpretation.

## Visual References

### Wikimedia Commons Manhattan Plot

- URL: https://commons.wikimedia.org/wiki/File:Manhattan_Plot.png
- License: Creative Commons Attribution 2.5 Generic.
- Used for: reference example of a Manhattan plot layout and open-license attribution pattern. The book uses an original synthetic Manhattan plot rather than copying this image.

### FinnGen Handbook: QQ and Manhattan Plots

- URL: https://docs.finngen.fi/faq/about-pheweb/what-are-qq-and-manhattan-plots
- Used for: teaching framing around good versus problematic Manhattan plots, QQ-plot inflation/deflation, and interpretation of diagnostic plots.

### GWASLab Manhattan, QQ, and Regional Plot Docs

- Manhattan and QQ URL: https://cloufield.github.io/gwaslab/visualization_mqq/
- Regional plot URL: https://cloufield.github.io/gwaslab/RegionalPlot/
- Used for: reference examples of modern GWAS visualization types, including Manhattan, QQ, and regional locus plots.

## Software Documentation

### PLINK 2

- URL: https://www.cog-genomics.org/plink/2.0/
- Tutorials: https://www.cog-genomics.org/plink/2.0/tutorials/
- Used for: command examples, file formats, QC operations, PCA, and association testing.

### PLINK 1.9

- URL: https://www.cog-genomics.org/plink/1.9/
- Used for: classic GWAS command patterns still seen in many tutorials and legacy pipelines.

### Hail

- URL: https://hail.is/docs/0.2/tutorials/01-genome-wide-association-study.html
- Used for: scalable matrix-based GWAS concepts and cloud-scale teaching option.

### Beagle 5.5

- URL: https://faculty.washington.edu/browning/beagle/beagle.html
- Used for: imputation and phasing context.

### Snakemake

- URL: https://snakemake.readthedocs.io/
- Used for: reproducible workflow principles.

### REGENIE

- URL: https://rgcgithub.github.io/regenie/
- Used for: large-scale GWAS and two-step whole-genome regression model context.

### GEMMA

- URL: https://github.com/genetics-statistics/GEMMA
- Used for: linear mixed model context and relatedness-aware association.

### SAIGE

- URL: https://saigegit.github.io/SAIGE-doc/
- Used for: binary trait, case-control imbalance, and mixed-model context.

### TASSEL

- URL: https://www.maizegenetics.net/tassel
- Used for: plant GWAS context, association mapping, kinship, and LD analysis.

## Databases and Post-GWAS Resources

### GWAS Catalog

- URL: https://www.ebi.ac.uk/gwas/
- Documentation: https://www.ebi.ac.uk/gwas/docs
- Used for: prior association lookup and downstream annotation.

### PGS Catalog

- URL: https://www.pgscatalog.org/
- Documentation: https://www.pgscatalog.org/rest/
- Used for: polygenic-score interpretation and score metadata.

### LDSC

- URL: https://github.com/bulik/ldsc
- Used for: distinguishing inflation from confounding versus polygenicity, and genetic correlation.

### FUMA

- URL: https://fuma.ctglab.nl/
- Used for: functional mapping and annotation of GWAS results.

### LocusZoom

- URL: https://my.locuszoom.org/
- Used for: regional association plot examples.

### Open Targets Genetics

- URL: https://genetics.opentargets.org/
- Used for: variant-to-gene evidence and trait-locus exploration.

## Reporting, Interpretation, and Equity

### STREGA

- URL: https://www.strobe-statement.org/extensions/
- Used for: reporting expectations for genetic association studies.

### Popejoy and Fullerton 2016

- Title: Genomics is failing on diversity.
- URL: https://www.nature.com/articles/538161a
- Used for: discussion of representation, equity, and generalizability in human genomics.

### Sirugo, Williams, and Tishkoff 2019

- Title: The Missing Diversity in Human Genetic Studies.
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7380073/
- Used for: ancestry diversity, risk-prediction transferability, and why globally diverse cohorts matter.

### Duncan et al. 2019

- Title: Analysis of polygenic risk score usage and performance in diverse human populations.
- URL: https://www.nature.com/articles/s41467-019-11112-0
- Used for: polygenic score transferability and diversity cautions.

## Suggested Reading Order

1. NHGRI overview for plain-language intuition.
2. Shinde et al. for beginner plant/crop framing.
3. Marees et al. for hands-on QC and analysis.
4. PLINK 2 documentation for commands.
5. Uffelmann et al. for modern methodological framing.
6. GWAS Catalog and post-GWAS resources for interpretation.
7. PGS Catalog and diversity literature for polygenic-score limitations.
