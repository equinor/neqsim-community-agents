# Tests

This agent is a coordination definition over public community skills. It has no
runnable code of its own; its behaviour is exercised through the underlying
skill.

## How to exercise the agent

1. Run the skill test suite (no OLGA installation required — the tests use
   synthetic fixtures and a fake installation tree):

   ```bash
   cd ../../../neqsim-community-skills/skills/flow-assurance/olga-multiphase-simulator
   python -m pytest        # discovery, genkey editing, batch command, result parsing
   ```

2. On a machine that has OLGA installed and licensed, confirm discovery and the
   command line the agent would issue:

   ```python
   from olga_multiphase_simulator import OlgaRunner, find_olga_installations, license_environment

   print([i.describe() for i in find_olga_installations()])
   print(license_environment())
   print(OlgaRunner().build_command("case.genkey", nthreads=4, rule_check_only=True))
   ```

3. Run the worked example against a real case:

   ```bash
   python ../../../neqsim-community-skills/skills/flow-assurance/olga-multiphase-simulator/examples/run_olga_case.py case.genkey
   ```

4. Walk through the prompts in `prompts/example-prompts.md`.

## Acceptance checks

- The engine reported is `OlgaExecutables/Olga-<version>.exe`, never an `OLGA-S` path.
- A rule check is proposed before any full run.
- Non-zero exit codes are reported with their category, name and description, and
  simulation-divergence codes (65–73) are distinguished from input errors.
- Results are reported with the units declared in the result catalog and at
  output times that exist in the file.
- The engine version and command line accompany every number.
- The human review requirement is stated.
