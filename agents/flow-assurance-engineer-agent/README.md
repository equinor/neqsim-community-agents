# Flow Assurance Engineer Agent

The Flow Assurance Engineer Agent supports early-stage flow assurance screening by combining hydrate-margin screening and wax-margin screening.

It helps engineers check whether operating points appear to keep safe temperature margins above hydrate and wax formation boundaries, produce preliminary indicators, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate hydrate margin and subcooling against a hydrate equilibrium temperature
- Estimate wax margin against a wax appearance temperature
- Flag operating points that appear to run with insufficient margin
- Identify required follow-up hydrate, wax, inhibitor, and thermal studies
- Generate screening reports
- Suggest validated NeqSim hydrate and wax workflows

## Required Skills

- `hydrate-margin-check`
- `wax-margin-check`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Flow assurance screening results are educational placeholders. They require qualified flow assurance, process engineering, thermal, and project review before any design or operational use. This agent does not replace hydrate or wax prediction, inhibitor design, deposition modelling, transient studies, or qualified engineering judgement.
