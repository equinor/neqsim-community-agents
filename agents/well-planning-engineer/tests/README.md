# Tests

The agent package is covered by `tests/test_repository_structure.py` (required files, sections, metadata alignment, catalog agreement, human-review language) and `tests/test_agent_manifest_schema.py` (manifest schema, coordinated agents, hand-offs, Python runtime policy) in the repository `tests` folder.

The calculation tests live with the skill: `skills/subsurface/neqsim-integrated-well-planning/tests` (basis and registers, envelope, ledger, hand-off schemas, chart and drawing rendering, NeqSim-backed chain tests that skip with an explicit reason when the wellplanning classes are not available).
