# Process Engineer Agent

The Process Engineer Agent supports early-stage process engineering screening by combining line-velocity screening and compressor operating-window screening.

It helps engineers check whether unit operations appear to run within public design and operating guidelines (such as erosional-velocity and surge/stonewall limits), produce preliminary indicators, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate line velocity against erosional velocity and a velocity guideline
- Estimate compressor surge and stonewall operating-window margins
- Flag unit operations that appear to run outside standard guidelines
- Identify required follow-up line sizing, hydraulic, and compressor studies
- Generate screening reports
- Suggest validated NeqSim, API RP 14E, NORSOK P-001, and API 617 workflows

## Required Skills

- `line-velocity-check`
- `compressor-operating-window-check`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Process engineering screening results are educational placeholders. They require qualified process engineering, rotating equipment, hydraulic, and project review before any design or operational use. This agent does not replace line sizing, compressor performance and anti-surge design, hydraulic studies, HAZOP, or qualified engineering judgement.
