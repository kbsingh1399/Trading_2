# Arena tournament cycle110_20261014T230045Z

- snapshot: `/tmp/snap110.json` generation `6a96f85bd4af40bb80306742add1e822` as_of `2026-10-14 23:00:45 UTC`
- cards: `docs/trade_plans/arena_cards/cycle110_20261014T230045Z.json` sha256 `08c7c22ac9a4f2f5`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 106 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle110`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle110` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `btc_armed_post_sweep_short` | WATCH | no | - | 69.00 | advisory only |
| `sol_ticket_18925879_reaudit` | DELETE | no | - | 59.64 | VERIFIED |
| `near_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 51.39 | CONTRADICTED |
| `btc_ladder_top_long` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `sol_repair_short` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD | 48.00 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `trx_bullish_regime_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `gold_minlot_floor_probe` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `ger40_engine1_long` | STAGE | YES | - | 44.84 | CONTRADICTED |
| `btc_ladder_straddle_short` | STAGE | YES | ENTRY_IN_FUEL | 43.77 | CONTRADICTED |
| `eth_straddle_short` | STAGE | YES | ENTRY_IN_FUEL | 42.58 | CONTRADICTED |
| `desk_batch_4x_max_risk` | STAGE_BATCH | YES | ENTRY_IN_FUEL | 42.58 | CONTRADICTED |
| `uswti_bullish_regime_long` | STAGE | YES | COUNTER_CVD | 42.50 | CONTRADICTED |
| `dj30_empty_book_probe` | STAGE | YES | NO_BUNKER_WALL, COUNTER_CVD | 42.50 | CONTRADICTED |

## Bracket
### Round 1
- `near_friction_probe` (51.39, fatal=True) vs `eth_straddle_short` (42.58, fatal=True) -> **near_friction_probe** — higher rubric total (51.39 vs 42.58)
- `gold_minlot_floor_probe` (48.0, fatal=True) vs `sol_repair_short` (48.0, fatal=True) -> **gold_minlot_floor_probe** — exact tie: fewer standing attacks (deterministic order)
- `btc_ladder_top_long` (48.0, fatal=True) vs `dj30_empty_book_probe` (42.5, fatal=True) -> **btc_ladder_top_long** — higher rubric total (48.0 vs 42.5)
- `ger40_engine1_long` (44.84, fatal=True) vs `sp500_core_short` (48.0, fatal=True) -> **sp500_core_short** — higher rubric total (48.0 vs 44.84)
- `sol_ticket_18925879_reaudit` (59.64, fatal=False) vs `btc_armed_post_sweep_short` (69.0, fatal=False) -> **btc_armed_post_sweep_short** — higher rubric total (69.0 vs 59.64)
- `desk_stand_aside_cycle110` (71.5, fatal=False) vs `uswti_bullish_regime_long` (42.5, fatal=True) -> **desk_stand_aside_cycle110** — uswti_bullish_regime_long is contradicted by the snapshot; desk_stand_aside_cycle110 is not
- `btc_ladder_straddle_short` (43.77, fatal=True) vs `trx_bullish_regime_long` (48.0, fatal=True) -> **trx_bullish_regime_long** — higher rubric total (48.0 vs 43.77)
- bye: `desk_batch_4x_max_risk`
### Round 2
- `near_friction_probe` (51.39, fatal=True) vs `gold_minlot_floor_probe` (48.0, fatal=True) -> **near_friction_probe** — higher rubric total (51.39 vs 48.0)
- `btc_ladder_top_long` (48.0, fatal=True) vs `sp500_core_short` (48.0, fatal=True) -> **btc_ladder_top_long** — exact tie: fewer standing attacks (deterministic order)
- `btc_armed_post_sweep_short` (69.0, fatal=False) vs `desk_stand_aside_cycle110` (71.5, fatal=False) -> **desk_stand_aside_cycle110** — higher rubric total (71.5 vs 69.0)
- `trx_bullish_regime_long` (48.0, fatal=True) vs `desk_batch_4x_max_risk` (42.58, fatal=True) -> **trx_bullish_regime_long** — higher rubric total (48.0 vs 42.58)
### Round 3
- `near_friction_probe` (51.39, fatal=True) vs `btc_ladder_top_long` (48.0, fatal=True) -> **near_friction_probe** — higher rubric total (51.39 vs 48.0)
- `desk_stand_aside_cycle110` (71.5, fatal=False) vs `trx_bullish_regime_long` (48.0, fatal=True) -> **desk_stand_aside_cycle110** — trx_bullish_regime_long is contradicted by the snapshot; desk_stand_aside_cycle110 is not
### Round 4
- `near_friction_probe` (51.39, fatal=True) vs `desk_stand_aside_cycle110` (71.5, fatal=False) -> **desk_stand_aside_cycle110** — near_friction_probe is contradicted by the snapshot; desk_stand_aside_cycle110 is not

## Findings per card
### `btc_ladder_straddle_short` — STAGE SHORT BTC
> Engine 2 short at the perimeter. Kills on geometry: mid sits INSIDE the $94.59M sell-stop ladder [80,500-81,600], so no front-runnable exit exists; the contiguous $41.04M buy-stop belt [81,600-82,600] forces a 2.6-ATR stop.
- metrics: symbol=BTCUSD.pi, mid=81563.5, atr_14=252.3035, regime=BEARISH, entry=82055.49, sl=82690.83, tp=81681.6, lots=0.02, stop_points=635.3399999999965, risk_usd=12.70679999999993, reward_usd=7.477799999999989, rr_gross=0.5884880536405728, rr_min_required=2.0, entry_distance_atr=1.949992766648125, friction_pct=2.675732678565822, sl_clearance_atr=0.36000293297557007, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=45859899.67, overwhelm_ratio=0.5310887678616676, post_stop_equity_usd=4841.6665, min_lot_spread_cash_usd=0.17
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82055.49 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 81563.5 sits inside the sell-stop/long-cascade ladder [80500.0, 81600.0] carrying 151.610M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (81563.5) to front-run; nearest qualifying pool is 80200.0-80300.0 USD 4.69 ATR from mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 81681.6 is 10.00 bps from the governing magnet edge 81600.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.59R < 2.0R required for BTCUSD.pi
  - Orderflow & Microstructure: 48.87/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_ladder_top_long` — STAGE LONG BTC
> Mirror probe: the long side is banned outright in a verified BEARISH HTF regime.
- metrics: symbol=BTCUSD.pi, mid=81563.5, atr_14=252.3035, regime=BEARISH, entry=81071.51, sl=80410.43, tp=81938.5, lots=0.02, stop_points=661.0800000000017, risk_usd=13.221600000000036, reward_usd=17.339800000000107, rr_gross=1.3114751618563607, rr_min_required=2.0, entry_distance_atr=1.949992766648125, friction_pct=2.571549585526707, sl_clearance_atr=0.35500894755723555, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=71382297.77000003, overwhelm_ratio=0.8755982630509819, best_reachable_rr=1.2804652992073622, best_reachable_tp=81918.0, post_stop_equity_usd=4841.023, min_lot_spread_cash_usd=0.17
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81071.51 sits inside un-swept sale-side stop fuel [80500.0, 81600.0] = 119.711M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.28R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.28R against the minimum compliant stop (659.8 points = clear the 80500.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.31R < 2.0R required for BTCUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -103,544,383
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `eth_straddle_short` — STAGE SHORT ETH
> ETH mirror of BTC: mid sits inside the $101.87M sell-stop ladder [2,320-2,420] and the buy-stop belt [2,420-2,530] is contiguous, so both the exit and the stop are gated.
- metrics: symbol=ETHUSD.pi, mid=2416.4, atr_14=11.1429, regime=BEARISH, entry=2438.13, sl=2534.01, tp=2422.42, lots=0.11, stop_points=95.88000000000011, risk_usd=10.546800000000012, reward_usd=1.728100000000004, rr_gross=0.16385064664163557, rr_min_required=2.2, entry_distance_atr=1.9501207046639581, friction_pct=2.9203170629954074, sl_clearance_atr=0.35987041075485005, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=28526309.55, overwhelm_ratio=0.6018035469996503, post_stop_equity_usd=4844.3665, min_lot_spread_cash_usd=0.027999999999999997
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.251 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2438.13 sits inside un-swept purchase-side stop fuel [2420.0, 2530.0] = 17.967M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 2416.4 sits inside the sell-stop/long-cascade ladder [2300.0, 2420.0] carrying 316.033M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2422.42 is 10.00 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.16R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 42.9/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sol_repair_short` — STAGE SHORT SOL
> Rebuild of the cancelled ticket: compliant stop clearing the [104,114] $15.38M belt by 0.36 ATR, exit front-running the [93,104] $67.3M ladder. Ceiling 0.28R, overwhelm 2.47:1.
- metrics: symbol=SOLUSD.p, mid=104.435, atr_14=0.5496, regime=BEARISH, entry=105.51, sl=114.2, tp=104.078, lots=0.01, stop_points=8.689999999999998, risk_usd=8.689999999999998, reward_usd=1.4320000000000022, rr_gross=0.16478711162255497, rr_min_required=2.5, entry_distance_atr=1.95596797671034, friction_pct=2.6467203682393565, sl_clearance_atr=0.36390101892285814, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=9001090.66, overwhelm_ratio=1.6767662375705923, best_reachable_rr=0.16179516685846035, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.6875, min_lot_spread_cash_usd=0.23
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.418 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.51 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 15.382M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 4.850M < 5.00M CRYPTO_ALT requirement
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.16R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.16R against the minimum compliant stop (8.7 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.16R < 2.5R required for SOLUSD.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 7,648,123
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD

### `sp500_core_short` — STAGE SHORT SP500
> TradFi friction champion (0.44 bps). Unpayable anyway: the [7,700-7,810] index cluster belt forces a 90-point stop against a 37-point reachable reward (0.41R).
- metrics: symbol=SP500.p, mid=7703.92, atr_14=9.8975, regime=BEARISH, entry=7723.22, sl=7813.51, tp=7685.76, lots=0.01, stop_points=90.28999999999996, risk_usd=9.028999999999996, reward_usd=3.7460000000000035, rr_gross=0.4148853693653788, rr_min_required=2.0, entry_distance_atr=1.9499873705481363, friction_pct=0.37656440358843746, sl_clearance_atr=0.35463500884063837, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=22407725.06, overwhelm_ratio=0.1948680086134545, best_reachable_rr=0.3936205559862763, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4846.26375, min_lot_spread_cash_usd=0.034
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7723.22 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 18418.565M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.39R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.39R against the minimum compliant stop (90.2 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.41R < 2.0R required for SP500.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 46
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `near_friction_probe` — STAGE SHORT NEAR
> The only >=2.0R geometry in the 24-asset screen (2.53R) dies on the 15% dynamic friction rule: spread 0.032 USD / 0.077 stop = 41.5% of risk. Banned-instrument list confirmed.
- metrics: symbol=NERUSD.p, mid=4.873, atr_14=0.0438, regime=BEARISH, entry=4.9584, sl=5.0355, tp=4.7636, lots=1.0, stop_points=0.07709999999999972, risk_usd=7.709999999999972, reward_usd=19.479999999999986, rr_gross=2.526588845655001, rr_min_required=2.0, entry_distance_atr=1.949771689497715, friction_pct=41.50453955901441, sl_clearance_atr=0.35388127853881945, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=2.511543450064875, best_reachable_tp=4.764759999999999, post_stop_equity_usd=4847.9125, min_lot_spread_cash_usd=3.2
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 65.67 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.731 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.20 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.032 / stop distance 0.077 = 41.50% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.9584 sits inside un-swept purchase-side stop fuel [4.87, 5.02] = 1.371M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 64.02/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.92/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `ger40_engine1_long` — STAGE LONG GER40
> Engine 1 mean-reversion probe (the only |Z| >= 2.0 on the book, Z = -2.07): banned in a BEARISH regime and structurally empty - zero L3 walls, zero stop clusters, zero magnets.
- metrics: symbol=GER40.p, mid=25203.4, atr_14=26.8077, regime=BEARISH, entry=25195.36, sl=25171.23, tp=25243.61, lots=0.04, stop_points=24.13000000000102, risk_usd=9.652000000000408, reward_usd=19.3, rr_gross=1.9995855781184402, rr_min_required=2.0, entry_distance_atr=0.2999138307277712, friction_pct=12.847078325735056, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4845.485, min_lot_spread_cash_usd=0.31
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 2.00R < 2.0R required for GER40.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 42.94/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Structural Price Action: 44.3/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Liquidation & Stop Forensic: 42.94/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 51.5/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_MAGNETS, COUNTER_TREND

### `trx_bullish_regime_long` — STAGE LONG TRX
> The book's only BULLISH regime (TRX). No wall >= 180s and no magnet >= 0.50M USD on the long side, and the min-lot spread cash is 9.00 USD - friction gate blocks it.
- metrics: symbol=TRXUSD.p, mid=0.3321, atr_14=0.0003, regime=BULLISH, entry=0.33195, sl=0.33174, tp=0.33246, lots=5.0, stop_points=0.00021000000000004349, risk_usd=10.500000000002174, reward_usd=25.499999999997748, rr_gross=2.428571428570711, rr_min_required=2.0, entry_distance_atr=0.499999999999945, friction_pct=380.9523809523021, sl_clearance_atr=-0.8666666666667934, hazard_union=[0.32, 0.332], hazard_union_usd=430171.96, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4844.424999999997, min_lot_spread_cash_usd=8.0
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 2.667 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 8.00 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.0008 / stop distance 0.000 = 380.95% of risk, above the 15% dynamic friction ceiling
- FATAL `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 0.33174 sits INSIDE the sale-side sweep belt [0.32, 0.332] carrying 0.430M USD
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS

### `uswti_bullish_regime_long` — STAGE LONG USWTI
> Second BULLISH regime asset. No material magnet within the 3.5-ATR horizon on the long side (largest buy-stop run above is 0.07M USD) - no reachable exit.
- metrics: symbol=USWTI.p, mid=94.9, atr_14=0.244, regime=BULLISH, entry=94.778, sl=94.461, tp=95.388, lots=0.33, stop_points=0.3170000000000073, risk_usd=10.46100000000024, reward_usd=20.12999999999998, rr_gross=1.9242902208201433, rr_min_required=2.0, entry_distance_atr=0.49999999999999956, friction_pct=14.511041009463387, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4844.47375, min_lot_spread_cash_usd=0.046
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.189 exceeds 0.18
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.92R < 2.0R required for USWTI.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -10
  - Orderflow & Microstructure: 42.5/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 42.5/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: COUNTER_CVD

### `gold_minlot_floor_probe` — STAGE SHORT GOLD
> Best raw TradFi geometry of the metals (0.39R ceiling) dies on lot granularity: the min lot 0.01 sizes a 92.54 USD risk against the 14.50 USD envelope (FLOOR_BREACH).
- metrics: symbol=XAUUSD.pi, mid=4106.59, atr_14=6.8146, regime=BEARISH, entry=4119.88, sl=4212.42, tp=4083.06, lots=0.01, stop_points=92.53999999999996, risk_usd=92.53999999999996, reward_usd=36.820000000000164, rr_gross=0.39788199697428334, rr_min_required=2.0, entry_distance_atr=1.9502245179467559, friction_pct=0.1296736546358332, sl_clearance_atr=0.3551198896487061, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=3956612.2699999996, overwhelm_ratio=0.4567156387047246, best_reachable_rr=0.3868597363302426, best_reachable_tp=4084.0799999999995, post_stop_equity_usd=4741.875, min_lot_spread_cash_usd=0.12
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4119.88 sits inside un-swept purchase-side stop fuel [4110.0, 4210.0] = 1.807M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.39R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.39R against the minimum compliant stop (92.5 points = clear the 4210.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.40R < 2.0R required for XAUUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 38
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4741.875 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `dj30_empty_book_probe` — STAGE SHORT DJ30
> DJ30 is the cleanest structural void: zero walls >= 180s, zero stop clusters, zero cascade bands, zero magnets - both engines have nothing to trade.
- metrics: symbol=DJ30.p, mid=51621.85, atr_14=56.0273, regime=BEARISH, entry=51731.1, sl=51845.96, tp=51509.8, lots=0.1, stop_points=114.86000000000058, risk_usd=114.86000000000058, reward_usd=221.29999999999563, rr_gross=1.926693365836623, rr_min_required=2.0, entry_distance_atr=1.9499422602909655, friction_pct=1.375587671948452, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4713.974999999999, min_lot_spread_cash_usd=0.158
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.93R < 2.0R required for DJ30.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 6
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4713.975 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 42.5/100 — fatal: NO_MAGNETS, FLOOR_BREACH | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 42.5/100 — fatal: NO_MAGNETS, FLOOR_BREACH | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_MAGNETS, FLOOR_BREACH | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_MAGNETS, FLOOR_BREACH | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_MAGNETS, FLOOR_BREACH | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD

### `desk_batch_4x_max_risk` — STAGE_BATCH SHORT BTC
> Floor-governance strawman: fill all 4 free slots at max risk (4 x 20.13 = 80.50 USD stress) against a 64.55 USD budget. Shows the exact boundary: 3 tickets fit, 4 breach.
- metrics: symbol=BTCUSD.pi, mid=81563.5, atr_14=252.3035, regime=BEARISH, entry=82055.49, sl=82690.83, tp=81681.6, lots=0.022, stop_points=635.3399999999965, risk_usd=13.977479999999922, reward_usd=8.225579999999987, rr_gross=0.5884880536405728, rr_min_required=2.0, entry_distance_atr=1.949992766648125, friction_pct=2.675732678565822, sl_clearance_atr=0.36000293297557007, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=45859899.67, overwhelm_ratio=0.5310887678616676, post_stop_equity_usd=4781.662600000001, min_lot_spread_cash_usd=0.17
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82055.49 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 81563.5 sits inside the sell-stop/long-cascade ladder [80500.0, 81600.0] carrying 151.610M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (81563.5) to front-run; nearest qualifying pool is 80200.0-80300.0 USD 4.69 ATR from mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 81681.6 is 10.00 bps from the governing magnet edge 81600.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.59R < 2.0R required for BTCUSD.pi
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4781.663 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 42.9/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sol_ticket_18925879_reaudit` — DELETE  SOL
> Part CP re-audit of the cancelled ticket's exact levels (SELL LIMIT 0.10 @ 104.90 / SL 105.75 / TP 103.10) against the newest generation: if the desk re-staged it, it would fail the same gates.
- metrics: symbol=SOLUSD.p, mid=104.435, atr_14=0.5496, regime=BEARISH, entry=104.9, sl=105.75, tp=103.1, lots=0.1, stop_points=0.8499999999999943, risk_usd=8.499999999999943, reward_usd=18.000000000000114, rr_gross=2.117647058823557, entry_distance_atr=0.8460698689956394, friction_pct=27.058823529411946, sl_clearance_atr=-3.184133915574964, hazard_union=[104.0, 114.0], hazard_union_usd=15382185.44, in_range_defense_usd=17108808.92, overwhelm_ratio=0.037739778556133405, best_reachable_rr=0.9364705882353247, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.925, min_lot_spread_cash_usd=0.23, delete_justification=['FRICTION_BUDGET', 'SL_INSIDE_SWEEP', 'UNPAYABLE_GEOMETRY', 'NO_PAYABLE_SETUP', 'TP_INSIDE_MAGNET', 'SPREAD_OVER_ATR', 'ENTRY_IN_FUEL', 'BUNKER_WALL_THIN', 'RR_BELOW_MIN', 'COUNTER_CVD'], probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.418 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.418 exceeds 0.18
- MINOR `PROBE_FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.23 / stop distance 0.850 = 27.06% of risk, above the 15% dynamic friction ceiling
- MINOR [purchase-side] `PROBE_SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 105.75 sits INSIDE the purchase-side sweep belt [104.0, 114.0] carrying 15.382M USD
- MINOR [purchase-side] `PROBE_ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 104.9 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 15.382M USD
- MINOR [purchase-side] `PROBE_BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 4.850M < 5.00M CRYPTO_ALT requirement
- MINOR `PROBE_UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.94R at this card's stop < required 2.5R
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.09R against the minimum compliant stop (9.3 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- MINOR `PROBE_TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 103.1 sits INSIDE the magnet pool [103.0, 104.0] carrying 3.273M USD instead of front-running it
- MINOR `PROBE_RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 2.12R < 2.5R required for SOLUSD.p
- MINOR [purchase-side] `PROBE_COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 7,648,123
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.418 exceeds 0.18
- probe FATAL `FRICTION_BUDGET` (A7) — spread 0.23 / stop distance 0.850 = 27.06% of risk, above the 15% dynamic friction ceiling
- probe FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1) — SL 105.75 sits INSIDE the purchase-side sweep belt [104.0, 114.0] carrying 15.382M USD
- probe MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8) — entry 104.9 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 15.382M USD
- probe MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4) — largest in-range wall 4.850M < 5.00M CRYPTO_ALT requirement
- probe FATAL `UNPAYABLE_GEOMETRY` (A6) — best reachable front-runnable target yields 0.94R at this card's stop < required 2.5R
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.09R against the minimum compliant stop (9.3 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- probe FATAL `TP_INSIDE_MAGNET` (A6) — TP 103.1 sits INSIDE the magnet pool [103.0, 104.0] carrying 3.273M USD instead of front-running it
- probe MAJOR `RR_BELOW_MIN` (A6) — quoted geometry 2.12R < 2.5R required for SOLUSD.p
- probe MAJOR [purchase-side] `COUNTER_CVD` (A2) — short against positive session CVD 7,648,123
  - Orderflow & Microstructure: 61.8/100 — no fatal flaw found
  - Structural Price Action: 65.41/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 58.19/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 53.41/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 59.4/100 — no fatal flaw found

### `btc_armed_post_sweep_short` — WATCH  BTC
> Armed posture, not an order: mid is pinned inside the $94.59M sell-stop ladder while $41.04M of buy-stop fuel sits overhead [81,600-82,600] behind a $22.83M verified wall at 82,868. If that fuel is swept and price closes back inside, the overhead hazard is consumed and a post-sweep short can be derived with a realised-high stop.
- metrics: symbol=BTCUSD.pi, mid=81563.5, atr_14=252.3035, regime=BEARISH, min_lot_spread_cash_usd=0.17
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: BTCUSD.pi prints a 15m high >= 82,620 (through the [81,600-82,600] belt top) AND closes back below 82,450 while session CVD stays negative
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle110` — STAND_ASIDE
> No new ticket: Engine 1 triggers nowhere usable (GER40 is the only |Z| >= 2.0 and is counter-trend with an empty book), Engine 2 geometry is unpayable or blocked on all 24 assets (BTC/ETH are pinned inside six-figure liquidation ladders; NEAR prints 2.53R but pays 41.5% friction), and the 4 free slots stay unspent.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 10 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
