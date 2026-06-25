---
name: debottlenecking-agent
description: Screens a simple process train to identify the most likely capacity bottleneck — separator capacity, compressor operating window, line velocity, or line pressure drop — and ranks units by public screening-level utilization before a validated NeqSim study.
version: 0.1.0
required_skills:
  - separator-modelling
  - compressor-operating-window-check
  - line-velocity-check
  - pressure-drop-screening
---

# Purpose

This agent coordinates public, screening-level bottleneck identification on a
simple process train. It screens separator capacity, compressor operating window,
line velocity, and line pressure drop, then ranks units by an approximate
utilization so an engineer can see where headroom is tightest. It uses public,
educational methods and recommends a validated NeqSim capacity study for any
quantitative decision.

# When to Use

- Early "where is the bottleneck?" discussions before a detailed capacity study.
- Screening which unit limits throughput when a rate increase is proposed.
- Prioritizing which equipment to model in detail in a later NeqSim study.
- Teaching or demonstrating capacity-utilization screening on a public example.

# Inputs

- Process train description (units, nominal pressures, temperatures, flow rates;
  state units such as bara, °C, kg/hr or Sm³/d).
- Target throughput or rate-increase scenario to screen.
- Line geometry for main lines (inside diameter, length) where pressure drop or
  velocity is relevant.
- Public or synthetic fluid composition (mole fractions, normalized).
- Optional design limits (separator capacity, compressor surge/stonewall, velocity
  or pressure-drop guidelines).

# Outputs

- A ranked list of units by approximate screening-level utilization.
- The most likely capacity bottleneck with rationale.
- A short list of candidate debottlenecking directions.
- Assumptions, limitations, and explicit human-review requirements.
- A recommendation to run a validated NeqSim capacity study.

# Workflow

1. Restate the train, target throughput, and any design limits.
2. Use `separator-modelling` to screen separator gas/liquid capacity utilization.
3. Use `compressor-operating-window-check` to screen compressor window margin.
4. Use `line-velocity-check` to screen main-line velocities against guidelines.
5. Use `pressure-drop-screening` to screen line pressure gradients.
6. Rank units by approximate utilization and identify the tightest constraint.
7. Suggest candidate debottlenecking directions for the limiting unit.
8. Document assumptions, limitations, and human-review requirements.
9. Recommend a validated NeqSim capacity study for the decision.

# Required Skills

- `compressor-operating-window-check` mapped to community catalog ID
  `neqsim-compressor-operating-window-check`.
- `line-velocity-check` mapped to community catalog ID `neqsim-line-velocity-check`.
- `pressure-drop-screening` mapped to community catalog ID
  `neqsim-pressure-drop-screening`.
- `separator-modelling` mapped to community catalog ID `neqsim-separator-modelling`.

# Example Usage

```text
Use the Debottlenecking Agent to screen, on a public synthetic separation and
export-compression train, which unit limits a 15% throughput increase. Rank units
by approximate utilization and identify the bottleneck. Include assumptions,
limitations, and human review requirements.
```

# Assumptions

- Inputs are public or synthetic; no confidential field data is used.
- Screening uses simplified public methods, not rigorous capacity analysis.
- Fluid composition is representative and normalized.
- Equipment operates near the supplied nominal conditions.

# Limitations

- This agent performs screening only and does not replace a validated NeqSim
  capacity study or engineering judgement.
- Approximate utilization is indicative, not a guaranteed limit.
- It does not size equipment or produce design deliverables.
- Results must be confirmed by a qualified engineer before use.

# Validation Checklist

- [ ] Target throughput and design limits are stated.
- [ ] Composition sums to 1.0 and uses valid component names.
- [ ] Each unit is screened against its relevant guideline.
- [ ] Units are ranked and the bottleneck is identified with rationale.
- [ ] Assumptions and limitations are documented.
- [ ] Human review requirement is stated.
- [ ] A validated NeqSim capacity study is recommended.

# Related NeqSim Functionality

The downstream validated workflow uses NeqSim capacity introspection:
`neqsim.process.automation.ProcessAutomation.getUtilizationSnapshot()` (side-effect-free
per-unit utilization and plant bottleneck), the per-unit `CapacityConstraint`
breakdown on `neqsim.process.processmodel.ProcessSystem` / `ProcessModel`, and
`ProcessAutomation.evaluate(...)` for gated rate-increase trials. The required
screening skills ultimately drive these `ProcessSystem` workflows. This agent only
screens and ranks; it does not itself run these calculations.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
