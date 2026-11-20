# Workflow: integrated well planning

| Step | Command or action | Output | Gate |
|---|---|---|---|
| 1 | `<python> -m integrated_well_planning init-study FOLDER --well-type TYPE --environment ENV` | study folder, starting basis, registers | basis exists |
| 2 | fill the basis; identify jurisdiction and requirements | standards register (TO_VERIFY) | gaps listed with consequences |
| 3 | request fluid, trajectory, host and reservoir inputs from the specialist agents; merge with SUPPLIED provenance | updated basis | schema-valid messages |
| 4 | `validate-basis FOLDER` | `results/validation.json` | no errors (fail-closed) |
| 5 | `run-model FOLDER` | `results/model_results.json`, envelope, hand-offs | wellplanning classes available |
| 6 | `alternatives FOLDER --profile-years 0,5,10` | scorecard, Pareto, tornado, deliverability bands | weights and missing criteria stated |
| 7 | add approved limits with sources; `envelope FOLDER` | envelope table | NEEDS_REVIEW rows have an action |
| 8 | send VFP request, flow-assurance requirements, integrity inputs, cost/profile | hand-off log | decisions and actions logged |
| 9 | `drawings FOLDER`, `report FOLDER` | A3 sheets, figures, report | readiness label, ledger, open actions |

Single calculations (flash, saturation pressure, standards lookup, sizing) go through the curated mcp_neqsim tools first.
