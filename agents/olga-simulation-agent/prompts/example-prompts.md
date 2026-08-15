# Example Prompts — OLGA Simulation Agent

The agent drives a licensed OLGA installation that is already on the machine.
Always state the case file and what the run must decide.

## Check the environment before committing to a run

```text
Which OLGA versions are installed on this machine, which one would you use for a transient run, and is the licence environment configured? Show me the engine path you would call and confirm it is the transient simulator and not the OLGA-S point model.
```

## Validate a case cheaply

```text
Rule-check C:\cases\riser\riser.genkey without simulating. Report the integration settings, the PVT tables it references, whether it will actually write .tpl and .ppl files, and any input error the rule check finds.
```

## Run and report

```text
Run C:\cases\riser\riser.genkey on 8 threads with the results in a separate output directory and a 4 hour wall-clock limit. Confirm the run reached a normal stop, then give me the arrival pressure and temperature trends with their units and the last output time they are reported at.
```

## Diagnose a failure

```text
This OLGA run exited with code 22 and no .tpl file. Tell me what that exit code means, which category of failure it is, whether the problem is the input or the numerics, and what to check first.
```

## Parameter sweep

```text
Sweep the simulation end time over 1 h, 6 h and 24 h for C:\cases\riser\riser.genkey. Write each variant next to the original so the PVT tables still resolve, rule-check each one, run each into its own output directory, and give me a table of exit status, run time and the final arrival pressure per variant.
```

## Cross-check against screening

```text
Before I trust this OLGA slugging result, cross-check it: classify the flow regime from the superficial velocities with the screening skill, compare that with the flow regime OLGA reports along the branch, and tell me whether the two agree. Treat any material disagreement as a finding.
```

## Hand over to NeqSim

```text
Take the arrival pressure, temperature and liquid rate trends from this OLGA run and turn them into a boundary condition for a NeqSim topside separation model. State the units, the output times, and which values are interpolated versus reported. Then tell me the hydrate margin at the coldest arrival temperature.
```

## Record the study

```text
Write the run record for this study: OLGA engine version, exact command line, exit code with its category and description, case file, output files produced, and the assumptions and limitations. Make it suitable for a task results.json and state the human review requirement.
```
