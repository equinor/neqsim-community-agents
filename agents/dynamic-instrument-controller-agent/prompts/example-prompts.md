# Example Prompts

## Add Separator Level Control

```text
Add a level controller to this public NeqSim dynamic separator model. Use LevelTransmitter on V-001, setpoint 0.30, range 0.01 to 0.99, reverse action, PID Kp=25.8 Ti=400.1 Td=0.0, and attach the controller to LCV-001. Include validation warnings and transient response checks.
```

## Add Pressure Control And Autotuning Plan

```text
Prepare a gas-outlet pressure control loop for a NeqSim dynamic separator. Use a PressureTransmitter, a ControllerDeviceBaseClass controller, PCV-001 as manipulated valve, and include an event-log autotuning workflow using resetEventLog and autoTuneFromEventLog(False).
```
