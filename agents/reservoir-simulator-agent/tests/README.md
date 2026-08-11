# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skills.

## How to exercise the agent

1. Run the underlying skill tests (from inside each skill folder):

   ```bash
   cd ../../neqsim-community-skills/skills/field-development/reservoir-model-builder
   python -m pytest        # volumetrics, provenance ladder, refinement, NeqSim spec

   cd ../norwegian-continental-shelf-data
   python -m pytest

   cd ../reservoir-depletion-screening
   python -m pytest

   cd ../resource-classification-screening
   python -m pytest

   cd ../../pvt/fluid-quality-check
   python -m pytest
   ```

2. Run the staged worked example and confirm the provenance audit trail and the
   NeqSim specification are produced:

   ```bash
   cd ../../neqsim-community-skills/skills/field-development/reservoir-model-builder
   python examples/build_wisting_style_model.py
   ```

3. Walk through `examples/staged-reservoir-model-checklist.md` with the example
   prompts in `prompts/example-prompts.md`.

## Acceptance checks

- The agent states the sizing basis (geometry, in-place volume, or a
  back-calculated recoverable volume).
- Every parameter it reports carries a provenance label, and public figures keep
  their source and reference year.
- The agent reports the data tier and the completeness score, and reports them
  again after each refinement.
- Earlier data sources keep their original provenance when a later batch is
  applied.
- The agent reconciles a geometry-derived in-place volume against any reported
  recoverable volume, or explains the divergence.
- The agent declares deliverability unconstrained rather than inventing a
  productivity index when neither a PI nor a permeability is available.
- The agent states the volume basis, the separate aquifer volume and the
  quadratic production-index unit when handing over to NeqSim.
- The agent always recommends validated NeqSim follow-up (`SimpleReservoir` /
  `WellFlow` / `runReservoir`, `PipeBeggsAndBrills` / `runPipeline`,
  field economics / `runFieldEconomics`).
- The agent flags screening limitations (no grid, no relative permeability, no
  history matching, no reserves statement).
- The agent requires qualified human review (`human_review_required: true`).
