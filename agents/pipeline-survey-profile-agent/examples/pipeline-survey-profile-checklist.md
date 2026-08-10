# Example: Pipeline Survey Profile Checklist

This example uses public, synthetic data only. It demonstrates how the Pipeline Survey Profile Agent turns a survey export into a pipeline profile. It does not perform free-span, stability or integrity assessment.

## Scenario

A 2 km flowline section has been surveyed twice. The 2010 survey is processed into a profile and compared against the 2006 baseline.

Public synthetic inputs:

- Survey rows at 5 m KP spacing with `depth_to_top_m` around -298 m (negative-up) and `seabed_depth_m` 0.2 m above the pipe top
- One row carrying the null marker -999.25
- One row with a 45 m depth spike
- An 11-station stretch where the seabed sits 0.4 m below the pipe top
- No outer diameter in the survey; 0.3239 m is taken from the line list
- Section of interest: the flowline end at KP 0 to the hot-tap at KP 2000
- Repeat comparison threshold: 0.2 m

## Screening Steps

1. Confirm the objective: preliminary survey processing and profile triage only.
2. Run `pipeline-survey-processing` to detect the depth convention, remove null markers and duplicates, apply the resolution filter, and build the profile.
3. Review the flagged erroneous points against the survey report; confirm the spike is flagged and that it is excluded from the span and cover geometry.
4. Trim the profile to KP 0 - 2000 and confirm no neighbouring line is included.
5. Review the free-span candidates and the controlling minimum cover.
6. Record the manually supplied outer diameter as a data gap.
7. Compare against the 2006 baseline and report the changed intervals without describing them as movement.
8. Hand the elevation profile to `pressure-drop-screening` and `line-velocity-check` if arrival conditions are in scope.
9. List required follow-up studies.

## Expected Screening Output Outline

- Detected depth convention and the retained, rejected and flagged point counts
- The processing log, in order, as evidence
- Free-span candidates with length and maximum gap, plus the controlling minimum cover
- Repeat-survey maximum lowering and lifting with the changed intervals
- The evenly spaced elevation profile handoff for a NeqSim pipe model
- Data gaps, assumptions, limitations, and a human review checklist
- A routing note that span candidates go to a qualified DNV-RP-F105 assessment
