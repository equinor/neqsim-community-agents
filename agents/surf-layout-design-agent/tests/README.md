# SURF Layout Design Agent Tests

This folder documents how the SURF Layout Design Agent is validated in the community repository.

Structure validation is provided by the repository-level test suite:

```bash
python -m unittest discover -s tests
python scripts/validate_agent_manifests.py
```

The repository tests confirm that this agent has:

- the required files (`AGENT.md`, `agent.yaml`, `README.md`, `examples`, `prompts`, `tests`)
- the required AGENT.md sections and front matter
- the required `agent.yaml` metadata keys, including `human_review_required: true`
- the declared required skills (`surf-field-layout-design`, `subsea-layout-geometry`, `pipe-route-profile`, `bathymetry-profile-screening`, `line-velocity-check`)
- human review language in `AGENT.md` and `README.md`

The underlying design logic is validated by the skill tests in the
`neqsim-community-skills` repository under
`skills/subsea/surf-field-layout-design/tests`,
`skills/subsea/subsea-layout-geometry/tests`,
`skills/subsea/pipe-route-profile/tests`,
`skills/subsea/bathymetry-profile-screening/tests`, and
`skills/process/line-velocity-check/tests`.
