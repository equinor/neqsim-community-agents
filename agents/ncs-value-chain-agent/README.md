# ncs-value-chain-agent

Whole-system Norwegian Continental Shelf value-chain screening on open data. It
builds the field → trunkline → plant → terminal → market graph, loads it,
stresses it, and optimises production and value across the shelf. Results are
handed to validated NeqSim classes (`TiebackAnalyzer`, `LoopedPipeNetwork`,
`ValueChainObjective`, `DebottleneckingAdvisor`, host process models).

- Definition: [AGENT.md](AGENT.md) · manifest: [agent.yaml](agent.yaml)
- Skills:
  - [neqsim-ncs-infrastructure-network](https://github.com/equinor/neqsim-community-skills/tree/main/skills/field-development/neqsim-ncs-infrastructure-network)
  - [neqsim-ncs-value-chain-optimization](https://github.com/equinor/neqsim-community-skills/tree/main/skills/field-development/neqsim-ncs-value-chain-optimization)
- Examples: [examples/ncs-value-chain-checklist.md](examples/ncs-value-chain-checklist.md)
- Prompts: [prompts/example-prompts.md](prompts/example-prompts.md)

Enterprise extension (governed forecasts, tariffs, meters):
`enterprise-ncs-value-chain-optimization-agent` in `neqsim-enterprise-agents`.

Screening only; qualified human review is required.
