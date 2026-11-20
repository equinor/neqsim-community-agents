# Example: subsea gas-condensate producer (synthetic)

Request: "Plan a gas-condensate producer on a subsea tie-back (1.2 MSm3/d, 90 bara host, 8 km flowline). Compare tubing sizes and tell me what you cannot assess."

Agent flow: init-study for `gas_condensate_producer` / `subsea`; the basis lists PVT, water chemistry, wax appearance temperature and approved limits as data gaps; `run-model` gives low/base/high operating points with the condensate-banking IPR, the drift-flux tubing and flowline back pressure; hydrate margin and MEG basis come from the CPA hydrate model; scale is NOT_PERFORMED, transient cooldown and slugging are EXTERNAL_TOOL_REQUIRED. `alternatives` compares tubing sizes with the erosional ratio as the binding constraint; the VFP request goes to `vfp-lift-curve-agent` and the flow-assurance requirements to `flow-assurance-study-agent`.

Result: report with readiness label SCREENING - FOR REVIEW, operating-envelope table (NEEDS_REVIEW where limits are not approved), barrier schematics (UNVERIFIED), capability ledger and open actions. All values in this example are synthetic.
