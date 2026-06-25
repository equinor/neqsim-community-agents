# Compressor Anti-Surge Agent

The Compressor Anti-Surge Agent supports early-stage setup of anti-surge recycle (spill-back) control for a centrifugal compressor in NeqSim.

It helps engineers estimate the recycle flow required to keep a compressor off its surge line, decide whether a compressor chart must be generated when no vendor chart is available, generate a NeqSim chart with surge and stonewall curves, and build the validated NeqSim anti-surge recycle topology. It is intended for transparent concept screening and model scaffolding only.

## Capabilities

- Estimate the surge margin and recommended recycle flow for an operating point
- Decide whether a compressor chart must be generated (with surge and stonewall curves)
- Explain how to auto-generate a NeqSim compressor chart from a design point
- Describe the NeqSim anti-surge recycle topology (surge curve, recycle stream, discharge splitter, anti-surge `Calculator`, anti-surge valve, `Recycle`)
- Flag operating points that fall at or below the surge line
- Identify required follow-up compressor performance and anti-surge control studies
- Generate anti-surge setup reports
- Suggest validated NeqSim, API 617, and API 692 workflows

## Required Skills

- `compressor-antisurge-recycle`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Anti-surge recycle estimates and generated compressor charts are educational placeholders and model estimates. They require qualified process engineering, rotating equipment, and project review before any design or operational use. This agent does not replace anti-surge controller design and tuning, dynamic surge or transient analysis, vendor performance maps, HAZOP, or qualified engineering judgement.
