# Example: Build And Screen A TEG Dehydration Plant

This example uses public synthetic conditions for demonstration only.

## Input

- Feed: public synthetic natural gas (default composition), 4.65 MSm3/day
- Feed conditions: 70 bara, 25 degC, water-saturated
- Absorber: 85 bara, 35 degC, 4 stages, 0.7 stage efficiency
- Lean TEG: 5500 kg/hr, 48.5 degC, 97 wt% purity
- Regeneration: flash drum 4.8 bara, reboiler 197.5 degC, stripping gas 180 Sm3/hr
- Scenario: compare once-through versus recirculated stripping gas

## Expected Agent Actions

1. Confirm that feed, absorber, lean-TEG, and regeneration conditions are available.
2. Use the `teg-dehydration-modeling` skill to build the closed-loop plant.
3. Run the flowsheet on a worker thread and wait for the recycles to converge.
4. Read the dry-gas water dew point, lean-TEG purity, and still-vent emissions.
5. Re-run with stripping-gas recirculation and compare emissions.
6. Identify missing composition, water salinity, and acceptance-criteria data.

## Example Output Summary

- Dry-gas water dew point is well below 0 degC at the reference pressure.
- Lean TEG purity is above 90 wt%.
- Recirculating stripping gas does not increase still-vent NMVOC or methane.
- Result is a screening estimate, not a guaranteed dew point or emission limit.
- Missing data includes detailed composition, water salinity, glycol losses, and
  emission acceptance criteria.

## Human Review

A qualified process and environmental engineer must review the dehydration model,
input data, convergence assumptions, and emission classification before design,
operational, or reporting use.
