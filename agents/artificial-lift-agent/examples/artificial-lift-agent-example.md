# Example: Artificial Lift Screening

This example uses a public synthetic well case for demonstration only.

## Input

- Reservoir pressure: 200 bara
- Productivity index: stated linear PI value
- Target production rate: stated oil rate
- Fluid: light oil with a stated gas-liquid ratio
- Well depth: 2500 m measured depth
- Screening objective: compare gas-lift and ESP feasibility

## Expected Agent Actions

1. Review the well data and identify missing data such as detailed well-test points.
2. Use `artificial-lift-screening` to build a simple IPR and screen achievable rate and drawdown.
3. Indicate gas-lift feasibility based on gas availability and GLR.
4. Indicate ESP feasibility based on depth, rate, and power availability.
5. Highlight major selection drivers.

## Example Output Summary

- The simple IPR gives an achievable rate against drawdown for the stated PI and reservoir pressure.
- Gas-lift feasibility depends on lift-gas availability and the well GLR.
- ESP feasibility depends on rate, depth, and available power, with stage count noted as screening only.
- Major selection drivers include GLR, depth, power availability, and gas supply.

## Human Review

A qualified production technology engineer must review IPR data, nodal analysis, lift selection, and equipment sizing before engineering use.
