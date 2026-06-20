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

[equinor/neqsim: NeqSim is a library for calculation of fluid behavior, phase equilibrium and process simulation](https://github.com/equinor/neqsim).

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
| `relief-load-screening` | `neqsim-relief-load-screening` |
| `depressurization-screening` | `neqsim-depressurization-screening` |
| `line-velocity-check` | `neqsim-line-velocity-check` |
| `compressor-operating-window-check` | `neqsim-compressor-operating-window-check` |
| `hydrate-margin-check` | `neqsim-hydrate-margin-check` |
| `wax-margin-check` | `neqsim-wax-margin-check` |

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

## Using an Agent in a Harness

A *harness* is any driver — a test, a script, a CLI, or the main NeqSim repo's task workflow — that loads an agent definition and runs its skills in order. An agent is mostly declarative: `agent.yaml` lists the `required_skills`, and each skill is an installable Python package. A harness reads that list, installs the matching skill packages, then calls them and assembles a reviewable summary.

1. Install the skill packages the agent declares. For the Flow Assurance Engineer Agent (`hydrate-margin-check`, `wax-margin-check`):

   ```bash
   python -m pip install -e ../neqsim-community-skills/skills/flow-assurance/hydrate-margin-check
   python -m pip install -e ../neqsim-community-skills/skills/flow-assurance/wax-margin-check
   ```

2. Drive the agent's skills from one harness:

   ```python
   # harness.py — runs a community agent's required skills, e.g. from the neqsim main repo
   import yaml
   from hydrate_margin_check import HydrateMarginModel

   # 1. Read the machine-readable agent contract.
   with open("agents/flow-assurance-engineer-agent/agent.yaml") as f:
       agent = yaml.safe_load(f)
   print("required skills:", agent["required_skills"])

   # 2. Invoke each skill with validated NeqSim-derived inputs.
   margin = HydrateMarginModel(min_margin=3.0).evaluate(
       operating_temperature=15.0,
       hydrate_equilibrium_temperature=8.0,
   )

   # 3. Assemble a review-ready summary that keeps assumptions visible.
   print("hydrate margin (C):", margin.hydrate_margin_c, margin.margin_warning)
   for note in margin.assumptions:
       print("assumption:", note)
   if agent.get("human_review_required"):
       print("Human review required before any engineering or operational use.")
   ```

The harness is the boundary where the agent's declared inputs, skills, assumptions, and review requirement become a runnable workflow. The agent definition stays transparent and reproducible; the harness only orchestrates the skills it names and surfaces their combined output for qualified human review.

### Automatic discovery via the Engineering Harness

This repository publishes a machine-readable catalog, [`community-agents.yaml`](community-agents.yaml), so a runtime can discover every agent and its `required_skills` without opening each `agent.yaml`. The [Engineering Harness](https://github.com/equinor/engineering-harness) lists this repo as a default plugin source and imports it with:

```powershell
engineering-harness plugins sync      # imports community agents (public, no token)
engineering-harness list agents       # shows the imported agents
```

Each catalog entry maps to a harness `Agent` (name, description, `allowed_skills` from `required_skills`, `allowed_tools: [neqsim]`, `requires_human_approval: true`). Because the agents only declare skills that the harness also imports, a workflow launched from the main NeqSim repo can run them end to end.

## Initial Example Agents

| Agent | Purpose | Required skills |
| --- | --- | --- |
| [PVT Agent](agents/pvt-agent/README.md) | Fluid characterization, composition checks, phase behavior evaluation, and thermodynamic analysis | `fluid-quality-check` |
| [Hydrate Screening Agent](agents/hydrate-screening-agent/README.md) | Preliminary hydrate risk assessment | `hydrate-screening` |
| [Tie-In Screening Agent](agents/tie-in-screening-agent/README.md) | Early-stage screening of tie-in opportunities | `fluid-quality-check`, `hydrate-screening`, `separator-modelling` |
| [Process Screening Agent](agents/process-screening-agent/README.md) | High-level process engineering screening studies | `separator-modelling` |
| [Process Safety Agent](agents/process-safety-agent/README.md) | Early-stage fire-case relief load and depressurization screening | `relief-load-screening`, `depressurization-screening` |
| [Process Engineer Agent](agents/process-engineer-agent/README.md) | Early-stage screening of unit operations against line-velocity and compressor operating-window guidelines | `line-velocity-check`, `compressor-operating-window-check` |
| [Flow Assurance Engineer Agent](agents/flow-assurance-engineer-agent/README.md) | Early-stage screening of operating points against hydrate-margin and wax-margin guidelines | `hydrate-margin-check`, `wax-margin-check` |

## How To Create A New Agent

1. Copy [templates/agent-template](templates/agent-template/) into `agents/<agent-name>/`.
2. Update `AGENT.md` and `agent.yaml` with the agent purpose, required skills, domains, inputs, outputs, assumptions, limitations, and review requirements.
3. Add realistic public examples in `examples/`.
4. Add example prompts in `prompts/`.
5. Add tests or validation notes in `tests/`.
6. Run the repository structure tests.
7. Open a pull request using the contribution checklist.

## How To Contribute

Not sure which repository a contribution belongs in? See the shared [Contribution Router](https://github.com/equinor/idea-sharing-AI-agents/blob/main/CONTRIBUTION-ROUTER.md).

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

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
