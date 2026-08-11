# Reservoir Simulator Agent

Sets up a screening-level reservoir model for a field from whatever data is
available, and keeps refining it as more data arrives.

The agent is built for the common case where a study must start from open public
information — a public field page, a discovery announcement, an approved
development plan summary — and where the model must later be upgraded with
appraisal-well logs, a well test and a PVT report. Every parameter carries a
provenance label, so the model always reports what was known, what was assumed
and on what basis, and which missing measurement matters most.

This agent supports screening and orientation only. It **does not replace**
grid-based reservoir simulation, history matching, official reserves statements,
or qualified reservoir engineering. A qualified **human review** is always
required before any decision.

## Required Skills

- `neqsim-reservoir-model-builder`
- `neqsim-norwegian-continental-shelf-data`
- `neqsim-reservoir-depletion-screening`
- `neqsim-resource-classification-screening`
- `neqsim-fluid-quality-check`

Loaded as context when the task calls for them:

- `neqsim-pseudocomponent-split-characterization`
- `neqsim-production-network-routing`
- `neqsim-asset-value-npv-screening`

## Data-maturity ladder

| Tier | Typically available | What the agent can produce |
| --- | --- | --- |
| 0 headline | field name, product, sea area | orientation only, plus a data request |
| 1 public volumetric | recoverable or in-place volume, depth | volumetrics, gradient-based conditions, a runnable tank model |
| 2 well and PVT | area, net pay, porosity, Sw, permeability, PVT | geometry volumetrics, Darcy inflow, well count, plateau |
| 3 static model | zone geometry, aquifer, well tests | a constrained model with only minor assumptions |

## Attribution

Public facts are reused with attribution to the source — for Norwegian
Continental Shelf fields, Norwegian Petroleum (www.norskpetroleum.no) and the
Norwegian Offshore Directorate. Every reused figure keeps its source and
reference year.

## Layout

- `AGENT.md` — agent definition and workflow.
- `agent.yaml` — machine-readable manifest.
- `prompts/example-prompts.md` — example prompts.
- `examples/staged-reservoir-model-checklist.md` — walkthrough checklist.
- `tests/README.md` — how to exercise the agent through its skills.

See `AGENT.md` for the full workflow, assumptions, limitations, and the validated
NeqSim path.
