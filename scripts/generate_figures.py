#!/usr/bin/env python3
"""Generate original SVG figures for the GWAS tutorial book.

The figures are synthetic teaching diagrams. They are not copied from any
paper, webpage, or the local PDF.
"""

from __future__ import annotations

import math
import random
from pathlib import Path
from xml.sax.saxutils import escape


OUT = Path("figures")

COLORS = {
    "ink": "#1f2933",
    "muted": "#52616b",
    "grid": "#d9e2ec",
    "bg": "#f8fafc",
    "blue": "#2563eb",
    "teal": "#0f766e",
    "green": "#16a34a",
    "amber": "#d97706",
    "red": "#dc2626",
    "purple": "#7c3aed",
    "slate": "#64748b",
}


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
  <style>
    .title {{ font: 700 22px Arial, sans-serif; fill: {COLORS['ink']}; }}
    .label {{ font: 600 14px Arial, sans-serif; fill: {COLORS['ink']}; }}
    .small {{ font: 12px Arial, sans-serif; fill: {COLORS['muted']}; }}
    .axis {{ stroke: {COLORS['ink']}; stroke-width: 1.4; }}
    .grid {{ stroke: {COLORS['grid']}; stroke-width: 1; }}
    .box {{ fill: white; stroke: {COLORS['grid']}; stroke-width: 1.3; rx: 8; }}
    .arrow {{ stroke: {COLORS['muted']}; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }}
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0 0, 8 3.5, 0 7" fill="{COLORS['muted']}"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="{COLORS['bg']}"/>
{body}
</svg>
"""


def text(x: float, y: float, value: str, cls: str = "small", anchor: str = "middle") -> str:
    value = escape(value)
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{value}</text>'


def rect(x: float, y: float, w: float, h: float, fill: str = "white", stroke: str = COLORS["grid"], rx: float = 8) -> str:
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>'


def line(x1: float, y1: float, x2: float, y2: float, cls: str = "axis") -> str:
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>'


def circle(x: float, y: float, r: float, fill: str, opacity: float = 1.0, stroke: str = "none") -> str:
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" opacity="{opacity:.2f}" stroke="{stroke}"/>'


def path(d: str, fill: str = "none", stroke: str = COLORS["ink"], width: float = 1.4, opacity: float = 1.0) -> str:
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width:.1f}" opacity="{opacity:.2f}"/>'


def write(name: str, content: str) -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(content)


def workflow() -> None:
    steps = [
        ("Question", "Trait, cohort, design"),
        ("Phenotype", "Measure and clean"),
        ("Genotype", "Array, WGS, GBS"),
        ("QC + PCA", "Samples, variants, PCs"),
        ("Model", "Regression or mixed model"),
        ("Plots", "Manhattan and QQ"),
        ("Biology", "LD, genes, validation"),
    ]
    body = [text(40, 40, "GWAS analysis workflow", "title", "start")]
    x0, y, w, h, gap = 34, 92, 116, 78, 20
    palette = [COLORS["blue"], COLORS["teal"], COLORS["green"], COLORS["amber"], COLORS["purple"], COLORS["red"], COLORS["slate"]]
    for i, (head, sub) in enumerate(steps):
        x = x0 + i * (w + gap)
        body.append(rect(x, y, w, h, fill="white", stroke=palette[i], rx=8))
        body.append(f'<circle cx="{x + 20}" cy="{y + 21}" r="11" fill="{palette[i]}" opacity="0.9"/>')
        body.append(text(x + 20, y + 26, str(i + 1), "label", "middle").replace(COLORS["ink"], "white"))
        body.append(text(x + w / 2, y + 38, head, "label"))
        body.append(text(x + w / 2, y + 59, sub, "small"))
        if i < len(steps) - 1:
            body.append(f'<line x1="{x + w + 5}" y1="{y + h / 2}" x2="{x + w + gap - 5}" y2="{y + h / 2}" class="arrow"/>')
    body.append(text(40, 220, "The central teaching point: each later result is only as credible as the earlier design and QC decisions.", "small", "start"))
    write("gwas_workflow.svg", svg(1010, 260, "\n".join(body)))


def snp_association() -> None:
    body = [text(34, 40, "Single-SNP association test", "title", "start")]
    body.append(rect(36, 70, 300, 170))
    body.append(text(60, 100, "DNA marker", "label", "start"))
    body.append(line(62, 136, 300, 136, "grid"))
    positions = [80, 118, 156, 194, 232, 270]
    bases = ["A", "C", "G", "T", "A", "C"]
    for x, b in zip(positions, bases):
        color = COLORS["red"] if x == 194 else COLORS["blue"]
        body.append(circle(x, 136, 17, color, 0.9))
        body.append(text(x, 141, b, "label").replace(COLORS["ink"], "white"))
    body.append(text(194, 184, "Tested SNP", "label"))
    body.append(text(194, 204, "Genotype coded 0, 1, 2 effect alleles", "small"))

    body.append(rect(380, 70, 390, 170))
    body.append(text(405, 100, "Association model", "label", "start"))
    body.append(text(405, 128, "phenotype = baseline + SNP effect + covariates + error", "small", "start"))
    body.append(text(405, 158, "Continuous trait: linear regression", "small", "start"))
    body.append(text(405, 181, "Binary trait: logistic regression", "small", "start"))
    body.append(text(405, 204, "Related samples: mixed model", "small", "start"))

    chart_x, chart_y = 820, 210
    body.append(line(820, 210, 820, 88))
    body.append(line(820, 210, 980, 210))
    body.append(text(900, 236, "0       1       2", "small"))
    body.append(text(802, 112, "trait", "small"))
    for gx, mean, color in [(845, 172, COLORS["blue"]), (900, 145, COLORS["teal"]), (955, 118, COLORS["red"])]:
        random.seed(int(gx))
        for _ in range(12):
            px = gx + random.uniform(-12, 12)
            py = mean + random.uniform(-16, 16)
            body.append(circle(px, py, 4, color, 0.72))
        body.append(line(gx - 18, mean, gx + 18, mean))
    body.append(text(900, 72, "Effect estimate", "label"))
    body.append(path("M845 172 L955 118", stroke=COLORS["ink"], width=2.4))
    write("snp_association_model.svg", svg(1020, 270, "\n".join(body)))


def ld_heatmap() -> None:
    body = [text(34, 40, "Linkage disequilibrium block", "title", "start")]
    x0, y0, cell = 150, 78, 34
    random.seed(8)
    n = 12
    for i in range(n):
        body.append(text(x0 + i * cell + cell / 2, y0 - 14, f"SNP{i+1}", "small"))
    for i in range(n):
        body.append(text(x0 - 22, y0 + i * cell + 22, f"SNP{i+1}", "small", "end"))
        for j in range(i + 1):
            dist = abs(i - j)
            block_bonus = 0.35 if (i // 4) == (j // 4) else 0
            r2 = max(0, min(1, 1.0 - dist * 0.18 + block_bonus + random.uniform(-0.08, 0.08)))
            red = int(245 - 80 * r2)
            green = int(245 - 170 * r2)
            blue = int(245 - 190 * r2)
            fill = f"rgb({red},{green},{blue})"
            x = x0 + j * cell
            y = y0 + i * cell
            body.append(f'<rect x="{x}" y="{y}" width="{cell - 2}" height="{cell - 2}" fill="{fill}" stroke="white" stroke-width="1"/>')
    body.append(rect(650, 95, 250, 255))
    body.append(text(675, 130, "How to read it", "label", "start"))
    body.append(text(675, 162, "Darker cells mean higher r2", "small", "start"))
    body.append(text(675, 190, "Blocks suggest inherited haplotypes", "small", "start"))
    body.append(text(675, 218, "A lead SNP can tag nearby variants", "small", "start"))
    body.append(text(675, 246, "LD patterns differ by ancestry", "small", "start"))
    body.append(text(675, 274, "and by species or breeding history", "small", "start"))
    for k, val in enumerate([0.0, 0.25, 0.5, 0.75, 1.0]):
        red = int(245 - 80 * val)
        green = int(245 - 170 * val)
        blue = int(245 - 190 * val)
        body.append(f'<rect x="{675 + k*32}" y="315" width="28" height="18" fill="rgb({red},{green},{blue})" stroke="none"/>')
    body.append(text(675, 350, "low", "small", "start"))
    body.append(text(835, 350, "high LD", "small", "end"))
    write("ld_heatmap.svg", svg(960, 520, "\n".join(body)))


def pca_plot() -> None:
    body = [text(34, 40, "PCA exposes population structure", "title", "start")]
    x0, y0, w, h = 88, 75, 680, 360
    body.append(line(x0, y0 + h, x0 + w, y0 + h))
    body.append(line(x0, y0 + h, x0, y0))
    for k in range(1, 5):
        body.append(line(x0, y0 + h - k * h / 5, x0 + w, y0 + h - k * h / 5, "grid"))
        body.append(line(x0 + k * w / 5, y0, x0 + k * w / 5, y0 + h, "grid"))
    random.seed(9)
    clusters = [
        (260, 285, COLORS["blue"], "Group A"),
        (490, 185, COLORS["teal"], "Group B"),
        (610, 315, COLORS["amber"], "Group C"),
    ]
    for cx, cy, color, _ in clusters:
        for _ in range(70):
            px = random.gauss(cx, 42)
            py = random.gauss(cy, 28)
            body.append(circle(px, py, 4.2, color, 0.56))
    for cx, cy, color, label in clusters:
        body.append(circle(cx, cy, 8, color, 0.95))
        body.append(text(cx + 16, cy - 10, label, "label", "start"))
    body.append(text(x0 + w / 2, 470, "PC1", "label"))
    body.append(text(40, y0 + h / 2, "PC2", "label"))
    body.append(rect(800, 105, 210, 220))
    body.append(text(825, 140, "Teaching cue", "label", "start"))
    body.append(text(825, 172, "If cases and controls", "small", "start"))
    body.append(text(825, 195, "separate by ancestry,", "small", "start"))
    body.append(text(825, 218, "a naive GWAS can", "small", "start"))
    body.append(text(825, 241, "find ancestry markers", "small", "start"))
    body.append(text(825, 264, "instead of trait loci.", "small", "start"))
    write("pca_population_structure.svg", svg(1060, 520, "\n".join(body)))


def manhattan_qq() -> None:
    random.seed(12)
    body = [text(34, 40, "Manhattan and QQ diagnostic plots", "title", "start")]
    # Manhattan panel
    mx, my, mw, mh = 70, 95, 590, 300
    body.append(rect(44, 70, 650, 370))
    body.append(line(mx, my + mh, mx + mw, my + mh))
    body.append(line(mx, my + mh, mx, my))
    for k in range(1, 6):
        body.append(line(mx, my + mh - k * mh / 6, mx + mw, my + mh - k * mh / 6, "grid"))
    n_chr = 8
    points = []
    for c in range(n_chr):
        for i in range(90):
            x = mx + (c + (i / 90)) * mw / n_chr
            yval = random.expovariate(0.9)
            if c == 2 and 40 < i < 58:
                yval += 3.5 + random.random() * 2.2
            if c == 5 and 66 < i < 75:
                yval += 2.2 + random.random() * 1.5
            yval = min(8.4, yval)
            y = my + mh - yval / 8.8 * mh
            color = COLORS["blue"] if c % 2 == 0 else COLORS["teal"]
            points.append((x, y, color, yval))
    for x, y, color, yval in points:
        body.append(circle(x, y, 2.4, color, 0.75))
    sig_y = my + mh - 7.3 / 8.8 * mh
    sug_y = my + mh - 5.0 / 8.8 * mh
    body.append(f'<line x1="{mx}" y1="{sig_y:.1f}" x2="{mx+mw}" y2="{sig_y:.1f}" stroke="{COLORS["red"]}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    body.append(f'<line x1="{mx}" y1="{sug_y:.1f}" x2="{mx+mw}" y2="{sug_y:.1f}" stroke="{COLORS["amber"]}" stroke-width="1.4" stroke-dasharray="5 4"/>')
    body.append(text(mx + mw / 2, 424, "Chromosome position", "small"))
    body.append(text(34, 235, "-log10(p)", "small", "start"))
    body.append(text(mx + 420, sig_y - 8, "genome-wide threshold", "small", "start"))
    for c in range(n_chr):
        body.append(text(mx + (c + 0.5) * mw / n_chr, my + mh + 22, str(c + 1), "small"))

    # QQ panel
    qx, qy, qw, qh = 770, 95, 270, 270
    body.append(rect(725, 70, 350, 370))
    body.append(line(qx, qy + qh, qx + qw, qy + qh))
    body.append(line(qx, qy + qh, qx, qy))
    for k in range(1, 5):
        body.append(line(qx, qy + qh - k * qh / 5, qx + qw, qy + qh - k * qh / 5, "grid"))
        body.append(line(qx + k * qw / 5, qy, qx + k * qw / 5, qy + qh, "grid"))
    body.append(path(f"M{qx} {qy+qh} L{qx+qw} {qy}", stroke=COLORS["grid"], width=2.2))
    for i in range(90):
        ex = i / 89 * 5.2
        obs = ex + max(0, ex - 3.2) ** 1.6 * 0.35 + random.uniform(-0.05, 0.08)
        px = qx + ex / 5.4 * qw
        py = qy + qh - min(5.4, obs) / 5.4 * qh
        body.append(circle(px, py, 3.0, COLORS["purple"], 0.74))
    body.append(text(qx + qw / 2, 424, "Expected -log10(p)", "small"))
    body.append(text(733, 235, "Observed", "small", "start"))
    body.append(text(902, 70, "QQ plot", "label"))
    write("manhattan_qq_diagnostics.svg", svg(1120, 470, "\n".join(body)))


def imputation_flow() -> None:
    body = [text(34, 40, "Genotype imputation fills untyped markers", "title", "start")]
    body.append(rect(50, 82, 260, 245))
    body.append(text(80, 118, "Observed study genotypes", "label", "start"))
    body.append(text(80, 145, "Typed SNPs are sparse", "small", "start"))
    for row, y in enumerate([185, 215, 245, 275]):
        body.append(line(88, y, 268, y, "grid"))
        for x in [100, 160, 240]:
            body.append(circle(x, y, 8, [COLORS["blue"], COLORS["teal"], COLORS["amber"]][(x + row) % 3], 0.85))
        for x in [130, 190, 215]:
            body.append(circle(x, y, 4, COLORS["grid"], 0.65))

    body.append(rect(390, 82, 260, 245))
    body.append(text(420, 118, "Reference panel", "label", "start"))
    body.append(text(420, 145, "Dense haplotypes provide context", "small", "start"))
    for row, y in enumerate([185, 215, 245, 275]):
        body.append(line(428, y, 608, y, "grid"))
        for idx, x in enumerate([440, 470, 500, 530, 560, 590]):
            body.append(circle(x, y, 6, [COLORS["blue"], COLORS["teal"], COLORS["amber"], COLORS["red"]][(idx + row) % 4], 0.8))

    body.append(rect(730, 82, 280, 245))
    body.append(text(760, 118, "Imputed dosage data", "label", "start"))
    body.append(text(760, 145, "Untyped variants receive probabilities", "small", "start"))
    for row, y in enumerate([185, 215, 245, 275]):
        body.append(line(768, y, 960, y, "grid"))
        for idx, x in enumerate([780, 812, 844, 876, 908, 940]):
            opacity = 0.95 if idx in (0, 2, 5) else 0.45
            body.append(circle(x, y, 7, [COLORS["blue"], COLORS["teal"], COLORS["amber"], COLORS["red"]][(idx + row) % 4], opacity))
    body.append('<line x1="320" y1="205" x2="375" y2="205" class="arrow"/>')
    body.append('<line x1="660" y1="205" x2="715" y2="205" class="arrow"/>')
    body.append(text(420, 365, "After imputation, filter by imputation quality, allele frequency, and ancestry-matched performance.", "small", "start"))
    write("imputation_flow.svg", svg(1060, 410, "\n".join(body)))


def regional_locus() -> None:
    random.seed(22)
    body = [text(34, 40, "Regional association plot: from lead SNP to locus", "title", "start")]
    x0, y0, w, h = 82, 78, 760, 315
    body.append(line(x0, y0 + h, x0 + w, y0 + h))
    body.append(line(x0, y0 + h, x0, y0))
    for k in range(1, 5):
        body.append(line(x0, y0 + h - k * h / 5, x0 + w, y0 + h - k * h / 5, "grid"))
    lead_pos = 0.55
    for i in range(170):
        pos = i / 169
        ld = max(0, 1 - abs(pos - lead_pos) / 0.28 + random.uniform(-0.1, 0.1))
        yval = random.expovariate(0.7) + ld * 4.8
        yval = min(8.2, yval)
        x = x0 + pos * w
        y = y0 + h - yval / 8.5 * h
        if ld > 0.72:
            color = COLORS["red"]
        elif ld > 0.45:
            color = COLORS["amber"]
        elif ld > 0.2:
            color = COLORS["teal"]
        else:
            color = COLORS["blue"]
        body.append(circle(x, y, 4.0, color, 0.78))
    lx = x0 + lead_pos * w
    ly = y0 + h - 8.0 / 8.5 * h
    body.append(circle(lx, ly, 7, COLORS["red"], 1.0, stroke=COLORS["ink"]))
    body.append(text(lx + 12, ly - 12, "lead SNP", "label", "start"))
    body.append(text(x0 + w / 2, 426, "Genomic position near locus", "small"))
    body.append(text(36, 230, "-log10(p)", "small", "start"))

    # Gene track
    gy = 460
    genes = [(130, 230, "GENE1", COLORS["slate"]), (300, 520, "GENE2", COLORS["teal"]), (570, 780, "GENE3", COLORS["purple"])]
    body.append(text(84, gy - 22, "Gene track", "label", "start"))
    for gx1, gx2, name, color in genes:
        body.append(f'<rect x="{gx1}" y="{gy}" width="{gx2-gx1}" height="14" fill="{color}" opacity="0.82"/>')
        body.append(f'<polygon points="{gx2},{gy-5} {gx2+16},{gy+7} {gx2},{gy+19}" fill="{color}" opacity="0.82"/>')
        body.append(text((gx1 + gx2) / 2, gy + 40, name, "small"))

    body.append(rect(880, 110, 210, 250))
    body.append(text(908, 145, "Interpretation", "label", "start"))
    body.append(text(908, 177, "Color shows LD with", "small", "start"))
    body.append(text(908, 200, "the lead variant.", "small", "start"))
    body.append(text(908, 230, "The nearest gene is", "small", "start"))
    body.append(text(908, 253, "only a hypothesis.", "small", "start"))
    body.append(text(908, 283, "Use annotation,", "small", "start"))
    body.append(text(908, 306, "fine mapping, and", "small", "start"))
    body.append(text(908, 329, "replication.", "small", "start"))
    write("regional_locus_plot.svg", svg(1120, 540, "\n".join(body)))


def multiple_testing() -> None:
    random.seed(32)
    body = [text(34, 40, "Multiple testing: why GWAS thresholds are strict", "title", "start")]
    x0, y0, w, h = 84, 92, 760, 310
    body.append(line(x0, y0 + h, x0 + w, y0 + h))
    body.append(line(x0, y0 + h, x0, y0))
    body.append(text(x0 + w / 2, 438, "Many independent SNP tests", "small"))
    body.append(text(32, 245, "p-value", "small", "start"))
    threshold_y = y0 + 70
    body.append(f'<line x1="{x0}" y1="{threshold_y}" x2="{x0+w}" y2="{threshold_y}" stroke="{COLORS["red"]}" stroke-width="2" stroke-dasharray="6 5"/>')
    body.append(text(x0 + w - 10, threshold_y - 10, "genome-wide threshold", "small", "end"))
    for i in range(260):
        x = x0 + i / 260 * w
        p = random.random()
        y = y0 + h - (1 - p) * h
        color = COLORS["slate"]
        if y < threshold_y:
            color = COLORS["red"]
        body.append(circle(x, y, 2.5, color, 0.72))
    body.append(rect(880, 112, 210, 205))
    body.append(text(910, 150, "Teaching cue", "label", "start"))
    body.append(text(910, 183, "With a million tests,", "small", "start"))
    body.append(text(910, 207, "nominal p < 0.05", "small", "start"))
    body.append(text(910, 231, "creates many false", "small", "start"))
    body.append(text(910, 255, "discoveries by chance.", "small", "start"))
    body.append(text(910, 290, "Control the family", "small", "start"))
    body.append(text(910, 314, "of tests, not one test.", "small", "start"))
    write("multiple_testing.svg", svg(1120, 480, "\n".join(body)))


def main() -> None:
    workflow()
    snp_association()
    ld_heatmap()
    pca_plot()
    manhattan_qq()
    imputation_flow()
    regional_locus()
    multiple_testing()
    print(f"Wrote SVG figures to {OUT}")


if __name__ == "__main__":
    main()
