# Example: tie-in host screening for a Santos Basin pre-salt discovery

Public, synthetic example. Numbers are illustrative.

## Input

- Discovery: 26.70 S, 42.84 W (SIRGAS 2000), water depth about 2400 m, oil with high CO2.
- Radius: 250 km. Weights: default.

## Calls

```python
from anp_open_data import (fetch_layer, locate_installations, nearest_pipeline,
                           rank_tie_in_hosts)

target = (-42.84, -26.70)                  # (lon, lat)
bbox = (-44.6, -28.0, -41.0, -24.0)        # lon_min, lat_min, lon_max, lat_max
wells, wells_log = fetch_layer("wells", "raw", bbox=bbox)
pipes, pipes_log = fetch_layer("gas_outflow_pipelines", "raw", bbox=bbox)
# well_to_installation: (well name, installation) pairs from the ANP production statistics
hosts = locate_installations(wells, well_to_installation)   # median wellhead per installation
pipe = nearest_pipeline(target, pipes, top=1)[0]             # distance to the nearest segment
ranking = rank_tie_in_hosts(target, hosts + [
    {"name": "Gas export line (nearest)", "kind": "pipeline", "distance_km": pipe["distance_km"]},
    {"name": "Stand-alone FPSO", "kind": "standalone"},
], max_step_out_km=150.0)
```

Check the exact signatures in the `neqsim-anp-open-data` SKILL.md before use.

## Output (shape)

| Rank | Host | Kind | Distance (km) | Score | Notes |
|------|------|------|---------------|-------|-------|
| 1 | FPSO A | installation | 100 | 0.58 | ullage unknown (neutral) |
| 2 | Gas export line | pipeline | 105 | 0.52 | gas only |
| 3 | Stand-alone FPSO | standalone | 0 | 0.50 | reference |
| 4 | FPSO B | installation | 190 | 0.31 | beyond step-out limit |

## Read-across

A host 100 km away with unknown ullage is not a tie-in decision: the shortlist goes to the
tie-in screening, subsea layout and flow-assurance agents for the routed length, arrival
pressure, hydrate margin and host process fit, and the operator must confirm capacity.
