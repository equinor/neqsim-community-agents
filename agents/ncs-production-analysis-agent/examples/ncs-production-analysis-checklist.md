# NCS Production Analysis Checklist

A walkthrough for an early-stage, public-data analysis of Norwegian Continental
Shelf (NCS) production. Public data only; keep every reused figure with its
source and reference year.

## 1. Scope

- [ ] State the objective: facts/inventory query, resource accounting,
      time-series analysis, or a forward production-to-value screening.
- [ ] Confirm all inputs and facts are public and reusable with attribution.

## 2. Load the NCS reference database (`norwegian-continental-shelf-data`)

- [ ] Load the bundled public snapshot and record the attribution and snapshot date.
- [ ] Answer the national/resource/field-inventory question with source URLs.
- [ ] If provided, ingest the official Sodir/norskpetroleum.no yearly-production CSV.

## 3. Resource accounting

- [ ] Compute the produced-versus-remaining split from the published total.
- [ ] Compute a static reserves-to-production horizon (label it a ratio, not a forecast).

## 4. Production time series (if available)

- [ ] Report the trend and CAGR from first to last year.
- [ ] Report the oil/gas/NGL/condensate share of oil equivalent for the latest year.

## 5. Forward screening (optional, `reservoir-depletion-screening`)

- [ ] Build a reservoir pressure and production profile versus time.
- [ ] Optionally run `asset-value-npv-screening` for NPV/IRR/payback.
- [ ] Optionally run `energy-emissions-screening` for CO2e and carbon intensity.

## 6. Report

- [ ] Separate facts, assumptions, and recommendations.
- [ ] Keep source attribution and reference year with every reused figure.
- [ ] Name the validated NeqSim reservoir and economics path.
- [ ] List required follow-up studies.
- [ ] Confirm qualified human review before any decision.

## Validated NeqSim path

- `SimpleReservoir` (`runTransient`) / MCP `runReservoir` for reservoir-versus-time.
- `PipeBeggsAndBrills` / MCP `runPipeline` for flowline/riser hydraulics.
- NeqSim field-economics / MCP `runFieldEconomics` for NPV/IRR/cash-flow.
