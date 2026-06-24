# Subsea Cooldown Agent

The Subsea Cooldown Agent supports early-stage subsea flowline and riser cooldown screening using a lumped exponential no-touch-time method.

It helps engineers check whether a shut-in section appears to keep enough no-touch time before it cools into the hydrate region, produce a preliminary indicator, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate the no-touch time (hours to reach the hydrate equilibrium temperature) from a lumped exponential cooldown
- Estimate a lumped cooldown time constant from approximate geometry and an overall heat transfer coefficient
- Flag shut-in cases that appear to run with insufficient no-touch time
- Identify required follow-up transient cooldown, insulation, and inhibitor studies
- Generate screening reports
- Suggest validated NeqSim cooldown and hydrate workflows

## Required Skills

- `surf-cooldown-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Cooldown screening results are educational placeholders. They require qualified flow assurance, process engineering, thermal, and project review before any design or operational use. This agent does not replace transient cooldown simulation, hydrate prediction, insulation qualification, inhibitor design, shutdown-procedure approval, or qualified engineering judgement.
