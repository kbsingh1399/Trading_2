# Specification: Autonomous 15-Minute Candle AI Trader & MT5 Execution Bridge

## 1. Executive Architecture

### 1.1 Objective and Mandate
The Autonomous 15-Minute Candle AI Trader is an institutional multi-asset quantitative trading engine designed to operate autonomously on 15-minute timeframe candles. The system executes disciplined trade entry evaluation, dynamic risk allocation, and microstructure trade management across perpetual cryptocurrency markets and CFD assets. It combines three distinct intelligence feeds into a 360-degree market model:
1. **Web Macro & Geopolitical Intelligence**: High-impact economic calendar events (CPI, Core PCE, FOMC interest rate announcements, Non-Farm Payrolls) and breaking real-time market catalysts.
2. **Hyperdash Microstructure Orderflow**: Sub-second Level 2 orderbook depth imbalance, liquidation concentration bands, resting stop clusters, and Level 3 whale orders streamed via `http://localhost:8095`.
3. **MetaTrader 5 (MT5) Real-Time Execution Engine**: Direct tick-level price discovery, symbol contract specifications, spread and slippage tracking, and live order/ticket management connected to Account 5064568 (Blueberry Markets).

### 1.2 The 14th-Minute Cadence Rationale
Standard retail trading bots evaluate signals at the exact bar close (:00, :15, :30, :45), introducing systemic flaws:
- High execution latency caused by broker gateway contention during candle open flushes.
- Network and API timeouts when simultaneously fetching orderbooks, macro data, and indicator metrics.
- Sub-optimal slippage as market orders cluster at the exact first second of a new bar.

To solve this, the AI Trader implements a **14th-Minute Cadence** (executing at minute 14:00 to 14:20 of each 15-minute bar, e.g. at :14, :29, :44, and :59):
```
15m Candle Timeline:
[Minute 00:00 ----------------------- Minute 14:00 ---------- Minute 15:00 / 00:00]
      |                                      |                        |
 Candle Open                           Wakeup Cadence           Candle Close &
                                       - Ingest 360 Data        Next Bar Open
                                       - Evaluate Macro         - Fire Pre-staged Orders
                                       - Compute Orderflow      - Execute MT5 Ratchets
                                       - Check Ratchets
```
- **Information Completeness**: At minute 14:00, 93.3 percent of the 15-minute volume, cumulative volume delta (CVD), and candle structure is formed, providing near-certain candle formation parameters.
- **Latency Decoupling**: The engine utilizes the final 40 to 60 seconds of the candle to ingest Hyperdash L2/L3 orderflow, scrape/verify macro news calendars, execute risk checks, and pre-stage orders.
- **Deterministic Routing**: Trade actions fire with sub-second precision exactly at candle close (:00, :15, :30, :45) or immediately upon ratchet threshold breach.

### 1.3 System Overview Diagram
```
+-----------------------------------------------------------------------------------+
|                        14th-Minute Master Event Trigger                           |
+-----------------------------------------------------------------------------------+
                                         |
         +-------------------------------+-------------------------------+
         |                               |                               |
         v                               v                               v
+------------------+           +------------------+            +------------------+
|  Macro Engine    |           | Hyperdash Stream |            |  MT5 Connector   |
|  - Web News RSS  |           |  - L2 Depth Imb  |            |  - Account Info  |
|  - CPI / FOMC    |           |  - Liq Clusters  |            |  - Active Tickets|
|  - Blackout Check|           |  - L3 Whale Tape |            |  - Tick Prices   |
+------------------+           +------------------+            +------------------+
         |                               |                               |
         +-------------------------------+-------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     360-Degree Market Decision Engine                             |
|  - Confluence Filter (S1 Pullback / S4 Sweep / S3 Breakout)                      |
|  - Macro Sentiment & Volatility Gate (Tier-1 Event Lockout)                       |
|  - Microstructure Imbalance & Whale Absorption Confirmation                       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                         Risk & Capital Governance                                 |
|  - Initial Capital: 5,000.00 USD | Account 5064568                                |
|  - Dynamic Conviction Risk: 10.00 to 20.00 USD per trade (0.20% to 0.40%)         |
|  - Hard Circuit Breaker: 4.50% Drawdown Stop (Equity <= 4,775.00 USD)             |
|  - Max Concurrent Positions: 2                                                    |
+-----------------------------------------------------------------------------------+
                                         |
         +-------------------------------+-------------------------------+
         |                                                               |
         v                                                               v
+----------------------------------+            +-----------------------------------+
| New Position Router              |            | Dynamic 3-Stage Ratchet Manager   |
| - Pre-staged Limit/Market Order  |            | - Active Position: SOLUSD.p       |
| - Dynamic Conviction Sizing      |            | - Phase 0 BE Lock (+0.80R)        |
| - Structural SL & 3.0R TP        |            | - Phase 1 Profit Lock (+1.50R)    |
| - Mode: Paper Ledger / MT5 Bridge|            | - Phase 2 Runner Trail (+2.00R)   |
+----------------------------------+            +-----------------------------------+
```

### 1.4 Single Strategy File Invariant
All trade logic, signal generation, ratchet evaluation, risk budgeting, and scheduling reside within `Terminal/OF_Strategy.py`, supported by an explicit modular execution bridge `Terminal/MT5_Execution_Bridge.py`. No fragmented scripts or uncoordinated background jobs are permitted.

---

## 2. Risk Governance Invariants

The trading engine operates under strict institutional risk controls designed to satisfy proprietary trading firm rules:

1. **Capital Base**:
   - Initial Evaluation Capital: 5,000.00 USD.
   - Broker & Account: Blueberry Markets (SVG) LLC, Login: 5064568.
   - Live Baseline: Balance 4,742.90 USD, Equity 4,834.90 USD.
2. **Base Risk per Trade**:
   - Primary Active Risk Budget (R): dynamic **10.00 to 20.00 USD** per trade (0.20% to 0.40% of 5,000.00 USD capital) for live deployment.
   - Dynamic Conviction Scaling: Score 1 (Base Orderflow) = 10.00 USD; Score 2 (Orderflow + Whale) = 15.00 USD; Score 3+ (Full Confluence + Macro Aligned) = 20.00 USD.
   - Sizing Formula: R_dist = max(price * 0.0075, 0.50); units = risk_budget / R_dist; lots = round(units / contract_size, 2).
   - Milestone Defense Risk: If capital drops by 100.00 USD or 2 consecutive losses occur, risk drops to 7.00 USD.
   - Defense Risk: 5.00 USD if drawdown exceeds 1.80%.
3. **Hard Drawdown Stop**:
   - Hard Circuit Breaker Limit: 4.50% drawdown relative to high water mark (5,000.00 USD peak implies hard equity floor at 4,775.00 USD).
   - Action upon Breach: Absolute trade halt. Zero new positions permitted. Open orders cancelled immediately. Active running positions managed with tight trailing stops to preserve remaining capital.
4. **Position Concurrency & Exposure**:
   - Maximum Concurrent Positions: 2 simultaneous positions across all asset sleeves.
   - Directional Correlation Filter: Prohibits opening 2 simultaneous long positions on highly correlated crypto assets (e.g. BTC and SOL).
   - Asset Cooldown: Minimum 4 bars (60 minutes) between consecutive entries on the same asset.
5. **Three-Stage Microstructure Ratchet (Oxford-Man Protocol)**:
   For every active trade with initial risk distance R_dist = abs(entry - initial_sl):
   - **Phase 0 (Breakeven Lock)**: When unrealized gain reaches +0.80R, move stop loss to Entry + 0.15R (locks friction and guarantees zero-loss execution).
   - **Phase 1 (Profit Lock)**: When unrealized gain reaches +1.50R, move stop loss to Entry + 0.85R (locks 0.85R profit, unlocks dynamic ATR trailing).
   - **Phase 2 (Runner Trail Lock)**: When unrealized gain reaches +2.00R, move stop loss to Entry + 1.50R, ratcheting with highest structural swing low/high.
   - **Target Exit (TP)**: Fixed convex target at +2.50R to +3.00R.
   - **Time Decay Stop**: If trade has not achieved +0.20R gain after 24 bars (6 hours), exit at market.

---

## 3. Current Live State & Active Position Audit

The engine initializes with awareness of current account status:
- **Account Number**: 5064568
- **Broker Server**: BlueberryMarketsSVG-Live
- **Currency**: USD
- **Balance**: 4,742.90 USD
- **Equity**: 4,834.90 USD
- **Margin Free**: 1,846.15 USD
- **Active Position**:
  - Symbol: `SOLUSD.p`
  - Ticket: 18464576
  - Direction: BUY (Long)
  - Volume: 0.50 lots (Contract size = 100.0 -> Notional exposure = 50 SOL)
  - Open Price: 119.55 USD
  - Current Stop Loss: 118.92 USD (Initial R_dist = 0.63 USD; Initial Risk = 50 * 0.63 = 31.50 USD)
  - Current Take Profit: 122.78 USD (+3.23 USD distance = +5.12R)
  - Current Price: 121.50 USD
  - Current Unrealized Gain: (121.50 - 119.55) / 0.63 = +3.10R (Floating Profit: +92.00 USD)
  - Immediate Action Required: Active position exceeds +2.00R (Phase 2). The Stop Loss must be ratcheted from 118.92 USD up to at least Entry + 1.50R (119.55 + 0.945 = 120.495 USD, rounded to 120.50 USD) to lock +47.25 USD net profit.

---

## 4. Phase Breakdown & Execution Plan

### Phase 1: Data Ingestion & Live Connectors
**Objective**: Establish low-latency, resilient data connections to MT5 terminal, Hyperdash local streaming server, and symbol metadata mapping.

#### Component 1.1: MetaTrader 5 Bridge (`Terminal/MT5_Execution_Bridge.py`)
- Initialize `MetaTrader5` Python package with IPC connection to terminal.
- Validate login against Account 5064568.
- Extract real-time account summary (`balance`, `equity`, `margin_free`, `margin_level`).
- Query active positions via `positions_get()` and map tickets into structured records.
- Implement symbol info reader (`contract_size`, `point`, `digits`, `spread`, `bid`, `ask`).
- Implement `modify_position_sltp(ticket, sl, tp)` via `TRADE_ACTION_SLTP`.
- Implement `open_market_order(symbol, direction, volume, sl, tp)` via `TRADE_ACTION_DEAL`.

#### Component 1.2: Hyperdash Live Client
- Query `http://localhost:8095/api/live/{coin}` for target symbols (`BTC`, `ETH`, `SOL`).
- Parse Level 2 orderbook depth and compute normalized bid/ask ratio imbalance:
  `Imbalance = (Total_Bid_Depth - Total_Ask_Depth) / (Total_Bid_Depth + Total_Ask_Depth)`
- Parse liquidation concentration ladders (`bands`, `total_long_size`, `total_short_size`).
- Parse resting stop clusters and Level 3 whale orders (orders with notional >= 50,000 USD).
- Implement fault tolerance: if local Hyperdash API is unreachable, fallback to direct cached data or raise safe diagnostic warning without crashing the loop.

#### Component 1.3: Cross-Venue Symbol Mapping
- Map internal crypto ticker symbols to MT5 broker symbols:
  - `BTC` -> `BTCUSD.p`
  - `ETH` -> `ETHUSD.p`
  - `SOL` -> `SOLUSD.p`
- Validate contract multipliers (e.g. `SOLUSD.p` contract size is 100, `BTCUSD.p` contract size is 1).

---

### Phase 2: Macro & Web Market Intelligence Engine
**Objective**: Safeguard the system against unexpected volatility spikes caused by macro economic releases and crypto-wide regulatory shocks.

#### Component 2.1: Economic Calendar Ingestion
- Ingest upcoming High-Impact USD and Global economic events:
  - Consumer Price Index (CPI / Core CPI)
  - Federal Open Market Committee (FOMC rate decision, press conference, minutes)
  - Non-Farm Payrolls (NFP) and Unemployment Rate
  - Gross Domestic Product (GDP) annualized prints
- Record event timestamp in UTC, consensus forecast, and prior reading.

#### Component 2.2: Event Blackout Window Controller
- Define strict blackout interval: `T_event - 15 minutes` to `T_event + 15 minutes`.
- When current time falls within blackout interval:
  - Suspend all new trade entries across all sleeves.
  - Set macro gate status to `BLACKOUT_ACTIVE`.
  - For running positions: advance ratchets to Breakeven Lock (Phase 0) if gain >= +0.50R to prevent sudden flash-crash liquidation.

#### Component 2.3: Real-Time Market Catalyst & News Sentiment Parser
- Lightweight web fetcher scraping high-frequency crypto and macro news headlines (CoinDesk, Bloomberg Markets, Reuters financial feeds).
- Keyword-based emergency sentiment filter:
  - Bearish shock keywords: SEC lawsuit, exchange insolvency, stablecoin depeg, regulatory ban, protocol exploit.
  - Bullish catalyst keywords: ETF approval, rate cut, reserve currency adoption, institutional treasury allocation.
- Output normalized Macro Sentiment Score bounded between -1.0 (extreme bearish fear) and +1.0 (extreme bullish mania).

---

### Phase 3: 360-Degree Trade Evaluator & Confluence Engine
**Objective**: Synthesize Orderflow, Technical Pivots, and Macro Sentiment into a unified trade decision at minute 14 of each candle.

#### Component 3.1: Technical & Microstructure Feature Extraction
- Calculate rolling 15-minute indicators:
  - 200 EMA slope and 50 EMA trend alignment.
  - Session Volume Weighted Average Price (VWAP) and VWAP distance z-score.
  - Structural Daily / Weekly Pivots (PDH, PDL, PWH, PWL) for sweep detection.
  - Orderflow Footprint Delta & Cumulative Volume Delta (CVD) divergence.
  - Hyperdash L2 Book Imbalance and Liquidation Band concentration.

#### Component 3.2: Multi-Sleeve Confluence Rules
The evaluator checks entries against 3 primary institutional sleeves:
1. **Sleeve S1 (Orderflow Pullback & CVD Absorption)**:
   - Price above rising 200 EMA and below VWAP (discount).
   - Liquidation sweep observed below market followed by CVD positive delta absorption.
   - Long entry trigger when whale buy aggressor volume exceeds sell volume by 1.5x.
2. **Sleeve S4 (Structural Liquidity Sweep)**:
   - Sweep of Previous Day Low (PDL) or Previous Day High (PDH).
   - Quick rejection candle closing back inside the range with delta divergence.
3. **Sleeve S3 (Session Breakout ORB + CRT)**:
   - London (07:00 UTC) or New York (13:30 UTC) opening range breakout.
   - False breakout (Judas swing) filter confirmed by orderbook depth.

#### Component 3.3: Confluence Scoring & Decision Output
- Combine Sleeve signals with Macro Sentiment Score:
  - Long Signal Valid IF: Technical Setup == LONG AND Macro Sentiment >= -0.20 AND Blackout == False AND L2 Imbalance > -0.15.
  - Short Signal Valid IF: Technical Setup == SHORT AND Macro Sentiment <= +0.20 AND Blackout == False AND L2 Imbalance < +0.15.
- Output structured trade signal:
```json
{
  "timestamp": "2026-10-04T12:29:00Z",
  "symbol": "SOLUSD.p",
  "decision": "NO_ENTRY",
  "reason": "Max concurrent positions reached or setup pending confirmation",
  "confluence_score": 0.78,
  "macro_bias": "NEUTRAL",
  "orderflow_imbalance": 0.24,
  "risk_budget_usd": 42.00
}
```

#### Component 3.4: Dynamic Position Sizing Calculator
- Input: `risk_budget_usd` (35.00 to 45.00 USD), `entry_price`, `stop_loss_price`, `contract_size`.
- Formula:
  `R_dist = abs(entry_price - stop_loss_price)`
  `Calculated_Units = risk_budget_usd / R_dist`
  `Lot_Size = Calculated_Units / contract_size`
- Round `Lot_Size` down to nearest broker allowed step (0.01 lots), ensuring risk never exceeds 45.00 USD.

---

### Phase 4: MT5 Trade Manager & 3-Stage Ratchet Controller
**Objective**: Dynamically manage all open MT5 positions in real-time, executing the 3-stage ratchet on existing tickets (specifically `SOLUSD.p` ticket 18464576).

#### Component 4.1: Position State Tracker
- Read open positions from MT5.
- Reconcile with local position state file `Data/mt5_active_positions.json`.
- Track metrics for each position:
  - `ticket`: MT5 position identifier (e.g. 18464576).
  - `symbol`: Instrument (e.g. SOLUSD.p).
  - `direction`: LONG or SHORT.
  - `volume`: Lot size.
  - `entry_price`: Execution price (119.55 USD).
  - `initial_sl`: Original stop loss (118.92 USD).
  - `current_sl`: Present broker stop loss.
  - `take_profit`: Present broker take profit (122.78 USD).
  - `r_dist`: Initial unit risk (0.63 USD).
  - `current_r`: Current gain in R units: `(current_bid - entry_price) / r_dist`.
  - `current_phase`: Current ratchet phase (0, 1, 2, or 3).

#### Component 4.2: Ratchet Transition Logic
For LONG positions:
- **Phase 0 Check**:
  If `current_r >= 0.80` and `current_phase < 1`:
  Target SL = `entry_price + 0.15 * r_dist` (119.64 USD).
  Execute `modify_position_sltp(ticket, sl=119.64)`.
  Advance `current_phase = 1`.
- **Phase 1 Check**:
  If `current_r >= 1.50` and `current_phase < 2`:
  Target SL = `entry_price + 0.85 * r_dist` (120.09 USD).
  Execute `modify_position_sltp(ticket, sl=120.09)`.
  Advance `current_phase = 2`.
- **Phase 2 Check**:
  If `current_r >= 2.00` and `current_phase < 3`:
  Target SL = `entry_price + 1.50 * r_dist` (120.50 USD).
  Execute `modify_position_sltp(ticket, sl=120.50)`.
  Advance `current_phase = 3`.
- **Dynamic Trail (Phase 3)**:
  If `current_r >= 2.50`:
  Ratchet SL upward behind trailing 15m candle low (minus 0.5x ATR), never lowering SL.

#### Component 4.3: Paper Trading vs Live Execution Switch
- Supported modes in `Terminal/OF_Strategy.py`:
  - `--exec-mode paper`: Writes simulated orders to `Data/ofc_paper_positions.json`, tracking MT5 live prices without sending broker orders.
  - `--exec-mode mt5-live`: Directly routes orders and ratchet SL updates to MetaTrader 5 via `TRADE_ACTION_SLTP` and `TRADE_ACTION_DEAL`.
  - `--exec-mode hybrid`: Manages existing MT5 live positions (e.g. ticket 18464576) with broker ratchets, while testing new strategy signals in paper mode.

---

### Phase 5: Autonomous 15-Minute Cadence Scheduler & Heartbeat Loop
**Objective**: Build an institutional production loop that wakes up at the 14th minute of every candle, runs end-to-end evaluations, persists telemetry, and self-heals.

#### Component 5.1: High-Precision 14th-Minute Clock
- Precision alignment formula:
  Determine seconds remaining until next `(minute % 15 == 14)` and `second == 0`.
  Example: At 12:05:30 -> Next wakeup at 12:14:00 (510 seconds sleep).
  At 12:14:15 -> Wakeup executed, next evaluation at 12:29:00 (885 seconds sleep).
- Drift-free sleep loop using monotonic clock compensation (`time.monotonic()`).

#### Component 5.2: Master Execution Pipeline
On each 14th-minute wakeup:
1. Ingest account balance and verify Drawdown Circuit Breaker (< 4.50%).
2. Ingest Hyperdash live orderflow data from `http://localhost:8095`.
3. Ingest upcoming macro economic events and check Blackout Window.
4. Evaluate open MT5 positions and execute 3-stage ratchet updates.
5. If open positions < 2 and no cooldown active: evaluate 360-degree entry confluences.
6. Stage new orders for execution at candle close or execute paper entry.
7. Save snapshot telemetry to `Data/ai_trader_telemetry.json`.
8. Log detailed status report to console.

#### Component 5.3: Fault Tolerance & Telemetry
- Automatic reconnection if MT5 terminal connection drops.
- Rate-limit handling and graceful fallback if Hyperdash stream pauses.
- Atomic state file writes with `.tmp` staging to prevent corruption during power failure.

---

## 5. Verification Matrix & Criteria

Every phase has concrete, independently verifiable criteria that can be tested from PowerShell or automated unit tests.

| Phase | Component | Verification Command / Procedure | Expected Output / Criteria |
| :--- | :--- | :--- | :--- |
| **Phase 1** | MT5 Connection | `python -c "import MetaTrader5 as mt5; mt5.initialize(); print(mt5.account_info().login, mt5.account_info().balance)"` | Returns login `5064568` and balance `4742.90 USD`. |
| **Phase 1** | MT5 Active Position | `python -c "import MetaTrader5 as mt5; mt5.initialize(); pos = mt5.positions_get(symbol='SOLUSD.p'); print(pos[0].ticket, pos[0].volume)"` | Returns ticket `18464576` and volume `0.5`. |
| **Phase 1** | Hyperdash Live Stream | `python -c "import urllib.request, json; d = json.loads(urllib.request.urlopen('http://localhost:8095/api/live/SOL').read()); print(d['price'], len(d['liquidations']['bands']))"` | Returns current SOL price (~121.50 USD) and liquidation band count > 0. |
| **Phase 2** | Macro Blackout Filter | Run unit test injecting scheduled FOMC event at `T_now + 5 min`. | System outputs `BLACKOUT_ACTIVE: TRUE` and blocks simulated trade entry. |
| **Phase 2** | Web News Ingestion | Run test fetching financial headlines parser. | Outputs parsed list of news items with computed sentiment score in range [-1.0, 1.0]. |
| **Phase 3** | Position Sizer | Run test with 42.00 USD risk, Entry = 120.00 USD, SL = 118.00 USD, Contract Size = 100. | `Calculated lots = 42.00 / (2.00 * 100) = 0.21 lots`. Risk strictly bounded between 35.00 and 45.00 USD. |
| **Phase 3** | 360 Trade Evaluator | Run single-bar evaluation with synthetic and live feeds. | Returns structured decision JSON containing all features, macro bias, and explicit trade action. |
| **Phase 4** | Ratchet State Machine | Test ratchet logic against SOLUSD.p position (entry 119.55 USD, current price 121.50 USD). | Identifies current gain is +3.10R (> +2.00R). Proposes ratcheting SL to 120.50 USD (Phase 2/3 lock). |
| **Phase 4** | MT5 SL Modification | Execute test SL update on ticket 18464576 to 120.50 USD via `TRADE_ACTION_SLTP`. | MT5 server confirms `retcode == 10009` (TRADE_RETCODE_DONE). Open position SL reflects 120.50 USD. |
| **Phase 5** | 14th-Minute Scheduler | Run `Terminal/OF_Strategy.py --mode ai-trader --dry-run-bars 2`. | System calculates correct sleep duration to next 14th minute, executes 2 consecutive cycles, logs telemetry, exits cleanly. |
| **Phase 5** | Hard DD Stop Guard | Test condition where equity is simulated at 4,770.00 USD (drawdown 4.60%). | System immediately asserts hard circuit breaker breach, halts trading, and logs warning. |

---

## 6. Implementation Task Roadmap

```
[Phase 1: Ingestion Bridge]
  ├── Task 1.1: Implement Terminal/MT5_Execution_Bridge.py (MT5 IPC & Order Routing)
  ├── Task 1.2: Connect Hyperdash Orderflow Ingestor for SOL, BTC, ETH
  └── Task 1.3: Validate symbol mapping and contract multipliers

[Phase 2: Macro Intelligence]
  ├── Task 2.1: Implement economic calendar parser (CPI, FOMC, NFP)
  ├── Task 2.2: Implement 15-minute event blackout gate
  └── Task 2.3: Build real-time news sentiment scoring module

[Phase 3: 360 Trade Evaluator]
  ├── Task 3.1: Construct orderflow & microstructure feature bundle
  ├── Task 3.2: Implement multi-sleeve confluence logic (S1, S4, S3)
  └── Task 3.3: Implement dynamic position sizing (35.00 - 45.00 USD risk)

[Phase 4: MT5 Trade Manager]
  ├── Task 4.1: Build real-time position reconciler for Account 5064568
  ├── Task 4.2: Implement 3-Stage Ratchet logic (BE Lock +0.8R, Profit +1.5R, Trail +2.0R)
  └── Task 4.3: Deploy ratchet management to active SOLUSD.p ticket 18464576

[Phase 5: Autonomous Scheduler Loop]
  ├── Task 5.1: Implement 14th-minute precision scheduling clock
  ├── Task 5.2: Integrate full pipeline into Terminal/OF_Strategy.py (--mode ai-trader)
  └── Task 5.3: Validate state persistence, telemetry logging, and hard DD stop
```
