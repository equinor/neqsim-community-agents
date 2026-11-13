# Umbilical Design Screening Example

Public synthetic example of the Umbilical Design Agent. Educational only; it does not replace vendor design or qualified review.

## 1. Inputs

| Parameter | Value |
| --- | --- |
| Length / water depth | 15 km / 100 m |
| Hydraulic lines | 9.5 mm ID at 345 bar; 6.35 mm ID at 690 bar |
| Chemical lines | MEG 25.4 mm at 0.5 m3/h; methanol 12.7 mm at 0.3 m3/h; scale inhibitor 12.7 mm at 0.05 m3/h (all 345 bar) |
| Power | 3 cores, 16 mm2, 3.3 kV, 50 kW |
| Fibre | 12 fibres |

All other values are screening defaults and are listed in the hand-off.

## 2. Result (from the NeqSim fixture of the skill)

- Overall diameter 84 mm, one armour layer, 11.3 kg/m in air (empty), 6.5 kg/m in seawater (filled).
- All checks pass, including the friction budget: MEG about 100 bar and methanol about 75 bar at design flow, below half of 345 bar.
- Hydraulic lines need about 6 to 15 min for 90 % of a pressure step at the template; the acoustic transit is about 10 s. Compare with the valve response requirement.
- Power cable: charging current 1.4 A at 15 km; the voltage drop depends strongly on the conductor size for such a small load.

## 3. Figures

Written by `python -m umbilical_design render` into `figures/`: `fig1_cross_section`, `fig2_hydraulics`, `fig3_mechanical`, `fig4_electrical`, `fig5_design_checks`, `fig6_umbilical_on_a_page`.

## 4. Open items

J-tube pull-in, topside hang-off, host hydraulic power unit and power interface, spare tubes, dynamic section, vendor data.
