# 🧠 ANTIGRAVITY x ARENA.AI THINKING CHAIN & FORENSIC COUNCIL PROTOCOL (V3.0 PRODUCTION HARDENED)

> **CANONICAL SPECIFICATION & MULTI-AGENT RE-ENGAGEMENT BLUEPRINT**  
> **Primary Locations**:  
> - `Data/Manditory/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`  
> - `Data/Manditory/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`  
> - `Data/Manditory/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`  
> **Operational Status**: ACTIVE PRODUCTION STANDARD (100% Causal, Empirical & Anti-Lookahead)  
> **Target Audience**: Antigravity Coordinators, Subagent Swarms, Arena.ai Council, GPT Astra, Human Operators across all sessions & accounts.  
> **Master Data Warehouse**: `Data/DataBase_Trading.xlsx` (All 33 Canonical Production Worksheets)  
> **Autonomous Cadence**: Joint 3-Entity Completion Lifecycle with Clean 20-Minute Relative Separation (`T_finish + 20 min`) + 30-Minute Watchdog Sentry Cron (`0,30 * * * *` at :00, :30 UTC).

---

## 1. PURPOSE & MISSION CONTINUITY MANDATE

When transitioning between AI models, switching operator accounts, or resuming trading sessions after context truncations, quantitative agents frequently suffer from **Context Amnesia** and **Heuristic Drift**. 

This document defines the **Canonical Thinking Chain, Mathematical Guardrails, Dialectic Review Protocols, and 33-Sheet Data Source Provenance Matrix** that govern every trading decision on MetaTrader 5 Account #5064568 (Blueberry Markets). Every agent, subagent, and external council member (Arena.ai, GPT Astra) MUST adhere to this exact reasoning chain before approving, staging, ratcheting, or closing any order.

---

## 2. THE DIALECTIC PHILOSOPHY & COLLABORATIVE CADENCE

We reject both single-agent hallucination and blind sycophancy. Our architecture pairs an external frontier LLM council (**Arena.ai Big Brain**) with a local, multi-agent execution desk (**Antigravity 4-Subagent Swarm**), grounded in the **33-sheet canonical master Excel data warehouse (`Data/DataBase_Trading.xlsx`)** across the full **156-asset universe**:

```
+----------------------------------------------------------------------------------------------------+
|                                  ARENA.AI BIG BRAIN (CDP Bridge)                                   |
| - Ingests 33-Sheet Master Excel Data Warehouse (DataBase_Trading.xlsx) across all 156 Assets       |
| - Dual Mandate: Affirmative Candidate Discovery across all 156 Instruments AND Adversarial Red-Team|
| - Injected via Chrome CDP port 9222 on joint autonomous cycle trigger (T_finish + 20 min)          |
| - Deliberates with deep Linux terminal reasoning; auto-harvested by arena_completion_daemon.py     |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
                                                  v [Dialectic Handshake / Challenge Loop]
+----------------------------------------------------------------------------------------------------+
|                               ANTIGRAVITY 4-SUBAGENT SWARM (Local)                                 |
| 1. Orderflow Analyst: CoinGlass & Hyperdash Liq/Stops (Sheets 10-18, 22-26), CVD zc_div > 0.8,     |
|    Resting Whales >= $100K (persist >= 180s), 156-Asset Scanner, Mandatory 10-Point Checklist.     |
| 2. Position Manager: Queries MT5 IPC, exact order_calc_profit risk sizing ($15-$25 USD),           |
|    frozen R0 ratchets (Early-BE +0.75R), stressed solvency preserving $4,775 floor & $4,795 buffer.|
| 3. Macro Risk Analyst: Audits 19_Calendar (Sheet 28) & macro_calendar.json, ETF netflows           |
|    (Sheets 00-01), CEX netflow (Sheet 02), 19_News (Sheet 27), 21:30-22:30 UTC FX rollover gate.   |
| 4. Excel Data Quality Auditor: Audits all 33 sheets of DataBase_Trading.xlsx, verifies 0 formula   |
|    errors, <= 15m freshness, unmerged Row 1 headers in Sheet 33 (20_Auction_Market_Structure).     |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
                                                  v [Fresh Execution Revalidation @ Candle Close]
+----------------------------------------------------------------------------------------------------+
|                                    METATRADER 5 EXECUTION DESK                                     |
| - Passive Maker Limits Only (BUY_LIMIT / SELL_LIMIT, priced at verified structural shelves)        |
| - Dynamic Spread Friction Budgeting (Efficiency Ratio: Spread Points / TP Distance Points <= 15%)  |
| - Multi-Asset Pristine Confluence Risk Rights ($25.00 to $35.00 USD) across ALL 156 Assets         |
| - Fluid 4-Slot Capacity (Any combination of crypto, forex, indices, metals) + Uncapped Limits      |
| - Inviolable Solvency Defense: Stressed Equity = Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD     |
+----------------------------------------------------------------------------------------------------+
```

### The 20-Minute Cadence & Mandatory Fresh Revalidation Bundle
1. **Autonomous Tri-Track Cycle Execution & 20-Minute Post-Completion Delay**: Cycles trigger with a strict 20-minute separation after all 3 entities (Antigravity Fleet, Arena.ai, Z.ai) finish processing, supervised by a 30-minute watchdog sentry (`0,30 * * * *`).
2. **Simultaneous Dual-Track Dispatch**:
   - **Track A**: Antigravity invokes the 4-subagent swarm (`Model='flash'`) with full Tier 2 Big Prompts citing `STANDARDIZED_TRADING_DECISION_CHAIN.md`.
   - **Track B**: Antigravity dispatches the surgical dual-mandate prompt to Arena.ai via Chrome CDP on port 9222.
3. **MANDATORY FRESH EXECUTION REVALIDATION BUNDLE**:
   - Deliberating on a snapshot does NOT make minutes-old depth or spreads executable at candle close!
   - Immediately prior to punching any order into MT5, the desk MUST fetch fresh broker tick quotes (`symbol_info_tick`), verify current L2 orderbook depth, recalculate live spreads, and re-check basis.
   - If spread expanded beyond the 15% efficiency gate, supporting whale depth thinned by > 50%, or market price drifted beyond the 2.0x ATR gate during deliberation, the desk MUST immediately mark the candidate `HOLD_VALIDATION` and stand aside.

### Core Arena Heuristic Traps & Mandatory Antigravity Rebuttals
Arena.ai provides exceptional macro context and pattern recognition, but exhibits systematic heuristic traps that our local swarm MUST actively audit and challenge:

1. **The Phantom 4,000 USD Free Margin Trap**:
   - *Arena's Bias*: Arena often freezes order staging claiming free margin is below 4,000 USD.
   - *Antigravity Reality*: The account operates on institutional portfolio margin (Margin Level 300% to 800%+). A 0.02 lot NAS100 or 0.18 lot USDJPY requires only 15 to 40 USD of margin. The true invariant is NOT arbitrary static cash, but the **Stressed Operating Buffer Cushion (>= 4,795.00 USD)**!
2. **The Missing Calendar Row Misdiagnosis**:
   - *Arena's Bias*: Arena frequently rejects setups claiming "the calendar jumps from Oct 20 to Oct 23, macro clearance cannot be asserted for Oct 22".
   - *Antigravity Reality*: Economic calendars only list days with scheduled macroeconomic releases. The absence of red-folder events on Thursday, Oct 22 means there are **ZERO active macro event blackouts**, providing a completely clear runway for trading!
3. **Premature Profit / Panic Cutting**:
   - *Arena's Bias*: Arena frequently urges exiting valid trades at breakeven or small losses during routine pullbacks.
   - *Antigravity Reality*: Cutting trades before invalidation violates positive expectancy. Stop losses placed behind structural swing points, whale bunkers, and EMA shelves MUST be respected unless the supporting orderbook whale wall pulls.
4. **Premature Deletion of Resting Maker Limits**:
   - *Arena's Bias*: Arena frequently recommends deleting resting limit orders simply because price drifted 0.5 to 1.0 ATR away.
   - *Antigravity Reality*: A maker limit resting at an institutional shelf within our 2.0x ATR drift gate provides wholesale liquidity. Deleting it forfeits queue priority right before price retraces to fill the order.
5. **The In-Range / Z-Score Entitlement Fallacy**:
   - *Arena's Bias*: Treating an in-range Z-score (`|Z| < 2.0 SD`) as an automatic obligation to enter trend pullbacks.
   - *Antigravity Reality*: `|Z| < 2.0 SD` measures price displacement, NOT continuation versus exhaustion. In-range setups must still prove positive expected value (EV) and favorable lower confidence bounds of net expectancy before admission.
6. **The Rigid Spread Gate Fallacy**:
   - *Arena's Bias*: Disqualifying setups based on rigid arbitrary bps cutoffs regardless of target reward.
   - *Antigravity Reality*: Spread friction must be evaluated dynamically via the **Efficiency Ratio** ($\text{Spread Points} / \text{TP Distance Points} \le 15\%$). If a trade targets 300 points, a 15-point spread takes only 5% of profit and is completely viable.
7. **The Cross-Venue Basis Proximity Illusion**:
   - *Arena's Bias*: Measuring whale wall proximity directly without adjusting for cross-venue basis (`mid_mt5 - mid_binance`).
   - *Antigravity Reality*: Council must compute venue-adjusted distance (`side * (mid_binance - wall_binance) / atr`), distinguishing venue basis skew from absent whale depth.

---

## 3. THE 7-STAGE FORENSIC THINKING CHAIN & VERIFICATION CHECKLIST

On EVERY cycle, every agent and subagent MUST step through these 7 verification gates sequentially:

```
[GATE 1: Capital Floor & Cushion] ──> [GATE 2: Dynamic Capacity] ──> [GATE 3: Causal Auction Regime]
                                                                                │
[GATE 7: Dynamic Ratchet Sentry]  <── [GATE 6: Structural TP]   <── [GATE 5: Maker Execution] <── [GATE 4: 5-Pillar Confluence]
```

### Gate 1: Capital Floor Defense & Stressed Worst-Case Simulation
- **Initial Capital Baseline**: 5,000.00 USD.
- **Hard Capital Floor**: 4,600.00 USD (Blueberry 8.00% max drawdown from 5,000.00 USD).
- **Operating Defense Buffer**: 4,650.00 USD (Defense buffer above hard floor).
- **Solvency Kernel Admission Floor**: 4,795.00 USD (Mandatory minimum stressed equity required to stage ANY new risk ticket).
- **Stressed Simulation Math (Unconditional Joint Reservation)**:
  $$\text{Stressed Worst-Case Equity} = \text{Current Equity} - \sum (\text{Nominal Risk}_i \times 1.25 + 2.00\text{ USD}) \ge 4,795.00\text{ USD}$$
  \text{Hard Floor Cushion} = \text{Stressed Worst-Case Equity} - 4,600.00\text{ USD}
  \text{Operating Buffer Cushion} = \text{Stressed Worst-Case Equity} - 4,650.00\text{ USD}
  \text{Kernel Floor Cushion} = \text{Stressed Worst-Case Equity} - 4,795.00\text{ USD}
- **Gate Invariant**: If `Operating Buffer Cushion < 0.00 USD` (or `Hard Floor Cushion < 20.00 USD`), ALL new order staging is strictly BLOCKED.
- **Current Live Solvency**: With Equity at 4,834.83 USD, buffer cushion is **+39.83 USD** (and hard floor cushion is **+59.83 USD**).

### Gate 2: Dynamic Capacity Policy & Fluid 4-Slot Architecture
- **Concurrency Cap**: Up to **4 concurrent FILLED positions in ANY combination** across the 156-asset universe (e.g. 4 crypto, 2 crypto + 1 forex + 1 index, 3 forex + 1 commodity, etc.), guided purely by edge.
- **Uncapped Resting Limits**: Resting pending limit orders do NOT consume filled capacity slots. The desk may stage resting limit orders at **any qualified candidate structural whale shelves** across the universe without arbitrary caps.
- **Risk Budget Recirculation**: Moving an active position's stop to Early-BE (+0.75R0 to +0.80R0) drops its downside cash risk to 0.00 USD, immediately liberating risk capacity to stage and fill subsequent positions!

### Gate 3: Causal Auction Regime & Market Structure Levels
Every scan evaluates structural auction location using ground-truth levels from Sheet 33 (`20_Auction_Market_Structure`) and Sheet 20 (`11_Technical`):
- **Auction Reference Shelves**:
  * **Volume Profile POC (VPOC)**: Institutional fair-value consensus node.
  * **Developing POC (d-POC)**: Current session volume POC migration.
  * **Value Area High (VAH) & Value Area Low (VAL)**: Boundaries containing 70% of volume distribution across Daily and Weekly horizons.
  * **Monday Opening Range (Monday High & Low / Initial Balance)**: Weekly rotational framework.
  * **Previous Day Extremes**: PDH, PDL, PDC.
  * **Previous Session Extremes**: Asian, London, and NY Session Highs and Lows.
  * **Weekly Macro Shelves**: Weekly POC, CWH, CWL, PWH, PWL.
- **Dual-Engine Assignment**:
  * **Model 1 (Extreme Mean Reversion)**: Admissible ONLY when `|VWAP Z-Score| >= 2.0 to 3.5 SD` in `MEAN_REVERT` regime with tape exhaustion.
  * **Model 2 (Trend Pullback)**: Admissible ONLY when |VWAP Z-Score| < 2.0 SD (0.2 to 1.7 SD) in confirmed TREND_UP or TREND_DOWN with Fibonacci Prime EMA ribbon hierarchy (5 > 13 > 34 > 89 > 144 > 233), retracing into the Symmetrical Fibonacci Golden Zone [0.618 GP, 0.702 OTE] or Fib-Prime EMA 34 / Session VWAP / VAH-VAL shelves, with SL anchored >= 0.40 ATR beyond 0.786 Invalidation Shelf.
  * **Stand-Aside Invariant**: If `Trend Regime == UNDEFINED`, the desk stands aside unconditionally in 100% Cash Defense.

### Gate 4: The 5-Pillar Confluence Stack & Liquidation/Stop Sweep Dynamics
Every admitted candidate must satisfy all 5 pillars simultaneously, grounded in the **33-sheet master Excel data warehouse (`Data/DataBase_Trading.xlsx`)**:
1. **Dynamic Spread Friction Efficiency**: Spread points / TP distance points <= 15%; baseline within ceiling.
2. **Cumulative Volume Delta (CVD) Absorption & Divergence (`zc_div > 0.8`)**: Sheet 27 (`18_CVD`) confirms aggressive market orders absorbed by passive limit books (`Delta Spot > 0` and `Delta Futures < 0` with `zc_div > 0.8`).
3. **Resting Whale Bunkers & Anti-Spoof Persistence**:
   - Sheet 19 (`10_Whale_Orders`) and Sheet 26 (`17_Orderbook`) confirm genuine resting whale orders >= $100K USD with `persist >= 180s`, `presence_frac >= 0.85`, and depth imbalance > +0.25 (longs) or < -0.25 (shorts).
4. **CoinGlass & Hyperdash Reconstructed Liquidation Cascade Pools**:
   - CoinGlass Clustered Liquidation Heatmap (Sheet 11 `7_Liq_Heapmap`), Live Liquidation Stream (Sheet 12 `7_Live_Liq`), and Exchange Liquidation Surfaces 1D/7D (Sheets 13 & 18: `8_Exchange_Liquidation_Map_1D` & `7D`).
   - Hyperdash Continuous Liquidation Ladder (Sheet 23: `14_Hyperdash_Liq_Map`, 5,700+ rows mapping exact continuous boundary [min_price, max_price] for long cascade bands and short squeeze bands).
   - Longs: Overhead Short Squeeze Band (`short_squeeze_band`).
   - Shorts: Downside Long Flush Band (`long_flush_target`).
5. **Hyperdash Resting Stop Clusters, Volume Profile & Fibonacci Golden Pocket**:
   - Hyperdash Resting Stop Orders Ladder (Sheet 24: `15_Hyperdash_Stops_Map`, 3,800+ rows mapping retail resting buy stops and sell stops). BANS placing limit orders inside un-swept stop clusters!
   - Sheet 33 (`20_Auction_Market_Structure`): Entry anchored at VPOC, VAH, VAL, or session shelves.
   - **Symmetrical Fibonacci Golden Zone Confluence**: Retracement aligns with the Symmetrical Golden Zone [0.618–0.650 GP, 0.702 OTE] with Stop Loss anchored >= 0.40 ATR beyond the 0.786 Invalidation Shelf, coinciding with resting whale bunkers.

### Gate 5: Microstructure Execution Hygiene & Broker CFD Mechanics
- **Passive Maker Limit Orders Only**: Strictly `BUY_LIMIT` or `SELL_LIMIT`. Zero market orders crossing the spread.
- **Dynamic Spread Friction Budgeting**:
  $$\text{Efficiency Ratio} = \frac{\text{Spread Points}}{\text{TP Distance Points}} \le 15\%$$
  - Baseline ceilings: Crypto <= 35.0 bps, Indices/Commodities <= 10.0 bps, Forex <= 6.0 bps, Exotics <= 25.0 bps.
- **2.0x ATR Drift Gate**: Limit order must rest within 2.0x ATR of current market price.
- **Fresh Execution Revalidation**: Verify tick Bid/Ask, broker spread, and L2 depth immediately prior to order transmission.

### Gate 6: Structural Take-Profit Anchoring Mandate & Expanded Risk Rights
- **Take-Profit Placement**: TP front-runs opposing liquidation magnets (Sheets 11, 13, 18, 23) by 5–10 bps to ensure fill before depletion.
- **Reward-to-Risk**: TP must yield >= +2.0R to +2.5R relative to the structural stop loss.
- **Expanded Operational Risk Envelope across ALL 156 Assets**:
  * **Standard Nominal Risk**: **15.00 to 20.00 USD per trade** (0.31% to 0.41% equity).
  * **Pristine Confluence Risk Rights (Operator Authorization)**: Authorized to scale nominal risk up to **25.00 to 35.00 USD per trade** (0.51% to 0.72% equity) across **ALL 156 assets** for pristine 5-pillar confluence setups.

### Gate 7: Cost-Aware Piecewise Ratchet Lifecycle Sentry (Frozen R0)
- **Phase Early-BE (+0.75R0 to +0.80R0)**: Move SL to $\text{Entry} + 0.10R_0$ once price reclaims session POC or VWAP. Downside risk drops to **0.00 USD**, releasing capacity for subsequent slots!
- **Phase 0 (+1.25R0)**: Move SL to $\text{Entry} + 0.15R_0$ (locks in minor profit + commission).
- **Phase 1 (+1.65R0)**: Move SL to $\text{Entry} + 0.80R_0$ (banks major profit).
- **Phase 2 (>= +2.00R0)**: Continuous trailing stop at $0.50\text{ ATR}$ behind 15m swing shelves.
- **Target Exit**: Full Take-Profit at **+2.00R to +2.50R**.
- **Time Decay Sentry**: If active for 24 bars (6 hours) with gain < +0.20R0, market close to redeploy capital.

---

## 4. 0–100 EVIDENCE-QUALITY ARBITRATION RUBRIC

To eliminate subjective debate between Arena.ai and Antigravity, every candidate setup is evaluated on this formal 100-point rubric:

| Dimension | Weight | Scoring Criteria |
|---|---|---|
| **1. 33-Sheet Data Provenance & Freshness** | 20 pts | All 33 sheets loaded (10 pts), Orderbook/CVD/Auction age <= 15m (5 pts), 0 formula errors (#REF! = 0) (5 pts). Deduct 20 pts if stale or schema broken. |
| **2. Structural Thesis & Invalidation** | 20 pts | Clear VPOC/VAH/VAL or EMA shelf anchor (10 pts), unambiguous structural SL outside liquidation/stop sweep band (10 pts). |
| **2. Structural Thesis & Invalidation** | 20 pts | Clear VPOC/VAH/VAL, Monday IB_W, Session/Macro Extremes, or Fib-Prime EMA shelf anchor (10 pts), unambiguous structural SL outside 0.786 Invalidation Shelf / liquidation / stop sweep band (10 pts). |
| **4. Capital Floor Defense & Capacity** | 20 pts | Stressed cushion >= +20 USD above 4,775 USD (10 pts), Stressed cushion >= +0 USD above 4,795 USD buffer (5 pts), Capacity slot available (5 pts). |
| **5. Execution Hygiene & Spread Efficiency**| 10 pts | Efficiency Ratio (Spread / TP) <= 15% (10 pts), baseline within ceiling (5 pts), > 15% ratio (0 pts & VETO). Maker limit within 2.0x ATR. |
| **6. Macro & Session Timing** | 10 pts | No Tier-1 macro event within blackout window (5 pts), Active liquid trading session / normal volatility (5 pts). |

### Arbitration Action Thresholds:
- **Score >= 80 pts + All Hard Gates Pass**: `APPROVED` -> Stage passive limit order live into MT5.
- **Score 60–79 pts**: `STANDBY` -> Maintain on Potential Candidate Radar Checklist; do not stage until missing evidence is established.
- **Score < 60 pts OR Any Hard Failure**: `STAND ASIDE / REJECTED` -> No order permitted.
- **Hard Failure Vetoes (Instant Rejection regardless of score)**:
  * Operating buffer cushion < 0.00 USD (or Hard floor cushion < 20.00 USD).
  * Efficiency Ratio > 15% or Spread exceeds baseline ceiling.
  * Master Excel data age > 30 minutes.
  * Tier-1 macro blackout active within ±15m (Crypto) or ±35m (TradFi).

---

## 5. COMPLETE DATA SOURCE PROVENANCE & VERIFICATION MATRIX (33 EXCEL SHEETS)

Every signal, metric, and decision MUST trace back to the **33-sheet canonical master Excel data warehouse (`Data/DataBase_Trading.xlsx`)** as the single definitive source of truth:

| # | Data Source Name | Provider / Worksheet Name | Update Cadence | Latency / Freshness | Verification Method | Tactical Trading Scope & Parameters |
|---|---|---|---|---|---|---|
| **1** | **Master Excel Data Warehouse** | `Data/DataBase_Trading.xlsx` (All 33 Canonical Production Worksheets) | Continuous pipeline daemon (`Run_Parallel_Pipeline.py`) | Every 300s rest cooldown (mtime < 10m) | Atomic zip CRC check, openpyxl load, 0 formula errors | Exclusive single source of truth for both Antigravity and Arena.ai across all 156 assets. |
| **2** | **Live MT5 Broker Telemetry & Spreads** | Sheet 00: `00_MT5_Account_Telemetry` + `Terminal/multi_asset_opportunity_scanner.py` | Tick-by-tick / updated continuously | < 100 ms | `mt5.initialize()`, `account_info()`, `order_calc_profit()` | Live equity, balance, hard floor cushion (+59.83 USD), buffer cushion (+39.83 USD), real spreads in bps across 156 assets. |
| **3** | **Institutional ETF Netflows** | Sheets 01 & 02: `Crypto_ETF_Flows` & `1_Crypto_ETF_Flows` | Daily post-market settlement | Daily / updated 4h | Sheet audit: IBIT, FBTC, ETHA net inflow USD | TradFi institutional accumulation barometer; positive inflows confirm macro tailwind. |
| **4** | **CEX Spot Netflow (500 Assets)** | Sheet 03: `2_Spot_Netflow_S` | 1h, 4h, 12h, 24h, 7d netflows | < 15 min | Column audit: physical spot inflow/outflow USD | Real spot accumulation vs distribution; exchange withdrawals confirm institutional accumulation. |
| **5** | **Derivatives Positioning & Crowding** | Sheets 04–06, 08–10: `3_Exchanges_LS_Ratio_*`, `5_OI`, `5_Funding_Rate`, `6_Funding_Fee_Settlement` | 15m, 1h, 4h intervals | < 15 min | Long/Short skew, Open Interest change %, funding rates | Retail crowding filter: Longs disqualified if retail > 70% long or funding > +0.03%. |
| **6** | **CoinGlass Clustered Liquidations & Whales** | Sheets 11–18, 19: `7_Liq_Heapmap`, `7_Live_Liq`, `8_Exchange_Liquidation_Map_1D/7D`, `9_Liquidation_Max_Pain_24H-7D`, `10_Whale_Orders` | Real-time & multi-timeframe | < 15 min | Dollar-by-dollar clusters, live liquidation tape | Locates dense liquidation magnets; identifies resting whale orders >= $100K with persist >= 180s. |
| **7** | **Hyperdash DEX & Continuous Ladders** | Sheets 07, 21–25: `4_Hyperliquid_Analysis`, `12_Hyperdash`, `13_Hyperliquid`, `14_Hyperdash_Liq_Map`, `15_Hyperdash_Stops_Map`, `16_Hyperdash_telegram_Intel` | Continuous on-chain stream | < 15 min | 2,001 whale wallets, 5,700-row liq ladder, 3,800-row stop map | Maps exact continuous boundary [min_price, max_price] of long cascade bands and un-swept retail stop clusters. |
| **8** | **Multi-Asset CVD Engine** | Sheet 27: `18_CVD` | 1m, 5m, 15m, 1h, session | < 15 min | Spot vs Futures delta divergence `zc_div > 0.8` | Core Pillar 2 Confluence: confirms passive institutional absorption of aggressive taker market orders. |
| **9** | **Sovereign Macro Calendar & News** | Sheets 28 & 29: `19_News`, `19_Calendar` + `Data/macro_calendar.json` | Scheduled releases & breaking feeds | Verified daily | Direct calendar inspection, event proximity | Enforces mandatory blackout windows (±15m Crypto, ±35m TradFi) around Tier-1 events (CPI, FOMC, NFP). |
| **10** | **Auction Market Structure & Key Levels** | Sheet 33: `20_Auction_Market_Structure` (Row 1 unmerged headers) | Real-time 15m candle bar close | < 15 min | 36 columns: Daily/Weekly VPOC, VAH, VAL, Monday Open, Session & Prior Day Extremes | Ground-truth auction profiling across 54 assets; identifies Volume Profile shelves and rotational boundaries. |
| **11** | **AST Knowledge Graph** | `graphify-out/graph.json` | Updated on code modification | Static AST index | `python -m graphify query` | 7,400+ nodes, classes, call-flows. Queried with zero API tokens to prevent context amnesia. |

---

## 6. AST KNOWLEDGE GRAPH INTEGRATION & ZERO-TOKEN QUERYING VIA /GRAPHIFY

To eliminate context bloating, prevent hallucination, and preserve model context windows across long-running sessions, agents MUST query the repository's pre-indexed Abstract Syntax Tree (AST) knowledge graph rather than ingesting entire raw python modules:

- **Graph Storage**: `graphify-out/graph.json` (contains 7,400+ semantic nodes, classes, call-flows, and dependencies).
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

## 8. ACTIVE PERFORMANCE SCORECARD & DESK STATE (CYCLE 260)

- **Account Baseline**: 5,000.00 USD (MetaTrader 5 Account #5064568).
- **Live Account Balance**: **4,834.83 USD**.
- **Live Floating Equity**: **4,834.83 USD** (100% Flat Cash, 0 open positions, 0 pending orders).
- **Free Margin**: **4,834.83 USD** (4 Liberated Capacity Slots).
- **Hard Capital Floor**: **4,775.00 USD** (Live Cushion: **+59.83 USD** / +1.25%).
- **Operating Buffer Floor**: **4,795.00 USD** (Live Cushion: **+39.83 USD** / +0.83%).
- **Phase 1 Goal Gap**: **+665.17 USD** to 5,500.00 USD | Runway: **~31.4 hours** remaining.
- **Dynamic Capacity Clearance**: **CLEARED FOR 1 NEW POSITION** at **15.00 to 25.00 USD nominal risk** (leaving **+6.58 to +21.74 USD buffer surplus** above 4,795.00 USD).
- **Expanded Operational Risk Rights**: Standard nominal risk $15.00–$20.00 USD, authorized up to **$25.00–$35.00 USD** for pristine 5-pillar setups across **ALL 156 assets**.

---
*Authorized by Antigravity Quantitative Command & Registered into `.agents/rules/ACTIVE_CONTEXT.md`.*
