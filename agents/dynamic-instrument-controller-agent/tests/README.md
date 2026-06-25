# Dynamic Instrument Controller Agent Tests

Validation notes for this agent:

- `AGENT.md` includes all required repository sections.
- `agent.yaml` declares `dynamic-instrument-controller-setup` as a required skill.
- Examples use public synthetic data only.
- Outputs state that human review is required and that the agent does not replace controller tuning or control-system design.

Suggested harness check:

1. Load `agent.yaml`.
2. Install `neqsim-dynamic-instrument-controller-setup` from the community skills repository.
3. Run the public level-controller example through the skill helper.
4. Confirm out-of-range setpoints and questionable controller actions are flagged.
