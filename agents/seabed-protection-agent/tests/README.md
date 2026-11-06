# Seabed Protection Agent Tests

This folder documents how the Seabed Protection Agent is validated in the community repository.

Structure validation is provided by the repository-level test suite:

```bash
python -m unittest discover -s tests
```

The repository tests confirm that this agent has:

- the required files (`AGENT.md`, `agent.yaml`, `README.md`, `examples`, `prompts`, `tests`)
- the required AGENT.md sections and front matter
- the required `agent.yaml` metadata keys, including `human_review_required: true`
- the declared required skills (`seabed-protection-screening`, `pipeline-survey-processing`, `surf-cooldown-screening`, `hydrate-margin-check`)
- human review language in `AGENT.md` and `README.md`

The underlying screening logic is validated by the skill tests in the
`neqsim-community-skills` repository under
`skills/subsea/neqsim-seabed-protection-screening/tests`,
`skills/subsea/neqsim-pipeline-survey-processing/tests`,
`skills/flow-assurance/neqsim-surf-cooldown-screening/tests` and
`skills/flow-assurance/neqsim-hydrate-margin-check/tests`.
