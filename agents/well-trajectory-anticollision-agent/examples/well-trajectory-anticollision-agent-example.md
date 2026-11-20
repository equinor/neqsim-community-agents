# Example: Slot-Recovery Sidetrack with Anti-Collision Screening

This example uses public synthetic data for demonstration only. It is the case in
`examples/synthetic_template_example.py` of the `neqsim-well-trajectory-anticollision` skill.

## Input

- A template with three slots, 2.5 m apart: T-1 H producing, T-2 H closed, T-3 H producing
- A vertical exploration well X-1, about 3 km north-east of the template
- Target at E 1490 / N 2680 / 2100 m TVDSS, 22 m from X-1
- Sidetrack from T-2 H tied in near 900 m MD, 3°/30 m build/turn
- ISCWSA SF rule: k = 3.5, STOP < 1.0, CAUTION < 1.5

## Expected Agent Actions

1. Group the wellbores by surface location. Slot 02 holds only a closed bore, so the result is
   RECOVERABLE and the plan becomes a slot-recovery sidetrack.
2. Plan the curve-hold from the T-2 H tie-in to the target and add new-hole uncertainty.
3. Scan against T-1 H, T-2 H (parent), T-3 H and X-1.
4. Report X-1 as the governing offset, with SF below 1.0 (STOP).
5. Run the pull-back search and propose a target about 25 m back towards the slot, which gives SF ≥ 1.5.
6. Report the parent exit depth and recommend an official anti-collision run.

## Example Output Summary

- Plan: TD about 4130 m MD, hold about 79°, max DLS 3.0°/30 m, step-out ratio about 1.75.
- Governing offset X-1: SF 0.94 (STOP) at TD.
- T-2 H parent: below CAUTION down to about 1060 m MD, then clear.
- Pulling the target back 25 m gives a governing SF of about 1.75. This moves the target, so subsurface
  must confirm it.
- The step-out ratio is above 1.5, so an ERD reach check is recommended.

## Human Review

A qualified directional-drilling engineer must review the plan. The official directional-planning
system must run the anti-collision with the operator's error models before the plan is used.
