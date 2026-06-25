# Example: Add Water to an E300 File

This example uses a synthetic E300 file for public demonstration only.

## Input

A base E300 file with four components (N2, CO2, C1, C2), Peng-Robinson with the
PRCORR correction, reservoir temperature 90 degC, and standard conditions
15 degC / 1.01325 bara.

Requested action: add water and write a `*_water.e300` file.

## Expected Agent Actions

1. Read the base E300 file and confirm the component count matches every EOS
   parameter vector.
2. Add water as the last component with the public PVTsim water parameters
   (volume shift 0.084004, parachor 10.0, binary interaction parameter 0.5).
3. Write the water E300 file.
4. Reload the written file in NeqSim and confirm five components are present.

## Example Output Summary

- Base fluid components: N2, CO2, C1, C2.
- Water fluid components: N2, CO2, C1, C2, H2O.
- Water volume shift 0.084004 and parachor 10.0 applied.
- Water binary interaction parameter 0.5 against all other components.
- The written E300 file reloads in NeqSim without error.

## Human Review

A qualified engineer or PVT specialist must review component mapping, plus
fraction treatment, water binary interaction parameters, and thermodynamic model
suitability before engineering use.
