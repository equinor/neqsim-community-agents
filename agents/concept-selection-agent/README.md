# Concept Selection Agent

Early-stage, public screening agent that compares a small set of development
concepts on a consistent resource, cost, value, emissions, and step-out basis.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Places the resource on a public classification basis.
- Builds an indicative cost, discounted-value, and emissions picture per concept.
- Screens tie-back step-out distance for tieback concepts.
- Produces a screening-level ranking and recommends validated NeqSim studies.

## Required skills

- `resource-classification-screening`
- `capex-opex-screening`
- `asset-value-npv-screening`
- `energy-emissions-screening`
- `step-out-screening`

## Human review

This agent performs public, educational screening only. It **does not replace**
validated NeqSim field-development, economics, or emissions studies or qualified
engineering judgement. All outputs require human review before use.

See [AGENT.md](AGENT.md) for the full specification.
