from pathlib import Path
import re
import unittest

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = REPO_ROOT / "agents"

REQUIRED_AGENT_FILES = [
    "AGENT.md",
    "agent.yaml",
    "README.md",
]

REQUIRED_FULL_AGENT_FILES = [
    "AGENT.md",
    "agent.yaml",
    "README.md",
    "examples",
    "prompts",
    "tests",
]

REQUIRED_AGENT_SECTIONS = [
    "# Purpose",
    "# When to Use",
    "# Inputs",
    "# Outputs",
    "# Workflow",
    "# Required Skills",
    "# Example Usage",
    "# Assumptions",
    "# Limitations",
    "# Validation Checklist",
    "# References",
]

REQUIRED_YAML_KEYS = [
    "name",
    "description",
    "required_skills",
    "supported_domains",
    "inputs",
    "outputs",
    "human_review_required",
]

EXPECTED_AGENTS = {
    "pvt-agent": ["neqsim-fluid-quality-check"],
    "hydrate-screening-agent": ["neqsim-hydrate-screening"],
    "tie-in-screening-agent": [
        "neqsim-fluid-quality-check",
        "neqsim-hydrate-screening",
        "neqsim-separator-modelling",
    ],
    "process-screening-agent": ["neqsim-separator-modelling"],
    "process-safety-agent": [
        "neqsim-relief-load-screening",
        "neqsim-depressurization-screening",
    ],
    "process-engineer-agent": [
        "neqsim-line-velocity-check",
        "neqsim-compressor-operating-window-check",
    ],
    "compressor-antisurge-agent": [
        "neqsim-compressor-antisurge-recycle",
    ],
    "dynamic-process-preparation-agent": [
        "neqsim-dynamic-process-preparation",
    ],
    "dynamic-instrument-controller-agent": [
        "neqsim-dynamic-instrument-controller-setup",
    ],
    "flow-assurance-engineer-agent": [
        "neqsim-hydrate-margin-check",
        "neqsim-wax-margin-check",
    ],
    "subsea-cooldown-agent": [
        "neqsim-surf-cooldown-screening",
    ],
    "sand-erosion-agent": [
        "neqsim-sand-erosion-screening",
    ],
    "produced-water-scale-agent": [
        "neqsim-produced-water-scale-screening",
    ],
    "production-optimization-agent": [
        "neqsim-separator-modelling",
        "neqsim-compressor-operating-window-check",
        "neqsim-compressor-power-screening",
        "neqsim-production-network-routing",
    ],
    "debottlenecking-agent": [
        "neqsim-separator-modelling",
        "neqsim-compressor-operating-window-check",
        "neqsim-line-velocity-check",
        "neqsim-pressure-drop-screening",
    ],
    "gas-lift-allocation-agent": [
        "neqsim-artificial-lift-screening",
        "neqsim-production-network-routing",
        "neqsim-reservoir-depletion-screening",
    ],
    "concept-selection-agent": [
        "neqsim-resource-classification-screening",
        "neqsim-capex-opex-screening",
        "neqsim-asset-value-npv-screening",
        "neqsim-energy-emissions-screening",
        "neqsim-step-out-screening",
    ],
}


def read_text(path):
    return path.read_text(encoding="utf-8")


def read_yaml(path):
    return yaml.safe_load(read_text(path))


def top_level_yaml_keys(text):
    keys = set()
    for line in text.splitlines():
        if line and not line.startswith(" ") and not line.startswith("#") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def front_matter(text):
    match = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    return match.group(1) if match else ""


def required_skills_from_yaml_text(text):
    skills = []
    in_required_skills = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "required_skills:":
            in_required_skills = True
            continue
        if in_required_skills:
            if stripped.startswith("- "):
                skills.append(stripped[2:].strip().strip('"\''))
                continue
            if stripped:
                break
    return skills


def scalar_from_yaml_text(text, key):
    match = re.search(r"^\s*" + re.escape(key) + r":\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"\'') if match else None


def catalog_agent_blocks(text):
    blocks = []
    current = []
    for line in text.splitlines():
        if line.startswith("- name: "):
            if current:
                blocks.append("\n".join(current))
            current = [line]
        elif current:
            current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


class RepositoryStructureTests(unittest.TestCase):
    def test_top_level_files_exist(self):
        for relative_path in [
            "README.md",
            "CONTRIBUTING.md",
            "LICENSE.md",
            "community-agents.yaml",
            "docs/agent-standard.md",
            "docs/repository-structure.md",
            "docs/governance.md",
            "docs/safety-guidelines.md",
            "docs/contribution-guide.md",
            "templates/agent-template/AGENT.md",
            "templates/agent-template/agent.yaml",
        ]:
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).exists())

    def test_expected_agents_exist(self):
        self.assertTrue(AGENTS_DIR.exists())
        actual_agents = {path.name for path in AGENTS_DIR.iterdir() if path.is_dir()}
        self.assertTrue(set(EXPECTED_AGENTS).issubset(actual_agents))

    def test_each_agent_has_required_structure(self):
        agent_names = [path.name for path in AGENTS_DIR.iterdir() if path.is_dir()]
        for agent_name in agent_names:
            agent_dir = AGENTS_DIR / agent_name
            for required_file in REQUIRED_AGENT_FILES:
                with self.subTest(agent=agent_name, required_file=required_file):
                    self.assertTrue((agent_dir / required_file).exists())

    def test_expected_agents_have_full_structure(self):
        for agent_name in EXPECTED_AGENTS:
            agent_dir = AGENTS_DIR / agent_name
            for required_file in REQUIRED_FULL_AGENT_FILES:
                with self.subTest(agent=agent_name, required_file=required_file):
                    self.assertTrue((agent_dir / required_file).exists())

    def test_agent_markdown_has_required_front_matter_and_sections(self):
        for agent_name, expected_skills in EXPECTED_AGENTS.items():
            agent_text = read_text(AGENTS_DIR / agent_name / "AGENT.md")
            metadata = front_matter(agent_text)
            with self.subTest(agent=agent_name, field="front_matter"):
                self.assertIn(f"name: {agent_name}", metadata)
                self.assertIn("description:", metadata)
                self.assertIn("version:", metadata)
                self.assertIn("required_skills:", metadata)
            for skill in expected_skills:
                with self.subTest(agent=agent_name, skill=skill):
                    self.assertIn(skill, metadata)
            for section in REQUIRED_AGENT_SECTIONS:
                with self.subTest(agent=agent_name, section=section):
                    self.assertIn(section, agent_text)

    def test_agent_yaml_has_required_metadata(self):
        for agent_name, expected_skills in EXPECTED_AGENTS.items():
            yaml_text = read_text(AGENTS_DIR / agent_name / "agent.yaml")
            keys = top_level_yaml_keys(yaml_text)
            for key in REQUIRED_YAML_KEYS:
                with self.subTest(agent=agent_name, key=key):
                    self.assertIn(key, keys)
            with self.subTest(agent=agent_name, field="human_review_required"):
                self.assertIn("human_review_required: true", yaml_text)
            for skill in expected_skills:
                with self.subTest(agent=agent_name, skill=skill):
                    self.assertIn(f"- {skill}", yaml_text)

    def test_agent_yaml_matches_front_matter_metadata(self):
        for agent_dir in AGENTS_DIR.iterdir():
            if not agent_dir.is_dir():
                continue
            markdown_metadata = front_matter(read_text(agent_dir / "AGENT.md"))
            yaml_text = read_text(agent_dir / "agent.yaml")
            for key in ["name", "version"]:
                with self.subTest(agent=agent_dir.name, key=key):
                    self.assertEqual(
                        scalar_from_yaml_text(markdown_metadata, key),
                        scalar_from_yaml_text(yaml_text, key),
                    )
            with self.subTest(agent=agent_dir.name, key="required_skills"):
                self.assertEqual(
                    required_skills_from_yaml_text(markdown_metadata),
                    required_skills_from_yaml_text(yaml_text),
                )

    def test_catalog_uses_canonical_skill_ids_and_matches_packages(self):
        catalog = read_yaml(REPO_ROOT / "community-agents.yaml")
        self.assertEqual(catalog["trust"], "community")
        for entry in catalog["agents"]:
            agent_dir = AGENTS_DIR / entry["name"]
            with self.subTest(agent=entry["name"], field="package"):
                self.assertTrue(agent_dir.exists())
            catalog_skills = entry["required_skills"]
            package_skills = read_yaml(agent_dir / "agent.yaml")["required_skills"]
            with self.subTest(agent=entry["name"], field="required_skills"):
                self.assertEqual(catalog_skills, package_skills)
            for skill in catalog_skills:
                with self.subTest(agent=entry["name"], skill=skill):
                    self.assertTrue(skill.startswith("neqsim-"))

    def test_catalog_metadata_matches_agent_packages(self):
        catalog = read_yaml(REPO_ROOT / "community-agents.yaml")
        for entry in catalog["agents"]:
            agent_dir = REPO_ROOT / Path(entry["path"]).parent
            package = read_yaml(agent_dir / "agent.yaml")
            for field in ["name", "version", "description"]:
                with self.subTest(agent=entry["name"], field=field):
                    self.assertEqual(str(entry[field]), str(package[field]))
            with self.subTest(agent=entry["name"], field="required_skills"):
                self.assertEqual(entry["required_skills"], package["required_skills"])

    def test_each_agent_has_examples_and_prompts(self):
        for agent_name in EXPECTED_AGENTS:
            agent_dir = AGENTS_DIR / agent_name
            example_files = list((agent_dir / "examples").glob("*.md"))
            prompt_files = list((agent_dir / "prompts").glob("*.md"))
            with self.subTest(agent=agent_name, folder="examples"):
                self.assertGreaterEqual(len(example_files), 1)
            with self.subTest(agent=agent_name, folder="prompts"):
                self.assertGreaterEqual(len(prompt_files), 1)

    def test_human_review_language_is_present(self):
        for agent_name in EXPECTED_AGENTS:
            combined_text = "\n".join(
                read_text(path)
                for path in [
                    AGENTS_DIR / agent_name / "AGENT.md",
                    AGENTS_DIR / agent_name / "README.md",
                ]
            ).lower()
            with self.subTest(agent=agent_name):
                self.assertIn("human review", combined_text)
                self.assertIn("does not replace", combined_text)


if __name__ == "__main__":
    unittest.main()