# Seabed Protection Agent

The Seabed Protection Agent scopes trenching, burial and rock dumping for a subsea flowline or export pipeline at concept stage. It samples public or project map layers along the route (seabed substrate, fishing intensity, ice scour, no-rock zones, existing pipelines), derives a hazard-driven cover requirement per segment, decides where the soil allows trenching and where it forces a rock dump, and sizes trench depth, rock volume and tonnage, crossing rock and free-span supports.

It hands the protected burial state to cooldown and hydrate-margin screening and asks for the unprotected case as well, so the margin that burial buys is visible in the flow-assurance study.

This agent supports screening only. It does not perform DNV-RP-F111 trawl-interference, DNV-RP-F110 upheaval-buckling, free-span, stability or pipe-soil assessment, and it does not replace pipeline engineering, geotechnical review or a contractor estimate. Trencher capability, rates and cover rules are placeholders until the project basis replaces them. A qualified human review is always required.

## Required Skills

- `seabed-protection-screening` (`neqsim-seabed-protection-screening`)
- `pipeline-survey-processing` (`neqsim-pipeline-survey-processing`)
- `surf-cooldown-screening` (`neqsim-surf-cooldown-screening`)
- `hydrate-margin-check` (`neqsim-hydrate-margin-check`)

## Context Skills

- `pipe-route-profile` (`neqsim-pipe-route-profile`)
- `bathymetry-profile-screening` (`neqsim-bathymetry-profile-screening`)
- `surf-field-layout-design` (`neqsim-surf-field-layout-design`)
- `subsea-layout-geometry` (`neqsim-subsea-layout-geometry`)

## Public Scope

All inputs must be public, synthetic, or approved for open-source use. The screening plans read-only requests to open map services (EMODnet, Norwegian Offshore Directorate FactMaps) and works on GeoJSON that the caller supplies; it performs no network access itself. For internal map services, the enterprise agents read the layers and supply the same GeoJSON.

## Related Agents

This agent is a companion to the `pipe-route-screening-agent`, the `pipeline-survey-profile-agent`, which supplies surveyed cover and free-span candidates, the `surf-layout-design-agent`, the `subsea-cooldown-agent` and the `flow-assurance-engineer-agent`.
