# Continuous Task Improvement Agent Tests

Repository-level tests validate that this agent includes required files, metadata
fields, documentation sections, examples, and prompts.

The behaviour the agent relies on is tested where it is implemented:

- `neqsim/devtools/test_neqsim_living_tasks.py` — living scaffold never overwrites,
  cycles resume and degrade, backtest finds the three reference faults with no
  false alarms, solve reaches `goal_met` and `infeasible`, promotion archives the baseline.
- `neqsim-community-skills/skills/process/neqsim-continuous-improvement-toolkit/tests`
  — tagreader adapter, Bayesian optimisation, EnKF, identifiability.
- `neqsim` JUnit `ImprovementCycleTest` — Java drift monitor, baseline comparator, cycle.
