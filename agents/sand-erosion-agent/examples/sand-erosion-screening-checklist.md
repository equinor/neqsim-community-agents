# Sand Erosion Screening Checklist (Example)

This public example shows how the Sand Erosion Agent screens a sand-producing line for erosional velocity and remaining wall life using synthetic data. It is educational only and does not replace qualified integrity review.

## 1. Screening Objective

- Confirm whether a subsea flowline appears to run below its erosional velocity and keeps enough remaining wall life over the design life.
- Decision criteria: velocity ratio at or below 1.0 and remaining wall life at least equal to the design life.

## 2. Public Synthetic Inputs

| Parameter | Value | Unit |
| --- | --- | --- |
| Flow velocity | 12.0 | m/s |
| Mixture density | 120.0 | kg/m3 |
| Pipe diameter | 0.25 | m |
| Wall thickness | 12.7 | mm |
| Sand rate | 50.0 | kg/day |
| Corrosion allowance | 3.0 | mm |
| Design life | 25.0 | years |

The mixture density and flow velocity are assumed to come from a validated NeqSim multiphase pipe-flow calculation. The sand rate is assumed to come from a sand-management estimate.

## 3. Erosional Velocity and Remaining Wall Life Screening

Using `sand-erosion-screening`:

- The erosional velocity is estimated from the public C-factor relation `c_factor / sqrt(density)`.
- The velocity ratio is the flow velocity divided by the erosional velocity.
- A screening erosion rate is estimated from a transparent placeholder coefficient, the sand rate, the velocity, and the diameter.
- The cumulative wall loss over the design life is compared with the usable wall after the corrosion allowance.
- For this heavy-sand case the erosion rate is high and the remaining wall life is well below the design life, so the verdict is `high`.

## 4. Recommended Validated Workflows

- Confirm the erosion rate with `neqsim.pvtsimulation.flowassurance.ErosionPredictionCalculator`.
- Confirm the velocity and density inputs with `neqsim.process.equipment.pipeline.PipeBeggsAndBrills`.
- Run a validated DNV RP O501 erosion calculation and set an inspection interval for design-grade work.

## 5. Assumptions and Limitations

- The screening erosion coefficient is a transparent public placeholder, not a DNV RP O501 constant.
- The result is an educational placeholder, not a validated erosion result.
- Erosion geometry factors, bends, local hot spots, and corrosion coupling are not modelled.

## 6. Human Review

A qualified human review is required before any design or operating decision. This screening does not replace validated erosion calculation, sand-management approval, or qualified integrity engineering.
