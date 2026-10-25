# Example: Long List to Short List (Public Synthetic Oil Discovery)

This example uses a public, synthetic opportunity. No confidential data is used.
The numbers below are the output of `examples/basic_screening.py` in the
`neqsim-concept-longlist-shortlist-screening` skill, with synthetic scores.

## Opportunity

- Deepwater oil discovery with associated gas, early maturity.
- No existing host within 60 km.
- Givens: subsea wells, water injection as drive.

## Framing

| Element | Options |
| --- | --- |
| Host | FPSO, semi-submersible, subsea tie-back, subsea to shore |
| Oil export | shuttle tanker, pipeline, via host |
| Gas disposal | reinjection, export pipeline, via host |
| Power | gas turbine, power from shore, power from host |

The default compatibility rules apply: a tie-back exports, disposes and takes
power through its host; a standalone floater cannot route "via host"; and
subsea-to-shore exports by pipeline and takes power from shore.

## Screening summary

| Step | Result |
| --- | --- |
| Long list | 108 combinations, 90 excluded by rules, 18 compatible concepts, 18 distinct topologies |
| Must-pass | The subsea tie-back concept is eliminated: no host within 60 km (evidenced) |
| Ranking | Leader: FPSO, pipeline oil export, gas reinjection, gas turbines |
| Crossovers | A semi-submersible with power from shore leads when the CO2 weight exceeds 0.37 (base 0.20); FPSO with power from shore leads when the NPV weight falls below 0.14 (base 0.40) |
| Short list | FPSO with pipeline export (leader); semi-submersible with power from shore (robust contender, top three in 71 % of weight samples); FPSO with shuttle tanker (reference case) |

## Outcome

The short list and reference case go to `concept-selection-agent` for the
detailed comparison. The crossovers tell the decision owner which weight
preference would change the leader.

**Human review required.** This screening does not replace a validated study and
does not select a concept.
