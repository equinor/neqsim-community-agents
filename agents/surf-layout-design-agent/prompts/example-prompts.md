# SURF Layout Design — example prompts

## Design a layout from a reservoir model

```text
Design a subsea layout for a shallow Barents Sea oil field on licence block 7324/8, in 400 m of water. The reservoir model gives 8 producers, 6 water injectors and 2 gas injectors, a 19 000 Sm3/day oil plateau rising to 28 500 Sm3/day of liquid, 20 000 Sm3/day of water injection and 0.63 MSm3/day of gas reinjection. Assume 4-slot templates and a weathervaning FPSO 2.5 km west of the field centre.

Place the drill centres on a field axis of 30 degrees, put the water injectors down-flank and the gas injectors up-dip, and use a round-trip-piggable dual production loop. Size every flowline and riser, and tell me which lines sit closest to the erosional limit. Give me the layout as GeoJSON plus a latitude/longitude map, and the quantity take-off for a SURF cost estimate.
```

## Compare flowline architectures

```text
For the same field, compare a dual production loop, one dedicated flowline per drill centre, and a daisy chain. Report the total flowline length, the selected sizes and the pigging consequence of each, and say which one you would carry forward and why.
```

## Plan the open data before designing

```text
Before you design anything, list the open bathymetry, licence-block and met-ocean data I should pull for a field in block 7324/8: which source, what it gives me, under which licence, and the attribution I have to reproduce on the map. Do not fetch anything — just give me the request plan.
```

## Put an existing layout on the map

```text
I have well and manifold coordinates from a public map. Georeference them, place a host 3 km to the south-west, route and size the flowlines for 25 000 Sm3/day of liquid at 860 kg/m3, and hand me the GeoJSON. Then screen the step-outs and tell me what a subsea engineer must check.
```

## Size only

```text
What nominal flowline size do I need for 0.33 m3/s of liquid at 850 kg/m3 if I split it over two loops and want to stay under 3 m/s? Show the erosional-velocity check.
```
