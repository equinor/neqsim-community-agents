# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skills.

## How to exercise the agent

1. Run the underlying skill tests (from inside each skill folder):

   ```bash
   cd ../../neqsim-community-skills/skills/field-development/norwegian-continental-shelf-data
   python -m pytest

   cd ../reservoir-depletion-screening
   python -m pytest

   cd ../asset-value-npv-screening
   python -m pytest

   cd ../../field-development/economy-basis-screening   # supporting economics
   python -m pytest
   ```

2. Walk through `examples/ncs-production-analysis-checklist.md` with the example
   prompts in `prompts/example-prompts.md`.

3. Confirm the agent output keeps facts, assumptions, and recommendations
   separate, keeps every reused figure with its source and reference year, names
   the validated NeqSim path (`SimpleReservoir` / `runReservoir`,
   `PipeBeggsAndBrills` / `runPipeline`, field-economics / `runFieldEconomics`),
   and states that qualified human review is required.

## Acceptance checks

- The agent always recommends validated NeqSim follow-up.
- The agent keeps source attribution and reference year with reused figures.
- The agent flags reference-data snapshot and screening limitations.
- The agent requires qualified human review (`human_review_required: true`).
