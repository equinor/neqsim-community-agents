# Continuous Task Improvement Agent

Public agent that keeps a NeqSim engineering task improving after its first
report: living-task scaffold, confirmed goal, backtested monitoring, scheduled or
on-demand cycles, solve-until-goal or until-converged, triage and ledger.

## Status

Draft (version 0.1.0). Runs without enterprise access; human review required.

## What it does

- Makes an existing task living without changing any of its files.
- Turns a Word or Markdown brief into `goal.yaml` for a person to confirm.
- Proves the monitoring on archived data before it runs unattended.
- Runs cycles on a laptop on demand or on a server on a schedule.
- Stops a solve loop on goal met, infeasible, blocked, budget or convergence,
  and reopens it on regression or new evidence.

## Try it

```bash
neqsim task-reference-case C:/tmp/living
neqsim task-backtest C:/tmp/living/reference_compressor_station --start 2025-10-02 --end 2026-09-30
neqsim task-solve C:/tmp/living/reference_compressor_station --no-agent
```
