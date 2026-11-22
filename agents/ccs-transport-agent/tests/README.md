# CCS Transport Agent Tests

Repository-level tests validate the required files, metadata, documentation
sections, examples and prompts.

The calculation is tested in the `neqsim-ccs-transport-chain` skill: input
validation and findings logic without Java, and NeqSim integration tests of
the two-phase boundary against the bubble point, water solubility, the
pipeline profile, depressurisation and the injection well. The numbers in
`examples/pipeline-to-aquifer.md` were produced with NeqSim 3.29.0 by the
skill's example script.
