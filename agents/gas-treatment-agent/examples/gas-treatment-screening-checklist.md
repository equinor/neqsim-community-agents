# Example: Gas Treatment and Compression Screening Checklist

This example uses public, synthetic data only. It demonstrates how the Gas Treatment Agent structures an early-stage screening of gas dehydration need and single-stage compression. It does not design dehydration systems or select compressors.

## Scenario

A gas stream is reviewed for dehydration need and a single compression stage is screened for power.

Public synthetic inputs:

- Gas temperature: 35 degC
- Gas pressure: 70 bar
- Sales-gas water spec: 32 mg/Sm^3
- Compression suction pressure: 30 bar
- Compression discharge pressure: 70 bar
- Suction temperature: 35 degC
- Polytropic efficiency: 0.75
- Molecular weight: 18 g/mol
- Gas flow rate: 5 kg/s

## Screening Steps

1. Confirm the objective: preliminary gas treatment triage only.
2. Run `water-dewpoint-dehydration-screening` to estimate the saturated water content and compare it against the sales-gas water spec.
3. Run `compressor-power-screening` to estimate the polytropic head, discharge temperature, and gas power.
4. Record the warning levels and the most important uncertainties.
5. List required follow-up studies.

## Expected Screening Output Outline

- Saturated water-content indicator and dehydration warning level
- Compression indicators (polytropic head, discharge temperature, gas power) and warning level
- Recommended validated NeqSim and standards workflows
- Required follow-up studies
- Assumptions, limitations, and human review checklist

## Required Follow-Up

- Validated equilibrium water-content and hydrate analysis with NeqSim.
- Validated dehydration design per GPSA and applicable standards.
- Validated compression analysis with vendor compressor maps per API 617 and API 619.
- Qualified process and rotating-equipment review before any decision.
