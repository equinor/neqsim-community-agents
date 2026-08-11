# Example: SURF Layout Design Checklist

This example uses public, synthetic data only. It shows how the SURF Layout Design Agent turns a well count and a reservoir footprint into a placed, routed and sized subsea layout. It does not design tie-backs, routes or subsea structures, and a qualified subsea engineering review is required before any of it is used.

## Scenario

A shallow Barents Sea style oil field in 400 m of water, on a licence block used only for orientation.

Public synthetic inputs:

- Wells: 8 producers, 6 water injectors, 2 gas injectors, 4 slots per template
- Reservoir footprint: 6.0 km by 3.1 km, field axis bearing 30 degrees
- Injector offset off the producer axis: 1.2 km
- Host: weathervaning FPSO, 2.5 km from the field centre on a bearing of 270 degrees, riser base 350 m short of it
- Production architecture: round-trip-piggable dual loop
- Design rates at the flowing condition: 0.330 m3/s liquid, 0.231 m3/s injection water, 0.088 am3/s injection gas
- Densities: 850 kg/m3 liquid, 1025 kg/m3 injection water, 90 kg/m3 injection gas

## Design Steps

1. Confirm the objective: concept-level SURF architecture and quantity take-off only.
2. Take the well count and the design rates from the reservoir side, and convert every standard rate to an actual volumetric rate before sizing.
3. Plan the open bathymetry, licence-block and infrastructure requests with `surf-field-layout-design`, and record the licence and attribution of each source. Execute them only with a read-only fetch adapter the user supplies.
4. Run `surf-field-layout-design` to place the drill centres, wells, Xmas trees, templates, PLEMs, riser base and host, and to route and size every line.
5. Replace the flat seabed with the open bathymetry grid through `bathymetry-profile-screening` and `pipe-route-profile`, and re-check the route and riser lengths.
6. Screen step-outs and tie-back distances with `subsea-layout-geometry`.
7. Check every selected size independently with `line-velocity-check`.
8. Record the warning levels and the most important uncertainties.

## Expected Screening Output

- 2 production drill centres, 2 water-injection drill centres, 1 gas-injection drill centre
- 16 wells and 16 Xmas trees, 5 templates with integrated manifolds, 5 flowline PLEMs plus the riser base PLEM
- Four production flowline legs forming two round-trip pigging loops
- A production flowline size that keeps the velocity under both the 3 m/s target and the API RP 14E erosional velocity
- Total flowline, umbilical and riser lengths for the SURF cost estimate
- A warning that the flat seabed must be replaced before any length is used for cost or hydraulics

## Required Follow-up

- Detailed routing with obstacle avoidance, corridor and crossing design
- On-bottom stability, free-span, expansion and buckling analysis
- Pressure-containment wall-thickness design
- Riser configuration and response analysis, and the host mooring pattern and heading
- Flow-assurance design: hydrate, wax, cooldown and insulation
- Qualified subsea engineering review and project assurance
