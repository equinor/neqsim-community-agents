# Pipe Route Screening Agent

The Pipe Route Screening Agent coordinates early-stage screening of a candidate pipe route. It builds an along-route elevation profile from ordered waypoints, then screens the route for single-phase pressure drop, line velocity, and hydrate temperature margin against public, educational guidelines using community skills.

This agent supports concept screening only. It does not design routes or pipelines, and it does not perform multiphase, transient, or validated flow-assurance analysis. A qualified human review is always required, and this agent does not replace project assurance or design reviews.

## Required Skills

- `pipe-route-profile` (`neqsim-pipe-route-profile`)
- `pressure-drop-screening` (`neqsim-pressure-drop-screening`)
- `line-velocity-check` (`neqsim-line-velocity-check`)
- `hydrate-margin-check` (`neqsim-hydrate-margin-check`)

## Public Scope

All inputs must be public, synthetic, or approved for open-source use. The agent performs no file or network access; route waypoints and fluid properties are supplied by the caller. Pressure-drop, velocity, and hydrate-margin indicators are screening placeholders only. For design-grade work, use validated NeqSim hydraulic and flow-assurance workflows and qualified pipeline engineering review.

## Related Agents

This agent is a companion to the `subsea-layout-screening-agent`, which prepares the route geometry, and to the `flow-assurance-engineer-agent`.
