# Gas Turbine Screening Agent

The Gas Turbine Screening Agent performs high-level screening of gas-turbine driver performance using NeqSim and the `gas-turbine-performance-screening` community skill.

It helps engineers apply site-rating corrections, screen heat rate and fuel consumption, and estimate exhaust conditions aligned with ISO 3977 concepts. It is intended for early screening and engineering assistance only.

## Capabilities

- Apply ambient and elevation site-rating corrections
- Screen heat rate and fuel gas consumption
- Estimate exhaust flow and temperature
- Compare driver power against duty
- Explain limitations

## Required Skill

- `gas-turbine-performance-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Gas-turbine screening outputs require qualified rotating equipment and process engineering review before driver selection, performance commitments, or operational decisions.
