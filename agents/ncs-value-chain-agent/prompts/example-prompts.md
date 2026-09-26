# Example prompts

## System map
Using open data, show how Johan Sverdrup, Troll and Aasta Hansteen gas reaches the market, which pipelines and plants each shares with other fields, and the bottleneck capacity on each route.

## Bottlenecks in a year
Load the NCS gas system for 2025 from Sodir production. List the ten most loaded trunklines and plants with flow, capacity and source, and the single points of failure ranked by stranded production.

## Outage
Kollsnes runs at 70 % for all of 2027. Using the value-chain optimiser, report curtailed production by field, where gas reroutes, the shadow price of Kollsnes capacity, and the NPV of adding 10 MSm3/d at a CAPEX of 3000 MNOK with NeqSim DebottleneckingAdvisor.

## Tie-in ranking
Rank the discoveries in clarification phase or later by the discounted revenue the network can accept from 2026 to 2040. For the top three, give the host, distance and first year, and run NeqSim TiebackAnalyzer against the three nearest hosts.

## Production uplift
Which producing fields could ship more oil or gas in 2026? For each, is the limit the field itself or a pipeline/plant, and what is the uplift worth per year?

## Host hand-off
Give the rate targets (own production plus tie-ins) that the Goliat FPSO process model must handle from 2029 to 2035, and the spare capacity on its export route, formatted for the NeqSim optimize-processmodel agent.
