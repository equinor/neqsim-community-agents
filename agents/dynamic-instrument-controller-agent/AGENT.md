---
name: dynamic-instrument-controller-agent
description: Adds NeqSim measurement devices and PID-style controllers for dynamic process simulations.
version: 0.1.0
required_skills:
  - dynamic-instrument-controller-setup
---

# Purpose

The Dynamic Instrument Controller Agent assists engineers with adding measurement devices and controller loops to NeqSim dynamic simulations. It organizes transmitter selection, controller setpoints and PID parameters, direct or reverse action, manipulated-equipment attachment, transient response checks, and optional event-log autotuning workflow.

The agent supports dynamic model scaffolding and control-loop review. It does not replace control-system design, controller tuning, safety-instrumented-system design, operating procedure approval, project assurance, or qualified engineering judgement. A qualified human review is always required.

# When to Use

Use this agent when an engineer needs to:

- Add level, pressure, temperature, or flow measurement devices to a dynamic NeqSim process
- Create transmitter-based controllers with `ControllerDeviceBaseClass`
- Attach controllers to throttling valves or other manipulated equipment
- Choose direct or reverse action for a first dynamic trial
- Document setpoints, transmitter ranges, and PID parameters
- Use controller event logs and `autoTuneFromEventLog(False)` in a tuning study
- Prepare a transparent control-loop setup checklist for `runTransient()` calculations

# Inputs

Typical inputs include:

- Control loop name and controlled variable
- Transmitter target equipment or stream
- Manipulated valve or equipment
- Controller setpoint and units or basis
- Transmitter minimum and maximum values
- Reverse/direct action basis
- PID parameters (`Kp`, `Ti`, `Td`)
- Transient response acceptance checks and autotuning objective

# Outputs

Typical outputs include:

- Control-loop setup plan
- Recommended NeqSim transmitter class
- Controller configuration steps
- Manipulated-equipment attachment steps
- Validation warnings for range, action, setpoint, and tuning metadata
- Autotuning workflow outline
- Human-review checklist

# Workflow

1. Confirm the dynamic control objective and controlled variable.
2. Use `dynamic-instrument-controller-setup` to map the controlled variable to a NeqSim transmitter class.
3. Validate transmitter range, setpoint, controller action, and PID metadata.
4. Define the NeqSim setup sequence: create transmitter, set range, create controller, attach transmitter, set action, set setpoint, set PID parameters, and attach controller to manipulated equipment.
5. Add the transmitter to the `ProcessSystem` and verify the manipulated unit is in dynamic mode.
6. Run transient checks for saturation, stability, and nonphysical states.
7. If autotuning is requested, define the event-log reset, setpoint-step, transient-run, and `autoTuneFromEventLog(False)` workflow.

# Required Skills

- `dynamic-instrument-controller-setup` mapped to community catalog ID `neqsim-dynamic-instrument-controller-setup`

# Example Usage

```text
Add a level controller to a public NeqSim dynamic separator model. Use a LevelTransmitter on V-001, controller setpoint 0.30, transmitter range 0.01 to 0.99, reverse action, PID parameters Kp=25.8, Ti=400.1, Td=0.0, and attach it to LCV-001. Produce the NeqSim setup sequence and transient validation checklist.
```

# Assumptions

- Inputs are public, synthetic, or approved for open-source use.
- A dynamic-ready NeqSim process exists or is being prepared.
- Controller action and PID parameters are first-trial setup metadata.
- Human review is required before design or operational use.

# Limitations

- The agent does not execute NeqSim, tune controllers, or guarantee closed-loop stability.
- The agent does not size valves or design control valves.
- The agent does not define safety instrumented functions, alarm limits, or operating procedures.
- The agent does not replace process-control engineering, dynamic simulation validation, HAZOP, or qualified engineering judgement.

# Validation Checklist

- Controlled variable and transmitter target are documented.
- Transmitter min/max values bracket the setpoint and expected range.
- Controller action is checked against process cause and effect.
- Manipulated equipment supports controller attachment and dynamic behavior.
- PID parameters are finite and recorded.
- Transient response is reviewed for saturation, oscillation, instability, and nonphysical values.
- Autotuning event logs contain deliberate excitation before tuning parameters are accepted.
- Human review is completed before engineering or operational decisions.

# Related NeqSim Functionality

- `neqsim.process.measurementdevice.LevelTransmitter` — level measurement for separators and vessels.
- `neqsim.process.measurementdevice.PressureTransmitter` — pressure measurement for streams or equipment outlets.
- `neqsim.process.controllerdevice.ControllerDeviceBaseClass` — transmitter-based controller with setpoint, action, PID parameters, response, event log, and autotuning support.
- `neqsim.process.equipment.valve.ThrottlingValve#setController(...)` — attach the controller to a manipulated valve.
- `neqsim.process.processmodel.ProcessSystem#runTransient()` — execute the controlled dynamic simulation.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skill: `dynamic-instrument-controller-setup`
