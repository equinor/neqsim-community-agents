# Dynamic Process Preparation Agent

The Dynamic Process Preparation Agent prepares NeqSim `ProcessSystem` and `ProcessModel` flowsheets for dynamic calculations.

It helps engineers identify dynamic equipment, organize mechanical-design and volume-readiness checks, initialize separator/vessel holdup, and document the NeqSim `run()`, `storeInitialState()`, `setTimeStep(...)`, and `runTransient()` sequence.

## Capabilities

- Identify dynamic candidates in a process flowsheet
- Estimate public vessel volumes from supplied geometry
- Document separator/vessel level and holdup initialization
- Recommend NeqSim mechanical-design handoff where supported
- Prepare transient initialization and execution checklists
- Flag missing geometry, holdup, or timing information

## Required Skills

- `dynamic-process-preparation`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Dynamic preparation outputs are model scaffolding and readiness checks. They require qualified process, dynamic simulation, mechanical design, and operations review before engineering or operational use. This agent does not replace dynamic simulation validation, pressure-vessel design, control-system design, HAZOP, or qualified engineering judgement.
