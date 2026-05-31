# Contributing To NeqSim Community Agents

Thank you for helping build a public ecosystem of transparent, reproducible engineering agents for NeqSim.

Contributions may include new agents, improved documentation, examples, prompt templates, tests, metadata corrections, safety guidance, or governance improvements.

All contributions must be suitable for a public open-source repository.

## Create An Agent

1. Choose a clear engineering purpose and a bounded scope.
2. Copy [templates/agent-template](templates/agent-template/) to `agents/<agent-name>/`.
3. Update `AGENT.md` with the required sections from [docs/agent-standard.md](docs/agent-standard.md).
4. Update `agent.yaml` with machine-readable metadata.
5. Add at least one realistic public example in `examples/`.
6. Add at least one reusable example prompt in `prompts/`.
7. Add tests or validation notes in `tests/`.
8. Run the repository tests before opening a pull request.

Agent names should be lowercase, descriptive, and hyphen-separated, for example `hydrate-screening-agent`.

## Required Files

Each agent directory must contain:

```text
agent-name/
├── AGENT.md
├── agent.yaml
├── examples/
├── prompts/
├── tests/
└── README.md
```

`AGENT.md` must include front matter with `name`, `description`, `version`, and `required_skills`.

`agent.yaml` must define `name`, `description`, `required_skills`, `supported_domains`, `inputs`, `outputs`, and `human_review_required`.

## Documentation Requirements

Agent documentation must:

- State the purpose and when to use the agent
- List required inputs and expected outputs
- Describe the workflow step by step
- Identify required community skills
- Document assumptions and limitations
- Include validation checks
- Explain where human review is required
- Avoid proprietary information
- Use realistic public examples

Agents must never claim to replace engineering judgement.

## Testing Requirements

Every contribution should include tests or validation material appropriate to the change.

Minimum expectations for new agents:

- The repository structure tests pass
- Required metadata fields are present
- Required AGENT.md sections are present
- Example prompts are included
- Example outputs or reports are reproducible from public inputs
- Assumptions, limitations, and human review requirements are documented

Run the current tests with:

```powershell
python -m unittest discover -s tests
```

## Review Checklist

Before submitting a pull request, confirm that:

- The agent has a clear engineering purpose
- The scope is bounded and suitable for screening or assistance
- Required skills are listed and already public or proposed publicly
- Inputs and outputs are documented
- Assumptions and limitations are explicit
- Human review is required for engineering decisions
- Examples use public, synthetic, or educational data only
- No proprietary data, credentials, personal data, or confidential procedures are included
- Tests and validation notes are updated
- Documentation links are valid

## Open-Source Requirements

Contributions must be compatible with the Apache License 2.0 and public distribution.

Do not contribute:

- Confidential field data or production data
- Proprietary design methods
- Vendor-confidential material
- Restricted standards text
- Credentials, tokens, cookies, or secrets
- Personal data
- Content that cannot be redistributed under the repository license

If a workflow depends on non-public methods or data, document a public placeholder and explain what qualified users must supply in their own environment.

## Human Review

All agents in this repository are engineering assistants. They can help organize work, identify checks, generate examples, and explain assumptions. Engineering conclusions, design decisions, operational actions, and safety-related decisions require qualified human review.