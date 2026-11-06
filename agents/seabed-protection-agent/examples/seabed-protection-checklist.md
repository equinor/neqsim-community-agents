# Example: Seabed Protection Checklist

This example uses public, synthetic data only. It demonstrates how the Seabed Protection Agent scopes trenching and rock dumping for a flowline and links the result to cooldown screening. It does not perform trawl-interference, upheaval-buckling, free-span or stability assessment.

## Scenario

A 14 km, 16 inch flowline (outer diameter 0.42 m with coating) crosses sand, a 4 km rock outcrop and soft mud, through an area of high fishing intensity, and crosses one 20 inch export pipeline.

Public synthetic inputs:

- Substrate polygons: sand, rock, mud to sandy mud
- Fishing-intensity polygons: low over the whole area, high over the central part
- One pipeline line feature, `EXPORT-1`, 20 inch
- No surveyed cover; no rock placement rate supplied

## Screening Steps

1. Confirm the objective: concept-stage scope of trenching and rock dump.
2. Plan the read-only map requests and load the synthetic layers.
3. Build the route at 250 m stations and sample substrate and fishing intensity, with the highest-ranked intensity winning where polygons overlap.
4. Find the crossing of `EXPORT-1` and record its KP, angle and diameter.
5. Run the screening and review the strategy per segment: trench in sand and mud, rock dump on the outcrop.
6. Review the data gaps: the mud uses a placeholder strength, there is no surveyed cover and no rock rate.
7. Replace placeholders with the project basis and rerun.
8. Hand the burial state to cooldown screening and run the unprotected case for comparison.
9. List the required follow-up studies.

## Expected Screening Output Outline

- Segments with controlling hazard, required cover and strategy
- Trench length by method and trench days
- Rock volume and tonnes for the route and the crossing, with the spillage factor stated
- Data gaps, assumptions and warnings
- The burial hand-off sections for the thermal model
- Protected against unprotected cooldown and hydrate margin
- A routing note that trawl interference, upheaval buckling and span assessments go to qualified engineering
