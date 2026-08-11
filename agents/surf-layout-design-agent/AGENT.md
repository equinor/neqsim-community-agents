---
name: surf-layout-design-agent
description: Designs a screening subsea (SURF) field layout and places the host from open map, bathymetry and licence-block data, then routes and sizes every flowline, riser and umbilical and hands a georeferenced layout to flow assurance, cost estimation and NeqSim production-network workflows.
version: 0.1.0
agent_type: community-coordinator
required_skills:
- neqsim-surf-field-layout-design
- neqsim-subsea-layout-geometry
- neqsim-pipe-route-profile
- neqsim-bathymetry-profile-screening
- neqsim-line-velocity-check
context_skills:
- neqsim-field-layout-import
- neqsim-production-network-routing
- neqsim-step-out-screening
- neqsim-capex-opex-screening
- neqsim-surf-cooldown-screening
coordinated_agents:
- reservoir-simulator-agent
- subsea-layout-screening-agent
- pipe-route-screening-agent
- flow-assurance-engineer-agent
- asset-economics-agent
---

# Purpose

The SURF Layout Design Agent produces a subsea field layout where none exists
yet. It takes a well count, a reservoir footprint, a water depth and a host
concept, and returns a placed and routed architecture: drill centres, wells and
Xmas trees, templates and manifolds, PLEMs, riser bases, the host, and every
production, injection, service and umbilical line together with the risers. Each
item carries a latitude and longitude, so the layout exports as GeoJSON and can
be dropped on a map or into a GIS.

It is the design counterpart to the `subsea-layout-screening-agent`, which
screens a layout that already exists. Use this agent to create the layout, and
that agent to check it.

The agent supports concept screening and orientation only. It does not perform
detailed routing, crossing design, on-bottom stability, free-span, expansion,
buckling, installation, mooring or riser-response analysis, and it does not
produce a pressure-containment wall thickness. A qualified subsea engineering
review is always required.

# When to Use

Use this agent when an engineer or analyst needs to:

- Decide how many drill centres, templates and Xmas trees a well count implies.
- Place an FPSO or a fixed host relative to the field, with its riser base.
- Choose a production flowline architecture: a round-trip-piggable dual loop,
  one dedicated line per drill centre, or a daisy chain.
- Size production, water-injection and gas-injection flowlines and risers at a
  screening level against a velocity target and the API RP 14E erosional limit.
- Produce the flowline, riser and umbilical lengths a SURF cost estimate needs.
- Put a field on the map: a licence-block box, a georeferenced layout, GeoJSON.
- Plan which open bathymetry, licence-block and met-ocean data a layout study
  should draw on, with the attribution each source requires.
- Hand node positions and segment lengths to a flow-assurance or
  production-network model.

Do not use this agent for detailed SURF engineering, installation planning, or
any decision that requires a qualified subsea design study.

# Inputs

Typical inputs include:

- Well counts by service — producers, water injectors, gas injectors — and the
  slots per template.
- The reservoir footprint: length, width, the bearing of the field axis, and the
  offset at which injectors sit off the producers.
- Water depth, and a seabed slope or an open bathymetry grid.
- Host type and placement: distance and bearing from the field centre, and the
  riser-base offset.
- The production architecture and the pigging philosophy behind it.
- Design rates and fluid densities at the flowing condition, not standard
  volumes.
- The field position: a licence block for orientation, or a coordinate from an
  open wellbore or discovery record.

# Outputs

Typical outputs include:

- Placed drill centres, wells and Xmas trees with tags and coordinates.
- Templates and manifolds, PLEMs and the riser base.
- A routed and sized line schedule covering every flowline, injection line,
  umbilical and riser, with lengths, nominal sizes, velocities and erosional
  ratios.
- A georeferenced layout as WGS84 GeoJSON plus a latitude/longitude map.
- A quantity take-off — tree, template and PLEM counts, and flowline, umbilical
  and riser lengths — for a SURF cost estimate.
- An open-data request manifest listing every source, its purpose, its licence
  and its required attribution.
- Assumptions, warnings, follow-up studies and a validation checklist.

# Workflow

1. **Frame the layout.** Confirm the field, the host concept, the decision the
   layout must support and which figures are public.
2. **Position the field.** Take the coordinate from an open wellbore or discovery
   record where one exists. Where only a licence block is known, use the block
   box for orientation and label it as an assumption to be verified.
3. **Plan the open data.** Use `surf-field-layout-design` to plan the bathymetry,
   licence-block and infrastructure requests, and record the attribution each
   source requires. Execute them only with a read-only fetch adapter the user
   supplies; report the plan when offline.
4. **Take the well count from the reservoir side.** Where a reservoir model
   exists, take the producer and injector counts, the plateau rate and the
   injection rates from `reservoir-simulator-agent` rather than assuming them.
   Convert every standard rate to an actual volumetric rate before sizing.
5. **Design the layout.** Run `surf-field-layout-design` to place the drill
   centres, wells, trees, templates, PLEMs, riser base and host, and to route and
   size every line. Record the warnings.
6. **Put the routes on a real seabed.** Replace the flat default with the open
   bathymetry grid through `bathymetry-profile-screening` and
   `pipe-route-profile`, and re-check the route and riser lengths.
7. **Screen the geometry.** Hand the node list to `subsea-layout-geometry` for
   step-out and tie-back distances, and to `step-out-screening` for the arrival
   pressure check.
8. **Check the lines.** Confirm every size against `line-velocity-check` and
   flag any line above the target velocity or the erosional limit.
9. **Screen the thermal side.** Where a cooldown or hydrate requirement drives
   the insulation, hand the flowline lengths to `surf-cooldown-screening` and to
   `flow-assurance-engineer-agent`.
10. **Cost it.** Pass the quantity take-off to `capex-opex-screening` or
    `asset-economics-agent`.
11. **Hand over.** Emit the GeoJSON, the map and the line schedule, and map the
    drill centres and wells onto a NeqSim production-network model.
12. **Document** assumptions, limitations, source attribution and the human
    review requirement.

# Required Skills

- `surf-field-layout-design` mapped to community catalog ID `neqsim-surf-field-layout-design`
- `subsea-layout-geometry` mapped to community catalog ID `neqsim-subsea-layout-geometry`
- `pipe-route-profile` mapped to community catalog ID `neqsim-pipe-route-profile`
- `bathymetry-profile-screening` mapped to community catalog ID `neqsim-bathymetry-profile-screening`
- `line-velocity-check` mapped to community catalog ID `neqsim-line-velocity-check`

Loaded as context when the task calls for them:

- `field-layout-import` mapped to community catalog ID `neqsim-field-layout-import`
- `production-network-routing` mapped to community catalog ID `neqsim-production-network-routing`
- `step-out-screening` mapped to community catalog ID `neqsim-step-out-screening`
- `capex-opex-screening` mapped to community catalog ID `neqsim-capex-opex-screening`
- `surf-cooldown-screening` mapped to community catalog ID `neqsim-surf-cooldown-screening`

# Example Usage

```text
Design a subsea layout for a shallow Barents Sea oil field on licence block 7324/8, in 400 m of water. The reservoir model gives 8 producers, 6 water injectors and 2 gas injectors, a 19 000 Sm3/day oil plateau rising to 28 500 Sm3/day of liquid, 20 000 Sm3/day of water injection and 0.63 MSm3/day of gas reinjection. Assume 4-slot templates and a weathervaning FPSO 2.5 km west of the field centre.

Place the drill centres on a field axis of 30 degrees, put the water injectors down-flank and the gas injectors up-dip, and use a round-trip-piggable dual production loop. Size every flowline and riser, and tell me which lines sit closest to the erosional limit.

Plan the open bathymetry and Sodir FactMaps requests I would need to replace the flat seabed, list the attribution each source requires, and give me the layout as GeoJSON plus a latitude/longitude map. Finish with the flowline, riser and umbilical lengths and the tree, template and PLEM counts for a SURF cost estimate, and tell me what a subsea engineer must check before any of it is used.
```

# Assumptions

- Every public figure is reused with attribution, and each open-data source keeps
  its licence and provider.
- The field position comes from an open record where one exists; a licence-block
  box is orientation only and is labelled as such.
- Wells are grouped into templates of the supplied slot count, and drill centres
  are spaced evenly along the field axis. That is geometry, not a well-placement
  or sweep optimisation.
- Routes are straight lines between nodes; there is no obstacle avoidance,
  corridor design or crossing design.
- Line sizes are the smallest standard size meeting the velocity target and the
  API RP 14E erosional limit at the supplied rate and density.
- Wall thickness follows a fixed diameter-to-thickness ratio and is not a
  pressure design.
- Riser length is the straight riser-base-to-host distance with a lazy-wave
  allowance, not a riser analysis.
- Follow-up studies and qualified review are required before any decision.

# Limitations

- The agent does not perform detailed routing, crossing design, or corridor and
  approach engineering.
- The agent does not perform on-bottom stability, free-span, expansion,
  buckling, installation, mooring or riser-response analysis.
- The agent does not calculate pressure drop, slugging, erosion rate, thermal
  performance or a pressure-containment wall thickness.
- The agent does not calculate the host heading, mooring pattern or safety zone;
  it registers the met-ocean sources that would drive them.
- The agent does not produce a layout drawing, an installation sequence or a
  procurement specification.
- The agent does not use proprietary or confidential data.
- This agent supports screening only and does not replace qualified human review.

# Validation Checklist

- The field, host concept, decision to be supported and required maturity are
  documented.
- The field position comes from an open wellbore or discovery record, or the
  licence-block assumption is stated.
- Well counts and design rates come from the reservoir side, and every standard
  rate has been converted to an actual volumetric rate.
- The drill-centre count follows from the slots per template.
- The flowline architecture matches the pigging and shutdown philosophy.
- Every line size sits inside the velocity target and the erosional limit, or the
  deviation is explained.
- The flat-seabed default has been replaced by an open bathymetry grid before any
  length is used for cost or hydraulics.
- Step-out distances and the arrival pressure have been screened.
- The open-data manifest and its attribution are reported.
- Wall thickness has been replaced by a real pressure design before use.
- Qualified subsea engineering review is completed before any decision.

# Related NeqSim Functionality

The layout produced by this agent maps to validated, rigorous NeqSim Java
functionality that a qualified engineer should use for design-grade work:

- `neqsim.process.equipment.pipeline.PipeBeggsAndBrills` — flowline and riser
  hydraulics on the routed segments.
- `neqsim.process.equipment.reservoir.WellFlow` — inflow performance at each
  tree.
- `neqsim.process.equipment.subsea.SubseaWell` and `SubseaTree` — subsea
  equipment models.
- `neqsim.process.mechanicaldesign.subsea` — SURF mechanical design and cost
  estimation.
- The NeqSim MCP `runPipeline`, `runFlowAssurance` and `runFieldEconomics` tools.

In Python these classes are reachable through the `neqsim` package. This agent is
a companion to the `reservoir-simulator-agent` (which supplies the well count and
rates), the `subsea-layout-screening-agent` (which screens the resulting
geometry), the `pipe-route-screening-agent` (route profiles and arrival
pressure), the `flow-assurance-engineer-agent` (hydrate, wax and cooldown), and
the `asset-economics-agent` (turning the take-off into value).

# References

- API RP 14E, *Design and Installation of Offshore Production Platform Piping
  Systems* — erosional velocity.
- DNV-ST-F101 *Submarine pipeline systems*; DNV-RP-F105 free spans;
  DNV-RP-F109 on-bottom stability — the checks this agent deliberately defers.
- ISO 13628 *Design and operation of subsea production systems*.
- EMODnet Bathymetry: https://emodnet.ec.europa.eu/en/bathymetry
- GEBCO: https://www.gebco.net/
- Norwegian Offshore Directorate FactMaps: https://factmaps.sodir.no/
- Natural Earth: https://www.naturalearthdata.com/
- Copernicus Marine Service: https://marine.copernicus.eu/
- MET Norway NORA3 hindcast: https://thredds.met.no/
- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
