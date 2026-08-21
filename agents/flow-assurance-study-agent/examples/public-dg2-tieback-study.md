# Example: Public Synthetic DG2 Tieback Study

This example contains no field-specific or confidential data.

## Decision

Assess whether a 120 km gas-condensate tieback has a defensible DG2
flow-assurance basis and identify which uncertainties require further work.

## Coordinator plan

| Stage | Existing agent | Handoff |
| --- | --- | --- |
| Evidence intake | `technical-document-intelligence-agent` | Source register with confidence and gaps |
| Fluid basis | `pvt-agent` | Quality-checked composition and PVT range |
| Route basis | `pipe-route-screening-agent` | Normalized geometry and boundary basis |
| Steady hydraulics | NeqSim `TwoFluidPipe` workflow | Base, turndown, and high-rate profiles with convergence evidence |
| Simple backup/topside check | NeqSim `PipeBeggsAndBrills` | Non-governing screening cross-check within its applicability range |
| Operating limits | `flow-assurance-engineer-agent` | Hydrate and wax margin flags |
| Pipeline validation/transients | `olga-simulation-agent` | Design-critical comparison, shutdown/restart, and liquid-surge trends |
| Cooldown | `subsea-cooldown-agent` | No-touch-time screen |
| Integrity | `piping-integrity-agent`, `sand-erosion-agent` | Velocity, vibration, wall, and erosion flags |

## Required gates

1. Freeze fluid, route, pipe, insulation, ambient, and boundary data before runs.
2. Accept NeqSim results only after convergence, plausibility, and grid checks.
3. Reconcile all comparison inputs before interpreting NeqSim/OLGA deviations.
4. Compare at least three matched rates and an independent hand check.
5. Keep missing evidence and specialist disagreements visible.
6. Obtain qualified human review before any recommendation becomes a decision.
