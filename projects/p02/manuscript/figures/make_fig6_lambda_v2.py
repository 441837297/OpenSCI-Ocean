"""Fig.6 (v2): magnitude-based Λ fails at all scales; resonance-window Λ₂
organizes per-event amplitude loss in the TIW zone.

a — V1 zone-mean Λ vs amplitude ratio: no discrimination (all Λ = 5-8).
b — scale dependence: zone-mean Λ vs along-ray Λ_min collapse to ~1 in all
    zones; magnitude criteria carry no zone information at any scale.
c — Λ₂ (resonance-window) vs amplitude ratio: TIW-zone events ordered by
    resonant TIW power (seasonality); islands uncorrelated (focusing-
    dominated).
"""
import json
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42, "font.size": 7,
    "axes.spines.right": False, "axes.spines.top": False,
    "axes.linewidth": 0.6, "legend.frameon": False,
})

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(BASE, "manuscript", "figures")
GL = os.path.join(BASE, "data", "glorys")

with open(os.path.join(GL, "lambda_event_zone.json")) as f:
    lam_zone = json.load(f)
with open(os.path.join(GL, "lambda_along_ray.json")) as f:
    lam_ray = json.load(f)
with open(os.path.join(GL, "lambda_v2_resonance.json")) as f:
    lam_v2 = json.load(f)
with open(os.path.join(BASE, "data", "duacs", "robustness_metrics_v2.json")) as f:
    rob_data = json.load(f)

MIN_RMS_UP = 0.01
rob_kelvin = {(r["event"], r["zone"]): r for r in rob_data["kelvin"]
              if r["rms_up"] > MIN_RMS_UP}

zone_colors = {"Gilbert Islands": "#27AE60", "Line Islands": "#2980B9",
               "TIW zone": "#E74C3C"}
zone_markers = {"Gilbert Islands": "o", "Line Islands": "s", "TIW zone": "D"}
zones = list(zone_colors)

fig, axes = plt.subplots(1, 3, figsize=(7.09, 2.7))

# --- (a) V1 zone-mean Λ vs amplitude ratio: no discrimination ---
ax = axes[0]
for ld in lam_zone:
    key = (ld["event_id"], ld["zone"])
    if key not in rob_kelvin:
        continue
    ax.scatter(ld["lambda"], rob_kelvin[key]["amp_ratio"],
               c=zone_colors[ld["zone"]], marker=zone_markers[ld["zone"]],
               s=28, alpha=0.85, edgecolors="k", linewidths=0.3,
               label=ld["zone"], zorder=3)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), fontsize=5.5, loc="upper left")
ax.axhline(1.0, color="grey", linewidth=0.6, linestyle="--", alpha=0.5)
ax.set_xlabel(r"Zone-mean $\Lambda$ (V1)", fontsize=7)
ax.set_ylabel("Amplitude ratio (dn/up)", fontsize=7)
ax.set_xlim(0, 9)
ax.text(-0.18, 1.02, "a", transform=ax.transAxes, fontsize=10,
        fontweight="bold", va="top")

# --- (b) scale dependence: zone-mean vs along-ray Λ collapse ---
ax = axes[1]
rng = np.random.default_rng(42)
for i, zone in enumerate(zones):
    zm = [ld["lambda"] for ld in lam_zone if ld["zone"] == zone]
    ar = [ld["lambda_min"] for ld in lam_ray if ld["zone"] == zone]
    for vals, dx, filled in [(zm, -0.16, True), (ar, 0.16, False)]:
        jit = rng.normal(0, 0.04, len(vals))
        ax.scatter(np.full(len(vals), i + dx) + jit, vals,
                   s=18, marker=zone_markers[zone],
                   facecolors=zone_colors[zone] if filled else "none",
                   edgecolors=zone_colors[zone], linewidths=0.7,
                   alpha=0.85, zorder=3)
ax.axhline(1.0, color="grey", linewidth=0.8, linestyle=":", alpha=0.7)
ax.text(-0.42, 1.13, r"$\Lambda_c \sim 1$", fontsize=6, color="grey",
        style="italic")
ax.set_yscale("log")
ax.set_xticks(range(3))
ax.set_xticklabels(["Gilbert\nIslands", "Line\nIslands", "TIW\nzone"],
                   fontsize=6)
ax.set_ylabel(r"$\Lambda$", fontsize=8)
ax.scatter([], [], s=18, marker="o", facecolors="grey", edgecolors="grey",
           label="zone-mean (V1)")
ax.scatter([], [], s=18, marker="o", facecolors="none", edgecolors="grey",
           label=r"along-ray $\Lambda_\mathrm{min}$")
ax.legend(fontsize=5.5, loc="center right")
ax.text(-0.18, 1.02, "b", transform=ax.transAxes, fontsize=10,
        fontweight="bold", va="top")

# --- (c) Λ₂ resonance criterion vs amplitude ratio ---
ax = axes[2]
pairs = []
for ld in lam_v2:
    key = (ld["event_id"], ld["zone"])
    if key not in rob_kelvin:
        continue
    amp = rob_kelvin[key]["amp_ratio"]
    pairs.append((ld["lambda_v2"], amp, ld["zone"]))
    ax.scatter(ld["lambda_v2"], amp,
               c=zone_colors[ld["zone"]], marker=zone_markers[ld["zone"]],
               s=28, alpha=0.85, edgecolors="k", linewidths=0.3, zorder=3)

tiw = [(x, y) for x, y, z in pairs if z == "TIW zone"]
tx, ty = np.log([p[0] for p in tiw]), np.log([p[1] for p in tiw])
r_tiw, p_tiw = stats.pearsonr(tx, ty)
slope, intercept = np.polyfit(tx, ty, 1)
xfit = np.linspace(min(tx), max(tx), 20)
ax.plot(np.exp(xfit), np.exp(slope * xfit + intercept),
        color=zone_colors["TIW zone"], linewidth=0.9, alpha=0.7, zorder=2)
rho_all, p_all = stats.spearmanr(np.log([p[0] for p in pairs]),
                                 np.log([p[1] for p in pairs]))
ax.set_xscale("log"), ax.set_yscale("log")
ax.axhline(1.0, color="grey", linewidth=0.6, linestyle="--", alpha=0.5)
ax.set_xlabel(r"$\Lambda_2$ (resonance window)", fontsize=7)
ax.set_ylabel("Amplitude ratio (dn/up)", fontsize=7)
ax.text(0.97, 0.04,
        (f"all: $\\rho$ = {rho_all:.2f} (p = {p_all:.2f}, n = {len(pairs)})\n"
         f"TIW: r = {r_tiw:.2f} (p = {p_tiw:.2f}, n = {len(tiw)})"),
        transform=ax.transAxes, fontsize=6, ha="right", va="bottom")
ax.text(-0.18, 1.02, "c", transform=ax.transAxes, fontsize=10,
        fontweight="bold", va="top")

plt.tight_layout(w_pad=1.2)
fig.savefig(os.path.join(OUT, "fig6_lambda.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(OUT, "fig6_lambda.png"), dpi=300, bbox_inches="tight")
plt.close()
print("Fig.6 v2 saved (3 panels: V1 fail / scale collapse / Lambda2 validation)")
