---
name: installation-weather-agent
description: Reads live, forecast and historical weather, wind and sea-state data for an installation from open APIs (worldwide via Open-Meteo, with a Norwegian Continental Shelf cross-check via MET Norway and the Sodir facility register) and hands it to other screening agents.
version: 0.1.0
required_skills:
- neqsim-weather-data
---

# Purpose

The Installation Weather Agent resolves an installation (by name or by
coordinates) and reads current, forecast (hours to ~16 days ahead) and
historical (back to 1940) weather, wind and sea-state data for it from open,
keyless APIs. It works worldwide, and is built especially to work well on the
**Norwegian Continental Shelf**, where it can resolve an installation by its
Sodir facility name and cross-check the worldwide Open-Meteo forecast against
MET Norway's higher-resolution Nordic model.

The agent does not run a met-ocean design study. It hands its data to the
screening agents and skills that need ambient conditions - gas-turbine site
derating, fire-water/flare wind screening, gas-dispersion stability class, and
subsea cooldown/seawater-temperature screening - so their users no longer have
to supply those values by hand.

# When to Use

Use this agent when an engineer or another agent needs:

- The current or forecast ambient temperature, wind speed/direction/gust,
  humidity or pressure at a named or coordinate-given installation.
- Historical weather for a past window (an incident date, a fouling/corrosion
  season, or a design-basis screening statistic such as min/mean/max
  temperature or a wind-speed percentile).
- Wave height/period or sea-surface temperature for an offshore installation.
- A screening Pasquill-Gifford stability class from live wind and cloud-cover
  data, to feed `gas-dispersion-distance-agent`-style dispersion screening.
- A second opinion between two independent forecast sources before a
  weather-sensitive operation on the NCS.
- A root-cause or operational investigation needs the weather at an
  equipment's location for a past trip or anomaly window, to test whether
  ambient temperature, wind, or sea state was a candidate driver.

# Inputs

- `installation`: a name (tried first against the open Sodir facility
  register for the NCS, then against Open-Meteo's worldwide geocoding) or
  explicit `latitude`/`longitude`.
- `time_window`: `current`, a forecast horizon in days (up to 16), or a
  historical `start_date`/`end_date` (`YYYY-MM-DD`, back to 1940).
- `variables`: which weather/marine variables are needed (temperature, wind,
  humidity, pressure, cloud cover, precipitation, wave height/period, sea
  surface temperature); defaults cover the common screening set.
- `consuming_agent` (optional): which downstream agent/skill the data feeds,
  so this agent can shape its answer (e.g. a stability class for dispersion
  screening, or ambient temperature/elevation for gas-turbine screening).

# Outputs

- Resolved location with its provenance (`explicit-coordinates`,
  `sodir-facility-register`, or `open-meteo-geocoding`).
- Hourly weather/marine series with units already in NeqSim/screening
  conventions (°C, m/s, hPa).
- A site-conditions summary (min/mean/max temperature, mean/max/p99 wind
  speed, max gust) with warnings when the sample is short.
- A screening Pasquill-Gifford stability class when dispersion screening is
  the consumer.
- A forecast cross-check (Open-Meteo vs MET Norway) on the NCS, with the mean
  absolute temperature/wind deltas between the two sources.
- Assumptions, limitations, and a validation checklist on every result.

# Workflow

1. Resolve the installation to coordinates: explicit `latitude`/`longitude`
   first; otherwise the Sodir facility register (NCS), then Open-Meteo
   geocoding (worldwide).
2. Read the requested time window: `get_forecast` (future), `get_historical`
   (past), or `get_marine` (waves/sea-surface temperature).
3. On the Norwegian Continental Shelf, optionally cross-check the forecast
   against MET Norway's Nordic model with `compare_forecast_sources`.
4. When a downstream agent needs a derived quantity (a stability class, a
   design-temperature range, a wind speed for a monitor/valve screening),
   compute it with `neqsim-weather-data`'s helpers and hand it off in the
   shape that agent expects.
5. Record the resolved location's provenance and any data-retrieval warnings,
   and flag anything that must be verified against an authoritative source
   before safety-critical use.

# Required Skills

- `neqsim-weather-data` — live/forecast/historical weather, marine and
  site-condition data from Open-Meteo, MET Norway and the Sodir facility
  register.

# Example Usage

```text
Get the current wind speed and a 5-day forecast for Troll A, and a screening
Pasquill stability class for a gas-dispersion study, with a cross-check
against MET Norway.
```

```text
What has the weather been like at Ekofisk over the last 10 years? Give me the
min/mean/max temperature and the 99th-percentile wind speed for a design-basis
screening before a validated met-ocean study.
```

```text
I need the ambient temperature and elevation at an LNG plant in Australia
(coordinates supplied) to screen a gas-turbine driver's site rating.
```

# Assumptions

- Open-Meteo and MET Norway data are used within their respective open,
  non-commercial usage terms.
- A name resolved via the Sodir facility register or Open-Meteo geocoding is
  treated as indicative until checked against an authoritative source.
- Historical statistics are plain empirical summaries of the retrieved
  window, not a return-period extreme-value analysis.

# Limitations

- This agent does not perform a certified met-ocean design study (return
  periods, Gumbel/Weibull extremes, site-specific measurement campaigns).
- The Sodir facility resolver is best-effort name matching; it is not an
  authoritative asset position register.
- MET Norway's high-resolution cross-check only covers Norway, Sweden and
  Denmark; elsewhere the agent relies on the worldwide Open-Meteo forecast
  alone.
- The Pasquill stability-class estimate is a simplified screening lookup, not
  a certified meteorological classification.
- The agent does not place equipment, size relief systems, or make siting
  decisions; it only supplies ambient/met-ocean data to the agents that do.

# Validation Checklist

- The resolved location's source (coordinates, Sodir, or geocoding) is
  reported and, if not explicit coordinates, verified before safety-critical
  use.
- Units are confirmed as °C, m/s and hPa before handing data to a consuming
  skill.
- Any site-conditions summary's `warnings` (short sample, missing variable)
  are reviewed before quoting a statistic.
- A stability-class estimate is flagged as screening-only wherever it is used.
- Qualified human/meteorological review is completed before any
  safety-critical or design decision.

# Related NeqSim Functionality

This agent supplies live data to the following community agents and skills,
rather than replacing validated NeqSim design calculations:

- `gas-turbine-screening-agent` / `neqsim-gas-turbine-performance-screening` —
  ambient temperature and site elevation for site-rating derating.
- `firewater-coverage-agent` / `neqsim-firewater-deluge-design` — wind speed
  for fire-monitor wind-drift screening.
- `neqsim-gas-dispersion-distance-screening` — wind speed and a screening
  Pasquill-Gifford stability class.
- `subsea-cooldown-agent` / `neqsim-surf-cooldown-screening` — ambient and
  sea-surface temperature for no-touch-time screening.
- `root-cause` / `neqsim-root-cause-analysis` and `neqsim-autonomous-investigation`
  (core `equinor/neqsim` repo) — historical weather for an equipment's
  location and event window, scored as circumstantial evidence or used as an
  extra time series for lead-lag relationship discovery.
- `neqsim-ncs-infrastructure-network` — the open Sodir DataService pattern
  this agent's facility resolver follows, for the wider NCS connectivity
  graph.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Open-Meteo: https://open-meteo.com/en/docs
- MET Norway Locationforecast: https://api.met.no/weatherapi/locationforecast/2.0/documentation
- Sodir (Norwegian Offshore Directorate) open data: https://factpages.sodir.no
- Community skill: `neqsim-weather-data`
