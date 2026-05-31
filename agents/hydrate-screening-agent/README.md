# Hydrate Screening Agent

The Hydrate Screening Agent assists with preliminary hydrate risk assessments using NeqSim and the `hydrate-screening` community skill.

It helps engineers review pressure and temperature conditions, identify missing data, explain assumptions, and recommend further analysis. It is intended for screening and engineering assistance only.

## Capabilities

- Review pressure and temperature conditions
- Evaluate screening-level hydrate risk
- Explain assumptions
- Recommend further analysis
- Prepare preliminary risk notes

## Required Skill

- `hydrate-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Hydrate screening outputs require qualified flow assurance review before use in design, operations, chemical strategy, or safety-related decisions.