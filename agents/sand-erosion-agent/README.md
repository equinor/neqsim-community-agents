# Sand Erosion Agent

The Sand Erosion Agent supports early-stage subsea and topside line sand-erosion screening using a public erosional-velocity ratio and a screening remaining-wall-life method.

It helps engineers check whether a sand-producing line appears to run below its erosional velocity and keeps enough remaining wall life, produce preliminary indicators, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening and operation support only.

## Capabilities

- Estimate the erosional velocity and velocity ratio from flow velocity and mixture density
- Estimate a screening erosion rate, cumulative wall loss, remaining wall, and remaining wall life
- Flag lines that appear to run above their erosional velocity or with insufficient remaining wall life
- Identify required follow-up erosion, sand-monitoring, and inspection studies
- Generate screening reports
- Suggest validated NeqSim erosion and pipe-flow workflows

## Required Skills

- `sand-erosion-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Sand-erosion screening results are educational placeholders. They require qualified flow assurance, integrity, and project review before any design or operational use. This agent does not replace validated DNV RP O501 erosion calculation, sand-management procedure approval, inspection-interval setting, or qualified engineering judgement.
