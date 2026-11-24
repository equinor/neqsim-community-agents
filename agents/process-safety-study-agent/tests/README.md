# Validation Notes

Repository tests validate the package structure, manifest schema, canonical skill resolution, coordinated-agent resolution and catalog consistency.

The coordinator has no calculation implementation. Behavioural validation is by review: each step is delegated once, every returned result keeps its source and evidence status, no document is treated as read without its text, and the gates of `neqsim-process-safety-study` (tested in the skill repository) are run before a result is carried forward.
