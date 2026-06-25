# Utilities Screening Agent

The Utilities Screening Agent performs high-level screening of facility utility systems using NeqSim and the `utility-balance-screening` community skill.

It helps engineers screen instrument air supply versus demand, fuel-gas Wobbe Index, and cooling-water duty and balance aligned with NORSOK U-001 and ISA-7.0.01 concepts. It is intended for early screening and engineering assistance only.

## Capabilities

- Screen instrument air supply versus demand and dew point
- Screen fuel-gas Wobbe Index against a target band
- Screen cooling-water duty and supply/return balance
- List utility bottlenecks
- Explain limitations

## Required Skill

- `utility-balance-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Utility screening outputs require qualified utility systems and process engineering review before design, equipment sizing, or operational decisions.
