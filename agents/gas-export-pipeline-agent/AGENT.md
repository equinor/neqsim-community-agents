---
name: gas-export-pipeline-agent
description: Performs preliminary gas-export pipeline screening by chaining line velocity, pressure drop, and export compression power checks.
version: 0.1.0
required_skills:
  - line-velocity-check
  - pressure-drop-screening
  - compressor-power-screening
---

# Purpose

The Gas Export Pipeline Agent assists with preliminary screening of a gas-export pipeline and its export compression for public, reproducible engineering workflows. It chains an erosional and recommended line-velocity check, a single-phase pressure-drop screening against a recommended gradient guideline, and an indicative export-compression power estimate. Together these provide an early view of whether an export line size and compression duty are in a sensible range.

The agent supports early-stage engineering screening. It does not replace validated multiphase pipeline simulation, detailed compressor selection, mechanical design, or specialist review.

# When to Use

Use this agent when an engineer needs to:

- Screen an export-line diameter for erosional and recommended gas velocity
- Estimate the single-phase pressure drop along an export line and compare it to a gradient guideline
- Estimate the export-compression power needed to deliver gas to the export pressure
- Identify missing data needed for a rigorous export pipeline study
- Prepare a transparent preliminary export-system note

# Inputs

Typical inputs include:

- Gas flow rate and gas density / molecular weight
- Pipeline internal diameter, length, and roughness
- Inlet and required export (delivery) pressure
- Gas temperature and compressibility information
- Compression suction and discharge pressure and efficiency assumptions

# Outputs

Typical outputs include:

- Line-velocity screening result against erosional and recommended limits
- Pressure-drop screening result against a recommended gradient guideline
- Indicative export-compression power estimate
- Missing input list
- Recommended NeqSim pipeline and compressor follow-up analysis
- Assumptions and limitations
- Human review checklist

# Workflow

1. Confirm the export flow rate, line geometry, and inlet and export pressures.
2. Use `line-velocity-check` to screen the line velocity against erosional and recommended limits.
3. Use `pressure-drop-screening` to estimate the single-phase pressure drop and compare it to a recommended gradient guideline.
4. Use `compressor-power-screening` to estimate the export-compression power for the required pressure rise.
5. Identify missing fluid, multiphase, terrain, and thermal data.
6. Explain uncertainty and screening assumptions.
7. Recommend appropriate NeqSim pipeline and compressor follow-up analysis.
8. Document limitations and human review requirements.

# Required Skills

- `line-velocity-check` mapped to community catalog ID `neqsim-line-velocity-check`
- `pressure-drop-screening` mapped to community catalog ID `neqsim-pressure-drop-screening`
- `compressor-power-screening` mapped to community catalog ID `neqsim-compressor-power-screening`

# Example Usage

```text
Screen this public example gas-export pipeline and its export compression. Check the line velocity, estimate the pressure drop along the line, and estimate the export-compression power. State the assumptions, identify missing information, and recommend what a pipeline engineer should check next.
```

# Assumptions

- Screening inputs are public, synthetic, or approved for open-source use.
- The agent provides preliminary triage only.
- Single-phase gas behaviour is assumed; multiphase, terrain, and thermal effects require explicit data and review.

# Limitations

- The agent does not replace validated multiphase pipeline simulation or transient analysis.
- The agent does not perform detailed compressor selection or surge analysis.
- The agent does not confirm a safe or optimal export-line size.
- The agent does not account for elevation, slugging, or compositional effects unless supplied and reviewed.

# Validation Checklist

- Flow rate, diameter, length, and roughness units are stated.
- Inlet and export pressure units are stated.
- Gas density / molecular weight and temperature assumptions are documented.
- Compression suction, discharge, and efficiency assumptions are documented.
- Velocity, pressure-drop, and power results are reported with their guidelines.
- Follow-up analysis recommendations are included.
- Qualified human review is completed before design decisions.

# Related NeqSim Functionality

The screening produced by this agent maps to validated, rigorous NeqSim Java functionality that a qualified engineer should use for design-grade work:

- `neqsim.process.equipment.pipeline.PipeBeggsAndBrills` — multiphase pipeline pressure and temperature profile.
- `neqsim.process.equipment.compressor.Compressor` — rigorous compression power with performance curves.

In Python these classes are reachable through the `neqsim` package (for example `from neqsim import jneqsim`).

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skills: `line-velocity-check`, `pressure-drop-screening`, `compressor-power-screening`
