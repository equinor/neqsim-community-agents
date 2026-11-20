# Example: Reference Station as a Living Task

Public synthetic data only.

1. Create the reference task — a compressor station with three injected faults
   (gradual fouling from day 120, a +4 % flow-meter bias from day 200, a 3 bar
   suction-pressure step at day 280):

   ```bash
   neqsim task-reference-case C:/tmp/living
   ```

   Without a folder the case is created in the task root used for all tasks
   (`neqsim --show-task-root`); the commands below then accept the bare name
   `reference_compressor_station` instead of the full path.

2. Backtest one year of daily cycles:

   ```bash
   neqsim task-backtest C:/tmp/living/reference_compressor_station --start 2025-10-02 --end 2026-09-30 --repeat
   ```

   Expected: 3 of 3 events detected (fouling after about 13 days, meter bias and
   pressure step after 2 days), 0 false alarms, reproducibility 100 %.

3. Solve the goal (2 % compression-power reduction by suction cooling, bounded by
   the dew-point margin):

   ```bash
   neqsim task-solve C:/tmp/living/reference_compressor_station --no-agent
   ```

   Expected: `goal_met` after three rounds at about 2.3 %. With the target raised
   to 5 % the loop stops as `infeasible` because the reachable bound is about 2.6 %.

4. Run a monitor cycle, read the digest, and decide the proposed ledger item:

   ```bash
   neqsim task-cycle C:/tmp/living/reference_compressor_station
   neqsim task-ledger C:/tmp/living/reference_compressor_station list
   ```
