# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skills.

## How to exercise the agent

1. Run the underlying skill tests (from inside each skill folder):

   ```bash
   cd ../../neqsim-community-skills/skills/environment/energy-emissions-screening
   python -m pytest

   cd ../../field-development/norwegian-continental-shelf-data
   python -m pytest        # includes the carbon-cost basis and abatement screening

   cd ../asset-value-npv-screening
   python -m pytest
   ```

2. Walk through `examples/emissions-abatement-checklist.md` with the example
   prompts in `prompts/example-prompts.md`.

3. Confirm the agent output keeps facts, assumptions, and recommendations
   separate, keeps every reused carbon-cost and emissions figure with its source
   and reference year, names the validated NeqSim path (`GasTurbine` /
   combined-cycle / `runProcess`, `PinchAnalysis`, field-economics /
   `runFieldEconomics`), and states that qualified human review is required.

## Acceptance checks

- The agent always recommends validated NeqSim follow-up.
- The agent keeps source attribution and reference year with reused figures.
- The agent states the gas combustion factor and any derived CO2 avoided.
- The agent reports per-measure NPV, payback, and breakeven CO2 price.
- The agent flags screening limitations (no validated energy model, no MACC curve).
- The agent requires qualified human review (`human_review_required: true`).
