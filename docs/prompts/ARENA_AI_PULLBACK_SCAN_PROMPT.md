# 🏛️ ARENA.AI 360° TELEMETRY PULLBACK ANALYSIS COMMISSION

> **INSTRUCTIONS FOR USER**: Copy and paste this prompt into your Arena.ai chat session right now. It tasks Arena with performing a deep 360-degree scan of the 24-asset telemetry to identify and specify every viable Model 2 Trend-Following Pullback entry for our post-FOMC order queue.

---

```markdown
# 🏛️ ARENA.AI MULTI-AGENT COUNCIL: 360° TELEMETRY DEEP SCAN & MODEL 2 PULLBACK IDENTIFICATION

## 🎯 EXECUTIVE COMMISSION FROM DESK LEAD
Antigravity has published Section 17 to `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` (commit `afb5515` on `arena/83d03e3f-trading-2`).
The user has directed us: *"further ask arena.ai to do deep analysis of telemetry and identify pullback trades"*.

While we maintain our mandatory observational blackout into the 18:00:00 UTC FOMC release, your mandate right now is to perform a **forensic, 360-degree quantitative scan of the 24-asset universe** in `docs/telemetry/live_snapshot_latest.json` to identify, design, and mathematically calibrate every high-confluence Model 2 Trend-Following Pullback trade.

---

## 🔬 STEP 1: CAUSAL TREND & PULLBACK GEOMETRY AUDIT (ALL 24 ASSETS)
Analyze all 24 assets across Crypto, FX, Indices, and Commodities:
1. **Regime Classification**:
   - Classify each asset into **Strong Bearish Trend**, **Strong Bullish Trend**, or **Chop / Range**.
   - Check Price vs 15m 200 EMA, 15m EMA slope, and Session VWAP slope.
2. **Pullback Retracement Zones (No Chasing)**:
   - For Bearish Trending Assets: Identify where the dynamic resistance shelf sits (Session VWAP, Value Area High, or 50/200 EMA). We will NOT chase the breakdown lows; we want to catch the reflex rally back into resistance!
   - For Bullish Trending Assets: Identify where the dynamic support shelf sits (Session VWAP, Value Area Low, or 50/200 EMA).
3. **Microstructure & Orderflow Confirmation**:
   - Check 1m/5m/15m taker CVD to identify whether buyers or sellers are exhausting.
   - Inspect top-20 orderbook depth and locate the nearest resting whale liquidity walls (>= 150k USD).
   - Verify broker spread in MT5 specs (must be <= 25 bps for crypto, <= 0.8 pips for FX).

---

## 📐 STEP 2: FULLY SPECIFIED TRADE BLUEPRINTS (READY FOR 18:35 PUNCH)
For the top 3 highest-confluence pullback candidates, provide the exact executable blueprint:
1. **Broker Symbol**: (e.g. `SOLUSD.p`, `ETHUSD.pi`, `BTCUSD.pi`, `USDJPY.pi`)
2. **Direction**: `SELL LIMIT` (for bear rally pullbacks) or `BUY LIMIT` (for bull dip pullbacks)
3. **Exact Entry Price**: Anchored strictly to the structural retracement level (not current spot).
4. **Protective Stop Loss**: Verifying distance >= 1.50x ATR and placed beyond structural invalidation.
5. **Take Profit**: Calibrated to **+2.50R minimum** at the opposing liquidity target.
6. **Lot Size & Sizing Math**: Using broker `contract_size` to risk **exactly 10.00 to 12.00 USD** (preserving our +20.00 USD cushion above the 4,775.00 USD hard floor).
7. **Orderflow Punch Gate**: The exact trigger required at 18:35 UTC (e.g., negative 5m CVD flip, rejection candle close, spread <= 25 bps).

---

## 📝 STEP 3: APPEND SECTION 18 & PUSH TO GITHUB
1. Format your findings as **Section 18: Deep 360° Pullback Opportunity Blueprints** in `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`.
2. Commit and push directly to `origin/arena/83d03e3f-trading-2`.
```
