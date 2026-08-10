# Pipeline Survey Profile Agent

The Pipeline Survey Profile Agent turns an as-built pipeline survey or inspection export into a usable pipeline profile. It cleans and sign-normalises the survey, filters null markers and resolution, flags erroneous points instead of deleting them, trims the section between two structures, locates free-span and cover candidates along KP, compares repeat surveys, and hands the elevation profile to hydraulic and flow-assurance screening.

Every operation is written to a processing log that travels with the result, so the profile in a report can be traced back to the raw file.

This agent supports screening only. It does not perform DNV-RP-F105 free-span, DNV-RP-F109 on-bottom-stability, or DNV-RP-F114 pipe-soil assessment, it is not a positioning or datum authority, and it does not conclude that a pipeline has moved. A qualified human review is always required.

## Required Skills

- `pipeline-survey-processing` (`neqsim-pipeline-survey-processing`)
- `bathymetry-profile-screening` (`neqsim-bathymetry-profile-screening`)
- `pressure-drop-screening` (`neqsim-pressure-drop-screening`)
- `line-velocity-check` (`neqsim-line-velocity-check`)

## Context Skills

- `pipe-route-profile` (`neqsim-pipe-route-profile`)
- `subsea-layout-geometry` (`neqsim-subsea-layout-geometry`)
- `hydrate-margin-check` (`neqsim-hydrate-margin-check`)

## Public Scope

All inputs must be public, synthetic, or approved for open-source use. The agent performs no file or network access; survey records are supplied by the caller. Span, cover and change indicators are screening placeholders only. For design-grade work, use validated NeqSim pipeline workflows, the DNV screening kernels, and qualified pipeline engineering review.

## Related Agents

This agent is a companion to the `pipe-route-screening-agent`, which screens a route built from waypoints rather than a survey, to the `subsea-layout-screening-agent`, which places the structures that bound the section, and to the `flow-assurance-engineer-agent`.
