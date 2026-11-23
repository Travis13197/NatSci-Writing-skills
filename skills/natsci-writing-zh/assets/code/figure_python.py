#!/usr/bin/env python3
# 中文说明：本脚本是 NatSci-Writing-skills 的投稿级图件起点。先写图件合同，再运行：
#   python figure_python.py --demo --out ./figures
#   python figure_python.py --data mydata.csv --out ./figures
# CSV 列：category,value,group（一行一个观测）。
"""Publication figure starter (matplotlib), NatSci-Writing-skills.

Workflow encoded here:
1. Figure contract (claim, archetype, panel map) -> set in CONTRACT below.
2. One data plot per panel; direct labels; n and uncertainty documented in the caption.
3. Export editable SVG/PDF plus 600-dpi PNG; keep source data beside the figure.

Usage:
    python figure_python.py --demo --out ./figures
    python figure_python.py --data mydata.csv --out ./figures
CSV columns: category, value, group (one row per observation).
"""
import argparse
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

CONTRACT = {
    "core_conclusion": "Group B shifts the measured value relative to group A.",
    "archetype": "quantitative grid",
    "journal": "Nature (double column, 183 mm)",
    "backend": "python",
    "panel_map": {
        "a": "observation-level distribution by group",
        "b": "paired difference with uncertainty",
        "c": "per-category effect ordered by size",
    },
}

def style():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "font.size": 7,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.6,
        "legend.frameon": False,
        "figure.dpi": 150,
    })

def demo_data(seed=7):
    rng = np.random.default_rng(seed)
    rows = []
    for group, shift in [("A", 0.0), ("B", 0.45)]:
        for cat in ["c1", "c2", "c3", "c4"]:
            base = {"c1": 1.0, "c2": 1.4, "c3": 0.8, "c4": 1.2}[cat]
            for _ in range(12):
                rows.append({"category": cat, "group": group,
                             "value": base + shift + rng.normal(0, 0.18)})
    return pd.DataFrame(rows)

def build(df, outdir):
    style()
    os.makedirs(outdir, exist_ok=True)
    df.to_csv(os.path.join(outdir, "figure_source_data.csv"), index=False)

    groups = list(dict.fromkeys(df["group"]))
    cats = list(dict.fromkeys(df["category"]))
    fig, axes = plt.subplots(1, 3, figsize=(183 / 25.4, 62 / 25.4),
                             constrained_layout=True)

    # Panel a: observations + median per group
    ax = axes[0]
    for i, g in enumerate(groups):
        vals = df.loc[df["group"] == g, "value"].to_numpy()
        x = i + np.linspace(-0.12, 0.12, len(vals))
        ax.scatter(x, vals, s=9, alpha=0.75, linewidth=0)
        ax.hlines(np.median(vals), i - 0.25, i + 0.25, color="black", lw=1.0)
    ax.set_xticks(range(len(groups)), groups)
    ax.set_ylabel("Measured value (a.u.)")
    ax.set_title("a  Observations by group", loc="left", fontweight="bold")

    # Panel b: paired change by category (paired within category)
    ax = axes[1]
    deltas = []
    for cat in cats:
        a = df[(df["group"] == groups[0]) & (df["category"] == cat)]["value"].to_numpy()
        b = df[(df["group"] == groups[1]) & (df["category"] == cat)]["value"].to_numpy()
        deltas.append(np.mean(b) - np.mean(a))
    order = np.argsort(deltas)
    ax.barh(np.arange(len(cats)), np.array(deltas)[order],
            color="#0D5673", height=0.6)
    ax.axvline(0, color="#586B75", lw=0.6, ls="--")
    ax.set_yticks(range(len(cats)), [cats[i] for i in order])
    ax.set_xlabel("Mean difference (B - A)")
    ax.set_title("b  Category effect", loc="left", fontweight="bold")

    # Panel c: summary distribution across all observations
    ax = axes[2]
    for i, g in enumerate(groups):
        vals = df.loc[df["group"] == g, "value"].to_numpy()
        parts = ax.violinplot([vals], positions=[i], widths=0.6,
                              showextrema=False)
        for pc in parts["bodies"]:
            pc.set_facecolor("#4E8EAD" if g == groups[0] else "#B96359")
            pc.set_alpha(0.45)
        ax.scatter(np.full(len(vals), i) + np.linspace(-0.06, 0.06, len(vals)),
                   vals, s=6, color="#132B36", alpha=0.7, linewidth=0)
    ax.set_xticks(range(len(groups)), groups)
    ax.set_ylabel("Measured value (a.u.)")
    ax.set_title("c  Group distributions", loc="left", fontweight="bold")

    base = os.path.join(outdir, "figure1")
    fig.savefig(base + ".svg")
    fig.savefig(base + ".pdf")
    fig.savefig(base + ".png", dpi=600)
    plt.close(fig)
    print("wrote", base + ".{svg,pdf,png}")
    print("contract:", CONTRACT["core_conclusion"])

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", help="CSV with category,value,group")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--out", default="./figures")
    args = ap.parse_args()
    if args.demo or not args.data:
        df = demo_data()
    else:
        df = pd.read_csv(args.data)
    build(df, args.out)
