# Example Workflow: Factor-Driven Fluid Characterization

This public example shows how the Fluid Characterization Agent chains its four
skills. All data are synthetic.

## 1. Composition quality (`fluid-quality-check`)

Review a reference gas-condensate composition: check the mole fraction total,
flag missing components, and note water/CO2/H2S presence.

## 2. Pseudocomponent split (`pseudocomponent-split-characterization`)

Split the C7+ plus fraction (z_plus = 0.05, M+ = 220 g/mol) into 4 pseudocomponents
with a Whitson gamma split factor `alpha`:

```python
import math
from pseudocomponent_split import gamma_mole_split

split = gamma_mole_split(0.05, 220.0, [90.0, 140.0, 200.0, 300.0, math.inf], alpha=1.0, eta=90.0)
```

## 3. Calibrate the factor (`pvt-regression-characterization-factor`)

Regress `alpha` against a measured saturation pressure and stock-tank-oil density:

```python
from pvt_regression import RegressionTarget, regress_characterization_factor

targets = [
    RegressionTarget("p_sat", 248.0, weight=2.0),
    RegressionTarget("rho_STO", 832.0, weight=1.0),
]
result = regress_characterization_factor(forward_model, targets, low=0.6, high=3.0)
```

Here `forward_model(alpha)` builds the fluid with that split factor and returns
the predicted saturation pressure and density (via NeqSim for design-grade work).

## 4. Generate and allocate (`reference-fluid-synthetic-generation`)

Generate low/base/high cases and blend wells by molar rate:

```python
from reference_fluid import generate_fluid_cases, blend_compositions

cases = generate_fluid_cases([0.8, result.factor, 1.2], build_from_reference)
field = blend_compositions([(3200.0, well_1), (1500.0, well_2), (900.0, well_3)])
```

## 5. Hand off and review

Hand the calibrated fluid(s) to a NeqSim process model and record assumptions,
residuals, allocation weights, and the required qualified human review.
