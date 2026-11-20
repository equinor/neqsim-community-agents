# Example Prompts - Reservoir Mercury Agent

Use measured data with stated basis. Keep company data out of public repositories.

## Prospect without a sample

```text
Estimate mercury in the gas of a gas-condensate prospect in the Tilje Formation at 150 C and 500 bara, position 64.9 N 6.9 E, using my registry mercury_registry.json and tests.csv. Give P10/P50/P90, the probability above 10 and 100 ug/Sm3, the worst case from mineral equilibrium and a Word report.
```

## Discovery with a drill-stem test

```text
The discovery well measured 4, 9 and 22 ug/Sm3 mercury in the test gas during the main flow. Reservoir is Garn at 120 C and 400 bara. What should the design basis be, and how far could production differ?
```

## Worst case only

```text
What is the highest mercury content a gas reservoir at 90 C and 280 bara with 1 mol % CO2 can hold if mercury is held as a trace in sulfide, and at what content would liquid mercury form?
```

## Calibration

```text
Fit the mercury model on this table of tested intervals (well, formation, province, reservoir temperature, highest gas reading) and report the leave-one-well-out error against the no-predictor baseline.
```
