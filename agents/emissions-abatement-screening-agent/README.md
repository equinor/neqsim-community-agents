# Emissions Abatement Screening Agent

Coordinates an early-stage, public-data business case for reducing greenhouse-gas
and NOx emissions from a Norwegian Continental Shelf (NCS) facility or process.
It estimates a screening baseline of field-life energy use and CO2-equivalent
emissions, values that emission stream with the public Norwegian carbon-cost
basis (CO2 Tax Act rate, EU ETS allowance cost, and NOx Fund contribution as
published on [norskpetroleum.no](https://www.norskpetroleum.no/en/environment-and-technology/emissions-to-air/)),
and turns a candidate abatement measure into a net-annual-saving, simple-payback,
discounted-NPV, and breakeven-CO2-price screening.

This agent supports screening and orientation only. It **does not replace** a
validated NeqSim energy/combustion model, a certified emission inventory, a
marginal-abatement-cost study, or a qualified commercial evaluation. A qualified
**human review** is always required before any decision.

## Required Skills

- `neqsim-energy-emissions-screening`
- `neqsim-norwegian-continental-shelf-data`
- `neqsim-asset-value-npv-screening`

## Attribution

Carbon-cost and emission facts are reused with attribution to Norwegian Petroleum
(www.norskpetroleum.no), the Norwegian Ministry of Energy, and the Norwegian
Offshore Directorate. Every reused figure keeps its source and reference year.

## Layout

- `AGENT.md` — agent definition and workflow.
- `agent.yaml` — machine-readable manifest.
- `prompts/example-prompts.md` — example prompts.
- `examples/emissions-abatement-checklist.md` — walkthrough checklist.
- `tests/README.md` — how to exercise the agent through its skills.

See `AGENT.md` for the full workflow, assumptions, limitations, and the validated
NeqSim path.
