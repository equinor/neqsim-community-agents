# Reciprocating Compressor Agent

The Reciprocating Compressor Agent performs high-level screening of reciprocating compressor performance using NeqSim and the `reciprocating-compressor-screening` community skill.

It helps engineers screen compression staging, per-stage volumetric efficiency, discharge temperature, and a public rod-load likelihood indication aligned with API 618 and API 619 concepts. It is intended for early screening and engineering assistance only.

## Capabilities

- Estimate stage count and per-stage pressure ratio
- Screen volumetric efficiency
- Estimate discharge temperature per stage
- Provide a screening-level rod-load indication
- Explain limitations

## Required Skill

- `reciprocating-compressor-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Reciprocating compressor screening outputs require qualified rotating equipment and process engineering review before design, vendor selection, or operational decisions.
