# Hydrate Screening Agent

The Hydrate Screening Agent assists with preliminary hydrate risk assessments using NeqSim and the `hydrate-screening` community skill.

It helps engineers review pressure and temperature conditions, identify missing data, explain assumptions, and recommend further analysis. It is intended for screening and engineering assistance only.

## Capabilities

- Review pressure and temperature conditions
- Evaluate screening-level hydrate risk
- Explain assumptions
- Recommend further analysis
- Prepare preliminary risk notes
- Size a MEG loop with NeqSim: lean MEG rate to a hydrate margin,
  regeneration duty, salt build-up and reclaimer slipstream

## Required Skills

- `hydrate-screening` (`neqsim-hydrate-screening`)
- `neqsim-meg-loop`

## MEG loop: how to use

Give the well stream (without MEG), the water forecast and the regeneration
basis:

```text
@hydrate-screening-agent Size MEG for this gas tie-back: 8 MSm3/d,
85 % methane, saturated with water, 20 m3/d formation water at 60 g/L TDS.
Shut-in 150 bara at 4 C seabed, 3 C margin, 90 wt % lean MEG, 30 %
reclaimer slipstream, arrival 60 bara and 15 C.
```

Public example result (NeqSim 3.29.0): 2774 kg/h lean MEG, rich MEG
49.2 wt % (Hammerschmidt 50.4), reboiler 143.7 C and 1705 kW, and a high
salt finding because at least 36 % slipstream is needed. See
[examples/meg-loop-gas-tieback.md](examples/meg-loop-gas-tieback.md).

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Hydrate screening outputs require qualified flow assurance review before use in design, operations, chemical strategy, or safety-related decisions.