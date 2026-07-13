# Reservoir Forecasting Checklist

A walkthrough for an early-stage, public-data production forecast of a Norwegian
Continental Shelf (NCS) field or well. Public data only; keep every reused figure
with its source and reference year.

## 1. Scope

- [ ] State the forecast unit (field or well) and the objective.
- [ ] Confirm the economic-limit rate and the forecast horizon.
- [ ] Confirm all inputs and facts are public and reusable with attribution.

## 2. Decline fit and forecast (`norwegian-continental-shelf-data`)

- [ ] Fit an Arps decline model to the produced-rate history with `fit_arps_decline`
      (from the peak); record the model type, decline rate, and R-squared.
- [ ] Project the forward profile with `forecast_production` to the economic-limit
      rate; record years-to-limit, remaining volume, and EUR (with cumulative to date).
- [ ] If provided, ingest the official Sodir/norskpetroleum.no production/reserves export.

## 3. Depletion cross-check (`reservoir-depletion-screening`)

- [ ] Build a tank-style pressure-and-production profile from a recoverable volume
      and offtake rate.
- [ ] Compare its horizon and remaining volume with the decline forecast; flag divergence.

## 4. Resource maturity (`resource-classification-screening`)

- [ ] Place the volumes in a reserves / contingent / prospective category.
- [ ] Record the classification basis and the project maturity stage.

## 5. Report

- [ ] Separate facts, assumptions, and recommendations.
- [ ] Keep source attribution and reference year with every reused figure.
- [ ] Name the validated NeqSim reservoir path.
- [ ] List required follow-up studies.
- [ ] Confirm qualified human review before any decision.

## Validated NeqSim path

- `SimpleReservoir` (`runTransient`) / MCP `runReservoir` for reservoir-versus-time.
- `PipeBeggsAndBrills` / MCP `runPipeline` for flowline/riser hydraulics.
- NeqSim field-economics / MCP `runFieldEconomics` to turn a forecast into value.
