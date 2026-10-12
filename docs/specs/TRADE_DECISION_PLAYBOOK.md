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
   - CVD confirmation: Aggressive selling delta must show deceleration or positive divergence.

2. **Model 2: VWAP Trend-Continuation Pullback (`|Z| < 2.0 SD`)**
   - The setup occurs in a confirmed directional regime (price > 200 EMA with positive slope, or higher-timeframe trend alignment).
   - Entry is placed as a **passive limit order** resting at a pullback zone: Session VWAP, Value Area Low (VAL), or the 20/50 EMA shelf.
   - Crucial check: Must be backed by resting L2/L3 whale bids within 0.25 - 0.50 ATR of the limit price.

### B. Constructing the Stop Loss (SL) — The Liquidity Bunker Principle
- **The Core Mistake to Avoid (Front-Running Trap):**
  * Retail traders place stop losses at obvious support levels or swing lows.
  * Market makers and institutional sweep algorithms intentionally drive price through these clusters to trigger stops and engineer exit liquidity.
  * *Lesson from Session History (Ticket #18785248 BTC):* Placing an SL in front of or directly inside a high-density stop cluster results in being swept before the true market reversal.
- **The Institutional SL Rule:**
  * Identify the major downside **reconstructed liquidation cascade band** and the primary **sell-stop cluster**.
  * Place the SL **behind** this entire liquidation pool (at least 0.5 - 1.0 ATR below the lowest liquidation band).
  * This ensures that if the market executes a liquidity sweep, your position survives the flush and catches the sharp recovery.
  * Size the position volume strictly so that `volume * (entry - SL)` equals $10.00 - $14.50 USD (0.20% - 0.29% account risk), defending the $4,775.00 USD hard floor.

### C. Constructing the Take Profit (TP) — The Liquidity Magnet Principle
- **Why Liquidations and Stops Act as Magnets:**
  * In an upward move, short positions have buy-stops resting above key swing highs, and overleveraged shorts face forced liquidation in discrete bands.
  * Price is naturally drawn to these pools because institutional traders require that liquidity to offload long positions without slipping the market.
- **The Institutional TP Rule:**
  * Identify the nearest major **short squeeze liquidation band** or high-density **buy-stop cluster** (e.g. >= 5M USD notional).
  * Target your Take Profit **directly inside or just before (5-10 bps front-run)** this cluster.
  * Verify that the target provides at least a **2.0R to 2.5R Risk-to-Reward ratio** relative to the entry and SL.
  * Align with psychological round numbers (e.g., target 84,400 USD just below the major 84,500 USD round number and 84,450 USD short squeeze band).

---

## 4. Empirical Lessons Learned from Session Chat History

The following table documents real historical outcomes from our active trading desk, extracting permanent rules:

| Ticket / Asset | Outcome | Root Cause Analysis | Invariant Rule Extracted |
|---|---|---|---|
| **#18791527 BTC Limit** | LIVE Resting | Staged BUY LIMIT at 83,150 USD backed by 200 EMA & 5.9M USD stop shelf; SL at 82,650 USD safely behind 32.4M USD liquidation cascade pool; TP at 84,400 USD targeting 7.8M USD buy-stop pool. | **Gold Standard Model 2 Setup:** Strict passive limit order anchored on structural support with SL in the liquidation bunker and TP at the liquidity magnet. |
| **#18785248 BTC Long** | -11.17 USD Loss | Entry was valid, but SL was placed at 83,472 USD—directly inside an intraday sell-stop sweep band. Price wicked down, triggered the stop, and immediately rebounded. | **Never place SL in front of resting stop clusters.** Always position the stop behind the complete liquidation zone with ATR buffer. |
| **#18734917 BTC Long** | +24.00 USD Profit | Bought pullback to 82,600 USD; TP placed at 83,250 USD directly into an overhead short-squeeze band. Price exploded into the band and filled TP cleanly. | **Liquidity magnets deliver clean fills.** Targeting known short squeeze bands yields rapid TP execution with zero slippage. |
| **#18740569 SP500 Long** | -13.00 USD Loss | High index volatility during NY cash open; tight stop within 1.0 ATR was clipped during inter-venue basis rebalancing. | **TradFi CFD volatility requires wider ATR spacing.** Always use at least 1.5 ATR stop distance for equity indices during active sessions. |
| **#18723453 SP500 Long** | +34.00 USD Profit | Model 1 extreme flush entry at Z = -2.4 SD; held through mean reversion to Session VWAP and POC. | **Extreme Z-score flushes (|Z| >= 2.0 SD) have massive edge** when entering with passive limit orders at structural exhaustion. |
| **Retail Altcoins** | Banned | Altcoins like DOGE, DOT, ADA, LINK exhibit spreads of 30 to 240 bps on MT5 broker feeds. | **Strict Friction Gate:** Never trade instruments with spread > 25 bps. Confine intraday trading to institutional assets (BTC, ETH, SOL, BNB, Indices, Metals, Major FX). |

---

## 5. Live Pre-Trade Analytical Checklist (Step-by-Step)

Before any order is staged or punched into MetaTrader 5, the desk conducts this rapid 7-point evaluation:

1. **Spread & Friction Check:**
   - [ ] Is `quotes.spread_bps` <= 25.0 bps (Crypto) or <= 5.0 bps (TradFi CFDs)?
   - *If NO: Discard immediately.*

2. **Floor Cushion & Risk Budget Defense:**
   - [ ] Is `risk.floor_cushion_usd` >= $20.00 USD?
   - [ ] Does `risk.stressed_equity_usd` remain >= $4,795.00 USD after this order?
   - [ ] Is single-trade risk capped strictly between $10.00 and $14.50 USD (0.20% - 0.29%)?
   - *If NO: Reject order to defend capital.*

3. **Macro Catalyst Runway:**
   - [ ] Is `macro_calendar.blackout_active` == False?
   - [ ] Is `macro_calendar.runway_hours_to_blackout` >= 2.0 hours?
   - *If NO: Stand aside until catalyst passes.*

4. **Regime & Strategic Setup Identification:**
   - [ ] Is setup **Model 1** (Extreme Mean Reversion, `|Z| >= 2.0 SD`) or **Model 2** (Trend Pullback, `|Z| < 2.0 SD`)?
   - [ ] Is there structural alignment (200 EMA slope, Session VWAP location, or Value Area boundary)?

5. **L2/L3 Orderbook & Whale Backing:**
   - [ ] For Longs: Is there a persistent resting bid wall or wallet-attributed L3 bid within 0.5 ATR below entry?
   - [ ] For Shorts: Is there a persistent resting ask wall or wallet-attributed L3 ask within 0.5 ATR above entry?
   - [ ] Does CVD taker delta confirm exhaustion (decelerating adverse flow)?

6. **Liquidation & Stop Cluster Coincidence (SL & TP Construction):**
   - [ ] **SL Placement:** Is the proposed Stop Loss positioned safely **behind** the nearest major liquidation cascade band and sell/buy stop cluster?
   - [ ] **TP Placement:** Is the proposed Take Profit targeted directly **into** an overhead short-squeeze band or high-density stop cluster?
   - [ ] **Risk/Reward:** Is the projected RR >= 2.0R (preferably 2.5R+)?

7. **Execution Integrity:**
   - [ ] Is the order a **PASSIVE LIMIT ORDER** resting strictly below ask (for buys) or above bid (for sells)?
   - [ ] Has broker clock calibration completed (`BrokerClock` tick age fresh)?
   - *If ALL YES: Punch the order autonomously without hesitation.*

---

## 6. Document Governance & Continuous Improvement

This document is governed by the Kaizen protocol. Whenever a live trade resolves (profit or loss), or new microstructure insights are uncovered:
- Update Section 4 with the trade ticket, outcome, and new lessons.
- Refine Section 3 parameters and threshold heuristics.
- Ensure bidirectional synchronization across `main` and `arena/537c1eb8-trading-2`.
