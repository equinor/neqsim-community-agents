# Subsea Cooldown Screening Checklist (Example)

This public example shows how the Subsea Cooldown Agent screens a shut-in case for cooldown no-touch time using synthetic data. It is educational only and does not replace qualified flow assurance review.

## 1. Screening Objective

- Confirm whether a subsea flowline keeps enough no-touch time before it cools into the hydrate region after shut-in.
- Decision criteria: no-touch time at least 12 hours before the fluid reaches the hydrate equilibrium temperature.

## 2. Public Synthetic Inputs

| Parameter | Value | Unit |
| --- | --- | --- |
| Initial temperature | 40.0 | C |
| Seabed temperature | 4.0 | C |
| Hydrate equilibrium temperature | 20.0 | C |
| Cooldown time constant | 18.0 | hours |
| Required no-touch time | 12.0 | hours |

The hydrate equilibrium temperature is assumed to come from a validated NeqSim calculation. The time constant is assumed to come from a lumped estimate or a validated cooldown calculation.

## 3. No-Touch-Time Screening

Using `surf-cooldown-screening`:

- The fluid follows a lumped exponential cooldown from 40 C toward 4 C with a time constant of 18 hours.
- The no-touch time is the time to reach the 20 C hydrate equilibrium temperature.
- No-touch time is approximately 18 x ln((40 - 4) / (20 - 4)) is about 14.6 hours.
- The estimate is above the 12 hour required time, so the verdict is `ok`.

## 4. Recommended Validated Workflows

- Confirm the no-touch time with `neqsim.pvtsimulation.flowassurance.SurfCooldownAnalyzer`.
- Confirm the hydrate equilibrium temperature with a validated NeqSim hydrate calculation.
- Run a transient cooldown simulation for a design-grade no-touch time.

## 5. Assumptions and Limitations

- The lumped exponential cooldown assumes uniform fluid temperature and constant properties.
- The result is an educational placeholder, not a validated cooldown result.
- Insulation, depressurization, and inhibitor effects are not modelled.

## 6. Human Review

A qualified human review is required before any design or operating decision. This screening does not replace transient cooldown simulation, hydrate prediction, or qualified flow assurance engineering.
