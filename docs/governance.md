# Governance

This document describes ownership, versioning, maintenance, and deprecation expectations for NeqSim Community Agents.

## Ownership

Agents are maintained by the repository community. Each agent should have clear maintainers or reviewers when it becomes mature enough for regular use.

Owners and reviewers are responsible for:

- Reviewing technical scope
- Maintaining documentation quality
- Checking assumptions and limitations
- Ensuring examples remain public and reproducible
- Reviewing required skills and metadata
- Updating or deprecating outdated agents

## Versioning

Each agent has a `version` field in `AGENT.md` front matter and may also be listed in `community-agents.yaml`.

Use semantic versioning principles:

- Patch updates for documentation corrections and minor metadata fixes
- Minor updates for new examples, prompts, tests, or compatible workflow improvements
- Major updates for breaking workflow changes, renamed inputs or outputs, or major scope changes

Version changes should be documented in the pull request description.

## Maintenance

Maintainers should periodically review agents for:

- Compatibility with NeqSim and community skills
- Broken links
- Outdated assumptions
- Missing human review statements
- Test coverage gaps
- Public open-source suitability

Agents should remain focused. If an agent grows too broad, split it into smaller agents or move reusable logic into skills.

## Deprecation Policy

An agent may be deprecated when:

- It depends on obsolete skills or unsupported workflows
- It duplicates a better maintained agent
- It contains assumptions that are no longer appropriate
- It cannot be maintained safely
- Its scope is no longer suitable for public open-source use

Deprecation should include:

- A clear deprecation notice in `README.md` and `AGENT.md`
- Suggested replacement agents or workflows when available
- Version and date of deprecation
- Removal plan if removal is expected

Deprecated agents must still avoid misleading users. They should clearly state that they are not recommended for new work.

## Governance Principles

- Agents assist engineers and do not replace engineering judgement.
- Assumptions and limitations must be explicit.
- Workflows should be transparent and reproducible.
- Examples must be public and non-proprietary.
- Human review is required for engineering decisions.
- Safety-related claims require appropriate review outside this repository.