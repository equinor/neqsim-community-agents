# Produced Water Scale Agent

The Produced Water Scale Agent supports early-stage produced-water characterization and screening-level scale risk evaluation.

It helps engineers turn an ion analysis, a named brine preset, or a TDS value into a transparent water description, emit a NeqSim-ready electrolyte ion mapping, and produce public, screening-level scale saturation and mixing-incompatibility indicators. It is intended for transparent concept screening only.

## Capabilities

- Build produced-water descriptions from ions, presets, or TDS
- Emit NeqSim-ready electrolyte ion compositions (water + ion mole fractions)
- Estimate screening-level scale saturation indices (BaSO4, SrSO4, CaSO4, CaCO3)
- Sweep seawater/formation-water mixing for sulfate and carbonate scale incompatibility
- Flag charge-balance and ionic-strength concerns
- Produce public corrosion flags from CO2 and H2S content
- Suggest validated NeqSim electrolyte and scale-potential workflows

## Required Skills

- `produced-water-scale-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Produced-water scale screening results are educational placeholders. They require qualified water-chemistry, flow assurance, integrity, and project review before any design or operational use. This agent does not replace validated electrolyte scale prediction, scale inhibitor design, corrosion qualification, or qualified engineering judgement.
