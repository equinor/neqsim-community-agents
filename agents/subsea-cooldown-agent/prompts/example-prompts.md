# Example Prompts

These prompts illustrate how to use the Subsea Cooldown Agent with public, synthetic, or approved data only. The agent performs early-stage screening and always requires qualified human review.

## No-Touch-Time Screening from a Known Time Constant

```text
Screen a subsea shut-in case for cooldown no-touch time. The initial temperature is 40 C, the seabed temperature is 4 C, the hydrate equilibrium temperature from a validated NeqSim calculation is 20 C, and the cooldown time constant is 18 hours. Report the no-touch time and the verdict, and recommend validated NeqSim cooldown and hydrate workflows.
```

## Time Constant from Lumped Geometry

```text
Estimate a lumped cooldown time constant for a flowline with a fluid density of 850 kg/m3, a specific heat of 2200 J/kgK, an internal diameter of 0.25 m, and an overall heat transfer coefficient of 5 W/m2K. Then screen the no-touch time for an initial temperature of 40 C, a seabed temperature of 4 C, and a hydrate equilibrium temperature of 20 C.
```

## Required No-Touch-Time Check

```text
Using public synthetic data, screen a shut-in case against a required no-touch time of 12 hours. Flag the case if the estimated no-touch time appears insufficient, list the required follow-up studies, and prepare a cooldown screening report outline with clear assumptions, limitations, and a human review checklist.
```

## Report Outline

```text
Prepare a transparent cooldown screening report outline based on the no-touch-time indicator. Separate facts, assumptions, and recommendations, and state that the results are educational placeholders that do not replace qualified flow assurance review.
```
