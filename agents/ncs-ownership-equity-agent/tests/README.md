# Tests

The skill `neqsim-ncs-ownership-equity` carries the offline unit tests (`tests/test_ownership.py`) for
the Sodir reader, period and operator handling, prospect validation and net-equity arithmetic.
Run them from the skill folder with `python -m pytest`.

Agent-level checks: every prompt in `prompts/example-prompts.md` must state the asset, `as_of`,
equity `basis`, data date and the human review requirement.
