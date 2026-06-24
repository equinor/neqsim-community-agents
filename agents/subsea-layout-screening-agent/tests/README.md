# Subsea Layout Screening Agent Tests

This folder documents how the Subsea Layout Screening Agent is validated in the community repository.

Structure validation is provided by the repository-level test suite:

```bash
python -m unittest discover -s tests
```

The repository tests confirm that this agent has:

- the required files (`AGENT.md`, `agent.yaml`, `README.md`, `examples`, `prompts`, `tests`)
- the required AGENT.md sections and front matter
- the required `agent.yaml` metadata keys, including `human_review_required: true`
- the declared required skills (`field-layout-import`, `subsea-layout-geometry`, `bathymetry-profile-screening`, `pipe-route-profile`)
- human review language in `AGENT.md` and `README.md`

The underlying screening logic is validated by the skill tests in the
`neqsim-community-skills` repository under
`skills/subsea/field-layout-import/tests`,
`skills/subsea/subsea-layout-geometry/tests`,
`skills/subsea/bathymetry-profile-screening/tests`, and
`skills/subsea/pipe-route-profile/tests`.
