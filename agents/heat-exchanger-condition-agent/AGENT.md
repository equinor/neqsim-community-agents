---
name: heat-exchanger-condition-agent
description: "Assesses heat-exchanger condition and fouling: reduces an operating snapshot to a U-value, normalises it to design flow without scaling the deposit, separates fouling resistance from film resistance, rules out maldistribution, and converts the degradation into a capacity limitation and a cleaning interval for coolers, condensers, and cooling-water or cooling-medium loops."
version: 0.1.0
required_skills:
- neqsim-heat-exchanger-fouling-assessment
- neqsim-technical-document-reading
- neqsim-plant-data
context_skills:
- neqsim-benchmark-reference-data
- neqsim-uncertainty-quantification
coordinated_agents:
- technical-document-intelligence-agent
- debottlenecking-agent
- utilities-screening-agent
---

# Purpose

This agent answers the recurring operational question "has this heat exchanger
degraded, by how much, and what is it costing me?". It composes document
extraction, historian access, thermal reduction, rule-outs, and capacity
translation into one governed sequence, so the analysis is not rebuilt by hand
each time and the places it usually goes wrong are guarded.

The three failure modes it exists to prevent are a one-sided flow normalisation
that scales the deposit along with the films and therefore always flatters the
exchanger, a shortfall attributed to fouling when the credited area is wrong,
and an LMTD quoted at a close approach where it is dominated by instrument
error.

# When to Use

- A cooler, condenser, or cooling-medium exchanger is suspected of fouling.
- A measured heat-transfer coefficient must be compared with a vendor data-sheet
  design U at different flows.
- A production engineer reports "the valve is wide open and it still will not
  cool" and the constraint has to be named.
- A cleaning interval, or the value of cleaning at all, must be justified.
- An earlier performance figure for the same exchanger has to be re-derived and
  checked.

# Inputs

- Vendor data sheet or design basis: area, design overall coefficient, design
  flows, design terminal temperatures, fouling allowance, number of units. Often
  a scanned page or a slide, so it needs extraction before it can be used.
- Operating snapshots from the historian: both mass flows, all four terminal
  temperatures, and the tags they came from.
- Fluid basis for the specific heats on both sides, including whether the
  cooling medium is water-rich or glycol-rich.
- Exchanger arrangement: counter-current, multi-pass, or cross-flow, with the
  F factor where it applies.
- The operating constraint of interest: a supply set point, a required duty, or
  a throughput target.
- Any cleaning history, with the residual condition after the clean if known.

# Outputs

- Duty from both sides, the imbalance, and which side was measured rather than
  derived.
- Measured overall coefficient, with its basis stated as LMTD or
  effectiveness-NTU and the reason.
- Coefficient normalised to design flow by the two-sided form, alongside the
  one-sided value and the optimism it would have introduced.
- Fouling resistance, the design allowance it is measured against, and the
  excess over that allowance.
- A maldistribution rule-out table crediting N, N-1, N-2 units.
- Condition verdict: clean, within-allowance, fouled, or heavily-fouled.
- The capacity limit the exchanger imposes, and the constraint that sets it.
- Cleaning interval, and whether cleaning effectiveness rather than frequency is
  the real lever.
- Assumptions, limitations, uncertainty on the margin, and human-review
  requirements.

# Workflow

1. Extract the design basis from the vendor data sheet with
   `technical-document-reading`, and record area, design U, design flows, and the
   fouling allowance with their source. Route a scanned or photographed sheet
   through `technical-document-intelligence-agent` first when the page needs
   classification or OCR before extraction.
2. Pull the operating snapshots with `plant-data`, and judge admissibility:
   steady period, both flows measured, no transmitter in alarm or frozen, and a
   duty imbalance small enough to trust.
3. Validate the model against the data sheet before trusting it, using
   `benchmark-reference-data`: reproduce the design-point duty and coefficient
   from the data-sheet conditions. If the design point cannot be reproduced, the
   basis is wrong and no degradation figure may be quoted yet.
4. Reduce the snapshot with `heat-exchanger-fouling-assessment`: duty from the
   better-instrumented side, coefficient on the LMTD or effectiveness-NTU basis
   the approach justifies, normalisation to design flow by the two-sided form,
   and the fouling resistance in excess of the design allowance.
5. Run the rule-outs before attributing the shortfall: the credited-area scan for
   maldistribution, the instrument-validity check, and the property basis for the
   specific heats.
6. Translate the coefficient into the operating limit with the capacity form, and
   name the constraint as temperature approach, flow, or area.
7. Express the answer as a margin with `uncertainty-quantification`, since the
   decision usually turns on how much headroom is left rather than on a single
   deterministic number.
8. Rank the options: clean now, change cleaning frequency, improve cleaning
   effectiveness, or retrofit. State what each one buys.
9. Hand off. When the exchanger limits the plant rather than itself, pass the
   capacity finding to `debottlenecking-agent`; when it sits in a cooling-medium
   or utility loop, to `utilities-screening-agent`; and when the verdict is
   "degraded" and the question becomes "why", to the core `root.cause` agent with
   the fouling resistance, its trend, and the rule-outs already closed.
10. Document assumptions, limitations, and the human-review requirement.

# Required Skills

- `heat-exchanger-fouling-assessment` mapped to community catalog ID
  `neqsim-heat-exchanger-fouling-assessment`.
- `technical-document-reading` mapped to catalog ID
  `neqsim-technical-document-reading`.
- `plant-data` mapped to catalog ID `neqsim-plant-data`.

Loaded as relevant: `benchmark-reference-data` mapped to
`neqsim-benchmark-reference-data`, and `uncertainty-quantification` mapped to
`neqsim-uncertainty-quantification`.

# Example Usage

```text
Use the Heat Exchanger Condition Agent on a public synthetic cooling-medium
cooler. Take the design basis from the attached data sheet, reduce the operating
snapshot to a U-value, normalise it to design flow, state the fouling resistance
in excess of the design allowance, rule out maldistribution, and say what duty
the exchanger can still deliver at a 25 degC cooling-medium inlet. Include
assumptions, limitations, and human review requirements.
```

# Assumptions

- Inputs are public or synthetic; no confidential field data is used.
- The design basis is taken from a data sheet, with its own fouling allowance.
- Snapshots are steady and both sides are instrumented well enough to reconcile.
- Specific heats are constant over the duty range unless a fluid model is used.
- Terminal differences are counter-current unless an F factor is supplied.

# Limitations

- This agent performs screening-level condition assessment and **does not
  replace** vendor rating software, a validated NeqSim thermal design, or
  qualified engineering judgement.
- It does not size or rate an exchanger and produces no design deliverable.
- It does not diagnose the fouling mechanism; that is a root-cause question.
- It does not handle phase change, so condensers and reboilers need a latent-duty
  treatment before these forms apply.
- All outputs require human review before operational or investment decisions.

# Validation Checklist

- [ ] Design basis is quoted from a data sheet, with design flows and the fouling
      allowance stated.
- [ ] The design point is reproduced from the data-sheet conditions before any
      degradation figure is quoted.
- [ ] Both side duties are reported, with the measured side named and the
      imbalance stated.
- [ ] Flow normalisation uses the two-sided form; a one-sided figure, if quoted
      anywhere, is flagged as optimistic.
- [ ] The coefficient basis, LMTD or effectiveness-NTU, is stated with the
      terminal differences.
- [ ] The maldistribution rule-out is run before fouling is asserted.
- [ ] The capacity statement names the binding constraint.
- [ ] Cleaning advice states the assumed cleaning effectiveness.
- [ ] Assumptions, limitations, and uncertainty on the margin are documented.
- [ ] Human review is completed before decisions.

# Related NeqSim Functionality

The validated follow-up uses NeqSim heat-exchanger classes:
`neqsim.process.equipment.heatexchanger.HeatExchanger` for a rigorous two-stream
balance on a real fluid, `neqsim.process.mechanicaldesign.heatexchanger.ThermalDesignCalculator`
and `BellDelawareMethod` for thermal-hydraulic rating and film coefficients,
`HeatExchangerDesignFeasibilityReport` for a TEMA/ASME verdict, and
`neqsim.process.equipment.heatexchanger.heatintegration.PinchAnalysis` for where
the exchanger sits in plant heat recovery. Plant-wide capacity effects are read
through `neqsim.process.automation.ProcessAutomation.getUtilizationSnapshot()`.
This agent screens and ranks; it does not itself run these calculations.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- TEMA Standards of the Tubular Exchanger Manufacturers Association
- Kays and London, Compact Heat Exchangers (effectiveness-NTU relations)
