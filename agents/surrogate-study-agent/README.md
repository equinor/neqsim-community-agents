# Surrogate Study Agent

Makes slow NeqSim studies fast. The agent builds an active-learning surrogate
of a NeqSim flowsheet, running NeqSim only where the surrogate is least
certain. It validates the surrogate against fresh NeqSim runs, then uses it for
the expensive part of the study.

## Capabilities

- Find where a capacity or specification limit binds, e.g. the maximum
  tie-in rate before a compressor driver, separator or export spec limits
- Probability of exceeding a limit over an uncertain operating envelope
- P10/P50/P90, tornado and Sobol sensitivity on a slow flowsheet, through the
  uncertainty-quantification skill
- Operating-envelope maps and fast proxies for dashboards
- Carries on when some NeqSim runs fail to converge, and reports where

In the bundled example, 21 NeqSim runs locate a compressor's 6.5 MW limit over
three uncertain inputs. The exceedance probability then comes from 20,000
cases (about 2.8 h of direct NeqSim time) in 0.1 s.

## How to Use

1. Install the agent and its skills (see the
   [installation guide](../../docs/installation-guide.md)):

   ```bash
   neqsim agent install surrogate-study-agent --vscode
   ```

2. Have a NeqSim model that can be run as a function of the study inputs:
   either your own Python function or a flowsheet another agent built
   (`@debottlenecking-agent`, `@tie-in-screening-agent`). The agent wraps it so
   that every call builds a fresh process and fails loudly on non-convergence.

3. In Copilot Chat, call `@surrogate-study-agent` with:

   | Input | Example |
   | --- | --- |
   | The model, or where it is | `host_model.py`, or "the flowsheet from the debottlenecking study" |
   | Inputs and their ranges | tie-in rate 0-60 t/h, separator 30-70 bara, inlet 30-70 C |
   | The question | a limit (output + threshold), or the outputs to learn everywhere |
   | Uncertainty, if wanted | tie-in rate triangular 10/35/55 t/h, separator 40-60 bara |
   | Budget | 40 NeqSim runs (default 60) |

4. Example prompt:

   ```text
   @surrogate-study-agent Using host_model.py, find where the export compressor
   exceeds its 6.5 MW driver over tie-in rate 0-60 t/h, separator pressure
   30-70 bara and inlet temperature 30-70 C. Give the maximum tie-in rate at
   40 bara / 60 C, confirm it with a direct NeqSim run, and the probability of
   exceeding 6.5 MW for tie-in rate triangular 10/35/55 t/h, separator 40-60 bara
   and inlet 35-60 C.
   ```

5. What you get back: number of NeqSim runs and failures, the learning curve,
   the validation against fresh NeqSim runs, the limit boundary and maximum
   feasible rate (best estimate and conservative), the exceedance probability
   or P10/P50/P90, the saved surrogate (JSON), assumptions and a validation
   checklist. Example output is in
   [examples/host-compressor-driver-limit.md](examples/host-compressor-driver-limit.md).

More prompts are in [prompts/example-prompts.md](prompts/example-prompts.md).

## Good to Know

- Ranges bound the surrogate. The agent checks every prediction it uses with
  `extrapolating()` and does not report values outside the trained ranges.
- Below about 10 ms per NeqSim run, the agent runs the study on NeqSim
  directly instead.
- Discontinuous responses (a phase disappearing, control logic) need split
  ranges or a boundary study.
- The decision value is always confirmed with a direct NeqSim run.

## Required Skills

- `neqsim-active-learning-surrogate`
- `neqsim-uncertainty-quantification`

## Directory Contents

- [AGENT.md](AGENT.md) defines the agent: purpose, workflow, limitations.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public worked example.
- [prompts/](prompts/) contains reusable prompts.
- [tests/](tests/) describes how the agent and its skill are tested.

## Human Review

A surrogate inherits every error of the NeqSim model behind it and is valid
only inside the trained ranges. Results need qualified review, and the final
design point needs a direct NeqSim run and vendor data, before any design or
operating decision.
