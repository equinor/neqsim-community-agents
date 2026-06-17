# Flow Assurance Screening Checklist (Example)

This public example shows how the Flow Assurance Engineer Agent screens an operating point against hydrate and wax margins using synthetic data. It is educational only and does not replace qualified flow assurance review.

## 1. Screening Objective

- Confirm whether a subsea operating point keeps a safe temperature margin above the hydrate and wax boundaries.
- Decision criteria: hydrate margin at least 3 C, wax margin at least 5 C, no operating point below a formation boundary.

## 2. Public Synthetic Inputs

| Parameter | Value | Unit |
| --- | --- | --- |
| Operating temperature (hydrate check) | 10.0 | C |
| Hydrate equilibrium temperature | 8.0 | C |
| Operating temperature (wax check) | 33.0 | C |
| Wax appearance temperature | 30.0 | C |
| Minimum hydrate margin | 3.0 | C |
| Minimum wax margin | 5.0 | C |

The hydrate equilibrium and wax appearance temperatures are assumed to come from validated NeqSim calculations or public lab measurements.

## 3. Hydrate Margin Screening

Using `hydrate-margin-check`:

- Hydrate margin = 10.0 - 8.0 = 2.0 C
- Subcooling = 0.0 C (operating point is outside the hydrate region)
- Margin is positive but below the 3 C minimum, so the warning is `watch`.

## 4. Wax Margin Screening

Using `wax-margin-check`:

- Wax margin = 33.0 - 30.0 = 3.0 C
- Below wax appearance temperature: no
- Margin is positive but below the 5 C minimum, so the warning is `watch`.

## 5. Required Follow-Up Studies

- Validated NeqSim hydrate equilibrium calculation with fluid composition, water content, and inhibitor basis.
- Validated NeqSim wax appearance and deposition study with fluid composition.
- Thermal and steady-state hydraulic profile along the line.
- Inhibitor selection, insulation, or heating evaluation if margins remain low.

## 6. Assumptions and Limitations

- Screening indicators are educational placeholders, not validated results.
- Minimum margins are configurable public guidelines, not design rules.
- No deposition rate, pigging interval, or operating limit is established here.

## 7. Human Review

A qualified flow assurance engineer must review all results before any design or operating decision. This screening does not replace project assurance or design reviews.
