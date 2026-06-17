# Example: Unit Operation Guideline Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Process Engineer Agent structures an early-stage screening of unit operations against standard guidelines. It does not size lines or compressors.

## Scenario

A process line and a compressor operating point are reviewed against public line-velocity and operating-window guidelines.

Public synthetic inputs:

- Line fluid velocity: 12 m/s
- Mixture density: 50 kg/m^3
- Erosional C-factor: 122
- Maximum velocity guideline: 20 m/s
- Compressor operating flow: 1300 m3/h
- Compressor surge flow: 1000 m3/h
- Compressor stonewall flow: 2000 m3/h
- Minimum surge margin: 0.10
- Minimum stonewall margin: 0.05

## Screening Steps

1. Confirm the objective: preliminary guideline triage only.
2. Run `line-velocity-check` to estimate the erosional velocity and the velocity ratio against the guideline.
3. Run `compressor-operating-window-check` to estimate the surge and stonewall margins for the operating point.
4. Record the warning levels and the most important uncertainties.
5. List required follow-up studies.

## Expected Screening Output Outline

- Line velocity indicators (erosional velocity, velocity ratio, guideline ratio) and warning level
- Compressor operating-window indicators (surge margin, stonewall margin, limiting margin) and warning level
- Recommended validated NeqSim and standards workflows
- Required follow-up studies
- Assumptions, limitations, and human review checklist

## Required Follow-Up

- Validated line sizing and hydraulics per API RP 14E and NORSOK P-001 with real fluid properties.
- Validated compressor performance and anti-surge review per API 617 with vendor curves.
- NeqSim simulation of line conditions and compressor performance for confirmation.
- Qualified process engineering review before any decision.
