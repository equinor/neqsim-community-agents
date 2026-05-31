# Example: Preliminary Hydrate Risk Screen

This example uses public synthetic conditions for demonstration only.

## Input

- Scenario: subsea cooldown screening
- Pressure: 80 bara
- Temperature range: 4 to 25 degC
- Fluid: methane-rich gas with CO2 present
- Water: free water may be present
- Inhibitor: none specified

## Expected Agent Actions

1. Confirm that pressure, temperature, water, and scenario information are available.
2. Use hydrate screening logic to flag that low temperature and water presence may require further analysis.
3. Identify missing composition, salinity, inhibitor, and transient cooldown information.
4. Recommend a validated NeqSim hydrate workflow or specialist review.

## Example Output Summary

- Conditions may require further hydrate analysis because pressure is elevated, temperature can be low, and water may be present.
- Screening result is not an operating envelope.
- Missing data includes detailed composition, water salinity, inhibitor strategy, cooldown profile, and acceptance criteria.

## Human Review

A qualified flow assurance engineer must review the hydrate prediction method, input data, operating scenario, and mitigation strategy before design or operational use.