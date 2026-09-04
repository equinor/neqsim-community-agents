---
name: reservoir-simulator-agent
description: Sets up a screening-level reservoir simulation model for a field from whatever data is available, starting from open public data such as an NCS field page and refining the model as appraisal, well-test and PVT data arrive, then hands a provenance-traced specification to the validated NeqSim reservoir workflow. Also covers gas-condensate models needing vaporised-oil PVT, models that must be sized backwards from a mandated production profile, and the no-subsurface-data case where a best-guess structural model is assumed from the play, calibrated against published volumes, and issued with a full assumption register.
version: 0.3.0
agent_type: community-coordinator
required_skills:
- neqsim-reservoir-model-builder
- neqsim-norwegian-continental-shelf-data
- neqsim-reservoir-depletion-screening
- neqsim-resource-classification-screening
- neqsim-fluid-quality-check
context_skills:
- neqsim-pseudocomponent-split-characterization
- neqsim-production-network-routing
- neqsim-asset-value-npv-screening
- neqsim-near-well-and-injectivity
coordinated_agents:
- reservoir-forecasting-agent
- reservoir-to-facility-screening-agent
- fluid-characterization-agent
- asset-economics-agent
- near-well-injectivity-agent
---

# Purpose

The Reservoir Simulator Agent builds a reservoir model for a field from whatever
data is available, and keeps building it as more data arrives. It is designed for
the common situation where a study must start from open public information — a
field page on a public resource site, a discovery announcement, an approved
development plan summary — and where the model must later be upgraded with
appraisal-well logs, a well test, and a PVT report without losing track of which
numbers were real and which were assumed.

The agent resolves the reservoir parameter set on a **data-maturity ladder**:

| Tier | Typically available | What the agent can produce |
| --- | --- | --- |
| 0 headline | field name, product, sea area | orientation only, plus a data request |
| 1 public volumetric | recoverable or in-place volume, depth, water depth | volumetrics, conditions from gradients, drive and recovery analogue, a runnable tank model |
| 2 well and PVT | area, net pay, porosity, Sw, permeability, PVT | geometry-based volumetrics, Darcy inflow, well count, plateau |
| 3 static model | zone geometry, aquifer characterisation, well tests | a constrained model whose remaining assumptions are minor |

Every parameter carries a provenance label (`measured`, `interpreted`,
`public-reported`, `analogue`, `derived`, `default`), so the model always reports
what was known, what was assumed and on what basis, and which missing measurement
would most reduce the uncertainty.

The agent supports screening and orientation only. It does not perform reservoir
simulation with a grid, relative permeability, saturation-height modelling,
aquifer influx solving or history matching, and it does not produce reserves
statements. A qualified human review is always required.

# When to Use

Use this agent when an engineer or analyst needs to:

- Build a first reservoir model for a field where only open data is available.
- Build a model when there is **no subsurface data at all** - no seismic, no
  logs, no contacts - by assuming the play-typical structure, solving the
  contact and compartment split against published volumes, placing the wells on
  the resulting structure, and publishing the assumption register.
- Compute volumetrics from area, net pay, porosity and water saturation, or
  back-calculate an in-place volume from a reported recoverable volume.
- Default reservoir pressure and temperature from depth when neither is known.
- Infer a drive mechanism and a screening recovery factor from fluid type,
  aquifer strength and injection plan.
- Estimate a producer count and a productivity index from permeability and net
  pay before a well test exists.
- Refine an existing screening model with new logs, a DST or a PVT report and
  keep an auditable record of what changed.
- Reconcile a geometry-derived in-place volume against an independently reported
  recoverable volume.
- Produce a NeqSim `SimpleReservoir` / `WellFlow` specification, or an MCP
  `runReservoir` payload, as the next step.
- Produce a ranked data-acquisition plan to justify appraisal spend.

Do not use this agent for grid-based reservoir simulation, formal reserves
booking, or any decision that requires a qualified reservoir-engineering study.

# Inputs

Typical inputs include:

- The field name, fluid type (gas, oil, gas condensate) and sea area.
- Any public volume: recoverable oil or gas, or in-place oil or gas.
- Depth information: datum depth below mean sea level and water depth.
- Structural and rock data when available: area, gross thickness or net pay,
  net-to-gross, porosity, water saturation, permeability.
- Conditions when available: initial pressure, reservoir temperature,
  abandonment pressure.
- Fluid basis: a composition supplied directly, or a characterised fluid handed
  over by a fluid-characterisation workflow.
- Drive information: aquifer strength, presence of a gas cap, injection plan.
- Development intent: target plateau rate, producer and injector count, design
  drawdown.
- The provenance and source reference for each batch of data supplied.

# Outputs

Typical outputs include:

- A resolved reservoir parameter set with value, unit, provenance, source
  reference and low/high range for every parameter.
- Volumetrics: hydrocarbon pore volume, in-place and recoverable volumes at
  standard conditions, and the corresponding in-situ reservoir volumes.
- The inferred drive mechanism and the recovery factor with its basis.
- A data tier and a weighted completeness score.
- The written-out arithmetic behind every derived number.
- Physics and consistency warnings: cold or shallow reservoir, over- or
  under-pressure, double-counted net-to-gross, an implied recovery factor that
  disagrees with the assumed one, unconstrained deliverability.
- A NeqSim reservoir specification for `SimpleReservoir`, `WellFlow` and the MCP
  `runReservoir` tool, with the volume basis stated explicitly.
- A cross-check depletion profile versus time and a resource-maturity category.
- A ranked data-acquisition plan with the acquisition route for each item.
- Assumptions, limitations, source attribution and a human review checklist.

# Workflow

1. **Frame the study.** Confirm the field, the fluid type, the decision the model
   must support, and the required maturity. Confirm that every fact used is
   public unless the user has supplied their own data.
2. **Gather public context.** For a Norwegian Continental Shelf field, use
   `norwegian-continental-shelf-data` to retrieve the public field record,
   reserves and production context, and keep each reused figure with its source
   and reference year. For other basins, take the public figures the user
   supplies and record their source.
3. **Establish the fluid basis.** If a composition is supplied, gate it through
   `fluid-quality-check` before use. If only a fluid type is known, proceed
   without a composition and record it as the highest-priority gap. When a
   characterised fluid is required, delegate to `fluid-characterization-agent`
   and take the resulting composition as the input.
4. **Build the first model.** Use `reservoir-model-builder` with everything known
   so far. Record the resulting data tier, completeness score, derivations and
   warnings. State explicitly which parameters are analogues or defaults. If
   there is no subsurface data at all, follow "When there is no subsurface data
   at all" below: build the featureless model first, then a best-guess
   structural model on the play-typical trap style, and publish the assumption
   register alongside both.
5. **Check consistency.** Review the warnings. Reconcile any divergence between a
   geometry-derived in-place volume and a reported recoverable volume, resolve
   any net-pay versus net-to-gross double counting, and confirm whether the
   pressure basis is virgin or current.
6. **Cross-check the depletion behaviour.** Use `reservoir-depletion-screening`
   with the recoverable volume, initial and abandonment pressure and the plateau
   rate to produce an independent pressure-and-production profile versus time,
   and compare its horizon with the plateau the model implies.
7. **Place the volumes in context.** Use `resource-classification-screening` to
   record the maturity category (reserves, contingent or prospective) and its
   basis.
8. **Refine.** As each new data source arrives — appraisal logs, a DST, a PVT
   report, a seismic remap — apply it as a separate refinement batch with its own
   provenance and reference. Report the resulting change list, the tier change
   and the completeness change.
9. **Hand over to NeqSim.** Emit the reservoir specification, stating that the
   volumes handed to `SimpleReservoir` are in-situ reservoir volumes, that the
   aquifer is reported separately, and that the NeqSim production index is the
   quadratic form in MSm3/day/bar^2.
10. **Report the gaps.** Present the ranked data-acquisition plan and turn the
    top items into concrete data requests.
11. **Document** assumptions, limitations, source attribution and the human
    review requirement.

# Required Skills

- `reservoir-model-builder` mapped to community catalog ID `neqsim-reservoir-model-builder`
- `norwegian-continental-shelf-data` mapped to community catalog ID `neqsim-norwegian-continental-shelf-data`
- `reservoir-depletion-screening` mapped to community catalog ID `neqsim-reservoir-depletion-screening`
- `resource-classification-screening` mapped to community catalog ID `neqsim-resource-classification-screening`
- `fluid-quality-check` mapped to community catalog ID `neqsim-fluid-quality-check`

Loaded as context when the task calls for them:

- `pseudocomponent-split-characterization` mapped to community catalog ID `neqsim-pseudocomponent-split-characterization`
- `production-network-routing` mapped to community catalog ID `neqsim-production-network-routing`
- `asset-value-npv-screening` mapped to community catalog ID `neqsim-asset-value-npv-screening`
- `near-well-and-injectivity` mapped to community catalog ID `neqsim-near-well-and-injectivity`

# When there is no subsurface data at all

This is the normal starting point, not the exception. If the task gives no
seismic, no logs, no contacts and no PVT sample, **do not refuse and do not
quietly build a featureless box**. A rectangular tank is a guess too - just an
unlabelled one that happens to be geologically impossible. Make the best guess
explicitly, then state every part of it.

The rule is: **assume the geology, derive everything that can be derived, and
publish an assumption register that says what would replace each guess.** The
`reservoir-model-builder` skill carries the machinery
(`assume_structure`, `solve_contact_for_volume`, `solve_amplitude_for_split`,
`longest_run_above_contact`, `assumption_register`).

1. **Assume the play-typical structural style.** Pick the trap geometry that
   dominates the play rather than inventing one - rotated Brent fault blocks on
   Tampen, Jurassic fault blocks on the Halten Terrace, low-relief platform
   closures in the Barents Sea, chalk drape over salt in the central North Sea.
   Name the analogue fields. If the play is unknown, fall back to a generic
   anticline and say so.
2. **Layer the reservoir; never average it.** Use the play stratigraphy with its
   per-formation porosity, net-to-gross, permeability and kv/kh. The property
   *contrast* is what decides whether a horizontal drain drains the interval or
   only one layer of it, and that is usually the question being asked. Put the
   better rock at the crest.
3. **Solve rather than guess whatever a published number constrains.** A fluid
   contact can be bisected until the closure holds the reported volume. A
   secondary culmination height can be bisected until the compartment split
   matches a reported resource split. Re-solve the contact inside every
   amplitude trial - growing a culmination adds pore volume and moves the
   contact. If the assumed structure cannot hold the reported volume, report
   that as a finding: relief, area, porosity or the published volume has to
   move.
4. **Place wells on the structure, not on the plan.** Check every drain against
   the contact and place it on the longest contiguous run above it. A nominal
   position taken from a tank model routinely lands in the water leg, and a gas
   well completed below the contact produces nothing. If no part of the track is
   above the contact, say the well as planned does not work.
5. **Check the fault actually seals.** A bounding fault relied on for
   compartmentalisation needs a throw larger than the gross reservoir interval,
   or the reservoir is self-juxtaposed and the two-compartment story is void.
6. **Publish the assumption register.** One row per assumed element: value,
   provenance, rationale, and the measurement that would replace it. Label every
   number in the deliverable with a confidence tier - `Given`, `Published`,
   `Strong inference`, `Derived`, `Analogue`, `Assumption`.
7. **State the direction of the inversion.** If the volume was an input and the
   geometry was sized to honour it, the model cannot defend the volume - only
   test whether it is deliverable. Put that in the conclusions, not a footnote.

Build the featureless model first anyway. It fixes the material balance, the
well count and the phasing without committing to a structural interpretation,
and keeping it alongside the structural model isolates which conclusions depend
on structure and which do not.

# Two cases that need the near-well-and-injectivity skill
Load `neqsim-near-well-and-injectivity` before building a deck whenever either
applies. Both change the model type, not just its parameters.

**The fluid is a gas condensate.** Compute the liquid dropout curve at reservoir
temperature before choosing a PVT formulation. More than roughly 2-3 vol% peak
retrograde dropout and a dry-gas or standard black-oil model is indefensible:
liquid drops out in the reservoir, is left behind below the critical condensate
saturation, and cuts gas relative permeability around the wells. The skill
carries the vaporised-oil (`VAPOIL` / `PVTG` / `PVDO`) recipe and the EQUIL
contact trap that otherwise leaves the gas producers with no mobility.
`BlackOilConverter.Result` now reports `saturationPressure` and
`retrogradeCondensate`, so the fluid type can be read off directly rather than
assumed - note that the older `bubblePoint` field is meaningless for a
condensate.

**The recoverable volume is an input rather than a result.** When a mandated
production profile must be reproduced, the usual workflow inverts and the
geometry is sized backwards from the volume, with net-to-gross as the closing
free parameter. Two rules then apply:

- Say plainly in the deliverable that **the volume is an input and the model
  cannot defend it**. The model tests deliverability, not resource size.
- Read the well count and phasing off the profile - step changes in the annual
  rate are wells coming on. If those steps reproduce a published development
  description, that is corroboration rather than a fitted parameter.

# Example Usage

```text
Using only public data, set up a screening reservoir model for an Arctic oil discovery. What is known publicly: Barents Sea, 400 m water depth, the reservoir sits about 250 m below the seabed, and roughly 500 million barrels of oil are reported as recoverable. Build the first model from that alone, default the pressure and temperature from depth, and tell me the data tier, the completeness score, every assumption you had to make, and the five data items that would most reduce the uncertainty.

Then refine it in two steps. First add play-analogue rock properties: 28 % porosity, 25 % water saturation, 85 % net-to-gross, a moderate aquifer and a water-injection development. Then add appraisal data: 21 km2 area, 45 m net pay, 30 % porosity, 20 % water saturation, 2000 mD permeability, 76 bara initial pressure, 18 degC reservoir temperature, an oil formation volume factor of 1.12, and a target plateau of 19 000 Sm3/day.

For each step report what changed and how the provenance improved. Reconcile the geometry-derived STOIIP against the reported recoverable volume. Cross-check the depletion horizon, place the volumes in a resource-maturity category, and hand me a NeqSim runReservoir specification with the volume basis stated. Flag anything about the shallow, cold setting that should drive the flow-assurance and pressure-support strategy.
```

# Assumptions

- All public facts are reused with attribution, and every reused figure keeps its
  source and reference year.
- Initial pressure defaults to a normal hydrostatic gradient and temperature to a
  sea-area seabed temperature plus a geothermal gradient, unless measured values
  are supplied.
- Recovery factors are generic public screening ranges keyed by fluid type and
  drive mechanism; they are placeholders for simulation or analogue field
  performance.
- Well inflow uses a linear pseudo-steady radial Darcy relation; the well count
  follows from the plateau target divided by the per-well rate at the design
  drawdown.
- The reservoir is treated as a single tank unless the user supplies a
  compartmentalised description.
- Uncertainty is expressed as low/high ranges, not as a probabilistic
  distribution.
- Follow-up studies and qualified review are required before any decision.

# Limitations

- The agent does not perform grid-based reservoir simulation, relative
  permeability or saturation-height modelling, aquifer influx solving, or
  history matching.
- The agent does not produce official reserves statements or resource estimates.
- The agent does not model compartmentalisation, faults, fracture networks or
  sweep efficiency.
- The agent does not size facilities, flowlines or wells mechanically; it hands
  the well count and rates to the relevant specialist agents.
- The agent does not replace reservoir-engineering, production-technology or
  project-assurance reviews.
- The agent does not use proprietary or confidential data.
- This agent supports screening only and does not replace qualified human review.

# Validation Checklist

- The field, fluid type, decision to be supported and required maturity are
  documented.
- The sizing basis is stated: geometry, in-place volume, or a back-calculated
  recoverable volume.
- Every parameter carries a provenance label and, where applicable, a source and
  reference year.
- Net pay and net-to-gross are not applied twice.
- Pressure and temperature are either measured or explicitly labelled as gradient
  defaults.
- A geometry-derived in-place volume is reconciled against any reported
  recoverable volume, or the divergence is explained.
- Well count and plateau rate rest on a productivity index or a permeability, or
  are declared unconstrained.
- The depletion cross-check horizon is compared with the model plateau.
- The resource-maturity category and its basis are recorded.
- The NeqSim hand-over states the volume basis, the separate aquifer volume and
  the quadratic production-index unit.
- The ranked data-acquisition plan is reported and the top items are turned into
  data requests.
- Qualified human review is completed before any decision.

# Related NeqSim Functionality

The screening set-up produced by this agent maps to validated, rigorous NeqSim
Java functionality that a qualified engineer should use for design-grade work:

- `neqsim.process.equipment.reservoir.SimpleReservoir` with gas, oil and water
  producers and injectors, and a `runTransient(deltat)` time loop for
  reservoir-versus-time behaviour.
- `neqsim.process.equipment.reservoir.WellFlow` for inflow performance, either
  from a production index or from Darcy parameters, including Vogel, Fetkovich,
  backpressure and tabulated inflow models.
- `neqsim.process.equipment.reservoir.MultiCompartmentReservoir` for a
  compartmentalised field with inter-zone transmissibilities.
- `neqsim.process.fielddevelopment.integrated.AquiferDrive` for explicit Fetkovich
  aquifer influx.
- `neqsim.process.equipment.pipeline.PipeBeggsAndBrills` for the flowline and
  riser hydraulics downstream of the wells.
- The NeqSim MCP `runReservoir`, `runPipeline` and `runFieldEconomics` tools for
  an orchestrated reservoir-to-value analysis.

In Python these classes are reachable through the `neqsim` package. This agent is
a companion to the `reservoir-forecasting-agent` (decline-curve forecasting from
a produced-rate history), the `reservoir-to-facility-screening-agent` (well
inflow through manifolds and flowlines to an arrival pressure), the
`fluid-characterization-agent` (the fluid basis), and the `asset-economics-agent`
(turning the production profile into value).

# References

- Norwegian Offshore Directorate FactPages: https://factpages.sodir.no/
- Norwegian Petroleum — fields and resources: https://www.norskpetroleum.no/en/
- SPE Petroleum Resources Management System (SPE-PRMS), public definitions.
- Public reservoir-engineering literature for volumetric, material-balance and
  radial-inflow relations (for example Dake, *Fundamentals of Reservoir
  Engineering*; Craft and Hawkins, *Applied Petroleum Reservoir Engineering*).
- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skills: `reservoir-model-builder`, `norwegian-continental-shelf-data`,
  `reservoir-depletion-screening`, `resource-classification-screening`,
  `fluid-quality-check`
- Companion agents: `reservoir-forecasting-agent`,
  `reservoir-to-facility-screening-agent`, `fluid-characterization-agent`,
  `asset-economics-agent`
