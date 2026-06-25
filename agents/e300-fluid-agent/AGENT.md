---
name: e300-fluid-agent
description: Reads Eclipse E300 files into NeqSim fluids, writes NeqSim fluids to E300, and adds water with the public PVTsim water parameters.
version: 0.1.0
required_skills:
  - e300-fluid-io
---

# Purpose

The E300 Fluid Agent helps engineers move fluids between Eclipse 300 (E300)
compositional EOS files and NeqSim, and add water to a fluid or E300 file using
the public PVTsim water parameterization.

The agent supports engineering analysis. It does not replace engineering
judgement, laboratory review, equation-of-state validation, or project
procedures.

# When to Use

Use this agent when an engineer needs to:

- Load an E300 file into a NeqSim fluid for simulation
- Export a NeqSim fluid to an E300 file for PVTsim or Eclipse
- Add water to a dry fluid or E300 file using the public PVTsim water parameters
  (volume shift 0.084004, parachor 10.0, binary interaction parameter 0.5)
- Reproduce a PVTsim `*_water.e300` file from a base E300 file
- Inspect or document the E300 keyword layout and confirm NeqSim can read a file

# Inputs

Typical inputs include:

- An E300 file path
- A NeqSim fluid (for export)
- Whether to add water and the water binary interaction parameter
- Reservoir temperature for the RTEMP keyword
- The intended downstream analysis objective

# Outputs

Typical outputs include:

- A NeqSim fluid created from an E300 file
- A written E300 file, with or without water
- E300 keyword text for a NeqSim fluid
- A summary of components, EOS parameters, and water treatment
- Assumptions and limitations
- A human review checklist

# Workflow

1. Confirm whether the task reads an E300 file, writes one, or adds water.
2. Use `e300-fluid-io` to read the E300 file or render the NeqSim fluid.
3. When water is required, add it with the public PVTsim water parameters.
4. Write the resulting E300 file and confirm it reloads in NeqSim.
5. Set `setMixingRule("classic")` before any NeqSim property calculation.
6. Document components, EOS, water treatment, assumptions, and limitations.
7. Ask for qualified human review before conclusions are used for design or
   operations.

# Required Skills

- `e300-fluid-io` mapped to community catalog ID `neqsim-e300-fluid-io`

# Example Usage

```text
Read this E300 file into a NeqSim fluid, add water using the PVTsim water
parameters, write a *_water.e300 file, and confirm the written file reloads in
NeqSim. List the components and the water parameters used, and explain what
needs human review before the fluid is used for engineering decisions.
```

# Assumptions

- Input E300 files are public, synthetic, or approved for open-source use.
- Water is added with the public PVTsim calibration unless validated
  project-specific data is supplied and reviewed.
- E300 files written by the skill are NeqSim-readable but not byte-identical to
  a PVTsim Nova export.

# Limitations

- The agent does not characterize plus fractions or regress binary interaction
  parameters.
- The agent does not validate laboratory data or tune the equation of state.
- The agent does not guarantee phase behavior or property accuracy.
- The agent does not replace PVT specialist judgement.

# Validation Checklist

- Component count matches all EOS parameter vectors.
- Overall composition sums to the expected basis.
- Water appears once as the last component with volume shift 0.084004 and
  parachor 10.0.
- Water binary interaction parameter is 0.5 (or the chosen value) against all
  components.
- A written E300 file reloads in NeqSim without error.
- `setMixingRule("classic")` is set before NeqSim property calculations.
- Assumptions and limitations are included in the output.
- Qualified human review is completed before design or operational decisions.

# Related NeqSim Functionality

The workflows produced by this agent map to validated, rigorous NeqSim Java
functionality that a qualified engineer should use for design-grade work:

- `neqsim.thermo.util.readwrite.EclipseFluidReadWrite#read(String)` — read an E300 file into a NeqSim fluid.
- `neqsim.thermo.util.readwrite.EclipseFluidReadWrite#read(String, boolean, double)` — read an E300 file and add water.
- `neqsim.thermo.util.readwrite.EclipseFluidReadWrite#addWaterToFluid(SystemInterface, double)` — add water with the PVTsim water parameters.
- `neqsim.thermo.util.readwrite.EclipseFluidReadWrite#write(SystemInterface, String, double)` — write a NeqSim fluid to an E300 file.

In Python these classes are reachable through the `neqsim` package (for example `from neqsim import jneqsim`).

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skill: `e300-fluid-io`
