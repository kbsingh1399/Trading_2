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

---

## 2. Complete Inventory of Consolidated Telemetry Parameters

The table below catalogs every parameter consolidated in `docs/telemetry/live_snapshot_latest.json`, detailing its source, interpretation, and strategic contribution to trade construction.

### A. Global Risk & Portfolio Level (`account`, `risk`, `capacity`)
| Parameter | Description | Decision Role |
|---|---|---|
| `account.balance` / `equity` | Live MT5 balance and equity in USD | Sets absolute baseline for risk sizing and cushion calculation |
| `account.margin_free` | Available margin for staging new limit orders | Validates leverage headroom (must maintain > 4,000 USD free margin) |
| `risk.hard_floor_usd` | Absolute capital floor ($4,775.00 USD) | Unconditional stop; no sequence of trades may ever risk breaching this floor |
| `risk.operating_buffer_usd`| Operating buffer ($4,795.00 USD) | Target minimum equity under worst-case stopout ($20.00 USD buffer above floor) |
| `risk.floor_cushion_usd` | Equity minus Hard Floor | Sizing governor; determines whether new tickets can be staged |
| `risk.stressed_equity_usd` | Equity if ALL active positions and pending orders hit SL | Gating condition; must be >= $4,795.00 USD before staging any new order |
| `capacity.available_slots` | Remaining concurrency slots (up to 4 tickets) | Prevents portfolio over-concentration across correlated instruments |

### B. Macro Calendar & Event Proximity (`macro_calendar`)
| Parameter | Description | Decision Role |
|---|---|---|
| `blackout_active` | Boolean flag for active Tier-1 news release | Hard trading freeze; no orders placed during high-volatility spikes |
| `runway_hours_to_blackout`| Time remaining until next Tier-1 catalyst | Sizing & duration filter; trades must have sufficient runway to resolve |
| `fng_index.value` | Fear and Greed Index (0-100) | Sentiment indicator; extreme fear (< 25) or greed (> 75) indicates crowding |
| `etf_net_flows.BTC_net_usd_millions` | Net daily institutional ETF inflow/outflow | Macro tailwind/headwind confirming multi-day directional bias |

### C. Cross-Universe Institutional Flow (`hyperdash_flow_intelligence`)
| Parameter | Description | Decision Role |
|---|---|---|
| `active_institutional_twaps` | Large algorithmic execution orders running over hours | Identifies persistent structural buying/selling pressure from funds |
| `imminent_liquidation_hazards` | Large positions within 2-5% of liquidation price | Identifies high-probability price magnets ready to trigger cascades |
| `recent_confirmed_liquidations`| Liquidations executed in the past 1-6 hours | Confirms whether a cascade has already exhausted or is just beginning |
| `whale_trades` | Live on-chain trade prints >= 100k USD with wallet addresses | Confirms authentic institutional accumulation or distribution |
| `open_interest_surges` | Net changes in derivative positioning | Distinguishes aggressive new positioning from mere short-covering |

### D. Per-Asset Market Telemetry (`assets_matrix_24.<SYMBOL>`)

#### 1. Execution & Broker Quotes (`quotes`)
- `bid`, `ask`, `mid`: Real-time broker top-of-book pricing.
- `spread_bps`: Bid-ask spread in basis points. **Rule: Must be <= 25.0 bps for Crypto, <= 5.0 bps for TradFi CFDs.** Retail altcoins with spreads > 30 bps (e.g. DOGE, DOT, ADA) are strictly excluded from intraday limit orders.
- `tick_size`, `min_lot`, `step_lot`: Broker contract specs for exact lot quantization and risk sizing.

#### 2. Causal Indicators & Regime (`causal_indicators`)
- `session_vwap_utc`: The volume-weighted benchmark price reset at 00:00 UTC. The foundational gravitational axis.
- `vwap_z_score`: Standardized distance of current price from Session VWAP.
  * `|Z| >= 2.0 SD`: Model 1 Extreme Mean Reversion territory.
  * `|Z| < 2.0 SD (0.2 to 1.7 SD)`: Model 2 Trend Pullback territory.
- `session_sigma`: Current volatility standard deviation of the session.
- `atr_14`: 14-period Average True Range. Defines minimum stop distance and order spacing.
- `ema_20`, `ema_50`, `ema_200`: Moving average hierarchy defining trend structure, dynamic support/resistance, and pullback boundaries.
- `rsi_14`: Relative Strength Index. Identifies momentum divergence and tape exhaustion (< 35 oversold, > 65 overbought).

#### 3. Volume Profile & Auction Geometry (`volume_profile`)
- `poc` (Point of Control): Price level with highest traded volume of the session. Primary mean-reversion magnet.
- `vah` / `val` (Value Area High / Low): The boundaries containing 70% of the day's auction volume. Pullbacks to VAL in uptrends or VAH in downtrends offer structural entry locations.

#### 4. Structural Stop Clusters (`structural_stop_clusters`)
- `total_buy_stops_usd` / `total_sell_stops_usd`: Aggregate capital waiting in stop-loss orders.
- `top_buy_stop_clusters_above`: Price levels where short traders have placed stops. **Primary Take-Profit targets for Longs; sweep targets for reversal shorts.**
- `top_sell_stop_clusters_below`: Price levels where long traders have placed stops. **Primary Take-Profit targets for Shorts; sweep targets for reversal longs.**
- `top_buy_whale_stops` / `top_sell_whale_stops`: Specific wallet-identified stop orders with massive single-ticket notionals.

#### 5. Reconstructed Liquidation Bands (`reconstructed_liquidations`)
- `top_long_cascade_bands_below`: Price zones where overleveraged longs face forced liquidation. Acting as major downward cascade cascades during selloffs, or deep exhaustion support once swept.
- `top_short_squeeze_bands_above`: Price zones where overleveraged shorts face forced liquidation. Acting as upward squeeze magnets and rocket fuel for rallies.
- `binance_futures_open_interest_contracts`: Derivative positioning depth.

#### 6. Orderbook Depth & Persistent Walls (`orderbook_live_depth`)
- `top20_bid_depth_usd` / `top20_ask_depth_usd`: Aggregate resting liquidity in the top 20 L2 levels.
- `book_imbalance` & `skew_ratio`: Bid-to-ask liquidity ratio. Positive imbalance indicates resting bid backing; negative indicates resting ask overhead.
- `whale_walls_l3`: Individual on-chain wallet orders (`0x...`) with size and price.
- `l2_wall_levels`: Persistent resting walls tracked across time (`persist_s`, `presence_frac`). Confirms genuine resting orders vs spoofing.

#### 7. Cumulative Volume Delta Buckets (`cvd_1m_buckets`)
- `taker_buy_usd` vs `taker_sell_usd`: Aggressive market order flow.
- `cvd_delta_usd`: Net aggressive delta per 1m candle. Identifies absorption (e.g. price dropping into a level while aggressive selling delta weakens or turns positive).

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
