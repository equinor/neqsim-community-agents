# Piping Mechanical Agent

The Piping Mechanical Agent performs high-level screening of process piping mechanical integrity using NeqSim and the `piping-flexibility-screening` and `acoustic-induced-vibration-screening` community skills.

It helps engineers screen hoop stress and minimum wall thickness, indicate thermal-flexibility concerns, and screen acoustic-induced vibration likelihood of failure aligned with ASME B31.3, ASME B16.5, and Energy Institute AIV concepts. It is intended for early screening and engineering assistance only.

## Capabilities

- Screen hoop stress and minimum wall thickness
- Indicate thermal-flexibility concerns
- Screen acoustic-induced vibration likelihood of failure
- List lines needing detailed analysis
- Explain limitations

## Required Skills

- `piping-flexibility-screening`
- `acoustic-induced-vibration-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Piping mechanical screening outputs require qualified piping mechanical and stress engineering review before design, support layout, or operational decisions.
