# Arena tournament cycle114_20261015T003957Z

- snapshot: `/tmp/snap114.json` generation `58546954882d4480970079703e97b9c2` as_of `2026-10-15 00:39:57 UTC`
- cards: `docs/trade_plans/arena_cards/cycle114_20261015T003957Z.json` sha256 `fc83cf06ecf81fcb`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 114 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle114`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle114` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `nas100_belt_thin_watch` | WATCH | no | - | 69.00 | advisory only |
| `btc_ladder_break_watch` | WATCH | no | - | 69.00 | advisory only |
| `eth_val_rejection_watch` | WATCH | no | - | 61.80 | advisory only |
| `desk_batch_4x_max_risk` | STAGE_BATCH | YES | - | 55.66 | CONTRADICTED |
| `uswti_bullish_pullback_long` | STAGE | YES | - | 48.36 | CONTRADICTED |
| `btc_belt_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `eth_shelf_long` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `sol_belt_short` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `sol_counter_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `sp500_long_variant` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `ltc_friction_short` | STAGE | YES | NO_BUNKER_WALL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `near_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 48.00 | CONTRADICTED |
| `silver_floor_probe` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD | 48.00 | CONTRADICTED |
| `nas100_extreme_probe` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `btc_relief_rally_short` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `eth_watch_probe` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `gold_range_gate_probe` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN | 48.00 | CONTRADICTED |

## Bracket
### Round 1
- `btc_ladder_break_watch` (69.0, fatal=False) vs `sp500_long_variant` (48.0, fatal=True) -> **btc_ladder_break_watch** — sp500_long_variant is contradicted by the snapshot; btc_ladder_break_watch is not
- `eth_shelf_long` (48.0, fatal=True) vs `eth_watch_probe` (48.0, fatal=True) -> **eth_shelf_long** — exact tie: fewer standing attacks (deterministic order)
- `ltc_friction_short` (48.0, fatal=True) vs `uswti_bullish_pullback_long` (48.36, fatal=True) -> **uswti_bullish_pullback_long** — higher rubric total (48.36 vs 48.0)
- `eth_val_rejection_watch` (61.8, fatal=False) vs `sp500_core_short` (48.0, fatal=True) -> **eth_val_rejection_watch** — sp500_core_short is contradicted by the snapshot; eth_val_rejection_watch is not
- `gold_range_gate_probe` (48.0, fatal=True) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 48.0)
- `silver_floor_probe` (48.0, fatal=True) vs `sol_belt_short` (48.0, fatal=True) -> **silver_floor_probe** — exact tie: fewer standing attacks (deterministic order)
- `btc_belt_long` (48.0, fatal=True) vs `nas100_extreme_probe` (48.0, fatal=True) -> **btc_belt_long** — exact tie: fewer standing attacks (deterministic order)
- `nas100_belt_thin_watch` (69.0, fatal=False) vs `desk_stand_aside_cycle114` (71.5, fatal=False) -> **desk_stand_aside_cycle114** — higher rubric total (71.5 vs 69.0)
- `btc_relief_rally_short` (48.0, fatal=True) vs `sol_counter_long` (48.0, fatal=True) -> **btc_relief_rally_short** — exact tie: fewer standing attacks (deterministic order)
- bye: `near_friction_probe`
### Round 2
- `btc_ladder_break_watch` (69.0, fatal=False) vs `eth_shelf_long` (48.0, fatal=True) -> **btc_ladder_break_watch** — eth_shelf_long is contradicted by the snapshot; btc_ladder_break_watch is not
- `uswti_bullish_pullback_long` (48.36, fatal=True) vs `eth_val_rejection_watch` (61.8, fatal=False) -> **eth_val_rejection_watch** — uswti_bullish_pullback_long is contradicted by the snapshot; eth_val_rejection_watch is not
- `desk_batch_4x_max_risk` (55.66, fatal=True) vs `silver_floor_probe` (48.0, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 48.0)
- `btc_belt_long` (48.0, fatal=True) vs `desk_stand_aside_cycle114` (71.5, fatal=False) -> **desk_stand_aside_cycle114** — btc_belt_long is contradicted by the snapshot; desk_stand_aside_cycle114 is not
- `btc_relief_rally_short` (48.0, fatal=True) vs `near_friction_probe` (48.0, fatal=True) -> **btc_relief_rally_short** — exact tie: fewer standing attacks (deterministic order)
### Round 3
- `btc_ladder_break_watch` (69.0, fatal=False) vs `eth_val_rejection_watch` (61.8, fatal=False) -> **btc_ladder_break_watch** — higher rubric total (69.0 vs 61.8)
- `desk_batch_4x_max_risk` (55.66, fatal=True) vs `desk_stand_aside_cycle114` (71.5, fatal=False) -> **desk_stand_aside_cycle114** — desk_batch_4x_max_risk is contradicted by the snapshot; desk_stand_aside_cycle114 is not
- bye: `btc_relief_rally_short`
### Round 4
- `btc_ladder_break_watch` (69.0, fatal=False) vs `desk_stand_aside_cycle114` (71.5, fatal=False) -> **desk_stand_aside_cycle114** — higher rubric total (71.5 vs 69.0)
- bye: `btc_relief_rally_short`
### Round 5
- `desk_stand_aside_cycle114` (71.5, fatal=False) vs `btc_relief_rally_short` (48.0, fatal=True) -> **desk_stand_aside_cycle114** — btc_relief_rally_short is contradicted by the snapshot; desk_stand_aside_cycle114 is not

## Findings per card
### `btc_belt_long` — STAGE LONG BTC
> Best geometry in the book again (0.81R ceiling): mid has slipped back under the EMA20 81,625 to 81,529, the compliant stop anchors on the 80,600 fuel edge, and the target is the 10 bps front-run of the [81,600-81,800] lane. A Model-1 long is banned in a BEARISH HTF and mid sits inside the [80,600-81,600] sell-stop/cascade lane carrying $125.2M.
- metrics: symbol=BTCUSD.pi, mid=81529.0, atr_14=235.7105, regime=BEARISH, entry=81069.364525, sl=80517.501325, tp=81518.4, lots=0.02, stop_points=551.8631999999925, risk_usd=11.03726399999985, reward_usd=8.98070949999994, rr_gross=0.8136717124823745, rr_min_required=2.0, entry_distance_atr=1.9500000000000117, friction_pct=2.899269239188302, sl_clearance_atr=0.34999999999997994, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=55048103.309999995, overwhelm_ratio=1.0592394859026433, best_reachable_rr=0.8136717124823744, best_reachable_tp=81518.4, post_stop_equity_usd=4843.75342, min_lot_spread_cash_usd=0.16
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 80600.0
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81069.364525 sits inside un-swept sale-side stop fuel [80600.0, 81600.0] = 100.886M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.81R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.81R against the minimum compliant stop (551.9 points = clear the 80600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 81518.4 is 10.00 bps from the governing magnet edge 81600.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.81R < 2.0R required for BTCUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `eth_shelf_long` — STAGE LONG ETH
> Bullish-reversion bid into the $15.48M/1,386 s 0xab5e6f grid at 2,392.2 (crypto shield satisfied) but the BEARISH stack (EMA20 2,419.7 < EMA50 2,435.1 < EMA200 2,476.6) and the $323.6M cascade structure under price cap the ceiling at 0.48R.
- metrics: symbol=ETHUSD.pi, mid=2418.15, atr_14=9.9609, regime=BEARISH, entry=2398.7262450000003, sl=2296.513685, tp=2447.55, lots=0.11, stop_points=102.2125600000004, risk_usd=11.243381600000044, reward_usd=5.370613049999988, rr_gross=0.4776688403069026, rr_min_required=2.2, entry_distance_atr=1.94999999999998, friction_pct=3.619907377332087, sl_clearance_atr=0.3500000000000104, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=20942709.09, overwhelm_ratio=10.64039685851359, best_reachable_rr=0.47766884030690265, best_reachable_tp=2447.55, post_stop_equity_usd=4843.495773000001, min_lot_spread_cash_usd=0.037000000000000005
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.371 exceeds 0.18
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2398.7262450000003 sits inside un-swept sale-side stop fuel [2300.0, 2420.0] = 253.265M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 222.839M exceeds in-range verified defense 20.943M by 10.64:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.48R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.48R against the minimum compliant stop (102.2 points = clear the 2300.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.48R < 2.2R required for ETHUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -2,078,147
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `sol_belt_short` — STAGE SHORT SOL
> Mid 104.295 is inside the [104,105]-adjacent belt with a $106M cascade stack below; compliant stop 9 ATR wide, ceiling 0.13R.
- metrics: symbol=SOLUSD.p, mid=104.295, atr_14=0.4743, regime=BEARISH, entry=105.219885, sl=114.166005, tp=104.10399999999998, lots=0.01, stop_points=8.946119999999993, risk_usd=8.946119999999993, reward_usd=1.11588500000002, rr_gross=0.12473396287999947, rr_min_required=2.5, entry_distance_atr=1.9500000000000068, friction_pct=2.570946958010849, sl_clearance_atr=0.34999999999999665, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=13831794.27, overwhelm_ratio=1.2001015447434065, best_reachable_rr=0.12473396287999947, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.36735, min_lot_spread_cash_usd=0.23
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.485 exceeds 0.18
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 114.0
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.219885 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 16.667M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.12R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.12R against the minimum compliant stop (8.9 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.12R < 2.5R required for SOLUSD.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 673,394
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `sol_counter_long` — STAGE LONG SOL
> Counter-trend long into a BEARISH stack; ceiling 0.24R with the $6.59M bid wall at 102.72 as the only eligible support.
- metrics: symbol=SOLUSD.p, mid=104.295, atr_14=0.4743, regime=BEARISH, entry=103.370115, sl=92.833995, tp=105.894, lots=0.01, stop_points=10.536119999999997, risk_usd=10.536119999999997, reward_usd=2.523885000000007, rr_gross=0.23954596189109537, rr_min_required=2.5, entry_distance_atr=1.9500000000000068, friction_pct=2.182966784736697, sl_clearance_atr=0.34999999999999665, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=8571615.32, overwhelm_ratio=10.966280573823044, best_reachable_rr=0.23954596189109537, best_reachable_tp=105.894, post_stop_equity_usd=4844.37985, min_lot_spread_cash_usd=0.23
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.485 exceeds 0.18
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 93.0
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 103.370115 sits inside un-swept sale-side stop fuel [93.0, 104.0] = 93.999M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 93.999M exceeds in-range verified defense 8.572M by 10.97:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.24R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.24R against the minimum compliant stop (10.5 points = clear the 93.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.24R < 2.5R required for SOLUSD.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `sp500_core_short` — STAGE SHORT SP500
> Cleanest microstructure in the book (0.44 bps) but the compliant stop walks to 92 pts while the reachable reward is 31 pts (0.34R); the $38.33M bid wall at 7,682 sits where the target must print.
- metrics: symbol=SP500.p, mid=7701.59, atr_14=9.23, regime=BEARISH, entry=7719.5885, sl=7813.2305, tp=7687.679999999999, lots=0.01, stop_points=93.64199999999983, risk_usd=9.364199999999983, reward_usd=3.190850000000046, rr_gross=0.3407498771918639, rr_min_required=2.0, entry_distance_atr=1.9499999999999669, friction_pct=0.3630849405181443, sl_clearance_atr=0.34999999999996373, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=22058743.730000004, overwhelm_ratio=0.2879128715459264, best_reachable_rr=0.3407498771918639, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4845.84475, min_lot_spread_cash_usd=0.034
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 7810.0
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7719.5885 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 6.379M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.34R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.34R against the minimum compliant stop (93.6 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.34R < 2.0R required for SP500.p
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sp500_long_variant` — STAGE LONG SP500
> Mirror geometry: 0.33R ceiling with the stop below the same 7,682 defence and the BEARISH stack overhead.
- metrics: symbol=SP500.p, mid=7701.59, atr_14=9.23, regime=BEARISH, entry=7683.5915, sl=7596.7695, tp=7712.28, lots=0.01, stop_points=86.82200000000012, risk_usd=8.682200000000012, reward_usd=2.8688499999999295, rr_gross=0.3304289235447151, rr_min_required=2.0, entry_distance_atr=1.9499999999999669, friction_pct=0.3916058141945585, sl_clearance_atr=0.34999999999996373, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=11963614.990000002, overwhelm_ratio=3.503615478685677, best_reachable_rr=0.3304289235447151, best_reachable_tp=7712.28, post_stop_equity_usd=4846.69725, min_lot_spread_cash_usd=0.034
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 7600.0
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7683.5915 sits inside un-swept sale-side stop fuel [7600.0, 7700.0] = 41.941M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 41.916M exceeds in-range verified defense 11.964M by 3.50:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.33R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.33R against the minimum compliant stop (86.8 points = clear the 7600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 7712.28 is 10.00 bps from the governing magnet edge 7720.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.33R < 2.0R required for SP500.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -31
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `ltc_friction_short` — STAGE SHORT LTC
> Gross 0.42R at 16.81% friction (rule ceiling 15%) with zero eligible walls on the entire book; LTC is friction-class this generation.
- metrics: symbol=LTCUSD.pi, mid=59.23, atr_14=0.2406, regime=BEARISH, entry=59.699169999999995, sl=61.48421, tp=58.95889999999999, lots=0.1, stop_points=1.7850400000000022, risk_usd=17.850400000000022, reward_usd=7.402700000000024, rr_gross=0.41470779366288796, rr_min_required=2.0, entry_distance_atr=1.9499999999999929, friction_pct=16.80634607627838, sl_clearance_atr=0.3499999999999949, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=0.41470779366288796, best_reachable_tp=58.95889999999999, post_stop_equity_usd=4835.237, min_lot_spread_cash_usd=3.0
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 50.65 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 1.247 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (0.1 lot) is 3.00 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.3 / stop distance 1.785 = 16.81% of risk, above the 15% dynamic friction ceiling
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 61.4
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.41R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.41R against the minimum compliant stop (1.8 points = clear the 61.4 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.41R < 2.0R required for LTCUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 14,170
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD

### `near_friction_probe` — STAGE SHORT NEAR
> Gross 1.02R at 25.86% friction; banned instrument, museum geometry.
- metrics: symbol=NERUSD.p, mid=4.821, atr_14=0.0408, regime=BEARISH, entry=4.90056, sl=5.02428, tp=4.774769999999999, lots=1.0, stop_points=0.1237200000000005, risk_usd=12.37200000000005, reward_usd=12.579000000000029, rr_gross=1.0167313288069817, rr_min_required=2.0, entry_distance_atr=1.9499999999999962, friction_pct=25.86485612673769, sl_clearance_atr=0.35000000000000714, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=1.0167313288069817, best_reachable_tp=4.774769999999999, post_stop_equity_usd=4842.085, min_lot_spread_cash_usd=3.2
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 66.38 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.784 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.20 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.032 / stop distance 0.124 = 25.86% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.90056 sits inside un-swept purchase-side stop fuel [4.82, 5.01] = 1.443M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.02R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.02R against the minimum compliant stop (0.1 points = clear the 5.01 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.02R < 2.0R required for NERUSD.p
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `silver_floor_probe` — STAGE SHORT SILVER
> 1.53R ceiling but min-lot risk 36.06 USD at the compliant stop (2.5x the envelope) and the best commodity-class wall is $0.29M against the $0.75M shield.
- metrics: symbol=XAGUSD.pi, mid=56.104, atr_14=0.2342, regime=BEARISH, entry=56.56069, sl=57.28197, tp=55.45539999999999, lots=0.01, stop_points=0.7212800000000001, risk_usd=36.06400000000001, reward_usd=55.26450000000054, rr_gross=1.532400732031958, rr_min_required=2.0, entry_distance_atr=1.9500000000000077, friction_pct=4.991126885536822, sl_clearance_atr=0.3499999999999929, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=197999.54, overwhelm_ratio=4.176274803466716, best_reachable_rr=1.532400732031958, best_reachable_tp=55.45539999999999, post_stop_equity_usd=4812.47, min_lot_spread_cash_usd=1.8
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 6.42 bps exceeds the 5 bps COMMODITY ceiling
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.350 ATR < 0.35 ATR outside the belt edge 57.2
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 56.56069 sits inside un-swept purchase-side stop fuel [56.1, 57.2] = 0.879M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.198M < 0.75M COMMODITY requirement
- FATAL [purchase-side] `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 0.827M exceeds in-range verified defense 0.198M by 4.18:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.53R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.53R against the minimum compliant stop (0.7 points = clear the 57.2 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.53R < 2.0R required for XAGUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 23
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO, COUNTER_CVD

### `nas100_extreme_probe` — STAGE SHORT NAS100
> Deepest RSI dislocation in the book (31.4, BEARISH stack 29,838 < 30,031 < 30,393) but the compliant stop anchors on the 30,900 fuel edge -> 1,053 pts = 105.33 USD at min lot.
- metrics: symbol=NAS100.p, mid=29747.14, atr_14=62.2389, regime=BEARISH, entry=29868.505855, sl=30921.783615, tp=29529.499999999996, lots=0.01, stop_points=1053.2777600000009, risk_usd=105.32777600000009, reward_usd=33.900585500000304, rr_gross=0.32185798264647947, rr_min_required=2.0, entry_distance_atr=1.9500000000000002, friction_pct=0.11582889588402578, sl_clearance_atr=0.35000000000000453, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=7036971.250000001, overwhelm_ratio=0.5467114875593673, best_reachable_rr=0.32185798264647947, best_reachable_tp=29529.499999999996, post_stop_equity_usd=4725.89028, min_lot_spread_cash_usd=0.122
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 29868.505855 sits inside un-swept purchase-side stop fuel [29800.0, 30900.0] = 3.847M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.32R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.32R against the minimum compliant stop (1053.3 points = clear the 30900.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.32R < 2.0R required for NAS100.p
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4725.890 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_relief_rally_short` — STAGE SHORT BTC
> Astra CP-113/114 hypothesis re-derived: relief flow into the EMA20 81,625 shelf, but mid has now slipped back BELOW the shelf (81,529) and the compliant stop must clear the [81,600-82,600] purchase belt.
- metrics: symbol=BTCUSD.pi, mid=81529.0, atr_14=235.7105, regime=BEARISH, entry=81600.0, sl=82530.0, tp=80950.0, lots=0.01, stop_points=930.0, risk_usd=9.3, reward_usd=6.5, rr_gross=0.6989247311827956, rr_min_required=2.0, entry_distance_atr=0.3012169589390375, friction_pct=1.7204301075268817, sl_clearance_atr=-0.29697446655961446, hazard_union=[81600.0, 82600.0], hazard_union_usd=39577093.589999996, in_range_defense_usd=97012767.37999997, overwhelm_ratio=0.40795757773795, post_stop_equity_usd=4845.925, min_lot_spread_cash_usd=0.16
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 82530.0 sits INSIDE the purchase-side sweep belt [81600.0, 82600.0] carrying 39.577M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81600.0 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 39.577M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 81529.0 sits inside the sell-stop/long-cascade ladder [80600.0, 81600.0] carrying 125.258M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (81529.0) to front-run; nearest qualifying pool is 80200.0-80300.0 USD 4.87 ATR from mid
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80950.0 sits INSIDE the magnet pool [80900.0, 81000.0] carrying 25.574M USD instead of front-running it
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.70R < 2.0R required for BTCUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 5,203,408
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD

### `eth_watch_probe` — STAGE SHORT ETH
> Astra's ETH VAL-shelf ticket skeleton tested verbatim for a third generation: entry 2,432 inside the 2,426.6-2,442.7 zone, SL 2,464.35, TP 2,395.2. No rejection wick has formed (max upper wick 0.29 ATR) and the engine returns no legal front-runnable geometry at all (mid sits inside the [2,300-2,420] ladder).
- metrics: symbol=ETHUSD.pi, mid=2418.15, atr_14=9.9609, regime=BEARISH, entry=2432.0, sl=2464.35, tp=2395.2, lots=0.38, stop_points=32.34999999999991, risk_usd=12.292999999999966, reward_usd=13.98400000000007, rr_gross=1.1375579598145373, rr_min_required=2.2, entry_distance_atr=1.3904366071338843, friction_pct=11.437403400309151, sl_clearance_atr=-4.452408918872783, hazard_union=[2420.0, 2540.0], hazard_union_usd=19000250.45, in_range_defense_usd=43087255.62999999, overwhelm_ratio=0.174562918896211, post_stop_equity_usd=4842.18375, min_lot_spread_cash_usd=0.037000000000000005
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.371 exceeds 0.18
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 2464.35 sits INSIDE the purchase-side sweep belt [2420.0, 2540.0] carrying 19.000M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2432.0 sits inside un-swept purchase-side stop fuel [2420.0, 2540.0] = 19.000M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 2418.15 sits inside the sell-stop/long-cascade ladder [2300.0, 2420.0] carrying 323.559M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2395.2 sits INSIDE the magnet pool [2390.0, 2400.0] carrying 35.627M USD instead of front-running it
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.14R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL

### `uswti_bullish_pullback_long` — STAGE LONG USWTI
> The only BULLISH regime with trapped sellers below; pullback into the prior-day POC 94.29 / weekly VWAP 93.85 shelf. Best commodity wall is $0.32M against the $0.75M shield and the stop belts overlap the shelf.
- metrics: symbol=USWTI.p, mid=94.506, atr_14=0.2168, regime=BULLISH, entry=94.29, sl=93.0, tp=94.94, lots=0.09, stop_points=1.2900000000000063, risk_usd=11.610000000000056, reward_usd=5.849999999999923, rr_gross=0.503875968992239, rr_min_required=2.0, entry_distance_atr=0.9963099630996033, friction_pct=3.5658914728682, sl_clearance_atr=-1.3837638376383634, hazard_union=[91.8, 93.3], hazard_union_usd=3957851.0700000003, in_range_defense_usd=1784384.3599999999, overwhelm_ratio=1.7317579660920142, post_stop_equity_usd=4843.0375, min_lot_spread_cash_usd=0.046
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.212 exceeds 0.18
- FATAL `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 93.0 sits INSIDE the sale-side sweep belt [91.8, 93.3] carrying 3.958M USD
- MAJOR `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.285M < 0.75M COMMODITY requirement
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.50R < 2.0R required for USWTI.p
  - Orderflow & Microstructure: 49.8/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN

### `gold_range_gate_probe` — STAGE SHORT GOLD
> GOLD is RANGE_BOUND again with RSI 75.18 while SELLER_AGGRESSION prints in the TradFi tape: the regime gate strikes the card down before geometry, and the commodity shield fails at $0.61M < $0.75M.
- metrics: symbol=XAUUSD.pi, mid=4140.615, atr_14=8.0394, regime=RANGE_BOUND, entry=4144.63, sl=4149.46, tp=4132.58, lots=0.02, stop_points=4.829999999999927, risk_usd=9.659999999999854, reward_usd=24.100000000000364, rr_gross=2.4948240165632223, rr_min_required=2.0, entry_distance_atr=0.4994153792571992, friction_pct=1.4492753623188626, sl_clearance_atr=-1.1767047292086519, hazard_union=[4140.0, 4260.0], hazard_union_usd=1982600.4, in_range_defense_usd=526971.3, overwhelm_ratio=0.07638744273170094, post_stop_equity_usd=4845.475, min_lot_spread_cash_usd=0.07
- FATAL `REGIME_GATED_STAND_ASIDE` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime=RANGE_BOUND: neither engine applies in non-trending noise
- MINOR `MAGNET_UNTRUSTED_EXCLUDED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — 1 bin(s) excluded as untrusted (> 10x the larger neighbour); largest [3980.0, 3990.0] carrying 10.123M USD cannot anchor a TP
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 4149.46 sits INSIDE the purchase-side sweep belt [4140.0, 4260.0] carrying 1.983M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4144.63 sits inside un-swept purchase-side stop fuel [4140.0, 4260.0] = 1.983M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.333M < 0.75M COMMODITY requirement
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (4140.615) to front-run; nearest qualifying pool is 4050.0-4080.0 USD 7.03 ATR from mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 4132.58 is 128.87 bps from the governing magnet edge 4080.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Structural Price Action: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN

### `desk_batch_4x_max_risk` — STAGE_BATCH SHORT BTC
> Capacity strawman: four max-envelope tickets (4 x 20.12 = 80.48 stress) against the 64.55 USD budget; the ceiling is three tickets (60.36).
- metrics: symbol=BTCUSD.pi, mid=81529.0, atr_14=235.7105, regime=BEARISH, min_lot_spread_cash_usd=0.16
- FATAL `CARD_INCOMPLETE` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — trade card is missing entry/SL/TP/lots
  - Orderflow & Microstructure: 64.3/100 — fatal: CARD_INCOMPLETE
  - Structural Price Action: 49.9/100 — fatal: CARD_INCOMPLETE
  - Liquidation & Stop Forensic: 49.9/100 — fatal: CARD_INCOMPLETE
  - Macro Risk & Portfolio Governor: 57.1/100 — fatal: CARD_INCOMPLETE
  - Adversarial Pre-Mortem Red Team: 57.1/100 — fatal: CARD_INCOMPLETE

### `eth_val_rejection_watch` — WATCH None ETH
> Peer-audit watch, generation 2 of the re-test spec. ETH traded DOWN out of the zone (mid 2,418.15, below the VAL 2,424.04 and the EMA20 2,419.68) with rising 15m closes back toward it. The rejection wick never formed (max upper wick 0.29 ATR vs the 0.5 ATR gate), and the engine now returns NO legal front-runnable geometry at all because mid sits inside the $323.6M [2,300-2,420] ladder.
- metrics: symbol=ETHUSD.pi, mid=2418.15, atr_14=9.9609, regime=BEARISH, min_lot_spread_cash_usd=0.037000000000000005
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.371 exceeds 0.18
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: >= 0.5 ATR rejection wick off the 2,424.0-2,442.7 zone AND >= 2.0R geometry at the compliant stop (currently none) AND symmetric shield (bid 2,392.2 $15.48M vs ask 2,442.0 $8.15M / 2,457.6 $15.90M - satisfied)
  - Orderflow & Microstructure: 61.8/100 — no fatal flaw found
  - Structural Price Action: 65.39/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 65.39/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 54.6/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 61.8/100 — no fatal flaw found

### `nas100_belt_thin_watch` — WATCH None NAS100
> The purchase-side belt that falsified this watch in Cycle 112 has THINNED: stops above now read [29,800-29,900] $0.109M and liquidation band [29,900-30,000] $0.114M (was $4.12M combined). One precondition of three now holds; the rally and the >= $1.0M ask shield do not (best shelf-adjacent ask wall is $0.97M at 29,868/481 s vs the $1.0M index shield).
- metrics: symbol=NAS100.p, mid=29747.14, atr_14=62.2389, regime=BEARISH, min_lot_spread_cash_usd=0.122
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: relief rally >= 29,930 with velocity_ratio < 0.70 AND a >= 1.0M USD ask wall defending the 29,850-29,900 EMA20 shelf AND engine geometry >= 2.0R (currently 0.32R ceiling)
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `btc_ladder_break_watch` — WATCH None BTC
> BTC is coiling under the EMA20 81,625 with the $25.0M/13,443 s bid wall at 81,196 the only defence and the [81,600-82,600] purchase belt overhead. A decisive loss of 81,000 opens the 79,800-80,100 pool.
- metrics: symbol=BTCUSD.pi, mid=81529.0, atr_14=235.7105, regime=BEARISH, min_lot_spread_cash_usd=0.16
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: 15m close < 81,000 with session CVD < 0 and the 81,196 bid wall thinning
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle114` — STAND_ASIDE
> Second consecutive generation with the session-VWAP bridge dark (vwap_z_score null on all 24 assets) and zero payable geometry: Engine 1 NOT EVALUABLE, Engine 2 fails the exit leg or min-lot affordability on every asset. Re-proves itself card by card.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 14 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
