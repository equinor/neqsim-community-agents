# Brazil Offshore Infrastructure Agent Tests

Repository-level tests validate that this agent includes required files, metadata fields, documentation sections, examples and prompts.

The functions this agent calls are tested in the skill package `neqsim-anp-open-data` (`tests/test_wfs_tieins.py`: GeoServer reads with an injected getter, truncation flags, accent folding, installation placement, point-to-polyline distance and host ranking with a stand-alone reference) and in `neqsim-near-field-discoveries` (`tests/test_brazil.py`: well-result classification, candidate clustering, evaluation-plan and returned-block staging, aliases and sourced volumes; `tests/test_inventory_map.py`: ranking, clusters, GeoJSON and the map).
