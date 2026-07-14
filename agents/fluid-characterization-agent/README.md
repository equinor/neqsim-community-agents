# Fluid Characterization Agent

The Fluid Characterization Agent assists with a reproducible, factor-driven
fluid characterization workflow using NeqSim and four community skills:
`fluid-quality-check`, `pseudocomponent-split-characterization`,
`reference-fluid-synthetic-generation`, and
`pvt-regression-characterization-factor`.

It implements the "common reference fluid → adjust split factor → match measured
data → generate representative fluids" methodology in a public, plant-agnostic
way. It does not replace PVT specialist judgement or validated laboratory
interpretation.

## Capabilities

- Review fluid composition quality
- Split a plus fraction into pseudocomponents with a controllable split factor
- Calibrate the split factor against weighted PVT / separator measurements
- Generate representative or synthetic fluid cases from a common reference fluid
- Blend well/fluid compositions by molar-rate allocation
- Explain assumptions and limitations

## Required Skills

- `fluid-quality-check`
- `pseudocomponent-split-characterization`
- `reference-fluid-synthetic-generation`
- `pvt-regression-characterization-factor`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

All generated splits, calibrated factors, generated fluids, and workflows require
qualified PVT review before use in design, assurance, reporting, or operations.
