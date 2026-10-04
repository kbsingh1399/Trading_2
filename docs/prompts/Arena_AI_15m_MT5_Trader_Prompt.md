# INSTITUTIONAL QUANTITATIVE AUDIT & ARCHITECTURAL CONSULTATION FOR ARENA.AI / OX ALPHA
## Autonomous 15-Minute Candle AI Trader, Hyperdash Microstructure Orderflow & MetaTrader 5 Bridge

---

### 1. MISSION BRIEFING & OBJECTIVE

You are acting as an Institutional Senior Quantitative Architect, High-Frequency Trading (HFT) Execution Engineer, and Market Microstructure Forensics Auditor.

We have engineered and deployed an **Autonomous 15-Minute Candle AI Trading & Execution Engine** (`Trading_2`). The system autonomously analyzes market microstructure right before the close of every 15-minute candle, dynamically sizes risk, manages active trades using 3-stage piecewise ratchets and orderflow liquidation targets, and executes orders directly on **MetaTrader 5 (MT5)** connected to **Blueberry Markets** (Account 5064568).

We require your **adversarial quantitative code review, architectural audit, and institutional optimization recommendations** to elevate execution efficiency, portfolio risk balancing, and long-term alpha generation.

---

### 2. CORE ARCHITECTURAL INVENTORY & REPOSITORY PROVENANCE

- **GitHub Repository**: `https://github.com/kbsingh1399/Trading_2` (Commit: `7b9a0b7`)
- **Primary Source Modules**:
  1. `Terminal/OF_Strategy.py`: Master Strategy Engine, Multi-Asset Orderflow Scanner, 3-Stage Microstructure Ratchet, and MT5 Autonomous Scheduler.
     Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/OF_Strategy.py`
  2. `Terminal/MT5_Execution_Bridge.py`: Native MetaTrader 5 IPC Bridge (Account discovery, symbol auto-resolution, lot sizing, SL/TP modification via `TRADE_ACTION_SLTP`).
     Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/MT5_Execution_Bridge.py`
  3. `Terminal/Market_Intelligence.py`: Real-Time Macro News Sentiment Scraper (Dow Jones, CoinDesk, Cointelegraph) and +/- 15m Economic Calendar Blackout Gate (CPI, Core PCE, FOMC, NFP).
     Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Market_Intelligence.py`
  4. `Terminal/Chrome_Terminal.py`: Real-time orderflow daemon streaming Level 2 orderbook, Level 3 resting whale orders with Ethereum wallet addresses, liquidation cascade ladders, and stop clusters (`http://localhost:8095`).
     Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Chrome_Terminal.py`
  5. `docs/specs/ai-15m-candle-mt5-trader.md`: Complete Architectural Specification and Risk Governance Protocol.
     Raw URL: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ai-15m-candle-mt5-trader.md`

---

### 3. EXECUTIVE TRADING ARCHITECTURE

#### 3.1 The 14th-Minute Cadence Rationale
Retail algorithms evaluate signals at exact bar boundaries (:00, :15, :30, :45), suffering from network congestion, broker queue latency, and adverse execution slippage. 
Our engine implements a **Dual-Tier 14th-Minute Architecture**:
- **Tier 1 (Execution Daemon)**: Runs continuously in the background. Employs a 10-second heartbeat to monitor open MT5 positions and trail stops in real time. At minute 14 (:14, :29, :44, :59 UTC), it triggers a comprehensive 360-degree multi-asset scan.
- **Tier 2 (AI Assistant Cron)**: Scheduled at `14,29,44,59 * * * *`, proactively waking up the AI model to synthesize orderflow depth, evaluate macro news catalysts, and formulate tactical adjustments for the upcoming bar.

```
15m Candle Timeline:
[Minute 00:00 ----------------------- Minute 14:00 ---------- Minute 15:00 / 00:00]
      |                                      |                        |
 Candle Open                           Wakeup Cadence           Candle Close &
                                       - Multi-Asset L2/L3      Next Bar Open
                                       - Macro Blackout Check   - Pre-staged Orders Filled
                                       - Confluence Scoring     - Ratchet Advances
                                       - Dynamic Risk Sizing
```

#### 3.2 360-Degree Data Ingestion
1. **Hyperdash Microstructure Orderflow (`http://localhost:8095`)**:
   - Level 2 Depth Imbalance: `(Bid_Vol - Ask_Vol) / (Bid_Vol + Ask_Vol)`.
   - Liquidation Heatmap: Quantified demand pools below price vs supply walls above price (within 3.0% price distance).
   - Level 3 Resting Whales: Large institutional limit orders (>= 150,000 USD notional) resolved to verified on-chain Ethereum wallet addresses.
   - Aggressor Trade Tape: Real-time tick stream segregating whale market buys vs sells.
2. **Web Macro & Calendar Intelligence**:
   - Automated RSS scraping of Tier-1 headlines with sentiment scoring (-1.0 to +1.0).
   - Mandatory +/- 15m blackout gate around Tier-1 releases (CPI, Core PCE, FOMC, NFP). If active, `BLACKOUT_VETO` prohibits all new positions.
3. **MetaTrader 5 (MT5) Execution Engine**:
   - Account: 5064568 (Blueberry Markets).
   - Symbol auto-discovery across `.p` and `.pi` variants (`SOLUSD.p`, `BTCUSD.pi`, `ETHUSD.pi`, `XRPUSD.pi`, `BNBUSD.p`).
   - Contract size scaling, lot normalization, and tick-level SL/TP modification.

---

### 4. RISK GOVERNANCE & MULTI-ASSET CONVICTION ENGINE

1. **Capital Base & Risk Sizing**:
   - Initial Capital: 5,000.00 USD.
   - Dynamic Conviction Risk Budget: **10.00 to 20.00 USD** per trade (0.20% to 0.40% of capital).
   - Conviction Tiers:
     * Score 3/6 (Baseline Confluence): 10.00 to 12.00 USD risk.
     * Score 4/6 (Whale Presence + Strong Liq Wall): 15.00 USD risk.
     * Score 5-6/6 (Full Orderflow Confluence + Macro Aligned): 20.00 USD risk.
   - Drawdown Defense Guardrail: If equity drops below 4,800.00 USD, risk automatically throttles to 10.00 USD.
   - Hard Circuit Breaker: 4.50% Drawdown Stop (Equity Floor: 4,775.00 USD).
   - Max Concurrent Positions: Strictly 2 simultaneous positions across all assets.

2. **Microstructure Exit Ratchet (Anti-Retracement Engine)**:
   - Initial Stop Loss: `Entry +/- 1.00R` (Proportional: `R_dist = round(price * 0.015, digits)`, minimum 25 points).
   - **Phase 0 (Breakeven Lock)**: When gain >= +0.80R, move SL to `Entry + 0.15R` (locks in guaranteed profit after 41 bps round-trip friction).
   - **Phase 1 (Profit Lock)**: When gain >= +1.50R, move SL to `Entry + 0.85R`.
   - **Phase 2 (Runner Trail)**: When gain >= +2.00R, trail SL dynamically at `Gain_R - 0.65R`.
   - **Dynamic Take Profit (TP)**: Maps overhead liquidation clusters and L3 whale ask walls, front-running supply walls by proportional offset `round(price * 0.001, digits)` (targeting +2.5R to +3.0R).

---

### 5. CURRENT LIVE DEPLOYMENT STATE (MT5 ACCOUNT 5064568)

- **Account Balance**: 4,742.90 USD | **Equity**: 4,841.40 USD | **Floating PnL**: +98.50 USD.
- **Active Positions (Max 2/2 Exposure Filled)**:
  1. `SOLUSD.p` Ticket #18464576: BUY 0.50 lots at 119.55 USD, current ~121.64 USD (+1.46R gain), SL at 120.96 USD (**+70.50 USD guaranteed profit locked**), TP at 122.78 USD (front-running 6,171,689 USD overhead short liquidation cascade wall).
  2. `XRPUSD.pi` Ticket #18474140: SHORT 1.00 lots at 1.498 USD, dynamic risk 15.00 USD (Conviction 4/6), SL at 1.528 USD (safely above 4.76M USD whale ask at 1.5258 USD and Blueberry 20-point stops level), TP at 1.474 USD (front-running 4.60M USD resting whale bid at 1.4731 USD). Floating PnL: -6.00 USD.

---

### 6. SPECIFIC CONSULTATION & AUDIT QUESTIONS FOR ARENA.AI

We request your forensic quantitative analysis on the following 5 strategic areas:

#### Question 1: Orderflow Entry Trigger Refinement
In `OF_Strategy.py`, our multi-asset entry trigger evaluates:
- Liquidation density (>= 100k and >= 500k USD)
- L2 depth volume imbalance (> +0.15 / < -0.15)
- L3 resting whale orders (>= 150k USD within 0.8% distance)
- Aggressive trade tape delta (whale buys > 1.5x whale sells)
*How can we mathematically optimize this scoring function? Should we incorporate Cumulative Volume Delta (CVD) slope divergence, sub-bar tick imbalance (imbalance ratios between bid/ask prints), or exponential time-decay on resting whale limit orders?*

#### Question 2: Cross-Asset Portfolio Beta & Hedging Governance
We currently hold `SOLUSD.p LONG` and `XRPUSD.pi SHORT`. While this naturally provides a market-neutral cross-crypto hedge, the position sizing was determined independently based on individual asset conviction.
*What quantitative framework (e.g. rolling covariance matrix, cointegration spread Z-score, or beta-neutral dollar weighting) should we implement to dynamically govern cross-asset risk when concurrent positions share underlying Bitcoin directional beta?*

#### Question 3: Dynamic Take Profit & Cascade Front-Running
Our dynamic TP algorithm identifies the nearest overhead liquidation band >= 200,000 USD located at least 2.0R away, and places the take-profit order 0.10 USD below it to front-run the cascade.
*Is front-running liquidation walls by 0.10 USD optimal across varying asset price scales (e.g. SOL at 120 USD vs BTC at 85,000 USD vs XRP at 1.50 USD)? How should we normalize this front-running offset using ATR or percentage of tick size?*

#### Question 4: Broker Friction, Spread Widening & Execution Defense
Blueberry Markets executes CFD perpetuals (`SOLUSD.p`, `BTCUSD.pi`, `XRPUSD.pi`). At candle open flushes (:00), spreads widen and liquidity temporarily dries up.
*How can we enhance `Terminal/MT5_Execution_Bridge.py` to prevent slippage on 15m candle closes? Should we pre-stage limit orders at the 14th minute (:14:30) inside the spread rather than firing market orders at candle open?*

#### Question 5: Lightweight Regime Classification
To complement our RSS news sentiment score (-1.0 to +1.0), we want to introduce a local, zero-latency market regime classifier (e.g. Volatility Regime via Parkinson / Garman-Klass volatility, or Trend Efficiency via Kaufman Adaptive Ratio).
*What lightweight mathematical formulation would you recommend to veto breakout trades during chop and veto mean-reversion trades during institutional momentum cascades?*

---

### 7. DESIRED DELIVERABLE

Please provide:
1. An **Architectural & Quantitative Scorecard** (Graded 1-10 across Microstructure Realism, Causal Rigor, Risk Governance, and Execution Latency).
2. **Mathematical formulations and pseudo-code/Python snippets** addressing Questions 1 through 5.
3. Recommended enhancements to be integrated directly into `Terminal/OF_Strategy.py` and `Terminal/MT5_Execution_Bridge.py`.
