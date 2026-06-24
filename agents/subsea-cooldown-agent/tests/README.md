# Subsea Cooldown Agent Tests

This agent is validated by the repository structure tests in
[tests/test_repository_structure.py](../../../tests/test_repository_structure.py).

Those tests confirm:

- The required agent files exist (AGENT.md, agent.yaml, README.md, examples, prompts, tests).
- AGENT.md contains all required sections and the correct required-skills frontmatter.
- agent.yaml contains all required keys, the required skill, and `human_review_required: true`.
- The agent declares its required community skill `surf-cooldown-screening`.
- The AGENT.md and README.md together include human-review and "does not replace" language.

## Manual Validation Notes

- The no-touch-time indicator is an educational placeholder.
- Example data is public and synthetic.
- The agent recommends validated NeqSim cooldown and hydrate workflows for real work.
- Qualified human review is required before any design or operating decision.

## Run the Tests

```bash
python -m unittest discover -s tests -v
```
