# Pipeline Survey Profile Agent Tests

This folder documents how the Pipeline Survey Profile Agent is validated in the community repository.

Structure validation is provided by the repository-level test suite:

```bash
python -m unittest discover -s tests
```

The repository tests confirm that this agent has:

- the required files (`AGENT.md`, `agent.yaml`, `README.md`, `examples`, `prompts`, `tests`)
- the required AGENT.md sections and front matter
- the required `agent.yaml` metadata keys, including `human_review_required: true`
- the declared required skills (`pipeline-survey-processing`, `bathymetry-profile-screening`, `pressure-drop-screening`, `line-velocity-check`)
- human review language in `AGENT.md` and `README.md`

The underlying screening logic is validated by the skill tests in the
`neqsim-community-skills` repository under
`skills/subsea/pipeline-survey-processing/tests`,
`skills/subsea/bathymetry-profile-screening/tests`,
`skills/process/pressure-drop-screening/tests`, and
`skills/process/line-velocity-check/tests`.
