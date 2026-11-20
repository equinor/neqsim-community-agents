# Tests - Reservoir Souring Agent

The agent is a documentation and workflow definition. It is covered by the repository-level manifest and structure tests (`tests/test_agent_manifest_schema.py`, `tests/test_repository_structure.py`) and `scripts/validate_agent_manifests.py`. The numerical behaviour is tested in the skills it references:

- `neqsim-h2s-phase-partitioning` (`tests/test_h2s_partitioning.py`)
- `neqsim-reservoir-souring-correlation` (`tests/test_reservoir_souring.py`)
