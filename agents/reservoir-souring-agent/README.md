# Reservoir Souring Agent

Coordinates screening of reservoir souring from measured separator-gas H2S: gas-to-wellstream H2S conversion with NeqSim, seawater fraction from tracers, automatically updated per-well H2S-versus-seawater-fraction correlations, and a mixing-zone plausibility bound.

This agent supports screening and orientation only. It **does not replace** reservoir simulation, microbiological study, materials selection or qualified engineering review. **Human review** is always required.

## Required Skills

- `neqsim-h2s-phase-partitioning`
- `neqsim-reservoir-souring-correlation`
- `neqsim-production-chemistry`

## Layout

- `AGENT.md` - agent definition
- `agent.yaml` - manifest
- `examples/` - walkthrough checklist
- `prompts/` - example prompts
- `tests/` - test notes
