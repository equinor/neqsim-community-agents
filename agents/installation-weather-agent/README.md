# Installation Weather Agent

The Installation Weather Agent reads live, forecast and historical weather,
wind and sea-state data for an installation using the `neqsim-weather-data`
community skill. It resolves an installation by name or coordinates from
open, keyless APIs (Open-Meteo worldwide; MET Norway and the Sodir facility
register for the Norwegian Continental Shelf) and hands the data to the
screening agents and skills that need ambient conditions.

## Capabilities

- Resolve an installation name to coordinates (Sodir facility register on the
  NCS, Open-Meteo geocoding worldwide), or use supplied coordinates directly.
- Read current and forecast weather (up to ~16 days ahead) and historical
  weather (reanalysis back to 1940), worldwide.
- Read wave height/period and sea-surface temperature for offshore
  installations.
- Cross-check the worldwide forecast against MET Norway's higher-resolution
  Nordic model, especially useful on the Norwegian Continental Shelf.
- Estimate a screening Pasquill-Gifford stability class from wind speed, time
  of day and cloud cover.
- Explain limitations and hand off data to consuming agents in the shape they
  expect.

## Required Skill

- `neqsim-weather-data`

## Directory Contents

- [AGENT.md](AGENT.md) defines the human-readable agent standard.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains public example workflows.
- [prompts/](prompts/) contains reusable prompt examples.
- [tests/](tests/) contains validation notes for this agent.

## Human Review

Weather, marine and stability-class outputs are screening-level data
retrieval, not a certified met-ocean or meteorological study. Any
safety-critical or design use requires qualified engineering and
meteorological review.
