# Example: Installation Weather Screening on the Norwegian Continental Shelf

This example uses a public installation name and open weather APIs for
demonstration only.

## Input

- Installation: Troll A (Norwegian Continental Shelf)
- Time window: current conditions plus a 5-day forecast
- Requested variables: temperature, wind speed/direction/gust, cloud cover
- Consuming agent: `firewater-coverage-agent` (wind speed for monitor
  wind-drift screening) and a gas-dispersion stability-class estimate

## Expected Agent Actions

1. Resolve "Troll A" against the open Sodir facility register and report the
   resolved coordinates and provenance.
2. Read a 5-day forecast from Open-Meteo (worldwide model) with
   `wind_speed_unit=ms` and `temperature_unit=celsius`.
3. Cross-check the forecast against MET Norway's Nordic model and report the
   mean absolute temperature/wind deltas.
4. Estimate a screening Pasquill-Gifford stability class from the current
   wind speed and cloud cover.
5. Hand off the wind speed to `neqsim-firewater-deluge-design`'s
   `wind_speed_m_s` input and the stability class to
   `neqsim-gas-dispersion-distance-screening`'s `stability_class` input.

## Example Output Summary

- Resolved location: Troll A, source `sodir-facility-register`.
- 5-day forecast wind speed and temperature series, in m/s and °C.
- Forecast cross-check: mean absolute wind-speed delta between Open-Meteo and
  MET Norway for the requested window.
- Screening stability class (e.g. `D`) with a note that it is not a certified
  meteorological classification.
- Hand-off values ready for the fire-water and dispersion screening skills.

## Human Review

Any safety-critical or design use of this screening data requires qualified
engineering and meteorological review, and verification of any name-resolved
coordinates against an authoritative source (STID, P&ID, operator records).
