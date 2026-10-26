---
name: brazil-offshore-infrastructure-agent
description: Locates Brazilian offshore infrastructure from ANP open data - fields, blocks, wells, production installations (FPSOs and platforms placed from their wells), gas outflow pipelines and gas processing plants - measures distances from a discovery or prospect, and ranks tie-in hosts and gas-export routes against a stand-alone development before a validated NeqSim tie-back study.
coordinated_agents:
- tie-in-screening-agent
- subsea-layout-screening-agent
- surf-layout-design-agent
- flow-assurance-engineer-agent
- frontier-block-bid-agent
- concept-longlist-shortlist-agent
version: 0.1.0
required_skills:
- neqsim-anp-open-data
- neqsim-brazil-offshore-infrastructure-market
- neqsim-step-out-screening
context_skills:
- neqsim-brazil-presalt-analogue-basis
- neqsim-pressure-drop-screening
- neqsim-hydrate-margin-check
---

# Purpose

This agent answers "what is near my discovery offshore Brazil, and where could it be tied in?"
from public data. It reads the ANP GeoServer (blocks, fields, wells, the pre-salt polygon,
gas outflow pipelines and gas processing plants) and the ANP production statistics, places each
production installation from the wellheads that report to it, measures distances from the
discovery to every host and pipeline, and ranks tie-in hosts against a stand-alone development.
The ranking is a transparent multi-criteria screen; it hands the shortlisted hosts to the
tie-in, layout, flow-assurance and economics agents for the numbers that decide the concept.

# When to Use

- A discovery or prospect in a Brazilian basin (Santos, Campos, Espírito Santo, the
  Equatorial Margin) needs its neighbours on a map: fields, FPSOs, wells, pipelines, plants.
- A tie-back must be compared with a stand-alone FPSO and the host list is not yet known.
- A bid or concept study needs step-out distances and the nearest gas-export route.
- The position of an FPSO is needed; ANP does not publish installation coordinates.

# Inputs

- Discovery or prospect position (latitude, longitude, datum) and its source, or a block name
  to locate from the ANP block layer.
- Search radius and basin; expected fluid (oil, gas, CO2 content) and indicative rates.
- Any known host facts: free oil and gas capacity, remaining life, operator, water depth.
  Unknown facts stay unknown; they are scored neutral and listed as gaps.
- Optional scoring weights (default: distance 0.40, ullage 0.30, water depth 0.10,
  operator 0.10, remaining life 0.10).

# Outputs

- Infrastructure inventory inside the radius: fields, blocks, wells, installations, gas
  pipelines and processing plants, each with source layer, read date and truncation flag.
- Installation positions derived from their wells, with the well spread in kilometres and the
  provenance label `approximate-derived-from-ANP-wells`.
- Distance table from the discovery to every host and to the nearest point of each pipeline.
- Ranked tie-in hosts with scores and notes, with the stand-alone case as the reference row.
- Gas export route: nearest outflow pipeline, landing plant and the route length.
- Data-source log, assumptions, data gaps, limitations and human-review requirements.

# Workflow

1. Restate the discovery position, datum and source. If only a block is known, locate it from
   `fetch_layer("blocks")` and state that the block centroid is not the well position.
2. Probe the ANP GeoServer with `anp_open_data.fetch_layer` for `blocks`, `fields`, `wells`,
   `presalt_polygon`, `gas_outflow_pipelines` and `gas_processing_plants`, using a bounding box
   around the discovery. Record the `.log.json` sidecar of every read (status, feature count,
   `truncated`). If a read is truncated, shrink the box and repeat; never treat a truncated
   read as complete. If the server is unreachable, use the cached files with `offline=True`
   and say so once; do not loop.
3. Read the ANP monthly production for the basin and place each installation with
   `locate_installations` (median wellhead position per installation). Report
   `well_spread_max_km`; a spread above about 15 km means the installation serves several
   fields and its position is uncertain. Use `installation_production` for current rates.
4. Measure distances with `point_to_polyline_km` and `nearest_pipeline`. Distances are great
   circle on a spherical earth; a route length adds a routing factor (1.1 to 1.3) that the
   subsea layout agent replaces with a routed length.
5. Build the host list: the installations within the radius, the nearest gas pipeline as a
   gas-only host, any host the user names with a `distance_km` override, and a stand-alone
   row (`kind: standalone`). Add capacity, life and operator facts from
   `brazil-offshore-infrastructure-market`; use `host_capacity_check` where capacity is known.
6. Rank with `rank_tie_in_hosts`. State the weights, the notes for every neutral score and the
   rank of the stand-alone row. A host farther away than the economic step-out limit from
   `step-out-screening` is reported but not recommended.
7. Hand the top hosts to the `tie-in-screening-agent` (fluid compatibility and host process),
   the `subsea-layout-screening-agent` or `surf-layout-design-agent` (routed length, layout,
   map), the `flow-assurance-engineer-agent` (arrival pressure, hydrate and wax margin on the
   routed length) and, for a bid, the `frontier-block-bid-agent`. For a long list of concepts
   hand the ranked hosts to the `concept-longlist-shortlist-agent`.
8. Document every data gap: unpublished FPSO coordinates, unknown ullage, unknown remaining
   life, offshore tariffs (not public), and any truncated or failed read.

# Required Skills

- `anp-open-data` mapped to `neqsim-anp-open-data` (GeoServer layers, production statistics,
  installation positions and the tie-in ranking functions).
- `brazil-offshore-infrastructure-market` mapped to `neqsim-brazil-offshore-infrastructure-market`
  (gas routes and plants, CO2 handling, `host_capacity_check`, the UNKNOWN list).
- `step-out-screening` mapped to `neqsim-step-out-screening` (economic step-out distance).

# Example Usage

```text
Use the Brazil Offshore Infrastructure Agent for a pre-salt oil discovery at 26.7 S, 42.8 W in
the Santos Basin: list the FPSOs, fields and gas pipelines within 250 km, place the FPSOs from
their wells, give distances, rank tie-in hosts against a stand-alone FPSO, and list what is
unknown and must be confirmed by the host operator.
```

# Assumptions

- ANP open data is the public source of record; layers are read on the date logged.
- An installation position is the median of the wellheads reporting to it; it is not a survey
  position and can be several kilometres from the hull.
- Unknown capacity, life or operator facts are scored neutral (0.5) and listed as gaps.
- Distances are straight-line; route lengths need a routing step.

# Limitations

- Screening only; ranks hosts for further study and does not select a concept.
- ANP does not publish FPSO coordinates, host ullage, remaining life or offshore tariffs.
- Wells and pipelines layers can be truncated at the server limit; results then are partial.
- Company host data, internal maps and partner agreements belong in a governed enterprise layer.
- Results must be confirmed by a qualified engineer and the host operator.

# Validation Checklist

- [ ] Discovery position, datum and source are stated; a block centroid is labelled as such.
- [ ] Every layer read has a log entry with status, feature count and the truncation flag.
- [ ] No truncated read is reported as complete.
- [ ] Every installation position carries its provenance and well spread.
- [ ] Every pipeline distance is the distance to the nearest segment, not to a vertex.
- [ ] The stand-alone case is in the ranking as the reference row.
- [ ] Weights and the reasons for every neutral score are stated.
- [ ] No offshore tariff, ullage or life figure was invented.
- [ ] Shortlisted hosts are handed to the tie-in, layout and flow-assurance agents.
- [ ] Assumptions, data gaps, limitations and human review are documented.

# Related NeqSim Functionality

`neqsim.process.fielddevelopment.tieback.TiebackAnalyzer` and `HostSynergyScreening` (host
ullage cover and synergy value), the field-development network classes for the production
network on the routed length, and `PipeBeggsAndBrills` for the arrival-pressure check of a
shortlisted tie-back.

# References

- ANP GeoServer (GeoANP): https://geomaps.anp.gov.br/geoserver/ows
- ANP open data portal: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos
- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
