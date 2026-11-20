# Example Prompts

These prompts use public, synthetic data only. They are intended for early-stage screening.

## Full Screening Study

```text
Screen unignited flare gas reaching a helideck for a hypothetical platform: flare tip 124 m ASL, helideck 76 m ASL, 240 m away on bearing 240 deg T, obstacle-free sector 135-345 deg T. Use a synthetic hourly wind record and three cases (one rated PSV discharge, a warm blowdown and a cold blowdown at 150 kg/s). Report peak % LFL at the helideck, the into-wind path and any flight path, the share of wind hours above 10 % and 20 % LFL given a release, and the tip-inclination scan. State every exceedance as conditional on a release.
```

## Facility Screening (any receptors)

```text
Screen a hypothetical facility with a flare tip (85 m ASL, inclined 30 deg) and a cold vent (60 m ASL, vertical). Receptors: a combustion-air intake at (55, -30) m and 40 m ASL, a muster area (60..90, -90..-60) m at 12 m ASL, an escape route along three vertices and a crane cab. Use a synthetic wind record and a cold blowdown at 60 kg/s from the flare and 8 kg/s from the vent. Rank the receptors by the share of wind hours above 20 % LFL given a release, report the inclination scan and list the CFD conditions. State every exceedance as conditional on a release.
```

## Independent Review

```text
Review a flare, vent or helideck dispersion run against the review checklist: stable-air limits, Gaussian versus free-jet distance, bearing and route sampling, receptor heights and criterion sources, lowest-bin speed, inclination scan, stability scheme sensitivity, speed-bin contributions and the missing platform wake and building effects. List what fails and what to rerun.
```

## CFD Hand-Off

```text
From a completed dispersion run, list the worst conditions per case and receptor with source terms and receptor coordinates, and recommend which conditions to hand to CFD. State that the screening result is not a CFD result.
```

## Annual Figure Request

```text
I need the annual frequency of flight-path exposure to unignited flare gas. Explain what is missing and what the study can state without a flame-out frequency.
```
