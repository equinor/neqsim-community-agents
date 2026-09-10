# firewater-coverage-agent

Screens fire-water and deluge coverage for a process area: required application rate and demand,
blanket area coverage against dedicated object protection, deluge nozzle-net sizing, fire-monitor
feasibility with wind drift, and the active-versus-passive substitution rules.

See [AGENT.md](AGENT.md) for the full description and [agent.yaml](agent.yaml) for the manifest.

## Required skills

- `neqsim-firewater-deluge-design`
- `neqsim-safety-function-coverage-screening`
- `neqsim-jet-fire-radiation-screening`

## Human review

Required. This agent produces screening indicators to scope a study; it does not replace
fire-water network hydraulics, a deluge coverage test, or a qualified technical-safety review.
