# E300 Fluid Agent

The E300 Fluid Agent moves fluids between Eclipse 300 (E300) compositional EOS
files and NeqSim, and adds water using the public PVTsim water parameterization,
with the `e300-fluid-io` community skill.

It is intended for public, reproducible engineering assistance. It can read an
E300 file into a NeqSim fluid, write a NeqSim fluid to E300, add water to a
fluid or E300 file, and explain assumptions. It does not replace PVT specialist
judgement or validated laboratory interpretation.

## Capabilities

- Read E300 files into NeqSim fluids
- Write NeqSim fluids to E300 files
- Add water with the public PVTsim water parameters
- Reproduce a PVTsim `*_water.e300` file from a base E300 file
- Explain the E300 keyword format, assumptions, and limitations

## Required Skill

- `e300-fluid-io`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

All generated fluids, E300 files, and water treatments require qualified review
before use in design, assurance, reporting, or operations.
