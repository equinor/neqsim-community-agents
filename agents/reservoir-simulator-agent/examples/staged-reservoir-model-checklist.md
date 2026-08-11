# Walkthrough Checklist — Staged Reservoir Model from Open Data

A public, reproducible walkthrough of the agent's workflow. Use only public data.
Every step names the skill that does the work and the evidence it must leave
behind.

## 1. Frame the study

- [ ] Field, fluid type (gas / oil / gas condensate) and sea area recorded.
- [ ] The decision the model must support is written down.
- [ ] Required maturity stated (orientation, screening, or input to a study).
- [ ] Confirmed that every fact used is public, or supplied by the user.

## 2. Gather public context — `norwegian-continental-shelf-data`

- [ ] Public field record retrieved (operator, sea area, product, status).
- [ ] Reserves and production context retrieved where available.
- [ ] Every reused figure carries its source and reference year.
- [ ] Figures that could not be found are listed as gaps, not invented.

## 3. Establish the fluid basis — `fluid-quality-check`

- [ ] If a composition is supplied, mole fractions sum to 1 and no component is
      negative.
- [ ] Water, CO2 and H2S content flagged for the downstream basis.
- [ ] If no composition exists, this is recorded as the highest-priority gap and
      the model proceeds on fluid type alone.

## 4. Build the first model — `reservoir-model-builder`

- [ ] Sizing basis stated: geometry, in-place volume, or a back-calculated
      recoverable volume.
- [ ] Pressure and temperature either measured or labelled as gradient defaults.
- [ ] Drive mechanism and recovery factor reported with their basis.
- [ ] Data tier and completeness score recorded.
- [ ] The derivation trail is included, not just the results.

## 5. Check consistency

- [ ] All warnings reviewed and each one either resolved or explained.
- [ ] Net pay and net-to-gross are not applied twice.
- [ ] Any divergence between geometry-derived in-place volume and a reported
      recoverable volume is reconciled.
- [ ] The pressure basis is confirmed as virgin or current.
- [ ] Deliverability is either constrained by a PI or a permeability, or is
      explicitly declared unconstrained.

## 6. Cross-check depletion — `reservoir-depletion-screening`

- [ ] Independent pressure-and-production profile versus time produced.
- [ ] Its horizon compared with the plateau the well count supports.
- [ ] Material divergence flagged and explained.

## 7. Place the volumes in context — `resource-classification-screening`

- [ ] Maturity category recorded (reserves / contingent / prospective).
- [ ] The basis for the category is stated.

## 8. Refine as data arrives

- [ ] Each new data source applied as its own refinement batch.
- [ ] Each batch carries its own provenance and source reference.
- [ ] Earlier sources keep their original provenance labels.
- [ ] Change list, tier change and completeness change reported per batch.

## 9. Hand over to NeqSim

- [ ] Specification emitted for `SimpleReservoir` / `WellFlow` / MCP
      `runReservoir`.
- [ ] Volume basis stated: in-situ reservoir volumes, not standard-condition
      volumes.
- [ ] Aquifer volume kept separate from the tank water volume.
- [ ] Production index given in the quadratic MSm3/day/bar^2 form NeqSim expects.

## 10. Report the gaps

- [ ] Ranked data-acquisition plan presented with the acquisition route for each
      item.
- [ ] Top items turned into concrete data requests.
- [ ] The effect each item would have on the model is stated.

## 11. Close out

- [ ] Assumptions, limitations and source attribution documented.
- [ ] Screening-only status stated.
- [ ] Qualified human review recorded as required before any decision.

## Worked example

The community skill ships a runnable three-stage example that follows this
checklist end to end:

```bash
cd ../../neqsim-community-skills/skills/field-development/reservoir-model-builder
python examples/build_wisting_style_model.py
```

It starts from a public headline volume and a depth, adds play-analogue rock
properties, then adds appraisal-well and PVT data, printing the provenance audit
trail and the resulting NeqSim specification at each stage. The figures in that
example are illustrative and must be verified against the public source before
any engineering use.
