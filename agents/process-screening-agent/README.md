# Process Screening Agent

The Process Screening Agent performs high-level process engineering screening studies using NeqSim and the `separator-modelling` community skill.

It helps engineers review process descriptions, identify major risks, recommend process simulations, generate engineering checklists, and explain limitations. It is intended for early screening and engineering assistance only.

## Capabilities

- Review process descriptions
- Identify major risks
- Recommend process simulations
- Generate engineering checklists
- Explain limitations

## Required Skill

- `separator-modelling`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Process screening outputs require qualified process engineering and process safety review before design, modification, or operational decisions.