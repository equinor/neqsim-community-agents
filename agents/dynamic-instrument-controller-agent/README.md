# Dynamic Instrument Controller Agent

The Dynamic Instrument Controller Agent helps add measurement devices and PID-style controllers to NeqSim dynamic simulations.

It guides transmitter selection, controller setpoint and PID setup, direct/reverse action checks, manipulated valve attachment, transient response review, and event-log autotuning workflow.

## Capabilities

- Map controlled variables to NeqSim transmitter classes
- Document transmitter range and setpoint checks
- Set up `ControllerDeviceBaseClass` loops
- Attach controllers to throttling valves or manipulated equipment
- Flag likely setup warnings before transient runs
- Outline `resetEventLog()` and `autoTuneFromEventLog(False)` workflows

## Required Skills

- `dynamic-instrument-controller-setup`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Control-loop setup outputs are model scaffolding and first-trial checks. They require qualified process-control, process engineering, dynamic simulation, and operations review before engineering or operational use. This agent does not replace controller tuning, safety instrumented function design, HAZOP, operating procedure approval, or qualified engineering judgement.
