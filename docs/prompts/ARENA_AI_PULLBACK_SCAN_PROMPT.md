# 🏛️ ARENA.AI 360° TELEMETRY DEEP STUDY & MULTI-AGENT PULLBACK COUNCIL COMMISSION

> **INSTRUCTIONS FOR USER**: Copy and paste this prompt into Arena.ai right now. It explicitly mandates that Arena deeply study our live telemetry data and deliberate across a multi-agent quantitative council before responding back with verified pullback setups.

---

```markdown
# 🏛️ ARENA.AI MULTI-AGENT COUNCIL: 360° TELEMETRY DEEP STUDY & MODEL 2 PULLBACK IDENTIFICATION

## 🎯 EXECUTIVE COMMISSION FROM DESK LEAD
Antigravity has published Section 17 to `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` (commit `afb5515` on `arena/83d03e3f-trading-2`).
The user has issued a direct mandate:
> *"Deeply study telemetry data and, based on that and multiple agent discussion, respond back with validated Model 2 pullback trades."*

While we maintain our mandatory observational blackout into the 18:00:00 UTC FOMC release, your mandate right now is to execute an exhaustive, data-driven investigation of our live telemetry stream, debate the findings across your internal specialist agents, and formulate concrete, verified pullback blueprints for our 18:35 UTC reopening queue.

---

## 📊 STEP 1: MANDATORY IN-DEPTH TELEMETRY DATA STUDY
Before forming opinions or proposing any trade, you MUST load and deeply inspect `docs/telemetry/live_snapshot_latest.json` (auto-synced every 60s from live MT5 L1 ticks and Binance L2 orderbooks across all 24 assets).

You must forensically extract and evaluate for every asset:
1. **L1 Broker Pricing & Spread Friction**: Live MT5 Bid, Ask, Spread in USD, and Spread in bps. Verify whether spread is <= 25 bps for crypto (SOL <= 0.28 USD) and <= 0.8 pips for FX (USDJPY <= 0.008 JPY). Reject spread-toxic pairs immediately.
2. **Anchored Daily Session VWAP (00:00 UTC) & Sigma Bands**: Current Session VWAP, 15m VWAP delta, Session Sigma, and VWAP Z-score (`vwap_z`). Check whether price is stretched or retracing toward the center VWAP / Value Area.
3. **Causal Moving Averages & Regime**: 15m EMA 20, EMA 50, EMA 200, and `ema_200_slope_pct`. Verify whether the higher-timeframe regime is unambiguously Bullish or Bearish.
4. **Binance Futures L2 Orderbook Depth & L3 Whale Walls**: Top-20 Bid vs Ask depth, Orderbook Imbalance (`imbalance`), Skew Ratio, and all persistent resting whale blocks (>= 150k USD with >= 180s persistence).
5. **Multi-Timeframe Taker CVD Deltas**: Inspect `cvd_1m_buckets`, 5m CVD, 15m CVD, and 60m CVD deltas to differentiate between active aggressive selling/buying and short-covering/dip-buying exhaustion.
6. **Structural Stop Clusters**: Examine `sell_stops` and `buy_stops` reconstructive levels to locate overhead and downside liquidity pools.

---

## 👥 STEP 2: MANDATORY MULTI-AGENT COUNCIL DIALECTIC (3 INTERNAL SPECIALISTS)
You MUST conduct a rigorous, cross-disciplinary debate among three distinct quantitative personas, detailing each agent's explicit findings:

### 1. Persona A: Lead Orderflow & Microstructure Specialist
- Examines orderbook depth, taker CVD deltas, and whale liquidity walls.
- Identifies where aggressive momentum is exhausting and passive absorption is stepping in.
- Rules whether an asset shows genuine orderflow rejection at structural levels or if it is a falling knife.

### 2. Persona B: Strategy Architect & Anti-Trap Sentry
- Enforces the **Model 2 Trend-Following Pullback Mandate**:
  * Prohibits knife-catching mean reversion (Model 1) in trending markets to avoid the losses seen earlier today.
  * For Bearish Trends: Qualifies ONLY bear-market rallies pulling back up into dynamic resistance (Session VWAP, Value Area High, or 50/200 EMA). Catches the rejection at the top of the retracement.
  * For Bullish Trends: Qualifies ONLY pullbacks dipping down into dynamic support (Session VWAP, Value Area Low, or 50/200 EMA).
- Calibrates exact broker geometry: MT5 `contract_size`, `tick_size`, Stop Loss (>= 1.50x ATR), Take Profit (+2.50R minimum), and position sizing for exactly 10.00 to 12.00 USD risk.

### 3. Persona C: Capital Floor & Microstructure Risk Guardian
- Enforces G-1 Hard Floor Defense: Account Balance 4,811.62 USD vs 4,775.00 USD Hard Floor (+36.62 USD cushion).
- Enforces the **Single-Fill Capacity Constraint**: Because available headroom above the mandatory +20.00 USD buffer is 16.62 USD, strictly ONE trade may be active at a time until Phase 0 Break-Even is locked.
- Enforces the 18:35 UTC Reopening Checklist (Spread normalization, 2 closed 15m post-FOMC candles, negative CVD, resting whale walls).

---

## 📐 STEP 3: FULLY SPECIFIED TRADE BLUEPRINTS (READY FOR 18:35 PUNCH)
Synthesize the multi-agent consensus and deliver the top 3 highest-confluence pullback blueprints:
1. **Broker Symbol**: (e.g. `SOLUSD.p`, `ETHUSD.pi`, `BTCUSD.pi`, `USDJPY.pi`)
2. **Direction**: `SELL LIMIT` (for bear rally pullbacks) or `BUY LIMIT` (for bull dip pullbacks)
3. **Exact Entry Price**: Anchored strictly to the structural retracement level (not current spot).
4. **Protective Stop Loss**: Verifying distance >= 1.50x ATR and placed beyond structural invalidation.
5. **Take Profit**: Calibrated to **+2.50R minimum** at the opposing liquidity target.
6. **Lot Size & Sizing Math**: Using broker `contract_size` to risk **exactly 10.00 to 12.00 USD** (preserving our +20.00 USD cushion above the 4,775.00 USD hard floor).
7. **Orderflow Punch Gate**: The exact trigger required at 18:35 UTC (e.g., negative 5m CVD flip, rejection candle close, spread <= 25 bps).

---

## 📝 STEP 4: DELIVER FORMAL BLACKBOARD ENTRY & PUSH TO GITHUB
1. Format your council findings and blueprints as **Section 18: Deep Telemetry Study & Multi-Agent Pullback Blueprints** in `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`.
2. Commit and push directly to `origin/arena/83d03e3f-trading-2`.
```
