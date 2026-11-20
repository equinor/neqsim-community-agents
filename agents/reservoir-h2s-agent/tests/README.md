# Tests - Reservoir H2S Agent

The agent is a documentation and workflow definition. It is covered by the repository-level manifest and structure tests (`tests/test_agent_manifest_schema.py`, `tests/test_repository_structure.py`) and `scripts/validate_agent_manifests.py`. The calculation is tested in the skill and in NeqSim:

- `neqsim-reservoir-h2s-estimation` (`tests/test_reservoir_h2s.py`)
- NeqSim Java: `ReservoirH2SEstimatorTest`, `MineralH2SBuffersTest`
