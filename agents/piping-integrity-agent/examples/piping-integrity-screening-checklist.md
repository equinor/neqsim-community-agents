# Example: Line Integrity Guideline Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Piping Integrity Agent structures an early-stage screening of a line against standard guidelines. It does not size lines or validate mechanical design.

## Scenario

A process line is reviewed against public line-velocity, pressure-drop, wall-thickness, and flow-induced vibration guidelines.

Public synthetic inputs:

- Line fluid velocity: 12 m/s
- Mixture density: 50 kg/m^3
- Erosional C-factor: 122
- Maximum velocity guideline: 20 m/s
- Line length: 150 m
- Inside diameter: 0.2 m
- Darcy friction factor: 0.018
- Pressure-gradient guideline: 0.5 bar per 100 m
- Design pressure: 50 bar
- Outside diameter: 219.1 mm
- Allowable stress: 138 MPa
- Nominal wall thickness: 8.18 mm
- Flow-induced vibration velocity: 12 m/s
- Flow-induced vibration density: 50 kg/m^3

## Screening Steps

1. Confirm the objective: preliminary integrity triage only.
2. Run `line-velocity-check` to estimate the erosional velocity and the velocity ratio against the guideline.
3. Run `pressure-drop-screening` to estimate the pressure gradient and the ratio against the gradient guideline.
4. Run `pipe-wall-thickness-screening` to estimate the minimum wall thickness and the margin against the nominal wall.
5. Run `flow-induced-vibration-screening` to estimate the kinetic-energy likelihood index.
6. Record the warning levels and the most important uncertainties.
7. List required follow-up studies.

## Expected Screening Output Outline

- Line velocity indicators (erosional velocity, velocity ratio, guideline ratio) and warning level
- Pressure-drop indicators (pressure gradient, guideline ratio) and warning level
- Wall-thickness indicators (minimum thickness, thickness margin ratio) and warning level
- Flow-induced vibration likelihood index and warning level
- Recommended validated NeqSim and standards workflows
- Required follow-up studies
- Assumptions, limitations, and human review checklist

## Required Follow-Up

- Validated line sizing and hydraulics per API RP 14E and NORSOK P-002 with real fluid properties.
- Validated piping wall-thickness design per ASME B31.3 with material and corrosion allowances.
- Validated flow-induced vibration assessment per Energy Institute guidelines.
- NeqSim simulation of line conditions for confirmation.
- Qualified piping and process engineering review before any decision.
