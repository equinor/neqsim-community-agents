# Production Optimization Agent

Early-stage, public screening agent that frames a setpoint-search problem on a
simple process train and screens candidate operating points for higher
throughput or lower compression power.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Frames decision variables, bounds, objective, and constraints.
- Screens candidate setpoints against public capacity and operating-window guidelines.
- Ranks promising operating directions and flags guideline violations.
- Recommends a validated NeqSim optimization run for any quantitative decision.

## Required skills

- `separator-modelling`
- `compressor-operating-window-check`
- `compressor-power-screening`
- `production-network-routing`

## Human review

This agent performs public, educational screening only. It **does not replace**
a validated NeqSim optimization study or qualified engineering judgement. All
outputs require human review before use.

See [AGENT.md](AGENT.md) for the full specification.
