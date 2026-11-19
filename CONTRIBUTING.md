# Contributing To NeqSim Community Agents

Thank you for helping build a public ecosystem of transparent, reproducible engineering agents for NeqSim.

Contributions may include new agents, improved documentation, examples, prompt templates, tests, metadata corrections, safety guidance, or governance improvements.

All contributions must be suitable for a public open-source repository.

## Where Does This Belong?

Before adding an agent here, confirm this is the right repository. See the
[Where Does This Go? placement guide](https://github.com/equinor/neqsim-community-skills/blob/main/docs/where-does-this-go.md).
The rules are mandatory:

- Equinor- or company-specific agents, internal systems, shares and policy go in the
  **enterprise** repos. Agents here stay vendor-neutral.
- Agents that are not NeqSim Java functionality go **here**, never in core neqsim.
- Community agents **orchestrate** community skills. They contain no
  engineering method themselves, claim only screening-level results, and reference
  validated NeqSim classes rather than reimplementing them.

Company-specific agents, internal workflow policy, private data integration, and confidential examples belong in private enterprise repositories instead. See the main NeqSim [Enterprise Agent and Skill Repositories](https://github.com/equinor/neqsim/blob/master/docs/integration/enterprise_agent_skill_repos.md) guide for the paired enterprise agents/skills setup and Engineering Harness installation workflow.

## Create An Agent

1. Choose a clear engineering purpose and a bounded scope.
2. Copy [templates/agent-template](templates/agent-template/) to `agents/<agent-name>/`.
3. Update `AGENT.md` with the required sections from [docs/agent-standard.md](docs/agent-standard.md).
4. Update `agent.yaml` with machine-readable metadata.
5. Add at least one realistic public example in `examples/`.
6. Add at least one reusable example prompt in `prompts/`.
7. Add tests or validation notes in `tests/`.
8. Add or update the root `community-agents.yaml` catalog entry with canonical `neqsim-*` skill IDs.
9. Run the repository tests before opening a pull request.

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

### Referencing a newly added skill

`required_skills` and `context_skills` are resolved against the vendored
`schemas/skills.index.json` snapshot, because CI checks out this repo alone and
cannot see the skill repositories. A skill added in `neqsim-community-skills`
therefore resolves locally but fails CI until the snapshot is refreshed. From the
core `neqsim` repo, run:

```bash
python devtools/generate_skill_index.py          # rewrites the snapshot in both agent repos
python devtools/generate_skill_index.py --check  # verify the snapshots are current
```

Commit the regenerated `schemas/skills.index.json` in the same change as the
agent that requires the new skill.

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

Use Python 3.10 or newer and uv for development. From the repository root:

```bash
uv sync --locked
uv run pre-commit install
uv run pre-commit run
uv run pytest tests/
uv run python scripts/validate_agent_manifests.py
uv run python scripts/generate_agent_skill_map.py --check
uv run python scripts/generate_orchestration_map.py --check
```

Pre-commit runs Ruff linting and Black formatting on staged Python files; CI
runs the same hooks on all tracked Python files. Fix findings introduced by
your changes without weakening rules, adding blanket suppressions, or bypassing
hooks. Report unrelated existing failures explicitly.

Manage development dependencies with `uv add --group dev <package>` and
commit the updated `uv.lock`. Agent users do not need uv.

Python 3.10 remains the end-user runtime minimum. The separate runtime CI job
installs only the test dependencies and the two public skill packages needed
by the executable reservoir-to-host examples, then runs `tests/`,
`runtime_tests/` and the manifest validator on Python 3.10. It does not install
the full developer environment or require plotting dependencies.
Keep the developer checks and Ruff's `py310` target unchanged. Pending
single-rule Ruff fixes remain separate from this runtime coverage.

### Devtools 0.3.0 readiness

The `neqsim-dev-setup` 0.3.0 release is defined by merged
[equinor/neqsim#5155](https://github.com/equinor/neqsim/pull/5155).
This agent catalog has no direct toolkit dependency. Development and CI
support Python 3.10+, with newer-version coverage retained. The lockfile
includes the 3.10 developer environment; lightweight end-user runtime
coverage remains separate. Do not bump agent versions solely for the toolkit
release.

Before a plugin release, run the repository checks above and the existing
Python 3.10 runtime/example CI job. Resolve declared skills against the
committed skill index, not just locally installed sibling packages. Toolkit
installation, shared-environment dependency checks, and the generated plugin
rebuild belong to the
[marketplace's 0.3.0 release gate](https://github.com/equinor/neqsim-copilot-plugin/blob/main/docs/maintaining.md#51-devtools-030-release-gate).
Do not treat passing catalog tests as verification of the new toolkit.

## Quiet by default (no pop-ups, no installs, no surprise sign-ins)

Agents and skills run from hooks, MCP servers and chat tool calls with no visible console. Anything that opens a window or asks the user to act breaks the flow, so every new or changed skill and agent must follow these rules:

- **Hidden child processes.** Every `subprocess.run/Popen/check_output/call` in skill code passes `creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)`. Never use `os.system`, `os.startfile` or `shell=True` to start tools. The repository test `test_quiet_processes.py` fails the build otherwise; annotate a deliberate user-requested exception with `# quiet-ok: <reason>`.
- **No installs at run time.** Declare dependencies in the skill's `pyproject.toml`; the plugin installs them once, in the background. Skill code and agent instructions must not run `pip install`, `npm install` or download tools mid-task. If a package is missing, report the blocker and the remedy.
- **Silent authentication first.** Get tokens through `enterprise-sso-auth` (cached tokens, `az account get-access-token`, session warm-up via `session_warmup.json`). Register new APIs in its service registry so they are warmed at session start. Never call `az login`, device-code flows, browser sign-in or credential prompts from skill code or agent steps unless every silent route has failed, and then ask once with the exact remedy.
- **Background by default.** Long installs, downloads and warm-ups run detached with output in a log file, never in the foreground chat. Agent instructions must tell the model to continue with other work rather than wait on them.
- **GUI automation is the exception.** Computer-use skills may start a visible application only when the user's task needs it; say so in the skill's Limitations section.

## Review Checklist

Before submitting a pull request, confirm that:

- The agent has a clear engineering purpose
- The scope is bounded and suitable for screening or assistance
- Required skills are listed and already public or proposed publicly
- Required skills use canonical `neqsim-*` IDs in `AGENT.md`, `agent.yaml`, and `community-agents.yaml`
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