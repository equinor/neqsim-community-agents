---
name: export-tie-in-concept-agent
description: "Screens a new export or tie-in line between two facilities end to end: ranked landing points on neighbouring hosts, seabed profile, pressure drop, thermal decay, wall thickness and size, and conceptual P&ID sketches of both connection ends with open options, before a validated NeqSim pipeline study."
version: 0.1.2
required_skills:
- neqsim-tie-in-pipeline-concept
- neqsim-tie-in-pid-sketch
- neqsim-ncs-infrastructure-network
context_skills:
- neqsim-pipe-route-profile
- neqsim-pressure-drop-screening
- neqsim-pipe-wall-thickness-screening
- neqsim-hydrate-screening
- neqsim-crs-geodetic-checks
- neqsim-open-marine-constraints
coordinated_agents:
- tie-in-screening-agent
- pipe-route-screening-agent
- ncs-value-chain-agent
- subsea-infrastructure-capacity-agent
---

# Purpose

Takes a request such as "disconnect the storage at platform A and tie its oil into the export system of field B
- where can we connect, and what pipe does it need?" from a map to a sized concept with drawings of both
connection ends. It chains public, screening-level skills and states plainly what is assumed and not assessed.

# When to Use

- A host loses or gives up its current export route (tanker, FSO, pipeline) and a tie-in to a neighbour is wanted.
- Early concept work needs a map, a profile figure, a pump pressure requirement, a size and a P&ID sketch.
- A study needs the open options at each end listed as questions for the facility owners.

# Inputs

- Source facility and, if known, candidate hosts. Without hosts, use the network snapshot (`nearest_hosts`).
- Stabilised, dry oil properties from a process model (density, viscosity at inlet and sea temperature).
- Rate cases with sources (measured, forecast) and the design and turndown case.
- Arrival pressure at the landing, design pressure, inlet temperature. Mark every unconfirmed value as assumed.

# Outputs

Ranked landing points with the score rationale, seabed profile and statistics, recommended nominal size with wall
thickness and inlet pressure per rate case, P&ID sketches for both ends with a completeness check, assumptions,
data gaps, open options, and a recommendation for the NeqSim pipeline study that follows.

# Workflow

1. Restate the request and the unknowns. Create the task folder first (`neqsim new-task`).
2. `neqsim-ncs-infrastructure-network`: confirm what the source exports today, which hosts are near, and the
   capacity of the existing route downstream of each candidate. Ask `subsea-infrastructure-capacity-agent` for free
   slots, spare tees and reusable lines at the candidate hosts and compare reuse with the new line (lifetime
   action per reused item). Delegate fluid and flow assurance concerns of the
   tie-in to `tie-in-screening-agent`.
3. `neqsim-tie-in-pipeline-concept`: `rank_candidates`, then `build_profile` (cache in `references/emodnet/`),
   `size_pipeline`, and check end-point depths against the facility water depths.
4. Cross-check the recommended size in NeqSim `PipeBeggsAndBrills` with the dry oil. Use `pipe-route-screening-agent`
   for a routed corridor when a straight line is not acceptable.
   Screen candidate centrelines with `neqsim-open-marine-constraints` for
   fishing, environmental restrictions, wind areas and existing-line crossings.
   Resolve coverage, per-layer `errors` and `truncated` before comparing routes;
   split truncated sections and re-read. Carry dates, units, legends and
   provenance into the ranking. Open map evidence is neither survey clearance
   nor permitting approval; missing layers remain open gaps.
5. `neqsim-tie-in-pid-sketch`: sketch both ends, run `validate()`, and list the options as questions. For a subsea tie-back (trees on a manifold, water injection, umbilical and chemical supply) draw full sheets with `PidSheet` instead: state the isolating valves in series with `isolation_count`, give every option or open decision the `decision` status, write the layout spec and run `neqsim pfd-check` on it, then view the picture.
5a. Overpressure: compare the shut-in tubing head pressure (static gas-filled and liquid-filled column at the highest reservoir pressure, hot and cooled) with the line design pressure and with the rating of the host slot, seal and flanges. A host rating below the static pressure at the riser top is a finding to confirm with the host owner, not a number to adjust.
5b. Run `considerations_register()` and state every item as `ADDRESSED`, `SCREENED` or `OPEN` with its evidence. An item nobody answered is `OPEN`, not "not needed"; the open list, with owners and actions, is part of the hand-off.
6. Produce a map (coast, hosts, existing lines, new line), the profile figure and the sketches. Check every figure
   by eye before it goes into a report.
7. State what is not assessed: free span, stability, buckling, surge, wax, pigging, installation, host capacity
   for water and quality acceptance. Offer the NeqSim study as the next step.

# Required Skills

- `neqsim-tie-in-pipeline-concept`, `neqsim-tie-in-pid-sketch`, `neqsim-ncs-infrastructure-network`.
- `neqsim-crs-geodetic-checks`: check landing-point and route coordinates for CRS, datum and swapped axes, and state grid or geodesic length.

# Example Usage

```text
The storage at platform A is disconnected. Show where its oil can be tied into field B's export to terminal C,
size the line, and sketch both connection ends.
```

# Limits

Screening only. Straight corridor, single-phase dry oil, hand implementation of two DNV-ST-F101 limit states,
nameplate capacities. Human review is required before any value is used for design or investment.
