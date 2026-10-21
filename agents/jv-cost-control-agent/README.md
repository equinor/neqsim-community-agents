# jv-cost-control-agent

Community coordinator for joint-venture cost control. It uses the
`neqsim-jv-cost-control-screening` skill to extract operator reports, prove them complete,
rank variances, reconcile reports and prepare operator questions. See [AGENT.md](AGENT.md).

Example request: "Load the August JIB and budget, compare year-to-date cost with the
Final Forecast on a 100 % and a 12 % basis, and list the questions for the operator."

Human review is always required; the agent never approves or disputes a cost.
