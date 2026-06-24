"""End-to-end reservoir-to-host screening for an example gas field.

This script couples two public community skills to show how a reservoir fluid is
screened from the reservoir, through wells and a manifold, along a flowline and
riser, to the arrival pressure at a host platform - and how that develops with
time as the reservoir depletes.

Chain:
  1. reservoir-depletion-screening  -> reservoir pressure vs time
  2. production-network-routing      -> wells -> manifold -> flowline/riser -> host

It is a transparent screening placeholder only. Real work must use validated
NeqSim tools: SimpleReservoir (runTransient), PipeBeggsAndBrills, and the NeqSim
MCP runReservoir / runPipeline / runProcess / runFlowAssurance workflows.

Run from this folder:
    python reservoir_to_host_example.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# --- Make the two community skill packages importable (src/ layout) ----------
SKILLS_ROOT = (
    Path(__file__).resolve().parents[4] / "neqsim-community-skills" / "skills"
)
for rel in (
    "field-development/reservoir-depletion-screening/src",
    "subsea/production-network-routing/src",
):
    sys.path.insert(0, str(SKILLS_ROOT / rel))

from production_network_routing import ProductionNetworkModel  # noqa: E402
from reservoir_depletion_screening import ReservoirDepletionModel  # noqa: E402


# --- Example case ------------------------------------------------------------
# A small subsea gas field: two wells route through one manifold, then an 8 km
# flowline and a 20 bar riser bring the fluid to a host that needs 90 bara.

FLUID_TYPE = "gas"
INITIAL_PRESSURE_BARA = 300.0
ABANDONMENT_PRESSURE_BARA = 80.0
RECOVERABLE_VOLUME_SM3 = 20.0e9  # 20 Gsm3 recoverable gas
OFFTAKE_RATE_SM3_PER_DAY = 8.0e6  # 8 MSm3/day plateau target
YEARS = 15.0

REQUIRED_ARRIVAL_BARA = 90.0

# Screening hydraulic offsets held constant over field life (placeholders):
DRAWDOWN_BAR = 30.0  # reservoir -> flowing bottomhole pressure
TUBING_LOSS_BAR = 40.0  # flowing bottomhole -> tubing head (well + completion)

WELLS = (
    {"name": "WELL-A", "manifold": "MAN-1", "pi": 1.0e5},
    {"name": "WELL-B", "manifold": "MAN-1", "pi": 0.9e5},
)
MANIFOLD = {
    "name": "MAN-1",
    "flowline_length_km": 8.0,
    "pressure_gradient_bar_per_km": 1.5,
    "riser_dp_bar": 20.0,
}


def main() -> None:
    # --- Step 1: reservoir pressure vs time ---------------------------------
    reservoir_model = ReservoirDepletionModel()
    depletion = reservoir_model.evaluate(
        fluid_type=FLUID_TYPE,
        initial_pressure_bara=INITIAL_PRESSURE_BARA,
        abandonment_pressure_bara=ABANDONMENT_PRESSURE_BARA,
        recoverable_volume_sm3=RECOVERABLE_VOLUME_SM3,
        offtake_rate_sm3_per_day=OFFTAKE_RATE_SM3_PER_DAY,
        years=YEARS,
    )

    print("=" * 72)
    print("RESERVOIR-TO-HOST SCREENING (example gas field)")
    print("=" * 72)
    print(f"Fluid                : {depletion.fluid_type}")
    print(f"Initial pressure     : {depletion.initial_pressure_bara:.1f} bara")
    print(f"Abandonment pressure : {depletion.abandonment_pressure_bara:.1f} bara")
    print(f"Recoverable volume   : {RECOVERABLE_VOLUME_SM3 / 1e9:.1f} Gsm3")
    print(f"Required arrival     : {REQUIRED_ARRIVAL_BARA:.1f} bara at host")
    print(f"Reservoir verdict    : {depletion.depletion_warning}")
    print()

    # --- Step 2: route wells -> manifold -> host for each year ---------------
    network_model = ProductionNetworkModel()

    header = (
        f"{'Year':>4} {'Pres':>7} {'WellTHP':>8} {'Rate':>11} "
        f"{'Arrival':>8} {'Margin':>8}  Verdict"
    )
    print(header)
    print("-" * len(header))

    first_shortfall_year = None
    for step in depletion.steps:
        res_p = step.pressure_bara
        bottomhole = max(0.0, res_p - DRAWDOWN_BAR)
        well_thp = bottomhole - TUBING_LOSS_BAR

        if well_thp <= 0.0:
            # Reservoir too depleted to lift to the tree at the assumed offsets.
            print(
                f"{step.year:>4.0f} {res_p:7.1f} {'shut-in':>8} "
                f"{0:11.0f} {'n/a':>8} {'n/a':>8}  high"
            )
            if first_shortfall_year is None:
                first_shortfall_year = step.year
            continue

        wells = [
            {
                "name": w["name"],
                "manifold": w["manifold"],
                "reservoir_pressure_bara": res_p,
                "flowing_bottomhole_pressure_bara": bottomhole,
                "productivity_index_sm3_per_day_bar": w["pi"],
                "tubing_head_pressure_bara": well_thp,
            }
            for w in WELLS
        ]

        network = network_model.evaluate(
            wells=wells,
            manifolds=[MANIFOLD],
            host_name="HOST",
            required_arrival_pressure_bara=REQUIRED_ARRIVAL_BARA,
        )

        man = network.manifolds[0]
        arrival = man.arrival_pressure_bara
        margin = man.arrival_margin_bar
        arrival_str = "n/a" if arrival is None else f"{arrival:8.1f}"
        margin_str = "n/a" if margin is None else f"{margin:8.1f}"

        if (
            first_shortfall_year is None
            and margin is not None
            and margin < 0.0
        ):
            first_shortfall_year = step.year

        print(
            f"{step.year:>4.0f} {res_p:7.1f} {well_thp:8.1f} "
            f"{network.total_rate_sm3_per_day:11.0f} "
            f"{arrival_str} {margin_str}  {man.arrival_warning}"
        )

    print()
    if first_shortfall_year is None:
        print("Arrival pressure stays above the host requirement over the horizon.")
    else:
        print(
            "Screening arrival pressure falls below the host requirement "
            f"around year {first_shortfall_year:.0f}."
        )

    print()
    print("NOTE: screening placeholder only. For design-grade results use NeqSim")
    print("SimpleReservoir (runTransient), PipeBeggsAndBrills, and MCP")
    print("runReservoir / runPipeline / runProcess / runFlowAssurance. Qualified")
    print("human review is required before any decision.")


if __name__ == "__main__":
    main()
