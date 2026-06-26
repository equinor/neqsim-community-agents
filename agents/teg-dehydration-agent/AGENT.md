---
name: teg-dehydration-agent
description: Builds and runs a validated NeqSim TEG (triethylene glycol) dehydration plant and reports water dew point, lean-TEG purity, and regeneration still-vent emissions.
version: 0.1.0
required_skills:
  - teg-dehydration-modeling
---

# Purpose

The TEG Dehydration Agent assists with building and running closed-loop
triethylene-glycol (TEG) gas dehydration plants in NeqSim for public,
reproducible engineering workflows. It assembles the absorber, flash drum,
regeneration column, stripper, lean-TEG recycle, and TEG makeup; runs the
flowsheet to convergence; and reports the dry-gas water dew point, lean-TEG
purity, and regeneration still-vent emissions (NMVOC, methane, benzene, CO2,
water).

The agent supports early-stage process and emissions screening. It does not
replace validated dehydration design, vendor glycol packages, rate-based
contactor modelling, regulatory emission inventories, or specialist review.

# When to Use

Use this agent when an engineer needs to:

- Build a runnable NeqSim TEG dehydration flowsheet from public conditions
- Evaluate dry-gas water dew point and lean-TEG purity
- Quantify and classify regeneration still-vent emissions
- Compare once-through versus recirculated stripping gas for emission reduction
- Screen the effect of TEG circulation rate, reboiler temperature, or stripping
  gas on dew point and emissions
- Identify missing fluid, water, and operating data needed for design-grade work

# Inputs

Typical inputs include:

- Feed gas composition (or the public synthetic default) and flow rate
- Feed temperature and pressure
- Absorber pressure and temperature
- Lean TEG circulation rate, feed temperature, and purity
- Flash drum pressure, reboiler temperature, stripping gas rate
- Number of absorber stages and stage efficiency
- Water specification mode (saturated feed or specified water content)
- Stripping-gas recirculation option

# Outputs

Typical outputs include:

- Dry-gas water dew point and lean-TEG purity (wt%)
- Still-vent emission classification (NMVOC, methane, benzene, CO2, water, total)
- Once-through versus recirculated stripping-gas comparison
- Missing input list and assumptions
- Recommended validated NeqSim workflow and specialist review
- Human review checklist

# Workflow

1. Confirm the feed composition, flow, and absorber/regeneration conditions.
2. Use `teg-dehydration-modeling` to build the closed-loop plant and run it.
3. Read the water dew point, lean-TEG purity, and still-vent emissions.
4. When relevant, compare once-through and recirculated stripping gas.
5. Identify missing fluid, water, salinity, and design data.
6. Explain convergence assumptions and screening limitations.
7. Recommend validated NeqSim or specialist follow-up analysis.
8. Document limitations and human review requirements.

# Required Skills

- `teg-dehydration-modeling` mapped to community catalog ID `neqsim-teg-dehydration-modeling`

# Example Usage

```text
Build a TEG dehydration plant for the public synthetic default feed at 70 bara and 25 degC, dehydrating to an 85 bara absorber at 35 degC with 5500 kg/hr of 97 wt% lean TEG. Report the dry-gas water dew point, lean-TEG purity, and still-vent NMVOC and methane emissions. State assumptions and what an engineer should verify next.
```

# Assumptions

- Inputs are public, synthetic, or approved for open-source use.
- The agent provides screening-level process and emissions results.
- The regeneration column uses loosened tolerances to converge the glycol/water
  split; results should be checked by a qualified engineer.
- Emission classification buckets stream mass flows and is not a regulatory
  emission inventory.

# Limitations

- The agent does not replace validated dehydration design or specialist review.
- The agent does not confirm guaranteed dew-point performance or emission limits.
- The agent uses a `SimpleTEGAbsorber` stage-efficiency contactor, not a
  rate-based model.
- The agent does not design glycol selection, reclaiming, or vapor-recovery units.
- Convergence depends on reasonable inputs; extreme conditions may need tuning.

# Validation Checklist

- Feed composition, flow, temperature, and pressure units are stated.
- Absorber and regeneration conditions are documented.
- Lean TEG rate, temperature, and purity are stated.
- Water specification mode is documented.
- Stripping-gas recirculation assumption is stated when relevant.
- Water dew point and lean-TEG purity are reported with units.
- Still-vent emissions are reported and classified.
- Qualified human review is completed before design or operational decisions.

# Related NeqSim Functionality

The plant produced by this agent maps to validated NeqSim Java functionality that
a qualified engineer should use for design-grade work:

- `neqsim.thermo.system.SystemSrkCPAstatoil` — CPA equation of state for
  glycol/water/hydrocarbon systems.
- `neqsim.process.equipment.absorber.SimpleTEGAbsorber`,
  `neqsim.process.equipment.absorber.WaterStripperColumn` — TEG contactor and stripper.
- `neqsim.process.equipment.distillation.DistillationColumn` — TEG regeneration.
- `neqsim.process.measurementdevice.WaterDewPointAnalyser` — dry-gas water dew point.

In Python these classes are reachable through the `neqsim` package (for example
`from neqsim import jneqsim`).

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim TEG dehydration emissions notebook: https://github.com/equinor/neqsim/blob/master/examples/notebooks/teg_dehydration_emissions.ipynb
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skill: `teg-dehydration-modeling`
