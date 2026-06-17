# Example Prompts

These prompts illustrate how to use the Flow Assurance Engineer Agent with public, synthetic, or approved data only. The agent performs early-stage screening and always requires qualified human review.

## Hydrate Margin Screening

```text
Screen a subsea operating point for hydrate margin. The operating temperature is 10 C and the hydrate equilibrium temperature from a validated NeqSim calculation is 8 C, with a minimum acceptable margin of 3 C. Report the hydrate margin, the subcooling, and the warning level, and recommend validated NeqSim hydrate workflows.
```

## Wax Margin Screening

```text
Screen a pipeline operating point for wax margin. The operating temperature is 33 C and the wax appearance temperature is 30 C, with a minimum acceptable margin of 5 C. Report the wax margin, whether the operating point is below the wax appearance temperature, and the warning level, and recommend validated NeqSim wax workflows.
```

## Combined Flow Assurance Screening

```text
Using public synthetic data, screen an operating point against both hydrate and wax margins. Flag any case that appears to run with insufficient margin, list the required follow-up studies, and prepare a flow assurance screening report outline with clear assumptions, limitations, and a human review checklist.
```

## Report Outline

```text
Prepare a transparent flow assurance screening report outline based on the hydrate-margin and wax-margin indicators. Separate facts, assumptions, and recommendations, and state that the results are educational placeholders that do not replace qualified flow assurance review.
```
