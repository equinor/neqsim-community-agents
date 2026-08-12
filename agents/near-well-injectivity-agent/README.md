# Near-Well Injectivity and Productivity Agent

Derives what the rock will give and take, instead of assuming it.

NeqSim answers what a well can **lift**. This agent answers what **feeds** it —
the productivity and injectivity indices, how they move over field life, and the
SCAL, geometry and skin assumptions behind them. The result is handed to a
NeqSim wellbore or process model as an `InflowPerformance` relationship.

Use it whenever a number like `productivityIndex = 200 Sm3/(day·bar)` is about
to be typed into a model and nobody can say where it came from.

## Tool stack

| Tool | Role |
| --- | --- |
| `open-darts` | near-well and full-field reservoir simulation in pure Python |
| `pyscal` | relative permeability and capillary pressure — the SCAL basis, made explicit |
| `resdata` | read Eclipse/E300 restart, summary and grid output |
| `welltestpy` | interpret drawdown and buildup tests |
| `opm`, `ResSimPy` | deck parsing and model manipulation |
| NeqSim `InflowPerformance` | the linear, Vogel, composite and Joshi horizontal inflow models the result feeds |

## Skills

| Skill | Role |
| --- | --- |
| `neqsim-near-well-and-injectivity` | the tool stack, fidelity choice, gridding, SCAL and the mobility-ratio reasoning |
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
grows.

**Injectors must be checked against the voidage requirement, not a rate target.**
An injector count that meets a rate target but not the voidage requirement fails
silently: pressure support collapses, rate and recovery both fall, and nothing
in the injection system reports a problem.

## Human review

Required. A derived index built on an analogue relative-permeability endpoint is
still an analogue number, and the agent is instructed to say so.
