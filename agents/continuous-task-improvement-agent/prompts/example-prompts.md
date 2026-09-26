# Example Prompts

## Make a Finished Task Living

```text
Use the Continuous Task Improvement Agent on my task folder. Make it living from
the attached Word brief, draft goal.yaml from the brief's success measure, and
list what I must confirm before any solve loop runs.
```

## Prove the Monitoring Before Scheduling

```text
Backtest the living task over the last year of archived data. The known events
are a heat-exchanger cleaning in March and a meter recalibration in June. Report
the detection delay for each and the false alarms per month, and tune the drift
floors if needed. Do not schedule anything yet.
```

## Solve Until Improvement Is Marginal

```text
Run the solve loop until converged. Report the stop state, the best validated
value, the recent gains against the tolerance, and the next best action with its
expected improvement. Include assumptions and human review requirements.
```

## Triage a Triggered Cycle

```text
Triage the latest cycle. For every trigger say whether it is a data fault, a model
mismatch, a real plant change or a new opportunity, and name the one check that
would tell them apart.
```
