# Subsea Equipment Placement Agent Tests

Structure validation is provided by the repository-level test suite:

```bash
python -m unittest discover -s tests
python scripts/validate_agent_manifests.py
```

The repository tests confirm the required files, front matter, `agent.yaml` keys (including `human_review_required: true`), the declared required skills and the human-review language.

The placement logic is validated by the skill tests in `neqsim-community-skills` under `skills/subsea/neqsim-subsea-equipment-placement/tests`.
