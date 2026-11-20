# Example Prompts - Reservoir H2S Agent

Use measured data with stated basis. Keep company data out of public repositories.

## Prospect without a test

```text
Estimate H2S in the test gas of a gas-condensate prospect in the Garn Formation at 150 C, 500 bara and 3 mol % CO2, position 64.9 N 6.9 E, using my registry h2s_registry.json and wells.csv. Give P10/P50/P90, the probability of sour service and a report.
```

## Prospect known by depth only

```text
A prospect at 3 100 m in a Middle Jurassic sandstone has no temperature or CO2 estimate yet. My temperature trend is 15 C plus 33 C per km, plus or minus 9 C. What H2S should be carried, and which measurement would narrow the range most?
```

## Discovery with a drill stem test

```text
The discovery well read 6, 8 and 9 ppm H2S in the separator gas at 30 bara and 45 C. Reservoir is 136 C, 420 bara, 2.5 mol % CO2. Is that consistent with the mineral buffer, and what should the design value be?
```

## Calibration

```text
Calibrate the H2S buffer on this table of wells (measured H2S in test gas, reservoir temperature, pressure, CO2, formation) and report the offset and scatter per depositional setting and the share of wells inside the P10 to P90 range with each well left out.
```
