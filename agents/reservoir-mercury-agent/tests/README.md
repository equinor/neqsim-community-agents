# Tests - Reservoir Mercury Agent

The agent is a documentation and workflow definition. It is covered by the repository-level manifest and structure tests (`tests/test_agent_manifest_schema.py`, `tests/test_repository_structure.py`) and `scripts/validate_agent_manifests.py`. The numerical behaviour is tested in the skill it references:

- `neqsim-reservoir-mercury-estimation` (`tests/test_reservoir_mercury.py`)
- NeqSim Java: `ReservoirMercuryEstimatorTest`, `MineralMercuryBuffersTest`
