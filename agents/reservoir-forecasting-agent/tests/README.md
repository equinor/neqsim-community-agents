# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skills.

## How to exercise the agent

1. Run the underlying skill tests (from inside each skill folder):

   ```bash
   cd ../../neqsim-community-skills/skills/field-development/norwegian-continental-shelf-data
   python -m pytest        # includes the Arps decline fit and forecast

   cd ../reservoir-depletion-screening
   python -m pytest

   cd ../resource-classification-screening
   python -m pytest
   ```

2. Walk through `examples/reservoir-forecasting-checklist.md` with the example
   prompts in `prompts/example-prompts.md`.

3. Confirm the agent output keeps facts, assumptions, and recommendations
   separate, keeps every reused figure with its source and reference year,
   reconciles the decline forecast against the reservoir-depletion screening,
   names the validated NeqSim path (`SimpleReservoir` / `runReservoir`,
   `PipeBeggsAndBrills` / `runPipeline`, field-economics / `runFieldEconomics`),
   and states that qualified human review is required.

## Acceptance checks

- The agent always recommends validated NeqSim follow-up.
- The agent keeps source attribution and reference year with reused figures.
- The agent reports the decline model, decline rate, and R-squared.
- The agent reports the forward profile, remaining volume, years-to-limit, and EUR.
- The agent reconciles the decline forecast with the reservoir-depletion screening.
- The agent flags decline-curve screening limitations (no material balance / simulation).
- The agent requires qualified human review (`human_review_required: true`).
