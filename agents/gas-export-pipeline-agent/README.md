# Gas Export Pipeline Agent

The Gas Export Pipeline Agent performs preliminary gas-export pipeline screening using NeqSim and the `neqsim-line-velocity-check`, `neqsim-pressure-drop-screening`, and `neqsim-compressor-power-screening` community skills.

It helps engineers check whether an export-line diameter, pressure-drop estimate, and compression duty are in a sensible screening range. It is intended for early screening and engineering assistance only.

## Capabilities

- Screen gas-export line velocity against erosional and recommended limits
- Estimate single-phase pressure drop against a pressure-gradient guideline
- Estimate export-compression power for the required pressure rise
- Identify missing multiphase, terrain, thermal, and compressor data
- Explain limitations and recommended follow-up analysis

## Required Skills

- `neqsim-line-velocity-check`
- `neqsim-pressure-drop-screening`
- `neqsim-compressor-power-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Gas-export pipeline screening outputs require qualified pipeline, process, rotating-equipment, and mechanical review before design, investment, or operational decisions.
