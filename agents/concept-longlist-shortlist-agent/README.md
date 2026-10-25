# Concept Long-list Short-list Agent

Early-stage, public screening agent that turns a field-development opportunity
into a long list of concepts and selects a defended short list with a reference
case.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Generates the long list from decision elements, options, and compatibility rules.
- Warns when the long list is capacity variants of one topology.
- Eliminates only on evidenced must-pass failures; keeps the rest pending with open
  questions.
- Ranks concepts on one common basis, reports the Pareto front, and tests the
  ranking against the criterion weights (robustness and crossovers).
- Selects a short list (leader, robust contenders, diversity, reference) and hands
  it to `concept-selection-agent`.

## Required skills

- `concept-longlist-shortlist-screening`
- `capex-opex-screening`
- `asset-value-npv-screening`
- `energy-emissions-screening`
- `step-out-screening`

## Human review

This agent performs public, educational screening only. It **does not replace**
validated NeqSim field-development, economics, or emissions studies or qualified
engineering judgement, and it does not select a concept. All outputs require
human review before use.

See [AGENT.md](AGENT.md) for the full specification.
