# Well Trajectory and Anti-Collision Agent

The Well Trajectory and Anti-Collision Agent plans a screening-level 3D well path and checks it against
existing wellbores with the ISCWSA separation-factor rule. It uses the community skill
`neqsim-well-trajectory-anticollision` and adds `neqsim-erd-reach-screening` for long step-outs.

## Capabilities

- Check whether a slot is free or needs a slot-recovery sidetrack
- Plan a curve-hold path from a kick-off or a sidetrack tie-in
- Attach position uncertainty (inherited at the tie-in, plus a reduced MWD model)
- Compute the separation factor against every offset and report the governing well
- Report the parent-bore exit depth for sidetracks
- Find the target pull-back that clears a separation-factor limit
- Run tie-in and DLS sensitivity, plus an ERD reach check

## Required Skills

- `neqsim-well-trajectory-anticollision`
- `neqsim-erd-reach-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Results are screening values. A qualified directional-drilling engineer must review them, and the
official directional-planning system must run the anti-collision with the operator's error models and
separation rule before the well is used for any decision.
