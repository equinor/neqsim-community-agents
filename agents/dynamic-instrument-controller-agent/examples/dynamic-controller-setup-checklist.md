# Dynamic Controller Setup Checklist

This example uses public, synthetic data only. It illustrates adding a level and pressure controller to a NeqSim dynamic separator model.

## 1. Objective

- Add a level transmitter and controller for separator liquid level.
- Add a pressure transmitter and controller for separator gas-outlet pressure.
- Prepare the loop setup for transient validation.

## 2. Level Loop (synthetic)

- Loop: LC-001
- Transmitter: `LevelTransmitter(V-001)`
- Transmitter range: 0.01 to 0.99 fraction
- Setpoint: 0.30 fraction
- Controller: `ControllerDeviceBaseClass`
- Action: reverse acting
- PID: Kp=25.8, Ti=400.1, Td=0.0
- Manipulated equipment: LCV-001 liquid outlet valve

## 3. Pressure Loop (synthetic)

- Loop: PC-001
- Transmitter: `PressureTransmitter(V-001 gas outlet)`
- Transmitter range: 0.01 to 10.0 bara
- Setpoint: 5.0 bara
- Controller: `ControllerDeviceBaseClass`
- Action: direct or reverse by process cause-and-effect review
- PID: Kp=1.0, Ti=2000.0, Td=0.0
- Manipulated equipment: PCV-001 gas outlet valve

## 4. NeqSim Sequence

- Create transmitter and set min/max values.
- Create controller and attach transmitter.
- Set action, setpoint, and PID parameters.
- Attach controller to manipulated valve with `setController(...)`.
- Add transmitter to the `ProcessSystem`.
- Run transient simulation and record response.

## 5. Autotuning Study

- Call `resetEventLog()` before excitation.
- Apply deliberate setpoint steps.
- Run enough transient time to capture response.
- Call `autoTuneFromEventLog(False)`.
- Re-run and verify stability before accepting parameters.

## 6. Human Review

- Qualified process-control review is required.
- This setup does not replace controller tuning, valve sizing, safety function design, or operations approval.
