# Subsea Layout Screening Agent

The Subsea Layout Screening Agent coordinates early-stage interpretation of a supplied subsea map. It normalizes a provided field layout, computes step-out distances and a distance matrix, builds along-route elevation profiles, and screens seabed bathymetry for candidate steep sections using public, educational community skills.

This agent supports concept screening only. It does not design tie-backs, routes, or subsea structures, and it does not perform free-span, on-bottom-stability, or validated flow-assurance analysis. A qualified human review is always required, and this agent does not replace project assurance or design reviews.

## Required Skills

- `field-layout-import` (`neqsim-field-layout-import`)
- `subsea-layout-geometry` (`neqsim-subsea-layout-geometry`)
- `bathymetry-profile-screening` (`neqsim-bathymetry-profile-screening`)
- `pipe-route-profile` (`neqsim-pipe-route-profile`)

## Public Scope

All inputs must be public, synthetic, or approved for open-source use. The agent performs no file or network access; the subsea map is parsed by the caller and passed in as an already-parsed object. Distances, profiles, and slope flags are screening indicators only. For design-grade work, use validated NeqSim routing and hydraulic workflows and qualified subsea engineering review.

## Related Agents

This agent is a companion and upstream step to the `tie-in-screening-agent`.
