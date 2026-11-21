# Example Prompts

## Capacity Boundary

```text
Use the Surrogate Study Agent on the public synthetic host model. Find where
the export compressor exceeds its 6.5 MW driver over tie-in rate 0-60 t/h,
separator pressure 30-70 bara and inlet temperature 30-70 C. Report the maximum
tie-in rate at the worst corner, confirm it with a direct NeqSim run, and state
how many NeqSim runs were needed.
```

## Monte Carlo on a Slow Flowsheet

```text
Use the Surrogate Study Agent to give P10/P50/P90 export gas rate and
compressor power for the uncertain inputs below. Build a global surrogate to
Q2 >= 0.99, validate it against 15 fresh NeqSim runs, and run the uncertainty
study on the surrogate. Report the validation before the percentiles.
```

## Compatibility Boundary

```text
Use the Surrogate Study Agent with the Fluid Commingling Agent's NeqSim
evaluator to learn, over condensate share 0-60 mol % and commingling pressure
100-250 bara, where the live-oil refractive index crosses the onset value 1.445.
```
