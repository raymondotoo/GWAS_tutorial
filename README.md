# Excellent GWAS Tutorial

This repository is a Markdown-first course package for teaching genome-wide association studies (GWAS) from first principles through practical analysis, interpretation, and reporting.

The design combines three anchors:

- The local paper `01_Decoding_Basic_GWAS.pdf`, which is a beginner-friendly, plant/crop GWAS overview.
- The Physalia GWAS course outline, which gives a strong multi-day teaching progression.
- Current high-quality public resources from PLINK, GWAS Catalog, PGS Catalog, GWASTutorial, Hail, Beagle, Snakemake, LDSC, REGENIE, GEMMA, and reporting-methods literature.

The material is original synthesis. It uses the source materials for structure, terminology, workflow choices, and reading recommendations, but does not copy their prose.

## Audience

This course is meant for graduate students, research staff, clinicians, computational biologists, plant breeders, and analysts who want to understand and run a GWAS responsibly.

Learners should ideally know:

- Basic genetics: chromosomes, alleles, SNPs, genotype, phenotype.
- Basic statistics: p-values, regression, multiple testing.
- Basic command line use.
- Optional but helpful: R or Python.

## Learning Outcomes

By the end, learners should be able to:

1. Explain what GWAS can and cannot infer.
2. Describe SNPs, linkage disequilibrium, minor allele frequency, population structure, relatedness, imputation, and association testing.
3. Build a defensible quality-control plan for samples, variants, and phenotypes.
4. Choose an association model for binary, quantitative, related, structured, or large-biobank data.
5. Interpret Manhattan plots, QQ plots, genomic inflation, effect estimates, confidence intervals, and regional association plots.
6. Move from significant loci to biological hypotheses using annotation, LD, credible sets, GWAS Catalog, functional resources, and replication.
7. Understand differences between human/biomedical GWAS and plant/crop GWAS.
8. Report a GWAS transparently using reproducible workflows and reporting checklists.

## Package Contents

- [docs/course_outline.md](docs/course_outline.md): five-day course structure with lectures, labs, deliverables, and capstone.
- [docs/core_tutorial.md](docs/core_tutorial.md): main teaching notes for the full tutorial.
- [labs/hands_on_labs.md](labs/hands_on_labs.md): practical lab sequence with example commands and expected outputs.
- [docs/qc_and_analysis_checklists.md](docs/qc_and_analysis_checklists.md): decision checklists for QC, modeling, interpretation, and reporting.
- [docs/facilitator_guide.md](docs/facilitator_guide.md): instructor guidance, pacing, common misconceptions, and assessment ideas.
- [docs/slide_deck_outline.md](docs/slide_deck_outline.md): slide-by-slide outline that can be converted into lectures.
- [docs/source_map.md](docs/source_map.md): curated bibliography and source map.
- [templates/gwas_project_report.md](templates/gwas_project_report.md): report template for student projects.
- [templates/Snakefile.gwas](templates/Snakefile.gwas): small workflow skeleton for reproducible GWAS projects.
- [templates/config.example.yaml](templates/config.example.yaml): example config for the workflow skeleton.
- [docs/glossary.md](docs/glossary.md): beginner-friendly GWAS glossary.
- [docs/assessment_bank.md](docs/assessment_bank.md): quizzes, interpretation prompts, and capstone checks.
- [environment.yml](environment.yml): suggested teaching environment.

## Recommended Teaching Flow

For a short seminar, use:

1. `docs/core_tutorial.md` sections 1 to 5.
2. `docs/qc_and_analysis_checklists.md`.
3. `labs/hands_on_labs.md` labs 1, 2, 5, and 6.

For a full workshop, use:

1. The five-day plan in `docs/course_outline.md`.
2. All labs in order.
3. The report template as a capstone.

For a plant-breeding audience, emphasize:

- Population panels, landraces, breeding lines, kinship, field-trial design, environmental effects, genotype-by-environment interaction, and candidate-gene validation.

For a human/biomedical audience, emphasize:

- Case-control design, ancestry, relatedness, imputation reference panels, mixed models, biobank-scale methods, GWAS Catalog lookup, fine mapping, colocalization, and polygenic scores.

## Source Note

The Dropbox PDF was checked at:

`/Users/raymondotoo/Barrow Neurological Institute Dropbox/Raymond Otoo/GWAS_Tutorial/01_Decoding_Basic_GWAS.pdf`

It initially appeared as a 0-byte Dropbox placeholder, then hydrated to a 557,038-byte, 9-page PDF. Its extracted title is:

`Decoding basic GWAS: The beginner's guide`

Authors: Shinde CS, Andhale GR, Thange VB, and Bhosale BR. Published in `International Journal of Advanced Biochemistry Research`, 2024.
