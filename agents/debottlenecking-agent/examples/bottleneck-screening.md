# Example: Bottleneck Screening (Public Synthetic Train)

This example uses a public, synthetic process train. No confidential data is used.

## Train

- Wellstream: 100 000 kg/hr, 70 bara, 60 °C; target +15% throughput.
- Fluid (mole fraction): methane 0.84, ethane 0.06, propane 0.03, n-butane 0.02,
  CO2 0.02, water 0.03 (normalized).
- Unit 1: first-stage separator, nominal 70 bara.
- Unit 2: export compressor, suction 20 bara, discharge 120 bara.
- Line: export line ID 0.30 m, length 1500 m.

## Screening result (illustrative)

| Unit / line | Screened metric | Approx. utilization | Note |
| --- | --- | --- | --- |
| First-stage separator | gas load factor | ~70% | headroom |
| Export compressor | operating-window margin | ~92% | tightest — likely bottleneck |
| Export line | velocity vs erosional guideline | ~65% | headroom |
| Export line | pressure gradient | ~60% | headroom |

## Outcome

At +15% throughput the export compressor operating window is the tightest
constraint. Candidate directions: raise suction pressure, add a parallel stage,
or relax discharge pressure. Recommendation: run a validated NeqSim capacity
study (`getUtilizationSnapshot` + `evaluate`) to confirm.

**Human review required.** This screening does not replace a validated study.
