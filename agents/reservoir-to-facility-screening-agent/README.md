# Reservoir-to-Facility Screening Agent

Coordinates early-stage, end-to-end screening of how a reservoir fluid flows from
the reservoir to the facility and how that develops over time. It chains:

1. `reservoir-depletion-screening` — reservoir pressure and gas/oil/water
   production versus time.
2. `production-network-routing` — well inflow (productivity index), manifold
   routing, and flowline/riser pressure drop to a platform arrival pressure.
3. `subsea-layout-geometry` and `step-out-screening` — optional layout and
   tie-back distance confirmation.

The result is a time-development picture of how falling reservoir pressure erodes
the arrival-pressure margin at the host.

This agent performs concept screening only. It does not replace reservoir
simulation, well/IPR design, multiphase hydraulics, or flow-assurance design.
A qualified human review is always required (`human_review_required: true`).

## Files

- `AGENT.md` — full agent definition, workflow, assumptions, and limitations.
- `agent.yaml` — catalog metadata.
- `examples/` — a worked screening checklist.
- `prompts/example-prompts.md` — example prompts.
- `tests/README.md` — how to exercise the agent.

## Validated NeqSim Path

For design-grade work use NeqSim `SimpleReservoir` (`runTransient`),
`PipeBeggsAndBrills`, and the NeqSim MCP `runReservoir` / `runPipeline` /
`runProcess` / `runFlowAssurance` tools, or the enterprise
`well-production-routing-agent`.

## License

Apache-2.0.
