# VFP Lift Curve Agent

Turns a calibrated NeqSim well, flowline and topside model into a deck-ready `VFPPROD` or `VFPINJ` keyword for
Eclipse or OPM Flow.

It does not hand-build a pipeline: it selects the curve type (tubing-only, flowline or full-system), designs the
axes, drives NeqSim's `VfpTableBuilder` with a lift model, validates the table (round trip, off-grid solves,
IPR x VFP, monotonicity) and exports it with a provenance header. Human review of the calibration and of a
single-well simulator run is required, and the agent does not replace engineering judgement.

## Skills

| Skill | Role |
| --- | --- |
| `neqsim-vfp-lift-curves` | the builder API, axis design, correlation choice, rate caps, deck conventions, validation and traps |
| `neqsim-api-patterns` | building the NeqSim fluids and models the lift providers wrap |

## Works with

| Agent | Role |
| --- | --- |
| `near-well-injectivity-agent` | the inflow relationship (productivity index, IPR) that the table is solved against, and the OPM Flow deck side |
| `reservoir-simulator-agent` | the reservoir model the table is used in |
| `flow-assurance-engineer-agent` | arrival temperature and hydrate margin from the same chain |

## What it will not do

It does not derive productivity indices, size equipment or run the user's reservoir model. Company data retrieval is
handled by the enterprise counterpart.
