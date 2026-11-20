"""Guardrail and neutrality checks for the flare-helideck dispersion agent."""

import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = REPO_ROOT / "agents" / "flare-helideck-dispersion-agent"
# built from fragments so that this file does not contain the terms itself
BANNED = [
    "equi" + "nor",
    "gull" + "faks",
    "st" + "id",
    "ec" + "ho 3d",
    "tr" + "1965",
    "tr" + "2237",
    "tr" + "3001",
]


def agent_texts():
    for path in sorted(AGENT_DIR.rglob("*")):
        if path.is_file() and path.suffix in {".md", ".yaml"}:
            yield path, path.read_text(encoding="utf-8")


class FlareHelideckDispersionAgentTests(unittest.TestCase):
    def setUp(self):
        self.manifest = yaml.safe_load(
            (AGENT_DIR / "agent.yaml").read_text(encoding="utf-8")
        )
        self.agent_md = (AGENT_DIR / "AGENT.md").read_text(encoding="utf-8")
        catalog = yaml.safe_load(
            (REPO_ROOT / "community-agents.yaml").read_text(encoding="utf-8")
        )
        self.catalog = catalog
        self.entry = next(
            a
            for a in catalog["agents"]
            if a["name"] == "flare-helideck-dispersion-agent"
        )

    def test_manifest_basics(self):
        self.assertEqual(self.manifest["version"], "0.1.0")
        self.assertEqual(self.manifest["status"], "draft")
        self.assertIs(self.manifest["human_review_required"], True)
        self.assertEqual(self.manifest["agent_type"], "community-coordinator")
        self.assertIn(
            "neqsim-flare-helideck-dispersion", self.manifest["required_skills"]
        )

    def test_catalog_entry_matches_manifest(self):
        for key in (
            "version",
            "description",
            "required_skills",
            "context_skills",
            "coordinated_agents",
            "status",
            "agent_type",
        ):
            self.assertEqual(self.entry[key], self.manifest[key], key)

    def test_coordinated_agents_exist_in_the_catalog(self):
        names = {a["name"] for a in self.catalog["agents"]}
        for agent in self.manifest["coordinated_agents"]:
            self.assertIn(agent, names)
            self.assertNotEqual(agent, self.manifest["name"])
        self.assertTrue(
            {"installation-weather-agent", "process-safety-agent"}
            <= set(self.manifest["coordinated_agents"])
        )

    def test_guardrails_are_documented(self):
        text = self.agent_md.lower()
        for phrase in (
            "conditional on an unignited release",
            "no annual frequency without a flame-out frequency",
            "flight paths are labelled assumptions unless supplied",
            "tip-inclination sensitivity is always reported",
            "flagged for human review",
            "schematic, not registered to the camera",
            "both 10 % and 20 % lfl are reported",
            "does not replace",
        ):
            self.assertIn(phrase, text)

    def test_workflow_and_review_checklist(self):
        text = self.agent_md.lower()
        order = [
            "freeze the basis",
            "wind statistics",
            "release rates",
            "run the toolkit",
            "independent review",
            "figures and results",
            "cfd hand-off",
        ]
        positions = [text.index(f"**{step}") for step in order]
        self.assertEqual(positions, sorted(positions))
        for item in (
            "stable-air limits",
            "free-jet distance",
            "5 degrees or finer",
            "1.0 m/s",
            "20 to 70 degrees",
            "neutral",
            "wake",
        ):
            self.assertIn(item, text)

    def test_no_vendor_or_site_identifiers(self):
        hits = []
        for path, text in agent_texts():
            lowered = text.lower()
            for term in BANNED:
                if term in lowered:
                    hits.append(f"{path.name}: {term}")
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
