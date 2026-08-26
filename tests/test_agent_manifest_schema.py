"""Validate every agent manifest against the shared agent-manifest schema.

Exercises the vendored ``scripts/validate_agent_manifests.py`` so schema
conformance, canonical skill namespaces, and ``extends`` overlay rules are
enforced in CI. Also guards against drift between the vendored schema copy and
the canonical schema in the core NeqSim repo when that repo is checked out
alongside this one.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_agent_manifests as validator  # noqa: E402


class AgentManifestSchemaTests(unittest.TestCase):
    def test_schema_file_present(self):
        self.assertTrue((REPO_ROOT / "schemas" / "agent-manifest.schema.json").exists())

    def test_all_manifests_conform(self):
        errors, _warnings = validator.validate_repo(REPO_ROOT)
        self.assertEqual(errors, [], "agent manifest errors:\n" + "\n".join(errors))

    def test_skills_index_present(self):
        self.assertTrue((REPO_ROOT / "schemas" / "skills.index.json").exists())

    def test_all_required_skills_resolve(self):
        _errors, warnings = validator.validate_repo(REPO_ROOT)
        unresolved = [w for w in warnings if "not found in known skill" in w]
        self.assertEqual(unresolved, [], "unresolved skills:\n" + "\n".join(unresolved))

    def test_extends_superset_violation_is_error(self):
        bases = {"base-agent": {"required_skills": ["neqsim-a", "neqsim-b"]}}
        manifest = {
            "extends": {"agent": "base-agent", "repo": "community"},
            "required_skills": ["neqsim-a"],
        }
        errors, _warnings = validator.check_extends(manifest, bases)
        self.assertTrue(errors)

    def test_extends_superset_is_accepted(self):
        bases = {"base-agent": {"required_skills": ["neqsim-a"]}}
        manifest = {
            "extends": {"agent": "base-agent", "repo": "community"},
            "required_skills": ["neqsim-a", "enterprise-policy-overlay"],
        }
        errors, _warnings = validator.check_extends(manifest, bases)
        self.assertEqual(errors, [])

    def test_unresolved_base_is_warning_not_error(self):
        manifest = {
            "extends": {"agent": "does-not-exist", "repo": "community"},
            "required_skills": ["neqsim-a"],
        }
        errors, warnings = validator.check_extends(manifest, {})
        self.assertEqual(errors, [])
        self.assertTrue(warnings)

    def test_python_runtime_conflicts_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            agent_dir = Path(temp_dir)
            (agent_dir / "AGENT.md").write_text(
                "Run `python task.py`.\nCreate a virtual environment first.\n",
                encoding="utf-8",
            )
            errors = validator.check_python_runtime_instructions(agent_dir)
        self.assertEqual(len(errors), 2)

    def test_compliant_python_runtime_policy_is_accepted(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            agent_dir = Path(temp_dir)
            (agent_dir / "AGENT.md").write_text(
                "Use C:\\appl\\neqsim-venv\\Scripts\\python.exe or sys.executable. "
                "Never invoke bare python or activate a per-agent environment.\n",
                encoding="utf-8",
            )
            errors = validator.check_python_runtime_instructions(agent_dir)
        self.assertEqual(errors, [])

    def test_typed_inbound_handoff_conforms_to_schema(self):
        schema, _path = validator.load_schema(REPO_ROOT)
        manifest = {
            "name": "receiver-agent",
            "description": "Receives a typed task-basis handoff.",
            "version": "0.1.0",
            "required_skills": [],
            "supported_domains": ["testing"],
            "inputs": ["test task basis"],
            "outputs": ["validated handoff"],
            "human_review_required": True,
            "inbound_handoffs": [
                {
                    "agent": "sender-agent",
                    "schema": "test_handoff.v1",
                    "purpose": "Preserve test provenance while ownership transfers.",
                }
            ],
        }
        self.assertEqual(validator.validate_against_schema(manifest, schema), [])

    def test_malformed_inbound_handoff_fails_schema_validation(self):
        schema, _path = validator.load_schema(REPO_ROOT)
        manifest = {
            "name": "receiver-agent",
            "description": "Receives a test handoff.",
            "version": "0.1.0",
            "required_skills": [],
            "supported_domains": ["testing"],
            "inbound_handoffs": [
                {"agent": "sender-agent", "schema": "test_handoff.v1"}
            ],
        }
        errors = validator.validate_against_schema(manifest, schema)
        self.assertTrue(any("purpose" in error for error in errors))

    def test_inbound_handoff_sender_checks(self):
        self_errors, self_warnings = validator.check_inbound_handoffs(
            {
                "name": "receiver-agent",
                "inbound_handoffs": [
                    {
                        "agent": "receiver-agent",
                        "schema": "test_handoff.v1",
                        "purpose": "Test self-reference rejection.",
                    }
                ],
            },
            {"receiver-agent"},
        )
        self.assertTrue(self_errors)
        self.assertEqual(self_warnings, [])

        errors, warnings = validator.check_inbound_handoffs(
            {
                "name": "receiver-agent",
                "inbound_handoffs": [
                    {
                        "agent": "missing-agent",
                        "schema": "test_handoff.v1",
                        "purpose": "Test unresolved sender warning.",
                    }
                ],
            },
            {"receiver-agent"},
        )
        self.assertEqual(errors, [])
        self.assertTrue(warnings)

    def test_inbound_agent_prose_reference_is_declared(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            agent_dir = Path(temp_dir)
            (agent_dir / "AGENT.md").write_text(
                "Accept a task basis from `sender-agent`.", encoding="utf-8"
            )
            warnings = validator.check_agent_md_agents(
                agent_dir,
                {
                    "name": "receiver-agent",
                    "inbound_handoffs": [
                        {
                            "agent": "sender-agent",
                            "schema": "test_handoff.v1",
                            "purpose": "Preserve test provenance while ownership transfers.",
                        }
                    ],
                },
                {"sender-agent", "receiver-agent"},
            )
        self.assertEqual(warnings, [])

    def test_vendored_schema_matches_core_canonical_when_present(self):
        canonical = (
            REPO_ROOT.parent
            / "neqsim"
            / "docs"
            / "integration"
            / "schemas"
            / "agent-manifest.schema.json"
        )
        if not canonical.exists():
            self.skipTest("core neqsim repo not checked out alongside this repo")
        vendored = REPO_ROOT / "schemas" / "agent-manifest.schema.json"
        self.assertEqual(
            json.loads(vendored.read_text(encoding="utf-8")),
            json.loads(canonical.read_text(encoding="utf-8")),
            "vendored schema has drifted from the canonical core schema",
        )


if __name__ == "__main__":
    unittest.main()
