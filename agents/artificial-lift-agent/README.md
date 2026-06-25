# Artificial Lift Agent

The Artificial Lift Agent performs high-level screening of artificial-lift options using NeqSim and the `artificial-lift-screening` community skill.

It helps engineers compare gas-lift and ESP feasibility against a simple inflow performance relationship (IPR), indicate achievable drawdown and rate, and highlight selection drivers. It is intended for early screening and engineering assistance only.

## Capabilities

- Build a simple IPR and screen deliverability
- Indicate gas-lift feasibility
- Indicate ESP feasibility
- Highlight selection drivers
- Explain limitations

## Required Skill

- `artificial-lift-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Artificial-lift screening outputs require qualified production technology and well engineering review before lift selection, design, or operational decisions.
