# Example Prompts

## Build a profile from a survey export

```text
Use public synthetic survey data for a flowline. Clean the survey into a pipeline profile, report the depth convention that was detected and everything that was filtered, and flag erroneous points without deleting them. List the processing log and any data gaps.
```

## Extract the section between two structures

```text
Only the section between the flowline end and the hot-tap is in scope. Trim the profile to that KP window, confirm no neighbouring line is included, and report the section length and maximum slope.
```

## Screen free spans and cover

```text
The survey carries seabed depth. Locate free-span candidates and cover intervals along KP, report the longest span, the total exposed length and the controlling minimum cover, and route the span candidates to a DNV-RP-F105 assessment.
```

## Handle a missing outer diameter

```text
The survey has no outer diameter. Use 0.3239 m from the line list, record the override as a data gap, and state what the diameter is used for downstream.
```

## Compare two surveys

```text
Compare the 2010 survey against the 2006 baseline on a common KP grid. Report the maximum lowering and lifting and the changed intervals, and state explicitly what must be reconciled before any change is described as pipeline movement.
```

## Carry the profile into hydraulic screening

```text
Hand the cleaned elevation profile to pressure-drop and line-velocity screening for the supplied fluid and flow rate, and prepare a screening summary that separates facts, assumptions and recommendations.
```
