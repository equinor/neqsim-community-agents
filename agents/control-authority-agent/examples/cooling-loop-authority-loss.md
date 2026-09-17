# Example: Cooling Loop Reported as a Growing Disturbance (Public Synthetic Case)

This example uses a public, synthetic loop. No confidential data is used. Numbers
are produced by the `control-authority-screening` skill.

## The complaint

A cooling loop is reported to be suffering from an increasing external
disturbance. An investigation into the source of that disturbance has been
running for some time, and an inspection campaign has already been mobilised.

## Multi-period evidence

Four comparable summers, each with the disturbance standard deviation and the
fraction of the period with the cooling valve fully open:

| Period | Disturbance sigma [K] | Output saturated |
| --- | --- | --- |
| year 1 | 1.03 | 25 % |
| year 2 | 0.70 | 45 % |
| year 3 | 0.98 | 53 % |
| year 4 | 1.11 | **78 %** |

| Quantity | Value |
| --- | --- |
| Saturation change | **+0.53** (25 % to 78 %) |
| Disturbance relative change | +8 % |
| Verdict | **control-authority-loss** |

The disturbance is flat across four years; saturation tripled. Nothing is wrong
with the disturbance — the plant lost the ability to absorb it. The investigation
into the source of the disturbance is looking in the wrong place.

## Single-period reduction (year 4, 24 hourly samples)

Set point 19.0 degC with a 0.5 K tolerance, trip limit 26.0 degC, output stops
0 to 100 % with a 1 % saturation band.

| Quantity | Value |
| --- | --- |
| Saturation fraction (upper stop) | 0.42 |
| Modulating fraction | 0.58 |
| Controlled-variable std, saturated | 1.22 K |
| Controlled-variable std, modulating | 0.25 K |
| **Variance ratio, saturated / modulating** | **23.4** |
| Disturbance gain, saturated | 0.84 at r-squared 0.06 |
| Disturbance gain, modulating | 0.05 at r-squared 0.03 |
| Time outside set point | 42 % |
| Largest observed rate | 1.6 K/h |
| Margin to trip limit | 7.3 K |
| **Time to limit** | **4.5 h** |
| Authority status | authority-marginal |

Two findings come straight off these numbers.

**Disturbance rejection has collapsed, not the disturbance grown.** While the
valve modulates, the loop holds the set point to a quarter of a kelvin. While it
is on its stop, the spread is more than twenty times wider. That factor is the
measurement of what the loop used to absorb and no longer does, in the units the
complaint was made in.

**The suspected disturbance is not the cause.** Its gain looks substantial at
0.84, but the fit is worthless: r-squared 0.06 means it accounts for about 6 % of
the saturated variance. A gain quoted without its fit quality is how a plausible
number survives a review, so the screening raises the weak fit as its own finding
rather than letting the slope stand alone.

## Rule-outs applied before the verdict

- Periods are the same season at comparable rate and operating mode.
- No time in manual mode is presented as automatic.
- Both output stops are counted; this loop only saturates on the upper stop.
- The valve was not undersized from new — that would be a design question for
  `control-valve-cv-screening`, not an operational one.

## What consumed the authority

A saturated valve is a symptom. The screening says the margin is gone; it does
not say where it went. The usual candidates are a degraded exchanger, a fouled
line, a lost pump or fan, a leaking bypass, or a genuinely higher load. Here the
handoff is to `heat-exchanger-condition-agent`, since a cooler drifting from its
design coefficient is the most common way a cooling loop runs out of valve.

## Outcome

The loop, not the disturbance, is the finding. The immediate operability issue is
that four and a half hours of margin remain against the trip at the observed rate
of change. The investigation into the external disturbance should be closed
pending the exchanger screening, and a validated loop review and NeqSim thermal
study should carry the decision.
