# GWAS Project Report Template

## 1. Project Title

Write a specific title:

```text
Genome-wide association study of [trait] in [population/panel/cohort]
```

## 2. Scientific Question

State the primary question in one paragraph.

## 3. Study Population or Panel

- Source:
- Inclusion criteria:
- Exclusion criteria:
- Sample size before QC:
- Sample size after QC:
- Ancestry/population/panel description:
- Ethical/data-use notes:

## 4. Phenotype

- Trait name:
- Trait type: binary, quantitative, ordinal, time-to-event, count, other.
- Measurement method:
- Units:
- Case/control definition if applicable:
- Transformations:
- Missingness:
- Outlier handling:
- Environmental or batch variables:

## 5. Genotype Data

- Genotyping or sequencing platform:
- Genome build:
- File format:
- Initial variant count:
- Imputed or directly genotyped:
- Reference panel if imputed:

## 6. Quality Control

### Sample QC

| Filter | Threshold | Removed | Remaining | Rationale |
| --- | --- | ---: | ---: | --- |
| Missingness |  |  |  |  |
| Heterozygosity |  |  |  |  |
| Relatedness |  |  |  |  |
| Ancestry/population outliers |  |  |  |  |
| Other |  |  |  |  |

### Variant QC

| Filter | Threshold | Removed | Remaining | Rationale |
| --- | --- | ---: | ---: | --- |
| Missingness |  |  |  |  |
| MAF/MAC |  |  |  |  |
| HWE |  |  |  |  |
| Imputation quality |  |  |  |  |
| Other |  |  |  |  |

## 7. Population Structure and Relatedness

Describe:

- PCA findings.
- Relatedness findings.
- Decisions about exclusions, stratification, or mixed models.
- Number of PCs used as covariates.

Insert PCA plot:

```text
[PCA plot here]
```

## 8. Association Model

- Software and version:
- Model:
- Trait:
- SNP coding:
- Covariates:
- Relatedness handling:
- Multiple-testing threshold:

Example:

```text
We tested each SNP using linear regression under an additive genetic model, adjusting for age, sex, genotyping batch, and the first 10 genetic PCs.
```

## 9. Diagnostic Plots

Insert Manhattan plot:

```text
[Manhattan plot here]
```

Insert QQ plot:

```text
[QQ plot here]
```

Interpretation:

- Manhattan plot:
- QQ plot:
- Inflation/deflation:
- Follow-up checks:

## 10. Top Results

| SNP | Chr | Position | Effect allele | Other allele | EAF | Effect | SE | P | Nearest gene | Notes |
| --- | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

## 11. Locus Interpretation

For each lead locus:

- LD region:
- Nearby genes:
- Functional annotation:
- Prior GWAS evidence:
- Biological plausibility:
- Alternative explanations:
- Replication status:

## 12. Limitations

Discuss:

- Sample size.
- Phenotype quality.
- Population diversity.
- Genotyping or imputation limitations.
- Confounding.
- Multiple testing.
- Generalizability.
- Lack of functional validation.

## 13. Replication and Validation Plan

- Replication dataset:
- Harmonization needs:
- Statistical model:
- Functional validation:
- Expected challenges:

## 14. Reproducibility

- Code location:
- Workflow manager:
- Software versions:
- Reference files:
- Random seeds if applicable:
- Date run:

## 15. Conclusion

Write a cautious conclusion that distinguishes association, evidence, and next steps.

