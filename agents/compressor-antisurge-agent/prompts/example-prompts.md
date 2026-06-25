# Example Prompts

These prompts use public, synthetic data only. They are intended for early-stage screening and model scaffolding.

## Anti-Surge Recycle Estimate

```text
Use public synthetic data to estimate anti-surge recycle for a centrifugal compressor with a suction flow of 4200 m3/h and a surge flow of 5000 m3/h at the operating head. Report whether the point is in surge, the surge margin, the recommended recycle flow, the total suction flow, and the warning level, and suggest validated API 617, API 692, and NeqSim anti-surge workflows.
```

## Compressor Chart Generation (No Vendor Chart)

```text
A centrifugal compressor has no vendor performance chart. Using public synthetic data, explain how to generate a NeqSim compressor chart with surge and stonewall curves from the design point (speed 8000 rpm, five speed lines), and how to read the surge flow and distance to surge afterward. Note that the generated chart is a model estimate, not a vendor map.
```

## Full Anti-Surge Setup

```text
Set up anti-surge recycle control for a centrifugal compressor using public synthetic data. No vendor chart is available, so first generate a NeqSim chart with surge and stonewall curves, then estimate the recommended recycle flow, describe the NeqSim anti-surge recycle topology (surge curve, recycle stream, discharge splitter, anti-surge Calculator, anti-surge valve, Recycle), list required follow-up studies, and prepare a setup report outline with assumptions, limitations, and a human review checklist.
```
