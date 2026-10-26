# Brazil Offshore Infrastructure Agent

Public screening coordinator that locates Brazilian offshore fields, wells, FPSOs, gas pipelines and gas processing plants from ANP open data, measures distances from a discovery, and ranks tie-in hosts against a stand-alone development.

## Status

Draft (version 0.1.0). Screening only.

## Required skills

- `neqsim-anp-open-data` (version 0.2.0 or later, for the GeoServer reader and the tie-in ranking)
- `neqsim-brazil-offshore-infrastructure-market`
- `neqsim-step-out-screening`

## Human review

This agent performs public, educational screening only. ANP does not publish FPSO coordinates, host capacity, remaining life or offshore tariffs; positions are derived from wells and unknown facts are listed as gaps. Host data must be confirmed with the operator and the result reviewed by a qualified engineer.

See [AGENT.md](AGENT.md) for the full specification.
