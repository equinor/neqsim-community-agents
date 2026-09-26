# Tests

This agent coordinates two runnable community skills. Its behaviour is exercised
through their test suites and examples.

## How to exercise the agent

```powershell
cd ..\..\..\neqsim-community-skills\skills\field-development\neqsim-ncs-infrastructure-network
C:\appl\neqsim-venv\Scripts\python.exe -m pytest
C:\appl\neqsim-venv\Scripts\python.exe examples\ncs_network_walkthrough.py

cd ..\neqsim-ncs-value-chain-optimization
C:\appl\neqsim-venv\Scripts\python.exe -m pytest
C:\appl\neqsim-venv\Scripts\python.exe examples\ncs_value_chain_study.py
```

With the `neqsim` Python package installed, the tests also run the NeqSim
hand-offs live: `TiebackAnalyzer`, `LoopedPipeNetwork`, `ValueChainObjective`
and `DebottleneckingAdvisor`.

Walk through `examples/ncs-value-chain-checklist.md` with the prompts in
`prompts/example-prompts.md`.

## Acceptance checks

- Recent-year utilisation routes > 99 % of production with nothing above capacity.
- Every optimiser year is `optimal` and the NeqSim `ValueChainObjective` cross-check agrees.
- The output keeps facts, assumptions and recommendations separate, with sources.
- The agent always names the validated NeqSim follow-up and requires qualified human
  review (`human_review_required: true`).
