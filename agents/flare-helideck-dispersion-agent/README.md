# Flare-Helideck Dispersion Agent

The Flare-Helideck Dispersion Agent coordinates a screening study of unignited flare-tip gas (rated PSV flow or blowdown peak) reaching a helideck and its approach and departure paths. It chains a frozen basis, wind statistics, release rates, the `neqsim-flare-helideck-dispersion` toolkit, an independent review checklist, house-style figures with a `results.json` fragment, and a CFD hand-off.

It is a draft (version 0.1.0) coordinator. It orchestrates community skills and agents and contains no engineering method of its own. Results are conditional on a release and screening level only.

## Capabilities

- Freeze and document the geometry, flight paths and acceptance criteria with their sources
- Obtain wind statistics through the installation weather agent and build the joint direction x speed table
- Establish release rates from PSV rated capacity (API 520) and blowdown peak flows
- Report peak % LFL and wind-weighted conditional exceedance of 10 % and 20 % LFL on the helideck, the into-wind path and any flight path
- Report the tip-inclination scan, tornado and a seeded Monte Carlo
- Apply an independent review checklist before reporting
- Produce page-width figures and a `results.json` fragment
- Prepare a CFD hand-off of the worst conditions

## Guardrails

- Conditional on a release; no annual frequency without a flame-out frequency
- Flight paths are assumptions unless supplied
- The helideck tip-inclination sensitivity is always reported
- Unverified source data are flagged for human review

## Required Skills

- `neqsim-flare-helideck-dispersion`
- `neqsim-weather-data`
- `neqsim-psv-orifice-screening`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public worked example.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

All results are screening-level and conditional. They require qualified safety engineering, helideck operations and project review before any design or operational use. This agent does not replace a quantitative risk assessment, CFD dispersion study, relief and flare design, or the helideck operations manual.
