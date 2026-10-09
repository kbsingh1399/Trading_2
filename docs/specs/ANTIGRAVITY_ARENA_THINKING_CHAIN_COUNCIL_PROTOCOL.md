# 🧠 ANTIGRAVITY x ARENA.AI THINKING CHAIN & FORENSIC COUNCIL PROTOCOL (V2.0 HARDENED)

> **CANONICAL SPECIFICATION & MULTI-AGENT RE-ENGAGEMENT BLUEPRINT**
> **Document Identifier:** `docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`
> **Operational Status:** ACTIVE PRODUCTION STANDARD (100% Causal, Empirical & Anti-Lookahead)
> **Target Audience:** Antigravity Coordinators, Subagent Swarms, Arena.ai Council, GPT Astra, Human Operators across all sessions & accounts.

---

## 1. PURPOSE & MISSION CONTINUITY MANDATE

When transitioning between AI models, switching operator accounts, or resuming trading sessions after context truncations, quantitative agents frequently suffer from **Context Amnesia** and **Heuristic Drift**. 

This document defines the **Canonical Thinking Chain, Mathematical Guardrails, Dialectic Review Protocols, and Data Source Provenance Matrix** that govern every trading decision on MetaTrader 5 Account #5064568 (Blueberry Markets). Every agent, subagent, and external council member (Arena.ai, GPT Astra) MUST adhere to this exact reasoning chain before approving, staging, ratcheting, or closing any order.

---

## 2. THE DIALECTIC PHILOSOPHY & COLLABORATIVE CADENCE

We reject both single-agent hallucination and blind sycophancy. Our architecture pairs an external frontier LLM council (**Arena.ai Big Brain**) with a local, multi-agent execution desk (**Antigravity Swarm**):

```
+-----------------------------------------------------------------------------------+
|                           ARENA.AI BIG BRAIN (CDP Bridge)                         |
|  - Ingests 48H Multi-Timeframe Telemetry across 24 Assets (Crypto, CFDs, FX, US)  |
|  - Conducts 4-Persona Debate (Orderflow, Position, Macro, Devil's Advocate)       |
|  - Injected at :25 & :55; completes inference by :29 & :59 (4-minute window)      |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v  [Dialectic Handshake / Challenge Loop]
+-----------------------------------------------------------------------------------+
|                        ANTIGRAVITY 4-SUBAGENT SWARM (Local)                       |
|  1. Orderflow Analyst: Pulls LIVE MT5 Bids/Asks & Binance Futures L2 Orderbook    |
|  2. Position Manager: Queries MT5 IPC, runs Stressed Worst-Case Stopout Sims      |
|  3. Macro Risk Analyst: Audits Data/macro_calendar.json & Session Volatility      |
|  4. Chain Auditor: Runs 360-degree forensic checks & enforces repo parity         |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v  [Fresh Execution Revalidation @ :29/:59]
+-----------------------------------------------------------------------------------+
|                             METATRADER 5 EXECUTION DESK                           |
|  - Passive Maker Limits Only (Priced at verified structural shelves)              |
|  - Cost-Aware Microstructure Ratchets (Inverting broker net PnL for true BE)      |
|  - Unconditional Floor Defense (min(balance, equity) - risk >= 4,795.00 USD)     |
+-----------------------------------------------------------------------------------+
```

### The 4-Minute Inference Cadence & Mandatory Fresh Revalidation Bundle
1. **Prompt Injection (:25 / :55 UTC)**: Antigravity captures live account state and verified telemetry, clears the Arena interface, injects the prompt, and initiates Arena's deliberative debate.
2. **Inference Window (4 Minutes)**: Arena deliberates between :25 and :29 (or :55 and :59).
3. **MANDATORY FRESH EXECUTION REVALIDATION BUNDLE (:29 / :59 UTC)**:
   - Deliberating on a :25/:55 snapshot does NOT make four-minute-old depth or spreads executable at :29/:59 candle close!
   - At :29:00 / :59:00 UTC, before punching any order into MT5, the Antigravity desk MUST fetch a fresh broker tick quote, verify current Binance L2 book depth, recalculate live spreads, and re-check basis.
   - If spread expanded, supporting whale depth thinned by >50%, or market price drifted beyond the 2.0x ATR gate during Arena's inference window, the desk MUST immediately mark the candidate `HOLD_VALIDATION` and stand aside.

### Core Arena Heuristic Traps & Mandatory Antigravity Rebuttals
Arena.ai provides exceptional macro context and pattern recognition, but exhibits six systematic heuristic traps that our local swarm MUST actively audit and challenge:

1. **The Phantom 4,000 USD Free Margin Trap**:
   - *Arena's Bias*: Arena often freezes order staging claiming free margin is below 4,000 USD.
   - *Antigravity Reality*: The account operates on institutional portfolio margin (Margin Level 300% to 800%+). A 0.10 lot SP500 CFD or 0.12 lot USDJPY requires only 70 to 80 USD of margin (less than 2% of available liquidity). The true invariant is NOT arbitrary static cash, but the **Stressed Hard Floor Cushion**!
2. **The Dark Stop-Loss Feed Fallacy**:
   - *Arena's Bias*: Arena frequently rejects setups claiming "stop-loss and liquidation feeds are UNAVAILABLE in public telemetry".
   - *Antigravity Reality*: No regulated broker or perpetual exchange broadcasts hidden client retail stop-loss queues. Institutional quants reconstruct liquidity bands mathematically from Volume Profile (POC, VAH, VAL), swing extremes, and structural R-multiples (+2.0R to +2.5R).
3. **Premature Profit / Panic Cutting**:
   - *Arena's Bias*: Arena frequently urges exiting valid trades at breakeven or small losses during routine pullbacks (e.g. urging exit on BTC @ 82,473 USD right before it surged to our 83,250 USD Take-Profit; urging exit on SP500 @ 7,787.50 USD minutes before the New York opening drive).
   - *Antigravity Reality*: Cutting trades before invalidation violates positive expectancy. Stop losses placed behind structural swing points and EMA shelves MUST be respected unless the supporting orderbook whale wall is pulled by >50%.
4. **Premature Deletion of Resting Maker Limits**:
   - *Arena's Bias*: Arena frequently recommends deleting resting limit orders simply because price drifted 0.5 to 1.0 ATR away.
   - *Antigravity Reality*: A maker limit resting at an institutional EMA shelf within our 2.0x ATR drift gate provides wholesale liquidity. Deleting it forfeits queue priority right before price retraces to fill the order (as proven by our live SP500 fill @ 7,791.50 USD).
5. **The In-Range / Z-Score Entitlement Fallacy**:
   - *Arena's Bias*: Treating an in-range Z-score (`|Z| < 2.0 SD`) as an automatic obligation to enter trend pullbacks.
   - *Antigravity Reality*: `|Z| < 2.0 SD` measures price displacement, NOT continuation versus exhaustion. In-range setups must still prove positive expected value (EV) and favorable lower confidence bounds of net expectancy before admission.
6. **The CFD Spread Exemption Fallacy**:
   - *Arena's Bias*: Assuming maker limit orders escape wide broker spreads entirely.
   - *Antigravity Reality*: In MetaTrader 5 CFDs, Buy Limits fill on broker Ask and exit on Bid. Maker orders do NOT eliminate broker spread or commission. Wide spreads (> 20 bps) impose severe adverse selection and cannot be exempted.

---

## 3. THE 7-STAGE FORENSIC THINKING CHAIN & VERIFICATION CHECKLIST

On EVERY cycle, every agent and subagent MUST step through these 7 verification gates sequentially:

```
[GATE 1: Capital Floor & Cushion] ──> [GATE 2: Dynamic Capacity] ──> [GATE 3: Dual-Engine Regime]
                                                                                │
[GATE 7: Microstructure Ratchet] <── [GATE 6: Structural TP]   <── [GATE 5: Maker Execution] <── [GATE 4: 5-Pillar Stack]
```

### Gate 1: Capital Floor Defense & Stressed Worst-Case Simulation
- **Initial Capital Baseline**: 5,000.00 USD.
- **Hard Capital Floor (G-1)**: 4,775.00 USD (Mandatory Stop: 4.50% / 225.00 USD max drawdown).
- **Operating Safety Buffer**: 4,795.00 USD (Mandatory >= 20.00 USD buffer above floor).
- **Stressed Simulation Math (Unconditional Joint Reservation)**:
  `Total Contingent Risk = Sum(Nominal Risk of all open positions) + Sum(Nominal Risk of all resting pending limits) + Proposed Order Risk`
  `Stressed Worst-Case Equity = min(Account Balance, Account Equity) - Total Contingent Risk`
  `Hard Floor Cushion = Stressed Worst-Case Equity - 4,775.00 USD`
  `Operating Buffer Cushion = Stressed Worst-Case Equity - 4,795.00 USD`
- **Gate Invariant**: If `Operating Buffer Cushion < 0.00 USD` (or `Hard Floor Cushion < 20.00 USD`), ALL new order staging is strictly BLOCKED.
- **Low-Equity Defense**: If current Equity < 4,800.00 USD, per-trade risk is hard-capped at 10.00 USD.

### Gate 2: Dynamic Capacity Policy
- **Concurrency Cap**: Up to **4 concurrent FILLED positions** across orthogonal asset clusters (Forex, Commodities, US Equities, Crypto).
- **Joint Pending Reservation**: Resting pending orders do not count as filled positions, BUT their contingent downside risk is reserved identically to filled positions under Gate 1. Total active tickets (filled + resting pending) cannot exceed 4 unless individual tickets are risk-neutralized.
- **Risk Budget Recirculation**: Moving an active position's stop to Phase 0 Breakeven drops its downside risk to 0.00 USD, immediately recirculating its risk budget to stage the next setup into vacant capacity.

### Gate 3: Dual-Engine Strategy Dialectic & Volatility-Normalized Retracements
Every scan must explicitly evaluate BOTH engines:
- **Engine 1 (Extreme Mean Reversion)**:
  * Condition: Price stretched to `|VWAP Z-Score| >= 2.0 SD` with RSI exhaustion (`RSI < 30` for Longs, `RSI > 70` for Shorts) and taker CVD divergence.
  * Entry: Passive maker limit resting at outer SD band / discount sweep level.
- **Engine 2 (Trend-Following Momentum Pullbacks)**:
  * Condition: `|VWAP Z-Score| < 2.0 SD` in an established trend (`200 EMA Slope > 0` for Bullish, `< 0` for Bearish).
  * **Causal Retracement Normalization**: Rather than a rigid universal 0.10–0.60 ATR band, shelf distances are normalized by `Price x Forecast Volatility` (Garman-Klass variance or completed-bar realized volatility).
  * **No In-Range Entitlement**: In-range Z measures displacement, not continuation. Admitting an Engine 2 setup requires positive lower confidence bound of net expectancy:
    `Entry Value = P(fill) x E(Net PnL | fill) - Tail Risk Penalty - Capacity Opportunity Cost > 0`

### Gate 4: The 5-Pillar Confluence Stack & Positive Expected Value (EV)
Every admitted candidate must satisfy all 5 pillars:
1. **VWAP Geometry**: Session VWAP position, Value Area alignment, and Z-score qualification.
2. **CVD Orderflow Absorption**: 1m, 5m, and 15m taker CVD delta showing seller exhaustion at bid shelves (for Longs) or buyer exhaustion at ask shelves (for Shorts).
3. **Binance Futures L2 Orderbook Depth & Whale Persistence**:
   - Top-20 depth imbalance >= 1.25x favoring trade direction.
   - Clustered resting whale walls >= 150,000 USD with persistent observation backing the entry shelf.
4. **Reconstructed Liquidation Cascade Pools**:
   - Formulated by differencing contract quantities before valuation (eliminating price-inflation artifacts).
   - Longs: Overhead Short Squeeze Band (`short_squeeze_band`).
   - Shorts: Downside Long Flush Band (`long_flush_target`).
5. **Structural Stop Clusters & Volume Profile**:
   - Entry anchored at Point of Control (POC), Value Area High (VAH), Value Area Low (VAL), or prior swing pivots.
- **Probability Score vs Expected Value Mandate**:
  A high win-probability score is insufficient if accompanied by an asymmetric negative tail. Every trade MUST demonstrate positive conservative EV:
  `Expected Net Utility = P(win) x Net Gain - P(loss) x Max Stressed Loss - Frictions > 0`

### Gate 5: Microstructure Execution Hygiene & Broker CFD Mechanics
- **Passive Maker Limit Orders Only**: Zero market/taker orders for entries. We provide liquidity at designated prices and avoid aggressive slippage.
- **Broker CFD Spread Realities**:
  * In MT5 CFDs, Buy Limits fill on broker Ask and exit on Bid; Sell Limits fill on Bid and exit on Ask.
  * Maker limit orders do NOT eliminate the broker spread.
  * Maximum allowable spread gate: **20.00 bps**. Any asset with spread > 20 bps (e.g. illiquid altcoins) is strictly quarantined.
- **2.0x ATR Drift Gate**: The limit order must rest within 2.0x ATR of current market price. If price moves beyond 2.0x ATR or supporting whale depth thins by >50%, cancel the pending order immediately to unencumber margin.
- **Fresh Execution Revalidation**: Verify tick Bid/Ask, broker spread, and L2 depth at :29/:59 immediately prior to order submission.

### Gate 6: Structural Take-Profit Anchoring Mandate
- **No Arbitrary Fixed Targets**: Take-Profit must NEVER be set to an arbitrary distance.
- **Longs**: TP anchored directly inside the nearest overhead Short Squeeze Band, Premium Stop Sweep, or Ask Whale Wall.
- **Shorts**: TP anchored directly inside the nearest downside Long Flush Band, Discount Stop Sweep, or Bid Whale Wall.
- **Reward-to-Risk**: TP must yield >= +2.0R to +2.5R relative to the structural stop loss.
- **Nominal Risk Cap**: 10.00 to 14.50 USD per trade (0.20% to 0.29% of 5,000 USD capital).

### Gate 7: Cost-Aware Piecewise Ratchet Lifecycle Sentry
- **Net Breakeven Inversion Mandate**:
  * A nominal +0.15R stop lock does NOT guarantee net breakeven under full friction models unless `R / Entry >= 2.73%`.
  * Compute the Phase 0 breakeven stop price by inverting broker-valued net PnL:
    `Stop Price = Price where (Broker Gross PnL - Broker Commission - Swap - Half Spread) >= +0.50 USD guaranteed net credit`
- **Phase 0 (Cost-Aware Breakeven Lock)**: At **+0.70R to +0.80R gain**, ratchet Stop Loss via MT5 IPC to the calculated Net Breakeven Price. Downside risk drops to 0.00 USD, liberating risk budget for new deployments.
- **Phase 1 (Profit Lock)**: At **+1.50R gain**, ratchet Stop Loss to **Entry +0.80R**.
- **Phase 2 (Trailing Ratchet)**: At **+2.00R gain**, trail Stop Loss behind the 15m EMA20 shelf.
- **Target Exit**: Full Take-Profit at **+2.00R to +2.50R**.
- **Time Decay Sentry**: If trade fails to gain +0.20R within 24 bars (6 hours), execute an orderly market exit.

---

## 4. 0–100 EVIDENCE-QUALITY ARBITRATION RUBRIC

To eliminate subjective debate between Arena.ai and Antigravity, every candidate setup is evaluated on this formal 100-point rubric:

| Dimension | Weight | Scoring Criteria |
|---|---|---|
| **1. Data Provenance & Freshness** | 20 pts | Live tick feed <= 5s (10 pts), Binance L2 snapshot <= 10s (5 pts), 0 nulls & monotonic parquet (5 pts). Deduct 20 pts if cached/stale. |
| **2. Structural Thesis & Invalidation** | 20 pts | Clear EMA shelf / Volume Profile POC anchor (10 pts), unambiguous structural invalidation level (10 pts). |
| **3. Conditional Expected Utility & EV** | 20 pts | Reward:Risk >= 2.0R (10 pts), Positive Lower Confidence Bound Net EV > 0 USD (10 pts). Deduct 15 pts if negative skew. |
| **4. Capital Floor Defense & Capacity** | 20 pts | Stressed cushion >= +20 USD above 4,775 USD (10 pts), Stressed cushion >= +0 USD above 4,795 USD (5 pts), Capacity slot available (5 pts). |
| **5. Execution Hygiene & Broker Spread** | 10 pts | Broker spread <= 5.0 bps (10 pts), 5.0–15.0 bps (5 pts), > 20.0 bps (0 pts & VETO). Maker limit within 2.0x ATR. |
| **6. Macro & Session Timing** | 10 pts | No Tier-1 macro event within 15m (5 pts), Active liquid trading session / normal volatility (5 pts). |

### Arbitration Action Thresholds:
- **Score >= 80 pts + All Hard Gates Pass**: `APPROVED` -> Stage passive limit order live into MT5.
- **Score 60–79 pts**: `STANDBY` -> Maintain on watchlist; do not stage until missing evidence is established.
- **Score < 60 pts OR Any Hard Failure**: `STAND ASIDE / REJECTED` -> No order permitted.
- **Hard Failure Vetoes (Instant Rejection regardless of score)**:
  * Operating buffer cushion < 0.00 USD (or Hard floor cushion < 20.00 USD).
  * Broker spread > 20.00 bps.
  * Telemetry or tick quote age > 60 seconds.
  * Tier-1 macro blackout active within 15 minutes.

---

## 5. COMPLETE DATA SOURCE PROVENANCE & VERIFICATION MATRIX

Every signal, metric, and decision MUST trace back to a verified, live data feed. The table below outlines all 8 primary data sources and their operational parameters:

| # | Data Source Name | Provider / Endpoint | Update Cadence | Latency / Age | Verification Method | Honest Boundaries & Limitations |
|---|---|---|---|---|---|---|
| **1** | **MT5 Native Broker Feed** | Blueberry Markets Account #5064568 via python `MetaTrader5` IPC | Tick-by-tick / polled 100 ms | 3.65 ms | `mt5.initialize()`, `account_info()`, `symbol_info_tick()` | Primary truth for account balance, equity, margin, bid/ask, and execution fills. Demo environment running on live server bridge. |
| **2** | **Binance Futures L2 Orderbook** | REST `fapi.binance.com/fapi/v1/depth?limit=20` & WebSocket `@depth20@100ms` | 100 ms | 178–350 ms | `ZeroCostDataFactory.fetch_binance_l2_depth()` | Anonymous top-20 orderbook depth. Measures resting liquidity; does NOT provide wallet-attributed L3 identities. |
| **3** | **Binance Forced Liquidations** | WebSocket `wss://fstream.binance.com/ws/!forceOrder@arr` | Real-time event stream | < 500 ms | Handled in `streams.py` by `ZeroCostDataFactory` | Realized public liquidations on Binance. Does NOT expose dark private margin levels of individual market participants. |
| **4** | **Multi-Asset Parquet Archives** | 24 assets in `Data/Candles/{symbol}_15m.parquet` | Continuous 15m bar append | <= 0.38 hours | `chain_verification_360.py` (`audit_parquet_integrity`) | 800 bars per asset, 0 nulls, 100% strictly monotonic timestamps. Used for EMA, ATR, RSI, VWAP feature generation. |
| **5** | **Macro Economic Calendar** | `Data/macro_calendar.json` cross-checked with BLS & Fed | Scheduled releases | Verified Oct 5 (runway: 120h) | Direct file inspection & event proximity checks | Verified US CPI (Oct 14) and FOMC (Oct 28) dates. 15-minute pre/post event blackout on affected currency/index clusters. |
| **6** | **Live Telemetry Snapshot** | `docs/telemetry/live_snapshot_latest.json` | Generated every 60s by Git Daemon | <= 60 seconds | `Telemetry_Provenance.py` digest check | Carries immutable receipt timestamp, MT5 account state, active tickets, and pending orders. |
| **7** | **AST Knowledge Graph** | `graphify-out/graph.json` | Updated on code modification | Static AST index | `python -m graphify query` | 8,200+ nodes, classes, call-flows. Queried with zero API tokens to prevent context amnesia. |
| **8** | **Reconstructed Stop Clusters & Liquidation Bands** | Mathematical models in `Terminal/stop_clusters.py` | Computed per candle | Real-time | Contract volume differencing & Volume Profile POC | Probabilistic latent-liquidity estimates. Private broker retail stop-loss queues are dark and never published. |

---

## 6. AST KNOWLEDGE GRAPH INTEGRATION & ZERO-TOKEN QUERYING VIA /GRAPHIFY

To eliminate context bloating, prevent hallucination, and preserve model context windows across long-running sessions, agents MUST query the repository's pre-indexed Abstract Syntax Tree (AST) knowledge graph rather than ingesting entire raw python modules:

- **Graph Storage**: `graphify-out/graph.json` (contains 8,200+ semantic nodes, classes, call-flows, and dependencies).
- **Query Command**:
  ```bash
  python -m graphify query "<concept or symbol>" --budget 300
  ```
- **Focused Node Explanation**:
  ```bash
  python -m graphify explain "<class_or_function_name>"
  ```
- **Relationship Path Finding**:
  ```bash
  python -m graphify path "<node_A>" "<node_B>"
  ```
- **Always Keep AST Synchronized**: Whenever modifying core strategy or terminal code, update the graph with zero API cost:
  ```bash
  python -m graphify update .
  ```

---

## 7. DUAL-REPO PARITY & EPHEMERAL DISCIPLINE

1. **Dual-Repo Synchronization**:
   - Primary Workspace: `C:\Users\SIGMA\Documents\Trading_2`
   - Secondary Mirror: `C:\Users\SIGMA\Documents\Trading_2\Engine_2`
   - Run `python .agents/scripts/verify_and_sync_agents.py` to ensure byte-for-byte parity across `.agents`.
2. **Ephemeral File Cleanliness**:
   - Zero scratch litter in root or `Engine/`.
   - Temporary test or debug scripts must be purged immediately after execution.

---

## 8. ACTIVE PERFORMANCE SCORECARD & OPERATIONAL STATUS

- **Account Baseline**: 5,000.00 USD.
- **Current Realized PnL**: **+84.05 USD Net Realized Cash Banked** across 17 completed trades (**64.7% Win Rate: 11 Wins / 6 Losses**).
- **Capital Floor**: 4,775.00 USD. Current Balance: 4,896.55 USD.
- **Current Hard Floor Cushion**: **+110.92 USD** (Defends floor under simultaneous stopout of all contingent book exposure).
- **Operating Buffer Cushion**: **+90.92 USD** above the 4,795.00 USD operating buffer.
- **Active Capacity**: 0 Filled Positions / 1 Resting Pending Limit (`USDJPY.pi` BUY LIMIT @ 158.180 USD, risk: 10.63 USD).
- **Free Margin**: **4,896.55 USD** (100% Cash Reserves | 4 Liberated Capacity Slots).

---
*Authorized by Antigravity Quantitative Command & Registered into `.agents/rules/ACTIVE_CONTEXT.md`.*
