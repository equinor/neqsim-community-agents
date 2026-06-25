# Example: Utility Balance Screening

This example uses a public synthetic facility utility case for demonstration only.

## Input

- Instrument air: stated consumer demand with a minus 40 degC dew-point requirement
- Instrument air supply: stated dryer and receiver capacity
- Fuel gas: methane-rich sales gas with a target Wobbe band
- Cooling water: stated heat duty with supply 20 degC and return 35 degC
- Screening objective: identify utility shortfalls and off-spec conditions

## Expected Agent Actions

1. Review the utility scope and identify missing data such as diversity factors.
2. Use `utility-balance-screening` to screen instrument air supply versus demand and dew point.
3. Screen the fuel-gas Wobbe Index against the target band.
4. Screen cooling-water duty and supply/return temperature balance.
5. List utility bottlenecks and follow-up studies.

## Example Output Summary

- Instrument air supply margin against demand is reported with the dew-point requirement noted.
- Fuel-gas Wobbe Index falls within the screening target band at the assumed composition.
- Cooling-water flow follows from duty and the 20 degC to 35 degC approach.
- Follow-up studies include dryer and compressor sizing and fuel-gas conditioning.

## Human Review

A qualified utility systems engineer must review demand profiles, diversity, dryer and compressor sizing, and fuel-gas interchangeability before engineering use.
