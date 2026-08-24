# Example: Current Gas-Valve Noise Assessment

This example uses synthetic public data only.

## Input

- Source: gas outlet control valve
- Operating snapshot: 12 kg/s, 50 bara inlet, 10 bara outlet, 35 kg/m3 inlet density
- Gas speed of sound: 410 m/s
- Receiver: operator position 3 m from the source
- Measurement: 92 dBA, uncertainty +/-2 dB, captured during the stated steady operating snapshot
- Project triggers: action at 85 dBA, high at 110 dBA
- Objective: current receiver-noise triage and next-work decision

## Expected Agent Actions

1. Record the operating window, source, receiver, measurement method, and uncertainty.
2. Use `noise-screening` with the measurement override and report `assessment_basis: measurement`.
3. Compare 92 +/-2 dBA against project triggers without describing them as universal ISO exposure limits.
4. Recommend a controlled survey and source contribution check before selecting controls.
5. Request valve/pipe data and run NeqSim IEC 60534-8-3 if source design or mitigation sizing is required.
6. Run AIV screening separately because this is a high pressure-drop source.

## Example Output Summary

- Receiver result: 92 dBA at 3 m, measurement basis, +/-2 dB uncertainty.
- Status: `action` under the stated project screening triggers.
- Evidence gap: octave bands, background/source separation, exposure duration, and verified valve trim/pipe data are absent.
- Next work: controlled ISO-aligned measurement and occupational-hygiene review; detailed IEC 60534-8-3 source prediction before mitigation design.
- AIV: separate screening required; no AIV conclusion is inferred from 92 dBA.

## Human Review

An acoustic specialist and occupational hygienist review receiver/exposure conclusions. Process and valve engineers review source inputs, and a piping-vibration specialist reviews AIV.