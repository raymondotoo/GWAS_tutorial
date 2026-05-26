# Facilitator Guide

## Teaching Stance

GWAS is easy to run badly and difficult to interpret well. The best teaching posture is to slow learners down at each decision point:

- What is the scientific claim?
- What assumption is being made?
- What evidence supports that assumption?
- What could create a false signal?
- What would change your mind?

## Recommended Pacing

For a five-day workshop:

- Day 1: conceptual foundation, study design, and file inspection.
- Day 2: QC, PCA, ancestry, relatedness.
- Day 3: association models, multiple testing, plots.
- Day 4: imputation, meta-analysis, locus interpretation.
- Day 5: polygenic scores, reporting, capstone presentations.

For a one-day bootcamp:

- Morning: GWAS concepts, QC, population structure.
- Midday: association testing demo.
- Afternoon: plots, top loci, reporting pitfalls.

For a two-hour seminar:

- Spend 40 minutes on concepts.
- Spend 30 minutes on QC and population structure.
- Spend 30 minutes on association plots and interpretation.
- Spend 20 minutes on mistakes and reporting.

## Suggested Live Demo Arc

1. Show raw sample and variant counts.
2. Show missingness and allele-frequency summaries.
3. Run or display PCA.
4. Ask learners what covariates they would use.
5. Show association output columns.
6. Show Manhattan and QQ plots.
7. Pick one top locus and ask what can and cannot be concluded.

## Common Misconceptions

### "The top SNP is the gene."

Correction: the top SNP is a marker. It may tag a causal variant nearby through LD.

### "A low p-value proves causality."

Correction: a low p-value is evidence against the null association model, conditional on assumptions and data quality.

### "PCA solves ancestry."

Correction: PCA helps, but it does not automatically solve confounding, sampling imbalance, or lack of diversity.

### "HWE filtering is always required."

Correction: HWE assumptions depend on the population. In selected, structured, inbred, or plant breeding populations, HWE can be inappropriate.

### "More covariates are always better."

Correction: covariates should match the scientific model. Some variables can introduce bias if they are consequences of genotype or disease.

### "Polygenic scores are diagnostic."

Correction: scores estimate genetic liability or trait propensity under a model. They require independent validation and careful communication.

## Discussion Prompts

- Why might the same GWAS hit have different allele frequencies across populations?
- When would you remove related samples instead of using a mixed model?
- What makes a phenotype "GWAS-ready"?
- How would you design replication for a rare disease GWAS?
- How would plant field-trial design change the covariates?
- What does a clean QQ plot look like, and when can inflation be real biology?

## Assessment Ideas

### Quick Checks

- Define LD in one sentence.
- Explain why Manhattan plots need a genome-wide threshold.
- Name two causes of false positives.
- Explain why imputation quality matters.
- State why nearest gene is not enough.

### Applied Assessment

Give learners:

- A small GWAS result table.
- A Manhattan plot.
- A QQ plot.
- A PCA plot.

Ask them to write:

- Three concerns.
- Two strengths.
- One next analysis.
- One sentence that accurately reports the finding without overclaiming.

## Capstone Rubric

| Category | Excellent |
| --- | --- |
| Study question | Specific, testable, tied to population and phenotype |
| QC | Thresholds justified and counts reported |
| Structure | PCA and relatedness handled appropriately |
| Model | Trait type and covariates match design |
| Plots | Manhattan and QQ plots interpreted cautiously |
| Locus interpretation | LD, annotation, prior evidence, and replication considered |
| Reporting | Effect sizes, software versions, build, limitations included |

## Instructor Notes on Plant Versus Human GWAS

Plant GWAS often emphasizes:

- Diversity panels.
- Landraces.
- Breeding lines.
- Inbreeding.
- Field trials.
- Genotype-by-environment interaction.
- Candidate gene validation in crop improvement.

Human GWAS often emphasizes:

- Case-control or population cohort design.
- Medical phenotype definition.
- Relatedness and ancestry.
- Imputation reference panels.
- Biobank-scale models.
- Summary statistics.
- GWAS Catalog lookup.
- Fine mapping and polygenic scores.

The shared logic is association testing under careful control of confounding and multiple testing.

