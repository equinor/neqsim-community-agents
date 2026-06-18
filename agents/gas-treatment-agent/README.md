# Gas Treatment Agent

The Gas Treatment Agent supports early-stage gas treatment and conditioning screening by combining gas water-content and dehydration screening with single-stage compression power screening.

It helps engineers check whether a gas appears to require dehydration against a sales-gas water spec, estimate preliminary compression head, discharge temperature, and gas power, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate saturated water content of natural gas
- Compare water content against a sales-gas water spec to indicate whether dehydration appears required
- Estimate polytropic head, discharge temperature, and gas power for a single compression stage
- Identify required follow-up dehydration and compression studies
- Generate screening reports
- Suggest validated NeqSim, GPSA, API 617, and API 619 workflows

## Required Skills

- `water-dewpoint-dehydration-screening`
- `compressor-power-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Gas treatment screening results are educational placeholders. They require qualified process and rotating-equipment review before any design or operational use. This agent does not replace dehydration design, compressor selection, equipment sizing, HAZOP, or qualified engineering judgement.
