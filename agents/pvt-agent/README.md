# PVT Agent

The PVT Agent assists with fluid characterization, composition checks, phase behavior evaluation, and thermodynamic analysis using NeqSim and the `fluid-quality-check` community skill.

It is intended for public, reproducible engineering assistance. It can help review fluid compositions, identify missing information, recommend NeqSim workflows, and explain assumptions. It does not replace PVT specialist judgement or validated laboratory interpretation.

## Capabilities

- Review fluid compositions
- Check composition quality
- Recommend thermodynamic workflows
- Generate NeqSim examples
- Explain assumptions and limitations

## Required Skill

- `fluid-quality-check`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

All generated checks, workflows, and examples require qualified review before use in design, assurance, reporting, or operations.