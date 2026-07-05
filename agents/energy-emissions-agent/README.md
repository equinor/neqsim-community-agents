# Energy Emissions Agent

The Energy Emissions Agent performs preliminary energy-use and CO2-equivalent emissions screening using NeqSim and the `neqsim-energy-emissions-screening` community skill.

It helps engineers convert annual energy use into indicative emissions, carbon intensity, and optional CO2-tax exposure. It is intended for early screening and engineering assistance only.

## Capabilities

- Estimate annual CO2-equivalent emissions from energy use and emission factor
- Estimate carbon intensity per barrel of oil equivalent
- Apply an optional CO2-tax exposure calculation
- Identify missing fuel, scope-boundary, and combustion-efficiency data
- Explain limitations and recommended follow-up analysis

## Required Skill

- `neqsim-energy-emissions-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Energy and emissions screening outputs require qualified environmental, process, and reporting review before regulatory, design, investment, or operational decisions.
