# Community Router Agent

Front door for the public NeqSim community agent catalog.

Describe an engineering job in plain language and this agent classifies the
request and routes it to the right community agent — or composes a short
multi-agent pipeline when the task spans disciplines. It performs no engineering
and reads no data itself.

Use it after a community-only install, where the core NeqSim repository's own
routing agent is not present:

```powershell
neqsim agent install --all --source community --vscode --force
```

## What it does

1. Extracts the intent, the system in scope, and the intended deliverable.
2. Classifies the request against a routing table covering the full community catalog.
3. Prefers a coordinator agent over a leaf specialist so its internal workflow is reused.
4. Compares the required rigor against the route's `calculation_basis`
   (`screening` versus `neqsim-java`) and names the NeqSim-backed follow-up when
   a design-grade number is needed.
5. Lists the inputs the selected agent needs and flags the missing ones.

## What it does not do

- No engineering calculation, no data retrieval, no numeric result.
- Routes only within the **community** catalog. Enterprise (Equinor-internal)
  agents and the core NeqSim task-solving agents are named as prerequisites, not
  routed to.
- Routing is a suggestion; it does not replace engineering judgement.

## Files

| File | Purpose |
|------|---------|
| `AGENT.md` | Agent definition, workflow, and routing table |
| `agent.yaml` | Machine-readable manifest (`coordinated_agents` = the routable catalog) |

## Related

- [NeqSim Community Agents](https://github.com/equinor/neqsim-community-agents)
- [NeqSim Skills Guide](https://github.com/equinor/neqsim/blob/master/docs/integration/skills_guide.md)
