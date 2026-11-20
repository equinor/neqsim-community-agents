# Flare-Helideck Dispersion Agent Tests

This folder documents how the Flare-Helideck Dispersion Agent is validated in the community repository.

Structure validation is provided by the repository-level tests:

```bash
python -m unittest discover -s tests
```

The repository tests confirm that this agent has:

- the required files (`AGENT.md`, `agent.yaml`, `README.md`, `examples`, `prompts`, `tests`)
- the required AGENT.md sections and front matter
- the required `agent.yaml` metadata keys, including `human_review_required: true`
- the declared required skills, resolved against the skills index
- coordinated agents that exist in the catalog
- human review language in `AGENT.md` and `README.md`

The repository-level test `tests/test_flare_helideck_dispersion_agent.py` checks the guardrails (conditional wording, no annual frequency without a flame-out frequency, flight paths as assumptions, tip-inclination sensitivity, human review of unverified data, the independent review checklist, the workflow order) and that no vendor, company or site identifiers are present.

The underlying calculations are validated by the skill tests in the `neqsim-community-skills` repository under `skills/safety/neqsim-flare-helideck-dispersion/tests`.
