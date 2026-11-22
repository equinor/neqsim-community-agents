# Example: Gas Condensate Tied Into an Asphaltenic Host

Public, synthetic case. The runnable version is
`skills/flow-assurance/neqsim-fluid-commingling-compatibility/examples/heavy_oil_condensate_tie_in.py`
in NeqSim Community Skills.

## Input

- Host oil: 18 mol % methane, C7-C30 cuts, marked asphaltenic; measured
  onset refractive index 1.445 (synthetic titration).
- Tie-in: gas condensate, 72 mol % methane, light C7-C15 cuts.
- Commingling at 200 bara and 80 C; separator 40 bara and 60 C; hydrate check
  at 120 bara; minimum operating temperature 25 C.
- Limits: separator-gas H2S 400 ppm, CO2 3 mol %.
- Planned rates: 150 t/h host oil and 25 t/h condensate.
- Blend grid: 0, 0.1, 0.2, 0.3, 0.4, the operating ratio, 0.7 and 1.0 mole
  fraction condensate.

## Expected Agent Actions

1. Quality-check both compositions.
2. Run the NeqSim blend sweep (about 15 s for eight blends).
3. Report the findings by severity and name the confirming tests.

## Expected Output (NeqSim 3.29.0)

- The planned 25 t/h of condensate is x_B = 0.49 of the blend on a molar
  basis (molar masses 0.169 and 0.029 kg/mol): the operating point sits deep in
  the unstable range, although it is only 14 % of the mass.
- **High**: live-oil refractive index falls below the onset (1.445) from 20 mol %
  condensate; the host oil alone is very stable (minimum RI 1.475 at its
  88 bara bubble point). Confirm with an onset titration or HPM test on the
  blend before accepting more than about 10 mol % condensate.
- de Boer reports no problem for every blend. The agent explains that de Boer
  describes depletion of one oil, while dilution raises the bubble point and
  shrinks the undersaturation it scores, so it cannot see this case.
- Free gas exists at the commingling point from 40 mol % condensate.
- Separator-gas H2S exceeds 400 ppm from 70 mol % condensate.
- Blend hydrate temperature 16-22 C, below the 25 C minimum operating
  temperature; free water was assumed and is stated.
- Human review required before any blending limit is set.
