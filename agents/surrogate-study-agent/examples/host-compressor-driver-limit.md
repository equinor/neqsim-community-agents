# Example: Tie-in Rate Limited by a Host Compressor Driver

Public, synthetic case. The runnable version is
`skills/process/neqsim-active-learning-surrogate/examples/host_compressor_capacity_boundary.py`
in NeqSim Community Skills.

## Input

- NeqSim host model: 150 t/h host well stream plus tie-in gas, inlet
  separator, export compressor to 150 bara at 75 % isentropic efficiency.
- Inputs: tie-in rate 0-60 t/h, separator pressure 30-70 bara, inlet
  temperature 30-70 C.
- Limit: compressor power 6,500 kW (driver rating).
- Uncertainty: tie-in rate triangular 10/35/55 t/h, separator 40-60 bara,
  inlet 35-60 C.

## Expected Agent Actions

1. Time one NeqSim run (about 0.3-0.5 s).
2. Run the limit-state learner with a 40-run budget.
3. Validate against 8 fresh NeqSim runs.
4. Compute the exceedance probability and the maximum tie-in rate at the
   worst corner (40 bara, 60 C); confirm that rate with a direct NeqSim run.

## Expected Output (NeqSim 3.29.0)

- Converged after 21 NeqSim runs (about 5 s of NeqSim time), no failures.
- 20,000 surrogate evaluations in about 0.1 s; direct NeqSim would take
  about 2.8 h.
- Compressor power P10/P50/P90 about 4,000 / 5,050 / 6,300 kW; probability of
  exceeding 6,500 kW about 7 %.
- Maximum tie-in rate at 40 bara / 60 C: 28.3 t/h. A direct NeqSim run at
  28.3 t/h gives 6,499 kW.
- Validation: 100 % side-of-limit agreement, maximum power error about 35 kW.
- Human review required before the rate limit is used.
