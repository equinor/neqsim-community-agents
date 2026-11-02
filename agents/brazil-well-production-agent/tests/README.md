# Brazil Well Production Agent Tests

Repository-level tests validate that this agent includes required files, metadata fields, documentation sections, examples and prompts.

The functions this agent calls are tested in the skill package `neqsim-anp-well-production-history` (`tests/test_anp_well_production.py`): Brazilian number and period parsing, the four ANP file families from public row excerpts, damaged and mixed-encoding files, pre-salt/offshore merge and duplicate guard, split wells, publication lag and gaps, well data flags, decline-series input, rate/volume reconciliation, fluid basis and the download cache. The same code was run on the full December 2023 ANP files (3.59 million bbl/d oil plus condensate, 364 of 364 pre-salt rows in the offshore file, zero rate/volume mismatches).
