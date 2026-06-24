# Example Prompts

These prompts use public, synthetic data only. They are intended for early-stage screening.

## Layout Import and Step-Out Screening

```text
Use public synthetic data to import a GeoJSON map of one host and three wells, then compute the host-to-well step-out distances and a node-to-node distance matrix. Report the maximum step-out and the step-out warning level, and flag any data-quality issues in the imported layout.
```

## Route Profile Screening

```text
Use public synthetic data to build the along-route horizontal and elevation profile between ordered waypoints from a host to the nearest well. Report the total route length, the net elevation change, the maximum slope, and the slope warning level.
```

## Combined Subsea Layout Screening

```text
Screen a subsea layout using public synthetic data. Import the supplied map, compute step-out distances and a distance matrix, build the elevation profile to the nearest well, and screen the seabed soundings for steep sections. List the required follow-up studies and prepare a screening report outline with assumptions, limitations, and a human review checklist.
```
