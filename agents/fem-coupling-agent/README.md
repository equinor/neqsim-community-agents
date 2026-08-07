# fem-coupling-agent

Runs finite-element models of the *solid* - conduction, cooldown, diffusion and
thermal stress - from whatever engineering information is available, with the fluid
side taken from a NeqSim flash.

```
P&ID / STID / datasheets / insulation spec / inspection report
        |
        v
  design basis  ->  missing fields and conflicts reported, not guessed
        |
        v
  NeqSim flash  ->  density, viscosity, conductivity, heat capacity, diffusivity
        |
        v
  film coefficient  ->  Re, Pr, Nu (Gnielinski), Biot, penetration depth,
                        element size, time step
        |
        v
  1D layered FEM  ->  interface temperatures, heat flow, U
                      checked against the closed-form composite resistance
        |
        v
  2D only where the geometry stops being radial
        |
        +--> backend screening: scikit-fem | fenicsx | sfepy | mfem | openseespy | pynite
        +--> structured Gmsh mesh, layer interfaces on element boundaries
        +--> generated case, run at two refinement levels
        |
        v
  quality gate  ->  usable | usable_with_caution | not_usable
        |
        v
  handoff  ->  effective U, U-multiplier, hot-spot factor, no-touch time,
               wall stress with its category
```

The agent also works backwards: when a thermal or thermo-mechanical finite-element
report already exists, it qualifies that report and extracts numbers from it
instead of running a new model.

This is the solid-side counterpart of `cfd-coupling-agent`. CFD resolves the fluid
and produces the film coefficient; this agent consumes it and resolves the wall.

## Loaded skills

- `neqsim-fem-coupling`
- `neqsim-cfd-coupling` (as relevant, when the film coefficient needs a resolved
  flow field rather than a correlation)

## Typical requests

- "A 0.4 m section of insulation on 20-P-001 is flooded - what U-value should the
  pipeline model carry?"
- "How long before this shut-in line reaches the hydrate temperature?"
- "What is the metal temperature gradient across the wall, and what thermal stress
  does it produce?"
- "Size the mesh and the time step for a twelve-hour cooldown on this build-up."
- "We have a vendor thermal FEM report for the clamp - can we use its heat flux?"
- "Does this problem even need a finite-element model?"

## Human review

Required. A `usable_with_caution` verdict means any derived factor must carry an
explicit uncertainty band, and a qualified thermal or stress analyst must review
before the number is used in a design decision.

See `AGENT.md` for the full workflow, inputs, outputs and traps.
