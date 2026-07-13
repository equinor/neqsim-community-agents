# Reservoir Forecasting Agent

Coordinates an early-stage, public-data production forecast for a Norwegian
Continental Shelf (NCS) field or well. It fits an Arps decline curve
(exponential, hyperbolic, or harmonic) to a produced-rate history, projects a
forward rate profile to an economic-limit rate, and reports remaining volume and
an estimated ultimate recovery (EUR). It cross-checks the decline forecast
against a tank-style reservoir-depletion screening and a resource-classification
maturity, using public data from
[norskpetroleum.no](https://www.norskpetroleum.no/en/) and the Norwegian
Offshore Directorate.

This agent supports screening and orientation only. It **does not replace**
reservoir simulation, material balance, probabilistic decline history matching,
official reserves statements, or qualified reservoir engineering. A qualified
**human review** is always required before any decision.

## Required Skills

- `neqsim-norwegian-continental-shelf-data`
- `neqsim-reservoir-depletion-screening`
- `neqsim-resource-classification-screening`

## Attribution

Facts are reused with attribution to Norwegian Petroleum
(www.norskpetroleum.no), the Norwegian Ministry of Energy, and the Norwegian
Offshore Directorate. Every reused figure keeps its source and reference year.

## Layout

- `AGENT.md` — agent definition and workflow.
- `agent.yaml` — machine-readable manifest.
- `prompts/example-prompts.md` — example prompts.
- `examples/reservoir-forecasting-checklist.md` — walkthrough checklist.
- `tests/README.md` — how to exercise the agent through its skills.

See `AGENT.md` for the full workflow, assumptions, limitations, and the validated
NeqSim path.
