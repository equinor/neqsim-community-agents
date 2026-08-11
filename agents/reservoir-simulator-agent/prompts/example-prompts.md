# Example Prompts — Reservoir Simulator Agent

Use public data only unless the user supplies their own. Keep every reused figure
with its source and reference year.

## Tier 1 — build from a public headline only

```text
Set up a first reservoir model for an Arctic oil discovery using only what is public: Barents Sea, 400 m water depth, reservoir about 250 m below the seabed, roughly 500 million barrels reported recoverable. Default the pressure and temperature from depth, tell me the data tier and the completeness score, list every assumption you had to make with its basis, and rank the five data items that would most reduce the uncertainty.
```

## Tier 1 — build from geometry instead of a reported volume

```text
Build a gas reservoir model from geometry: 32 km2 mapped area, 60 m gross thickness, 0.7 net-to-gross, 0.20 porosity, 0.30 water saturation, 2900 m datum depth, no measured pressure or temperature. Report the hydrocarbon pore volume, GIIP, the gas formation volume factor and the standard conditions it assumes, and the recovery factor with its basis.
```

## Tier 2 — refine with play analogues, then with appraisal data

```text
Refine the model in two labelled steps. First add play-analogue rock properties: 28 % porosity, 25 % water saturation, 85 % net-to-gross, a moderate aquifer and a water-injection development. Then add appraisal data: 21 km2 area, 45 m net pay, 30 % porosity, 20 % water saturation, 2000 mD permeability, 76 bara initial pressure, 18 degC reservoir temperature, an oil formation volume factor of 1.12 and a target plateau of 19 000 Sm3/day. For each step report the change list, the provenance upgrade, the new data tier and the new completeness score.
```

## Consistency check

```text
Reconcile the geometry-derived in-place volume against the reported recoverable volume. What recovery factor does the reported volume imply, how does that compare with the assumed recovery factor for this drive mechanism, and which of the three inputs is most likely to be wrong?
```

## Cross-check and context

```text
Cross-check the model against a tank-style depletion profile from the recoverable volume, the initial and abandonment pressure and the plateau rate. Compare the depletion horizon with the plateau the well count supports, place the volumes in an SPE-PRMS / NPD maturity category, and flag any material divergence.
```

## Hand over to NeqSim

```text
Produce the NeqSim reservoir specification for this model. State explicitly which volumes are in-situ reservoir volumes and which are standard-condition volumes, keep the aquifer volume separate from the tank water volume, and give me the WellFlow production index in the unit NeqSim expects. Name the validated NeqSim classes and MCP tools for the next step.
```

## Cold and shallow setting

```text
The reservoir is shallow and cold. Explain what that implies for the drive energy, the gas expansion, the need for pressure support and artificial lift, and for the flow-assurance strategy in the flowline, and say which of those conclusions the screening model can actually support.
```

## Data-acquisition plan

```text
Give me the ranked data-acquisition plan for this model: which measurement, why it matters for this specific answer, how it would be acquired, and what the model would look like once it lands. Keep it to the items that actually change the decision.
```
