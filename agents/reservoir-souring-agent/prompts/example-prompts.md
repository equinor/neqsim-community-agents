# Example Prompts - Reservoir Souring Agent

Use measured data with stated basis. Keep company data out of public repositories.

## Gas to wellstream

```text
Gas H2S measured at the 70 C, 10 bara first-stage separator is 170 ppmv. For a wellstream with 30 percent water mole fraction, back-calculate the wellstream H2S, report how the H2S splits between gas, oil and water, and give the conversion factor for water fractions from 0 to 0.6.
```

## Per-well correlation

```text
Fit an H2S-versus-seawater-fraction correlation for this well from the paired series [f_sw, wellstream H2S ppmv], pick the best model, report valid range, R2 and warnings, and save it to the correlation registry.
```

## Update

```text
New measurements for this well arrived. Refit with a half-life of 20 points, compare with the previous correlation and tell me if the model family or the prediction at the highest seawater fraction changed by more than 25 percent.
```

## Plausibility

```text
Is a wellstream H2S of 60 ppmv at 40 percent seawater fraction plausible for 2700 mg/L injected sulfate, 300 mg/L formation-water VFA and a mixing-zone temperature of 70 C? Show the substrate-limited bound with and without sulfate removal.
```
