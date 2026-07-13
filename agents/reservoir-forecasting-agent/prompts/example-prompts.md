# Example Prompts — Reservoir Forecasting Agent

Use public data only. Keep every reused figure with its source and reference year.

## Fit a decline curve

```text
Fit an Arps decline curve to this annual gas production history [(2018, 3.2), (2019, 2.8), (2020, 2.45), (2021, 2.15), (2022, 1.9), (2023, 1.68) GSm3/year]. Report the decline model type (exponential/hyperbolic/harmonic), the nominal decline rate, the initial rate at the peak, and the goodness of fit.
```

## Forecast to an economic limit

```text
Using the fitted decline, project the forward production profile to an economic-limit rate of 0.3 GSm3/year over a 30-year horizon. Report the years to the economic limit, the remaining volume, and the estimated ultimate recovery given 22 GSm3 produced to date.
```

## Cross-check with reservoir depletion

```text
Cross-check the decline forecast against a tank-style reservoir-depletion screening for a 35 GSm3 recoverable volume declining from 320 to 90 bara at 3.5 GSm3/year. Compare the horizon and remaining volume between the two methods and flag any material divergence.
```

## Resource maturity and report

```text
Place the field volumes in a resource-classification maturity (reserves / contingent / prospective) for a producing field, name the validated NeqSim reservoir workflow, and prepare a screening forecast report outline with assumptions, limitations, and a human review checklist. Keep every figure with its source and reference year.
```
