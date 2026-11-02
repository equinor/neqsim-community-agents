# Brazil Well Production Agent

Public screening coordinator that reads ANP well-level production open data for Brazilian wells and fields, proves the units and totals, screens decline, GOR and water cut, prepares a declared fluid basis and states what the public data can and cannot support before a calibrated NeqSim model.

## Status

Draft (version 0.1.0). Screening only.

## Required skills

- `neqsim-anp-well-production-history` (version 0.1.0 or later)
- `neqsim-anp-open-data` (version 0.2.1 or later)
- `neqsim-norwegian-continental-shelf-data` (Arps decline fit)
- `neqsim-reservoir-depletion-screening`

## Human review

This agent performs public, educational screening only. ANP statistics are operator-reported monthly figures; the open files contain no reservoir pressure, PVT or well geometry, and the by-well fluid data stop at 2023-12. Results must be reviewed by a qualified engineer.

See [AGENT.md](AGENT.md) for the full specification.
