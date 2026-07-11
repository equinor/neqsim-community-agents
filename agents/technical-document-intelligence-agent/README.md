# Technical Document Intelligence Agent

This community agent is the source-intake front door for NeqSim tasks. It combines native document parsing, OCR, and multimodal image interpretation through a common evidence contract, then routes the reviewed output to the appropriate engineering specialist.

The agent does not assume that visible text is sufficient. Drawings, charts, layouts, symbols, and topology require vision or document-specific tools, while spreadsheets and digital documents should retain their native structure.

Human review is mandatory for gated facts. This agent does not replace engineering judgement,
document control, or qualified interpretation of safety-critical information.
