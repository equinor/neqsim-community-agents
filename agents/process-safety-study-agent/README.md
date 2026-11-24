# Process Safety Study Agent

Vendor-neutral coordinator for a full process safety study of a tie-in, modification or new facility. It freezes the scope and the evidence basis, routes each step to the specialist agent or skill, runs the evidence gates and keeps every result at its evidence status.

## What it does

- Builds the step plan S00 to S14 from `neqsim-process-safety-study` with the skill, agent, evidence and gate per step.
- Turns unread documents and unverified data into data gaps, never into passes.
- Checks carried profiles against their source, release numbers against hand calculations, screening against transient results, drawing items against P&ID tags, and quantities used twice against each other.
- Coordinates `process-safety-agent`, `cfd-coupling-agent`, `olga-simulation-agent`, `flare-helideck-dispersion-agent`, `firewater-coverage-agent`, `flow-assurance-study-agent`, `technical-document-intelligence-agent` and `subsea-layout-screening-agent`.

## What it does not do

It has no calculation of its own, does not replace a facilitated HAZID or HAZOP, a QRA, a SIL verification by qualified staff or project assurance, and holds no company document access. An enterprise overlay agent can extend it with company systems.

## Package contents

- [AGENT.md](AGENT.md): coordinator contract and workflow.
- [agent.yaml](agent.yaml): machine-readable composition metadata.
- [examples/](examples/): a public synthetic study plan.
- [prompts/](prompts/): reusable invocation prompts.
- [tests/](tests/): validation notes.

## Human review

All outputs require human review by qualified process safety engineers and the affected disciplines. This agent does not replace formal safety assurance or authority approval.
