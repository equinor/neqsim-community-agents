# Example: Fire-Case Relief and Blowdown Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Process Safety Agent structures an early-stage screening. It does not size relief or blowdown systems.

## Scenario

A separator segment is reviewed for a fire-case relief load and an emergency blowdown to a target pressure.

Public synthetic inputs:

- Wetted fire area: 50 m^2
- Environment factor: 1.0 (no credit)
- Latent heat: 300 kJ/kg
- Relief pressure: 20 bara
- Inventory: 500 kg
- Initial pressure: 20 bara
- Target pressure: 7 bara
- Representative blowdown rate: 8000 kg/h
- Relieving temperature: 60 C
- MDMT: -46 C

## Screening Steps

1. Confirm the objective: preliminary relief and blowdown triage only.
2. Run `relief-load-screening` to estimate fire-case heat input and a relief load indicator.
3. Run `depressurization-screening` to estimate a blowdown time indicator and a low-temperature flag.
4. Record the warning levels and the most important uncertainties.
5. List required follow-up studies.

## Expected Screening Output Outline

- Relief load indicator and warning level
- Estimated blowdown time and indicator
- Cold-end temperature estimate and low-temperature flag
- Recommended validated NeqSim and API 520/521 workflows
- Required follow-up studies
- Assumptions, limitations, and human review checklist

## Required Follow-Up

- Validated relief sizing per API 520/521 with real fluid properties.
- Transient depressurization modeling in NeqSim for time and cold-end temperature.
- Materials low-temperature review against the controlling case.
- Qualified process safety review before any decision.
