# Gas Lift Allocation Agent

Early-stage, public screening agent that frames a lift-gas allocation problem
across a small set of gas-lifted wells and ranks candidate splits.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Frames wells, lift-gas budget, objective, and constraints.
- Screens each well's lift-gas response trend and routing effects.
- Ranks candidate lift-gas splits and flags wells near a screening limit.
- Recommends a validated NeqSim production-optimization run for any decision.

## Required skills

- `artificial-lift-screening`
- `production-network-routing`
- `reservoir-depletion-screening`

## Human review

This agent performs public, educational screening only. It **does not replace**
a validated NeqSim production-optimization study or qualified engineering
judgement. All outputs require human review before use.

See [AGENT.md](AGENT.md) for the full specification.
