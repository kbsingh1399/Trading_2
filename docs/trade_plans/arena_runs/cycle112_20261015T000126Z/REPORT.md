# Arena tournament cycle112_20261015T000126Z

- snapshot: `/tmp/snap112.json` generation `7b193feddf874dfda838cfaae6ac9d39` as_of `2026-10-15 00:01:26 UTC`
- cards: `docs/trade_plans/arena_cards/cycle112_20261015T000126Z.json` sha256 `262e65686541e705`
- evidence ledgers: `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_144200Z.json`, `docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_150912Z.json`
- seed: 112 | rubric weights: correctness 30, completeness 25, specificity 15, robustness 20, clarity 10
- **winner: `desk_stand_aside_cycle112`**

## Scoreboard

| card | action | fatal | purchase-side hazard | rubric /100 | verdict |
|---|---|---|---|---:|---|
| `desk_stand_aside_cycle112` | STAND_ASIDE | no | - | 71.50 | advisory only |
| `nas100_relief_rally_short` | WATCH | no | - | 69.00 | advisory only |
| `btc_armed_post_ladder_short` | WATCH | no | - | 69.00 | advisory only |
| `desk_batch_4x_max_risk` | STAGE_BATCH | YES | - | 55.66 | CONTRADICTED |
| `near_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 51.39 | CONTRADICTED |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL | 48.72 | CONTRADICTED |
| `btc_belt_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `eth_artifact_anchor_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `eth_shelf_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `sol_belt_short` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN | 48.00 | CONTRADICTED |
| `sp500_long_variant` | STAGE | YES | COUNTER_CVD | 48.00 | CONTRADICTED |
| `silver_floor_probe` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN | 48.00 | CONTRADICTED |
| `nas100_extreme_probe` | STAGE | YES | ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `xrp_alt_long` | STAGE | YES | - | 48.00 | CONTRADICTED |
| `eth_artifact_probe` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `fx_range_gate_probe` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD | 48.00 | CONTRADICTED |

## Bracket
### Round 1
- `nas100_extreme_probe` (48.0, fatal=True) vs `sp500_long_variant` (48.0, fatal=True) -> **nas100_extreme_probe** — exact tie: fewer standing attacks (deterministic order)
- `btc_belt_long` (48.0, fatal=True) vs `sol_belt_short` (48.0, fatal=True) -> **btc_belt_long** — exact tie: fewer standing attacks (deterministic order)
- `btc_armed_post_ladder_short` (69.0, fatal=False) vs `eth_artifact_anchor_short` (48.0, fatal=True) -> **btc_armed_post_ladder_short** — eth_artifact_anchor_short is contradicted by the snapshot; btc_armed_post_ladder_short is not
- `fx_range_gate_probe` (48.0, fatal=True) vs `eth_shelf_long` (48.0, fatal=True) -> **fx_range_gate_probe** — exact tie: fewer standing attacks (deterministic order)
- `near_friction_probe` (51.39, fatal=True) vs `silver_floor_probe` (48.0, fatal=True) -> **near_friction_probe** — higher rubric total (51.39 vs 48.0)
- `sp500_core_short` (48.72, fatal=True) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 48.72)
- `xrp_alt_long` (48.0, fatal=True) vs `eth_artifact_probe` (48.0, fatal=True) -> **xrp_alt_long** — exact tie: fewer standing attacks (deterministic order)
- `nas100_relief_rally_short` (69.0, fatal=False) vs `desk_stand_aside_cycle112` (71.5, fatal=False) -> **desk_stand_aside_cycle112** — higher rubric total (71.5 vs 69.0)
### Round 2
- `nas100_extreme_probe` (48.0, fatal=True) vs `btc_belt_long` (48.0, fatal=True) -> **nas100_extreme_probe** — exact tie: fewer standing attacks (deterministic order)
- `btc_armed_post_ladder_short` (69.0, fatal=False) vs `fx_range_gate_probe` (48.0, fatal=True) -> **btc_armed_post_ladder_short** — fx_range_gate_probe is contradicted by the snapshot; btc_armed_post_ladder_short is not
- `near_friction_probe` (51.39, fatal=True) vs `desk_batch_4x_max_risk` (55.66, fatal=True) -> **desk_batch_4x_max_risk** — higher rubric total (55.66 vs 51.39)
- `xrp_alt_long` (48.0, fatal=True) vs `desk_stand_aside_cycle112` (71.5, fatal=False) -> **desk_stand_aside_cycle112** — xrp_alt_long is contradicted by the snapshot; desk_stand_aside_cycle112 is not
### Round 3
- `nas100_extreme_probe` (48.0, fatal=True) vs `btc_armed_post_ladder_short` (69.0, fatal=False) -> **btc_armed_post_ladder_short** — nas100_extreme_probe is contradicted by the snapshot; btc_armed_post_ladder_short is not
- `desk_batch_4x_max_risk` (55.66, fatal=True) vs `desk_stand_aside_cycle112` (71.5, fatal=False) -> **desk_stand_aside_cycle112** — desk_batch_4x_max_risk is contradicted by the snapshot; desk_stand_aside_cycle112 is not
### Round 4
- `btc_armed_post_ladder_short` (69.0, fatal=False) vs `desk_stand_aside_cycle112` (71.5, fatal=False) -> **desk_stand_aside_cycle112** — higher rubric total (71.5 vs 69.0)

## Findings per card
### `btc_belt_long` — STAGE LONG BTC
> Best legal long geometry in the book (0.94R): price is under EMA20 81,613.5 < EMA50 81,951.6 < EMA200 82,700.9 (bearish stack), so a Model-1 long is banned outright and the $151.6M cascade ladder below mid overwhelms defence.
- metrics: symbol=BTCUSD.pi, mid=81609.5, atr_14=239.1908, regime=BEARISH, entry=81143.07794, sl=80615.087266, tp=81638.72499999999, lots=0.02, stop_points=527.9906740000006, risk_usd=10.559813480000011, reward_usd=9.912941199999768, rr_gross=0.9387420733116734, rr_min_required=2.0, entry_distance_atr=1.9499999999999882, friction_pct=3.2197538398187655, sl_clearance_atr=0.3549999999999905, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=65621096.00999999, overwhelm_ratio=0.9550398605114673, best_reachable_rr=0.9000576779126965, best_reachable_tp=81618.3, post_stop_equity_usd=4844.35023315, min_lot_spread_cash_usd=0.17
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 81143.07794 sits inside un-swept sale-side stop fuel [80700.0, 81700.0] = 101.714M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.90R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.90R against the minimum compliant stop (526.8 points = clear the 80700.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.94R < 2.0R required for BTCUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `eth_artifact_anchor_short` — STAGE SHORT ETH
> Artifact-free geometry after the trusted-magnet exclusion still pays only ~0.19R; the merged prop belt [2,300-2,420] carries $202.8M of cascade structure under price.
- metrics: symbol=ETHUSD.pi, mid=2419.75, atr_14=10.2393, regime=BEARISH, entry=2439.716635, sl=2533.6349515, tp=2421.815, lots=0.12, stop_points=93.91831649999995, risk_usd=11.270197979999994, reward_usd=2.14819620000002, rr_gross=0.1906085593005724, rr_min_required=2.2, entry_distance_atr=1.950000000000022, friction_pct=3.0877895900103804, sl_clearance_atr=0.35500000000001664, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=31831081.150000002, overwhelm_ratio=0.5121211561486656, best_reachable_rr=0.39733074857661665, best_reachable_tp=2402.3999999999996, post_stop_equity_usd=4843.462252525001, min_lot_spread_cash_usd=0.028999999999999998
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.283 exceeds 0.18
- MINOR `MAGNET_UNTRUSTED_EXCLUDED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — 1 bin(s) excluded as untrusted (> 10x the larger neighbour); largest [2400.0, 2410.0] carrying 1650.425M USD cannot anchor a TP
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2439.716635 sits inside un-swept purchase-side stop fuel [2420.0, 2530.0] = 17.174M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 2419.75 sits inside the sell-stop/long-cascade ladder [2410.0, 2420.0] carrying 0.913M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.40R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.40R against the minimum compliant stop (93.9 points = clear the 2530.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.19R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `eth_shelf_long` — STAGE LONG ETH
> Bearish stack (EMA20 2,419.1 < EMA50 2,436.1 < EMA200 2,477.7) with a 2,083-point stop against $202.8M of cascade structure below mid: defence loses 51:1.
- metrics: symbol=ETHUSD.pi, mid=2419.75, atr_14=10.2393, regime=BEARISH, entry=2418.214105, sl=2296.3650485, tp=2448.1625, lots=0.09, stop_points=121.84905650000019, risk_usd=10.966415085000017, reward_usd=2.69535554999999, rr_gross=0.245782740221709, rr_min_required=2.2, entry_distance_atr=0.14999999999999827, friction_pct=2.3799938081588636, sl_clearance_atr=0.35500000000001664, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=70614774.63000003, overwhelm_ratio=26.36195110504737, best_reachable_rr=0.24075602916137573, best_reachable_tp=2447.55, post_stop_equity_usd=4843.84198114375, min_lot_spread_cash_usd=0.028999999999999998
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.283 exceeds 0.18
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2418.214105 sits inside un-swept sale-side stop fuel [2300.0, 2420.0] = 1861.543M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 1861.543M exceeds in-range verified defense 70.615M by 26.36:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.24R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.24R against the minimum compliant stop (121.8 points = clear the 2300.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.25R < 2.2R required for ETHUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND

### `sol_belt_short` — STAGE SHORT SOL
> SOL is inside the buy-stop belt [104-114] $16.9M; the only reachable front-runnable pool sits directly under mid and the compliant stop is 9.0 ATR wide.
- metrics: symbol=SOLUSD.p, mid=104.18, atr_14=0.4914, regime=BEARISH, entry=105.13823000000001, sl=114.174447, tp=104.078, lots=0.01, stop_points=9.036216999999994, risk_usd=9.036216999999994, reward_usd=1.0602300000000042, rr_gross=0.11733117962970621, rr_min_required=2.5, entry_distance_atr=1.9500000000000006, friction_pct=2.4346471537812797, sl_clearance_atr=0.35500000000000137, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=8679781.44, overwhelm_ratio=1.9340909060954423, best_reachable_rr=0.11445386935705759, best_reachable_tp=104.10399999999998, post_stop_equity_usd=4846.25472875, min_lot_spread_cash_usd=0.22
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.448 exceeds 0.18
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 105.13823000000001 sits inside un-swept purchase-side stop fuel [104.0, 114.0] = 16.899M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 4.853M < 5.00M CRYPTO_ALT requirement
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.11R at this card's stop < required 2.5R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.11R against the minimum compliant stop (9.0 points = clear the 114.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.5R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.12R < 2.5R required for SOLUSD.p
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN

### `sp500_core_short` — STAGE SHORT SP500
> The $812.6M buy-stop cluster at [7,700-7,710] sits at price; best reachable reward is 32.7 pts against a 94.8-pt compliant stop.
- metrics: symbol=SP500.p, mid=7700.63, atr_14=9.1432, regime=BEARISH, entry=7718.45924, sl=7813.245836, tp=7685.76, lots=0.01, stop_points=94.78659599999992, risk_usd=9.478659599999991, reward_usd=3.269923999999992, rr_gross=0.3449774691771815, rr_min_required=2.0, entry_distance_atr=1.9500000000000028, friction_pct=0.3587005065568557, sl_clearance_atr=0.35500000000000587, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=22010418.580000002, overwhelm_ratio=0.2889027328984127, best_reachable_rr=0.3247214405716266, best_reachable_tp=7687.679999999999, post_stop_equity_usd=4845.7016755, min_lot_spread_cash_usd=0.034
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7718.45924 sits inside un-swept purchase-side stop fuel [7700.0, 7810.0] = 818.974M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.32R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.32R against the minimum compliant stop (94.7 points = clear the 7810.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.34R < 2.0R required for SP500.p
  - Orderflow & Microstructure: 51.62/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `sp500_long_variant` — STAGE LONG SP500
> Long-side variant of the same wall: reward 20.0 pts against a 97.5-pt stop = 0.21R.
- metrics: symbol=SP500.p, mid=7700.63, atr_14=9.1432, regime=BEARISH, entry=7694.22976, sl=7596.754164, tp=7714.21, lots=0.01, stop_points=97.47559600000022, risk_usd=9.747559600000022, reward_usd=1.9980239999999867, rr_gross=0.20497684363991805, rr_min_required=2.0, entry_distance_atr=0.6999999999999934, friction_pct=0.3488052537785963, sl_clearance_atr=0.35500000000000587, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=11966322.700000001, overwhelm_ratio=3.5085994221098518, best_reachable_rr=0.18517701599895356, best_reachable_tp=7712.28, post_stop_equity_usd=4845.365550500001, min_lot_spread_cash_usd=0.034
- MINOR `MAGNET_ARTIFACT_EXCLUDED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — 1 bin(s) excluded as provider artifacts (>= 100x the larger price-adjacent neighbour); largest [7700.0, 7710.0] carrying 812.615M USD cannot anchor a TP
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 7694.22976 sits inside un-swept sale-side stop fuel [7600.0, 7700.0] = 41.985M USD
- FATAL `OVERWHELM_RATIO` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — forced fuel 41.985M exceeds in-range verified defense 11.966M by 3.51:1 (> 2.0:1 cap)
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.19R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.19R against the minimum compliant stop (97.4 points = clear the 7600.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.20R < 2.0R required for SP500.p
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — long against negative session CVD -83
  - Orderflow & Microstructure: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: OVERWHELM_RATIO, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND | purchase-side sweep hazard: COUNTER_CVD

### `near_friction_probe` — STAGE SHORT NEAR
> 2.94R gross - the best geometry in the book - burning 48.34% of risk in friction at the 1.81 lots required; NEAR is on the banned-instrument list.
- metrics: symbol=NERUSD.p, mid=4.89, atr_14=0.04, regime=BEARISH, entry=4.968, sl=5.034199999999999, tp=4.7735775, lots=2.0, stop_points=0.06619999999999937, risk_usd=13.239999999999874, reward_usd=38.88449999999999, rr_gross=2.9368957703927765, rr_min_required=2.0, entry_distance_atr=1.9500000000000073, friction_pct=48.33836858006088, sl_clearance_atr=0.3549999999999942, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=2.9188821752266243, best_reachable_tp=4.774769999999999, post_stop_equity_usd=4841.0, min_lot_spread_cash_usd=3.2
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 65.44 bps exceeds the 35 bps CRYPTO_ALT ceiling
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.800 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.20 USD, above 2.175 USD (15% of max risk)
- FATAL `FRICTION_BUDGET` (A7: Friction drag (broker spread consumes the risk budget)) — spread 0.032 / stop distance 0.066 = 48.34% of risk, above the 15% dynamic friction ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 4.968 sits inside un-swept purchase-side stop fuel [4.89, 5.02] = 1.366M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
  - Orderflow & Microstructure: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Structural Price Action: 64.02/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Liquidation & Stop Forensic: 48.92/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: FRICTION_BUDGET | purchase-side sweep hazard: ENTRY_IN_FUEL, NO_BUNKER_WALL

### `silver_floor_probe` — STAGE SHORT SILVER
> Ceiling 0.70R against a 2.0R mandate AND min-lot risk 54.08 USD: a 1.08-point structural stop cannot be traded at 0.01 lots inside the envelope.
- metrics: symbol=XAGUSD.pi, mid=55.738, atr_14=0.2385, regime=BEARISH, entry=56.203075, sl=57.284667500000005, tp=55.44155, lots=0.01, stop_points=1.0815925000000064, risk_usd=54.07962500000033, reward_usd=38.076249999999945, rr_gross=0.7040775523129037, rr_min_required=2.0, entry_distance_atr=1.949999999999995, friction_pct=3.328425446737083, sl_clearance_atr=0.355000000000008, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=397693.29000000004, overwhelm_ratio=1.2172103029447643, best_reachable_rr=1.0614672346563043, best_reachable_tp=55.05499999999999, post_stop_equity_usd=4789.950468749999, min_lot_spread_cash_usd=1.8
- MAJOR `SPREAD_CEILING` (A7: Friction drag (broker spread consumes the risk budget)) — spread 6.46 bps exceeds the 5 bps COMMODITY ceiling
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 56.203075 sits inside un-swept purchase-side stop fuel [55.8, 57.2] = 0.568M USD
- MAJOR [purchase-side] `BUNKER_WALL_THIN` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — largest in-range wall 0.200M < 0.75M COMMODITY requirement
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 1.06R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 1.06R against the minimum compliant stop (1.1 points = clear the 57.2 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.70R < 2.0R required for XAGUSD.pi
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4789.950 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, BUNKER_WALL_THIN

### `nas100_extreme_probe` — STAGE SHORT NAS100
> Deepest statistical extreme in the book (Z -2.01, RSI 17.3, EMA stack down 29,862 < 30,057 < 30,406) but the compliant stop must clear the [29,700-30,900] buy belt -> 119.50 USD at min lot.
- metrics: symbol=NAS100.p, mid=29724.82, atr_14=61.7065, regime=BEARISH, entry=29845.147675, sl=30921.9058075, tp=29722.275, lots=0.01, stop_points=1076.7581324999992, risk_usd=107.67581324999992, reward_usd=12.28726749999987, rr_gross=0.11411353329156193, rr_min_required=2.0, entry_distance_atr=1.9500000000000075, friction_pct=0.11330306808711296, sl_clearance_atr=0.35499999999998955, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=5896421.59, overwhelm_ratio=0.6528258896087518, best_reachable_rr=0.2931463115742978, best_reachable_tp=29529.499999999996, post_stop_equity_usd=4722.9552334375, min_lot_spread_cash_usd=0.122
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 29845.147675 sits inside un-swept purchase-side stop fuel [29700.0, 30900.0] = 4.192M USD
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.29R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.29R against the minimum compliant stop (1076.4 points = clear the 30900.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.11R < 2.0R required for NAS100.p
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 11
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4722.955 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, FLOOR_BREACH | purchase-side sweep hazard: ENTRY_IN_FUEL, COUNTER_CVD

### `xrp_alt_long` — STAGE LONG XRP
> Counter-trend long into a bearish stack; min-lot risk 101.41 USD at the compliant stop, and the [1.30-1.31] bin is excluded as untrusted (>10x neighbours).
- metrics: symbol=XRPUSD.pi, mid=1.3305, atr_14=0.0057, regime=BEARISH, entry=1.319385, sl=1.2179765, tp=1.3489875, lots=1.0, stop_points=0.10140850000000001, risk_usd=101.40850000000002, reward_usd=29.602499999999978, rr_gross=0.2919133997643193, rr_min_required=2.0, entry_distance_atr=1.9499999999999975, friction_pct=2.9583318952553284, sl_clearance_atr=0.35499999999999227, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=0, overwhelm_ratio=None, best_reachable_rr=0.28858527638215825, best_reachable_tp=1.3486500000000001, post_stop_equity_usd=4730.789375, min_lot_spread_cash_usd=3.0
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.526 exceeds 0.18
- MAJOR `MIN_LOT_FRICTION` (A7: Friction drag (broker spread consumes the risk budget)) — spread cash at min lot (1.0 lot) is 3.00 USD, above 2.175 USD (15% of max risk)
- MAJOR `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 1.319385 sits inside un-swept sale-side stop fuel [1.22, 1.33] = 33.071M USD
- MAJOR `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no bid whale wall at or inside the SL
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.29R at this card's stop < required 2.0R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.29R against the minimum compliant stop (0.1 points = clear the 1.22 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.0R in this generation
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.29R < 2.0R required for XRPUSD.pi
- FATAL `COUNTER_TREND` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — Model 1/2 longs are banned in a verified BEARISH regime
- FATAL `FLOOR_BREACH` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — joint post-stop equity 4730.789 USD < 4795.0 USD operating buffer
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN, COUNTER_TREND, FLOOR_BREACH

### `eth_artifact_probe` — STAGE SHORT ETH
> Deliberate probe of the peer-audited Trusted-Magnet Rule: TP 2,412.41 anchors the [2,400-2,410] bin carrying $1,650.43M after per-bucket consolidation (~54x its larger neighbour, ~1,904x its smaller), so the engine must refuse to let it anchor an exit.
- metrics: symbol=ETHUSD.pi, mid=2419.75, atr_14=10.2393, regime=BEARISH, entry=2439.72, sl=2533.69, tp=2412.41, lots=0.12, stop_points=93.97000000000025, risk_usd=11.27640000000003, reward_usd=3.2771999999999935, rr_gross=0.2906246674470562, rr_min_required=2.2, entry_distance_atr=1.9503286357465648, friction_pct=3.0860913057358648, sl_clearance_atr=0.3603761975916376, hazard_union=[None, None], hazard_union_usd=0, in_range_defense_usd=31831081.150000002, overwhelm_ratio=0.5121211561486656, best_reachable_rr=0.3971480259657344, best_reachable_tp=2402.3999999999996, post_stop_equity_usd=4843.4545, min_lot_spread_cash_usd=0.028999999999999998
- MAJOR `SPREAD_OVER_ATR` (A7: Friction drag (broker spread consumes the risk budget)) — spread/ATR 0.283 exceeds 0.18
- MINOR `MAGNET_UNTRUSTED_EXCLUDED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — 1 bin(s) excluded as untrusted (> 10x the larger neighbour); largest [2400.0, 2410.0] carrying 1650.425M USD cannot anchor a TP
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 2439.72 sits inside un-swept purchase-side stop fuel [2420.0, 2530.0] = 17.174M USD
- MINOR `PRICE_INSIDE_MAGNET_LADDER` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — mid 2419.75 sits inside the sell-stop/long-cascade ladder [2410.0, 2420.0] carrying 0.913M USD: no front-runnable TP exists inside the ladder, the exit must clear its near edge
- FATAL `UNPAYABLE_GEOMETRY` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — best reachable front-runnable target yields 0.40R at this card's stop < required 2.2R
- FATAL `NO_PAYABLE_SETUP` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — asset-level verdict: the best front-runnable target pays 0.40R against the minimum compliant stop (93.9 points = clear the 2530.0 fuel edge by 0.35 ATR), so no card on this asset can be staged at >= 2.2R in this generation
- FATAL `TP_INSIDE_MAGNET` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — TP 2412.41 sits INSIDE the magnet pool [2410.0, 2420.0] carrying 0.913M USD instead of front-running it
- FATAL `RR_BELOW_MIN` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — quoted geometry 0.29R < 2.2R required for ETHUSD.pi
  - Orderflow & Microstructure: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Structural Price Action: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Liquidation & Stop Forensic: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET, RR_BELOW_MIN | purchase-side sweep hazard: ENTRY_IN_FUEL

### `fx_range_gate_probe` — STAGE SHORT GBPUSD
> RANGE_BOUND regime (EMA20 1.3199 vs EMA50 1.3201 vs EMA200 1.3224, RSI 77.3): neither engine applies in non-trending noise, so the regime gate must strike the card down before geometry. EURUSD is range-bound too.
- metrics: symbol=GBPUSD.pi, mid=1.3231, atr_14=0.0008, regime=RANGE_BOUND, entry=1.32466, sl=1.32514, tp=1.3207, lots=0.23, stop_points=0.00048000000000003595, risk_usd=11.040000000000827, reward_usd=91.07999999999917, rr_gross=8.249999999999307, rr_min_required=2.0, entry_distance_atr=1.9500000000000073, friction_pct=0.0, sl_clearance_atr=-6.424999999999903, hazard_union=[1.32, 1.37], hazard_union_usd=1299698.1800000002, in_range_defense_usd=0, overwhelm_ratio=None, post_stop_equity_usd=4843.749999999999, min_lot_spread_cash_usd=0.0
- FATAL `REGIME_GATED_STAND_ASIDE` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — trend_regime=RANGE_BOUND: neither engine applies in non-trending noise
- FATAL [purchase-side] `SL_INSIDE_SWEEP` (A1: SL inside sweep band / insufficient structural buffer) — SL 1.32514 sits INSIDE the purchase-side sweep belt [1.32, 1.37] carrying 1.300M USD
- MAJOR [purchase-side] `ENTRY_IN_FUEL` (A8: Stop-on-stop / entry parked inside un-swept opposing stop fuel) — entry 1.32466 sits inside un-swept purchase-side stop fuel [1.32, 1.37] = 1.300M USD
- MAJOR [purchase-side] `NO_BUNKER_WALL` (A4: Ephemeral wall defense (unverified persistence / relocated wall)) — no ask whale wall at or inside the SL
- FATAL `NO_MAGNETS` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — no opposing stop/liquidation magnet >= 0.50M USD on the target side
- MAJOR [purchase-side] `COUNTER_CVD` (A2: Counter-trend entry against HTF regime or unabsorbed opposing CVD) — short against positive session CVD 62
  - Orderflow & Microstructure: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_MAGNETS | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD
  - Structural Price Action: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_MAGNETS | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD
  - Liquidation & Stop Forensic: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_MAGNETS | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD
  - Macro Risk & Portfolio Governor: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_MAGNETS | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD
  - Adversarial Pre-Mortem Red Team: 48.0/100 — fatal: REGIME_GATED_STAND_ASIDE, SL_INSIDE_SWEEP, NO_MAGNETS | purchase-side sweep hazard: SL_INSIDE_SWEEP, ENTRY_IN_FUEL, NO_BUNKER_WALL, COUNTER_CVD

### `desk_batch_4x_max_risk` — STAGE_BATCH SHORT BTC
> Capacity strawman: four max-envelope tickets (4 x 20.12 = 80.48 stress) against the 64.55 USD budget. Included so the bracket contains the boundary case the governor computes by hand.
- metrics: symbol=BTCUSD.pi, mid=81609.5, atr_14=239.1908, regime=BEARISH, min_lot_spread_cash_usd=0.17
- FATAL `CARD_INCOMPLETE` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — trade card is missing entry/SL/TP/lots
  - Orderflow & Microstructure: 64.3/100 — fatal: CARD_INCOMPLETE
  - Structural Price Action: 49.9/100 — fatal: CARD_INCOMPLETE
  - Liquidation & Stop Forensic: 49.9/100 — fatal: CARD_INCOMPLETE
  - Macro Risk & Portfolio Governor: 57.1/100 — fatal: CARD_INCOMPLETE
  - Adversarial Pre-Mortem Red Team: 57.1/100 — fatal: CARD_INCOMPLETE

### `nas100_relief_rally_short` — WATCH None NAS100
> Peer-audit watch (Astra, seed 111). Relief rally into the EMA20 shelf 29,850-29,900 paying >=2.0R to a 29,729.7 front-run requires SL <=30,050; on this generation that stop sits INSIDE the [29,700-30,900] buy belt ($4.12M) = archetype-1 kill. The watch is therefore latent until the belt is consumed or thinned below the index wall threshold.
- metrics: symbol=NAS100.p, mid=29724.82, atr_14=61.7065, regime=BEARISH, min_lot_spread_cash_usd=0.122
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: relief rally >=29,930 with velocity_ratio < 0.70, a >=1.0M USD ask wall defending the shelf AND the [29,700-30,900] buy belt thinned below 1.0M USD
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `btc_armed_post_ladder_short` — WATCH None BTC
> The merged seller ladder [80,500-81,500] ($79.0M) is the wall that blocks the exit; a decisive break below 80,400 clears it and re-opens a front-runnable path to the 79,800-80,100 pool.
- metrics: symbol=BTCUSD.pi, mid=81609.5, atr_14=239.1908, regime=BEARISH, min_lot_spread_cash_usd=0.17
- INFO `CONDITIONAL_UNTRIGGERED` (A5: Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)) — armed trigger has not fired in this generation: 15m close < 80,400 with session CVD < 0 (ladder vacated)
  - Orderflow & Microstructure: 69.0/100 — no fatal flaw found
  - Structural Price Action: 69.0/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 69.0/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 69.0/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 69.0/100 — no fatal flaw found

### `desk_stand_aside_cycle112` — STAND_ASIDE
> Every candidate carries at least one fatal gate failure on generation 7b193feddf874dfda838cfaae6ac9d39 (2026-10-15 00:01:26 UTC); 0 of 24 assets clear the dual engine. Re-proves itself by re-running each member card.
- metrics: qualified_candidates=[]
- INFO `STAND_ASIDE_JUSTIFIED` (A6: Unpayable geometry (no reachable front-runnable liquidity magnet)) — every one of the 12 candidate cards in the universe carries at least one fatal gate failure
  - Orderflow & Microstructure: 71.5/100 — no fatal flaw found
  - Structural Price Action: 71.5/100 — no fatal flaw found
  - Liquidation & Stop Forensic: 71.5/100 — no fatal flaw found
  - Macro Risk & Portfolio Governor: 71.5/100 — no fatal flaw found
  - Adversarial Pre-Mortem Red Team: 71.5/100 — no fatal flaw found

## Runtime disclosure

Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not immunity to unbounded gaps, and no broker execution was performed.
