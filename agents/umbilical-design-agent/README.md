# Umbilical Design Agent

The Umbilical Design Agent sizes, checks and draws a subsea control or service umbilical with the NeqSim umbilical physics, and hands a figure set, key numbers and open items to SURF, flow-assurance and cost workflows.

## Capabilities

- Tube wall from burst and collapse, cross-section and weights from the element mix, armour from catenary tension
- Friction drop and pressure-step response of hydraulic and chemical lines
- Power cable voltage drop, loss and charging current with a step-out sweep
- Design checks with causes and the cheapest change for each failure
- Cross-section drawing, charts and an "umbilical on a page" with basis version on every figure
- `HANDOFF.md` with ready-to-paste captions, evidence status of inputs, screening defaults and open items

## Required Skills

- `neqsim-umbilical-design`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public synthetic example.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Results are screening estimates. They require qualified SURF, controls, electrical and project review before any design or procurement use. The agent does not replace vendor design, dynamic riser analysis, fatigue, installation analysis or qualification.
