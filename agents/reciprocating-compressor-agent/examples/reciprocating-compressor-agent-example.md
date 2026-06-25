# Example: Reciprocating Compressor Screening

This example uses a public synthetic reciprocating compressor duty for demonstration only.

## Input

- Service: reciprocating compressor for a methane-rich gas
- Suction pressure: 5 bara
- Discharge pressure: 150 bara
- Suction temperature: 30 degC
- Estimated cylinder clearance fraction: 0.12
- Allowable discharge temperature: 150 degC
- Screening objective: estimate staging and check discharge temperature

## Expected Agent Actions

1. Review the duty and identify missing data such as composition detail and cylinder data.
2. Use `reciprocating-compressor-screening` to estimate the number of stages and per-stage pressure ratio.
3. Screen per-stage volumetric efficiency and estimate discharge temperature.
4. Provide a screening-level rod-load likelihood indication.
5. Recommend rigorous NeqSim compressor simulation for design-grade work.

## Example Output Summary

- Overall ratio of 30 suggests roughly 3 stages with a per-stage ratio near 3.1.
- Screening volumetric efficiency decreases with pressure ratio and clearance fraction.
- Estimated per-stage discharge temperature is below the 150 degC limit at the screening assumptions.
- Rod-load indication is reported as screening only and requires vendor frame-load certification.

## Human Review

A qualified rotating equipment engineer must review staging, rod load, valve and cylinder selection, and discharge temperature limits before engineering use.
