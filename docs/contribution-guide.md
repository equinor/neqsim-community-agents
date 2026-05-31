# Contribution Guide

This guide expands the repository contribution process for new agents and documentation updates.

## Before You Start

Confirm that your contribution is:

- Public and open-source suitable
- Compatible with the Apache License 2.0
- Free of proprietary data, credentials, personal data, and confidential methods
- Focused on assisting engineers
- Clear about human review requirements

## New Agent Checklist

1. Create `agents/<agent-name>/` from [templates/agent-template](../templates/agent-template/).
2. Update `AGENT.md` front matter and required sections.
3. Update `agent.yaml` metadata.
4. Add public examples under `examples/`.
5. Add reusable prompts under `prompts/`.
6. Add tests or validation notes under `tests/`.
7. Update [community-agents.yaml](../community-agents.yaml) if the agent should appear in the catalog preview.
8. Run tests.
9. Open a pull request with the review checklist completed.

## Documentation Quality

Good agent documentation is specific and bounded. It should explain what the agent can assist with, what inputs it needs, what outputs it produces, what skills it uses, and what it cannot do.

Avoid broad claims such as "optimizes production" or "ensures safe operation" unless the actual workflow and validation support that scope. Prefer precise statements such as "screens public example conditions for hydrate risk indicators and recommends follow-up review."

## Testing Guidance

At minimum, run:

```powershell
python -m unittest discover -s tests
```

Additional tests can be added for mature agents. Examples include:

- Metadata schema checks
- Example output checks
- Prompt coverage checks
- Generated report structure checks
- NeqSim script smoke tests
- Skill traceability checks

## Pull Request Review

Pull requests should explain:

- What changed
- Why the change is useful
- Which agents or docs are affected
- Which skills are required
- What tests were run
- What human review is required for outputs

Reviewers should check technical scope, open-source suitability, documentation clarity, safety wording, metadata consistency, and test coverage.