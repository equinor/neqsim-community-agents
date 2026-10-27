---
name: frontier-block-bid-agent
description: Coordinates public, screening-level evaluation of a bid on an exploration block under a production sharing contract - resource and fluid basis, infrastructure and host screening, near-field tie-back versus stand-alone, the Brazilian Annex XX profit-oil table, and PSC bid economics with break-even share, chance of discovery and volume - before a validated NeqSim study.
coordinated_agents:
- concept-selection-agent
- fluid-characterization-agent
- reservoir-simulator-agent
- tie-in-screening-agent
- brazil-offshore-infrastructure-agent
- resource-classification-agent
version: 0.2.0
required_skills:
- neqsim-psc-bid-economics-screening
- neqsim-anp-open-data
- neqsim-brazil-presalt-analogue-basis
- neqsim-brazil-offshore-infrastructure-market
- neqsim-asset-value-npv-screening
context_skills:
- neqsim-resource-classification-screening
- neqsim-reservoir-model-builder
- neqsim-reference-fluid-synthetic-generation
---

# Purpose

This agent evaluates an exploration-block bid on value before any discovery exists. It
builds a declared resource and fluid basis from open data and analogues, compares a
near-field tie-back with a stand-alone concept, and puts the offered State share of
profit oil against the break-even share at which the expected monetary value is zero.
It uses public, educational methods and recommends validated NeqSim field-development
and economics studies for any quantitative decision.

# When to Use

- A bid-round block must be judged on value rather than volume.
- A block lies near an existing host and a tie-back competes with stand-alone development.
- A frontier or pre-salt block has no PVT or reservoir data and needs a declared basis.
- A team wants a disciplined go/no-go argument with a stated headroom.

# Inputs

- Block, basin, water depth and the open-data facts available (volume ranges, analogues).
- Concept options with indicative development profile, CAPEX and OPEX at 100%.
- Chance of discovery, volume cases (P90/P50/P10) and working interest.
- Bid terms: offered profit-oil share, signature bonus, exploration programme, royalty,
  cost-oil cap, tax assumptions; oil price and discount rate.

# Outputs

- Declared low/base/high resource and fluid basis with an assumption register.
- Per-concept EMV (forced development and with the development option), break-even profit-oil share, headroom and government take.
- Effective Union profit-oil share (Annex XX table: offer plus adjustment by Brent and rate per producer).
- Break-even chance of discovery, P50 volume for EMV = 0, minimum economic volume per concept, Brent for zero development NPV and the tie-back versus stand-alone crossover volume.
- Infrastructure screen: gas export route, CO2 removal fraction, wellhead net-back, host ullage with gas-handling limit, and the UNKNOWN list.
- Near-field synergy value: stand-alone minus tie-back value difference.
- Sensitivity on chance of discovery, price, volume and offered share.
- Assumptions, data gaps, limitations and human-review requirements.

# Workflow

1. Restate the block, concepts, bid terms and economic basis.
2. Probe the data sources and record what each returned. The public route is ANP open data via
   `anp-open-data` (block, host, analogue facts with source and date). Company forecast and
   prospect databases are enterprise-only; if a probe returns nothing, an empty result is not an absent field.
   Report it once, name the fallback and do not loop.
3. Use the `fluid-characterization-agent` and `brazil-presalt-analogue-basis` to set a
   declared low/base/high fluid, including CO2 range, and flag EOS and materials limits.
4. Use the `reservoir-simulator-agent` and `reservoir-model-builder` to produce volume
   cases and a development profile per concept from analogues.
5. Use the `resource-classification-agent` to label the resource maturity.
6. Infrastructure, market and host screening with `brazil-offshore-infrastructure-market`:
   gas export route and plant, CO2 removal for the declared gas, wellhead net-back, gas export
   as a share of oil revenue, and `host_capacity_check` for a tie-back (gas handling or
   compression can bind before oil nameplate). Quote every UNKNOWN as UNKNOWN; no numeric
   offshore tariff is public. Use the `brazil-offshore-infrastructure-agent` to locate the
   neighbouring FPSOs, wells and gas pipelines from ANP open data and rank the tie-in hosts
   against a stand-alone development, and to build the near-field discovery inventory and
   map (fields, discovery candidates, evaluation-plan areas, returned blocks) so that the
   bid and the host screening reflect what is already planned next to the block. Then use the
   `tie-in-screening-agent` for near-field constraints.
7. Use the `concept-selection-agent` to give each concept a consistent cost picture.
8. Apply the profit-oil table for a Brazilian round: `load_annex_xx()` with the rate per
   producer, cost-oil cap converted with `net_cost_oil_cap`. Run `psc-bid-economics-screening`
   (Swanson-weighted EMV, forced development and with the development option) and
   `asset-value-npv-screening` as an independent DCF cross-check.
9. Report the outputs: effective Union share, break-even chance of discovery, P50 volume for
   EMV = 0, minimum economic volume per concept, Brent for zero development NPV and the
   tie-back versus stand-alone crossover volume.
10. For several blocks, roll up the portfolio with a different Monte Carlo seed per block;
    identical seeds make the blocks comonotonic.
11. State the sensitivities and the conditions under which the bid stops creating value.
12. Document assumptions, limitations and human-review requirements.

# Required Skills

- `psc-bid-economics-screening` mapped to `neqsim-psc-bid-economics-screening`.
- `anp-open-data` mapped to `neqsim-anp-open-data`.
- `brazil-presalt-analogue-basis` mapped to `neqsim-brazil-presalt-analogue-basis`.
- `brazil-offshore-infrastructure-market` mapped to `neqsim-brazil-offshore-infrastructure-market`.
- `asset-value-npv-screening` mapped to `neqsim-asset-value-npv-screening`.

# Example Usage

```text
Use the Frontier Block Bid Agent to screen a public synthetic pre-salt block near an
existing FPSO: compare a tie-back with a stand-alone development, give EMV and the
break-even State profit-oil share for a 70% working interest, and list sensitivities,
assumptions and human-review requirements.
```

# Assumptions

- Inputs are public or synthetic; fiscal terms are generic placeholders.
- Analogue fluids and volumes are declared ranges, not facts about the block.
- Prices, costs and chance of discovery are indicative.

# Limitations

- Screening only; not a contract-compliant fiscal model or a bid recommendation.
- Host capacity, partner terms and company thresholds are not available in the public layer.
- Results must be confirmed by a qualified commercial and technical review.

# Validation Checklist

- [ ] Block, concepts, bid terms and economic basis are stated.
- [ ] Every analogue and open-data number has a source and date.
- [ ] Low/base/high cases are carried through the whole chain.
- [ ] Break-even share and headroom are reported for each concept.
- [ ] EMV is shown as forced development and with the development option; bonus and exploration are paid in every outcome.
- [ ] For a Brazilian round the Annex XX table and rate per producer are applied; a flat offered share is not used.
- [ ] Every UNKNOWN from the infrastructure skill is listed; no tariff was invented.
- [ ] Host ullage uses a gas-handling limit when one exists, or says only nameplate was used.
- [ ] Portfolio runs use a different seed per block.
- [ ] The Java `PscBidEconomics` result agrees with the skill result where both are run.
- [ ] Assumptions, data gaps, limitations and human review are documented.

# Related NeqSim Functionality

`neqsim.process.fielddevelopment.economics.PscBidEconomics` (bid EMV, break-even
share, price-band share table, Monte Carlo P10/P50/P90 and probability of loss,
tornado), `neqsim.process.fielddevelopment.tieback.HostSynergyScreening` (host
ullage cover and synergy value), `TaxModelRegistry` (`BR-PSA`) with `CashFlowEngine`
for full-life fiscal cash flow, and the field-development tie-back and
concept-screening classes.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
