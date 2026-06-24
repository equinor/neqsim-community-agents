# Example: Subsea Layout Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Subsea Layout Screening Agent turns a supplied subsea map into an early-stage layout inventory. It does not design tie-backs, routes, or subsea structures.

## Scenario

A supplied map of one host and three wells is screened for step-out distances and route profile.

Public synthetic inputs (Cartesian metres):

- Host: x=0, y=0, water depth=120 m
- W1: x=8000, y=1500, water depth=340 m
- W2: x=6000, y=-2000, water depth=330 m
- W3: x=12000, y=500, water depth=355 m
- Route waypoints (Host to W1): (0, 0, 120), (4000, 800, 300), (8000, 1500, 340)
- Seabed soundings (distance, depth): (0, 120), (4000, 300), (6000, 305), (8000, 340)

## Screening Steps

1. Confirm the objective: preliminary subsea layout triage only.
2. Run `field-layout-import` to normalize the map into a validated node list and surface data-quality issues.
3. Run `subsea-layout-geometry` to compute host-to-node step-out distances and a distance matrix.
4. Run `pipe-route-profile` to build the along-route horizontal and elevation profile and screen route slope.
5. Run `bathymetry-profile-screening` to interpolate seabed depth and flag candidate steep sections.
6. Record the warning levels and the most important uncertainties.
7. List required follow-up studies.

## Expected Screening Output Outline

- Normalized node count and any flagged data-quality issues
- Host-to-node step-out distances and a node-to-node distance matrix with a step-out warning level
- Route length and elevation profile with a slope warning level
- Bathymetry interpolation, candidate steep sections, and a slope warning level
- Recommended validated NeqSim routing and hydraulic workflows
- Assumptions, limitations, and a human review checklist

This output is an educational screening outline only and requires qualified human review before any design or operating decision.
