# Field-Development Economics Agent

The Field-Development Economics Agent coordinates an end-to-end reservoir-to-market concept screening using NeqSim and community skills for fluid quality, reservoir depletion, hydrate margin, separator capacity, line velocity, CAPEX/OPEX, emissions, and NPV.

It helps engineers connect technical screening results to concept economics. It is intended for early concept screening and engineering assistance only.

## Capabilities

- Screen reservoir fluid quality and depletion assumptions
- Check subsea hydrate-margin and topside separator indicators
- Screen gas-export line velocity and export-system constraints
- Roll up CAPEX/OPEX, emissions, carbon intensity, and CO2-tax exposure
- Estimate screening NPV and payback for concept comparison

## Required Skills

- `neqsim-fluid-quality-check`
- `neqsim-reservoir-depletion-screening`
- `neqsim-hydrate-margin-check`
- `neqsim-separator-modelling`
- `neqsim-line-velocity-check`
- `neqsim-capex-opex-screening`
- `neqsim-energy-emissions-screening`
- `neqsim-asset-value-npv-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Field-development economics screening outputs require qualified reservoir, process, flow-assurance, cost, environmental, commercial, and project assurance review before concept selection, investment, design, or operational decisions.
