# Control Authority Agent

Public, screening-level agent that decides whether a control loop still has
authority, or whether the final control element has been driven onto its stop
and the loop has quietly stopped regulating.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Reads the controller configuration so the real output stops are used, not an
  assumed 0 to 100 span.
- Measures saturation at both stops, because bottoming out costs the same
  authority as topping out.
- Trends saturation across comparable periods beside the disturbance measure,
  which is what separates "the disturbance grew" from "the loop lost authority".
- Quantifies lost disturbance rejection as the controlled-variable variance
  ratio between the saturated and modulating regimes.
- Fits the disturbance-to-process gain separately per regime, so a disturbance
  that explains almost none of the complaint can be ruled out on the numbers.
- Converts a trip margin and the observed rate of change into the time an
  operator actually has.

## Required skills

- `control-authority-screening`
- `plant-data`
- `technical-document-reading`

Loaded as relevant: `control-valve-cv-screening`,
`heat-exchanger-fouling-assessment`, `uncertainty-quantification`.

## Human review

This agent performs public, educational screening only. It **does not replace**
a validated loop performance review, control-valve rating, or qualified
control-engineering judgement. All outputs require human review before
operational or investment decisions.

See [AGENT.md](AGENT.md) for the full specification.
