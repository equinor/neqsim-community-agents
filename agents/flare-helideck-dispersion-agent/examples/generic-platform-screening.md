# Example: Generic Platform, Unignited Flare Gas and Helideck Flight Paths

This example uses public, synthetic data only. It shows how the Flare-Helideck Dispersion Agent structures the study. It does not size relief systems and does not replace CFD.

## Scenario

A hypothetical platform has a flare tip at 124 m ASL and a helideck at 76 m ASL, 240 m away on bearing 240 deg T. The obstacle-free sector is 135-345 deg T. The wind record is synthetic. Three release cases are considered: one rated PSV discharge, a warm blowdown and a cold dense blowdown (150 kg/s each).

## Steps

1. **Freeze the basis.** Geometry and sector as above; flight paths are the radial default (5 deg bearing step, 5 deg climb, 1 NM) and are declared assumptions; criteria are 10 % and 20 % LFL, with the source to be taken from the project design basis and flagged as open.
2. **Wind statistics.** The installation weather agent provides an hourly speed and direction record; the joint table is built from it. In this example the synthetic record is used.
3. **Release rates.** The rated capacity of the PSV orifice comes from the API 520 critical-flow equation in the toolkit; the blowdown peaks are supplied inputs.
4. **Run.** The example script of the skill runs the chain:

```bash
<python> examples/generic_platform_example.py output_dir
```

5. **Review.** The review checklist in `AGENT.md` is worked through: stable-air limits applied, Gaussian versus free-jet distance, 5 deg bearings, 1.0 m/s lowest bin, tilt scan 20-70 deg, neutral stability scheme, speed-bin contributions, no wake.
6. **Figures and results.** Twelve page-width figures and `results_fragment.json` are written.
7. **CFD hand-off.** `cfd_handoff` lists the worst condition of each case; CFD is recommended for the cold dense case at light wind and for the flattened-tip case.

## Expected Output Outline

- Peak % LFL at the helideck, the into-wind path and any flight path, per case
- Exceedance hours at 10 % and 20 % LFL, given a release, by speed bin
- Tilt scan, tornado and Monte Carlo spread (seed recorded)
- Review log, assumptions, data gaps, human review checklist

## Required Follow-Up

- The agent does not perform a quantitative risk assessment or CFD.
- The agent does not replace relief and flare design or the helideck operations manual.
- The agent does not use confidential layouts, flight paths or wind records.
