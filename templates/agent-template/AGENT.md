---
name: agent-name
description: Short description of the engineering task this agent assists with.
version: 0.1.0
required_skills:
  - skill-name
---

# Purpose

Describe the engineering purpose of the agent and the type of assistance it provides.

# When to Use

List the situations where this agent is appropriate.

# Inputs

List required and optional inputs, including units and data quality expectations.

# Outputs

List expected outputs, reports, examples, checklists, and validation material.

# Workflow

Describe the reproducible workflow steps.

# Python Runtime

Reuse whichever Python interpreter the calling workflow has already selected — the active virtual environment (for example the `.venv` created by `install.cmd`/`install.sh`), a VS Code-selected interpreter, or an `NEQSIM_PYTHON` environment variable if the caller sets one — and launch every child Python process with that same absolute executable or `sys.executable`. If no interpreter has been selected yet, resolve `python3`/`python` from PATH. Never call Python environment configuration/selection tools, never ask the user to choose an environment, never invoke a bare `python`/`py`/`pip`/`pytest` once an absolute path is known, never create or activate a separate per-agent environment, and never silently fall back to a different interpreter. Report a missing required package as a blocker instead of switching interpreters.

# Required Skills

List required NeqSim Community Skills and catalog mappings when available.

# Example Usage

```text
Use this agent to review a public synthetic engineering example. Include assumptions, limitations, and human review requirements.
```

# Assumptions

Document assumptions required for the agent to operate.

# Limitations

Document what the agent cannot do. State that it does not replace engineering judgement.

# Validation Checklist

List checks required before outputs can be used or shared.

# Related NeqSim Functionality

Link this agent to NeqSim functionality where possible. Name the NeqSim Java classes/methods and/or NeqSim MCP tools that the required skills ultimately drive (for example `neqsim.process.processmodel.ProcessSystem`). If the agent only orchestrates data-supply or reporting skills, name the downstream NeqSim Java/MCP workflow rather than claiming it runs calculations. Only cite functionality that actually exists.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills