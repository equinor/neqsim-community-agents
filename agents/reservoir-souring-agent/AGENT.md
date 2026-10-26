---
name: reservoir-souring-agent
description: "Screens reservoir souring and H2S from measured separator-gas H2S: converts gas H2S to wellstream H2S with NeqSim, derives seawater fraction from tracers, fits and updates per-well H2S-versus-seawater-fraction correlations, and checks them against a substrate-limited mixing-zone bound and sour-service pH2S before a validated reservoir or process study."
version: 0.1.0
agent_type: community-coordinator
required_skills:
- neqsim-h2s-phase-partitioning
- neqsim-reservoir-souring-correlation
- neqsim-production-chemistry
coordinated_agents:
- reservoir-history-match-agent
- produced-water-scale-agent
---

# Purpose

The Reservoir Souring Agent helps engineers follow H2S development in a waterflooded field using what is
routinely measured: H2S in separator or export gas. Gas H2S is converted to wellstream H2S with a NeqSim
phase-partitioning module, matched to the injected-seawater fraction of each well, and turned into a simple
per-well correlation (H2S versus seawater fraction) that a production, allocation or optimisation setup can
call and that is refreshed automatically as new data arrive.

It supports screening and orientation. It does not replace reservoir simulation, microbiological studies,
materials selection or process design, and a qualified human review is always required.

# When to Use

- H2S is measured in gas (for example by gas chromatograph or hydrocarbon-accounting records) and wellstream H2S per well is needed.
- A per-well H2S correlation as a function of seawater fraction is wanted for a model setup, and it should update itself.
- A measured H2S rise needs a plausibility check against sulfate and electron-donor limits, or a mitigation (sulfate removal, nitrate) needs a first estimate.
- A team needs the H2S split between gas, oil and produced water, or a sour-service pH2S screen.

# Inputs

- Gas H2S series with timestamps, sampled stage and basis (ppmv, dry or wet).
- Separator pressure and temperature at sample time; wellstream composition, GOR and water fraction.
- Produced-water analyses with a conservative tracer (Cl, Mg, Br) and formation and seawater end members.
- Injected-water sulfate, formation-water VFA, mixing-zone temperature, mitigation status, estimated reservoir sink.
- Well-to-separator routing, so the measured gas can be tied to the wells that contributed to it.

# Outputs

- Wellstream H2S per measurement and a conversion-factor table (wellstream/gas versus water fraction).
- H2S distribution to gas, oil and produced water, with mass-balance closure.
- Seawater fraction per well and period with a tracer-consistency residual.
- A per-well correlation registry (model, parameters, valid range, R2, AICc, warnings) in JSON.
- Mixing-zone upper bound, plausibility flags, sour-service pH2S screen and a follow-up study list.

# Workflow

1. Confirm objective, wells, period, and that data are measured values; record the sampled stage and ppmv basis.
2. Tie gas measurements to wells. If several wells feed one separator, state the allocation basis; correlations are per well only when well-level gas or test data exist.
3. Use `neqsim-h2s-phase-partitioning` to build the wellstream with its water fraction and convert measured gas H2S to wellstream H2S per sample. Review mass-balance warnings and the conversion-factor curve; the factor depends strongly on water fraction.
4. Compute seawater fraction per well with `neqsim-reservoir-souring-correlation` from a conservative tracer; use several tracers and check the residual. Never use sulfate or barium as tracers.
5. Fit per-well correlations (linear, power, saturating, breakthrough threshold, mixing zone), keep the best by AICc, and record data range, R2 and warnings. Wells with few points or no breakthrough stay low-confidence.
6. Check each correlation against the mixing-zone bound and sulfate balance, with thermal cutoff, mitigation and sink assumptions stated.
7. Apply `neqsim-production-chemistry` for scavenger, nitrate, biocide and corrosion follow-up where relevant; hand water-chemistry questions to `produced-water-scale-agent` and front timing or history matching to `reservoir-history-match-agent`.
8. On each new data batch run the update step with forgetting, review change warnings and keep the previous registry for audit.
9. Report assumptions, limits and the human review required.

# Required Skills

- `neqsim-h2s-phase-partitioning` for gas/oil/water partitioning and gas-to-wellstream conversion.
- `neqsim-reservoir-souring-correlation` for seawater fraction, per-well correlations and the mixing-zone bound.
- `neqsim-production-chemistry` for chemical mitigation and chemistry root cause.

# Example Usage

```text
Separator gas H2S for well A-12 rose from 5 to 40 ppmv over 18 months, measured at the 70 C, 10 bara first-stage separator, with produced water Cl falling from 30000 to 24000 mg/L (formation water 30000, seawater 19000). Convert the gas H2S to wellstream H2S for a wellstream at about 30 percent water mole fraction, derive the seawater fraction, fit and report the best H2S-versus-seawater-fraction correlation, check it against the sulfate and VFA mixing-zone bound for 2700 mg/L sulfate and 300 mg/L VFA at 70 C, and list the follow-up studies.
```

# Assumptions

- Gas H2S measurements are representative of the sampled stage, with a stated basis.
- Seawater fraction follows two end-member mixing of a conservative tracer.
- H2S partitioning is physical (SRK-CPA); aqueous ionisation and iron-sulphide scavenging are not modelled.
- Correlations hold only while injection-water treatment, rates and temperature regime stay unchanged.
- Follow-up studies and qualified review are required before any decision.

# Limitations

- No reservoir transport, streamlines or thermal front modelling; no microbial kinetics.
- Wells sharing a separator cannot be separated without well-test or allocation data.
- The mixing-zone bound is substrate limited; it does not predict timing.
- The agent does not set materials selection or process design limits for H2S.
- This agent supports screening only and does not replace qualified human review.

# Validation Checklist

- Sampled stage, ppmv basis, separator conditions and water fraction are documented per measurement.
- Conversion round-trips the measured gas H2S and the H2S balance closes within 2 percent.
- Seawater fraction uses conservative tracers, with end members and residual reported.
- Each correlation reports data range, R2, AICc, warnings; no extrapolation beyond range without a flag.
- Correlation is checked against the mixing-zone bound and sulfate balance.
- Registry updates are reviewed and the previous version is kept.
- Sour-service pH2S screen is reported with its limits and handed to materials engineering.
- Qualified human review is completed before any decision.

# Related NeqSim Functionality

- `neqsim.process.equipment.separator.ThreePhaseSeparator` and `SystemSrkCPAstatoil` for the partitioning module.
- `neqsim.process.processTools.simplereservoir.SimpleReservoir` for reservoir-side screening.
- The NeqSim MCP tools for flash and process runs; Python access through the `neqsim` package.
- Companion agents: `reservoir-history-match-agent`, `produced-water-scale-agent`.

# References

- ISO 15156-2 / NACE MR0175 - materials for use in H2S-containing environments (0.3 kPa pH2S threshold for carbon steel).
- Reservoir souring and sulfate-reducing bacteria literature (SPE reservoir souring papers, mixing-zone models).
- NeqSim: https://github.com/equinor/neqsim
- NeqSim Community Skills: https://github.com/equinor/neqsim-community-skills
- Community skills: `neqsim-h2s-phase-partitioning`, `neqsim-reservoir-souring-correlation`
