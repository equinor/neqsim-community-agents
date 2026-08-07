# cfd-coupling-agent

Runs single-phase and multiphase CFD from whatever engineering information is
available, with the fluid taken from a NeqSim flash.

```
P&ID / STID / datasheets / plant data
        |
        v
  design basis  ->  missing fields and conflicts reported, not guessed
        |
        v
  NeqSim flash  ->  density, viscosity, speed of sound, flow
                    (multiphase: both phases + interfacial tension)
        |
        v
  boundary conditions  ->  Re, Ma, regime, k / epsilon / omega, solver class
                           (multiphase: We, Fr, Stokes, model screening)
        |
        v
  OpenFOAM case  ->  steady RANS, or transient volume of fluid
        |
        v
  quality gate  ->  usable | usable_with_caution | not_usable
        |
        v
  enhancement factors  ->  velocity, wall shear, mass transfer
```

The agent also works backwards: when a CFD report already exists, it qualifies
that report and extracts factors from it instead of running a new case.

## Loaded skills

- `neqsim-cfd-coupling`

## Typical requests

- "Compute the wall shear in line 20-P-001 from the P&ID and the STID dimensions."
- "Is this two-phase line stratified, and how much liquid collects in the low point?"
- "We have a vendor CFD report for the inlet device - can we use its peak velocity?"
- "Size the near-wall mesh for a y+ of 50 on this gas stream."
- "What local enhancement factor should the corrosion screening use at this bend?"

## Human review

Required. A `usable_with_caution` verdict means any derived factor must carry an
explicit uncertainty band, and a qualified CFD engineer must review before the
factor is used in a design decision.

See `AGENT.md` for the full workflow, inputs, outputs and traps.
