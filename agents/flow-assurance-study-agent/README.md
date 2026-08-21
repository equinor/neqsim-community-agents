# Flow Assurance Study Agent

Thin coordinator for reviewable flow-assurance studies. It freezes the basis,
routes bounded work to existing community specialist agents, and reconciles
NeqSim and OLGA evidence without duplicating their methods.

## What it does

- Builds an evidence register and scenario matrix.
- Uses NeqSim `TwoFluidPipe` plus OLGA for multiphase pipelines.
- Limits `PipeBeggsAndBrills` to topside piping or simple backup screening.
- Coordinates existing hydrate, cooldown, integrity, vibration, and erosion agents.
- Enforces convergence, input-equivalence, provenance, uncertainty, and approval gates.

## What it does not do

It has no calculation skill of its own and does not replace any specialist agent,
simulator, project acceptance criterion, or qualified engineering judgement.

## Package contents

- [AGENT.md](AGENT.md): complete coordinator contract.
- [agent.yaml](agent.yaml): machine-readable composition metadata.
- [examples/](examples/): a public synthetic DG2 workflow example.
- [prompts/](prompts/): reusable invocation prompts.
- [tests/](tests/): package validation notes.

## Human review

All outputs require human review by qualified flow-assurance and affected
discipline engineers before design or operational use. This agent does not
replace formal project assurance.
