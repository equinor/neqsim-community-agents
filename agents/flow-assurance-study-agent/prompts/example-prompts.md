# Example Prompts

## Coordinate a Full Study

```text
Use the Flow Assurance Study Agent to coordinate a public synthetic DG2 tieback
study. Reuse existing specialist agents, freeze the basis, define a scenario
matrix, run NeqSim TwoFluidPipe steady cases, escalate transient cases to OLGA,
and return a source-traceable review package. Do not invent missing inputs.
```

## Audit an Existing Comparison

```text
Audit an existing NeqSim/OLGA comparison through the Flow Assurance Study Agent.
Check fluid and source phase split, geometry, heat transfer, mesh, boundary
conditions, output definitions, units, convergence, and rate sensitivity before
accepting any explanation for the discrepancy.
```

## Plan Only

```text
Create only the evidence, scenario, agent-handoff, and validation plan for a
flow-assurance study. Do not run calculations. Route each bounded question to an
existing community agent and identify the required human reviewers.
```
