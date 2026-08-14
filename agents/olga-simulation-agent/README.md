# OLGA Simulation Agent

Runs the OLGA transient multiphase flow simulator (SLB) end to end: discover the
installed engine, rule-check the case, execute it in batch, decode the exit
status, and read the `.tpl` trend and `.ppl` profile results with their declared
units.

OLGA is licensed commercial software. This agent drives an installation the user
already has. It bundles no OLGA code, documentation or data, and it never handles
licence credentials.

The agent **executes and post-processes**; it does not author flow-assurance
models, invent PVT tables or pipeline geometry, or replace a qualified
flow-assurance review. A **human review** is always required.

## Required Skills

- `neqsim-olga-multiphase-simulator`

Loaded as context when the task calls for them:

- `neqsim-multiphase-flow-slug-screening`
- `neqsim-two-phase-flow-regime-screening`
- `neqsim-hydrate-margin-check`
- `neqsim-surf-cooldown-screening`
- `neqsim-pipe-route-profile`

## When OLGA, when screening

| Question | Route |
| --- | --- |
| Liquid surge on ramp-up, terrain slugging, shut-in/restart, blowdown dynamics | OLGA — this agent |
| Steady-state pressure drop, holdup, flow regime, erosional velocity | screening skills / `flow-assurance-engineer-agent` |
| Phase envelope, hydrate curve, wax appearance temperature | `pvt-agent` and NeqSim thermodynamics |
| Topside response to an arriving slug | NeqSim `ProcessSystem` fed by OLGA arrival trends |

Screen first. Escalate to OLGA only when the transient actually decides the
answer — a licence checkout and a multi-hour solve are not free.

## Non-negotiables

- Rule-check (`-exitRC`) before every long run.
- Run with the working directory set to the case directory, so relative
  `FILES PVTFILE=./x.tab` references resolve.
- Never point the runner at an `OLGA-S` path — that is the steady-state point
  model, not the transient simulator.
- Gate on exit code 0 **and** `NORMAL STOP IN EXECUTION` in the `.out` file.
- Report the engine version and the command line with every number.
- Read units from the result catalog; never assume them.

## Layout

- `AGENT.md` — agent definition and workflow.
- `agent.yaml` — machine-readable manifest.
- `prompts/example-prompts.md` — example prompts.
- `tests/README.md` — how to exercise the agent through its skill.

See `AGENT.md` for the full workflow, assumptions and limitations.
