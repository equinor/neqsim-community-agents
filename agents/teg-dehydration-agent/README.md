# TEG Dehydration Agent

The TEG Dehydration Agent builds and runs closed-loop triethylene-glycol (TEG)
gas dehydration plants in NeqSim using the `teg-dehydration-modeling` community
skill.

It helps engineers assemble the absorber, flash drum, regeneration column,
stripper, and lean-TEG recycle; run the flowsheet to convergence; and report the
dry-gas water dew point, lean-TEG purity, and regeneration still-vent emissions.
It is intended for screening and engineering assistance only.

## Capabilities

- Build a runnable NeqSim TEG dehydration plant from public conditions
- Report dry-gas water dew point and lean-TEG purity
- Classify regeneration still-vent emissions (NMVOC, methane, benzene, CO2, water)
- Compare once-through versus recirculated stripping gas
- Identify missing data and recommend validated follow-up analysis

## Required Skill

- `teg-dehydration-modeling`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

TEG dehydration outputs require qualified process and environmental review before
use in design, operations, emission reporting, or safety-related decisions.
