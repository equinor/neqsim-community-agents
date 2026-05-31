# NeqSim Community Agents

NeqSim Community Agents is the public open-source repository for community-developed AI agents built on [NeqSim](https://github.com/equinor/neqsim) and [NeqSim Community Skills](https://github.com/equinor/neqsim-community-skills).

The repository provides reusable, transparent, and reproducible engineering agents for process engineering, thermodynamics, flow assurance, field development, energy systems, and sustainability applications.

**Energy for people. Progress for society.**

## What This Repository Contains

Agents in this repository combine:

- NeqSim calculations
- Community skills
- Engineering workflows
- Documentation
- Examples
- Tests
- Human review and validation

The goal is to create a shared ecosystem of engineering-focused agents that assist engineers, researchers, students, and industry professionals while keeping assumptions, inputs, limitations, and validation steps visible.

Agents support engineering work. They never replace engineering judgement, qualified review, project procedures, regulatory requirements, or operational decision making.

## Relationship to NeqSim

[NeqSim](https://github.com/equinor/neqsim) is an open-source library for calculation of fluid behavior, phase equilibrium, thermodynamic properties, and process simulation.

Community agents are designed to make NeqSim-based workflows easier to discover, document, reproduce, and review. An agent may recommend NeqSim calculations, generate example scripts, organize engineering checks, or help explain assumptions. Any generated NeqSim workflow must still be verified by a qualified user before engineering or operational use.

Future versions of this repository may publish agent catalog entries that can be installed into the main NeqSim ecosystem.

## Relationship to NeqSim Community Skills

[NeqSim Community Skills](https://github.com/equinor/neqsim-community-skills) contains reusable skill definitions such as fluid quality checks, hydrate screening, and separator modelling.

Agents use those skills as building blocks. Skills describe focused capabilities; agents combine one or more skills into complete engineering workflows with inputs, outputs, examples, validation checklists, and review expectations.

Current skill mappings used by the example agents:

| Agent skill name | Community skill catalog ID |
| --- | --- |
| `fluid-quality-check` | `neqsim-fluid-quality-check` |
| `hydrate-screening` | `neqsim-hydrate-screening` |
| `separator-modelling` | `neqsim-separator-modelling` |

## What Is An Engineering Agent?

An engineering agent is a documented workflow that can help an engineer perform a bounded task. It may collect inputs, check data quality, invoke skills, propose NeqSim examples, prepare screening reports, and list follow-up studies.

A good agent is:

- Transparent about assumptions and limitations
- Reproducible from documented inputs and steps
- Focused on assisting engineers
- Traceable to skills, examples, and tests
- Clear about when human review is required

## How Agents Work

Each agent has a standard directory layout:

```text
agent-name/
├── AGENT.md
├── agent.yaml
├── examples/
├── prompts/
├── tests/
└── README.md
```

`AGENT.md` is the human-readable agent specification. `agent.yaml` is the machine-readable metadata. The `examples/`, `prompts/`, and `tests/` directories keep usage examples, reusable prompt examples, and validation material close to the agent.

## Initial Example Agents

| Agent | Purpose | Required skills |
| --- | --- | --- |
| [PVT Agent](agents/pvt-agent/README.md) | Fluid characterization, composition checks, phase behavior evaluation, and thermodynamic analysis | `fluid-quality-check` |
| [Hydrate Screening Agent](agents/hydrate-screening-agent/README.md) | Preliminary hydrate risk assessment | `hydrate-screening` |
| [Tie-In Screening Agent](agents/tie-in-screening-agent/README.md) | Early-stage screening of tie-in opportunities | `fluid-quality-check`, `hydrate-screening`, `separator-modelling` |
| [Process Screening Agent](agents/process-screening-agent/README.md) | High-level process engineering screening studies | `separator-modelling` |

## How To Create A New Agent

1. Copy [templates/agent-template](templates/agent-template/) into `agents/<agent-name>/`.
2. Update `AGENT.md` and `agent.yaml` with the agent purpose, required skills, domains, inputs, outputs, assumptions, limitations, and review requirements.
3. Add realistic public examples in `examples/`.
4. Add example prompts in `prompts/`.
5. Add tests or validation notes in `tests/`.
6. Run the repository structure tests.
7. Open a pull request using the contribution checklist.

## How To Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements, required files, documentation expectations, testing expectations, review checklist, and open-source requirements.

Contributions should use public information only. Do not include proprietary field data, confidential design methods, vendor-confidential information, private operational procedures, credentials, or personal data.

## Governance Principles

This repository follows these principles:

- Open, public, and reusable documentation
- Human review for engineering decisions
- Versioned agent metadata
- Transparent assumptions and limitations
- Reproducible examples and validation checks
- Clear deprecation of outdated agents

See [docs/governance.md](docs/governance.md) and [docs/safety-guidelines.md](docs/safety-guidelines.md) for details.

## Testing

Run the repository structure and metadata tests with:

```powershell
python -m unittest discover -s tests
```

The initial tests use only the Python standard library. They validate that each agent has the required files, documentation sections, metadata fields, prompt examples, and examples.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [LICENSE.md](LICENSE.md).
