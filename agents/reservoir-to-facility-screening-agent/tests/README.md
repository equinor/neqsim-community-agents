# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skills.

## How to exercise the agent

1. Run the underlying skill tests (from inside each skill folder):

   ```bash
   cd ../../neqsim-community-skills/skills/field-development/reservoir-depletion-screening
   python -m pytest

   cd ../../subsea/production-network-routing
   python -m pytest

   cd ../subsea-layout-geometry
   python -m pytest

   cd ../step-out-screening
   python -m pytest
   ```

2. Walk through `examples/reservoir-to-facility-screening-checklist.md` with the
   example prompts in `prompts/example-prompts.md`.

3. Confirm the agent output keeps facts, assumptions, and recommendations
   separate, names the validated NeqSim path (`SimpleReservoir` / `runTransient`,
   `PipeBeggsAndBrills`, MCP `runReservoir` / `runPipeline` /
   `runFlowAssurance`), and states that qualified human review is required.

## Acceptance checks

- The agent always recommends validated NeqSim follow-up.
- The agent flags reservoir-depletion and network-routing limitations.
- The agent requires qualified human review (`human_review_required: true`).
