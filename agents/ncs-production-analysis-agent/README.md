# NCS Production Analysis Agent

Coordinates an early-stage, public-data analysis of production on the Norwegian
Continental Shelf (NCS). It loads a source-attributed database of headline NCS
facts (production, resources, exports, field inventory) from
[norskpetroleum.no](https://www.norskpetroleum.no/en/) and the Norwegian
Offshore Directorate FactPages, answers inventory and resource-accounting
questions, and can chain a screening reservoir-depletion profile into asset-value
(NPV) and energy/emissions screening.

This agent supports screening and orientation only. It **does not replace**
reservoir simulation, official production statistics, commercial evaluation, or
qualified reservoir, production-technology, and economics engineering. A
qualified **human review** is always required before any decision.

## Required Skills

- `neqsim-norwegian-continental-shelf-data`
- `neqsim-reservoir-depletion-screening`
- `neqsim-asset-value-npv-screening`
- `neqsim-energy-emissions-screening`

## Attribution

Facts are reused with attribution to Norwegian Petroleum
(www.norskpetroleum.no), the Norwegian Ministry of Energy, and the Norwegian
Offshore Directorate. Every reused figure keeps its source and reference year.

## Layout

- `AGENT.md` — agent definition and workflow.
- `agent.yaml` — machine-readable manifest.
- `prompts/example-prompts.md` — example prompts.
- `examples/ncs-production-analysis-checklist.md` — walkthrough checklist.
- `tests/README.md` — how to exercise the agent through its skills.

See `AGENT.md` for the full workflow, assumptions, limitations, and the validated
NeqSim path.
