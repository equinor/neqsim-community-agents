# Fluid Commingling Agent

Checks whether two fluids that will be mixed behave worse together than apart,
and at which blend ratio. Typical cases are a tie-in into a host, two zones in
one well, gas lift into heavy oil, or a new well sharing a flowline. The agent
runs a NeqSim blend sweep and returns the worst ratio for each check, with the
laboratory test that should confirm it.

## Capabilities

- Asphaltene destabilisation by dilution: live-oil refractive index along the
  depressurisation path against the onset value, with de Boer for comparison
- Asphaltene onset pressure of every blend when the host onset was measured:
  a solid model calibrated on the host alone (light diluents raise the onset)
- Gas breakout where two single-phase streams meet
- Blend hydrate temperature, including maxima above both fluids
- Separator-gas H2S and CO2 of the mixture against limits
- Blend wax appearance temperature and calcium naphthenate risk
- Water-water scale when both streams carry water
- Converts planned mass rates to the operating point on the molar blend axis

## How to Use

1. Install the agent and its skills (see the
   [installation guide](../../docs/installation-guide.md)):

   ```bash
   neqsim agent install fluid-commingling-agent --vscode
   ```

2. In Copilot Chat, call `@fluid-commingling-agent` and describe the case.
   Give as much of this as you have:

   | Input | Example | If missing |
   | --- | --- | --- |
   | Both compositions with C7+ cuts (molar mass, density) | PVT report tables | The agent asks; it cannot screen without them |
   | Which fluid carries asphaltenes, and its onset refractive index | "host oil, onset RI 1.445" | SARA gives a correlation estimate; with neither, only a relative result |
   | Measured asphaltene onset pressure of that fluid | "150 bara at 80 C (HPM)" | No onset pressures; refractive-index result only |
   | Commingling pressure and temperature | 200 bara, 80 C | The agent asks |
   | Planned rates of both streams | 150 t/h oil, 25 t/h condensate | A default grid of ratios is used |
   | Separator conditions, hydrate pressure, minimum operating temperature | 40 bara / 60 C, 120 bara, 25 C | Those checks are skipped |
   | Limits | H2S 400 ppm, CO2 3 mol % | Values are reported without a pass/fail |
   | Water analyses of both streams | Ion tables | The water-water scale check is skipped |

3. Example prompt:

   ```text
   @fluid-commingling-agent A gas condensate (composition attached) will be tied
   into our host, whose oil has had asphaltene deposits; its onset refractive
   index is 1.445. The streams meet at 200 bara and 80 C. Planned rates are
   150 t/h oil and 25 t/h condensate. Separator 40 bara / 60 C, H2S limit 400 ppm.
   Which blend ratios are a problem, and where is our operating point?
   ```

   With a measured onset pressure:

   ```text
   @fluid-commingling-agent Same case. The host's asphaltene onset is 150 bara at
   80 C (HPM test). At what condensate share does the onset reach our 200 bara
   commingling pressure?
   ```

   Public example result (synthetic data, NeqSim): onset 150, 166, 179, 187 and
   208 bara at 0, 20, 40, 60 and 80 mol % condensate; the 80 % blend
   precipitates where the streams meet.

4. What you get back: the operating point as a mole fraction, findings by
   severity, the blend table, the worst ratio per check, recommended laboratory
   tests, assumptions and a validation checklist. Example output is in
   [examples/condensate-into-asphaltenic-host.md](examples/condensate-into-asphaltenic-host.md).

5. Follow-ups the agent can hand over:
   - `@tie-in-screening-agent` to place the result in the wider tie-in screen
   - `@produced-water-scale-agent` for a fuller water-chemistry study
   - `@surrogate-study-agent` to map the compatibility boundary over blend
     ratio, pressure and temperature with a few dozen NeqSim runs

More prompts are in [prompts/example-prompts.md](prompts/example-prompts.md).

## Required Skills

- `neqsim-fluid-commingling-compatibility`
- `neqsim-produced-water-scale-screening`
- `neqsim-fluid-quality-check`

## Directory Contents

- [AGENT.md](AGENT.md) defines the agent: purpose, workflow, limitations.
- [agent.yaml](agent.yaml) defines machine-readable metadata.
- [examples/](examples/) contains a public worked example.
- [prompts/](prompts/) contains reusable prompts.
- [tests/](tests/) describes how the agent and its skill are tested.

## Human Review

Results are screening-level and rank blend ratios. They need laboratory
compatibility testing (onset titration, HPM), a flow assurance study and
qualified review before any design or operating decision. The agent does not
predict how much asphaltene deposits, or how fast.
