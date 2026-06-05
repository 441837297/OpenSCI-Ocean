# P01: Scale-Dependent Regime Transition in Submesoscale Air-Sea Coupling Revealed by SWOT

> Does air-sea coupling undergo a regime transition from mesoscale to submesoscale, and can SWOT SSH combined with geostationary SST and scatterometer winds reveal where and how the coupling physics changes?

## Status

| Item | Content |
|---|---|
| Current stage | 🔬 D0 Explore (候选 / candidate) |
| Lead / proposer | Kris19999 |
| Target journal | Nature Communications (primary); GRL (fallback if regime change signal is weak but scale dependence is significant) |
| Start date | 2026-06-05 |
| Expected submission | TBD |

## D0 Priority Checklist

- [ ] Download SWOT KaRIn L2 SSH for Gulf Stream and Kuroshio Extension pilot boxes; verify swath geometry, noise floor, and along-track/cross-track resolution
- [ ] Download concurrent GOES/Himawari SST and ASCAT winds; quantify collocation sample size (SWOT pass × clear-sky SST × scatterometer overlap)
- [ ] Compute scale-dependent coupling coefficient (wind speed gradient vs. SST gradient regression slope) as a function of spatial filter cutoff wavelength, using ASCAT + GOES SST as a quick prototype
- [ ] Literature search: existing work on scale-dependent air-sea coupling coefficients, especially any evidence of regime change or nonlinearity at submesoscales
- [ ] If collocation sample size < statistical threshold, evaluate whether ERA5 or CCMP can extend temporal coverage for the scale-dependence analysis, with SWOT providing the submesoscale ocean structure anchor

## Scientific Question

The mesoscale framework for air-sea coupling (Chelton et al. 2004; Small et al. 2008) describes a quasi-linear relationship: warm SST anomalies destabilize the atmospheric boundary layer, accelerating near-surface winds, with a roughly constant coupling coefficient across mesoscale wavelengths (100–500 km). But what happens when the ocean exhibits sharp fronts and filaments at submesoscale (2–50 km)?

This project asks whether the air-sea coupling coefficient is scale-invariant or undergoes a regime transition at submesoscales. Three possibilities exist:

1. **Continuity**: the mesoscale linear coupling framework extends smoothly to finer scales, and the coupling coefficient remains constant.
2. **Saturation or decay**: at sufficiently sharp fronts, the atmospheric boundary layer cannot adjust fast enough, and coupling weakens — the atmosphere becomes "blind" to the finest ocean structures.
3. **Regime change**: nonlinear boundary-layer responses (convective triggering, hydraulic jumps, secondary circulations) activate at sharp fronts, producing a qualitatively different coupling signature — altered coupling slope, phase shift, or cross-wind component emergence.

Possibility 1 is the null hypothesis. Possibilities 2 and 3 are both publishable, but 3 is the high-impact outcome that would warrant Nature Communications.

The Gulf Stream and Kuroshio Extension are the natural laboratories: they host the world's sharpest SST fronts co-located with energetic submesoscale SSH structures that SWOT can resolve.

## Hypotheses

1. The air-sea coupling coefficient (regression slope of wind speed anomaly on SST anomaly, binned by spatial scale) varies with wavelength and does not remain constant from mesoscale into submesoscale.
2. At wavelengths below a critical threshold (hypothesized 20–50 km), the coupling relationship changes character: the slope, coherence, or phase between wind and SST fields shifts detectably relative to the mesoscale regime.
3. SWOT SSH gradient magnitude is a better predictor of the regime boundary than SST gradient alone, because SSH integrates the dynamical structure (frontal jets, strain field) that controls the sharpness and persistence of surface temperature fronts.
4. The scale at which regime transition occurs differs between the Gulf Stream and Kuroshio Extension, reflecting differences in frontal sharpness, mixed-layer depth, and atmospheric background state.
5. In the submesoscale regime, wind anomalies show a cross-wind component relative to SST fronts (not purely downwind as in mesoscale pressure-adjustment coupling), indicating a shift from pressure-adjustment dominance to vertical-mixing or secondary-circulation dominance.

## Data

All datasets are public. Raw data must not be committed; only download scripts, access notes, and processed outputs are tracked.

**Primary datasets (the observational triad):**

- **SWOT KaRIn L2 Low Rate SSH** (PO.DAAC): submesoscale ocean structure — fronts, eddies, filaments, strain. This is the primary SWOT product with well-validated quality. Used to identify and characterize submesoscale ocean features, not as a wind source.
- **Geostationary SST**: high-frequency, cloud-permitting SST frontal structure.
  - GOES-East ABI SST / NOAA ACSPO (Gulf Stream sector)
  - Himawari-8/9 AHI SST (Kuroshio Extension sector)
- **ASCAT ocean vector winds** (MEaSUREs-OSVW, MetOp ASCAT): the atmospheric response field. Vector winds enable decomposition into downwind and crosswind components relative to SST fronts.

**Supporting datasets:**

- ERA5 10 m winds: gridded background for large-scale atmospheric state removal.
- CCMP ocean surface winds: optional comparison for scale sensitivity.
- SWOT L2 sigma0-derived wind speed: secondary product; used only if validated quality is confirmed, as an independent check at SWOT resolution.

## Method

### Pilot regions

- **Gulf Stream** (35–42°N, 75–55°W): GOES-East SST + SWOT SSH + ASCAT winds.
- **Kuroshio Extension** (30–40°N, 140–170°E): Himawari SST + SWOT SSH + ASCAT winds.

### Analysis framework

**Step 1: Collocation and quality control**

Collocate SWOT swaths, geostationary SST, and ASCAT winds within defined time windows (±1 h for SST, ±3 h for scatterometer). Apply cloud masking, rain flagging, and quality filters. Report final sample sizes.

**Step 2: Multi-scale decomposition**

Apply spatial filtering (Gaussian, Lanczos, or wavelet) at a series of cutoff wavelengths (10, 20, 50, 100, 200, 500 km) to separate the SST, SSH, and wind fields into scale bands. Sensitivity tests on filter choice.

**Step 3: Scale-dependent coupling coefficient (core diagnostic)**

For each scale band, compute:
- Regression slope: ∂U'/∂SST' (wind speed anomaly vs. SST anomaly) — the classic coupling coefficient
- Coherence: magnitude-squared coherence between SST gradient and wind speed gradient as a function of wavenumber
- Phase: phase angle between SST and wind fields — downwind coupling produces ~0° phase; cross-wind emergence shifts the phase

Plot all three quantities as functions of wavelength. The key figure: does the coupling coefficient curve show a break, plateau, or sign change in the submesoscale band?

**Step 4: SWOT SSH as a regime boundary predictor**

Condition the coupling analysis on SWOT SSH gradient magnitude:
- Partition observations into bins of SSH gradient strength (proxy for frontal sharpness and dynamical intensity)
- Test whether the scale of regime transition shifts as a function of SSH gradient — sharper fronts may trigger regime change at larger wavelengths

**Step 5: Downwind vs. crosswind decomposition**

Using ASCAT vector winds and SST front orientation (from geostationary SST gradient direction):
- Decompose wind anomalies into front-parallel and front-perpendicular components
- At mesoscale, expect dominant downwind (pressure-adjustment) signal
- At submesoscale, test for emergence of crosswind component (vertical-mixing or secondary-circulation signal)

**Step 6: Gulf Stream vs. Kuroshio comparison**

Compare the regime transition wavelength, coupling coefficient curves, and crosswind emergence between the two basins. Interpret differences in terms of frontal sharpness, mixed-layer depth climatology, and atmospheric stability.

**Step 7: Control regions**

Repeat the coupling analysis in weak-gradient regions (e.g., subtropical gyres, 20–25°N) to confirm that regime transition signatures are absent where submesoscale fronts are weak.

## Expected Outputs

- D0 feasibility note: data access verification, collocation statistics, literature landscape, and prototype coupling coefficient curve (ASCAT + GOES, before SWOT integration).
- Candidate figures for the manuscript:
  1. **Scale-dependent coupling coefficient curve** for Gulf Stream and Kuroshio Extension, showing the mesoscale-to-submesoscale transition (the "money figure").
  2. **Coherence and phase spectra** between SST and wind fields as functions of wavenumber, with the regime boundary marked.
  3. **SWOT SSH gradient conditioning**: how frontal dynamical intensity modulates the transition wavelength.
  4. **Downwind vs. crosswind decomposition** showing emergence of crosswind coupling at submesoscales.
  5. **Gulf Stream vs. Kuroshio comparison** of transition characteristics.
  6. **Control region null result**: flat coupling coefficient curve in weak-gradient regions.
- Reproducible Python scripts for all analyses.

## Feasibility and Risks

**Critical risks:**

- The regime transition may not exist — the coupling may be smoothly scale-invariant or simply decay monotonically. This would rule out NC but still support a GRL paper on the scale dependence itself.
- Collocation sample size between SWOT, clear-sky geostationary SST, and scatterometer passes may be small. Mitigation: extend temporal baseline, use ERA5 as supplementary wind field, prioritize high-coverage seasons.
- ASCAT resolution (~25 km) limits the smallest scales accessible for wind-SST coupling. The analysis can characterize coupling down to ~25 km from the wind side, while SWOT SSH extends ocean structure identification to ~2 km. The gap between 2–25 km must be discussed honestly.

**Manageable risks:**

- Geostationary SST cloud contamination: mitigate with multi-pass composites and quality flags.
- Atmospheric variability (synoptic storms, frontal passages) can mask coupling signals: conditional sampling on atmospheric stability and large-scale wind speed.
- Causal attribution (ocean drives atmosphere vs. atmosphere drives ocean) is inherently difficult from observations alone. Use lead-lag analysis exploiting geostationary SST temporal resolution, and frame claims carefully.
- AI-generated references must be manually verified.

**Pivot strategy:**

If regime transition is not detected but scale-dependent coupling is clear, pivot to GRL with the story: "Submesoscale air-sea coupling weakens below X km — implications for coupled model parameterization."

## Contributor Role

The proposer has worked on ocean submesoscale processes from the master's stage to the present, is affiliated with a National Science Fund for Distinguished Young Scholars team, and has published three related papers in JGR and Ocean Modelling. The proposer can contribute domain-expert AI review, physical interpretation, figure processing, reference verification, and manuscript-level scientific correction, especially for submesoscale dynamics and submesoscale air-sea interaction.

## Progress Log

| Date | Stage | Content | Output |
|---|---|---|---|
| 2026-06-05 | D0 | Participant submitted initial topic proposal (wind KE distribution + coupling) | Original README |
| 2026-06-05 | D0 | Reviewed and reshaped toward scale-dependent regime transition framing | Revised README |

## AI Interaction Log

See `logs/2026-06-05_D0_topic_proposal.md`.

## References

See `literature/literature_seed.md` for a seed list. Key framing references to verify:

- Chelton et al. (2004) — mesoscale SST-wind coupling framework
- Small et al. (2008) — air-sea interaction at mesoscale: review
- Renault et al. (2016, 2019) — current feedback and eddy killing
- Gaube et al. (2015) — SST-wind coupling and eddy-induced Ekman pumping
- Schneider & Qiu (2015) — SST fronts and atmospheric boundary layer adjustment

Each reference must be manually checked before citation.
