# Compressor Anti-Surge Screening Checklist

This example uses public, synthetic data only. It illustrates a transparent
anti-surge recycle setup screening for a centrifugal compressor.

## 1. Screening Objective

- Confirm the operating point and whether anti-surge recycle protection is needed.
- Decide whether a compressor chart must be generated (no vendor chart available).

## 2. Input Data (synthetic)

- Design speed: 8000 rpm
- Number of speed lines for chart generation: 5
- Suction (inlet) volumetric flow: 4200 m3/h
- Surge flow at operating head: 5000 m3/h
- Vendor compressor chart available: no
- Existing recycle flow: 0 m3/h
- Suction pressure / discharge pressure: known operating values

## 3. Chart Generation (when no vendor chart)

- Run the compressor at the design point first.
- Generate a NeqSim chart with surge and stonewall curves
  (`generateCompressorChart("normal curves", 5)`).
- Read the surge flow (`getSurgeFlowRate()`) and distance to surge
  (`getDistanceToSurge()`).
- Record that the generated chart is a model estimate, not a vendor map.

## 4. Recycle Screening

- Estimate the surge margin `(inlet_flow - surge_flow) / surge_flow`.
- Estimate the recommended recycle flow (proportional, capped per iteration).
- Record the total suction flow and warning level (`ok`, `recycle`, `surge`).

## 5. Anti-Surge Topology

- Surge curve active on the compressor chart.
- Low-flow placeholder recycle stream into suction.
- Discharge splitter (forward branch 0, recycle branch 1).
- Anti-surge `Calculator` named starting with `"anti surge calculator"`.
- Anti-surge valve on the recycle branch, dropping to suction pressure.
- `Recycle` unit closing the loop into the placeholder suction stream.

## 6. Required Follow-Up Studies

- Validated compressor performance and surge-margin analysis.
- Anti-surge controller design, tuning, and recycle valve sizing.
- Dynamic surge / transient and ESD analysis.

## 7. Assumptions and Limitations

- Inputs are synthetic and for screening only.
- Recycle estimates and generated charts are educational placeholders.
- Results require qualified human review before any design or operating use.

## 8. Human Review

- Qualified process engineering and rotating-equipment review is required.
- This screening does not replace anti-surge control design or project assurance.
