# Example: Offshore CO2 Pipeline to an Aquifer Injector

Public, synthetic case. The runnable version is
`skills/flow-assurance/neqsim-ccs-transport-chain/examples/ccs_pipeline_to_injector.py`
in NeqSim Community Skills.

## Input

- 95.5 mol % CO2 with N2 2 %, Ar 0.5 %, H2 0.5 %, CH4 about 1.5 %,
  20 ppm O2, 50 ppm(mol) water, SO2 10 ppmv, NOx 5 ppmv.
- 80 km, 0.38 m ID pipeline, 200 t/h, 150 bara and 35 C inlet, 4 C seabed,
  U = 5 W/m2K, MAOP 180 bara.
- Injector 1300 m, 0.157 m tubing, reservoir 120 bara, fracture 210 bara.

## Expected Agent Actions

1. State the limits used (10 bar single-phase margin, water factor 2).
2. Run `assess_transport_chain`.
3. Lead with the binding link, then the margins, depressurisation and
   impurity screen.
4. Suggest hand-offs and list the limitations.

## Expected Result (NeqSim 3.29.0)

- The stream stays single-phase along the pipeline; lowest margin 70.6 bar.
- Water solubility is about 42 times the delivered water.
- Blowdown to atmosphere passes the CO2 triple point: dry ice.
- Bottom-hole pressure about 247 bara exceeds the 210 bara fracture pressure:
  this is the binding link. Lower the arrival pressure or choke at the
  wellhead (and check the JT cooling) before injecting.
