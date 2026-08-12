# Near-Well Injectivity and Productivity Agent

Derives what the rock will give and take, instead of assuming it.

NeqSim answers what a well can **lift**. This agent answers what **feeds** it —
the productivity and injectivity indices, how they move over field life, and the
SCAL, geometry and skin assumptions behind them. The result is handed to a
NeqSim wellbore or process model as an `InflowPerformance` relationship.

Use it whenever a number like `productivityIndex = 200 Sm3/(day·bar)` is about
to be typed into a model and nobody can say where it came from.

## Tool stack

Reservoir simulation is standardised on **OPM Flow**. A second simulator is not
added unless the task genuinely cannot be done in Flow. OpenFOAM is CFD and
cannot do this work at all — no black-oil PVT, no well models, no relative
permeability.

| Tool | Role |
| --- | --- |
| **OPM Flow** 2026.04 | the reservoir simulator: black-oil, three-phase, Eclipse-format decks |
| `pyscal` | relative permeability and capillary pressure — the SCAL basis, made explicit, written as SWOF/SGOF |
| `resdata` | read the EGRID, INIT, UNRST and SMSPEC output Flow writes |
| NeqSim `BlackOilConverter` | compositional EOS fluid → black-oil PVT for the deck |
| NeqSim `InflowPerformance` | the linear, Vogel, composite and Joshi horizontal inflow models the result feeds |

## Skills

| Skill | Role |
| --- | --- |
| `neqsim-near-well-and-injectivity` | the OPM Flow stack, black-oil conversion and deck traps, fidelity choice, gridding, SCAL and the mobility-ratio reasoning |
| `neqsim-api-patterns` | building the NeqSim model that consumes the inflow relationship |
| `neqsim-subsea-and-wells` | completion, casing and barrier context |
| `neqsim-benchmark-reference-data` | validating a derived index against published data |

## What it will not do

It does not rebuild wellbore hydraulics — that is `PipeBeggsAndBrills`, and it
is already done. It produces the inflow relationship and hands it over.

It will also refuse to produce a number it cannot trace. If permeability, SCAL
and geometry are all assumed, it reports a range and says the index is an
assumption with arithmetic applied to it.

## Two things it exists to catch

**Injectivity does not always decline.** Whether it rises or falls is decided by
the endpoint mobility ratio, not by intuition. On a viscous-oil field water is
often more mobile than the oil it replaces, and injectivity improves as the bank
grows — while cold seawater into a warm reservoir can flip the ratio the other
way on its own.

**Injectors must be checked against the voidage requirement, not a rate target.**
An injector count that meets a rate target but not the voidage requirement fails
silently: pressure support collapses, rate and recovery both fall, and nothing
in the injection system reports a problem.

## Two things it exists to refuse

**A black-oil table it has not validated.** The conversion from a compositional
fluid can fail quietly — the table looks plausible plotted and every number
downstream is wrong. Rs must be continuous, strictly increasing to the bubble
point and non-zero; Bo must rise below the bubble point and fall above it.

**A simulated rate it has not sanity-checked.** Water injection an order of
magnitude above the voidage demand means the wells are on the wrong control, not
that the rock is good.

## Human review

Required. A derived index built on an analogue relative-permeability endpoint is
still an analogue number, and the agent is instructed to say so.
