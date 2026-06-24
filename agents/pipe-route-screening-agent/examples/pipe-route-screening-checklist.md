# Example: Pipe Route Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Pipe Route Screening Agent screens a candidate route. It does not design routes or pipelines.

## Scenario

A candidate route is screened for elevation profile, pressure drop, velocity, and hydrate margin.

Public synthetic inputs:

- Route waypoints (distance, lateral, depth): (0, 0, 120), (4000, 800, 300), (8000, 1500, 340)
- Fluid density: 850 kg/m^3
- Fluid viscosity: 0.0012 Pa.s
- Flow rate: 0.05 m^3/s
- Pipe inner diameter: 0.25 m
- Recommended pressure gradient: 0.25 bar/km
- Erosional velocity limit and recommended velocity limit per the velocity skill defaults
- Operating temperature: 8 degC
- Hydrate equilibrium temperature: 14 degC
- Hydrate margin guideline: 3 degC

## Screening Steps

1. Confirm the objective: preliminary pipe-route triage only.
2. Run `pipe-route-profile` to build the along-route horizontal and elevation profile and screen route slope.
3. Run `pressure-drop-screening` to estimate the single-phase pressure drop and compare against the recommended gradient.
4. Run `line-velocity-check` to screen the line velocity against erosional and recommended limits.
5. Run `hydrate-margin-check` to screen the hydrate temperature margin against the guideline.
6. Record the warning levels and the most important uncertainties.
7. List required follow-up studies.

## Expected Screening Output Outline

- Route length and elevation profile with a slope warning level
- Pressure-drop indicator against the recommended gradient with a warning level
- Line-velocity indicator against erosional and recommended limits with a warning level
- Hydrate-margin indicator with a warning level
- Recommended validated NeqSim, NORSOK P-002, and GPSA workflows
- Assumptions, limitations, and a human review checklist

This output is an educational screening outline only and requires qualified human review before any design or operating decision.
