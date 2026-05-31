# Repository Structure

NeqSim Community Agents is organized to keep each agent self-contained while sharing common documentation, governance, templates, and tests.

## Top-Level Layout

```text
neqsim-community-agents/
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── community-agents.yaml
├── agents/
├── templates/
├── docs/
└── tests/
```

## Agent Organization

Each agent lives under `agents/<agent-name>/` and must contain:

```text
agent-name/
├── AGENT.md
├── agent.yaml
├── examples/
├── prompts/
├── tests/
└── README.md
```

`AGENT.md` is the primary human-readable specification. `agent.yaml` is machine-readable metadata for cataloging and future installation workflows. `README.md` explains the agent for contributors and users.

## Domains

Agents may support one or more domains, including:

- PVT and thermodynamics
- Flow assurance
- Process engineering
- Field development
- Energy systems
- Sustainability
- Operations support
- Educational workflows

Supported domains must be listed in `agent.yaml`.

## Required Files

Agent directories require:

- `AGENT.md` for specification and review
- `agent.yaml` for metadata
- `examples/` for public examples
- `prompts/` for reusable prompt examples
- `tests/` for validation notes or automated tests
- `README.md` for local agent overview

Empty directories should contain a short `README.md` so the structure is visible in git.

## Examples

Examples must use public, synthetic, or educational data. They should include expected inputs, expected agent actions, expected outputs, assumptions, limitations, and human review requirements.

Examples must not include proprietary field data, confidential process data, credentials, personal data, or restricted standards text.

## Relationship To Skills

NeqSim Community Skills provide reusable focused capabilities. Agents combine skills into complete engineering workflows.

For example, a tie-in screening agent can combine:

- `fluid-quality-check` for composition review
- `hydrate-screening` for hydrate risk triage
- `separator-modelling` for separator screening considerations

Agents should reference skill names in both `AGENT.md` and `agent.yaml`. When available, include catalog mappings to the corresponding `neqsim-*` skill IDs.