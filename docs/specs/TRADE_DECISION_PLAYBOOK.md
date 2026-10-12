# 📘 LIVE TELEMETRY TRADE DECISION PLAYBOOK & CONFLUENCE CHECKLIST

> **Canonical Living Document:** `docs/specs/TRADE_DECISION_PLAYBOOK.md`  
> **Source of Truth:** Consolidated live telemetry from `docs/telemetry/live_snapshot_latest.json`  
> **Target Execution Venue:** Blueberry Markets MetaTrader 5 (Account #5064568) & Binance USDT-M / Hyperliquid DEX  
> **Version:** 1.0 (Living Document — Continuously Upgraded from Empirical Trading Sessions)

---

## 1. Executive Mission & Strategic Pivot

The quantitative trading desk operates on a fundamental truth demonstrated through empirical session trading:
**Brittle binary gates fail by discarding valid high-confluence setups, whereas human-grade multi-parameter coincidence reasoning generates asymmetric positive expectancy.**

Rather than filtering out assets via isolated threshold checks (e.g. an arbitrary efficiency ratio floor or rigid trend memory), the desk systematically digests the complete, unabridged telemetry across five intersecting pillars:
1. **Causal Statistical & Structural Geography** (VWAP Z-scores, Standard Deviation bands, EMA shelves, Session POC/VAH/VAL)
2. **On-Chain & L3 Wallet Liquidity** (Hyperliquid verified whale wallets `0x...`, resting orders >= 150k USD, institutional TWAPs)
3. **Reconstructed Liquidation Cascades** (Overhead short squeeze pools, downside long cascade exhaustion bands)
4. **Structural Stop Clusters** (Dense retail/bot stop-loss clusters acting as price magnets or sweep barriers)
5. **Live L2 Orderbook Depth & CVD Taker Absorption** (Bid/ask imbalance, persistent book walls, 1m taker CVD delta exhaustion)

### 1.1 Dual-Venue Hybrid Architecture (Crucial Core Concept)
- **Spread & Quotes from MT5 (`quotes`)**: MT5 (Blueberry Markets Account #5064568) is our actual financial execution venue. All order placement, fills, slippage, and broker transaction costs occur on MT5. Therefore, broker spread (`spread_bps`), top-of-book bid/ask/mid, tick size, min lot, and stops level MUST be queried directly from MT5 ticks. An asset may be tight on Binance or Hyperliquid, but if the MT5 CFD spread is wide (e.g. 80 bps on retail alts), trading it incurs lethal negative drag.
- **Orderbook Depth, Whale Walls & Liquidations from Hyperdash / Binance (`orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`)**: MT5 CFD brokers only provide synthetic L1/L2 pricing and do not reveal real institutional orderflow or whale wallet identities. In contrast, Hyperdash exposes:
  1. Real Hyperliquid L1 blockchain on-chain orderbook with verified wallet addresses (`0x...`), resting sizes, and persistent walls.
  2. Aggregated Binance USDT-M Futures L2 depth (top 20 bid/ask ladder and imbalance).
  3. Reconstructed liquidation cascade bands across open positions.
  4. Real structural stop clusters and institutional TWAPs.
- **Cross-Venue Basis Mapping (`venue_basis`)**: The telemetry pipeline calculates the live price basis between MT5 mid and Hyperdash/Binance mid (`basis_median = mid_mt5 - mid_binance`). This aligns on-chain whale walls, stop clusters, and liquidation levels directly onto the broker's tick grid.

---

## 2. Complete Inventory of Consolidated Telemetry Parameters

The table below catalogs every parameter consolidated in `docs/telemetry/live_snapshot_latest.json`, detailing its source, interpretation, and strategic contribution to trade construction.

### A. Global Risk & Portfolio Level (`account`, `risk`, `capacity`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `account.balance` / `equity` | `NATIVE_MT5_ACCOUNT_INFO` (`mt5.account_info()`) | Live MT5 balance and equity in USD | Sets absolute baseline for risk sizing and cushion calculation |
| `account.margin_free` | `NATIVE_MT5_ACCOUNT_INFO` (`mt5.account_info()`) | Available margin for staging new limit orders | Validates leverage headroom (must maintain > 4,000 USD free margin) |
| `account.margin_level_pct` | `NATIVE_MT5_ACCOUNT_INFO` (`mt5.account_info()`) | Broker margin utilization health | Circuit breaker if margin level falls towards broker margin call |
| `risk.hard_floor_usd` | Institutional Invariant (`AGENTS.md`) | Absolute capital floor ($4,775.00 USD) | Unconditional stop; no sequence of trades may ever risk breaching this floor |
| `risk.operating_buffer_usd`| Institutional Invariant (`AGENTS.md`) | Operating buffer ($4,795.00 USD) | Target minimum equity under worst-case stopout ($20.00 USD buffer above floor) |
| `risk.floor_cushion_usd` | `live_admission.py` (Calculated) | Equity minus Hard Floor ($110.38 USD) | Sizing governor; determines whether new tickets can be staged |
| `risk.stressed_equity_usd` | `live_admission.py` (Modeled) | Equity if ALL active positions and pending orders hit SL | Gating condition; must be >= $4,795.00 USD before staging any new order |
| `risk.total_contingent_stress_usd`| `live_admission.py` (Modeled) | Sum of worst-case dollar losses across open/pending orders | Reserves capital for resting limit orders |
| `capacity.available_slots` | Antigravity Risk Engine (Calculated) | Remaining concurrency slots (up to 4 tickets) | Prevents portfolio over-concentration across correlated instruments |

### B. Macro Calendar & Event Proximity (`macro_calendar`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `blackout_active` | `Data/macro_calendar.json` | Boolean flag for active Tier-1 news release | Hard trading freeze; no orders placed during high-volatility spikes |
| `runway_hours_to_blackout`| `Data/macro_calendar.json` | Time remaining until next Tier-1 catalyst | Sizing & duration filter; trades must have sufficient runway to resolve |
| `event` / `event_release_utc` | Official Central Bank Schedules (BoE, Fed, ECB) | Upcoming high-impact release name & timestamp | Identifies upcoming market-wide volatility drivers |
| `fng_index.value` | Alternative.me API (Live Ingest) | Fear and Greed Index (0-100) | Sentiment indicator; extreme fear (< 25) or greed (> 75) indicates crowding |
| `etf_net_flows.BTC_net_usd_millions` | Farside Investors (Live Web Scrape) | Net daily institutional spot ETF flows | Macro tailwind/headwind confirming multi-day directional bias |

### C. Cross-Universe Institutional Flow (`hyperdash_flow_intelligence`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `active_institutional_twaps` | Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Large algorithmic execution orders running over hours | Identifies persistent structural buying/selling pressure from funds |
| `imminent_liquidation_hazards` | Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Large positions within 2-5% of liquidation price | Identifies high-probability price magnets ready to trigger cascades |
| `recent_confirmed_liquidations`| Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Liquidations executed in the past 1-6 hours | Confirms whether a cascade has already exhausted or is just beginning |
| `whale_trades` | Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Live on-chain trade prints >= 100k USD with wallet addresses | Confirms authentic institutional accumulation or distribution |
| `open_interest_surges` | Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Net changes in derivative positioning | Distinguishes aggressive new positioning from mere short-covering |
| `volume_surges` | Hyperliquid L1 DEX Blockchain (Hyperdash Stream) | Spikes in turnover above 24h baseline | Confirms volume breakout vs low-liquidity drift |

### D. Per-Asset Market Telemetry (`assets_matrix_24.<SYMBOL>`)

#### 1. Execution & Broker Quotes (`quotes` & `execution_specs`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `bid`, `ask`, `mid` | `MT5_L1_TICK` (`mt5.symbol_info_tick()`) | Real-time broker top-of-book pricing | Base price grid for passive limit placement |
| `spread_bps` | `MT5_L1_TICK` (`mt5.symbol_info_tick()`) | Broker spread in basis points | **Friction Gate:** <= 25 bps for Crypto, <= 5 bps for TradFi CFDs |
| `quote_freshness` / `broker_tick_age_s` | `MT5_L1_TICK` & `BrokerClock` | Age of latest broker tick | Staleness filter; must be fresh (< 10s) |
| `tick_size`, `point`, `digits` | `BROKER_MT5_SYMBOL_INFO` (`mt5.symbol_info()`) | Price quantization parameters | Exact limit order price snapping |
| `min_lot`, `step_lot`, `max_lot` | `BROKER_MT5_SYMBOL_INFO` (`mt5.symbol_info()`) | Broker discrete volume rules | Exact risk sizing calculation ($10.00 - $14.50 USD) |
| `stops_level` | `BROKER_MT5_SYMBOL_INFO` (`mt5.symbol_info()`) | Minimum broker distance for pending orders | Ensures limit and stop orders are placeable |

#### 2. Causal Indicators & Regime (`causal_indicators`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `session_vwap_utc` | `LIVE_BRIDGE` (00:00 UTC Causal Reset) | Volume-weighted average price of session | Central gravitational equilibrium axis |
| `vwap_z_score` | `LIVE_BRIDGE` (Calculated) | Standardized distance from Session VWAP | Model 1 Extreme (|Z| >= 2.0 SD) vs Model 2 Pullback (|Z| < 2.0 SD) |
| `session_sigma` | `LIVE_BRIDGE` (Calculated) | Session standard deviation volatility scalar | Volatility-adjusted band width |
| `atr_14` / `atr_pct` | `LIVE_BRIDGE` (14-period Wilder ATR) | Average True Range in dollars and % | Stop-loss distance and order spacing anchor |
| `ema_20`, `ema_50`, `ema_200` | `LIVE_BRIDGE` (800 completed 15m bars) | Exponential moving average hierarchy | Dynamic support/resistance and trend definition |
| `ema_200_slope_3h_pct` | `LIVE_BRIDGE` (Calculated) | 3-hour slope of 200 EMA | Directional trend persistence confirmation |
| `rsi_14` | `LIVE_BRIDGE` (14-period RSI) | Relative Strength Index | Momentum divergence and exhaustion (< 35 oversold, > 65 overbought) |
| `trend_regime` | `decision_gates_v3.py` (`classify_regime()`) | Categorical regime label | `BULLISH`, `BEARISH`, `RANGE_BOUND`, or `UNDEFINED` |

#### 3. Volume Profile & Auction Geometry (`volume_profile`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `poc` | `DERIVED_FROM_MT5_BAR_VOLUME` | Point of Control (highest volume price) | Primary mean-reversion magnet |
| `vah` / `val` | `DERIVED_FROM_MT5_BAR_VOLUME` | Value Area High / Low (70% volume range) | Structural auction boundaries for pullbacks and breakout targets |
| `total_volume` | `DERIVED_FROM_MT5_BAR_VOLUME` | Aggregate session tick volume | Auction participation gauge |

#### 4. Structural Stop Clusters (`structural_stop_clusters`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `total_buy_stops_usd` / `total_sell_stops_usd` | `HYPERDASH_GRAPHQL_STOP_LEVELS` (Hyperliquid) | Aggregate resting stop-loss capital | Market liquidity pool sizing |
| `top_buy_stop_clusters_above` | `HYPERDASH_GRAPHQL_STOP_LEVELS` (Hyperliquid) | Dense buy-stop clusters above market | **Take Profit targets for Longs; sweep zones for reversal shorts** |
| `top_sell_stop_clusters_below` | `HYPERDASH_GRAPHQL_STOP_LEVELS` (Hyperliquid) | Dense sell-stop clusters below market | **Take Profit targets for Shorts; sweep zones for reversal longs** |
| `top_buy_whale_stops` / `top_sell_whale_stops` | `HYPERDASH_GRAPHQL_STOP_LEVELS` (Hyperliquid) | Wallet-identified institutional stop orders | High-impact sweep and exhaustion markers |

#### 5. Reconstructed Liquidation Bands (`reconstructed_liquidations`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `total_long_liquidations_usd` / `total_short_liquidations_usd` | `HYPERDASH_GRAPHQL_LIQUIDATION_LEVELS` | Aggregate potential liquidation capital | Systemic cascade risk / fuel gauge |
| `top_long_cascade_bands_below` | `HYPERDASH_GRAPHQL_LIQUIDATION_LEVELS` | Major long liquidation cascade bands | **Stop Loss shelter (bunker behind these); sweep exhaustion entry** |
| `top_short_squeeze_bands_above` | `HYPERDASH_GRAPHQL_LIQUIDATION_LEVELS` | Major short squeeze liquidation bands | **Take Profit targets (liquidity magnets) for long positions** |
| `top_long_liquidation_whales` / `top_short_liquidation_whales` | `HYPERDASH_GRAPHQL_LIQUIDATION_LEVELS` | Individual whale liquidation trigger levels | Discrete catastrophic cascade triggers |
| `binance_futures_open_interest_contracts` | `BINANCE_FUTURES_OPEN_INTEREST` | Open interest across Binance perpetuals | Structural leverage density in derivatives |

#### 6. Orderbook Depth & Persistent Walls (`orderbook_live_depth`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `binance_mid` / `hyperliquid_mid` | `BINANCE_USDM_FUTURES` & `HYPERLIQUID_L1` | Top-of-book mid price on crypto exchanges | External reference price for basis calculation |
| `venue_basis` & `basis_median` | Live Telemetry Pipeline (Calculated) | MT5 mid minus Binance/Hyperliquid mid | Shifts on-chain walls/stops onto MT5 broker grid |
| `top20_bid_depth_usd` / `top20_ask_depth_usd` | `REAL_BINANCE_FUTURES_L2` (Aggregated Depth) | Cumulative dollar depth in top 20 levels | Passive order absorption capacity |
| `book_imbalance` & `skew_ratio` | `REAL_BINANCE_FUTURES_L2` (Calculated) | Bid vs ask liquidity ratio (-1.0 to +1.0) | Real-time orderbook skew supporting direction |
| `bids_top20` / `asks_top20` | `REAL_BINANCE_FUTURES_L2` (20-level ladder) | Price, size, notional, and cumulative depth | Visualizes resting liquidity shelves |
| `whale_walls_l3` | `REAL_HYPERDASH_WALLET_ATTRIBUTED_L3` | Array of on-chain wallet orders (`0x...`) | Verified resting institutional liquidity backing |
| `l2_wall_levels` | Live Telemetry Daemon (Time-series persistence) | Persistent resting walls (`persist_s`, `presence_frac`) | Filters out algorithmic spoofing; confirms genuine resting orders |

#### 7. Cumulative Volume Delta Buckets (`cvd_1m_buckets`)
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `taker_buy_usd` / `taker_sell_usd` | `BINANCE_FUTURES_AGG_TRADES` | Aggressive market buy vs market sell volume | Measures aggressive market participant aggression |
| `cvd_delta_usd` | `BINANCE_FUTURES_AGG_TRADES` (Calculated) | Net taker buy minus sell dollar delta | Identifies tape absorption (e.g. selling into resting bids) |

#### 8. Multi-Timeframe OHLCV Data
| Parameter | Exact Data Source | Description | Decision Role |
|---|---|---|---|
| `bars_15m_ohlcv` | `MT5_BROKER_COMPLETED_BARS` | Completed 15m candles with OHLCV | Primary trading timeframe structure |
| `htf_1h_ohlcv` / `htf_4h_ohlcv` | `MT5_BROKER_COMPLETED_BARS` | Higher timeframe completed bars | Macro trend alignment and key swing levels |
| `binance_htf_4h_ohlcv` | `BINANCE_FUTURES_PUBLIC_REST` | Binance USDT-M 4h bars | Exchange volume and price action parity check |

---

## 3. The Parameter Coincidence Framework: Synthesizing Entry, SL, and TP

Trading decisions must never rely on a single parameter in isolation. High-probability institutional setups emerge when multiple orthogonal parameters **coincide** at the same price zone.

```
+-----------------------------------------------------------------------------------+
|                           PARAMETER COINCIDENCE MATRIX                            |
+-----------------------------------------------------------------------------------+
|  ENTRY LEVEL         | Supported by:                                              |
|                      |  - Structural shelf (EMA 20/50/200, Session VAL/VAH)       |
|                      |  - Resting L2/L3 Whale Wall (verified on-chain wallet)     |
|                      |  - Psychological round number anchor                       |
|                      |  - CVD absorption (aggressive selling into passive bids)   |
+----------------------+------------------------------------------------------------+
|  STOP LOSS (SL)      | Protected behind:                                          |
|                      |  - Major Reconstructed Long Liquidation Cascade Band      |
|                      |  - Dense Sell-Stop Cluster (the sweep pool)                |
|                      |  - Major Whale Stop Wall                                   |
|                      |  - ATR buffer (minimum 1.0 - 1.5 ATR from entry)           |
|                      |  * NEVER place SL directly AT the stop cluster!            |
+----------------------+------------------------------------------------------------+
|  TAKE PROFIT (TP)    | Targeted directly into:                                    |
|                      |  - Overhead Short Squeeze Liquidation Band                 |
|                      |  - High-density Buy-Stop Cluster (liquidity magnet)        |
|                      |  - Session POC or Value Area High (VAH)                    |
|                      |  - Round number resistance shelf (psychological barrier)   |
+-----------------------------------------------------------------------------------+
```

### A. Constructing the Entry Level
1. **Model 1: Extreme Mean Reversion (`|Z| >= 2.0 SD`)**
   - The setup occurs at statistical extremes where price has flushed 2.0 to 3.5 SD away from Session VWAP.
   - Entry is placed as a **passive limit order** resting directly at a structural support shelf (e.g. daily low, prior day VAH/VAL) coinciding with a **persistent L2/L3 bid whale wall**.
   - CVD confirmation: Aggressive selling delta must show deceleration or positive divergence across 5m/15m/30m windows.

2. **Model 2: VWAP Trend-Continuation Pullback (`|Z| < 2.0 SD`)**
   - The setup occurs in a confirmed directional regime (price > 200 EMA with positive slope, or higher-timeframe trend alignment).
   - Entry is placed as a **passive limit order** resting at a pullback zone: Session VWAP, Value Area Low (VAL), or the 20/50 EMA shelf.
   - Crucial check: Must be backed by resting L2/L3 whale bids within 0.25 - 0.50 ATR of the limit price.

3. **Entry Proximity & Margin Efficiency Rule (`<= 2.0 ATR` Bound for Mandate 1 & Mandate 3)**
   - Every proposed **Mandate 1** new passive limit order AND every **Mandate 3** resting limit order must sit within **`<= 2.0 ATR_14`** of the current MT5 mid price (`|Entry - Mid| <= 2.0 * ATR_14`).
   - Never encumber free margin on deep-fish limit orders (`> 2.0 ATR` away) that require a multi-ATR crash or spike just to reach entry.

### B. Constructing the Stop Loss (SL) — The Liquidity Bunker Principle
- **The Core Mistake to Avoid (Front-Running Trap & Midpoint Trap):**
  * Retail traders place stop losses at obvious support levels, swing lows, or inside liquidation bands.
  * Market makers and institutional sweep algorithms intentionally drive price through these clusters to trigger stops and engineer exit liquidity.
  * *Lesson from Session History (Ticket #18785248 BTC & Cycle 39 SOL Audit):* Placing an SL in front of or directly inside a high-density stop/liquidation band (such as subtracting 0.5 ATR from `mid_price` instead of `min_price`) results in the SL sitting inside the sweep zone.
- **The Institutional SL Rule (`min_price` / `max_price` Boundary Rule & Forced-Fuel Overwhelm Ratio):**
  * Identify the major downside **reconstructed liquidation cascade band** and the primary **sell-stop cluster** (using both `top_*` and `nearest_*` lists in `live_snapshot_latest.json`).
  * **Measure Buffer from the Outer Band Edge (`min_price` for Longs, `max_price` for Shorts) — NEVER from `mid_price`:**
    - For a **Long**: `SL <= band.min_price - (0.25 to 0.50 * ATR_14)`
    - For a **Short**: `SL >= band.max_price + (0.25 to 0.50 * ATR_14)`
  * **Forced-Fuel vs. Resting L3 Defense Overwhelm Ratio (`<= 2.0:1` Cap for Mandate 1 New Setups):**
    - For **Mandate 1 (New Setup Admission)**, compare total forced selling/buying fuel inside the governing `[min_price, max_price]` band (`reconstructed_liquidations` + `structural_stop_clusters` notional) against the total resting (`persist_s >= 180s`, or wallet-continuous `(address, size)` across re-pegs) L3 whale wall defense located **at or inside the Stop Loss boundary** (`price_mt5 >= SL` for Longs; `price_mt5 <= SL` for Shorts — bids below a Long SL cannot defend that stop before it triggers).
    - If forced fuel exceeds in-range resting L3 whale defense by **`> 2.0:1`** on a Mandate 1 candidate, **reject the new setup regardless of R:R**. (Note: this `2.0:1` threshold governs Mandate 1 new-order staging, not automatic Mandate 2 market exits on open positions where anchor wallets remain active).
  * Size the position volume strictly via `mt5.order_calc_profit` / `execution_specs` so that single-ticket risk equals $10.00 - $14.50 USD (0.20% - 0.29% account risk), defending the $4,775.00 USD hard floor, and always report lot-scaled cash risk and lot-scaled cash reward consistently.

### C. Constructing the Take Profit (TP) — The Liquidity Magnet Principle
- **Why Liquidations and Stops Act as Magnets:**
  * In an upward move, short positions have buy-stops resting above key swing highs, and overleveraged shorts face forced liquidation in discrete bands.
  * Price is naturally drawn to these pools because institutional traders require that liquidity to offload long positions without slipping the market.
- **The Institutional TP Rule:**
  * Identify the nearest major **short squeeze liquidation band** or high-density **buy-stop cluster** (using both `top_*` and `nearest_*` lists).
  * Target your Take Profit **directly inside or slightly front-running (5-10 bps before)** this cluster — never *above* the cluster (for Longs) or *below* the cluster (for Shorts), which would require price to fully clear the entire wall to fill your exit.
  * Verify that the target provides at least a **2.0R to 2.5R Risk-to-Reward ratio** relative to the entry and SL.
  * *Worked Example (Ticket #18791527 BTCUSD.pi):* With buy-stop clusters at `84,250 USD` ($6.18M) and `84,350 USD` ($7.04M), setting TP at **`84,300 USD`** front-runs the larger $7.04M cluster at `84,350 USD` by 5.9 bps after absorbing the $6.18M cluster at `84,250 USD`, locking in 2.05R ($23.00 reward on $11.20 risk).

---

## 4. Empirical Lessons Learned from Session Chat History

The following table documents real historical outcomes and forensic audits from our active trading desk, extracting permanent rules:

| Ticket / Asset | Outcome | Root Cause Analysis | Invariant Rule Extracted |
|---|---|---|---|
| **Cycle 43/43B SOL Audit** | Withdrawn Premature Close on `#18795304` -> Kept `HOLD AS-IS` (`commit 21c3acc6`) | Arena Cycle 43 proposed closing `SOLUSD.p #18795304` at market claiming both `0xeac842b2` anchor walls (`3.40M @ 109.09` and `1.74M @ 109.64`) had left the book and eligible defense fell to `0.18M USD`. Independent verification (`Cycle 43B`) proved: (1) `0xeac842b2` never left the book — its byte-identical `31,124 SOL` (`3.40M USD`) and `15,899 SOL` (`1.74M USD`) orders simply re-pegged to `109.11` (`109.22` MT5) and `109.53` (`109.48` MT5), which reset `persist_s` under `WALLET_PRICE_LEVEL_NO_ORDER_ID`; (2) Filtering on the retired `gate_g7_eligible` flag (`presence_frac >= 0.90`) falsely discarded `18–21` walls from `0x5323b922` (`3.22M–3.76M USD` at `persist_s = 1,910s–2,291s`), understating defense by `28.9x` (`9.30M USD` actual at/above SL); (3) The `[109.00, 110.00]` sell-stop band shrank `-22.3%` (`22.05M -> 17.13M USD`). | **Four Permanent Rules:** (1) Track L3 whale wall continuity by `(address, size)` across re-pegs, never static `(address, price)`; (2) Never filter on the retired `gate_g7_eligible` boolean — use `persist_s >= 180s` directly; (3) Count only L3 bids `>= SL` (for Longs) or asks `<= SL` (for Shorts) as ticket defense; (4) `book_imbalance` flips sign across generations and is informational context, whereas `15m/30m CVD` is the stable directional flow anchor. |
| **Cycle 42/42B ETH Audit** | Withdrawn `ETHUSD.pi BUY LIMIT @ 2,495.00` (`commit 7f53c562`) | Arena Cycle 42 proposed `ETHUSD.pi BUY LIMIT 1.06 lots @ 2,495.00` (`SL 2,485.50`, `TP 2,573.00`). Independent verification (`Cycle 42B`) proved 4 flaws: (1) Entry `2,495.00` sat `3.37 ATR` below mid (`2,524.55`), violating the `<= 2.0 ATR` proximity bound and encumbering `1,322.35 USD` (`29.8%` of free margin); (2) 5m/15m/30m CVD were all deeply negative (`-877.8k / -2.13M / -2.46M USD`); (3) `[2,490, 2,500]` held `51.76M USD` of forced liquidation + stop fuel against a single `13.23M USD` L3 bid wall (`3.91:1` overwhelm ratio), and the zone drained within 11 minutes; (4) Reward was quoted unscaled (`78.00` instead of lot-scaled `82.68 USD`). | **Three Permanent Rules (`§3.A`, `§3.B`, `§5`):** (1) Enforce `<= 2.0 ATR` entry proximity on both Mandate 1 new proposals and Mandate 3 resting orders; (2) Reject any Mandate 1 bunker where forced fuel exceeds in-range L3 defense by `> 2.0:1`; (3) Never override negative 5m/15m/30m CVD. |
| **#18791527 BTC Limit** | FILLED & Stopped Out (`-11.20 USD` at `82,590`) | Modified SL from `82,650` to `82,590` (`0.51 ATR` below `min_price = 82,700` of the $32.24M cascade band) and TP from `84,400` to `84,300` (exact `max_price = 84,300` edge of the $6.10M buy-stop cluster at `84,200–84,300`, 106.50 USD below the $21.09M L3 Ask wall). Stopped out at `-11.20 USD` (`-1.00R`) during market-wide flush to `82,590`. | **Gold Standard Model 2 Setup & Exact Risk Control:** Measure SL buffer from `min_price` (not `mid_price`), keep TP inside/at `max_price` of the buy-stop magnet, and size exact lot risk via `mt5.order_calc_profit`. |
| **Cycle 40/40B BTC TP Audit** | Rejected `84,340` TP Raise -> Kept `84,300` | In Cycle 40, Arena proposed raising `#18791527` TP from `84,300` to `84,340` to front-run a $21.09M L3 SELL wall at `84,401–84,406` after the `84,350` buy-stop cluster was pulled. Independent verification caught that `84,340` sat 40 USD *above* `max_price = 84,300` of the $6.10M buy-stop cluster (`84,200–84,300`) in a 600-pt zero-fuel gap right beneath a $21.09M Ask barrier. Arena withdrew `84,340` in Cycle 40B (`commit d55fd2d6`). | **Forced Magnets vs. Passive Barriers:** Buy-stops are forced market-buys (magnets that propel price and supply exit liquidity); L3 SELL walls are passive supply barriers that cap price. Never raise a Long TP above `max_price` of the last buy-stop magnet into an un-fueled gap toward an L3 Ask wall. |
| **Cycle 39 SOL Audit** | Rejected `110.80` Entry / `109.30` SL -> Staged `#18795304` @ `110.15` | Arena proposed `BUY LIMIT @ 110.80` (`SL 109.30`). Independent verification revealed: (1) `109.30` subtracted `0.5 ATR` (`0.20 USD`) from `mid_price = 109.50`, leaving the SL *inside* the `109.00–110.00` ($8.59M stop + $4.02M liq) band; (2) `110.80` sat inside the MT5 spread (`110.77/111.00`), *above* a $2.72M sell-stop cluster at `110.50` and *above* $7.50M of L3 whale bids at `110.23–110.40` while 5m CVD was `-371k USD`. | **Two Permanent Rules:** (1) Always measure SL buffer from `min_price`/`max_price`, never `mid_price`; (2) Never place a Long Limit *above* an immediate nearby sell-stop sweep cluster when the main L3 whale bid wall sits *below* that stop cluster and 1m CVD is negative. |
| **#18785248 BTC Long** | -11.17 USD Loss | Entry was valid, but SL was placed at 83,472 USD—directly inside an intraday sell-stop sweep band. Price wicked down, triggered the stop, and immediately rebounded. | **Never place SL in front of resting stop clusters.** Always position the stop behind the complete liquidation zone with ATR buffer. |
| **#18734917 BTC Long** | +24.00 USD Profit | Bought pullback to 82,600 USD; TP placed at 83,250 USD directly into an overhead short-squeeze band. Price exploded into the band and filled TP cleanly. | **Liquidity magnets deliver clean fills.** Targeting known short squeeze bands yields rapid TP execution with zero slippage. |
| **#18740569 SP500 Long** | -13.00 USD Loss | High index volatility during NY cash open; tight stop within 1.0 ATR was clipped during inter-venue basis rebalancing. | **TradFi CFD volatility requires wider ATR spacing.** Always use at least 1.5 ATR stop distance for equity indices during active sessions. |
| **#18723453 SP500 Long** | +34.00 USD Profit | Model 1 extreme flush entry at Z = -2.4 SD; held through mean reversion to Session VWAP and POC. | **Extreme Z-score flushes (\|Z\| >= 2.0 SD) have massive edge** when entering with passive limit orders at structural exhaustion. |
| **Retail Altcoins** | Banned | Altcoins like DOGE, DOT, ADA, LINK exhibit spreads of 30 to 240 bps on MT5 broker feeds. | **Strict Friction Gate:** Never trade instruments with spread > 25 bps. Confine intraday trading to institutional assets (BTC, ETH, SOL, BNB, Indices, Metals, Major FX). |

---

## 5. Live Pre-Trade Analytical Checklist (Step-by-Step)

Before any order is staged or punched into MetaTrader 5, the desk conducts this rapid 7-point evaluation:

1. **Spread, Friction, Entry Proximity (`<= 2.0 ATR`) & Minimum-Lot Sizability Check:**
   - [ ] Is `quotes.spread_bps` <= 25.0 bps (Crypto) or <= 5.0 bps (TradFi CFDs)?
   - [ ] Is the proposed passive limit `Entry` within **`<= 2.0 * ATR_14`** of current MT5 mid price (both for Mandate 1 new proposals and Mandate 3 resting orders)?
   - [ ] **Minimum-Lot Risk Sizability:** Can the instrument reach the `10.00–14.50 USD` risk band at `>= min_lot` with a `§3.B`-compliant stop distance (rejecting instruments like `NAS100.p` when `min_lot = 0.01` at a compliant stop risks only `2.01 USD`)?
   - *If NO: Discard immediately.*

2. **Floor Cushion, Margin Encumbrance & Risk Budget Defense:**
   - [ ] Is `risk.floor_cushion_usd` >= $20.00 USD?
   - [ ] Does `risk.stressed_equity_usd` remain >= $4,795.00 USD after this order?
   - [ ] Is single-trade risk verified via `mt5.order_calc_profit` strictly between $10.00 and $14.50 USD (0.20% - 0.29%), with both Risk and Reward reported in lot-scaled USD alongside `mt5.order_calc_margin`?
   - *If NO: Reject order to defend capital.*

3. **Macro Catalyst Runway:**
   - [ ] Is `macro_calendar.blackout_active` == False?
   - [ ] Is `macro_calendar.runway_hours_to_blackout` >= 2.0 hours?
   - *If NO: Stand aside until catalyst passes.*

4. **Regime & Strategic Setup Identification:**
   - [ ] Is setup **Model 1** (Extreme Mean Reversion, `|Z| >= 2.0 SD`) or **Model 2** (Trend Pullback, `|Z| < 2.0 SD` with price & 200 EMA slope aligned)?
   - [ ] Is there structural alignment (200 EMA slope, Session VWAP location, or Value Area boundary)?

5. **L3 Persistent Whale Backing (`persist_s >= 180s` or `(address, size)` Continuity) & 15m/30m CVD Alignment:**
   - [ ] For Longs: Is there a **persistent** wallet-attributed L3 bid (`0x...`, `persist_s >= 180s` or verified `(address, size)` continuity across market-maker re-pegs — **never filter on the retired `gate_g7_eligible` boolean**) located **at or above the Stop Loss** (`price_mt5 >= SL`, basis-adjusted via `venue_basis`)?
   - [ ] For Shorts: Is there a **persistent** wallet-attributed L3 ask (`0x...`, `persist_s >= 180s` or verified `(address, size)` continuity) located **at or below the Stop Loss** (`price_mt5 <= SL`)?
   - [ ] **15m/30m CVD Stability & Multi-Generation Confirmation:** Use `15m` and `30m` cumulative CVD windows as the primary directional flow anchor, confirm `5m` CVD and `whale_walls_l3` across `>= 3` consecutive generations, and treat `book_imbalance` as informational context rather than a hard gate (since top-20 L2 depth flips sign across generations).

6. **Liquidation & Stop Cluster Coincidence (SL Bunker, Overwhelm Ratio & TP Magnet):**
   - [ ] **SL Placement (`min_price` / `max_price` edge):** Is the Stop Loss positioned at least `0.25–0.50 ATR` below `min_price` (for Longs) or above `max_price` (for Shorts) of the liquidation/stop band — NEVER measured from `mid_price`?
   - [ ] **Mandate 1 Forced-Fuel Overwhelm Ratio (`<= 2.0:1`):** For any Mandate 1 new setup, is the total forced liquidation + stop cluster notional inside `[min_price, max_price]` `<= 2.0x` the resting L3 whale wall defense located at or inside the Stop Loss (`>= SL` for Longs, `<= SL` for Shorts)?
   - [ ] **TP Placement (5–10 bps front-run):** Is the Take Profit targeted directly inside or 5–10 bps in front of the opposing short-squeeze band or stop cluster (with real notional `>= 0.50M USD`)?
   - [ ] **Risk/Reward:** Is the projected RR >= 2.0R?

7. **Execution Integrity:**
   - [ ] Is the order a **PASSIVE LIMIT ORDER** resting strictly outside the Bid-Ask spread (below Bid for buys or at a true pullback level, above Ask for sells)?
   - [ ] Has broker clock calibration completed (`BrokerClock` tick age fresh)?
   - *If ALL YES: Punch the order autonomously without hesitation.*

---

## 6. Document Governance, 3-Mandate Arena Prompting & 2-Step Antigravity Wake-Up Verification Loop

This document is governed by the Kaizen protocol and is always-on via `.agents/rules/ACTIVE_CONTEXT.md`:

### A. Prompting to Arena.ai — 3 Mandatory Points Considered in Every Cycle (`Terminal/dispatch_comprehensive_wake_up_prompt.py`)
1. **Mandate 1 — Look for New Trading Opportunities**: Screen all 24 assets in `docs/telemetry/live_snapshot_latest.json` line-by-line under this Playbook to identify high-confluence Model 1 (`|Z| >= 2.0 SD` Mean Reversion) or Model 2 (Trend Pullback to VWAP/VAL/VAH/EMA) passive limit order candidates backed by seasoned (`>= 180s`) L3 whale walls, positive L2/CVD absorption, SL outside `min_price`/`max_price` of the bunker, and TP front-running the opposing magnet by 5–10 bps.
2. **Mandate 2 — Look for Active / Running Trades (Logical TP or SL Modification Based on Data)**: Inspect every open MT5 position (`positions_get()`) and check whether TP or SL modification is logically required based on the latest data snapshot (Piecewise Ratchets at `+0.80R` / `+1.50R` / `+2.00R`, tightening SL behind newly formed structural bunkers, adjusting TP to front-run shifted liquidity magnets, or emergency exit if the supporting shelf broke).
3. **Mandate 3 — Look for Unfilled Limit Orders (Wait & Fill vs. Slight Modification vs. Delete)**: Inspect every unfilled pending limit order on MT5 (`orders_get()`) against the latest data snapshot and classify each order with full quantitative reasoning into:
   - **(A) Viable & Wait to be Filled As-Is**: Thesis valid, distance `<= 2.0 ATR`, supporting `>= 180s` whale walls intact, 5m/15m/30m CVD & L2 depth absorbing, SL outside `min_price`/`max_price`, and TP front-running magnet by 5–10 bps.
   - **(B) Slight Modification Required**: Thesis valid, but shifted whale walls, stop clusters (`nearest_*`), or liquidation band boundaries (`min_price`/`max_price`) require modifying Entry, SL, or TP.
   - **(C) Delete / Cancel Immediately**: Thesis invalidated (supporting whale walls pulled/thinned `> 50%`, price drifted `> 2.0 ATR` away, or adverse regime break).

### B. Antigravity Wake-Up to Check Arena.ai Output — 2 Mandatory Steps (`Terminal/arena_completion_daemon.py`)
1. **Step 1 — Use Logical & Quantitative Reasoning to Verify Arena.ai Outputs**: Immediately upon instant daemon wakeup (`Copy` button or `Was this task successful?` `Yes`/`No` banner detected), Antigravity independently verifies every claim, price level, `min_price`/`max_price` bunker edge, `>= 180s` whale wall persistence, 15m/30m CVD flow, and `mt5.order_calc_profit` figure across all 3 mandates against `docs/telemetry/live_snapshot_latest.json` and live MT5.
2. **Step 2 — Same-Cycle Part-B Re-Prompt on Any Logic Flaw (`Cycle NB`)**: If ANY logic does not match the data or if there is ANY flaw in Arena.ai's output, Antigravity immediately re-prompts Arena.ai as **Part 2 of the same cycle (`Cycle NB`)** with the exact telemetry proof and waits via `arena_completion_daemon.py --wait` for Arena's corrected output before executing changes on MT5.
3. **Continuous Persistence**: Every operator feedback point and trade outcome is immediately persisted into this Playbook and `.agents/rules/ACTIVE_CONTEXT.md`, and synchronized across `main` and `arena/537c1eb8-trading-2`.


