# Agents

This directory contains reusable engineering agents built on NeqSim and NeqSim Community Skills.

Each agent must follow the repository standard:

```text
agent-name/
├── AGENT.md
├── agent.yaml
├── examples/
├── prompts/
├── tests/
└── README.md
```

Agents assist engineers by making workflows transparent and reproducible. They must document assumptions, limitations, validation checks, and human review requirements.

Initial agents:

- [pvt-agent](pvt-agent/README.md)
- [hydrate-screening-agent](hydrate-screening-agent/README.md)
- [tie-in-screening-agent](tie-in-screening-agent/README.md)
- [process-screening-agent](process-screening-agent/README.md)