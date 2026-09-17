# Example: Cooling-Medium Cooler Condition Assessment (Public Synthetic Case)

This example uses a public, synthetic exchanger. No confidential data is used.
Numbers are produced by the `heat-exchanger-fouling-assessment` skill example.

## Design basis (from the data sheet)

| Item | Value |
| --- | --- |
| Area (3 parallel units) | 420 m2 |
| Design overall coefficient | 1250 W/(m2 K) |
| Design fouling allowance | 2.0 x 10^-4 m2 K/W |
| Design hot flow | 220 kg/s |
| Design cold flow | 300 kg/s |

## Operating snapshot

| Item | Hot side | Cold side |
| --- | --- | --- |
| Mass flow | 180 kg/s | 260 kg/s |
| Specific heat | 3.6 kJ/(kg K) | 4.0 kJ/(kg K) |
| Inlet temperature | 65.0 degC | 15.0 degC |
| Outlet temperature | 45.0 degC | 27.5 degC |

Duty from the hot side 12 960 kW, from the cold side 13 000 kW, imbalance 0.3 %,
so the reconciliation is trusted and 12 980 kW is used. Terminal differences are
37.5 K and 30.0 K, so the LMTD of 33.6 K is well conditioned and the coefficient
is taken on the LMTD basis.

## Reduction

| Quantity | Value |
| --- | --- |
| Measured U at operating flow | 919 W/(m2 K) |
| U normalised to design flow, two-sided form | 1001 W/(m2 K) — **80 % of design** |
| U normalised, one-sided form | 1080 W/(m2 K) — 86 % of design |
| Optimism introduced by the one-sided form | **6.3 percentage points** |
| Fouling resistance | 3.99 x 10^-4 m2 K/W |
| Excess over design allowance | 1.99 x 10^-4 m2 K/W |
| Condition | fouled |

The one-sided form scales the whole coefficient, deposit included, by the flow
ratio. Below design flow that always reports the exchanger as healthier than it
is, and here it would have hidden a fifth of the degradation.

## Maldistribution rule-out

| Units credited | Credited area | Apparent U | Fraction of design |
| --- | --- | --- | --- |
| 3 | 420 m2 | 919 W/(m2 K) | 0.74 |
| 2 | 280 m2 | 1379 W/(m2 K) | 1.10 |
| 1 | 140 m2 | 2758 W/(m2 K) | 2.21 |

Crediting two units would require the surviving units to run 10 % above their
clean design coefficient, which they cannot. The shortfall is therefore a film
and fouling effect on all three units, not one unit bypassing.

## Capacity translation

With the cooling medium supplied at 25 degC in the warm season and a 45 degC
supply set point to hold, the maximum duty is 8 662 kW against the 12 980 kW
being asked of it. The exchanger is limited, and the binding constraint is the
**temperature approach**, not a valve or a pump. Opening the control valve
further cannot recover the duty.

## Cleaning

From 2.0 x 10^-5 to 3.99 x 10^-4 m2 K/W over 180 days the fouling rate is
2.1 x 10^-6 m2 K/W per day. Against a 6.0 x 10^-4 limit that leaves 96 days of
run time. A perfect clean supports a 285-day cycle; a clean that leaves 40 % of
the deposit behind supports 209 days. If a clean were to leave 90 % behind, no
interval would recover the duty and the cleaning method itself would have to
change.

## Outcome

The bank is fouled to 80 % of design, roughly double its design fouling
allowance, and is already capacity-limiting in warm-season conditions. Cleaning
is justified; cleaning **effectiveness** should be specified and verified, since
frequency alone cannot compensate for a poor clean.

**Human review required.** This screening does not replace vendor rating
software, a validated NeqSim thermal study, or qualified engineering judgement.
