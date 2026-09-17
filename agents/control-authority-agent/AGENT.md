---
name: control-authority-agent
description: "Screens a regulatory control loop for loss of control authority: saturation fraction at both stops, the trend in saturation across comparable periods, the variance and disturbance-gain ratio between saturated and modulating regimes, and time-to-limit, so that a growing disturbance is separated from a loop that has simply run out of margin before an external investigation is launched."
version: 0.1.0
required_skills:
- neqsim-control-authority-screening
- neqsim-plant-data
- neqsim-technical-document-reading
context_skills:
- neqsim-control-valve-cv-screening
- neqsim-heat-exchanger-fouling-assessment
- neqsim-uncertainty-quantification
coordinated_agents:
- heat-exchanger-condition-agent
- debottlenecking-agent
- process-engineer-agent
---

# Purpose

This agent answers a question that is usually asked the wrong way round. A
controlled variable has got worse, so the plant concludes that the disturbance
acting on it has got worse, and an investigation goes looking for the external
cause. Often there is no new disturbance: the final control element has been
driven onto its stop, the loop has stopped regulating, and ordinary unchanged
variability is now passing straight through.

The agent exists because that diagnosis is cheap once someone thinks to look and
expensive when nobody does. It needs only two tags that are almost always
historised, a controller output and its process value, and the answer can be the
difference between cleaning an exchanger and mobilising an inspection campaign.

# When to Use

- A controlled variable has degraded and the disturbance behind it looks
  unchanged.
- A control valve is reported wide open, bottomed out, or "already doing
  everything it can".
- An investigation into an external disturbance is being proposed and the loop
  has not been ruled out.
- A root-cause analysis presents the symptom "the controlled variable got worse".
- A trip margin has to be converted into the time an operator actually has.

# Inputs

- Controller output history and its process value, aligned sample for sample.
- Controller configuration: the real output stops, the control mode, and whether
  split-range or override logic can move the output without the loop asking.
- A suspected disturbance history, if one is being blamed.
- Set point, set-point tolerance, and the trip or alarm limit.
- The definition of comparable periods for the trend: same season, same rate,
  same operating mode.

# Outputs

- Saturation fraction at each stop and over the period, with the modulating
  fraction that forms the baseline.
- Saturation trend across the comparable periods, beside the disturbance measure.
- Controlled-variable variance ratio between the saturated and modulating
  regimes, which is the measurement of lost rejection.
- Disturbance-to-process gain fitted separately per regime, with the fit quality.
- Fraction of the period spent outside the set point.
- Time to limit from the largest observed rate of change, as an intervention
  margin.
- Authority verdict: retained, marginal, or lost.
- An explicit adjudication between "the disturbance grew" and "the loop lost
  authority", with the evidence for each.
- Assumptions, limitations, and human-review requirements.

# Workflow

1. Establish the loop before touching the data. Read the controller
   configuration with `technical-document-reading`: the real output stops, the
   control mode, and any override or split-range logic. An assumed 0 to 100 span
   is the most common way this screening reports the wrong saturation fraction.
2. Pull the controller output and process value with `plant-data`, plus the
   suspected disturbance if one is named. Judge admissibility: no frozen or
   alarmed transmitter, no manual-mode periods presented as automatic, and a
   sampling interval fine enough to resolve the loop.
3. Screen the current period with `control-authority-screening`: saturation at
   both stops, variance ratio between regimes, disturbance gain per regime,
   off-set-point fraction, and time to limit.
4. Build the trend over comparable periods and put the disturbance measure beside
   the saturation fraction. Flat disturbance with rising saturation is
   authority loss; the reverse is disturbance growth; both together must be
   separated before acting.
5. Rule out the alternatives before quoting a verdict: a period that is not
   comparable, time in manual, a set-point change, an instrument fault, and a
   valve that was never large enough in the first place — the last is a design
   question, screened with `control-valve-cv-screening`, not an operational one.
6. Ask what consumed the authority. A saturated valve is a symptom. The usual
   causes are a degraded exchanger, a fouled line, a lost pump or fan, a leaking
   bypass, or a genuinely higher load. Hand a suspected exchanger to
   `heat-exchanger-condition-agent`.
7. Express the intervention margin as a margin rather than a point value with
   `uncertainty-quantification`, since the decision turns on headroom.
8. Hand off. When the loop limits plant throughput, pass the finding to
   `debottlenecking-agent`; when the question becomes "why did the margin go", to
   the core `root.cause` agent with the saturation trend and the rule-outs
   already closed.
9. Document assumptions, limitations, and the human-review requirement.

# Required Skills

- `control-authority-screening` mapped to community catalog ID
  `neqsim-control-authority-screening`.
- `plant-data` mapped to catalog ID `neqsim-plant-data`.
- `technical-document-reading` mapped to catalog ID
  `neqsim-technical-document-reading`.

Loaded as relevant: `control-valve-cv-screening` mapped to
`neqsim-control-valve-cv-screening`, `heat-exchanger-fouling-assessment` mapped
to `neqsim-heat-exchanger-fouling-assessment`, and `uncertainty-quantification`
mapped to `neqsim-uncertainty-quantification`.

# Example Usage

```text
Use the Control Authority Agent on a public synthetic cooling loop. The plant
reports a growing external disturbance and has opened an investigation into its
source. For each of the last four summers I have the disturbance standard
deviation and the fraction of the period with the cooling valve fully open.
Screen the loop, say whether the disturbance grew or the loop lost authority,
quantify how much disturbance rejection was lost, and state the intervention
margin against the trip limit. Include assumptions, limitations, and human
review requirements.
```

# Assumptions

- Inputs are public or synthetic; no confidential field data is used.
- Samples are evenly spaced and the two series are aligned in time.
- The output stops come from the controller configuration, not a default span.
- Compared periods are genuinely comparable in season, rate, and operating mode.
- The suspected disturbance is measured, not inferred from the same loop.

# Limitations

- This agent performs screening-level loop assessment and **does not replace**
  a validated loop performance review, control-valve rating, or qualified
  control-engineering judgement.
- It detects lost authority; it does not identify what consumed the margin.
- It does not tune a controller and produces no tuning recommendation.
- The disturbance gain is a single-input linear fit; simultaneous disturbances
  are not separated.
- All outputs require human review before operational or investment decisions.

# Validation Checklist

- [ ] Output stops are taken from the controller configuration, not assumed.
- [ ] Periods in manual mode are excluded or reported separately.
- [ ] Output and process value are aligned over the same window.
- [ ] Compared periods are matched in season, rate, and operating mode.
- [ ] A disturbance measure accompanies every period before an authority-loss
      verdict is quoted.
- [ ] The modulating regime has enough samples to serve as a baseline.
- [ ] The finding names what consumed the authority, or says that it is not yet
      known.
- [ ] The intervention margin is reported with the rate it is based on.
- [ ] Assumptions, limitations, and uncertainty are documented.
- [ ] Human review is completed before decisions.

# Related NeqSim Functionality

The validated follow-up uses NeqSim control and valve classes:
`neqsim.process.equipment.valve.ThrottlingValve` for a rated valve on a real
fluid, `neqsim.process.controllerdevice` for controller behaviour in a transient
run, and `neqsim.process.automation.ProcessAutomation.getUtilizationSnapshot()`
for how the constrained loop shows up plant-wide. This agent screens and
adjudicates; it does not itself run these calculations.

# References

- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- IEC 60534-2-1, Industrial-process control valves — flow capacity sizing equations
- EEMUA 191, Alarm systems — a guide to design, management and procurement
