# Asset Economics Agent

The Asset Economics Agent coordinates early-stage asset-economics screening using NeqSim and the `neqsim-capex-opex-screening`, `neqsim-energy-emissions-screening`, and `neqsim-asset-value-npv-screening` community skills.

It helps engineers assemble a screening CAPEX/OPEX view, field-life energy and emissions roll-up, and discounted asset-value estimate. It is intended for concept screening and engineering assistance only.

## Capabilities

- Build a screening CAPEX/OPEX cost picture
- Roll up field-life energy use and CO2-equivalent emissions
- Estimate carbon intensity and optional CO2-tax exposure
- Discount net cash flow into a screening NPV and payback view
- Explain major assumptions, uncertainties, and follow-up studies

## Required Skills

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

Asset-economics screening outputs require qualified cost, environmental, commercial, and project assurance review before investment, design, or operational decisions.
