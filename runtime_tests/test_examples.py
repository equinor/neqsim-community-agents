import runpy
from pathlib import Path

EXAMPLES = (
    Path(__file__).resolve().parents[1]
    / "agents"
    / "reservoir-to-facility-screening-agent"
    / "examples"
)


def test_reservoir_to_host_example_executes(capsys):
    runpy.run_path(str(EXAMPLES / "reservoir_to_host_example.py"), run_name="__main__")

    output = capsys.readouterr().out
    assert "RESERVOIR-TO-HOST SCREENING" in output
    assert "Screening arrival pressure falls below" in output


def test_planning_example_executes_without_plotting():
    example = runpy.run_path(str(EXAMPLES / "reservoir_to_host_planning.py"))

    result = example["run_chain"](example["BASE_OFFTAKE_SM3_PER_DAY"])

    assert len(result["years"]) == len(result["reservoir_p"])
    assert len(result["years"]) > 1
    assert result["reservoir_p"][-1] < result["reservoir_p"][0]
    assert result["cumulative"][-1] > result["cumulative"][0]
    assert result["first_shortfall_year"] is not None
