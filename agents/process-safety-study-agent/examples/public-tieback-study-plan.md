# Example: study plan for a public synthetic subsea tie-back

Scope: a new subsea gas-condensate producer tied back 15 km to an existing platform; concept phase.

| Step | Call | Result carried | Evidence status |
| --- | --- | --- | --- |
| S00 | `neqsim-process-safety-study` | scope and acceptance criteria written | n/a |
| S01 | `technical-document-intelligence-agent` | pressure profile checked with `profile_gate` against the design-case table | MATCH within 2 % |
| S02 | register of 12 documents | 7 READ, 5 NOT_READ | `evidence_gate`: UNVERIFIED_SCREENING, 5 data gaps |
| S04 | `process-safety-agent` | release rate 464 t/h, hand calculation 449 t/h | `hand_calc_gate`: MATCH |
| S06 | `olga-simulation-agent` | screening surge 9.6 m3 against 55 m3 in the transient run | `conservatism_gate`: NON_CONSERVATIVE |
| S10 | `neqsim-hazop-node-pack` | node pack, 3 orphan tags | `tag_anchor_gate`: ORPHANS |
| S13 | `reconcile_values` | segment volume differs 24 % between two workstreams | conflict explained or fixed |

Numbers are synthetic. The plan ends with the data gaps, their owners and the human review list; nothing in it is a statement of compliance.
