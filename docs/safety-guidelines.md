# Safety Guidelines

NeqSim Community Agents are engineering assistants. They help organize analysis, identify checks, generate examples, and document assumptions. They do not replace engineering judgement, qualified discipline review, safety review, regulatory compliance, or operational procedures.

## Engineering Limitations

Agents may provide screening-level outputs, example calculations, checklists, and recommendations for further analysis. These outputs can be incomplete or wrong if inputs are incomplete, assumptions are invalid, models are unsuitable, or context is missing.

Agents must not claim to:

- Certify designs
- Define safe operating limits
- Approve operations
- Replace specialist review
- Replace project assurance
- Guarantee thermodynamic, process, or flow assurance accuracy

## Human Review Requirements

All agents must set `human_review_required: true` in `agent.yaml`.

Human review is required before using agent outputs for:

- Design decisions
- Operational decisions
- Safety-related decisions
- Project sanction or concept selection
- Regulatory submissions
- Procurement or equipment sizing
- Chemical strategy
- Production forecasting or economic decisions

Review should be performed by qualified personnel for the relevant discipline.

## Operational Safety Considerations

Agent outputs may affect how users think about process safety, flow assurance, chemical injection, equipment limits, and operating envelopes. Treat outputs as decision support only.

Before operational use, users must verify:

- Input data source and quality
- Unit consistency
- Model suitability
- Assumptions and boundary conditions
- Sensitivity to uncertainty
- Applicable procedures and standards
- Required discipline and safety reviews

## Model Limitations

AI-generated outputs may contain reasoning errors, omissions, unsupported assumptions, or incorrect references. NeqSim examples may require adaptation to the user's installed version and must be validated.

Agents should:

- Separate facts, assumptions, and recommendations
- Identify missing information
- Explain uncertainty
- Avoid unsupported confidence
- Provide reproducible workflow steps
- Ask for human review where conclusions matter

## Responsible AI Principles

Agents in this repository should follow responsible AI principles:

- Transparency: document workflow, inputs, outputs, assumptions, and limitations
- Accountability: require human review for engineering decisions
- Reproducibility: use public examples and clear steps
- Privacy: do not include personal data or credentials
- Security: do not include secrets or confidential procedures
- Fairness and openness: make contributions suitable for public review and reuse

## Public Example Safety

Examples must use public, synthetic, or educational data. They should not be copied from confidential projects or presented as validated designs.

Every example should include a short human review statement.