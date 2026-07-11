#!/usr/bin/env python3
"""Validate agent package manifests against the shared NeqSim agent schema.

This script is intentionally self-contained and identical across the community
and enterprise agent repositories. It performs three families of checks:

1. Structural validation of every ``agents/*/agent.yaml`` against the vendored
   ``schemas/agent-manifest.schema.json``. Uses the ``jsonschema`` package when
   available; otherwise falls back to a minimal built-in structural check so the
   script never hard-fails on a missing optional dependency.

2. Skill-reference reachability. Every ``required_skills`` entry must use a
   canonical namespace (``neqsim-*`` for core/community skills, ``enterprise-*``
   for internal skills). If a skills index is discoverable (a sibling community
   skills repo, an ``enterprise-skills.yaml`` catalog, or a vendored
   ``schemas/skills.index.json``), each id is additionally resolved against it.

3. ``extends`` resolution. An agent that declares ``extends`` must point at a
   base agent that can be resolved, and its own ``required_skills`` must be a
   superset of the base agent's ``required_skills`` so the overlay is a genuine
   extension rather than a divergent fork. Base agents are resolved from a
   sibling checkout of the referenced catalog repo when present, or from a
   vendored ``schemas/base-agents.index.json`` snapshot, and are skipped with a
   warning (not an error) when neither source is available.

Exit codes:
    0 - all checks pass (warnings allowed)
    1 - one or more errors found
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:  # pragma: no cover - exercised indirectly
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

try:  # optional, richer validation when present
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


SKILL_ID_RE = re.compile(r"^(neqsim|enterprise)-[a-z0-9]+(-[a-z0-9]+)*$")
SIBLING_COMMUNITY_ENV = "NEQSIM_COMMUNITY_AGENTS_DIR"
SIBLING_ENTERPRISE_ENV = "NEQSIM_ENTERPRISE_AGENTS_DIR"


def repo_root_from_script():
    """Return the repository root (parent of this scripts/ folder)."""
    return Path(__file__).resolve().parents[1]


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_schema(repo_root):
    schema_path = repo_root / "schemas" / "agent-manifest.schema.json"
    if not schema_path.exists():
        return None, schema_path
    return json.loads(schema_path.read_text(encoding="utf-8")), schema_path


def minimal_structural_check(manifest, schema):
    """Fallback validation used when jsonschema is not installed."""
    errors = []
    for key in schema.get("required", []):
        if key not in manifest:
            errors.append("missing required field '{}'".format(key))
    props = schema.get("properties", {})
    if isinstance(manifest.get("required_skills"), list):
        for skill in manifest["required_skills"]:
            if not isinstance(skill, str) or not SKILL_ID_RE.match(skill):
                errors.append("required_skills entry '{}' is not a canonical id".format(skill))
    if "human_review_required" in manifest and not isinstance(
        manifest["human_review_required"], bool
    ):
        errors.append("human_review_required must be a boolean")
    extends = manifest.get("extends")
    if extends is not None:
        if not isinstance(extends, dict) or "agent" not in extends or "repo" not in extends:
            errors.append("extends must be an object with 'agent' and 'repo'")
        elif extends.get("repo") not in props["extends"]["properties"]["repo"]["enum"]:
            errors.append("extends.repo '{}' is not a valid catalog".format(extends.get("repo")))
    return errors


def validate_against_schema(manifest, schema):
    if jsonschema is not None:
        validator = jsonschema.Draft7Validator(schema)
        return [
            "{}: {}".format("/".join(str(p) for p in err.path) or "<root>", err.message)
            for err in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path))
        ]
    return minimal_structural_check(manifest, schema)


def discover_base_agents(repo_root, repo_kind):
    """Return {agent_name: manifest_dict} for base agents that can be resolved.

    Looks, in priority order, at: an env-var override, a sibling checkout of the
    referenced catalog repo, and a vendored snapshot index.
    """
    bases = {}

    # 1. Sibling community checkout (the common case in this workspace / CI matrix).
    candidate_dirs = []
    env_community = os.environ.get(SIBLING_COMMUNITY_ENV)
    if env_community:
        candidate_dirs.append(Path(env_community))
    candidate_dirs.append(repo_root.parent / "neqsim-community-agents" / "agents")
    env_enterprise = os.environ.get(SIBLING_ENTERPRISE_ENV)
    if env_enterprise:
        candidate_dirs.append(Path(env_enterprise))
    candidate_dirs.append(repo_root.parent / "neqsim-enterprise-agents" / "agents")

    for agents_dir in candidate_dirs:
        if not agents_dir.is_dir():
            continue
        for agent_dir in agents_dir.iterdir():
            manifest_path = agent_dir / "agent.yaml"
            if agent_dir.is_dir() and manifest_path.exists() and agent_dir.name not in bases:
                try:
                    bases[agent_dir.name] = load_yaml(manifest_path)
                except Exception:  # noqa: BLE001 - tolerate malformed sibling files
                    continue

    # 2. Vendored snapshot index (makes the check self-contained in standalone CI).
    index_path = repo_root / "schemas" / "base-agents.index.json"
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            for name, manifest in index.get("agents", {}).items():
                bases.setdefault(name, manifest)
        except Exception:  # noqa: BLE001
            pass

    return bases


def _skill_name_from_md(path):
    """Return the `name:` field from a SKILL.md frontmatter, or None."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    frontmatter = text.split("---", 2)[1]
    match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    return match.group(1).strip().strip('"').strip("'") if match else None


def discover_known_skills(repo_root):
    """Return the set of known skill ids for required_skills existence checks.

    Combines a vendored ``schemas/skills.index.json`` snapshot (self-contained
    for standalone CI) with a fresh scan of sibling skill repositories when they
    are checked out alongside this repo (core, community, and enterprise skills).
    """
    skills = set()

    index_path = repo_root / "schemas" / "skills.index.json"
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            skills.update(index.get("skills") or [])
        except Exception:  # noqa: BLE001
            pass

    workspace = repo_root.parent
    patterns = {
        workspace / "neqsim" / ".github" / "skills": "*/SKILL.md",
        workspace / "neqsim-community-skills" / "skills": "*/*/SKILL.md",
        workspace / "neqsim-enterprise-skills" / "skills": "*/*/SKILL.md",
    }
    for base, pattern in patterns.items():
        if not base.is_dir():
            continue
        for skill_md in base.glob(pattern):
            name = _skill_name_from_md(skill_md)
            if name:
                skills.add(name)
    return skills


def check_extends(manifest, bases):
    """Return (errors, warnings) for an agent's extends declaration."""
    errors, warnings = [], []
    extends = manifest.get("extends")
    if not extends:
        return errors, warnings
    base_name = extends.get("agent")
    base = bases.get(base_name)
    if base is None:
        warnings.append(
            "extends base '{}' could not be resolved (base catalog not checked "
            "out and no vendored snapshot) - skipping superset check".format(base_name)
        )
        return errors, warnings
    base_skills = set(base.get("required_skills") or [])
    own_skills = set(manifest.get("required_skills") or [])
    missing = sorted(base_skills - own_skills)
    if missing:
        errors.append(
            "extends '{}' but does not re-declare inherited skills {} "
            "(an overlay must be a superset of its base)".format(base_name, missing)
        )
    return errors, warnings


def validate_repo(repo_root):
    schema, schema_path = load_schema(repo_root)
    if schema is None:
        return ["schema not found at {}".format(schema_path)], []

    agents_dir = repo_root / "agents"
    if not agents_dir.is_dir():
        return ["agents/ directory not found at {}".format(agents_dir)], []

    repo_kind = "enterprise" if (repo_root / "enterprise-agents.yaml").exists() else "community"
    bases = discover_base_agents(repo_root, repo_kind)
    known_skills = discover_known_skills(repo_root)

    all_errors, all_warnings = [], []
    manifests = sorted(agents_dir.glob("*/agent.yaml"))
    if not manifests:
        return ["no agent.yaml files found under {}".format(agents_dir)], []

    for manifest_path in manifests:
        name = manifest_path.parent.name
        try:
            manifest = load_yaml(manifest_path)
        except Exception as exc:  # noqa: BLE001
            all_errors.append("[{}] could not parse agent.yaml: {}".format(name, exc))
            continue
        if not isinstance(manifest, dict):
            all_errors.append("[{}] agent.yaml is not a mapping".format(name))
            continue

        for err in validate_against_schema(manifest, schema):
            all_errors.append("[{}] schema: {}".format(name, err))

        if manifest.get("name") != name:
            all_errors.append(
                "[{}] name field '{}' does not match folder".format(name, manifest.get("name"))
            )

        if known_skills:
            for skill in manifest.get("required_skills") or []:
                if skill not in known_skills:
                    all_warnings.append(
                        "[{}] required skill '{}' not found in known skill "
                        "catalogs (typo or missing skill?)".format(name, skill)
                    )

        ext_errors, ext_warnings = check_extends(manifest, bases)
        all_errors.extend("[{}] {}".format(name, e) for e in ext_errors)
        all_warnings.extend("[{}] {}".format(name, w) for w in ext_warnings)

    return all_errors, all_warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=repo_root_from_script(),
        help="Repository root (defaults to the parent of this scripts/ folder).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings (e.g. unresolved extends bases) as errors.",
    )
    args = parser.parse_args(argv)

    errors, warnings = validate_repo(args.repo_root.resolve())

    for warning in warnings:
        print("WARNING: {}".format(warning))
    for error in errors:
        print("ERROR: {}".format(error))

    if jsonschema is None:
        print("NOTE: jsonschema not installed - used minimal structural checks only.")

    failed = bool(errors) or (args.strict and bool(warnings))
    if failed:
        print("\nAgent manifest validation FAILED ({} errors, {} warnings).".format(
            len(errors), len(warnings)))
        return 1
    print("\nAgent manifest validation passed ({} warnings).".format(len(warnings)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
