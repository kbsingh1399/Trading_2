# 🏛️ ARENA.AI MULTI-AGENT COUNCIL: PIVOT TO SYSTEMATIC TREND-FOLLOWING PULLBACKS (MODEL 2 OVERHAUL)

## 📌 CONTEXT & EMPIRICAL DIAGNOSIS: THE MEAN-REVERSION TRAP
Council Handshake & Systematic Audit: 2026-10-07 | Session Branch: `arena/83d03e3f-trading-2`
Target Account: Blueberry Markets MT5 `5064568` | Capital: 4,810.36 USD | Hard Floor: 4,775.00 USD

### 1. Empirical Forensic Breakdown of Today's Trades (2026-10-07):
Our trading book today provides incontrovertible empirical evidence of a fatal structural bias: **The Mean-Reversion Trap (Knife-Catching)**:
1. `EURUSD.pi` (Deal 16847110): Loss **-11.00 USD**. Attempted long mean-reversion at session discount while higher-timeframe dollar momentum was aggressively trending up. Stopped out.
2. `BTCUSD.pi` (Deal 16857838): Loss **-6.80 USD**. Attempted long flush catch at 83,380 USD against a 15m/4H markdown regime (below 200 EMA). Stopped out cleanly at 82,700 USD.
3. `USWTI.p` (Deal 16865551): Loss **-10.03 USD**. Staged BUY LIMIT at 90.740 USD seeking a deep flush mean-reversion catch beneath a synthetic 90.52 shelf. Oil was in a severe bearish momentum cascade (Z = -2.80 SD, falling 200 EMA). The knife sliced through bids and stopped out at 90.113 USD.
4. `SP500.p` (Deal 16861171): Gain **+3.87 USD**. Mean-reversion long off 7,770 USD session sweep. Barely bounced +0.80R before momentum stalled; forced exit at Phase 0 BE lock. Meanwhile, the second SP500 limit at 7,752 USD drifted 4.5+ ATR away because the market ripped away in a relentless trend continuation!
5. `USDJPY.pi` (Ticket #18644889): **CURRENTLY RUNNING & PROFITABLE (+3.50 to +4.66 USD floating / +0.52R)**. Stop loss moved to **158.046 USD** (Phase 0 BE / profit lock armed with retcode 10009). Downside risk is **0.00 USD**. 
   - **WHAT IS THIS TRADE?** It was executed under **Model 2: Trend-Continuation Pullback**! Price was trading above the 200 EMA (bullish regime). We waited for price to pull back toward Session VWAP / Value Area, and bought in the direction of the dominant momentum! It immediately worked, locked profit, and eliminated downside risk!

### 2. The Core Quant Problem:
In crypto and momentum macro assets, strong trends do not easily mean-revert. Assets at Z = -2.0 SD frequently cascade to Z = -3.5 SD or -5.0 SD due to stop-runs and liquidation cascades. Trying to pick tops and bottoms via Model 1 (Extreme Mean Reversion) exposes the book to adverse selection and negative drift.

---

## 🎯 MANDATORY TASK FOR ARENA.AI
Arena.ai, as our Quantitative Strategy and Governance Partner, you are tasked with executing a complete pivot across our 24-asset universe from knife-catching mean reversion to **Systematic Trend-Following Pullbacks (Model 2 Overhaul)**.

### Scope of Analysis:
Using the latest real-time telemetry from `docs/telemetry/live_snapshot_latest.json` on branch `arena/83d03e3f-trading-2` (synchronized every 60 seconds from live MT5 L1 ticks and Binance L2 depth across all 24 assets):

1. **Systematic Trend Regime Classification (15m + 4H Causal Trend)**:
   - Classify all 24 assets into:
     * **BULLISH TREND REGIME**: Price > 15m 200 EMA AND 200 EMA slope > 0 AND Daily Session VWAP slope > 0.
     * **BEARISH TREND REGIME**: Price < 15m 200 EMA AND 200 EMA slope < 0 AND Daily Session VWAP slope < 0.
     * **CHOP / RANGE-BOUND**: Price oscillating around 200 EMA with flat slope. (DISQUALIFIED FROM NEW TRADES).

2. **The Trend-Following Pullback Architecture (Model 2 Rules)**:
   - **For Bullish Trends (Longs Only — Absolutely Zero Knife-Catch Shorts)**:
     * Wait for a retracement back into dynamic value: Session VWAP, Value Area Low (VAL), or 15m 50/200 EMA confluence.
     * Orderflow Confirmation: Delta absorption (CVD divergence showing selling exhaustion into the support band) + presence of resting bid depth.
     * Invalidation: Stop loss placed strictly below the pullback swing shelf (minimum 1.50x ATR floor).
     * Profit Targets: Overhead liquidity magnets (recent swing high, resting buy-stop pools, +2.50R minimum).
   - **For Bearish Trends (Shorts Only — Absolutely Zero Knife-Catch Longs)**:
     * Wait for bear-market rallies that retrace UP into dynamic resistance: Session VWAP from below, Value Area High (VAH), or 200 EMA.
     * Orderflow Confirmation: CVD divergence showing buyer exhaustion / absorption at the resistance shelf + resting ask depth.
     * Invalidation: Stop loss placed strictly above the rally swing high (minimum 1.50x ATR floor).
     * Profit Targets: Downside liquidity pools (recent swing low, cascading sell stops, +2.50R minimum).

3. **Asset-by-Asset Audit & Candidate Selection across 4 Clusters**:
   - **Cluster A: Crypto Perpetuals (Binance / Blueberry CFD)**:
     * Evaluate `SOLUSD.p`: 15m EMA200 is at 119.12 USD (falling, bearish regime). Pullback rally toward 118.00 USD represents a high-confluence Model 2 Bearish Pullback Short. Specify exact entry, SL, TP, contract sizing (contract_size=100 -> 0.07 lots for 10.50 USD risk), and orderflow triggers (completed 15m candle close rejecting below 117.87 USD).
     * Evaluate `BNBUSD.p`: 15m EMA200 at 776.46 USD (falling). Rally toward 770.00 USD represents a Model 2 Bearish Pullback Short. Specify exact geometry (contract_size=1 -> 2.83 lots for 10.02 USD risk, TP 761.15 USD).
     * Evaluate `TRXUSD.p`, `BTCUSD.pi`, `ETHUSD.pi`, `DOGEUSD.p`, `NEARUSD.p`, `AVAXUSD.p`.
   - **Cluster B: Foreign Exchange**:
     * Evaluate `USDJPY.pi`: Bullish trend pullback continuation Long @ 158.140 USD (Hawkish FOMC scenario).
     * Evaluate `GBPUSD.pi`: Bullish trend reversal Long @ 1.32090 USD (Dovish FOMC scenario).
   - **Cluster C: Equity Indices**:
     * Evaluate `SP500.p`, `NAS100.p`, `DJ30.p`, `GER40.p` under trend-following rules (buying pullbacks in uptrends or shorting pullbacks in downtrends).
   - **Cluster D: Commodities**:
     * Evaluate `GOLD` (XAUUSD) and `USWTI` (Crude Oil) — do not catch falling knives in Oil; evaluate rally-short setups or wait for confirmed trend reversal.

4. **Strict Execution & Floor Defense Governance**:
   - Capital Floor: **4,775.00 USD** on account balance **4,810.36 USD**.
   - Floor Cushion Invariant: Every individual trade and joint multi-fill scenario must strictly preserve **>= +20.00 USD cushion** above the 4,775.00 USD floor at all times.
   - Dynamic Risk Budget: **10.00 to 14.50 USD per trade** (0.20% to 0.29% of capital).
   - Timeline Protocol:
     * Blackout Window: 17:00:00 to 18:30:00 UTC (100% frozen, zero new orders).
     * FOMC Minutes Release: 18:00:00 UTC.
     * Post-FOMC Reopening: 18:35:00 UTC.
     * Deliver machine-readable, fully validated trade plans for immediate staging at 18:35:00 UTC!

---

## 📋 ARENA.AI DELIVERABLES REQUIRED:
1. **Regime Diagnostic Matrix**: A table mapping each of the 24 assets to its causal trend regime (Bullish / Bearish / Chop) and identifying its dynamic pullback zone.
2. **Top 3 Priority Trend-Following Setups for 18:35 UTC**:
   - Exact broker symbol, direction (BUY/SELL), entry limit price, stop loss (with ATR-floor verification), take profit (+2.50R target), lot size calculated using MT5 contract size, dollar risk (10.00 to 14.50 USD), and orderflow confluence triggers.
3. **Formal Ratification of Collaborative Order Desk Section 12**:
   - Confirm receipt of Antigravity's Section 12 update on `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` and ratify the Phase 0 armed status of `USDJPY.pi` #18644889.
