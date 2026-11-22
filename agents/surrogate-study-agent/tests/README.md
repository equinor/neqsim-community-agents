# Surrogate Study Agent Tests

Repository-level tests validate the required files, metadata, documentation
sections, examples and prompts.

The calculation is tested in the `neqsim-active-learning-surrogate` skill:
Gaussian-process and learner tests on analytic functions (convergence,
boundary learning, exceedance probability against brute force, failure
handling, JSON round trip) and a NeqSim integration test that learns a real
flowsheet boundary and validates it against fresh NeqSim runs. The numbers in
`examples/host-compressor-driver-limit.md` were produced with NeqSim 3.29.0 by
the skill's example script.
