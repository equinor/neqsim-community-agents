# CCS Transport Agent

Screens a CO2 transport chain, pipeline to reservoir, with NeqSim and names
the binding link: two-phase flow, free water, impurities, dry ice on
blowdown, or bottom-hole pressure above fracture.

## How to use

1. Install the skill and NeqSim (see the
   [installation guide](../../docs/installation-guide.md)):
   `neqsim-ccs-transport-chain`, `neqsim>=3.29.0`.
2. Ask in plain language, giving the stream, pipeline, well and limits:

   ```text
   @ccs-transport-agent Screen this CO2 chain: 95.5 % CO2 with 2 % N2,
   0.5 % Ar, 0.5 % H2, 1.5 % CH4 and 50 ppm water; 80 km, 0.38 m ID,
   200 t/h from 150 bara and 35 C, seabed 4 C; 1300 m injector, reservoir
   120 bara, fracture 210 bara, MAOP 180 bara.
   ```

3. Read the station table and the findings. The agent leads with the binding
   link and suggests the fix (higher pressure, tighter impurity limits,
   wellhead choke, lower inlet pressure).

## What you get (public example, NeqSim 3.29.0)

| Check | Result |
| --- | --- |
| Lowest single-phase margin | 70.6 bar |
| Water margin factor | 42 |
| Depressurisation | Dry ice (below -56.6 C) |
| Bottom-hole pressure | 247 bara, above 210 bara fracture: binding |

See [examples/pipeline-to-aquifer.md](examples/pipeline-to-aquifer.md).

## Hand-offs

- Internal corrosion and materials: `piping-integrity-agent`
  (`neqsim-co2-corrosion-profile`, dense-phase mode).
- Near-wellbore injectivity and cooling: `near-well-injectivity-agent`.
- Blowdown and vents: `process-safety-agent`.
- Operating window over uncertain inputs: `surrogate-study-agent`.

## Limits

Screening only; verify impure-CO2 phase boundaries for design. See
[AGENT.md](AGENT.md).
