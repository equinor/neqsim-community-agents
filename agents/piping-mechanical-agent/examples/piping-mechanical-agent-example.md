# Example: Piping Mechanical Screening

This example uses a public synthetic line list for demonstration only.

## Input

- Line: 8-inch process gas line, schedule 40
- Material: carbon steel with stated allowable stress
- Design pressure: 100 bara
- Design temperature: 120 degC
- Operating temperature range: 5 degC to 120 degC
- Downstream source: pressure-reducing valve with stated pressure drop
- Screening objective: hoop stress, thermal flexibility, and AIV screening

## Expected Agent Actions

1. Review the line and identify missing data such as support spacing and branch geometry.
2. Use `piping-flexibility-screening` to screen hoop stress, minimum wall thickness, and thermal-flexibility concerns from the temperature swing.
3. Use `acoustic-induced-vibration-screening` to screen AIV likelihood of failure downstream of the valve.
4. Flag the line for detailed analysis if screening thresholds are exceeded.

## Example Output Summary

- Screening hoop stress is below the stated allowable, with adequate wall margin at the design conditions.
- The 5 degC to 120 degC swing indicates a thermal-flexibility concern to confirm with stress analysis.
- AIV likelihood of failure is reported as a screening indicator and may require small-bore connection review.
- The line is listed for detailed flexibility and AIV assessment.

## Human Review

A qualified piping mechanical engineer must review stress, flexibility, support layout, small-bore connections, and vibration risk before engineering use.
