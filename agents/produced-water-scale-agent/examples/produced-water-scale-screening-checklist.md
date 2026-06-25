# Produced Water Scale Screening Checklist (Public Example)

This worked example uses only public, synthetic data. It demonstrates an
early-stage produced-water scale screening. All values are illustrative and must
not be used for design or operating decisions.

## 1. Objective

Screen a high-barium formation water and a seawater injection water for scale
risk, and assess sulfate/carbonate scale incompatibility on commingling.

## 2. Synthetic Inputs

| Property | Formation Water | Seawater |
| --- | --- | --- |
| Source | preset: formation_water_high_ba | preset: seawater |
| Temperature | 80 degC | 20 degC |
| Pressure | 150 bara | 1 bara |
| pH | 6.0 | 8.1 |
| TDS (approx.) | 97,350 mg/L | 35,081 mg/L |

Ions modelled (public screening set): Na+, Cl-, Ca++, Mg++, SO4--, HCO3-, plus
Ba++ and Sr++ for scale evaluation.

## 3. Brine Build

- Build both waters with the `produced-water-scale-screening` skill.
- Emit NeqSim-ready ion mappings (water + ion mole fractions).
- Report ionic strength and charge-balance error.
  - Formation water: ionic strength approx. 1.83, charge balance approx. -1.8%.
  - Seawater: ionic strength approx. 0.70, charge balance approx. +0.1%.
- Flag charge-balance errors above the screening threshold for review.

## 4. Single-Water Scale Results (Screening Only)

| Scale | Formation Water SI | Risk Band |
| --- | --- | --- |
| BaSO4 | screening value | review |
| SrSO4 | screening value | review |
| CaSO4 | screening value | review |
| CaCO3 | screening value | review |

Values are computed with a public Davies-activity screening method, not a
validated electrolyte equation of state.

## 5. Mixing Incompatibility Sweep

- Sweep seawater/formation-water mixing fractions (for example 0 to 1 in 11 steps).
- Worst-case (illustrative): BaSO4 supersaturation peaks at a high formation-water
  fraction (for example fraction_a approx. 0.70) with a high screening SI.
- Report the worst-case scale, fraction, and risk band for each scale salt.

## 6. Corrosion Flags (Screening Only)

- CO2 content: low partial-pressure indicator (illustrative).
- H2S content: sour-service indicator triggered; reference ISO 15156 / NACE MR0175.

## 7. Required Follow-Up Studies

- Validated electrolyte-CPA scale prediction with NeqSim `checkScalePotential`.
- Scale inhibitor selection, dosing, and squeeze design.
- Corrosion qualification and materials selection (NORSOK M-001, ISO 15156).
- Water-chemistry sampling and analysis quality assurance.

## 8. Assumptions and Limitations

- Public, synthetic presets; not a specific facility.
- Screening indices only; not validated thermodynamic predictions.
- Ba++ and Sr++ presets are illustrative.
- The example does not establish scale adequacy or compliance.

## 9. Human Review

A qualified water-chemistry, flow assurance, and integrity review is required
before any design or operating decision. This example does not replace validated
NeqSim scale prediction, inhibitor design, or qualified engineering judgement.
