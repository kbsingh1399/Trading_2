# Arena tournament cycle109_20261014T223246Z

- snapshot: `/tmp/snap109.json` generation `f9286408c3e24884ac0bd85af53c4fb5` as_of `2026-10-14 22:32:46 UTC`
- cards: `docs/trade_plans/arena_cards/cycle109_20261014T223246Z.json` sha256 `1adc0d105567ccc5`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 106 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle109`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle109` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `btc_armed_post_sweep_short` | WATCH | no | - | 69.00 | advisory only |
| `sol_ticket_18925879_postmortem` | DELETE | no | - | 67.80 | VERIFIED |
| `desk_batch_3x_max_risk` | STAGE_BATCH | YES | ENTRY_IN_FUEL | 49.55 | CONTRADICTED |
| `btc_perimeter_short_robust` | STAGE | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED |
| `btc_perimeter_short_exact` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `btc_deep_tp_extension` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `eth_repair_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `sol_short_repair` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD | 48.00 | CONTRADICTED |
| `near_short_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 48.00 | CONTRADICTED |
| `trx_long_bullish_regime` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `ger40_engine1_meanreversion` | STAGE | YES | - | 42.59 | CONTRADICTED |

## Bracket
### Round 1
- `sol_short_repair` (48.0, fatal=True) vs `sol_ticket_18925879_postmortem` (67.8, fatal=False) -> **sol_ticket_18925879_postmortem** — sol_short_repair is contradicted by the snapshot; sol_ticket_18925879_postmortem is not
- `eth_repair_short` (48.0, fatal=True) vs `btc_perimeter_short_robust` (48.18, fatal=True) -> **btc_perimeter_short_robust** — higher rubric total (48.18 vs 48.0)
- `ger40_engine1_meanreversion` (42.59, fatal=True) vs `btc_deep_tp_extension` (48.0, fatal=True) -> **btc_deep_tp_extension** — higher rubric total (48.0 vs 42.59)
- `desk_batch_3x_max_risk` (49.55, fatal=True) vs `desk_stand_aside_cycle109` (71.5, fatal=False) -> **desk_stand_aside_cycle109** — desk_batch_3x_max_risk is contradicted by the snapshot; desk_stand_aside_cycle109 is not
- `sp500_core_short` (48.0, fatal=True) vs `trx_long_bullish_regime` (48.0, fatal=True) -> **sp500_core_short** — exact tie: fewer standing attacks (deterministic order)
- `btc_perimeter_short_exact` (48.0, fatal=True) vs `near_short_friction_probe` (48.0, fatal=True) -> **btc_perimeter_short_exact** — exact tie: fewer standing attacks (deterministic order)
- bye: `btc_armed_post_sweep_short`
### Round 2
- `sol_ticket_18925879_postmortem` (67.8, fatal=False) vs `btc_perimeter_short_robust` (48.18, fatal=True) -> **sol_ticket_18925879_postmortem** — btc_perimeter_short_robust is contradicted by the snapshot; sol_ticket_18925879_postmortem is not
- `btc_deep_tp_extension` (48.0, fatal=True) vs `desk_stand_aside_cycle109` (71.5, fatal=False) -> **desk_stand_aside_cycle109** — btc_deep_tp_extension is contradicted by the snapshot; desk_stand_aside_cycle109 is not
- `sp500_core_short` (48.0, fatal=True) vs `btc_perimeter_short_exact` (48.0, fatal=True) -> **sp500_core_short** — exact tie: fewer standing attacks (deterministic order)
- bye: `btc_armed_post_sweep_short`
### Round 3
- `sol_ticket_18925879_postmortem` (67.8, fatal=False) vs `desk_stand_aside_cycle109` (71.5, fatal=False) -> **desk_stand_aside_cycle109** — higher rubric total (71.5 vs 67.8)
- `sp500_core_short` (48.0, fatal=True) vs `btc_armed_post_sweep_short` (69.0, fatal=False) -> **btc_armed_post_sweep_short** — sp500_core_short is contradicted by the snapshot; btc_armed_post_sweep_short is not
### Round 4
- `desk_stand_aside_cycle109` (71.5, fatal=False) vs `btc_armed_post_sweep_short` (69.0, fatal=False) -> **desk_stand_aside_cycle109** — higher rubric total (71.5 vs 69.0)

## Findings per card
### `btc_perimeter_short_exact` — STAGE SHORT BTC
> The single most favourable card on the book: Model 2 short at the extreme mid + 2.0 ATR perimeter (8,2044.08), stop clearing the 41.04M USD 81,600-82,600 belt by 0.35 ATR, TP front-running the deepest reachable sell-stop pool. Tests whether BTC's 2.001R ceiling is real and reachable.
- metrics: symbol=BTCUSD.pi, mid=81554.5, atr_14=244.7899, regime=BEARISH, entry=82044.08, sl=82685.68, tp=80720.0, lots=0.02, stop_points=641.5999999999913, risk_usd=12.831999999999825, reward_usd=26.481600000000036, rr_gross=2.063715710723223, rr_min_required=2.0, entry_distance_atr=2.00000081702718, friction_pct=2.649625935162131, sl_clearance_atr=0.35001444095525597, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=43424134.73000001, overwhelm_ratio=0.5608719524622752, best_reachable_rr=1.9691084788030266, best_reachable_tp=80780.7, post_stop_equity_usd=4841.51, min_lot_spread_cash_usd=0.17
- FATAL `ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.00 ATR from mid (>2.0 ATR bound)
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82044.08 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.97R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.97R against the minimum compliant stop (641.6 points = clear the 82600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80720.0 sits INSIDE the magnet pool [80700.0, 80800.0] carrying 15.512M USD instead of front-running it
  - Orderflow & Microstructure: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_perimeter_short_robust` — STAGE SHORT BTC
> Robustness probe: identical but with a 0.50 ATR bunker clearance instead of the 0.35 ATR minimum. If the payable window only exists at the 0.35 ATR boundary, this card must fail - that is what makes the previous card a knife-edge rather than a setup.
- metrics: symbol=BTCUSD.pi, mid=81554.5, atr_14=244.7899, regime=BEARISH, entry=82044.0, sl=82722.0, tp=80720.0, lots=0.02, stop_points=678.0, risk_usd=13.56, reward_usd=26.48, rr_gross=1.952802359882006, rr_min_required=2.0, entry_distance_atr=1.999674006157934, friction_pct=2.5073746312684366, sl_clearance_atr=0.4983865755899243, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=43424134.73000001, overwhelm_ratio=0.5608719524622752, best_reachable_rr=1.86327433628319, best_reachable_tp=80780.7, post_stop_equity_usd=4840.6, min_lot_spread_cash_usd=0.17
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82044.0 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.86R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.97R against the minimum compliant stop (641.7 points = clear the 82600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80720.0 sits INSIDE the magnet pool [80700.0, 80800.0] carrying 15.512M USD instead of front-running it
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.95R < 2.0R required for BTCUSD.pi
  - Orderflow & Microstructure: 48.92/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_deep_tp_extension` — STAGE SHORT BTC
> Horizon-sensitivity probe: what if the 3.5 ATR reachability horizon is relaxed and the 79600-79700 pool (17.21M) is targeted? Tests whether widening the horizon manufactures payable geometry.
- metrics: symbol=BTCUSD.pi, mid=81554.5, atr_14=244.7899, regime=BEARISH, entry=82044.0, sl=82685.0, tp=79959.93, lots=0.02, stop_points=641.0, risk_usd=12.82, reward_usd=41.68140000000014, rr_gross=3.2512792511700574, rr_min_required=2.0, entry_distance_atr=1.999674006157934, friction_pct=2.65210608424337, sl_clearance_atr=0.3472365485667505, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=43424134.73000001, overwhelm_ratio=0.5608719524622752, best_reachable_rr=1.9708268330733274, best_reachable_tp=80780.7, post_stop_equity_usd=4841.525000000001, min_lot_spread_cash_usd=0.17
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.347 ATR < 0.35 ATR outside the belt edge 82600.0
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82044.0 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.97R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.97R against the minimum compliant stop (641.7 points = clear the 82600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 79959.93 sits INSIDE the magnet pool [79900.0, 80000.0] carrying 4.715M USD instead of front-running it
  - Orderflow & Microstructure: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `eth_repair_short` — STAGE SHORT ETH
> ETH Model 2 short with a compliant bunker and a true front-run of the 42.27M USD 2400-2410 pool; tests whether ETH's 0.61R ceiling can be escaped with a deeper target.
- metrics: symbol=ETHUSD.pi, mid=2416.95, atr_14=11.1089, regime=BEARISH, entry=2439.0, sl=2534.0, tp=2411.81, lots=0.01, stop_points=95.0, risk_usd=0.9500000000000001, reward_usd=0.27190000000000053, rr_gross=0.28621052631579, rr_min_required=2.0, entry_distance_atr=1.984894994103843, friction_pct=3.263157894736842, sl_clearance_atr=0.36007165425919757, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=24818829.270000003, overwhelm_ratio=0.6918450581694177, best_reachable_rr=0.5960000000000036, best_reachable_tp=2382.3799999999997, post_stop_equity_usd=4856.3625, min_lot_spread_cash_usd=0.031000000000000003
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.279 exceeds 0.18
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 0.95 USD outside [7.5, 14.5]
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2439.0 sits inside un-swept purchase-side stop fuel [2420.0, 2530.0] = 17.970M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.60R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.60R against the minimum compliant stop (94.9 points = clear the 2530.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2411.81 sits INSIDE the magnet pool [2410.0, 2420.0] carrying 2.111M USD instead of front-running it
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.29R < 2.0R required for ETHUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sol_short_repair` — STAGE SHORT SOL
> SOL Model 2 short with the stop correctly outside the 105-115 belt and the TP front-running the 47.22M USD 100-101 pool; tests whether the recently-deleted ticket's thesis was salvageable at any size.
- metrics: symbol=SOLUSD.p, mid=104.525, atr_14=0.5263, regime=BEARISH, entry=105.58, sl=115.18, tp=101.08, lots=0.2, stop_points=9.600000000000009, risk_usd=192.0000000000002, reward_usd=90.0, rr_gross=0.4687499999999995, rr_min_required=2.0, entry_distance_atr=2.00456013680409, friction_pct=2.6041666666666643, sl_clearance_atr=0.3420102603078222, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=7741985.93, overwhelm_ratio=1.9838891802274305, best_reachable_rr=0.25802083333333353, best_reachable_tp=103.103, post_stop_equity_usd=4617.55, min_lot_spread_cash_usd=0.25
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.475 exceeds 0.18
- FATAL `ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.00 ATR from mid (>2.0 ATR bound)
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 192.00 USD outside [7.5, 14.5]
- FATAL `SL_BUFFER_THIN` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — SL clearance 0.342 ATR < 0.35 ATR outside the belt edge 115.0
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.58 sits inside un-swept purchase-side stop fuel [105.0, 115.0] = 15.359M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 4.853M < 5.00M CRYPTO_ALT requirement
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.26R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.26R against the minimum compliant stop (9.6 points = clear the 115.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 101.08 sits INSIDE the magnet pool [101.0, 102.0] carrying 6.599M USD instead of front-running it
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.47R < 2.0R required for SOLUSD.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 7,667,371
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4617.550 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: ENTRY_TOO_FAR, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: ENTRY_TOO_FAR, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: ENTRY_TOO_FAR, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: ENTRY_TOO_FAR, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: ENTRY_TOO_FAR, SL_BUFFER_THIN, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD

### `sol_ticket_18925879_postmortem` — DELETE  SOL
> Confirms the desk's cancellation of ticket #18925879 (SELL LIMIT 0.10 @ 104.90 / SL 105.75 / TP 103.10) by auditing it on its last observable generation. A DELETE ruling is only certified if the probe shows at least one fatal gate failure.
- metrics: symbol=SOLUSD.p, mid=104.525, atr_14=0.5263, regime=BEARISH, entry=104.9, sl=105.75, tp=103.1, lots=0.1, stop_points=0.8499999999999943, risk_usd=8.499999999999943, reward_usd=18.000000000000114, rr_gross=2.117647058823557, entry_distance_atr=0.7125213756412693, friction_pct=29.411764705882547, sl_clearance_atr=-1.4250427512825385, hazard_union=[105.0, 115.0], hazard_union_usd=15359242.120000001, in_range_defense_usd=12842687.209999999, overwhelm_ratio=0.027771866912890426, best_reachable_rr=2.1141176470588507, best_reachable_tp=103.103, post_stop_equity_usd=4846.925, min_lot_spread_cash_usd=0.25, delete_justification=['FRICTION_BUDGET', 'SL_INSIDE_SWEEP', 'NO_PAYABLE_SETUP', 'TP_INSIDE_MAGNET', 'SPREAD_OVER_ATR', 'BUNKER_WALL_THIN', 'COUNTER_CVD'], probe_fatal=True
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.475 exceeds 0.18
- MINOR `PROBE_SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.475 exceeds 0.18
- MINOR `PROBE_FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.25 / stop distance 0.850 = 29.41% of risk, above the 15% dynamic friction ceiling
- MINOR [purchase-side] `PROBE_SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 105.75 sits INSIDE the purchase-side sweep belt [105.0, 115.0] carrying 15.359M USD
- MINOR [purchase-side] `PROBE_BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 2.484M < 5.00M CRYPTO_ALT requirement
- MINOR `PROBE_NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.17R against the minimum compliant stop (10.3 points = clear the 115.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MINOR `PROBE_TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 103.1 sits INSIDE the magnet pool [103.0, 104.0] carrying 3.277M USD instead of front-running it
- MINOR [purchase-side] `PROBE_COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 7,667,371
- probe MAJOR `SPREAD_OVER_ATR` (A7) — spread/ATR 0.475 exceeds 0.18
- probe FATAL `FRICTION_BUDGET` (A7) — spread 0.25 / stop distance 0.850 = 29.41% of risk, above the 15% dynamic friction ceiling
- probe FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1) — SL 105.75 sits INSIDE the purchase-side sweep belt [105.0, 115.0] carrying 15.359M USD
- probe MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4) — largest in-range wall 2.484M < 5.00M CRYPTO_ALT requirement
- probe FATAL `NO_PAYABLE_SETUP` (A6) — asset-level verdict: the best front-runnable target pays 0.17R against the minimum compliant stop (10.3 points = clear the 115.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- probe FATAL `TP_INSIDE_MAGNET` (A6) — TP 103.1 sits INSIDE the magnet pool [103.0, 104.0] carrying 3.277M USD instead of front-running it
- probe MAJOR [purchase-side] `COUNTER_CVD` (A2) — short against positive session CVD 7,667,371
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 73.8/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 70.19/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 59.4/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 66.6/100 — no fatal flaw found

### `ger40_engine1_meanreversion` — STAGE LONG GER40
> GER40 is the only asset in the matrix with |Z| >= 2.0 (Z = -2.14), so it is the sole Engine 1 trigger on the board. Mean reversion from an extreme statistical dislocation is a LONG here; this card tests it against the trend-first hierarchy, the whale-backing requirement and the absence of any magnet.
- metrics: symbol=GER40.p, mid=25204.9, atr_14=26.9285, regime=BEARISH, entry=25204.9, sl=25150.0, tp=25300.0, lots=0.01, stop_points=54.900000000001455, risk_usd=5.490000000000146, reward_usd=9.509999999999854, rr_gross=1.7322404371583973, rr_min_required=2.0, entry_distance_atr=0.0, friction_pct=5.646630236794022, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4850.6875, min_lot_spread_cash_usd=0.31
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 5.49 USD outside [7.5, 14.5]
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.73R < 2.0R required for GER40.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 42.5/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Structural Price Action: 42.5/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 42.94/100 — fatal: NO_MAGNETS, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_MAGNETS, COUNTER_TREND

### `near_short_friction_probe` — STAGE SHORT NEAR
> NEAR screens as the highest raw R:R on the book (2.78R) but is on the operator's banned list at 62% friction. This card exists to prove the ban arithmetically rather than by assertion.
- metrics: symbol=NERUSD.p, mid=4.8715, atr_14=0.0448, regime=BEARISH, entry=4.96, sl=5.036, tp=4.7508, lots=1.0, stop_points=0.07599999999999962, risk_usd=7.599999999999962, reward_usd=20.920000000000005, rr_gross=2.752631578947383, rr_min_required=2.0, entry_distance_atr=1.9754464285714242, friction_pct=43.421052631579165, sl_clearance_atr=0.3571428571428575, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=3.227500000000025, best_reachable_tp=4.714709999999999, post_stop_equity_usd=4848.05, min_lot_spread_cash_usd=3.3000000000000003
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 67.74 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.737 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.30 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.033 / stop distance 0.076 = 43.42% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.96 sits inside un-swept purchase-side stop fuel [4.87, 5.02] = 1.372M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 4.7508 sits INSIDE the magnet pool [4.75, 4.76] carrying 0.840M USD instead of front-running it
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `trx_long_bullish_regime` — STAGE LONG TRX
> TRX is one of only two BULLISH regimes on the board (with USWTI), so it is the only place a Model 2 long is even permitted. Tests whether the long side of the book offers anything today.
- metrics: symbol=TRXUSD.p, mid=0.3322, atr_14=0.0004, regime=BULLISH, entry=0.3322, sl=0.329, tp=0.336, lots=1.0, stop_points=0.0031999999999999806, risk_usd=31.999999999999808, reward_usd=38.000000000000256, rr_gross=1.187500000000015, rr_min_required=2.0, entry_distance_atr=0.0, friction_pct=28.12500000000017, sl_clearance_atr=-7.500000000000006, hazard_union=[0.32, 0.332], hazard_union_usd=430327.3, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4817.55, min_lot_spread_cash_usd=9.0
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 2.250 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 9.00 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.0009 / stop distance 0.003 = 28.13% of risk, above the 15% dynamic friction ceiling
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 32.00 USD outside [7.5, 14.5]
- FATAL `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 0.329 sits INSIDE the sale-side sweep belt [0.32, 0.332] carrying 0.430M USD
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.19R < 2.0R required for TRXUSD.p
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS

### `sp500_core_short` — STAGE SHORT SP500
> SP500 is the desk's core index with the tightest friction (0.44 bps); tests whether the 18.4B USD stop-cluster belt above the entry can be survived at any target.
- metrics: symbol=SP500.p, mid=7703.32, atr_14=9.948, regime=BEARISH, entry=7723.22, sl=7813.5, tp=7655.74, lots=0.01, stop_points=90.27999999999975, risk_usd=9.027999999999976, reward_usd=6.748000000000047, rr_gross=0.7474523704031973, rr_min_required=2.0, entry_distance_atr=2.000402090872592, friction_pct=0.3766061143110334, sl_clearance_atr=0.3518295134700442, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=23149297.360000003, overwhelm_ratio=0.18862064373257503, best_reachable_rr=0.5045414266725877, best_reachable_tp=7677.669999999999, post_stop_equity_usd=4846.265, min_lot_spread_cash_usd=0.034
- FATAL `ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.00 ATR from mid (>2.0 ATR bound)
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7723.22 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 18418.087M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.50R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.50R against the minimum compliant stop (90.3 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 7655.74 sits INSIDE the magnet pool [7650.0, 7660.0] carrying 8.931M USD instead of front-running it
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.75R < 2.0R required for SP500.p
  - Orderflow & Microstructure: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: ENTRY_TOO_FAR, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `desk_batch_3x_max_risk` — STAGE_BATCH SHORT BTC
> Strawman: fill all three capacity tickets the briefing says are available, since the book is flat with 4/4 slots free and 64.55 USD of stress budget.
- metrics: symbol=BTCUSD.pi, mid=81554.5, atr_14=244.7899, regime=BEARISH, entry=82100.0, sl=82722.0, tp=80720.0, lots=0.01, stop_points=622.0, risk_usd=6.22, reward_usd=13.8, rr_gross=2.2186495176848875, rr_min_required=2.0, entry_distance_atr=2.22844161462544, friction_pct=2.7331189710610935, sl_clearance_atr=0.4983865755899243, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=36482974.49000001, overwhelm_ratio=0.6331594589780937, best_reachable_rr=2.1210610932475933, best_reachable_tp=80780.7, post_stop_equity_usd=4830.225, min_lot_spread_cash_usd=0.17
- FATAL `ENTRY_TOO_FAR` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — entry is 2.23 ATR from mid (>2.0 ATR bound)
- MAJOR `RISK_ENVELOPE` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — nominal risk 6.22 USD outside [7.5, 14.5]
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 82100.0 sits inside un-swept purchase-side stop fuel [81600.0, 82600.0] = 41.036M USD
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80720.0 sits INSIDE the magnet pool [80700.0, 80800.0] carrying 15.512M USD instead of front-running it
  - Orderflow & Microstructure: 55.74/100 — fatal: ENTRY_TOO_FAR, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: ENTRY_TOO_FAR, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: ENTRY_TOO_FAR, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: ENTRY_TOO_FAR, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: ENTRY_TOO_FAR, TP_INSIDE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_armed_post_sweep_short` — WATCH  BTC
> The correct BTC posture: do not fade 41M USD of intact squeeze fuel. Arm a post-sweep short - if price punches the 22.83M USD verified sell wall at 82,868 (persist 4512s) and closes back below 82,700, the belt is consumed and the short becomes payable against the 25.0M USD buy wall at 81,196.
- metrics: symbol=BTCUSD.pi, mid=81554.5, atr_14=244.7899, regime=BEARISH, min_lot_spread_cash_usd=0.17
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: BTCUSD.pi prints a 15m high >= 82880 AND closes back below 82700 while session CVD stays negative
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle109` — STAND_ASIDE
> No new ticket: Engine 1 triggers nowhere (the one |Z| >= 2.0 asset is counter-trend, unwalled and unmagnetised), Engine 2 geometry is unpayable on every asset (BTC ceiling 1.97R, ETH 0.61R, SOL 0.19R), and the SOL ticket's cancellation is confirmed correct.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 8 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
