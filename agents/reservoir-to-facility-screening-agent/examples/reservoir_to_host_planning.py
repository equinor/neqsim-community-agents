"""Reservoir-to-host screening illustrated for production planning & optimization.

This builds on ``reservoir_to_host_example.py`` and turns the same two-skill chain
into a picture an engineer can use for early production planning:

  * Panel 1 - pressure development (reservoir, well THP, host arrival) with the
    host requirement line and the feasible production window shaded.
  * Panel 2 - field production rate vs time (plateau, decline, shut-in).
  * Panel 3 - cumulative production and recovery factor vs time.
  * Panel 4 - an OPTIMIZATION sweep: how the chosen plateau offtake rate trades
    off against how many years the host arrival-pressure constraint is met
    (i.e. how long you can produce before boosting/compression is needed).

Chain (both are public community skills):
  1. reservoir-depletion-screening  -> reservoir pressure vs time
  2. production-network-routing      -> wells -> manifold -> flowline/riser -> host

It is a transparent screening placeholder only. Real planning must use validated
NeqSim tools: SimpleReservoir (runTransient), PipeBeggsAndBrills, and the NeqSim
MCP runReservoir / runPipeline / runProcess / runFlowAssurance workflows, with
qualified human review.

Run from this folder:
    python reservoir_to_host_planning.py
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
FLUID_TYPE = "gas"
INITIAL_PRESSURE_BARA = 300.0
ABANDONMENT_PRESSURE_BARA = 80.0
RECOVERABLE_VOLUME_SM3 = 20.0e9  # 20 Gsm3 recoverable gas
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

# Plateau offtake rates to compare in the optimization sweep [Sm3/day].
OFFTAKE_SWEEP_SM3_PER_DAY = (4.0e6, 6.0e6, 8.0e6, 10.0e6, 12.0e6)
BASE_OFFTAKE_SM3_PER_DAY = 8.0e6


def run_chain(offtake_rate_sm3_per_day: float) -> dict:
    """Run the reservoir -> host chain for one plateau offtake rate.

    :param offtake_rate_sm3_per_day: plateau offtake target [Sm3/day].
    :return: dict of per-year time series and a summary feasibility window.
    """
    reservoir_model = ReservoirDepletionModel()
    depletion = reservoir_model.evaluate(
        fluid_type=FLUID_TYPE,
        initial_pressure_bara=INITIAL_PRESSURE_BARA,
        abandonment_pressure_bara=ABANDONMENT_PRESSURE_BARA,
        recoverable_volume_sm3=RECOVERABLE_VOLUME_SM3,
        offtake_rate_sm3_per_day=offtake_rate_sm3_per_day,
        years=YEARS,
    )

    network_model = ProductionNetworkModel()

    years: list[float] = []
    reservoir_p: list[float] = []
    well_thp: list[float] = []
    arrival_p: list[float] = []
    field_rate: list[float] = []
    cumulative: list[float] = []
    recovery: list[float] = []

    first_shortfall_year = None
    feasible_years = 0

    for step in depletion.steps:
        res_p = step.pressure_bara
        bottomhole = max(0.0, res_p - DRAWDOWN_BAR)
        thp = bottomhole - TUBING_LOSS_BAR

        years.append(step.year)
        reservoir_p.append(res_p)
        cumulative.append(step.cumulative_production_sm3)
        recovery.append(step.recovery_factor)

        if thp <= 0.0:
            well_thp.append(0.0)
            arrival_p.append(float("nan"))
            field_rate.append(0.0)
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
                "tubing_head_pressure_bara": thp,
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

        well_thp.append(thp)
        arrival_p.append(float("nan") if arrival is None else arrival)
        field_rate.append(network.total_rate_sm3_per_day)

        if margin is not None and margin >= 0.0:
            feasible_years += 1
        elif first_shortfall_year is None and margin is not None and margin < 0.0:
            first_shortfall_year = step.year

    return {
        "years": years,
        "reservoir_p": reservoir_p,
        "well_thp": well_thp,
        "arrival_p": arrival_p,
        "field_rate": field_rate,
        "cumulative": cumulative,
        "recovery": recovery,
        "first_shortfall_year": first_shortfall_year,
        "feasible_years": feasible_years,
    }


def main() -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is required for this illustration: pip install matplotlib")
        raise

    base = run_chain(BASE_OFFTAKE_SM3_PER_DAY)
    years = base["years"]
    arrival = base["arrival_p"]
    shortfall = base["first_shortfall_year"]

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    fig.suptitle(
        "Reservoir-to-host screening for production planning (example gas field)\n"
        "PUBLIC SCREENING PLACEHOLDER - escalate to validated NeqSim tools",
        fontsize=12,
        fontweight="bold",
    )

    # -- Panel 1: pressure development + feasible window ----------------------
    ax = axes[0, 0]
    ax.plot(years, base["reservoir_p"], "o-", color="#8c564b", label="Reservoir P")
    ax.plot(years, base["well_thp"], "s-", color="#1f77b4", label="Well THP")
    ax.plot(years, arrival, "^-", color="#2ca02c", label="Arrival P (host)")
    ax.axhline(
        REQUIRED_ARRIVAL_BARA,
        ls="--",
        color="red",
        label=f"Host requirement ({REQUIRED_ARRIVAL_BARA:.0f} bara)",
    )
    # Shade feasible (arrival >= requirement) vs not, across the time axis.
    if shortfall is not None:
        ax.axvspan(
            years[0], shortfall, color="green", alpha=0.08, label="Feasible window"
        )
        ax.axvspan(shortfall, years[-1], color="red", alpha=0.08, label="Boosting needed")
        ax.axvline(shortfall, color="red", ls=":", lw=1.2)
        ax.annotate(
            f"crossover\n~ year {shortfall:.0f}",
            xy=(shortfall, REQUIRED_ARRIVAL_BARA),
            xytext=(shortfall + 0.5, REQUIRED_ARRIVAL_BARA + 60),
            arrowprops=dict(arrowstyle="->", color="red"),
            fontsize=9,
            color="red",
        )
    ax.set_xlabel("Year")
    ax.set_ylabel("Pressure [bara]")
    ax.set_title("1. Pressure development & feasible production window")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, loc="upper right")

    # -- Panel 2: field production rate --------------------------------------
    ax = axes[0, 1]
    rate_mm = [r / 1e6 for r in base["field_rate"]]
    ax.plot(years, rate_mm, "o-", color="#ff7f0e")
    ax.fill_between(years, 0, rate_mm, color="#ff7f0e", alpha=0.15)
    if shortfall is not None:
        ax.axvline(shortfall, color="red", ls=":", lw=1.2)
    ax.set_xlabel("Year")
    ax.set_ylabel("Field gas rate [MSm3/day]")
    ax.set_title("2. Deliverable field rate vs time")
    ax.grid(True, alpha=0.3)

    # -- Panel 3: cumulative production & recovery factor --------------------
    ax = axes[1, 0]
    cum_g = [c / 1e9 for c in base["cumulative"]]
    ax.plot(years, cum_g, "o-", color="#9467bd", label="Cumulative [Gsm3]")
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative production [Gsm3]", color="#9467bd")
    ax.tick_params(axis="y", labelcolor="#9467bd")
    ax.grid(True, alpha=0.3)
    ax2 = ax.twinx()
    rec_pct = [r * 100.0 for r in base["recovery"]]
    ax2.plot(years, rec_pct, "s--", color="#17becf", label="Recovery factor [%]")
    ax2.set_ylabel("Recovery factor [%]", color="#17becf")
    ax2.tick_params(axis="y", labelcolor="#17becf")
    ax.set_title("3. Cumulative production & recovery")

    # -- Panel 4: optimization sweep (offtake vs feasible plateau years) ------
    ax = axes[1, 1]
    sweep_rates = []
    sweep_feasible_years = []
    sweep_feasible_production = []
    for q in OFFTAKE_SWEEP_SM3_PER_DAY:
        res = run_chain(q)
        sweep_rates.append(q / 1e6)
        sweep_feasible_years.append(res["feasible_years"])
        # Approx feasible production = plateau rate over the feasible years.
        sweep_feasible_production.append(q * 365.0 * res["feasible_years"] / 1e9)

    color_y = "#1f77b4"
    ax.plot(sweep_rates, sweep_feasible_years, "o-", color=color_y)
    ax.set_xlabel("Plateau offtake rate [MSm3/day]")
    ax.set_ylabel("Years host constraint met", color=color_y)
    ax.tick_params(axis="y", labelcolor=color_y)
    ax.grid(True, alpha=0.3)
    ax.axvline(
        BASE_OFFTAKE_SM3_PER_DAY / 1e6, color="gray", ls=":", lw=1.2
    )
    ax3 = ax.twinx()
    color_p = "#d62728"
    ax3.plot(
        sweep_rates, sweep_feasible_production, "s--", color=color_p
    )
    ax3.set_ylabel(
        "Feasible-window production [Gsm3]", color=color_p
    )
    ax3.tick_params(axis="y", labelcolor=color_p)
    ax.set_title("4. Optimization: offtake rate vs constraint-feasible plateau")

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out_path = Path(__file__).resolve().parent / "reservoir_to_host_planning.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved illustration -> {out_path}")

    # -- Console planning summary --------------------------------------------
    print()
    print("=" * 64)
    print("PRODUCTION PLANNING SUMMARY (screening)")
    print("=" * 64)
    print(f"Base plateau offtake : {BASE_OFFTAKE_SM3_PER_DAY / 1e6:.0f} MSm3/day")
    if shortfall is not None:
        print(f"Host constraint met  : up to ~ year {shortfall:.0f}")
        print("After that           : boosting/compression needed to keep flowing")
    else:
        print("Host constraint met  : across the full screening horizon")
    print()
    print(f"{'Offtake [MSm3/d]':>16} {'Feasible yrs':>13} {'Feasible Gsm3':>14}")
    print("-" * 45)
    for q_mm, fy, fp in zip(
        sweep_rates, sweep_feasible_years, sweep_feasible_production
    ):
        print(f"{q_mm:>16.0f} {fy:>13d} {fp:>14.1f}")
    print()
    print("Read panel 4 as the planning trade-off: a higher plateau rate brings")
    print("production forward but shortens the window where the host arrival-")
    print("pressure constraint is met unboosted. Use it to screen plateau/offtake")
    print("targets BEFORE detailed NeqSim deliverability and network modelling.")
    print()
    print("NOTE: screening placeholder only. For design-grade planning use NeqSim")
    print("SimpleReservoir (runTransient), PipeBeggsAndBrills, and MCP")
    print("runReservoir / runPipeline / runProcess / runFlowAssurance. Qualified")
    print("human review is required before any decision.")


if __name__ == "__main__":
    main()
