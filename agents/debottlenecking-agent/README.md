# Debottlenecking Agent

Early-stage, public screening agent that ranks units of a simple process train by
approximate capacity utilization and identifies the most likely bottleneck.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Screens separator capacity, compressor operating window, line velocity, and
  line pressure drop.
- Ranks units by approximate screening-level utilization.
- Identifies the most likely bottleneck and suggests debottlenecking directions.
- Recommends a validated NeqSim capacity study for any quantitative decision.

## Required skills

- `separator-modelling`
- `compressor-operating-window-check`
- `line-velocity-check`
- `pressure-drop-screening`

## Human review

This agent performs public, educational screening only. It **does not replace**
a validated NeqSim capacity study or qualified engineering judgement. All outputs
require human review before use.

See [AGENT.md](AGENT.md) for the full specification.
