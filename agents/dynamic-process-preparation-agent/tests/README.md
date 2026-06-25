# Dynamic Process Preparation Agent Tests

Validation notes for this agent:

- `AGENT.md` includes all required repository sections.
- `agent.yaml` declares `dynamic-process-preparation` as a required skill.
- Examples use public synthetic data only.
- Outputs state that human review is required and that the agent does not replace dynamic simulation validation or mechanical design.

Suggested harness check:

1. Load `agent.yaml`.
2. Install `neqsim-dynamic-process-preparation` from the community skills repository.
3. Run the public separator-train example through the skill helper.
4. Confirm missing geometry and missing total-time inputs are flagged.
