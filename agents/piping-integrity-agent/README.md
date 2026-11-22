# Piping Integrity Agent

The Piping Integrity Agent supports early-stage piping integrity screening by combining line-velocity screening, single-phase pressure-drop screening, wall-thickness screening, flow-induced vibration screening, and internal CO2 corrosion along the flowline.

It helps engineers check whether lines appear to run within public design and integrity guidelines (such as erosional-velocity, pressure-gradient, ASME B31.3 wall-thickness, and Energy Institute vibration limits), produce preliminary indicators, identify required studies, generate screening reports, and suggest validated NeqSim and standards workflows. It is intended for transparent concept screening only.

## Capabilities

- Estimate line velocity against erosional velocity and a velocity guideline
- Estimate single-phase pressure drop against a pressure-gradient guideline
- Estimate minimum wall thickness against a nominal schedule wall
- Estimate a flow-induced vibration likelihood index
- Run NORSOK M-506 Rev. 2 CO2 corrosion along the NeqSim pipeline profile: free water, design rate with inhibitor availability, wall loss against the corrosion allowance, NORSOK M-001 material recommendation and the NeqSim materials review
- Flag lines that appear to run outside standard guidelines
- Identify required follow-up line sizing, hydraulic, mechanical, and vibration studies
- Generate screening reports
- Suggest validated NeqSim, API RP 14E, NORSOK P-002, ASME B31.3, and Energy Institute workflows

## Required Skills

- `line-velocity-check`
- `pressure-drop-screening`
- `pipe-wall-thickness-screening`
- `flow-induced-vibration-screening`
- `co2-corrosion-profile`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Piping integrity screening results are educational placeholders. They require qualified piping, process, hydraulic, mechanical, and project review before any design or operational use. This agent does not replace line sizing, piping mechanical design, hydraulic studies, flow-induced vibration design, HAZOP, or qualified engineering judgement.
