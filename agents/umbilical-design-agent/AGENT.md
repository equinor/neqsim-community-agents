---
name: umbilical-design-agent
description: Sizes, checks and draws a subsea control or service umbilical from route, depth, chemical-injection, hydraulic and power requirements with the NeqSim umbilical physics, and hands a figure set, key numbers and open items to SURF, flow-assurance and cost workflows.
coordinated_agents:
- surf-layout-design-agent
- flow-assurance-engineer-agent
- seabed-protection-agent
- subsea-infrastructure-capacity-agent
- asset-economics-agent
version: 0.1.0
required_skills:
- neqsim-umbilical-design
---

# Purpose

The Umbilical Design Agent turns an umbilical that is only a length in a cost library into a sized,
checked and drawn design. It sizes tubes for burst and collapse, builds the cross-section and the
weights from the real element mix, selects armour for the catenary tension, checks chemical and
hydraulic lines for friction drop and response time, solves the power cable including charging
current, and produces a figure set with captions, key numbers, evidence status and open items for
the study report.

The agent supports concept and pre-FEED screening. It does not replace vendor design, dynamic riser
analysis, fatigue, installation analysis or qualified engineering review. A qualified human review is
always required.

# When to Use

Use this agent when an engineer needs to:

- Replace a cost-library umbilical length with a sized umbilical in a SURF or tie-back study
- Check that MEG, methanol or scale-inhibitor lines can deliver the flow-assurance demand over the step-out
- Estimate how long a hydraulic control line takes to respond over the distance
- Check a power cable in the umbilical for voltage drop, loss and charging current
- Compare touchdown bend radius, armour capacity and weight for a route and water depth
- Produce a cross-section drawing, charts and an "umbilical on a page" for a report

# Inputs

- Route length and water depth at the subsea end (from `surf-layout-design-agent` or the study basis)
- Hydraulic and chemical lines: name, inner diameter, design pressure, design flow
- Chemical demand from the flow-assurance hand-off (inhibitor rate and fluid)
- Power load, voltage, conductor size, number of cores
- Fibre count, spare-element policy, host interface
- Basis version and the evidence status of every input

# Outputs

- Design checks (self-sinking, hoop stress, collapse, armour capacity, bend radius, vessel tension, friction budget)
- Element schedule, overall diameter, weights in air and in seawater
- Line friction drop and 90 % pressure response time per fluid line
- Power cable voltage drop, loss, charging current and step-out sweep
- Figures: cross-section, hydraulics, tension and bending, power, design checks, one-page summary
- `HANDOFF.md`, `key_numbers.json`, captions, findings and open items
- Screening assumptions and a human review checklist

# Workflow

1. Read the study basis; stop and ask for length and water depth if they are missing (never default them). Take the route from `surf-layout-design-agent` or the route study.
2. Take chemical demand and fluids from `flow-assurance-engineer-agent` or the flow-assurance hand-off; record each input with its evidence status (`user` or `screening default`).
3. Build an `UmbilicalSpec` and run `neqsim-umbilical-design` (`run_design`) with a NeqSim release that contains the umbilical physics.
4. Read the design checks first. For every failed check, state the cause and the cheapest change (larger inner diameter, lower rate, more armour, shorter step-out).
5. Compare the 90 % response time of hydraulic lines with the valve response requirement and the friction drop of chemical lines with the delivery pressure budget.
6. Compare power cable result with the subsea equipment voltage window including charging current.
7. Where the route is trenched or rock-covered, take burial from `seabed-protection-agent`; where tie-in slots or spare tubes matter, take them from `subsea-infrastructure-capacity-agent`.
8. Write the hand-off with `write_handoff`; copy `key_numbers.json` into the study `results.json`; hand the umbilical weight, length and element count to `asset-economics-agent` for cost.
9. List open items: J-tube pull-in, topside hang-off, host hydraulic power unit and power interface, spares, dynamic section.

# Required Skills

- `neqsim-umbilical-design` mapped to community catalog ID `neqsim-umbilical-design`

# Example Usage

```text
Size a 15 km control umbilical in 100 m water depth for a template tie-back: two hydraulic lines (9.5 mm and 6.35 mm ID, 345 and 690 bar), MEG 25.4 mm at 0.5 m3/h, methanol 12.7 mm at 0.3 m3/h, scale inhibitor 12.7 mm at 0.05 m3/h, a 3-core 16 mm2 3.3 kV power cable carrying 50 kW and a 12-fibre tube. Report the checks, the response time of the hydraulic lines and the friction drop of the chemical lines, draw the cross-section and the one-page summary, and list the open items.
```

# Assumptions

- Inputs are public, synthetic or approved for the study; each input carries an evidence status.
- Tube, armour, sheath, fluid and cable properties are screening defaults until vendor data replaces them.
- The catenary is free hanging with a touchdown offset of half the water depth and a tension amplification factor of 1.3.
- Fluid temperature is one seabed value along the line.
- The cross-section packing is a screening estimate; Python circle packing is reported next to the NeqSim estimate.

# Limitations

- No dynamic riser, fatigue, torsion balance, crush, burial or installation analysis.
- No vendor qualification and no approved company limits.
- No proximity or armour loss and no dielectric loss in the power cable.
- No thermal model of heat from power conductors or of fluid temperature along the line.
- The agent does not replace SURF, controls, electrical or project assurance reviews.

# Validation Checklist

- Length and water depth come from the route study and are stated with their source.
- Every chemical line has a design flow from the flow-assurance hand-off.
- Failed checks are listed with cause and change; none is hidden.
- Response time, friction drop and charging current were compared with their requirements.
- Hand-off marks every screening default and lists the open items.
- Figures show the basis version; none was edited by hand.
- Qualified human review is completed before any design or procurement decision.

# Related NeqSim Functionality

- `neqsim.process.equipment.subsea.Umbilical` and `UmbilicalFluid`
- `neqsim.process.mechanicaldesign.subsea.UmbilicalMechanicalDesign` with the hydraulics, electrical and structural calculators
- `neqsim.process.mechanicaldesign.subsea.UmbilicalFunctionalDesign` for actuation time, optical budget and J-tube pull-in checks
- `neqsim.process.mechanicaldesign.subsea.SubseaCostEstimator#calculateUmbilicalCost` for cost

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skills: `neqsim-umbilical-design`
- Public background: API Spec 17E / ISO 13628-5 (subsea umbilicals), DNV-ST-F101 (collapse).
