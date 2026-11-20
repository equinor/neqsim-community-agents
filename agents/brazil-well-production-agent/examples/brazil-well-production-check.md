# Example: December 2023 national check and a field series from ANP by-well files

Public data. Figures are from the ANP files `2023_12_producao_Mar.csv`, `_PreSal.csv` and `_Terra.csv`, read on 2026-11-02.

## Calls

```python
from anp_well_production import (read_zip, read_table_bytes, normalize, merge_environments,
                                 aggregate, completeness, expected_latest_period)

by_env = {}
for name, raw in read_zip(zip_path).items():            # zip_path: downloaded producao-12.zip
    headers, rows, meta = read_table_bytes(raw)
    by_env[name.rsplit("_", 1)[-1][:-4]] = normalize(headers, rows, source=name)

records, report = merge_environments(by_env)            # PreSal is a subset of Mar
assert report["presalt_is_subset"]                      # 364 of 364 pre-salt rows are in Mar
national = aggregate(records, by=())[0]
fields = aggregate(records, by=("field",))
```

## What the check showed

- Oil plus condensate about 3.59 million bbl/d, gas about 157 million m3/d, 6,546 wells with production; pre-salt about 2.74 million bbl/d.
- Adding the pre-salt file to the offshore file raises `ValueError` in `aggregate` (duplicate rows).
- A well can appear in several fields (for example onshore wells in Potiguar); `well_history` sums them.
- The by-well rate file and the by-well volume file agree for every offshore well (`reconcile` returns an empty list).
- Reported composition for Mero shows oxygen 2.6 %: `fluid_basis` warns and the composition is checked against the gross calorific value before use.

## Hand-offs

- Decline series to `fit_arps_decline`; label as screening.
- Fluid basis to the `fluid-characterization-agent`; `readiness("material_balance")` lists the missing pressure and PVT data.
