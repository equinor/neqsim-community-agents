# Agent Catalog and Workflows

This page is the reader-friendly overview of every agent in **NeqSim Community
Agents**: what each agent does, how the agents are grouped by discipline, and
which multi-agent workflows chain them together.

It is written to be read as documentation. You do not need to open any
`AGENT.md` file to understand what this repository offers.

- **Installing the agents:** [Installation Guide](installation-guide.md)
- **Machine-readable delegation graph:** [Orchestration Map](ORCHESTRATION_MAP.md)
- **Machine-readable skill dependencies:** [Agent Skill Map](AGENT_SKILL_MAP.md)
- **What a good agent must contain:** [Agent Standard](agent-standard.md)

---

## 1. How to read this catalog

### Agent types

Every agent declares an `agent_type` in its `agent.yaml`:

| Type | Meaning |
|------|---------|
| `community-agent` | A **specialist**. Performs one bounded screening job using one or a few skills. |
| `community-coordinator` | A **coordinator**. Frames the problem, delegates to specialist agents, and assembles their outputs into one comparable view. Coordinators do not hide the specialists — the delegation is declared in `coordinated_agents`. |

### What every agent gives you

The [Agent Standard](agent-standard.md) requires each agent to return the same
shape of answer, regardless of discipline:

- the screening result, with the numbers and the method used
- the **inputs it needed** and which of them were missing
- **assumptions and limitations** made explicit
- a **validation checklist**
- **recommended follow-up analysis** — what a validated NeqSim study should do next
- a **human review** requirement

### Scope: screening, not design

Community agents use **public, educational methods** and public data only. They
are built for early-stage screening, teaching, and framing — to tell you whether
an idea is worth a detailed study and what that study must cover. They are not a
substitute for a validated NeqSim study, project procedures, regulatory
requirements, or qualified engineering review.

### Invoking an agent

After installation the agents appear in GitHub Copilot Chat:

```text
@hydrate-screening-agent  Is there hydrate risk at 80 bara and 8 °C for this gas?
@asset-economics-agent    Concept economics for a 40 MMboe subsea tieback
@flow-assurance-study-agent  Plan a flow-assurance study for a 25 km wet-gas tieback
```

---

## 2. Agent catalog

The repository contains **48 agents**. They are grouped below by the engineering
question they answer.

### 2.1 Fluids, PVT and characterization

| Agent | What it does |
|-------|--------------|
| `pvt-agent` | Fluid characterization, composition checks, phase-behaviour evaluation, and thermodynamic analysis. |
| `fluid-characterization-agent` | Plus-fraction split-factor characterization, reference-fluid synthetic generation, and PVT regression of a characterization factor for reproducible fluid modelling. |
| `e300-fluid-agent` | Reads Eclipse E300 files into NeqSim fluids, writes NeqSim fluids back to E300, and adds water using public PVTsim water parameters. |

### 2.2 Reservoir and subsurface

| Agent | What it does |
|-------|--------------|
| `reservoir-simulator-agent` *(coordinator)* | Sets up a screening-level reservoir model from whatever data exists — starting from open public data such as an NCS field page — and refines it as appraisal, well-test, and PVT data arrive. |
| `reservoir-forecasting-agent` *(coordinator)* | Fits an Arps decline curve to a produced-rate series and cross-checks it against depletion screening and resource maturity to project a forward profile, remaining volume, and EUR. |
| `ncs-production-analysis-agent` *(coordinator)* | Frames production, resource-accounting, and field-inventory studies from a source-attributed Norwegian Continental Shelf reference-facts database. |
| `resource-classification-agent` | Classifies resources on the public SODIR RC0–RC9 maturity ladder and the SPE-PRMS category axis, without confusing maturity with quantity uncertainty. |
| `near-well-injectivity-agent` | Derives productivity and injectivity indices from the rock instead of assuming them, using OPM Flow with pyscal and resdata, and hands a defensible inflow relationship to wellbore and process models. |
| `reservoir-to-facility-screening-agent` *(coordinator)* | Chains reservoir depletion versus time, well inflow, manifold routing, and flowline/riser pressure drop into a platform arrival-pressure roll-up with time development. |

### 2.3 Wells and artificial lift

| Agent | What it does |
|-------|--------------|
| `artificial-lift-agent` | Screens gas-lift versus ESP feasibility against a simple inflow performance relationship. |
| `gas-lift-allocation-agent` | Frames lift-gas allocation across a small set of gas-lifted wells and ranks candidate splits. |

### 2.4 Flow assurance

| Agent | What it does |
|-------|--------------|
| `flow-assurance-engineer-agent` *(coordinator)* | Checks operating points against public hydrate-margin and wax-margin guidelines; the usual entry point for flow-assurance questions. |
| `flow-assurance-study-agent` *(coordinator)* | Runs a reviewable study: freezes the engineering basis, delegates calculations to the NeqSim and OLGA specialists, and enforces like-for-like validation gates. |
| `hydrate-screening-agent` | Preliminary hydrate risk assessment with recommended follow-up analysis. |
| `subsea-cooldown-agent` | Flowline and riser cooldown screening — checks no-touch time against hydrate-margin guidelines. |
| `sand-erosion-agent` | Subsea and topside erosional-velocity and remaining-wall-life screening. |
| `produced-water-scale-agent` | Builds produced-water brines from ion analyses, presets, or TDS values and evaluates scale risk indicators. |
| `olga-simulation-agent` *(coordinator)* | Runs the OLGA transient multiphase simulator end to end — locates the engine, rule-checks the case, executes it in batch, decodes the exit status, and reads trend and profile results. |
| `pipe-route-screening-agent` *(coordinator)* | Builds a route elevation profile and checks arrival pressure drop, line velocity, and hydrate margin. |

### 2.5 Subsea layout and pipelines

| Agent | What it does |
|-------|--------------|
| `subsea-layout-screening-agent` *(coordinator)* | Turns a supplied subsea map into a well and tie-back inventory with step-out distances, route profiles, and seabed slope flags. |
| `surf-layout-design-agent` *(coordinator)* | Designs a screening SURF layout and places the host from open map, bathymetry, and licence-block data, then routes and sizes every flowline, riser, and umbilical. |
| `pipeline-survey-profile-agent` | Cleans as-built survey data into a pipeline profile, flags erroneous points, screens free-span and cover candidates, and compares repeat surveys. |
| `tie-in-screening-agent` | Early-stage screening of tie-in opportunities with fluid, flow-assurance, and process checks. |

### 2.6 Process engineering and screening

| Agent | What it does |
|-------|--------------|
| `process-engineer-agent` | Checks unit operations against line-velocity and compressor operating-window guidelines. |
| `process-screening-agent` | High-level process screening studies and engineering checklist generation. |
| `debottlenecking-agent` | Identifies the most likely capacity bottleneck in a train — separator, compressor window, line velocity, or pressure drop — and ranks units by utilization. |
| `production-optimization-agent` | Searches operating setpoints (separation pressures, compressor discharge, routing) for higher throughput or lower compression power within capacity and operating-window limits. |
| `gas-treatment-agent` | Checks gas water content and dehydration against a sales-gas spec and estimates single-stage compression power. |
| `teg-dehydration-agent` | Builds and runs a validated NeqSim TEG dehydration plant and reports water dew point, lean-TEG purity, and regeneration still-vent emissions. |
| `gas-export-pipeline-agent` | Chains line velocity, pressure drop, and export compression power into a gas-export line screen. |

### 2.7 Rotating equipment and drivers

| Agent | What it does |
|-------|--------------|
| `compressor-antisurge-agent` | Sets up anti-surge recycle control for a centrifugal compressor — chart generation, steady-state recycle initialization, dynamic anti-surge control, and hot/cold recycle and speed-runback topology binding. |
| `reciprocating-compressor-agent` | Screens staging, volumetric efficiency, discharge temperature, and rod load. |
| `gas-turbine-screening-agent` | Screens driver site-rating, heat rate, and exhaust conditions. |

### 2.8 Dynamic simulation and control

| Agent | What it does |
|-------|--------------|
| `dynamic-process-preparation-agent` | Prepares `ProcessSystem` and `ProcessModel` flowsheets for dynamic calculation, with mechanical-design and volume-readiness checks. |
| `dynamic-instrument-controller-agent` | Adds measurement devices and PID-style controllers for dynamic simulations. |

### 2.9 Piping, mechanical and vibration

| Agent | What it does |
|-------|--------------|
| `piping-integrity-agent` | Line velocity, pressure drop, wall thickness, and flow-induced vibration screening. |
| `piping-mechanical-agent` | Hoop and thermal-flexibility margins plus acoustic-induced vibration likelihood. |
| `noise-assessment-agent` | Assesses gas-valve and restriction noise from measurements or process data, routes detailed prediction to IEC 60534-8-3, and keeps workplace-noise and AIV decisions separate. |

### 2.10 Process safety

| Agent | What it does |
|-------|--------------|
| `process-safety-agent` | Fire-case relief loads, emergency depressurization, vacuum collapse, flare radiation, PSV orifice, and safety-function coverage screening. |

### 2.11 Utilities

| Agent | What it does |
|-------|--------------|
| `utilities-screening-agent` | Instrument air, fuel-gas Wobbe, and cooling-water balance screening. |

### 2.12 Energy, emissions and economics

| Agent | What it does |
|-------|--------------|
| `energy-emissions-agent` | Preliminary energy-use and CO2-equivalent emissions screening for a facility or process. |
| `emissions-abatement-screening-agent` *(coordinator)* | Ranks emission-reduction measures — power-from-shore, waste-heat recovery, flaring reduction — using the public Norwegian carbon-cost basis (CO2 tax, EU ETS, NOx Fund) and NPV screening. |
| `asset-economics-agent` *(coordinator)* | Chains a CAPEX/OPEX cost picture, a field-life energy and emissions roll-up, and a discounted NPV into one concept-economics view with carbon intensity and CO2-tax exposure. |
| `concept-selection-agent` | Chains resource classification, CAPEX/OPEX, NPV, energy/emissions, and step-out screening into a comparable concept summary. |
| `field-development-economics-agent` *(coordinator)* | End-to-end reservoir-to-market screening: reservoir fluid and depletion, subsea hydrate margins, topside separation duty, gas-export line, and an asset-economics roll-up. |

### 2.13 Numerical coupling (CFD and FEM)

| Agent | What it does |
|-------|--------------|
| `cfd-coupling-agent` | Runs single-phase and multiphase CFD from governed inputs, qualifies existing CFD, and assesses aeroacoustic readiness. Tonal-noise cases **fail closed** unless the required evidence exists; steady RANS is never used as tonal-source diagnosis. |
| `fem-coupling-agent` | Finite-element models of the solid — layered heat conduction, transient cooldown, porous-medium diffusion, thermal stress — converted into the effective U-value, hot-spot factor, no-touch time, and wall stress a one-dimensional model consumes. Can also qualify an existing FEM report instead of running a new model. |

### 2.14 Documents and evidence

| Agent | What it does |
|-------|--------------|
| `technical-document-intelligence-agent` | Classifies mixed engineering documents and images and produces source-traceable evidence packages before analysis. |

---

## 3. Workflows

Individual agents answer one question. The workflows below are the recurring
chains — each one is declared in the coordinators' `coordinated_agents` lists and
rendered in the [Orchestration Map](ORCHESTRATION_MAP.md).

### 3.1 The standard screening workflow

Every agent, coordinator or specialist, runs the same loop:

```text
1. Frame          state the question, the decision it supports, and the scope
2. Collect        list required inputs; report what is missing rather than inventing it
3. Screen         run the public screening method from the required skills
4. Qualify        record assumptions, limitations, and validity range
5. Recommend      name the validated NeqSim study that must follow
6. Review         hand to a qualified human — always required
```

Step 2 is the one that makes the output trustworthy: a community agent that
lacks an input says so instead of guessing.

### 3.2 Concept-to-economics chain

The main field-development workflow, from subsurface to an investment view:

```text
reservoir-simulator-agent          build a screening reservoir model
        │
        ▼
reservoir-forecasting-agent        decline fit → production profile, EUR
        │
        ▼
reservoir-to-facility-screening-agent   depletion → inflow → routing → arrival pressure
        │
        ▼
concept-selection-agent            comparable concept summary
        │
        ▼
asset-economics-agent              CAPEX/OPEX + energy/emissions + NPV
```

`field-development-economics-agent` runs this whole value chain as a single
request when you want the reservoir-to-market picture in one pass, delegating to
`asset-economics-agent` and `reservoir-to-facility-screening-agent`.

`resource-classification-agent` sits alongside the chain: it keeps the maturity
class (RC0–RC9 / SPE-PRMS) honest so a screening number is never reported at a
maturity the evidence does not support.

### 3.3 Flow-assurance study workflow

`flow-assurance-study-agent` is the coordinator with the widest delegation set.
It exists to make a study *reviewable*: the basis is frozen first, then the
specialists are called, then results are gated like-for-like.

```text
flow-assurance-study-agent
    ├── technical-document-intelligence-agent   evidence package from documents
    ├── pvt-agent                               fluid basis
    ├── pipe-route-screening-agent              route profile, dP, velocity, hydrate margin
    ├── flow-assurance-engineer-agent           hydrate and wax margins
    ├── olga-simulation-agent                   transient multiphase behaviour
    ├── subsea-cooldown-agent                   no-touch time
    ├── piping-integrity-agent                  velocity, dP, wall thickness, FIV
    └── sand-erosion-agent                      erosional velocity, wall life
```

### 3.4 Subsea layout and SURF design workflow

```text
subsea-layout-screening-agent   map → well and tie-back inventory, step-outs
        │
        ▼
surf-layout-design-agent        host placement, flowline/riser/umbilical routing and sizing
        │
        ├── pipe-route-screening-agent        route profiles and hydraulics
        ├── flow-assurance-engineer-agent     margins along the route
        └── asset-economics-agent             cost and value of the layout
```

`pipeline-survey-profile-agent` feeds the same chain from the other direction
when as-built survey data exists: it cleans the survey into an elevation profile
that route screening and flow assurance can consume.

### 3.5 Emissions abatement workflow

```text
emissions-abatement-screening-agent
    ├── energy-emissions-agent          field-life energy and emissions
    ├── ncs-production-analysis-agent   public production basis
    ├── concept-selection-agent         comparable alternatives
    └── asset-economics-agent           NPV of each abatement measure
```

The output is a ranked list of measures (power-from-shore, waste-heat recovery,
flaring reduction) with their cost and carbon consequences, not a single number.

### 3.6 Numerical escalation workflow

Screening correlations have a validity range. When the geometry or the physics
leaves that range, the coupling agents take over:

```text
flow-assurance-engineer-agent / subsea-cooldown-agent / piping-mechanical-agent
        │  correlation no longer defensible
        ▼
fem-coupling-agent      solid-side FEM → U-value, hot-spot factor, no-touch time, wall stress
cfd-coupling-agent      CFD → flow field, aeroacoustic readiness
        │
        ▼
back into the one-dimensional NeqSim model as qualified inputs
```

Both coupling agents can also be used in *qualification mode* — reviewing an
existing CFD or FEM report rather than running a new model.

### 3.7 Document-to-screening workflow

```text
technical-document-intelligence-agent   classify documents and images,
                                        build a source-traceable evidence package
        │
        ▼
discipline agent (pvt / process / flow assurance / …)   screen using traced inputs
```

### 3.8 Dynamic simulation workflow

```text
dynamic-process-preparation-agent      make the flowsheet dynamics-ready
        │                              (volumes, mechanical design, readiness checks)
        ▼
dynamic-instrument-controller-agent    add transmitters and PID controllers
        │
        ▼
compressor-antisurge-agent             anti-surge recycle control and speed runback
```

---

## 4. Relationship to the other NeqSim agent repositories

| Repository | Role |
|------------|------|
| [equinor/neqsim](https://github.com/equinor/neqsim) | The simulation engine plus the core agents that drive it directly (`@process.model`, `@thermo.fluid`, `@solve.task`, …). See `docs/integration/agents_and_workflows_overview.md` there. |
| **neqsim-community-agents** (this repository) | Public screening agents built on public, educational methods. |
| [equinor/neqsim-enterprise-agents](https://github.com/equinor/neqsim-enterprise-agents) | Private, governed agents that add company data sources and company policy on top of these community methods. |

Enterprise agents deliberately reuse community methods rather than
re-implementing them: an enterprise hydrate-margin agent applies a company
acceptance policy on top of the community hydrate-margin screening. That is why
community agents must stay plant-agnostic and public-data only.

---

## 5. Related documentation

- [Installation Guide](installation-guide.md) — install the `neqsim` CLI and these agents into VS Code
- [Agent Standard](agent-standard.md) — what every agent must contain
- [Repository Structure](repository-structure.md) — how agents are organized on disk
- [Orchestration Map](ORCHESTRATION_MAP.md) — generated delegation graph
- [Agent Skill Map](AGENT_SKILL_MAP.md) — generated agent→skill dependencies
- [Governance](governance.md) — ownership, versioning, deprecation
- [Safety Guidelines](safety-guidelines.md) — limits on agent use
- [Contribution Guide](contribution-guide.md) — adding a new agent
