# Example: Production Optimization Screening (Public Synthetic Train)

This example uses a public, synthetic process train. No confidential data is used.

## Train

- Stream: wellstream, 100 000 kg/hr, 70 bara, 60 °C.
- Fluid (mole fraction): methane 0.82, ethane 0.07, propane 0.04, n-butane 0.02,
  CO2 0.02, water 0.03 (normalized).
- Unit 1: first-stage separator, nominal 70 bara.
- Unit 2: second-stage separator, nominal 20 bara.
- Unit 3: export compressor, suction 20 bara, discharge 120 bara.

## Decision variables

| Variable | Low | Base | High | Unit |
| --- | --- | --- | --- | --- |
| First-stage pressure | 60 | 70 | 80 | bara |
| Export discharge pressure | 110 | 120 | 130 | bara |

## Objective

Maximize export gas throughput subject to: export compressor inside operating
window, compression power within a public guideline, arrival pressure ≥ 110 bara.

## Screening result (illustrative)

| Candidate | Throughput trend | Window OK? | Power trend | Note |
| --- | --- | --- | --- | --- |
| Base | reference | yes | reference | baseline |
| +5 bar first stage | slightly higher | yes | slightly higher | promising, screen further |
| +10 bar first stage | higher | check | higher | near window edge — validate |

## Outcome

Raising first-stage pressure shows a promising throughput direction but the
larger step approaches the compressor window edge. Recommendation: run a
validated NeqSim optimization (`ProcessAutomation.evaluate` /
`AgenticProcessOptimizer`) to confirm feasibility and quantify the gain.

**Human review required.** This screening does not replace a validated study.
