# Example Prompts

## Tubing-only table

```text
Use the VFP Lift Curve Agent to build a tubing-only VFPPROD table for a synthetic gas well. I will give the survey,
fluid and axis ranges. Validate off-grid and give me the include file.
```

## Full-system curve

```text
Use the VFP Lift Curve Agent to build a full-system VFPPROD from reservoir datum to a fixed separator pressure for a
synthetic well, flowline and compressor train. State what the THP axis means and how the compressor limit enters.
```

## Repair an existing table

```text
Use the VFP Lift Curve Agent to review this VFPPROD include file: check axes, U-shape in rate, extrapolation for the
late-life range and the dry-gas jump, and tell me what to regenerate.
```
