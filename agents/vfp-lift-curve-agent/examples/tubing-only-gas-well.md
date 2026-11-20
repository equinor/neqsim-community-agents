# Example: tubing-only VFPPROD for a synthetic deviated gas well

Public synthetic basis; no field data.

## Request

A gas-condensate producer, datum 2500 m TVD, survey stations (MD/TVD) 0/0, 1500/1450, 3200/2500 m, inner diameter
0.15 m, flowing temperatures 95 C at the bottom and 40 C at the wellhead. Surface gas methane 0.90, ethane 0.06,
propane 0.03, n-butane 0.01; condensate n-hexane 0.6 and n-octane 0.4. Expected ranges: rate 0.2-1.0 MSm3/d,
wellhead pressure 40-80 bara, WGR 1e-6 to 1e-4 Sm3/Sm3, OGR 1e-5 to 1e-4 Sm3/Sm3. Simulator OPM Flow, METRIC,
table number 1.

## What the agent does

1. Chooses a tubing-only table; THP axis = wellhead pressure; datum 2500 m TVD.
2. Builds `RecombinationFluidFactory` (GAS, WGR, OGR) and `TubingVlpProvider` with Gray and six segments.
3. Calibrates roughness on gauge rows if provided; otherwise labels the table "uncalibrated screening".
4. Axes: `rateAxis(0.2e6, 1.0e6, 8, 1.3)`, `pressureAxis(40, 80, 6, 0.3, 0.1)`, three points in each ratio axis.
5. Builds with `RateMonotoneMode.FULL` for OPM Flow and a rate cap if a compressor limit applies.
6. Validates: warnings, round trip, three off-grid solves within 0.3 bar, IPR x VFP against the supplied inflow.
7. Writes `vfp1.inc` with the provenance header and reports the minimum stable rate from the raw curve.

## Expected outputs

- `vfp1.inc` (VFPPROD, 1-based indices, BHP in bara)
- validation table with off-grid errors and the repair count
- a note on extrapolation limits and the group rate limit the deck must carry
