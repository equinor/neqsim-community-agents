# Example: Synthetic Composition Review

This example uses a synthetic gas composition for public demonstration only.

## Input

| Component | Mole fraction |
| --- | ---: |
| nitrogen | 0.010 |
| CO2 | 0.020 |
| methane | 0.850 |
| ethane | 0.070 |
| propane | 0.030 |
| n-butane | 0.010 |
| n-pentane | 0.005 |
| n-hexane | 0.005 |

Pressure range: 20 to 120 bara  
Temperature range: -10 to 80 degC

## Expected Agent Actions

1. Check that the mole fractions sum to 1.000.
2. Flag whether water, H2S, and heavier fractions are missing or intentionally excluded.
3. Recommend a preliminary NeqSim phase behavior workflow.
4. Explain that the result is screening-level until reviewed against laboratory data.

## Example Output Summary

- Composition total is 1.000 on the supplied basis.
- CO2 is present and should be retained in thermodynamic calculations.
- No water content is supplied, so hydrate and water phase conclusions cannot be made from this input alone.
- A preliminary NeqSim workflow may include fluid setup, equation-of-state selection, TP flash checks, and phase envelope exploration.

## Human Review

A qualified engineer or PVT specialist must review component mapping, plus fraction treatment, laboratory consistency, and thermodynamic model suitability before engineering use.