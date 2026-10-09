---
name: frontier-block-bid-agent
description: Coordinates public, screening-level evaluation of a bid on an exploration block under a production sharing contract - resource and fluid basis, near-field tie-back versus stand-alone concept, and PSC bid economics with the break-even offered profit-oil share - before a validated NeqSim study.
version: 0.1.0
required_skills:
- neqsim-psc-bid-economics-screening
- neqsim-anp-open-data
- neqsim-brazil-presalt-analogue-basis
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
- Per-concept EMV, break-even profit-oil share, headroom and government take.
- Near-field synergy value: stand-alone minus tie-back value difference.
- Sensitivity on chance of discovery, price, volume and offered share.
- Assumptions, data gaps, limitations and human-review requirements.

# Workflow

1. Restate the block, concepts, bid terms and economic basis.
2. Use `anp-open-data` to collect block, host and analogue facts with source and date.
3. Use the `fluid-characterization-agent` and `brazil-presalt-analogue-basis` to set a
   declared low/base/high fluid, including CO2 range, and flag EOS and materials limits.
4. Use the `reservoir-simulator-agent` and `reservoir-model-builder` to produce volume
   cases and a development profile per concept from analogues.
5. Use the `resource-classification-agent` to label the resource maturity.
6. Use the `tie-in-screening-agent` for the near-field concept constraints.
7. Use the `concept-selection-agent` to give each concept a consistent cost picture.
8. Use `psc-bid-economics-screening` for EMV, break-even share and headroom per concept,
   and `asset-value-npv-screening` as an independent DCF cross-check.
9. State the sensitivities and the conditions under which the bid stops creating value.
10. Document assumptions, limitations and human-review requirements.

# Required Skills

- `psc-bid-economics-screening` mapped to `neqsim-psc-bid-economics-screening`.
- `anp-open-data` mapped to `neqsim-anp-open-data`.
- `brazil-presalt-analogue-basis` mapped to `neqsim-brazil-presalt-analogue-basis`.
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
