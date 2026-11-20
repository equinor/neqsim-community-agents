# NCS value-chain study checklist

## 1. Frame
- [ ] Request type: map / load / resilience / optimise / tie-in / invest / process hand-off
- [ ] Horizon and scenario agreed (years, prices, tariffs, discount rate, outages)
- [ ] Snapshot date stated; live refresh (`scripts/build_snapshot.py`) if the current year matters

## 2. Map the system (`neqsim-ncs-infrastructure-network`)
- [ ] `export_routes(field)` for the fields in scope; `needs_review` routes read against Sodir text
- [ ] `utilization(year)` routes > 99 % of production, nothing above capacity
- [ ] `single_points_of_failure(year)` and `outage_impact(element, year)` for the elements in scope
- [ ] Capacities quoted with `source_url`; estimates flagged

## 3. Optimise (`neqsim-ncs-value-chain-optimization`)
- [ ] Supply methods reviewed (`supply[entity].method`); overrides from `reservoir-forecasting-agent` where relevant
- [ ] All years `optimal`; `bottlenecks`, `curtailment`, `ullage_timeline` read
- [ ] `tiein_ranking` with status/RC; `stranded_discoveries` listed
- [ ] `production_uplift`: field-limited vs network-limited separated

## 4. Verify with NeqSim
- [ ] `run_tieback_screening` for the top tie-ins (TiebackAnalyzer)
- [ ] `run_trunk_hydraulics` for any stressed path (LoopedPipeNetwork)
- [ ] `value_objective_check` relative difference < 1e-6 (ValueChainObjective)
- [ ] `run_debottlenecking` with user/cited CAPEX (DebottleneckingAdvisor)
- [ ] `process_model_targets` handed to `optimize-processmodel` for the host

## 5. Report
- [ ] Facts, assumptions and recommendations separated; sources and years kept
- [ ] Follow-up studies named; qualified human review recorded
