# Emissions Abatement Screening Checklist

A walkthrough for an early-stage, public-data screening of an emission-reduction
business case on the Norwegian Continental Shelf (NCS). Public data only; keep
every reused figure with its source and reference year.

## 1. Scope

- [ ] State the objective and the facility/process scope of the abatement study.
- [ ] Confirm the carbon-cost year (default: latest published).
- [ ] Confirm all inputs and facts are public and reusable with attribution.

## 2. Emissions baseline (`energy-emissions-screening`)

- [ ] Estimate field-life energy use, CO2e emissions, and carbon intensity, or
      take a supplied emissions basis.
- [ ] Record the CO2-by-source context (turbines dominate NCS CO2) for orientation.

## 3. Carbon-cost basis (`norwegian-continental-shelf-data`)

- [ ] Load the public Norwegian carbon-cost basis for the year with `carbon_cost_basis`.
- [ ] Record the CO2 tax (per Sm3 gas / per litre oil / per tonne CO2), the
      gas-venting tax, the EU ETS allowance cost, the combined effective cost, and
      the NOx Fund rate — each with its source URL and reference year.

## 4. Per-measure abatement screening (`norwegian-continental-shelf-data`)

- [ ] For each measure, run `abatement_screening` with CAPEX, avoided fuel gas or
      avoided CO2/NOx, any added energy cost, gas price, horizon, and discount rate.
- [ ] Report avoided carbon cost, avoided fuel value, net annual saving, simple
      payback, discounted NPV, breakeven CO2 price, and the verdict.
- [ ] State the gas combustion factor and any derived CO2 avoided explicitly.

## 5. Ranking and context (optional `asset-value-npv-screening`)

- [ ] Rank the measures by NPV and payback.
- [ ] Optionally place the abatement cash flow in a wider project NPV/IRR context.
- [ ] Record the power-from-shore context (which fields are electrified).

## 6. Report

- [ ] Separate facts, assumptions, and recommendations.
- [ ] Keep source attribution and reference year with every reused figure.
- [ ] Name the validated NeqSim energy and economics path.
- [ ] List required follow-up studies.
- [ ] Confirm qualified human review before any decision.

## Validated NeqSim path

- `GasTurbine` and combined-cycle / HRSG classes / MCP `runProcess`,
  `designUtilities` for turbine fuel use and waste-heat recovery.
- `PinchAnalysis` for heat-recovery targeting behind a measure.
- NeqSim field-economics / MCP `runFieldEconomics` for NPV/IRR/cash-flow.
