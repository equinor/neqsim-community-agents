# Example: Gas Turbine Driver Screening

This example uses a public synthetic gas-turbine driver case for demonstration only.

## Input

- Driver: single gas-turbine for a gas export compressor
- ISO base power rating: 30 MW
- Site ambient temperature: 30 degC
- Site elevation: 50 m
- Fuel gas: methane-rich sales gas
- Required shaft power: 24 MW
- Screening objective: check site-rated margin

## Expected Agent Actions

1. Review the driver duty and identify missing data such as detailed performance curves.
2. Use `gas-turbine-performance-screening` to apply ambient and elevation derating.
3. Screen heat rate and fuel gas consumption.
4. Estimate exhaust mass flow and temperature.
5. Compare site-rated power against the 24 MW required power.

## Example Output Summary

- Ambient temperature above ISO 15 degC reduces site power below the 30 MW base rating.
- Screening heat rate and fuel consumption increase relative to base load.
- Estimated exhaust temperature suggests a waste-heat-recovery follow-up study.
- Driver margin against the 24 MW duty is reported as screening only.

## Human Review

A qualified rotating equipment engineer must review site-rating corrections, performance guarantees, emissions, and part-load behaviour before engineering use.
