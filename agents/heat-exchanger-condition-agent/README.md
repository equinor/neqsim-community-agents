# Heat Exchanger Condition Agent

Public, screening-level agent that assesses whether a heat exchanger has
degraded, by how much against its design coefficient, what it is costing in duty
or capacity, and how often it should be cleaned.

## Status

Draft (version 0.1.0). Screening only.

## What it does

- Extracts the design basis from a vendor data sheet and pulls admissible
  operating snapshots from the historian.
- Reduces the snapshot to an overall coefficient on the LMTD or
  effectiveness-NTU basis the temperature approach justifies.
- Normalises to design flow with the two-sided form, so the fouling deposit is
  not scaled with the films, and reports what the one-sided form would have
  claimed instead.
- Reports fouling resistance in excess of the design allowance, not total
  fouling.
- Rules out maldistribution by crediting N, N-1, N-2 units before blaming the
  deposit.
- Converts the coefficient into a capacity limit and names the binding
  constraint.
- Ranks cleaning frequency against cleaning effectiveness against retrofit.

## Required skills

- `heat-exchanger-fouling-assessment`
- `technical-document-reading`
- `plant-data`

Loaded as relevant: `benchmark-reference-data`, `uncertainty-quantification`.

## Human review

This agent performs public, educational screening only. It **does not replace**
vendor rating software, a validated NeqSim thermal design, or qualified
engineering judgement. All outputs require human review before operational or
investment decisions.

See [AGENT.md](AGENT.md) for the full specification.
