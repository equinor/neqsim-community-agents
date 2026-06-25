from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = REPO_ROOT / "agents"

REQUIRED_AGENT_FILES = [
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
    "pvt-agent": ["fluid-quality-check"],
    "hydrate-screening-agent": ["hydrate-screening"],
    "tie-in-screening-agent": [
        "fluid-quality-check",
        "hydrate-screening",
        "separator-modelling",
    ],
    "process-screening-agent": ["separator-modelling"],
    "process-safety-agent": [
        "relief-load-screening",
        "depressurization-screening",
    ],
    "process-engineer-agent": [
        "line-velocity-check",
        "compressor-operating-window-check",
    ],
    "compressor-antisurge-agent": [
        "compressor-antisurge-recycle",
    ],
    "dynamic-process-preparation-agent": [
        "dynamic-process-preparation",
    ],
    "dynamic-instrument-controller-agent": [
        "dynamic-instrument-controller-setup",
    ],
    "flow-assurance-engineer-agent": [
        "hydrate-margin-check",
        "wax-margin-check",
    ],
    "subsea-cooldown-agent": [
        "surf-cooldown-screening",
    ],
    "sand-erosion-agent": [
        "sand-erosion-screening",
    ],
    "produced-water-scale-agent": [
        "produced-water-scale-screening",
    ],
    "production-optimization-agent": [
        "separator-modelling",
        "compressor-operating-window-check",
        "compressor-power-screening",
        "production-network-routing",
    ],
    "debottlenecking-agent": [
        "separator-modelling",
        "compressor-operating-window-check",
        "line-velocity-check",
        "pressure-drop-screening",
    ],
    "gas-lift-allocation-agent": [
        "artificial-lift-screening",
        "production-network-routing",
        "reservoir-depletion-screening",
    ],
    "concept-selection-agent": [
        "resource-classification-screening",
        "capex-opex-screening",
        "asset-value-npv-screening",
        "energy-emissions-screening",
        "step-out-screening",
    ],
}


def read_text(path):
    return path.read_text(encoding="utf-8")


def top_level_yaml_keys(text):
    keys = set()
    for line in text.splitlines():
        if line and not line.startswith(" ") and not line.startswith("#") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def front_matter(text):
    match = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    return match.group(1) if match else ""


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
        for agent_name in EXPECTED_AGENTS:
            agent_dir = AGENTS_DIR / agent_name
            for required_file in REQUIRED_AGENT_FILES:
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