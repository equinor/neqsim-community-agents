# NeqSim Community Agents

A community-driven collection of AI agents for thermodynamics, process engineering, flow assurance, energy systems, and field development built on NeqSim.

This repository contains reusable agent definitions, workflows, and engineering assistants that combine NeqSim capabilities with engineering skills, domain knowledge, and external tools to solve real-world engineering problems.

The goal is to provide a shared ecosystem of transparent, reproducible, and extensible engineering agents that can assist engineers, researchers, students, and industry professionals throughout the lifecycle of energy and process systems.

## What is an Agent?

An agent is an engineering workflow that combines:

* Engineering skills
* NeqSim calculations
* Domain knowledge
* External tools and data sources
* Human review and validation

Agents can perform tasks such as:

* Gathering engineering information
* Running simulations
* Evaluating alternatives
* Generating reports
* Screening concepts
* Explaining assumptions and limitations

Agents support engineers but do not replace engineering judgement.

## Example Agents

### Process Engineering

* Process Screening Agent
* Process Troubleshooting Agent
* Process Optimization Agent
* Digital Twin Agent

### PVT and Thermodynamics

* PVT Characterization Agent
* Fluid Quality Assurance Agent
* Phase Behavior Analysis Agent
* EOS Selection Agent

### Flow Assurance

* Hydrate Screening Agent
* Wax Risk Assessment Agent
* Scale Evaluation Agent
* Pipeline Operations Agent

### Rotating Equipment

* Compressor Performance Agent
* Compressor Monitoring Agent
* Turbine Evaluation Agent

### Field Development

* Tie-In Evaluation Agent
* Field Development Screening Agent
* Concept Comparison Agent
* Production Optimization Agent

### Energy Transition

* CCS Screening Agent
* Hydrogen Transport Agent
* LNG Agent
* Energy Efficiency Agent
* Emissions Reduction Agent

## Relationship to NeqSim Skills

Agents are built using reusable skills from:

[NeqSim Community Skills](https://github.com/equinor/neqsim-community-skills?utm_source=chatgpt.com)

A typical workflow may look like:

```text
Agent
  ├── PVT Skill
  ├── Flow Assurance Skill
  ├── Process Simulation Skill
  └── Facility-Specific Skill
```

This separation allows skills to be reused across many different agents.

## Example Agent Structure

```text
tie-in-agent/
├── AGENT.md
├── agent.yaml
├── examples/
├── prompts/
└── tests/
```

An agent may define:

* Objectives
* Required skills
* Tool integrations
* Decision logic
* Validation requirements
* Reporting templates

## Who Can Contribute?

We welcome contributions from:

* Process engineers
* Thermodynamics specialists
* Researchers
* Students
* Universities
* Technology providers
* Open-source developers

Contributors can create new agents, improve existing workflows, and share engineering knowledge with the wider community.

## Vision

Build an open ecosystem of engineering agents that combine physics-based simulation, engineering expertise, and artificial intelligence to accelerate innovation in energy, process industries, and sustainability.

Together with NeqSim and the community skills ecosystem, these agents help transform engineering knowledge into scalable, reusable, and collaborative workflows.

**Energy for people. Progress for society.**
