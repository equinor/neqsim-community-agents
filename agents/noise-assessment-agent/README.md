# Noise Assessment Agent

The Noise Assessment Agent evaluates gas-valve and restriction noise from a current operating measurement or process conditions. It uses the `noise-screening` skill for transparent triage, routes detailed source work to NeqSim's IEC 60534-8-3 class, and keeps workplace noise and AIV conclusions separate.

## Capabilities

- Preserve operating, receiver, measurement, and uncertainty context.
- Screen measured or modelled receiver noise.
- Route detailed source prediction to `ControlValveNoise_IEC_60534_8_3`.
- Map the decision to IEC 60534-8-3 and ISO 3744, 11201, 9613-2, 15664, and 1999.
- Trigger a separate AIV screen for high-energy pressure reduction.
- Report evidence gaps, mitigations, and required human review.

## Required Skills

- `noise-screening`
- `acoustic-induced-vibration-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public synthetic workflow.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes.

## Human Review

This agent does not replace qualified human review. Acoustic and occupational-hygiene review is required for exposure or compliance decisions. Detailed source design also requires verified valve data and process review; AIV conclusions require piping-vibration review.