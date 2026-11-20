# Well Design Study Agent

The Well Design Study Agent leads a screening-level well design study and report from public data. It uses the community skill `neqsim-well-design-study` and adds `neqsim-erd-reach-screening` for long reach.

## Capabilities

- Collect or load offset-well evidence with source and tier
- Build and calibrate a pore and fracture pressure model and the mud-weight window
- Check a planned casing programme or propose seats bottom-up, with kick tolerance
- Select casing and tubing strings with design factors and governing load cases
- Screen torque and drag, ECD, erosional velocity and wellhead class
- Produce time and cost P10/P50/P90 and a Word report with registers

## Required Skills

- `neqsim-well-design-study`
- `neqsim-erd-reach-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public example workflow.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Results are screening values. A qualified well engineer and drilling engineer must review them before any decision. This agent contains no company data or design basis; company-specific routes live in private repositories.
