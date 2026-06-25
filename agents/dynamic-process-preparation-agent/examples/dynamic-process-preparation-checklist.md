# Dynamic Process Preparation Checklist

This example uses public, synthetic data only. It illustrates preparing a NeqSim separator train for dynamic simulation.

## 1. Objective

- Convert a steady-state `ProcessSystem` into a dynamic-ready process.
- Estimate separator volume from public geometry.
- Prepare the NeqSim transient run sequence.

## 2. Input Data (synthetic)

- Process kind: `ProcessSystem`
- Separator: V-001
- Separator length: 4.0 m
- Separator internal diameter: 1.0 m
- Initial liquid level: 0.25 fraction
- Time step: 10 s
- Total duration: 600 s

## 3. Equipment Actions

- V-001: call `setCalculateSteadyState(False)`.
- V-001: call `setSeparatorLength(4.0)` and `setInternalDiameter(1.0)`.
- V-001: call `setLiquidLevel(0.25)`.
- V-001: initialize and calculate mechanical design if supported.
- Dynamic valves: set opening/pressure basis and switch to dynamic mode.

## 4. Volume Readiness

- Geometric volume estimate: `pi * D^2 / 4 * L`.
- For D = 1.0 m and L = 4.0 m, volume is approximately 3.14 m3.
- Liquid holdup at 0.25 level is approximately 0.79 m3.

## 5. NeqSim Sequence

- Run the steady-state model.
- Inspect pressures, temperatures, flows, and levels.
- Call `storeInitialState()`.
- Call `setTimeStep(10.0)`.
- Call `runTransient()` in a documented loop.

## 6. Required Follow-Up

- Verify transient mass balance.
- Review pressure and level limits.
- Add instruments and controllers if closed-loop dynamics are required.
- Complete qualified human review before engineering use.
