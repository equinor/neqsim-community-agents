# Example Prompts

These prompts use only public or synthetic data. They illustrate how to ask the
Produced Water Scale Agent for early-stage produced-water scale screening.

## Build a brine from a preset or TDS

```text
Build a produced-water description from the high-barium formation-water preset using public synthetic data. Report the ion analysis, TDS, molality, ionic strength, and charge-balance error, and emit the NeqSim-ready electrolyte ion mapping.
```

```text
Build a brine from a TDS value of 95,000 mg/L using public assumptions. Show the resulting ion split, ionic strength, and the NeqSim-ready ion composition, and note that the split is a screening assumption.
```

## Single-water scale screening

```text
Screen a standalone formation water for scale using the produced-water-scale-screening skill. Report screening-level saturation indices and risk bands for barium sulfate, strontium sulfate, calcium sulfate, and calcium carbonate, and state the method and its limitations.
```

## Seawater/formation-water mixing incompatibility

```text
Sweep mixing fractions between a high-barium formation water and a seawater injection water using public synthetic presets. Report the worst-case barium-sulfate, strontium-sulfate, calcium-sulfate, and calcium-carbonate scale risk and the mixing fraction where it occurs.
```

## Corrosion flags

```text
From a produced water with 2 mol% CO2 and 50 ppm H2S, produce public corrosion flags (CO2 partial pressure indicator and sour-service indicator) and reference the relevant materials standards. Make clear this is screening only.
```

## Screening report outline

```text
Prepare a produced-water scale screening report outline that includes the objective, synthetic inputs, brine build, single-water scale results, mixing-incompatibility sweep, corrosion flags, required follow-up studies, assumptions, limitations, and the human review checklist.
```
