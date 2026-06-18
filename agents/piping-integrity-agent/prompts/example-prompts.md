# Example Prompts

These prompts use public, synthetic data only. They are intended for early-stage screening.

## Line Velocity Screening

```text
Use public synthetic data to screen a process line with a fluid velocity of 12 m/s, a mixture density of 50 kg/m^3, an erosional C-factor of 122, and a maximum velocity guideline of 20 m/s. Report the erosional velocity, the velocity ratio, the guideline ratio, and the warning level, and suggest validated API RP 14E, NORSOK P-002, and NeqSim workflows.
```

## Pressure-Drop Screening

```text
Use public synthetic data to screen a single-phase line that is 150 m long with an inside diameter of 0.2 m, a Darcy friction factor of 0.018, a fluid velocity of 12 m/s, and a density of 50 kg/m^3, against a pressure-gradient guideline of 0.5 bar per 100 m. Report the pressure gradient, the guideline ratio, and the warning level, and suggest validated NORSOK P-002 and NeqSim workflows.
```

## Wall-Thickness Screening

```text
Use public synthetic data to screen a process pipe with a design pressure of 50 bar, an outside diameter of 219.1 mm, an allowable stress of 138 MPa, and a nominal wall thickness of 8.18 mm using the ASME B31.3 hoop-stress equation. Report the minimum wall thickness, the thickness margin ratio, and the warning level, and suggest validated ASME B31.3 and NeqSim workflows.
```

## Flow-Induced Vibration Screening

```text
Use public synthetic data to screen a line for flow-induced vibration with a flow velocity of 12 m/s and a density of 50 kg/m^3 using the fluid kinetic-energy index. Report the kinetic-energy value, the likelihood index, and the warning level, and suggest validated Energy Institute and NeqSim workflows.
```

## Combined Piping Integrity Screening

```text
Screen a process line for integrity using public synthetic data. Summarize the line velocity ratio, the single-phase pressure gradient, the minimum wall thickness, and the flow-induced vibration likelihood index, and flag any line that appears to run outside guidelines. List the required follow-up studies and prepare a screening report outline with assumptions, limitations, and a human review checklist.
```
