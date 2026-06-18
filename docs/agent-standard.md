# Agent Standard

This document defines the required structure, metadata, documentation standards, validation requirements, and testing expectations for NeqSim Community Agents.

## Required AGENT.md Structure

Every `AGENT.md` file must begin with YAML-style front matter:

```yaml
---
name: agent-name
description: Short description of the engineering task this agent assists with.
version: 0.1.0
required_skills:
  - skill-name
---
```

Every `AGENT.md` file must then include these sections in clear markdown:

- `# Purpose`
- `# When to Use`
- `# Inputs`
- `# Outputs`
- `# Workflow`
- `# Required Skills`
- `# Example Usage`
- `# Assumptions`
- `# Limitations`
- `# Validation Checklist`
- `# Related NeqSim Functionality`
- `# References`

## Required Metadata

Every `agent.yaml` file must define:

```yaml
name: agent-name
description: Short description.
required_skills:
  - skill-name
supported_domains:
  - domain-name
inputs:
  - input-name
outputs:
  - output-name
human_review_required: true
```

`human_review_required` must be `true` for engineering agents in this repository.

## Agent Documentation Standards

Agent documentation must be:

- Public and open-source suitable
- Transparent about assumptions and limitations
- Reproducible from stated inputs and workflow steps
- Clear about which skills are required
- Clear about where NeqSim calculations may be used
- Clear that the agent assists engineers and does not replace engineering judgement

Where possible, every agent should include a `# Related NeqSim Functionality` section that links the agent to NeqSim functionality. Name the concrete NeqSim Java classes or methods, and/or the NeqSim MCP tools, that the agent's required skills ultimately drive, so the agent stays traceable to the validated engine. If an agent only orchestrates data-supply or reporting skills, name the downstream NeqSim Java/MCP workflow rather than claiming it runs calculations itself. Only cite NeqSim functionality that actually exists.

Documentation should avoid claims of certified accuracy, operational readiness, or guaranteed safety unless supported by an approved validation process outside this repository.

## Validation Requirements

Each agent must include a validation checklist that covers:

- Input completeness
- Unit consistency
- Data quality checks
- Skill-specific checks
- Assumption review
- Limitation review
- Required human review

Validation checklists should distinguish between screening-level results and engineering conclusions.

## Testing Expectations

Each agent should include tests or validation notes appropriate to its maturity.

Minimum expectations:

- Required files exist
- Required metadata fields exist
- Required documentation sections exist
- At least one example prompt exists
- At least one public example exists
- Human review is required

More mature agents should add tests for example workflows, expected warnings, generated report structure, and reproducibility of NeqSim examples.