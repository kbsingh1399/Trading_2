# Arena tournament cycle106_20261014T205621Z

- snapshot: `docs/telemetry/live_snapshot_latest.json` generation `c82b8c85623c4368812f708ca9dd33e8` as_of `2026-10-14 20:56:21 UTC`
- cards: `docs/trade_plans/arena_cards/cycle106_20261014.json` sha256 `8c965e4510ddf8d5`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 106 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle106`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle106` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `btc_armed_post_sweep_short` | WATCH | no | - | 69.00 | advisory only |
| `eth_delete_18925596` | DELETE | no | - | 67.31 | VERIFIED |
| `btc_stage_82190_argon` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL | 53.58 | CONTRADICTED |
| `eth_modify_r3_forced_rr` | MODIFY | YES | - | 52.58 | CONTRADICTED |
| `eth_hold_18925596` | HOLD | YES | - | 52.29 | CONTRADICTED |
| `btc_stage_argon_tp_fixed` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL | 51.10 | CONTRADICTED |
| `btc_stage_belt_cleared` | STAGE | YES | ENTRY_IN_FUEL | 49.73 | CONTRADICTED |
| `eth_modify_safe_stop_near_tp` | MODIFY | YES | - | 48.74 | CONTRADICTED |
| `eth_modify_safe_stop_deep_tp` | MODIFY | YES | - | 48.74 | CONTRADICTED |
| `sp500_stage_short_7738` | STAGE | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED |
| `desk_batch_3x_max_risk` | STAGE_BATCH | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED |
| `nas100_stage_short_30000` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `gold_stage_short_4115` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN | 48.00 | CONTRADICTED |

## Bracket
### Round 1
- `eth_delete_18925596` (67.31, fatal=False) vs `btc_stage_82190_argon` (53.58, fatal=True) -> **eth_delete_18925596** — btc_stage_82190_argon is contradicted by the snapshot; eth_delete_18925596 is not
- `eth_modify_r3_forced_rr` (52.58, fatal=True) vs `eth_modify_safe_stop_near_tp` (48.74, fatal=True) -> **eth_modify_r3_forced_rr** — higher rubric total (52.58 vs 48.74)
- `nas100_stage_short_30000` (48.0, fatal=True) vs `eth_modify_safe_stop_deep_tp` (48.74, fatal=True) -> **eth_modify_safe_stop_deep_tp** — higher rubric total (48.74 vs 48.0)
- `btc_stage_argon_tp_fixed` (51.1, fatal=True) vs `desk_stand_aside_cycle106` (71.5, fatal=False) -> **desk_stand_aside_cycle106** — btc_stage_argon_tp_fixed is contradicted by the snapshot; desk_stand_aside_cycle106 is not
- `btc_armed_post_sweep_short` (69.0, fatal=False) vs `gold_stage_short_4115` (48.0, fatal=True) -> **btc_armed_post_sweep_short** — gold_stage_short_4115 is contradicted by the snapshot; btc_armed_post_sweep_short is not
- `sp500_stage_short_7738` (48.18, fatal=True) vs `eth_hold_18925596` (52.29, fatal=True) -> **eth_hold_18925596** — higher rubric total (52.29 vs 48.18)
- `btc_stage_belt_cleared` (49.73, fatal=True) vs `desk_batch_3x_max_risk` (48.18, fatal=True) -> **btc_stage_belt_cleared** — higher rubric total (49.73 vs 48.18)
### Round 2
- `eth_delete_18925596` (67.31, fatal=False) vs `eth_modify_r3_forced_rr` (52.58, fatal=True) -> **eth_delete_18925596** — eth_modify_r3_forced_rr is contradicted by the snapshot; eth_delete_18925596 is not
- `eth_modify_safe_stop_deep_tp` (48.74, fatal=True) vs `desk_stand_aside_cycle106` (71.5, fatal=False) -> **desk_stand_aside_cycle106** — eth_modify_safe_stop_deep_tp is contradicted by the snapshot; desk_stand_aside_cycle106 is not
- `btc_armed_post_sweep_short` (69.0, fatal=False) vs `eth_hold_18925596` (52.29, fatal=True) -> **btc_armed_post_sweep_short** — eth_hold_18925596 is contradicted by the snapshot; btc_armed_post_sweep_short is not
- bye: `btc_stage_belt_cleared`
### Round 3
- `eth_delete_18925596` (67.31, fatal=False) vs `desk_stand_aside_cycle106` (71.5, fatal=False) -> **desk_stand_aside_cycle106** — higher rubric total (71.5 vs 67.31)
- `btc_armed_post_sweep_short` (69.0, fatal=False) vs `btc_stage_belt_cleared` (49.73, fatal=True) -> **btc_armed_post_sweep_short** — btc_stage_belt_cleared is contradicted by the snapshot; btc_armed_post_sweep_short is not
### Round 4
- `desk_stand_aside_cycle106` (71.5, fatal=False) vs `btc_armed_post_sweep_short` (69.0, fatal=False) -> **desk_stand_aside_cycle106** — higher rubric total (71.5 vs 69.0)

## Findings per card
### `eth_hold_18925596` — HOLD  ETH
> Mandate 3 option A: keep the live ETHUSD.pi SELL LIMIT 1.00 lot @ 2447.50 (SL 2457.00, TP 2425.00) resting unchanged because the bearish Model 2 relief-rally thesis is still directionally alive.
- metrics: symbol=ETHUSD.pi, mid=2421.2, atr_14=10.6894, regime=BEARISH, entry=2447.5, sl=2457.0, tp=2425.0, lots=1.0, stop_points=9.5, risk_usd=9.5, reward_usd=22.5, rr_gross=2.3684210526315788, entry_distance_atr=2.460381312328118, friction_pct=33.68421052631579, sl_clearance_atr=-3.4613729489026515, hazard_union=[2420.0, 2540.0], hazard_union_usd=18526825.509999998, in_range_defense_usd=69069493.96999998, overwhelm_ratio=0.2682345626861989, best_reachable_rr=5.801052631578961, best_reachable_tp=2392.39, post_stop_equity_usd=4831.8, min_lot_spread_cash_usd=0.032, probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.46 ATR from mid (>2.0 ATR bound)
- MINOR `PROBE_FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 3.2 / stop distance 9.500 = 33.68% of risk, above the 15% dynamic friction ceiling
- MINOR [purchase-side] `PROBE_SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 2457.0 sits INSIDE the purchase-side sweep belt [2420.0, 2540.0] carrying 18.527M USD
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2447.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.57R against the minimum compliant stop (96.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MINOR `PROBE_TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2425.0 is 20.66 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
- FATAL `HOLD_CONTRADICTED` (A1: SL inside sweep band / insufficient structural buffer) — HOLD-as-is recommended for an order with fatal gate failures
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.299 exceeds 0.18
- probe FATAL `ENTRY_TOO_FAR` (A5) — entry is 2.46 ATR from mid (>2.0 ATR bound)
- probe FATAL `FRICTION_BUDGET` (A7) — spread 3.2 / stop distance 9.500 = 33.68% of risk, above the 15% dynamic friction ceiling
- probe FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1) — SL 2457.0 sits INSIDE the purchase-side sweep belt [2420.0, 2540.0] carrying 18.527M USD
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 2447.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.57R against the minimum compliant stop (96.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- probe MAJOR `TP_FRONT_RUN_OFF` (A6) — TP 2425.0 is 20.66 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 64.2/100 — fatal: HOLD_CONTRADICTED
  - Structural Price Action: 49.8/100 — fatal: HOLD_CONTRADICTED
  - Liquidation & Stop Forensic: 48.0/100 — fatal: HOLD_CONTRADICTED
  - Macro Risk & Portfolio Governor: 50.99/100 — fatal: HOLD_CONTRADICTED
  - Adversarial Pre-Mortem Red Team: 48.44/100 — fatal: HOLD_CONTRADICTED

### `eth_modify_safe_stop_near_tp` — MODIFY  ETH
> Mandate 3 option B: repair the ticket - entry pulled to the 2.0 ATR proximity perimeter, SL pushed clear of the whole 2440-2530 purchase-side belt, TP front-running the 2410 sell-stop magnet, lots downsized for the wider bunker (Gate R-4).
- metrics: symbol=ETHUSD.pi, mid=2421.2, atr_14=10.6894, regime=BEARISH, entry=2442.5, sl=2544.0, tp=2412.4, lots=0.14, stop_points=101.5, risk_usd=14.21, reward_usd=4.213999999999988, rr_gross=0.2965517241379302, entry_distance_atr=1.9926282111250568, friction_pct=3.152709359605912, sl_clearance_atr=0.3742024809624488, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=74357900.1, overwhelm_ratio=0.0, best_reachable_rr=0.4936945812807894, best_reachable_tp=2392.39, post_stop_equity_usd=4825.9125, min_lot_spread_cash_usd=0.032, probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- MINOR `PROBE_UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MINOR `PROBE_TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2412.4 sits INSIDE the magnet pool [2410.0, 2420.0] carrying 5.248M USD instead of front-running it
- MINOR `PROBE_RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.30R < 2.0R required for ETHUSD.pi
- FATAL `MODIFY_STILL_FATAL` (A1: SL inside sweep band / insufficient structural buffer) — the modified geometry still carries a fatal flaw
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.299 exceeds 0.18
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- probe FATAL `UNPAYABLE_GEOMETRY` (A6) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- probe FATAL `TP_INSIDE_MAGNET` (A6) — TP 2412.4 sits INSIDE the magnet pool [2410.0, 2420.0] carrying 5.248M USD instead of front-running it
- probe FATAL `RR_BELOW_MIN` (A6) — quoted geometry 0.30R < 2.0R required for ETHUSD.pi
  - Orderflow & Microstructure: 61.1/100 — fatal: MODIFY_STILL_FATAL
  - Structural Price Action: 45.49/100 — fatal: MODIFY_STILL_FATAL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: MODIFY_STILL_FATAL
  - Macro Risk & Portfolio Governor: 50.29/100 — fatal: MODIFY_STILL_FATAL
  - Adversarial Pre-Mortem Red Team: 44.3/100 — fatal: MODIFY_STILL_FATAL

### `eth_modify_safe_stop_deep_tp` — MODIFY  ETH
> Mandate 3 option B variant: identical repaired bunker, TP pushed to the 2300-2310 liquidation cascade magnet to manufacture payable reward.
- metrics: symbol=ETHUSD.pi, mid=2421.2, atr_14=10.6894, regime=BEARISH, entry=2442.5, sl=2544.0, tp=2311.5, lots=0.14, stop_points=101.5, risk_usd=14.21, reward_usd=18.340000000000003, rr_gross=1.2906403940886702, entry_distance_atr=1.9926282111250568, friction_pct=3.152709359605912, sl_clearance_atr=0.3742024809624488, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=74357900.1, overwhelm_ratio=0.0, best_reachable_rr=0.4936945812807894, best_reachable_tp=2392.39, post_stop_equity_usd=4825.9125, min_lot_spread_cash_usd=0.032, probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- MINOR `PROBE_UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MINOR `PROBE_TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2311.5 sits INSIDE the magnet pool [2310.0, 2320.0] carrying 24.093M USD instead of front-running it
- MINOR `PROBE_RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.29R < 2.0R required for ETHUSD.pi
- FATAL `MODIFY_STILL_FATAL` (A1: SL inside sweep band / insufficient structural buffer) — the modified geometry still carries a fatal flaw
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.299 exceeds 0.18
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- probe FATAL `UNPAYABLE_GEOMETRY` (A6) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- probe FATAL `TP_INSIDE_MAGNET` (A6) — TP 2311.5 sits INSIDE the magnet pool [2310.0, 2320.0] carrying 24.093M USD instead of front-running it
- probe MAJOR `RR_BELOW_MIN` (A6) — quoted geometry 1.29R < 2.0R required for ETHUSD.pi
  - Orderflow & Microstructure: 61.1/100 — fatal: MODIFY_STILL_FATAL
  - Structural Price Action: 45.49/100 — fatal: MODIFY_STILL_FATAL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: MODIFY_STILL_FATAL
  - Macro Risk & Portfolio Governor: 50.29/100 — fatal: MODIFY_STILL_FATAL
  - Adversarial Pre-Mortem Red Team: 44.3/100 — fatal: MODIFY_STILL_FATAL

### `eth_modify_r3_forced_rr` — MODIFY  ETH
> Mandate 3 option B adversarial variant: the only TP that satisfies a 2.2R gross requirement is 2241.2, which is 60 points BELOW the outer edge of the 108.45M USD 2300-2310 magnet cluster. Tests whether a compliant R:R can be claimed without front-running the magnet.
- metrics: symbol=ETHUSD.pi, mid=2421.2, atr_14=10.6894, regime=BEARISH, entry=2442.5, sl=2544.0, tp=2219.2, lots=0.14, stop_points=101.5, risk_usd=14.21, reward_usd=31.26200000000003, rr_gross=2.200000000000002, entry_distance_atr=1.9926282111250568, friction_pct=3.152709359605912, sl_clearance_atr=0.3742024809624488, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=74357900.1, overwhelm_ratio=0.0, best_reachable_rr=0.4936945812807894, best_reachable_tp=2392.39, post_stop_equity_usd=4825.9125, min_lot_spread_cash_usd=0.032, probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- MINOR `PROBE_UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `MODIFY_STILL_FATAL` (A1: SL inside sweep band / insufficient structural buffer) — the modified geometry still carries a fatal flaw
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.299 exceeds 0.18
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 2442.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- probe FATAL `UNPAYABLE_GEOMETRY` (A6) — best reachable front-runnable target yields 0.49R at this card's stop < required 2.0R
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.49R against the minimum compliant stop (101.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
  - Orderflow & Microstructure: 63.5/100 — fatal: MODIFY_STILL_FATAL
  - Structural Price Action: 52.69/100 — fatal: MODIFY_STILL_FATAL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: MODIFY_STILL_FATAL
  - Macro Risk & Portfolio Governor: 55.09/100 — fatal: MODIFY_STILL_FATAL
  - Adversarial Pre-Mortem Red Team: 49.1/100 — fatal: MODIFY_STILL_FATAL

### `eth_delete_18925596` — DELETE  ETH
> Mandate 3 option C: cancel the resting order - price drifted 2.46 ATR from the entry, the stop sits inside the 2450-2460 purchase-side sweep bin, friction is 33.7% of risk, and the cited sheltering ask wall relocated from 2450.30 down to 2439.10.
- metrics: symbol=ETHUSD.pi, mid=2421.2, atr_14=10.6894, regime=BEARISH, entry=2447.5, sl=2457.0, tp=2425.0, lots=1.0, stop_points=9.5, risk_usd=9.5, reward_usd=22.5, rr_gross=2.3684210526315788, entry_distance_atr=2.460381312328118, friction_pct=33.68421052631579, sl_clearance_atr=-3.4613729489026515, hazard_union=[2420.0, 2540.0], hazard_union_usd=18526825.509999998, in_range_defense_usd=69069493.96999998, overwhelm_ratio=0.2682345626861989, best_reachable_rr=5.801052631578961, best_reachable_tp=2392.39, post_stop_equity_usd=4831.8, min_lot_spread_cash_usd=0.032, delete_justification=['ENTRY_TOO_FAR', 'FRICTION_BUDGET', 'SL_INSIDE_SWEEP', 'NO_PAYABLE_SETUP', 'SPREAD_OVER_ATR', 'ENTRY_IN_FUEL', 'TP_FRONT_RUN_OFF'], probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.299 exceeds 0.18
- MINOR `PROBE_ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.46 ATR from mid (>2.0 ATR bound)
- MINOR `PROBE_FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 3.2 / stop distance 9.500 = 33.68% of risk, above the 15% dynamic friction ceiling
- MINOR [purchase-side] `PROBE_SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 2457.0 sits INSIDE the purchase-side sweep belt [2420.0, 2540.0] carrying 18.527M USD
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2447.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.57R against the minimum compliant stop (96.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MINOR `PROBE_TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2425.0 is 20.66 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.299 exceeds 0.18
- probe FATAL `ENTRY_TOO_FAR` (A5) — entry is 2.46 ATR from mid (>2.0 ATR bound)
- probe FATAL `FRICTION_BUDGET` (A7) — spread 3.2 / stop distance 9.500 = 33.68% of risk, above the 15% dynamic friction ceiling
- probe FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1) — SL 2457.0 sits INSIDE the purchase-side sweep belt [2420.0, 2540.0] carrying 18.527M USD
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 2447.5 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 18.527M USD
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.57R against the minimum compliant stop (96.2 points = clear the 2540.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- probe MAJOR `TP_FRONT_RUN_OFF` (A6) — TP 2425.0 is 20.66 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 71.4/100 — no fatal flaw found
  - Structural Price Action: 71.4/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 67.79/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 58.19/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 67.79/100 — no fatal flaw found

### `btc_stage_82190_argon` — STAGE SHORT BTC
> Peer-question card from the Gemini/Argon desk: Model 2 relief-rally short at 82190 (SL 82420, TP 81660), quoted 2.30R at 11.50 USD nominal risk.
- metrics: symbol=BTCUSD.pi, mid=81725.0, atr_14=248.6643, regime=BEARISH, entry=82190.0, sl=82420.0, tp=81660.0, lots=0.05, stop_points=230.0, risk_usd=11.5, reward_usd=26.5, rr_gross=2.3043478260869565, rr_min_required=2.0, entry_distance_atr=1.8699909878498844, friction_pct=6.956521739130435, sl_clearance_atr=-1.5281646782429164, hazard_union=[81800.0, 82800.0], hazard_union_usd=28090314.490000002, in_range_defense_usd=95438743.66999994, overwhelm_ratio=0.29432820896226725, best_reachable_rr=5.692173913043529, best_reachable_tp=80880.79999999999, post_stop_equity_usd=4829.3, min_lot_spread_cash_usd=0.16
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 82420.0 sits INSIDE the purchase-side sweep belt [81800.0, 82800.0] carrying 28.090M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82190.0 sits inside un-swept purchase-side stop fuel [81800.0, 82800.0] = 28.090M USD
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.88R against the minimum compliant stop (697.0 points = clear the 82800.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
  - Orderflow & Microstructure: 59.88/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 64.02/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL

### `btc_stage_argon_tp_fixed` — STAGE SHORT BTC
> Isolates a single defect: the Argon card with only the TP repaired to a true 8.5 bps front-run of the 81700 band edge. Tests whether the take-profit placement or the stop placement is the binding flaw.
- metrics: symbol=BTCUSD.pi, mid=81725.0, atr_14=248.6643, regime=BEARISH, entry=82190.0, sl=82420.0, tp=81710.0, lots=0.05, stop_points=230.0, risk_usd=11.5, reward_usd=24.0, rr_gross=2.0869565217391304, rr_min_required=2.0, entry_distance_atr=1.8699909878498844, friction_pct=6.956521739130435, sl_clearance_atr=-1.5281646782429164, hazard_union=[81800.0, 82800.0], hazard_union_usd=28090314.490000002, in_range_defense_usd=95438743.66999994, overwhelm_ratio=0.29432820896226725, best_reachable_rr=5.692173913043529, best_reachable_tp=80880.79999999999, post_stop_equity_usd=4829.3, min_lot_spread_cash_usd=0.16
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 82420.0 sits INSIDE the purchase-side sweep belt [81800.0, 82800.0] carrying 28.090M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82190.0 sits inside un-swept purchase-side stop fuel [81800.0, 82800.0] = 28.090M USD
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.88R against the minimum compliant stop (697.0 points = clear the 82800.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 81710.0 is 13.48 bps from the governing magnet edge 81600.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 55.74/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 55.74/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_PAYABLE_SETUP | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL

### `btc_stage_belt_cleared` — STAGE SHORT BTC
> Maximum-effort repair: same entry, stop pushed clear of the entire contiguous 81800-83300 purchase-side fuel belt, TP front-running the 80000-80100 stop magnet (22.93M USD). Tests whether a fully compliant bunker can still pay 2.0R.
- metrics: symbol=BTCUSD.pi, mid=81725.0, atr_14=248.6643, regime=BEARISH, entry=82190.0, sl=83390.0, tp=80160.0, lots=0.01, stop_points=1200.0, risk_usd=12.0, reward_usd=20.3, rr_gross=1.6916666666666667, rr_min_required=2.0, entry_distance_atr=1.8699909878498844, friction_pct=1.3333333333333335, sl_clearance_atr=0.3619337395838486, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=146909942.6999999, overwhelm_ratio=0.0, best_reachable_rr=1.0910000000000097, best_reachable_tp=80880.79999999999, post_stop_equity_usd=4828.675, min_lot_spread_cash_usd=0.16
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82190.0 sits inside un-swept purchase-side stop fuel [81800.0, 82800.0] = 28.090M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.09R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.88R against the minimum compliant stop (697.0 points = clear the 82800.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.69R < 2.0R required for BTCUSD.pi
  - Orderflow & Microstructure: 55.74/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.92/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sp500_stage_short_7738` — STAGE SHORT SP500
> Model 2 relief-rally short at the 2.0 ATR perimeter with the stop above the 7720-7820 purchase-side belt and the TP front-running the 7650-7660 magnet.
- metrics: symbol=SP500.p, mid=7717.695, atr_14=10.0704, regime=BEARISH, entry=7737.8, sl=7823.6, tp=7650.8, lots=0.01, stop_points=85.80000000000018, risk_usd=8.580000000000018, reward_usd=8.700000000000001, rr_gross=1.013986013986012, rr_min_required=2.0, entry_distance_atr=1.9964450270098977, friction_pct=1.013986013986012, sl_clearance_atr=0.35748331744522205, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=25335828.24, overwhelm_ratio=0.0, best_reachable_rr=0.5841491841491923, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4832.95, min_lot_spread_cash_usd=0.087
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7737.8 sits inside un-swept purchase-side stop fuel [7720.0, 7820.0] = 5.336M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.58R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.58R against the minimum compliant stop (85.7 points = clear the 7820.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 7650.8 sits INSIDE the magnet pool [7650.0, 7660.0] carrying 17.611M USD instead of front-running it
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.01R < 2.0R required for SP500.p
  - Orderflow & Microstructure: 48.92/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `nas100_stage_short_30000` — STAGE SHORT NAS100
> Model 2 short into NAS100's thin overhead fuel pocket with 1.0M+ walls on both sides; tests whether any setup can be certified on an asset with no causal indicators.
- metrics: symbol=NAS100.p, mid=29917.5, atr_14=None, regime=INSUFFICIENT_HISTORY, entry=30000.0, sl=30260.0, tp=29620.0, lots=0.01, stop_points=260.0, risk_usd=26.0, reward_usd=38.0, rr_gross=1.4615384615384615, rr_min_required=2.0, friction_pct=0.5461538461538461, sl_clearance_atr=None, hazard_union=[29900.0, 30900.0], hazard_union_usd=4306420.62, in_range_defense_usd=8534063.56, overwhelm_ratio=0.5046154847246064, post_stop_equity_usd=4811.175, min_lot_spread_cash_usd=0.142
- FATAL `REGIME_UNVERIFIED` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime='INSUFFICIENT_HISTORY': neither engine can be certified on this snapshot
- FATAL `ATR_UNAVAILABLE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — ATR(14) unavailable; stop distance, buffers and friction ratios are undefined
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 26.00 USD outside [7.5, 14.5]
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 30260.0 sits INSIDE the purchase-side sweep belt [29900.0, 30900.0] carrying 4.306M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 30000.0 sits inside un-swept purchase-side stop fuel [29900.0, 30900.0] = 4.306M USD
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 29620.0 sits INSIDE the magnet pool [29600.0, 29700.0] carrying 0.827M USD instead of front-running it
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.46R < 2.0R required for NAS100.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 9
  - Orderflow & Microstructure: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD

### `gold_stage_short_4115` — STAGE SHORT GOLD
> Commodity relief-rally short with the 1.04M USD ask wall at 4139.90 as backsplash and a 7.58M USD cascade magnet below; tests the commodity card class against the 750k wall threshold.
- metrics: symbol=XAUUSD.pi, mid=4103.795, atr_14=None, regime=INSUFFICIENT_HISTORY, entry=4115.0, sl=4125.0, tp=4090.0, lots=0.01, stop_points=10.0, risk_usd=10.0, reward_usd=25.0, rr_gross=2.5, rr_min_required=2.0, friction_pct=3.1, sl_clearance_atr=None, hazard_union=[4110.0, 4210.0], hazard_union_usd=2293762.9699999997, in_range_defense_usd=3318029.65, overwhelm_ratio=0.6913027344406039, post_stop_equity_usd=4831.175, min_lot_spread_cash_usd=0.31
- FATAL `REGIME_UNVERIFIED` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime='INSUFFICIENT_HISTORY': neither engine can be certified on this snapshot
- FATAL `ATR_UNAVAILABLE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — ATR(14) unavailable; stop distance, buffers and friction ratios are undefined
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 4125.0 sits INSIDE the purchase-side sweep belt [4110.0, 4210.0] carrying 2.294M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4115.0 sits inside un-swept purchase-side stop fuel [4110.0, 4210.0] = 2.294M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.618M < 0.75M COMMODITY requirement
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 4090.0 is 24.51 bps from the governing magnet edge 4080.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Structural Price Action: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: REGIME_UNVERIFIED, ATR_UNAVAILABLE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN

### `desk_batch_3x_max_risk` — STAGE_BATCH SHORT BTC
> Strawman capacity card: fill all three 'available' joint-fill slots with structurally sound copies of the best geometry. Tests the briefing's capacity arithmetic (3 available slots) against the snapshot's broker-valued contingent stress.
- metrics: symbol=BTCUSD.pi, mid=81725.0, atr_14=248.6643, regime=BEARISH, entry=82190.0, sl=83390.0, tp=80160.0, lots=0.012, stop_points=1200.0, risk_usd=14.4, reward_usd=24.36, rr_gross=1.6916666666666667, rr_min_required=2.0, entry_distance_atr=1.8699909878498844, friction_pct=1.3333333333333335, sl_clearance_atr=0.3619337395838486, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=146909942.6999999, overwhelm_ratio=0.0, best_reachable_rr=1.0910000000000097, best_reachable_tp=80880.79999999999, post_stop_equity_usd=4785.675, min_lot_spread_cash_usd=0.16
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82190.0 sits inside un-swept purchase-side stop fuel [81800.0, 82800.0] = 28.090M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.09R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.88R against the minimum compliant stop (697.0 points = clear the 82800.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.69R < 2.0R required for BTCUSD.pi
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4785.675 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.92/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_armed_post_sweep_short` — WATCH  BTC
> Do not fade intact fuel. Arm the Model 1 sweep-and-reverse instead: if BTC takes the 82400-82500 purchase-side bin and closes an M15 back below 82300, the belt above is consumed and a short becomes payable with a tight stop.
- metrics: symbol=BTCUSD.pi, mid=81725.0, atr_14=248.6643, regime=BEARISH, min_lot_spread_cash_usd=0.16
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: BTCUSD.pi prints a 15m high >= 82450 AND closes back below 82300 while session CVD stays negative
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle106` — STAND_ASIDE
> No new ticket and no hold: the snapshot denies trade authorisation, 21 of 24 assets carry no causal indicators, the ETH ticket is fatally mis-specified, and every STAGE geometry above is contradicted by the same gate set. The card proves it by running the whole universe through the gates.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 9 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
