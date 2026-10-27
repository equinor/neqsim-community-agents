# Technology Qualification Agent

General technology-qualification evaluation for any technology a project may need:
qualification basis, technology assessment (novelty, TRL, step-out, role), failure-mode
ranking (FMIRR), a preliminary qualification outline, and a full technology assessment
report that a project study can deliver.

## Status

Draft (version 0.1.0). Public, general method. Company governance (gates, approvals,
templates) belongs in the enterprise overlay agent.

## What it does

- Builds the technology qualification basis and decomposes the technology.
- Categorises novelty and TRL per element and for the system.
- Classifies the technology as enabling or enhancing and defines step-out.
- Registers and ranks failure modes and links critical ones to qualification tests.
- Writes the technology assessment report in Markdown and Word with an issues list.

## Required skills

- `neqsim-technology-assessment`
- `neqsim-technology-fmirr`
- `neqsim-technology-assessment-report`

## Human review

The agent structures judgement and evidence. It **does not qualify** a technology and
does not replace an expert panel. All outputs require human review.
