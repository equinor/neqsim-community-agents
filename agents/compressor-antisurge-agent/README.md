# Compressor Anti-Surge Agent

The Compressor Anti-Surge Agent supports early-stage setup of anti-surge recycle (spill-back) control for a centrifugal compressor in NeqSim.

It helps engineers estimate the recycle flow required to keep a compressor off its surge line, decide whether a compressor chart must be generated when no vendor chart is available, generate a NeqSim chart with surge and stonewall curves, and choose the validated NeqSim anti-surge implementation path: steady-state `AntiSurgeRecycleCalculator`, dynamic `AntiSurgeController`, or `CompressorAntiSurgeApplication` topology binding for real hot/cold recycle valves and compressor speed runback. It is intended for transparent concept screening and model scaffolding only.

## Capabilities

- Estimate the surge margin and recommended recycle flow for an operating point
- Decide whether a compressor chart must be generated (with surge and stonewall curves)
- Explain how to auto-generate a NeqSim compressor chart from a design point
- Describe the NeqSim anti-surge recycle topology (surge curve, recycle stream, discharge splitter or recycle branch, anti-surge valve, `Recycle`, optional cooler/mixer)
- Recommend `AntiSurgeRecycleCalculator` for steady-state recycle initialization on charted compressors
- Point to the dynamic `AntiSurgeController` (reverse-acting PI on distance to surge) and the reproducible `AntiSurgeDynamicBenchmark` for transient studies, including the deep-surge gotchas
- Point to `CompressorAntiSurgeApplication.bindTopology(...)` and `runDynamicStep(...)` for executable dynamic studies with hot/cold recycle split, diagnostics, and speed runback
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

Anti-surge recycle estimates, generated compressor charts, and application-level topology-binding examples are educational and simulation-oriented. They require qualified process engineering, rotating equipment, and project review before any design or operational use. This agent does not replace anti-surge controller design and tuning, dynamic surge or transient analysis, vendor performance maps, HAZOP, certified machinery protection, or qualified engineering judgement.
