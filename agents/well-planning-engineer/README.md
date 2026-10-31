# Well Planning Engineer

Coordinator for integrated well planning: oil, gas-condensate, water-injection and gas-injection wells, onshore, platform or subsea. It runs the reproducible workflow of the skill `neqsim-integrated-well-planning` (planning basis, registers, reservoir-well-facility chain, operating envelope, barrier schematics, alternatives, drawings, report) and coordinates the specialist community agents through versioned `iwp_*.v1` hand-offs.

It supersedes `well-design-study-agent`, which stays available as a deprecated drilling-focused entry point; the drilling and casing design module `neqsim-well-design-study` is now part of this workflow.

The agent does not replace the well engineer, the drilling, geomechanics, cementing, completion or integrity specialists, or the company process. It states which calculations are implemented, which are screening and which were not performed, and makes no compliance statement. Human review is required.

Files: [`AGENT.md`](AGENT.md), [`agent.yaml`](agent.yaml), [`prompts/`](prompts), [`workflows/`](workflows), [`examples/`](examples), [`tests/`](tests).
