# Example: MEG Loop for a Gas Tie-Back

Public, synthetic case. The runnable version is
`skills/flow-assurance/neqsim-meg-loop/examples/gas_tieback_meg_loop.py` in
NeqSim Community Skills.

## Input

- 8 MSm3/d gas (85 % methane, 6 % ethane, 3 % propane, C4-C6, 2 % CO2,
  1 % N2) with 0.6 mol % water; 20 m3/d formation water at 60 g/L TDS.
- Design point: shut-in at 150 bara and 4 C seabed, 3 C hydrate margin.
- Arrival 60 bara and 15 C; 90 wt % lean MEG regenerated at 1.2 bara;
  30 % reclaimer slipstream, 5 wt % salt limit, 150 m3 inventory.

## Expected Agent Actions

1. Confirm the design point is the coldest, highest-pressure condition.
2. Run `assess_meg_loop` with 80 and 85 wt % alternatives.
3. Report injection, rich MEG, duty and the salt balance; flag the salt
   finding and the divalent-salt caveat.
4. For a tie-in, compare the injection and duty with the host MEG system.

## Expected Result (NeqSim 3.29.0)

| Quantity | Value |
| --- | ---: |
| Uninhibited hydrate temperature | 22.2 C |
| Lean MEG injection | 2774 kg/h (60.5 m3/d) |
| Rich MEG at arrival | 49.2 wt % (Hammerschmidt 50.4) |
| Reboiler | 143.7 C, 1705 kW |
| Salt in | 1200 kg/day |
| Minimum reclaimer slipstream | 36.1 % (30 % given: high finding) |

At 80 wt % lean the injection rises to 3661 kg/h while the duty stays about
the same: the duty is set by the produced water to boil off.
