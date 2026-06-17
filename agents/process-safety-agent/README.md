# Process Safety Agent

The Process Safety Agent supports early-stage process safety screening by combining fire-case relief load screening and emergency depressurization screening.

It helps engineers produce preliminary relief load indicators, blowdown time indicators, and auto-refrigeration low-temperature flags, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate fire-case relief load indicators
- Estimate blowdown time to a target pressure
- Flag potential low-temperature (auto-refrigeration) concerns against an MDMT
- Identify required follow-up studies
- Generate screening reports
- Suggest validated NeqSim and API 520/521 workflows

## Required Skills

- `relief-load-screening`
- `depressurization-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Process safety screening results are educational placeholders. They require qualified process safety, relief and flare, materials, and project review before any design or operational use. This agent does not replace relief and flare design, depressurization design, HAZOP, LOPA, SIL determination, or qualified engineering judgement.
