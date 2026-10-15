# Arena tournament cycle113_20261015T003156Z

- snapshot: `/tmp/snap113.json` generation `92f847703ca744488026fec4ba7e6cd5` as_of `2026-10-15 00:31:56 UTC`
- cards: `docs/trade_plans/arena_cards/cycle113_20261015T003156Z.json` sha256 `f0d9cc122483ae89`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 113 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle113`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle113` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `btc_ladder_break_watch` | WATCH | no | - | 69.00 | advisory only |
| `eth_val_rejection_watch` | WATCH | no | - | 61.80 | advisory only |
| `desk_batch_4x_max_risk` | STAGE_BATCH | YES | - | 55.66 | CONTRADICTED |
| `eth_val_shelf_short` | STAGE | YES | - | 48.46 | CONTRADICTED |
| `btc_relief_rally_short` | STAGE | YES | SL_INSIDE_SWEEP, COUNTER_CVD | 48.45 | CONTRADICTED |
| `uswti_bullish_pullback_long` | STAGE | YES | - | 48.36 | CONTRADICTED |
| `btc_belt_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `eth_wall_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `eth_shelf_long` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `sol_belt_short` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `xrp_alt_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `sp500_long_variant` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `ltc_friction_short` | STAGE | YES | NO_BUNKER_WALL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `near_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 48.00 | CONTRADICTED |
| `silver_floor_probe` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO | 48.00 | CONTRADICTED |
| `nas100_extreme_probe` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `gold_range_gate_probe` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD | 48.00 | CONTRADICTED |

## Bracket
### Round 1
- `nas100_extreme_probe` (48.0, fatal=True) vs `btc_relief_rally_short` (48.45, fatal=True) -> **btc_relief_rally_short** — higher rubric total (48.45 vs 48.0)
- `silver_floor_probe` (48.0, fatal=True) vs `uswti_bullish_pullback_long` (48.36, fatal=True) -> **uswti_bullish_pullback_long** — higher rubric total (48.36 vs 48.0)
- `eth_val_shelf_short` (48.46, fatal=True) vs `ltc_friction_short` (48.0, fatal=True) -> **eth_val_shelf_short** — higher rubric total (48.46 vs 48.0)
- `gold_range_gate_probe` (48.0, fatal=True) vs `eth_shelf_long` (48.0, fatal=True) -> **gold_range_gate_probe** — exact tie: fewer standing attacks (deterministic order)
- `xrp_alt_long` (48.0, fatal=True) vs `eth_wall_short` (48.0, fatal=True) -> **xrp_alt_long** — exact tie: fewer standing attacks (deterministic order)
- `eth_val_rejection_watch` (61.8, fatal=False) vs `sp500_long_variant` (48.0, fatal=True) -> **eth_val_rejection_watch** — sp500_long_variant is contradicted by the snapshot; eth_val_rejection_watch is not
- `sol_belt_short` (48.0, fatal=True) vs `sp500_core_short` (48.0, fatal=True) -> **sol_belt_short** — exact tie: fewer standing attacks (deterministic order)
- `btc_ladder_break_watch` (69.0, fatal=False) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **btc_ladder_break_watch** — desk_batch_4x_max_risk is contradicted by the snapshot; btc_ladder_break_watch is not
- `desk_stand_aside_cycle113` (71.5, fatal=False) vs `near_friction_probe` (48.0, fatal=True) -> **desk_stand_aside_cycle113** — near_friction_probe is contradicted by the snapshot; desk_stand_aside_cycle113 is not
- bye: `btc_belt_long`
### Round 2
- `btc_relief_rally_short` (48.45, fatal=True) vs `uswti_bullish_pullback_long` (48.36, fatal=True) -> **btc_relief_rally_short** — higher rubric total (48.45 vs 48.36)
- `eth_val_shelf_short` (48.46, fatal=True) vs `gold_range_gate_probe` (48.0, fatal=True) -> **eth_val_shelf_short** — higher rubric total (48.46 vs 48.0)
- `xrp_alt_long` (48.0, fatal=True) vs `eth_val_rejection_watch` (61.8, fatal=False) -> **eth_val_rejection_watch** — xrp_alt_long is contradicted by the snapshot; eth_val_rejection_watch is not
- `sol_belt_short` (48.0, fatal=True) vs `btc_ladder_break_watch` (69.0, fatal=False) -> **btc_ladder_break_watch** — sol_belt_short is contradicted by the snapshot; btc_ladder_break_watch is not
- `desk_stand_aside_cycle113` (71.5, fatal=False) vs `btc_belt_long` (48.0, fatal=True) -> **desk_stand_aside_cycle113** — btc_belt_long is contradicted by the snapshot; desk_stand_aside_cycle113 is not
### Round 3
- `btc_relief_rally_short` (48.45, fatal=True) vs `eth_val_shelf_short` (48.46, fatal=True) -> **eth_val_shelf_short** — higher rubric total (48.46 vs 48.45)
- `eth_val_rejection_watch` (61.8, fatal=False) vs `btc_ladder_break_watch` (69.0, fatal=False) -> **btc_ladder_break_watch** — higher rubric total (69.0 vs 61.8)
- bye: `desk_stand_aside_cycle113`
### Round 4
- `eth_val_shelf_short` (48.46, fatal=True) vs `btc_ladder_break_watch` (69.0, fatal=False) -> **btc_ladder_break_watch** — eth_val_shelf_short is contradicted by the snapshot; btc_ladder_break_watch is not
- bye: `desk_stand_aside_cycle113`
### Round 5
- `btc_ladder_break_watch` (69.0, fatal=False) vs `desk_stand_aside_cycle113` (71.5, fatal=False) -> **desk_stand_aside_cycle113** — higher rubric total (71.5 vs 69.0)

## Findings per card
### `btc_belt_long` — STAGE LONG BTC
> Best legal long geometry in the book (0.87R gross): price has reclaimed the EMA20 81,625 and the target is the front-run of the [81,800-82,800] purchase lane ($32.24M), but mid sits INSIDE the $130.68M sell-stop/cascade lane [80,700-81,800] below (price-inside-ladder) and a Model-1 long is banned in a BEARISH HTF.
- metrics: symbol=BTCUSD.pi, mid=81676.0, atr_14=235.7105, regime=BEARISH, entry=81216.364525, sl=80616.3227725, tp=81738.65, lots=0.02, stop_points=600.0417524999939, risk_usd=12.000835049999878, reward_usd=10.44570949999994, rr_gross=0.870415221647434, rr_min_required=2.0, entry_distance_atr=1.9500000000000117, friction_pct=2.666481112912249, sl_clearance_atr=0.3549999999999858, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=100277716.31999998, overwhelm_ratio=0.7690371617948311, best_reachable_rr=0.8363342599230292, best_reachable_tp=81718.2, post_stop_equity_usd=4842.5489561875, min_lot_spread_cash_usd=0.16
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81216.364525 sits inside un-swept sale-side stop fuel [80700.0, 81800.0] = 110.676M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.84R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.84R against the minimum compliant stop (598.9 points = clear the 80700.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.87R < 2.0R required for BTCUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `eth_wall_short` — STAGE SHORT ETH
> Continuation short at the 2,442.0 ask wall ($8.15M/905s) with the EMA50 2,435 overhead; the exit lane below is the merged [2,300-2,420] structure ($320.44M; the [2,400-2,410] bucket is now a legitimate $36.28M, the $1.65B phantom did not recur) whose near edge sits only 0.23 ATR under mid, while the compliant stop is ~119 pts (12 ATR).
- metrics: symbol=ETHUSD.pi, mid=2424.15, atr_14=9.9609, regime=BEARISH, entry=2443.573755, sl=2553.5361195, tp=2421.815, lots=0.1, stop_points=109.96236450000015, risk_usd=10.996236450000016, reward_usd=2.1758754999999836, rr_gross=0.19787456461978686, rr_min_required=2.2, entry_distance_atr=1.94999999999998, friction_pct=3.001026774028668, sl_clearance_atr=0.3550000000000041, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=30976662.51, overwhelm_ratio=0.6009133467490523, best_reachable_rr=0.19237268220073828, best_reachable_tp=2422.4199999999996, post_stop_equity_usd=4843.8047044375, min_lot_spread_cash_usd=0.033
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.331 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2443.573755 sits inside un-swept purchase-side stop fuel [2430.0, 2550.0] = 20.637M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.19R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.19R against the minimum compliant stop (109.9 points = clear the 2550.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.20R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `eth_shelf_long` — STAGE LONG ETH
> Bullish-reversion attempt from below the EMA20; the $1.9B cascade structure under price and the BEARISH stack cap the ceiling at 0.22R.
- metrics: symbol=ETHUSD.pi, mid=2424.15, atr_14=9.9609, regime=BEARISH, entry=2404.7262450000003, sl=2296.4638805, tp=2428.1775, lots=0.1, stop_points=108.26236450000033, risk_usd=10.826236450000033, reward_usd=2.3451254999999493, rr_gross=0.21661502691454168, rr_min_required=2.2, entry_distance_atr=1.94999999999998, friction_pct=3.0481506802855667, sl_clearance_atr=0.3550000000000041, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=32143745.790000003, overwhelm_ratio=7.796957712936168, best_reachable_rr=0.39555532707767305, best_reachable_tp=2447.55, post_stop_equity_usd=4844.0172044375, min_lot_spread_cash_usd=0.033
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.331 exceeds 0.18
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2404.7262450000003 sits inside un-swept sale-side stop fuel [2300.0, 2430.0] = 251.808M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 250.623M exceeds in-range verified defense 32.144M by 7.80:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.40R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.40R against the minimum compliant stop (108.2 points = clear the 2300.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.22R < 2.2R required for ETHUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -2,078,147
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `sol_belt_short` — STAGE SHORT SOL
> SOL mid 104.45 is inside the buy-stop belt [104,105]-adjacent structure with a $106M cascade stack below; compliant stop 9 ATR wide.
- metrics: symbol=SOLUSD.p, mid=104.45, atr_14=0.4743, regime=BEARISH, entry=105.374885, sl=114.1683765, tp=104.078, lots=0.01, stop_points=8.793491499999988, risk_usd=8.793491499999988, reward_usd=1.2968850000000032, rr_gross=0.14748237375336123, rr_min_required=2.5, entry_distance_atr=1.9500000000000068, friction_pct=2.501850374222802, sl_clearance_atr=0.3549999999999867, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=10299467.72, overwhelm_ratio=1.6130801524566554, best_reachable_rr=0.14452564149291813, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.558135625, min_lot_spread_cash_usd=0.22
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.464 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.374885 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 16.681M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.14R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.14R against the minimum compliant stop (8.8 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.15R < 2.5R required for SOLUSD.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 673,394
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `xrp_alt_long` — STAGE LONG XRP
> Counter-trend long with min-lot risk 103.39 USD; the [1.30,1.31] bin is excluded as untrusted (>10x) and there are zero eligible walls on this asset.
- metrics: symbol=XRPUSD.pi, mid=1.332, atr_14=0.0054, regime=BEARISH, entry=1.3214700000000001, sl=1.218083, tp=1.3489875, lots=1.0, stop_points=0.10338700000000012, risk_usd=103.38700000000011, reward_usd=27.517499999999863, rr_gross=0.26616015553212524, rr_min_required=2.0, entry_distance_atr=1.9499999999999866, friction_pct=3.868958379680226, sl_clearance_atr=0.3549999999999901, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=0.2628957218992712, best_reachable_tp=1.3486500000000001, post_stop_equity_usd=4728.31625, min_lot_spread_cash_usd=4.0
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.741 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 4.00 USD, above 2.175 USD (15% of max risk)
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 1.3214700000000001 sits inside un-swept sale-side stop fuel [1.22, 1.33] = 33.153M USD
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.26R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.26R against the minimum compliant stop (0.1 points = clear the 1.22 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.27R < 2.0R required for XRPUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4728.316 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH

### `sp500_core_short` — STAGE SHORT SP500
> 0.44 bps spread, but the compliant stop is 92 pts while the best reachable reward is 33 pts (0.38R); the $38.33M bid wall at 7,682 sits exactly where the target must print.
- metrics: symbol=SP500.p, mid=7703.09, atr_14=9.23, regime=BEARISH, entry=7721.0885, sl=7813.27665, tp=7685.76, lots=0.01, stop_points=92.18814999999995, risk_usd=9.218814999999996, reward_usd=3.532849999999962, rr_gross=0.3832217047418745, rr_min_required=2.0, entry_distance_atr=1.9499999999999669, friction_pct=0.36881095889222226, sl_clearance_atr=0.3549999999999773, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=22222045.900000002, overwhelm_ratio=0.2801531811254156, best_reachable_rr=0.3623947329456169, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4846.02648125, min_lot_spread_cash_usd=0.034
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7721.0885 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 6.379M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.36R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.36R against the minimum compliant stop (92.1 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.38R < 2.0R required for SP500.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 39
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `sp500_long_variant` — STAGE LONG SP500
> Mirror geometry of the same wall: 0.33R ceiling with the stop below the 7,682 defence.
- metrics: symbol=SP500.p, mid=7703.09, atr_14=9.23, regime=BEARISH, entry=7685.0915, sl=7596.72335, tp=7714.21, lots=0.01, stop_points=88.36815000000024, risk_usd=8.836815000000025, reward_usd=2.9118499999999585, rr_gross=0.32951351816236396, rr_min_required=2.0, entry_distance_atr=1.9499999999999669, friction_pct=0.38475400922164726, sl_clearance_atr=0.3549999999999773, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=11963614.990000002, overwhelm_ratio=3.5035472417856526, best_reachable_rr=0.3076730699918378, best_reachable_tp=7712.28, post_stop_equity_usd=4846.50398125, min_lot_spread_cash_usd=0.034
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7685.0915 sits inside un-swept sale-side stop fuel [7600.0, 7700.0] = 41.941M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 41.915M exceeds in-range verified defense 11.964M by 3.50:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.31R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.31R against the minimum compliant stop (88.3 points = clear the 7600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.33R < 2.0R required for SP500.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `ltc_friction_short` — STAGE SHORT LTC
> Gross 0.53R at 18.00% friction - above the 15% rule - with zero eligible walls on the book; LTC is a friction-class asset this generation.
- metrics: symbol=LTCUSD.pi, mid=59.35, atr_14=0.2406, regime=BEARISH, entry=59.81917, sl=61.485413, tp=58.944175, lots=0.1, stop_points=1.6662430000000015, risk_usd=16.662430000000015, reward_usd=8.749949999999984, rr_gross=0.5251304881700914, rr_min_required=2.0, entry_distance_atr=1.9499999999999929, friction_pct=18.004576763413244, sl_clearance_atr=0.3550000000000109, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=0.5162932417420546, best_reachable_tp=58.95889999999999, post_stop_equity_usd=4836.7219625, min_lot_spread_cash_usd=3.0
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 50.55 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 1.247 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (0.1 lot) is 3.00 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.3 / stop distance 1.666 = 18.00% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.52R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.52R against the minimum compliant stop (1.7 points = clear the 61.4 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.53R < 2.0R required for LTCUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 14,170
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD

### `near_friction_probe` — STAGE SHORT NEAR
> Gross 1.06R at 25.21% friction; NEAR is on the banned-instrument list.
- metrics: symbol=NERUSD.p, mid=4.828, atr_14=0.0408, regime=BEARISH, entry=4.90756, sl=5.034484, tp=4.7735775, lots=1.0, stop_points=0.12692399999999981, risk_usd=12.692399999999981, reward_usd=13.398250000000012, rr_gross=1.0556120197913736, rr_min_required=2.0, entry_distance_atr=1.9499999999999962, friction_pct=25.21193785257323, sl_clearance_atr=0.3550000000000094, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=1.0462166335760066, best_reachable_tp=4.774769999999999, post_stop_equity_usd=4841.6845, min_lot_spread_cash_usd=3.2
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 66.28 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.784 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.20 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.032 / stop distance 0.127 = 25.21% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.90756 sits inside un-swept purchase-side stop fuel [4.83, 5.02] = 1.488M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.05R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.05R against the minimum compliant stop (0.1 points = clear the 5.02 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.06R < 2.0R required for NERUSD.p
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `silver_floor_probe` — STAGE SHORT SILVER
> 1.44R ceiling but min-lot risk 37.67 USD at the compliant stop (x2.6 the envelope) and the best commodity-class wall is only $0.29M against the $0.75M shield.
- metrics: symbol=XAGUSD.pi, mid=56.073, atr_14=0.2342, regime=BEARISH, entry=56.52969, sl=57.283141, tp=55.44155, lots=0.01, stop_points=0.7534509999999983, risk_usd=37.672549999999916, reward_usd=54.40700000000014, rr_gross=1.4442080506894346, rr_min_required=2.0, entry_distance_atr=1.9500000000000077, friction_pct=4.77801476141117, sl_clearance_atr=0.35499999999999016, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=395999.14, overwhelm_ratio=2.0859422826019265, best_reachable_rr=1.6915366759085992, best_reachable_tp=55.255199999999995, post_stop_equity_usd=4810.4593125, min_lot_spread_cash_usd=1.8
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 6.42 bps exceeds the 5 bps COMMODITY ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 56.52969 sits inside un-swept purchase-side stop fuel [56.1, 57.2] = 0.878M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.198M < 0.75M COMMODITY requirement
- FATAL [purchase-side] `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 0.826M exceeds in-range verified defense 0.396M by 2.09:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.69R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.69R against the minimum compliant stop (0.8 points = clear the 57.2 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.44R < 2.0R required for XAGUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, OVERWHELM_RATIO

### `nas100_extreme_probe` — STAGE SHORT NAS100
> Deepest RSI dislocation in the book (31.4, BEARISH stack 29,838 < 30,031 < 30,393) but the compliant stop is ~1,043 pts (104.30 USD at min lot) and the 29,807 ask wall is only $1.99M/184s with $1.62M/303s bid support - BUNKER_WALL_THIN.
- metrics: symbol=NAS100.p, mid=29757.7, atr_14=62.2389, regime=BEARISH, entry=29879.065855, sl=30922.0948095, tp=29722.275, lots=0.01, stop_points=1043.0289544999978, risk_usd=104.30289544999978, reward_usd=15.679085499999928, rr_gross=0.15032262941843347, rr_min_required=2.0, entry_distance_atr=1.9500000000000002, friction_pct=0.11696703094736596, sl_clearance_atr=0.35499999999997617, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=7370211.3900000015, overwhelm_ratio=0.5221763768162421, best_reachable_rr=0.14320393921528854, best_reachable_tp=29729.699999999997, post_stop_equity_usd=4727.1713806875005, min_lot_spread_cash_usd=0.122
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 29879.065855 sits inside un-swept purchase-side stop fuel [29800.0, 30900.0] = 3.849M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.14R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.14R against the minimum compliant stop (1042.7 points = clear the 30900.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.15R < 2.0R required for NAS100.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 5
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4727.171 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `btc_relief_rally_short` — STAGE SHORT BTC
> Astra CP-113 hypothesis re-derived on the newest generation: genuine relief flow to the EMA20 81,625 shelf with taker-buy 0.71 and 30m CVD +4.64M, but the entry sits inside its own target ladder and the compliant stop must clear the [81,700-82,600] purchase belt.
- metrics: symbol=BTCUSD.pi, mid=81676.0, atr_14=235.7105, regime=BEARISH, entry=81740.0, sl=82530.0, tp=80950.0, lots=0.01, stop_points=790.0, risk_usd=7.9, reward_usd=7.9, rr_gross=1.0, rr_min_required=2.0, entry_distance_atr=0.2715195122830761, friction_pct=2.0253164556962027, sl_clearance_atr=-1.1454729424442271, hazard_union=[81800.0, 82800.0], hazard_union_usd=32236773.479999997, in_range_defense_usd=97699955.83000006, overwhelm_ratio=0.2996162787518016, post_stop_equity_usd=4847.675, min_lot_spread_cash_usd=0.16
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 82530.0 sits INSIDE the purchase-side sweep belt [81800.0, 82800.0] carrying 32.237M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 81676.0 sits inside the sell-stop/long-cascade ladder [80700.0, 81800.0] carrying 130.713M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (81676.0) to front-run; nearest qualifying pool is 80200.0-80300.0 USD 5.50 ATR from mid
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80950.0 sits INSIDE the magnet pool [80900.0, 81000.0] carrying 25.623M USD instead of front-running it
- MAJOR `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 1.00R < 2.0R required for BTCUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 5,203,408
  - Orderflow & Microstructure: 50.23/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, COUNTER_CVD

### `eth_val_shelf_short` — STAGE SHORT ETH
> Astra's ETH VAL-shelf ticket skeleton, tested verbatim (entry 2,434.65 inside the 2,426.6-2,442.7 zone, SL 2,464.35, TP 2,395.2). The engine's compliant-stop walk returns ~119 pts (12 ATR) because the [2,400-2,410] and [2,450-2,460] belts overlap the shelf, collapsing the ceiling to ~0.10R.
- metrics: symbol=ETHUSD.pi, mid=2424.15, atr_14=9.9609, regime=BEARISH, min_lot_spread_cash_usd=0.033
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.331 exceeds 0.18
- FATAL `CARD_INCOMPLETE` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — trade card is missing entry/SL/TP/lots
  - Orderflow & Microstructure: 57.1/100 — fatal: CARD_INCOMPLETE
  - Structural Price Action: 46.29/100 — fatal: CARD_INCOMPLETE
  - Liquidation & Stop Forensic: 46.29/100 — fatal: CARD_INCOMPLETE
  - Macro Risk & Portfolio Governor: 42.7/100 — fatal: CARD_INCOMPLETE
  - Adversarial Pre-Mortem Red Team: 49.9/100 — fatal: CARD_INCOMPLETE

### `uswti_bullish_pullback_long` — STAGE LONG USWTI
> The only BULLISH regime with a usable book: pullback into the weekly VWAP 93.85 / prior-day POC 94.29 shelf, but the best commodity-class wall is $0.31M against the $0.75M shield and stop-belt geometry fails SL_INSIDE_SWEEP.
- metrics: symbol=USWTI.p, mid=94.546, atr_14=0.2168, regime=BULLISH, entry=94.481, sl=93.0, tp=95.0, lots=0.07, stop_points=1.4809999999999945, risk_usd=10.366999999999964, reward_usd=3.6330000000000386, rr_gross=0.350438892640113, rr_min_required=2.0, entry_distance_atr=0.2998154981550366, friction_pct=3.10600945307226, sl_clearance_atr=-1.8450184501845281, hazard_union=[91.8, 93.4], hazard_union_usd=3948984.5000000005, in_range_defense_usd=2927781.6599999997, overwhelm_ratio=1.0653410644016401, post_stop_equity_usd=4844.59125, min_lot_spread_cash_usd=0.046
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.212 exceeds 0.18
- FATAL `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 93.0 sits INSIDE the sale-side sweep belt [91.8, 93.4] carrying 3.949M USD
- MAJOR `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.315M < 0.75M COMMODITY requirement
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.35R < 2.0R required for USWTI.p
  - Orderflow & Microstructure: 49.8/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Structural Price Action: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: SL_INSIDE_SWEEP, NO_MAGNETS, RR_BELOW_MIN

### `gold_range_gate_probe` — STAGE SHORT GOLD
> GOLD flipped to RANGE_BOUND on this generation (was BEARISH) with RSI 75.18 - the regime gate must strike the card down before geometry, and the commodity wall shield fails anyway ($0.61M < $0.75M).
- metrics: symbol=XAUUSD.pi, mid=4141.74, atr_14=8.0394, regime=RANGE_BOUND, entry=4145.76, sl=4150.58, tp=4133.7, lots=0.02, stop_points=4.819999999999709, risk_usd=9.639999999999418, reward_usd=24.1200000000008, rr_gross=2.5020746887969145, rr_min_required=2.0, entry_distance_atr=0.5000373162176824, friction_pct=2.489626556016748, sl_clearance_atr=-1.316018608353848, hazard_union=[4140.0, 4260.0], hazard_union_usd=1982648.27, in_range_defense_usd=526906.92, overwhelm_ratio=0.7104272230852462, post_stop_equity_usd=4845.500000000001, min_lot_spread_cash_usd=0.12
- FATAL `REGIME_GATED_STAND_ASIDE` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime=RANGE_BOUND: neither engine applies in non-trending noise
- MINOR `MAGNET_UNTRUSTED_EXCLUDED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — 1 bin(s) excluded as untrusted (> 10x the larger neighbour); largest [3980.0, 3990.0] carrying 10.123M USD cannot anchor a TP
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 4150.58 sits INSIDE the purchase-side sweep belt [4140.0, 4260.0] carrying 1.983M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4145.76 sits inside un-swept purchase-side stop fuel [4140.0, 4260.0] = 1.983M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.333M < 0.75M COMMODITY requirement
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (4141.74) to front-run; nearest qualifying pool is 4050.0-4080.0 USD 7.17 ATR from mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 4133.7 is 131.62 bps from the governing magnet edge 4080.0; desk doctrine is a 5-10 bps front-run
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 51
  - Orderflow & Microstructure: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_REACHABLE_MAGNET | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD

### `desk_batch_4x_max_risk` — STAGE_BATCH SHORT BTC
> Capacity strawman: four max-envelope tickets (4 x 20.12 = 80.48 stress) against the 64.55 USD budget. Included so the bracket contains the boundary case the governor computes by hand; the ceiling is three tickets (60.36).
- metrics: symbol=BTCUSD.pi, mid=81676.0, atr_14=235.7105, regime=BEARISH, min_lot_spread_cash_usd=0.16
- FATAL `CARD_INCOMPLETE` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — trade card is missing entry/SL/TP/lots
  - Orderflow & Microstructure: 64.3/100 — fatal: CARD_INCOMPLETE
  - Structural Price Action: 49.9/100 — fatal: CARD_INCOMPLETE
  - Liquidation & Stop Forensic: 49.9/100 — fatal: CARD_INCOMPLETE
  - Macro Risk & Portfolio Governor: 57.1/100 — fatal: CARD_INCOMPLETE
  - Adversarial Pre-Mortem Red Team: 57.1/100 — fatal: CARD_INCOMPLETE

### `eth_val_rejection_watch` — WATCH None ETH
> Peer-audit watch (Astra): ETH is APPROACHING the VAL shelf with a full ticket skeleton on file. Gates remain 0/4 - arrival alone does not arm the trade; the desk requires a >= 0.5 ATR rejection wick plus a symmetrical-wall confirmation before staging.
- metrics: symbol=ETHUSD.pi, mid=2424.15, atr_14=9.9609, regime=BEARISH, min_lot_spread_cash_usd=0.033
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.331 exceeds 0.18
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: arrival at the 2,424.0-2,442.7 shelf AND >= 0.5 ATR rejection wick AND >= 2.0R geometry at the compliant stop (currently 0.10R)
  - Orderflow & Microstructure: 61.8/100 — no fatal flaw found
  - Structural Price Action: 65.39/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 65.39/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 54.6/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 61.8/100 — no fatal flaw found

### `btc_ladder_break_watch` — WATCH None BTC
> BTC is coiling between the $98M buy-stop/cascade stack below (81,000-81,700) and the 81,700-82,600 purchase belt above. A decisive loss of 81,000 opens the 80,600-80,900 pool; a reclaim of 82,838 re-arms the sellers' bunker.
- metrics: symbol=BTCUSD.pi, mid=81676.0, atr_14=235.7105, regime=BEARISH, min_lot_spread_cash_usd=0.16
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: 15m close < 81,000 with session CVD < 0 and the 81,196 bid wall ($25.0M) thinning
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle113` — STAND_ASIDE
> Session VWAP is NULL on all 24 assets this generation (bridge reset at 00:00 UTC, session_bars = 0), so Engine 1 is structurally dark and Engine 2 fails on every asset for exit-leg or affordability reasons. Re-proves itself by re-running each member card.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 15 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
