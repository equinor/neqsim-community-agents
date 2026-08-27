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

4. Optional-skill hygiene (warnings). ``context_skills`` ids are existence-
   checked like ``required_skills``. When an ``AGENT.md`` sits next to the
   manifest, any canonical skill id named in its prose that is not declared in
   ``required_skills``/``context_skills`` (or inherited via ``extends``) is
   flagged, so a skill can no longer be mentioned in prose while staying
   invisible to the machine-checkable linkage. When validating the enterprise
   catalog, an agent that shares its ``name`` with a community agent but does
   not declare ``extends`` is flagged as a probable divergent fork (it should
   either use an ``enterprise-*`` id or declare ``extends``). Orchestration
    edges are checked too: ids in ``coordinated_agents`` and sender ids in typed
    ``inbound_handoffs`` are existence-checked against the catalogs
    (self-reference is an error), an agent whose
   ``agent_type`` is a coordinator/orchestrator but that declares no
   ``coordinated_agents`` is flagged, a missing ``agent_type`` is flagged, any
    known agent named in ``AGENT.md`` prose but not in ``coordinated_agents``,
    ``inbound_handoffs``, or ``extends`` is flagged, and the legacy
    ``referenced_skills`` field is flagged as deprecated in favour of
    ``context_skills``.

5. Python-runtime consistency. Runtime instruction surfaces must not launch
    bare Python tools, select/create/activate an interpreter environment, or
    direct fallback to a different interpreter. The shared Harness policy owns
    interpreter selection and defaults to the shared NeqSim environment.

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
# Matches a canonical skill id embedded in free-text (AGENT.md prose). The
# lookbehind/lookahead avoid matching a longer hyphenated token by accident.
SKILL_ID_IN_TEXT_RE = re.compile(
    r"(?<![a-z0-9-])((?:neqsim|enterprise)-[a-z0-9]+(?:-[a-z0-9]+)*)"
)
# Matches an agent id in free text. Agent ids in the folder-per-agent catalogs
# all end in ``-agent``, which keeps this precise and low-false-positive.
AGENT_ID_IN_TEXT_RE = re.compile(
    r"(?<![a-z0-9-])([a-z0-9]+(?:-[a-z0-9]+)*-agent)(?![a-z0-9-])"
)
ORCHESTRATION_TYPES = ("community-coordinator", "enterprise-coordinator", "enterprise-orchestrator")
SIBLING_COMMUNITY_ENV = "NEQSIM_COMMUNITY_AGENTS_DIR"
SIBLING_ENTERPRISE_ENV = "NEQSIM_ENTERPRISE_AGENTS_DIR"
RUNTIME_INSTRUCTION_GLOBS = ("AGENT.md", "prompts/*.md", "workflows/*.md")
BARE_PYTHON_LAUNCH_RE = re.compile(
    r"(?<![A-Za-z0-9_./\\-])(python(?:\.exe)?|py|pip|pytest)\s+"
    r"(?:-m\s+)?[A-Za-z0-9_.\"'<]"
)
PYTHON_ENV_CONFLICT_RE = re.compile(
    r"(?:select (?:a |another |the )?(?:python )?interpreter|"
    r"(?:create|activate) (?:a |the )?(?:new |per-agent )?"
    r"(?:virtual environment|venv)|"
    r"fall back to (?:the )?(?:system|another|different) (?:python|interpreter))",
    re.IGNORECASE,
)
PYTHON_ENV_SETUP_TOOL_RE = re.compile(
    r"(?:configure_python_environment|pylanceUpdatePythonEnvironment|"
    r"Python:\s*Select Interpreter)",
    re.IGNORECASE,
)
NEGATED_RUNTIME_DIRECTIVE_RE = re.compile(
    r"\b(?:do not|don't|never|must not|without)\b", re.IGNORECASE
)


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
    inbound_handoffs = manifest.get("inbound_handoffs")
    if inbound_handoffs is not None:
        if not isinstance(inbound_handoffs, list):
            errors.append("inbound_handoffs must be an array")
        else:
            for handoff in inbound_handoffs:
                if not isinstance(handoff, dict) or not all(
                    key in handoff for key in ("agent", "schema", "purpose")
                ):
                    errors.append(
                        "inbound_handoffs entries must contain agent, schema, and purpose"
                    )
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


def declared_skills(manifest, bases):
    """Return the skills an agent declares directly or inherits via extends."""
    skills = set(manifest.get("required_skills") or [])
    skills.update(manifest.get("context_skills") or [])
    extends = manifest.get("extends")
    if isinstance(extends, dict):
        base = bases.get(extends.get("agent"))
        if isinstance(base, dict):
            skills.update(base.get("required_skills") or [])
            skills.update(base.get("context_skills") or [])
    return skills


def check_agent_md_skills(manifest_dir, manifest, bases, known_skills):
    """Warn when AGENT.md names a known skill id the manifest does not declare.

    Closes the gap where a skill is only mentioned in AGENT.md prose (so it is
    invisible to existence checks and the agent<->skill map). Only skill ids
    that exist in a known skill catalog are flagged, so example ids or prose
    that merely resembles a skill id do not produce false positives. When no
    skill catalog is discoverable the check is skipped entirely.
    """
    warnings = []
    if not known_skills:
        return warnings
    agent_md = manifest_dir / "AGENT.md"
    if not agent_md.exists():
        return warnings
    try:
        text = agent_md.read_text(encoding="utf-8")
    except OSError:
        return warnings
    declared = declared_skills(manifest, bases)
    mentioned = {m.group(1) for m in SKILL_ID_IN_TEXT_RE.finditer(text)}
    for skill in sorted(mentioned - declared):
        if skill in known_skills:
            warnings.append(
                "AGENT.md names skill '{}' but it is not in required_skills or "
                "context_skills (declare it so the linkage is machine-checkable)".format(
                    skill
                )
            )
    return warnings


def check_agent_md_agents(manifest_dir, manifest, known_agents):
    """Warn when AGENT.md names a known agent with no declared relationship.

    Delegation and inbound provenance that live only in prose are invisible to
    the orchestration graph. Accept outbound ``coordinated_agents``, typed
    ``inbound_handoffs``, and the base linked through ``extends`` as distinct
    machine-readable relationships.
    """
    warnings = []
    if not known_agents:
        return warnings
    agent_md = manifest_dir / "AGENT.md"
    if not agent_md.exists():
        return warnings
    try:
        text = agent_md.read_text(encoding="utf-8")
    except OSError:
        return warnings
    own = manifest.get("name")
    declared = set(manifest.get("coordinated_agents") or [])
    declared.update(
        handoff.get("agent")
        for handoff in manifest.get("inbound_handoffs") or []
        if isinstance(handoff, dict) and handoff.get("agent")
    )
    extends = manifest.get("extends")
    if isinstance(extends, dict) and extends.get("agent"):
        declared.add(extends["agent"])
    mentioned = {m.group(1) for m in AGENT_ID_IN_TEXT_RE.finditer(text)}
    for agent in sorted(mentioned - declared):
        if agent != own and agent in known_agents:
            warnings.append(
                "AGENT.md names agent '{}' but no coordinated_agents, inbound_handoffs, "
                "or extends relationship declares it (declare the relationship so the "
                "orchestration graph is machine-checkable)".format(agent)
            )
    return warnings


def check_python_runtime_instructions(agent_dir):
    """Return errors for agent instructions that conflict with shared Python runtime policy."""
    errors = []
    paths = []
    for pattern in RUNTIME_INSTRUCTION_GLOBS:
        paths.extend(agent_dir.glob(pattern))
    for path in sorted(set(paths)):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line_number, line in enumerate(lines, start=1):
            context = " ".join(lines[max(0, line_number - 4) : line_number])
            if NEGATED_RUNTIME_DIRECTIVE_RE.search(context):
                continue
            bare_match = BARE_PYTHON_LAUNCH_RE.search(line)
            conflict_match = PYTHON_ENV_CONFLICT_RE.search(line)
            setup_tool_match = PYTHON_ENV_SETUP_TOOL_RE.search(line)
            if bare_match:
                errors.append(
                    "{}:{} uses bare '{}' launcher; use the parent-selected absolute "
                    "executable or sys.executable".format(
                        path.relative_to(agent_dir), line_number, bare_match.group(1)
                    )
                )
            elif conflict_match or setup_tool_match:
                matched_directive = conflict_match or setup_tool_match
                errors.append(
                    "{}:{} conflicts with the shared Python runtime policy: '{}'".format(
                        path.relative_to(agent_dir), line_number, matched_directive.group(0)
                    )
                )
    return errors


HARDCODED_LOCAL_PATH_RE = re.compile(
    r"[A-Za-z]:[\\/](?:Users|home|appl)[\\/]", re.IGNORECASE
)


def check_hardcoded_local_paths(agent_dir):
    """Return errors for absolute local machine paths baked into shipped agent text.

    AGENT.md/prompts/workflows are copied verbatim into every user's install
    directory by ``neqsim agent install``, so an absolute path such as
    ``C:\\Users\\<name>\\...`` or ``C:\\appl\\...`` that only exists on the
    author's machine breaks the agent for everyone else.
    """
    errors = []
    paths = []
    for pattern in RUNTIME_INSTRUCTION_GLOBS:
        paths.extend(agent_dir.glob(pattern))
    for path in sorted(set(paths)):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line_number, line in enumerate(lines, start=1):
            match = HARDCODED_LOCAL_PATH_RE.search(line)
            if match:
                errors.append(
                    "{}:{} hardcodes an author-machine path '{}'; describe the "
                    "runtime portably (active venv, sys.executable, or an env "
                    "var) instead of a literal local path".format(
                        path.relative_to(agent_dir), line_number, match.group(0)
                    )
                )
    return errors


def discover_community_agent_names(repo_root):
    """Return the set of agent ids defined in the community agents catalog."""
    names = set()
    candidate_dirs = []
    env_community = os.environ.get(SIBLING_COMMUNITY_ENV)
    if env_community:
        candidate_dirs.append(Path(env_community))
    candidate_dirs.append(repo_root.parent / "neqsim-community-agents" / "agents")
    for agents_dir in candidate_dirs:
        if not agents_dir.is_dir():
            continue
        for agent_dir in agents_dir.iterdir():
            if agent_dir.is_dir() and (agent_dir / "agent.yaml").exists():
                names.add(agent_dir.name)
    return names


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


def check_inbound_handoffs(manifest, known_agents):
    """Return errors and warnings for receiver-declared inbound handoffs."""
    errors, warnings = [], []
    name = manifest.get("name")
    for handoff in manifest.get("inbound_handoffs") or []:
        if not isinstance(handoff, dict):
            continue
        sender = handoff.get("agent")
        if sender == name:
            errors.append("inbound_handoffs lists itself")
        elif sender and known_agents and sender not in known_agents:
            warnings.append(
                "inbound handoff agent '{}' not found in known agent catalogs "
                "(typo or missing agent?)".format(sender)
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
    community_names = (
        discover_community_agent_names(repo_root) if repo_kind == "enterprise" else set()
    )
    known_agents = set(bases.keys())
    known_agents.update(m.parent.name for m in agents_dir.glob("*/agent.yaml"))

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
            for skill in manifest.get("context_skills") or []:
                if skill not in known_skills:
                    all_warnings.append(
                        "[{}] context skill '{}' not found in known skill "
                        "catalogs (typo or missing skill?)".format(name, skill)
                    )

        for warn in check_agent_md_skills(manifest_path.parent, manifest, bases, known_skills):
            all_warnings.append("[{}] {}".format(name, warn))

        if repo_kind == "enterprise" and name in community_names and not manifest.get("extends"):
            all_warnings.append(
                "[{}] shares its name with a community agent but does not declare "
                "`extends`; use an enterprise-* id or declare extends so the overlay "
                "linkage is explicit".format(name)
            )

        coordinated = manifest.get("coordinated_agents") or []
        for other in coordinated:
            if other == name:
                all_errors.append("[{}] coordinated_agents lists itself".format(name))
            elif known_agents and other not in known_agents:
                all_warnings.append(
                    "[{}] coordinated agent '{}' not found in known agent catalogs "
                    "(typo or missing agent?)".format(name, other)
                )

        inbound_errors, inbound_warnings = check_inbound_handoffs(manifest, known_agents)
        all_errors.extend("[{}] {}".format(name, error) for error in inbound_errors)
        all_warnings.extend("[{}] {}".format(name, warning) for warning in inbound_warnings)

        agent_type = manifest.get("agent_type")
        if agent_type in ORCHESTRATION_TYPES and not coordinated:
            all_warnings.append(
                "[{}] agent_type '{}' implies delegation but coordinated_agents is "
                "empty (declare the delegated agents, or use a leaf agent_type)".format(
                    name, agent_type
                )
            )
        if agent_type is None:
            all_warnings.append(
                "[{}] no agent_type declared (add one so the orchestration role is "
                "explicit; leaf agents use community-agent/enterprise-agent)".format(name)
            )

        if manifest.get("referenced_skills") is not None:
            all_warnings.append(
                "[{}] 'referenced_skills' is deprecated; move these ids into "
                "'context_skills'".format(name)
            )

        for warn in check_agent_md_agents(manifest_path.parent, manifest, known_agents):
            all_warnings.append("[{}] {}".format(name, warn))

        for err in check_python_runtime_instructions(manifest_path.parent):
            all_errors.append("[{}] {}".format(name, err))

        for err in check_hardcoded_local_paths(manifest_path.parent):
            all_errors.append("[{}] {}".format(name, err))

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
