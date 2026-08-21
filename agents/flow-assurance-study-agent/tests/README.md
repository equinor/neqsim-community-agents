# Validation Notes

Repository tests validate the package structure, manifest schema, canonical
context-skill resolution, coordinated-agent resolution, and catalog consistency.

The coordinator has no calculation implementation. Behavioral validation is by
reviewing that each scenario is delegated once, every returned result retains its
source and limitations, and no model comparison is accepted before the documented
input-equivalence and convergence gates pass.
