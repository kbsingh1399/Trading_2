# Arena tournament cycle111_20261014T233635Z

- snapshot: `/tmp/snap111e.json` generation `92182f87cfd347e79d2e5e20c1f8689b` as_of `2026-10-14 23:36:35 UTC`
- cards: `docs/trade_plans/arena_cards/cycle111_20261014T233635Z.json` sha256 `33269ffc6fcd2e47`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 111 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle111`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle111` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `btc_armed_post_ladder_short` | WATCH | no | - | 69.00 | advisory only |
| `desk_batch_4x_max_risk` | STAGE_BATCH | YES | - | 55.66 | CONTRADICTED |
| `ger40_empty_book_probe` | STAGE | YES | NO_BUNKER_WALL, COUNTER_CVD | 52.72 | CONTRADICTED |
| `near_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 51.39 | CONTRADICTED |
| `btc_straddle_ladder_short` | STAGE | YES | ENTRY_IN_FUEL | 50.10 | CONTRADICTED |
| `btc_ladder_top_long` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `eth_shelf_long` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `sol_repair_short` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD | 48.00 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `nas100_momentum_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `gold_minlot_floor_probe` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `usdjpy_quote_currency_probe` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `eth_shelf_short` | STAGE | YES | ENTRY_IN_FUEL | 42.58 | CONTRADICTED |
| `eurusd_range_gate_probe` | STAGE | YES | NO_BUNKER_WALL, COUNTER_CVD | 42.50 | CONTRADICTED |

## Bracket
### Round 1
- `ger40_empty_book_probe` (52.72, fatal=True) vs `sol_repair_short` (48.0, fatal=True) -> **ger40_empty_book_probe** — higher rubric total (52.72 vs 48.0)
- `btc_straddle_ladder_short` (50.1, fatal=True) vs `near_friction_probe` (51.39, fatal=True) -> **near_friction_probe** — higher rubric total (51.39 vs 50.1)
- `eurusd_range_gate_probe` (42.5, fatal=True) vs `btc_ladder_top_long` (48.0, fatal=True) -> **btc_ladder_top_long** — higher rubric total (48.0 vs 42.5)
- `desk_batch_4x_max_risk` (55.66, fatal=True) vs `eth_shelf_short` (42.58, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 42.58)
- `usdjpy_quote_currency_probe` (48.0, fatal=True) vs `nas100_momentum_short` (48.0, fatal=True) -> **usdjpy_quote_currency_probe** — exact tie: fewer standing attacks (deterministic order)
- `desk_stand_aside_cycle111` (71.5, fatal=False) vs `gold_minlot_floor_probe` (48.0, fatal=True) -> **desk_stand_aside_cycle111** — gold_minlot_floor_probe is contradicted by the snapshot; desk_stand_aside_cycle111 is not
- `sp500_core_short` (48.0, fatal=True) vs `eth_shelf_long` (48.0, fatal=True) -> **sp500_core_short** — exact tie: fewer standing attacks (deterministic order)
- bye: `btc_armed_post_ladder_short`
### Round 2
- `ger40_empty_book_probe` (52.72, fatal=True) vs `near_friction_probe` (51.39, fatal=True) -> **ger40_empty_book_probe** — higher rubric total (52.72 vs 51.39)
- `btc_ladder_top_long` (48.0, fatal=True) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 48.0)
- `usdjpy_quote_currency_probe` (48.0, fatal=True) vs `desk_stand_aside_cycle111` (71.5, fatal=False) -> **desk_stand_aside_cycle111** — usdjpy_quote_currency_probe is contradicted by the snapshot; desk_stand_aside_cycle111 is not
- `sp500_core_short` (48.0, fatal=True) vs `btc_armed_post_ladder_short` (69.0, fatal=False) -> **btc_armed_post_ladder_short** — sp500_core_short is contradicted by the snapshot; btc_armed_post_ladder_short is not
### Round 3
- `ger40_empty_book_probe` (52.72, fatal=True) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 52.72)
- `desk_stand_aside_cycle111` (71.5, fatal=False) vs `btc_armed_post_ladder_short` (69.0, fatal=False) -> **desk_stand_aside_cycle111** — higher rubric total (71.5 vs 69.0)
### Round 4
- `desk_batch_4x_max_risk` (55.66, fatal=True) vs `desk_stand_aside_cycle111` (71.5, fatal=False) -> **desk_stand_aside_cycle111** — desk_batch_4x_max_risk is contradicted by the snapshot; desk_stand_aside_cycle111 is not

## Findings per card
### `btc_straddle_ladder_short` — STAGE SHORT BTC
> Engine 2 short at the perimeter. Mid 81,453 sits INSIDE the $79.08M sell-stop ladder [80,500-81,500], so no front-runnable exit exists below; the nearest front-runnable pool (79,800-80,100, +$31.65M) is 5.1 ATR away against a 3.5-ATR horizon. Stop must clear the $30.37M buy-stop belt [81,500-82,600].
- metrics: symbol=BTCUSD.pi, mid=81453.0, atr_14=249.2923, regime=BEARISH, entry=81939.12, sl=82689.75, tp=80180.1, lots=0.01, stop_points=750.6300000000047, risk_usd=7.506300000000047, reward_usd=17.590199999999896, rr_gross=2.34339155109705, rr_min_required=2.0, entry_distance_atr=1.9500000601703114, friction_pct=2.1315428373499463, sl_clearance_atr=0.3600191421877049, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=34719343.309999995, overwhelm_ratio=0.442033031355742, post_stop_equity_usd=4848.167125, min_lot_spread_cash_usd=0.16
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81939.12 sits inside un-swept purchase-side stop fuel [81500.0, 82600.0] = 35.153M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 81453.0 sits inside the sell-stop/long-cascade ladder [80400.0, 81500.0] carrying 134.847M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (81453.0) to front-run; nearest qualifying pool is 80200.0-80300.0 USD 4.30 ATR from mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 80180.1 is 10.00 bps from the governing magnet edge 80100.0; desk doctrine is a 5-10 bps front-run
  - Orderflow & Microstructure: 57.16/100 — fatal: NO_REACHABLE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 43.42/100 — fatal: NO_REACHABLE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_REACHABLE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 55.77/100 — fatal: NO_REACHABLE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 51.63/100 — fatal: NO_REACHABLE_MAGNET | purchase-side sweep hazard: ENTRY_IN_FUEL

### `btc_ladder_top_long` — STAGE LONG BTC
> Mirror probe: an Engine 1 long fade is banned outright in a verified BEARISH HTF regime (archetype 2), and the $106.99M in-range fuel below mid overwhelms the $37.27M verified defence 3.74:1.
- metrics: symbol=BTCUSD.pi, mid=81453.0, atr_14=249.2923, regime=BEARISH, entry=80966.88, sl=79311.5, tp=81438.88, lots=0.01, stop_points=1655.3800000000047, risk_usd=16.553800000000045, reward_usd=4.72, rr_gross=0.2851309064988091, rr_min_required=2.0, entry_distance_atr=1.9500000601703114, friction_pct=0.9665454457586751, sl_clearance_atr=0.3550049480068177, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=50298796.59, overwhelm_ratio=2.7714253737775163, best_reachable_rr=0.2728195338834552, best_reachable_tp=81418.5, post_stop_equity_usd=4836.85775, min_lot_spread_cash_usd=0.16
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 80966.88 sits inside un-swept sale-side stop fuel [80400.0, 81500.0] = 107.026M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 139.399M exceeds in-range verified defense 50.299M by 2.77:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.27R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.27R against the minimum compliant stop (1654.1 points = clear the 79400.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.29R < 2.0R required for BTCUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -107,058,007
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `eth_shelf_short` — STAGE SHORT ETH
> Engine 2 shelf short. The [2,310-2,420] sell-stop ladder carries $1,711.24M and contains mid 2,414.65; the ceiling on this asset is <=0.6R against a 2.20R mandate. A 0.35-ATR stop under the belt edge is impossible — the belt is the tape.
- metrics: symbol=ETHUSD.pi, mid=2414.65, atr_14=10.6426, regime=BEARISH, entry=2435.4, sl=2533.83, tp=2422.42, lots=0.11, stop_points=98.42999999999984, risk_usd=10.827299999999981, reward_usd=1.427800000000002, rr_gross=0.13187036472620176, rr_min_required=2.2, entry_distance_atr=1.949711536654577, friction_pct=2.9462562226963374, sl_clearance_atr=0.3598744667656331, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=39487692.150000006, overwhelm_ratio=0.41196908465059534, post_stop_equity_usd=4844.015875, min_lot_spread_cash_usd=0.028999999999999998
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.272 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2435.4 sits inside un-swept purchase-side stop fuel [2420.0, 2530.0] = 17.139M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 2414.65 sits inside the sell-stop/long-cascade ladder [2300.0, 2420.0] carrying 1912.508M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2422.42 is 10.00 bps from the governing magnet edge 2420.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.13R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 42.9/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: NO_REACHABLE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `eth_shelf_long` — STAGE LONG ETH
> Mirror probe: long into a bearish HTF with $1,860M of forced fuel below = archetypes 2+6.
- metrics: symbol=ETHUSD.pi, mid=2414.65, atr_14=10.6426, regime=BEARISH, entry=2393.9, sl=2296.22, tp=2418.18, lots=0.11, stop_points=97.68000000000029, risk_usd=10.744800000000032, reward_usd=2.670799999999972, rr_gross=0.2485667485667452, rr_min_required=2.2, entry_distance_atr=1.949711536654577, friction_pct=2.9688779688779596, sl_clearance_atr=0.3551763666773345, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=29895029.270000003, overwhelm_ratio=7.344838585936597, best_reachable_rr=0.5492424242424235, best_reachable_tp=2447.55, post_stop_equity_usd=4844.119000000001, min_lot_spread_cash_usd=0.028999999999999998
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.272 exceeds 0.18
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2393.9 sits inside un-swept sale-side stop fuel [2300.0, 2420.0] = 1860.808M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 219.574M exceeds in-range verified defense 29.895M by 7.34:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.55R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.55R against the minimum compliant stop (97.6 points = clear the 2300.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.25R < 2.2R required for ETHUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -101,839,952
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `sol_repair_short` — STAGE SHORT SOL
> The cleanest engine-2 short in the book still pays 0.12R: the only reachable front-runnable pool sits directly under mid, and the $16.90M buy-stop belt [104-114] forces a 9.3-ATR stop.
- metrics: symbol=SOLUSD.p, mid=104.165, atr_14=0.5289, regime=BEARISH, entry=105.2, sl=114.19, tp=104.1, lots=0.01, stop_points=8.989999999999995, risk_usd=8.989999999999995, reward_usd=1.1000000000000085, rr_gross=0.12235817575083528, rr_min_required=2.5, entry_distance_atr=1.9568916619398686, friction_pct=2.558398220244718, sl_clearance_atr=0.3592361505010356, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=12149229.469999999, overwhelm_ratio=1.3820388997887616, best_reachable_rr=0.12191323692992419, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.3125, min_lot_spread_cash_usd=0.23
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.435 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.2 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 16.902M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 4.853M < 5.00M CRYPTO_ALT requirement
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.12R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.12R against the minimum compliant stop (9.0 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.12R < 2.5R required for SOLUSD.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 7,679,268
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD

### `sp500_core_short` — STAGE SHORT SP500
> Index short into the $817.3M buy-stop belt [7,700-7,810]. The exit pool [7,630-7,680] is 0.34R away; archetype 4 (ephemeral fuel) is not the issue here — geometry is.
- metrics: symbol=SP500.p, mid=7701.03, atr_14=9.3783, regime=BEARISH, entry=7719.32, sl=7813.33, tp=7687.68, lots=0.01, stop_points=94.01000000000022, risk_usd=9.401000000000023, reward_usd=3.163999999999942, rr_gross=0.33655994043186194, rr_min_required=2.0, entry_distance_atr=1.9502468464433815, friction_pct=0.36166365280289253, sl_clearance_atr=0.35507501359520677, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=22474457.029999997, overwhelm_ratio=0.2830148217378313, best_reachable_rr=0.33655994043187165, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4845.79875, min_lot_spread_cash_usd=0.034
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7719.32 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 819.197M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.34R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.34R against the minimum compliant stop (94.0 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 7687.68 is 10.00 bps from the governing magnet edge 7680.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.34R < 2.0R required for SP500.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 3
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `nas100_momentum_short` — STAGE SHORT NAS100
> Most extreme z in the book (z=-2.05) with RSI 19.5 — an Engine 1 exhaustion candidate that dies on affordability: min lot risk 107.00 USD against a 14.50 envelope (contract 10 x 2,970 index points).
- metrics: symbol=NAS100.p, mid=29729.45, atr_14=63.0269, regime=BEARISH, entry=29852.35, sl=30922.37, tp=29729.7, lots=0.01, stop_points=1070.0200000000004, risk_usd=107.00200000000005, reward_usd=12.264999999999782, rr_gross=0.11462402571914335, rr_min_required=2.0, entry_distance_atr=1.9499610483777217, friction_pct=0.11401656043812261, sl_clearance_atr=0.3549278165354631, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=7678741.86, overwhelm_ratio=0.5366672399116175, best_reachable_rr=0.30172333227416503, best_reachable_tp=29529.499999999996, post_stop_equity_usd=4723.797500000001, min_lot_spread_cash_usd=0.122
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 29852.35 sits inside un-swept purchase-side stop fuel [29800.0, 30900.0] = 4.121M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.30R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.30R against the minimum compliant stop (1069.7 points = clear the 30900.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- MAJOR `TP_FRONT_RUN_OFF` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 29729.7 is 10.00 bps from the governing magnet edge 29700.0; desk doctrine is a 5-10 bps front-run
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.11R < 2.0R required for NAS100.p
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4723.798 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL

### `gold_minlot_floor_probe` — STAGE SHORT GOLD
> Gold's sell-stop belt [3,980-4,100] carries $15.49M and contains nothing front-runnable inside the horizon; the min lot (0.01 on contract 100) risks 97.38 USD for a 3.6-ATR stop — 6.7x the envelope.
- metrics: symbol=XAUUSD.pi, mid=4102.135, atr_14=6.5737, regime=BEARISH, entry=4114.95, sl=4212.33, tp=4084.08, lots=0.01, stop_points=97.38000000000011, risk_usd=97.38000000000011, reward_usd=30.86999999999989, rr_gross=0.317005545286505, rr_min_required=2.0, entry_distance_atr=1.9494348692516543, friction_pct=0.07188334360238235, sl_clearance_atr=0.3544427035003008, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=6705817.410000001, overwhelm_ratio=0.18799848443830505, best_reachable_rr=0.31700554528650965, best_reachable_tp=4084.0799999999995, post_stop_equity_usd=4735.825, min_lot_spread_cash_usd=0.07
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4114.95 sits inside un-swept purchase-side stop fuel [4100.0, 4210.0] = 1.265M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.32R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.32R against the minimum compliant stop (97.4 points = clear the 4210.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.32R < 2.0R required for XAUUSD.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 96
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4735.825 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `near_friction_probe` — STAGE SHORT NEAR
> The only >=2.0R geometry in the book (2.22R) and it is unusable: at the 1.42 lot needed to hold risk at 11.98 USD the 63.69 bps spread burns 36.73% of the risk budget against a 15% ceiling.
- metrics: symbol=NERUSD.p, mid=4.8675, atr_14=0.0427, regime=BEARISH, entry=4.95076, sl=5.03516, tp=4.76357, lots=1.0, stop_points=0.08440000000000047, risk_usd=8.440000000000047, reward_usd=18.71900000000002, rr_gross=2.217890995260653, rr_min_required=2.0, entry_distance_atr=1.949882903981267, friction_pct=36.72985781990501, sl_clearance_atr=0.35503512880563765, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=2.2037914691943103, best_reachable_tp=4.764759999999999, post_stop_equity_usd=4847.0, min_lot_spread_cash_usd=3.1
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 63.69 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.726 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.10 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.031 / stop distance 0.084 = 36.73% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.95076 sits inside un-swept purchase-side stop fuel [4.87, 5.02] = 1.436M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 64.02/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.92/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `usdjpy_quote_currency_probe` — STAGE SHORT USDJPY
> Quote-currency probe. The short fades into the [148-158] long-cascade band ($9.93M) that contains mid 158.05, and the structural stop is 8.8 price units = 8,800 pips: at 0.01 lots that is 55.70 USD of risk once the JPY quote is converted to USD. Structurally unaffordable, not merely mis-scaled.
- metrics: symbol=USDJPY.pi, mid=158.049, atr_14=0.0929, regime=BEARISH, entry=158.23015, sl=167.03298, tp=158.1185, lots=0.01, stop_points=8.80283, risk_usd=55.696840853153134, reward_usd=0.7064264879878858, rr_gross=0.012683421127069064, rr_min_required=2.0, entry_distance_atr=1.9499461786867855, friction_pct=0.04543993238538061, sl_clearance_atr=0.35500538213142213, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=3293977.55, overwhelm_ratio=0.39815384898418626, best_reachable_rr=0.008196227804015518, best_reachable_tp=158.158, post_stop_equity_usd=4787.928948933559, min_lot_spread_cash_usd=0.02530860682446583
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 158.23015 sits inside un-swept purchase-side stop fuel [158.0, 167.0] = 1.312M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.01R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.01R against the minimum compliant stop (8.8 points = clear the 167.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.01R < 2.0R required for USDJPY.pi
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 35
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4787.929 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `eurusd_range_gate_probe` — STAGE SHORT EURUSD
> RANGE_BOUND regime (z=+0.85, RSI 77): neither engine applies in non-trending noise, so the card must be struck down by the regime gate before geometry. Also no reachable front-runnable pool exists (buy stops start at 1.1200).
- metrics: symbol=EURUSD.pi, mid=1.1183, atr_14=0.0006, regime=RANGE_BOUND, entry=1.11947, sl=1.11866, tp=1.1165, lots=0.14, stop_points=0.0008099999999999774, risk_usd=11.339999999999685, reward_usd=41.57999999999884, rr_gross=3.666666666666666, rr_min_required=2.0, entry_distance_atr=1.9499999999998223, friction_pct=0.0, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4843.375000000001, min_lot_spread_cash_usd=0.0
- FATAL `REGIME_GATED_STAND_ASIDE` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime=RANGE_BOUND: neither engine applies in non-trending noise
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 1.1183 sits inside the sell-stop/long-cascade ladder [1.09, 1.12] carrying 5.476M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `NO_REACHABLE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no magnet within 3.5 ATR of mid (1.1183) to front-run; nearest qualifying pool is 1.05-1.07 USD 78.72 ATR from mid
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 1.1165 sits INSIDE the magnet pool [1.11, 1.12] carrying 2.530M USD instead of front-running it
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 27
  - Orderflow & Microstructure: 42.5/100 — fatal: REGIME_GATED_STAND_ASIDE, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 42.5/100 — fatal: REGIME_GATED_STAND_ASIDE, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 42.5/100 — fatal: REGIME_GATED_STAND_ASIDE, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 42.5/100 — fatal: REGIME_GATED_STAND_ASIDE, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 42.5/100 — fatal: REGIME_GATED_STAND_ASIDE, NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD

### `ger40_empty_book_probe` — STAGE SHORT GER40
> Engine 1 exhaustion probe (z=-2.07, RSI 35.2) on a book with ZERO stop clusters and ZERO liquidation bands — there is no structure to fade against.
- metrics: symbol=GER40.p, mid=25199.9, atr_14=25.0699, regime=BEARISH, entry=25248.79, sl=25273.86, tp=25124.69, lots=0.04, stop_points=25.06999999999971, risk_usd=10.027999999999883, reward_usd=49.640000000000875, rr_gross=4.9501396090946805, rr_min_required=2.0, entry_distance_atr=1.9501473879033988, friction_pct=9.174311926605611, sl_clearance_atr=None, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4845.015, min_lot_spread_cash_usd=0.23
- INFO `SL_HAS_NO_HAZARD_REFERENCE` (A3: Insufficient structural buffer (sub-0.35 ATR clearance)) — no sweep belt on the stop's side of price: clearance is bounded by the 0.35 ATR minimum only
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 1
  - Orderflow & Microstructure: 50.24/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 54.38/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 50.24/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 58.52/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 50.24/100 — fatal: NO_MAGNETS | purchase-side sweep hazard: NO_BUNKER_WALL, COUNTER_CVD

### `desk_batch_4x_max_risk` — STAGE_BATCH SHORT BTC
> Capacity strawman: four max-envelope tickets would prove the joint floor boundary empirically (4 x 20.13 = 80.50 stressed against a 64.55 budget). Included so the bracket contains the boundary case, not to propose it.
- metrics: symbol=BTCUSD.pi, mid=81453.0, atr_14=249.2923, regime=BEARISH, min_lot_spread_cash_usd=0.16
- FATAL `CARD_INCOMPLETE` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — trade card is missing entry/SL/TP/lots
  - Orderflow & Microstructure: 64.3/100 — fatal: CARD_INCOMPLETE
  - Structural Price Action: 49.9/100 — fatal: CARD_INCOMPLETE
  - Liquidation & Stop Forensic: 49.9/100 — fatal: CARD_INCOMPLETE
  - Macro Risk & Portfolio Governor: 57.1/100 — fatal: CARD_INCOMPLETE
  - Adversarial Pre-Mortem Red Team: 57.1/100 — fatal: CARD_INCOMPLETE

### `btc_armed_post_ladder_short` — WATCH None BTC
> Forward posture only. The seller ladder [80,500-81,500] is the wall that blocks every exit; a decisive break below 80,400 would clear it and re-open a front-runnable path to the 79,800-80,100 pool.
- metrics: symbol=BTCUSD.pi, mid=81453.0, atr_14=249.2923, regime=BEARISH, min_lot_spread_cash_usd=0.16
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: 15m close < 80,400 with session CVD < 0 (ladder vacated)
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle111` — STAND_ASIDE
> Every candidate in the universe carries at least one fatal gate failure on generation 92182f87cfd347e79d2e5e20c1f8689b (2026-10-14 23:36:35 UTC); 0 of 24 assets clear the dual engine. Re-proves itself by re-running each member card.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 12 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
