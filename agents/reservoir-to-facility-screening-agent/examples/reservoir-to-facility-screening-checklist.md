# Reservoir-to-Facility Screening Checklist (Worked Example)

Public, synthetic example. No proprietary data is used.

## Scenario

A gas field is screened from reservoir to facility:

- Reservoir: gas, 20 Gsm3 recoverable, declining from 300 to 80 bara,
  8 MSm3/day offtake, 15-year horizon, water cut starting at 5 % rising 3 %/year.
- Two production wells route through one manifold:
  - WELL-A: reservoir 300 bara, bottomhole 250 bara, PI 1.0e5 Sm3/day/bar, THP 140 bara.
  - WELL-B: reservoir 295 bara, bottomhole 240 bara, PI 0.9e5 Sm3/day/bar, THP 135 bara.
- MANIFOLD-1: 8 km flowline at 1.5 bar/km, 20 bar riser drop.
- Host requires 90 bara arrival.

## Step 1 — Reservoir versus time (`reservoir-depletion-screening`)

- Build the year-by-year pressure, cumulative production, recovery factor, and
  water-cut profile.
- Note the plateau years and the year the reservoir reaches abandonment.
- Record the depletion warning level.

## Step 2 — Layout confirmation (optional)

- Use `subsea-layout-geometry` and `step-out-screening` to confirm the
  well/manifold/host positions and tie-back step-out distances are sensible.

## Step 3 — Network routing (`production-network-routing`)

- Estimate per-well inflow rate from drawdown and productivity index.
- Aggregate rates at MANIFOLD-1.
- Roll up the arrival pressure: manifold pressure (lowest routed THP) minus
  flowline drop minus riser drop.
- Compare to the 90 bara requirement and record the margin and warning.

## Step 4 — Time development

- Combine Step 1 and Step 3: as reservoir pressure falls, bottomhole/tubing-head
  pressures and rates fall, eroding the arrival-pressure margin.
- Identify the screening year when arrival pressure can no longer be sustained.

## Step 5 — Escalation

- Replace every step with validated NeqSim tools: `SimpleReservoir`
  (`runTransient`) for the reservoir, `PipeBeggsAndBrills` for the multiphase
  flowline/riser, and MCP `runReservoir` / `runPipeline` / `runFlowAssurance`
  for arrival conditions and flow assurance.
- Complete a qualified human review before any design or operating decision.

## Validation Notes

- All numbers above are illustrative placeholders.
- The reservoir and network steps are transparent screening algebra, not
  validated reservoir or hydraulic results.
- Human review is mandatory.
