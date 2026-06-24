# Example Prompts

Public, synthetic prompts for the Reservoir-to-Facility Screening Agent.

## Reservoir versus time

```text
Use public synthetic data. Screen a gas reservoir of 20 Gsm3 recoverable volume
declining from 300 to 80 bara at 8 MSm3/day over 15 years, with water cut
starting at 5 % and rising 3 % per year. Show the pressure, recovery-factor, and
water-cut development versus time and flag when it reaches abandonment.
```

## Wells via manifold to a platform

```text
Route two production wells through one manifold and an 8 km flowline with a
1.5 bar/km gradient and a 20 bar riser drop to a host that requires 90 bara
arrival. WELL-A has reservoir 300 bara, bottomhole 250 bara, PI 1.0e5
Sm3/day/bar, THP 140 bara; WELL-B has reservoir 295 bara, bottomhole 240 bara,
PI 0.9e5 Sm3/day/bar, THP 135 bara. Estimate per-well rates, the aggregated
manifold rate, and the platform arrival pressure and margin.
```

## Full reservoir-to-facility with time development

```text
Use public synthetic data to screen a gas field from reservoir to facility.
Combine the 15-year reservoir depletion profile with the two-well, single-manifold
network routing and show how the platform arrival-pressure margin develops as the
reservoir depletes. Suggest validated NeqSim reservoir and multiphase workflows
and prepare a screening report outline with assumptions and limitations.
```

## Escalation reminder

```text
List the validated NeqSim tools and qualified reviews required before this
reservoir-to-facility screening can be used for any design or operating decision.
```
