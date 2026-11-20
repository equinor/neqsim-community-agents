# Well Trajectory and Anti-Collision Agent Tests

Repository-level tests check that this agent includes the required files, metadata fields,
documentation sections, examples and prompts.

The calculation tests live with the skill in `neqsim-community-skills`
(`skills/subsurface/neqsim-well-trajectory-anticollision/tests`). They cover:

- minimum curvature against an analytic arc;
- the curve-hold target hit;
- the unreachable-target error;
- the SF formula;
- parallel wells;
- parent exit;
- target pull-back;
- the error-model check;
- slot occupancy.
