# Example: Lift-Gas Allocation Screening (Public Synthetic Wells)

This example uses a public, synthetic well set. No confidential data is used.

## Wells

| Well | Reservoir pressure | Productivity (relative) | Current lift gas | Unit |
| --- | --- | --- | --- | --- |
| W-1 | 220 | high | 40 000 | bara / Sm³/d |
| W-2 | 180 | medium | 40 000 | bara / Sm³/d |
| W-3 | 150 | low | 40 000 | bara / Sm³/d |

- Total lift-gas budget: 120 000 Sm³/d (fixed).
- Fluid (mole fraction): methane 0.78, ethane 0.07, propane 0.05, n-butane 0.03,
  CO2 0.02, water 0.05 (normalized).
- Common manifold; arrival pressure 30 bara.

## Screening result (illustrative)

| Candidate split (W-1/W-2/W-3) | Total production trend | Note |
| --- | --- | --- |
| 40/40/40 (base) | reference | even split |
| 55/40/25 | higher | favour higher-PI well — promising |
| 30/40/50 | lower | over-lifting low-PI well risks instability |

## Outcome

Shifting lift gas toward the higher-productivity well (W-1) is the promising
direction; over-lifting the low-PI well (W-3) risks instability. Recommendation:
run a validated NeqSim production-optimization study to confirm the optimal split.

**Human review required.** This screening does not replace a validated study.
