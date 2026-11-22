# Fluid Commingling Agent Tests

Repository-level tests validate the required files, metadata, documentation
sections, examples and prompts.

The calculation is tested in the `neqsim-fluid-commingling-compatibility` skill:
analytic-evaluator tests of every finding, and NeqSim integration tests that
check the bubble point rises and the refractive index falls with condensate
share, the minimum sits at the bubble point, and the onset crossing is flagged.
The numbers in `examples/condensate-into-asphaltenic-host.md` were produced with
NeqSim 3.29.0 by the skill's example script.
