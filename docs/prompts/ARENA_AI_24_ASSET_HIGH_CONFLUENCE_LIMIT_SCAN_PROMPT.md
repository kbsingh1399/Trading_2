# 🏛️ ARENA.AI 24-ASSET 360° TELEMETRY SCAN & HIGH-CONFLUENCE LIMIT ORDER COMMISSION

> **INSTRUCTIONS FOR USER**: Copy and paste the block below directly into Arena.ai. It mandates that Arena strictly evaluate our live telemetry snapshot across all 24 assets, debate whether to push limit trades now versus waiting for approach triggers, and deliver concrete candidate blueprints.

---

```markdown
# 🏛️ ARENA.AI MULTI-AGENT COUNCIL: 24-ASSET 360° TELEMETRY SCAN & HIGH-CONFLUENCE LIMIT TRADES

## 🎯 EXECUTIVE MANDATE & OBJECTIVE
The desk lead has issued an authoritative directive:
> *"Scan all 24 assets based strictly on live telemetry data, find high-confluence limit trade setups, debate with Antigravity whether we should push/stage limit orders now or wait for approach triggers, and deliver concrete execution blueprints."*

Antigravity and Arena.ai are operating in continuous collaborative governance over **MetaTrader 5 Account 5064568 (Blueberry Markets)**.
This review must be grounded **strictly in the live telemetry snapshot data points** synced to GitHub:
📂 **Live Telemetry Snapshot**: `docs/telemetry/live_snapshot_latest.json`
🌐 **GitHub Link**: https://github.com/kbsingh1399/Trading_2/blob/arena/83d03e3f-trading-2/docs/telemetry/live_snapshot_latest.json

---

## 📊 1. LIVE BROKER & ACCOUNT STATE (GROUND TRUTH)
From `docs/telemetry/live_snapshot_latest.json` (as of ~21:32 UTC):
- **Account Balance**: **4,811.62 USD** | **Equity**: **4,811.62 USD** (100% Cash)
- **Margin Used**: **0.00 USD** | **Free Margin**: **4,811.62 USD**
- **Active Positions**: **0 Open Positions**
- **Pending Orders**: **0 Resting Orders**
- **G-1 Hard Capital Floor**: **4,775.00 USD**
- **Mandatory Operating Buffer**: **>= +20.00 USD** (Hard floor defense threshold: **4,795.00 USD**)
- **Preserved Floor Cushion**: **+36.62 USD** (4,811.62 USD - 4,775.00 USD)
- **Stressed Available Headroom**: Strictly **16.62 USD** (4,811.62 USD - 4,795.00 USD)
- **Capacity Constraint**: Because each trade requires 1.25x nominal stop stress + 2.00 USD fee reserve, a 10.00 to 11.04 USD nominal risk order consumes 14.50 to 15.80 USD of stressed headroom. Therefore, **strictly ONE trade slot** is available until Phase 0 Break-Even is armed to recirculate risk. Two simultaneous 10.00 USD risk orders would consume 29.00 USD stressed headroom and project equity to 4,782.62 USD, violating the 4,795.00 USD floor threshold.

---

## 🔍 2. 24-ASSET MATRIX 360° TELEMETRY AUDIT
Arena must inspect the telemetry dictionary `assets_matrix_24` across all 24 institutional assets and apply our 5-gate institutional model:

### Gate 1: Spread & Friction Gate
- Audit MT5 `spread_bps` from the snapshot:
  * Prohibitive / Toxic Spreads (REJECT): DOGE (237 bps), DOT (189 bps), ADA (83 bps), SILVER (86 bps), NEAR (68 bps), LINK (65 bps), LTC (46 bps), XRP (42 bps), AVAX (27 bps).
  * Viable / Low-Spread Candidates:
    - **BTCUSD.pi**: ~1.92 bps (16.00 USD spread / tick size 0.01 / contract size 1.0)
    - **ETHUSD.pi**: ~12.85 bps (3.30 USD spread / contract size 1.0)
    - **BNBUSD.p**: ~9.10 bps (0.70 USD spread / contract size 1.0)
    - **SOLUSD.p**: ~19.00 bps (0.22 USD spread / contract size 100.0)
    - **SP500.p**: ~1.12 bps (0.87 pts spread / contract size 10.0)
    - **NAS100.p**: ~0.46 bps (1.42 pts spread / contract size 10.0)
    - **DJ30.p**: ~0.40 bps (2.04 pts spread / contract size 10.0)
    - **USWTI.p**: ~3.32 bps (0.030 USD spread / contract size 100.0)
    - **EURUSD.pi / GBPUSD.pi / USDJPY.pi**: 3.0 to 5.1 bps

### Gate 2: Causal Trend Regime & Retracement Geometry
- Inspect `causal_indicators`: `trend_regime`, `session_vwap_utc`, `vwap_z_score`, `atr_14`, `ema_200_slope_3h_pct`:
  * **BTC**: Bearish regime (EMA 200 slope -0.174%), VWAP 83,795.50 USD (Z = -0.86), ATR 210.88 USD, Bid 83,257 USD (distance to VWAP: 538 pts / 2.55x ATR).
  * **BNB**: Bearish regime, VWAP 769.16 USD (Z = +0.14), ATR 1.50 USD, Bid 769.00 USD (at VWAP!).
  * **SOL**: Bearish regime, VWAP 117.40 USD (Z = -1.17), ATR 0.42 USD, Bid 115.66 USD.
  * **SP500 / NAS100**: Bullish regime (EMA 200 positive slope), pullbacks to VWAP eligible for Long.
  * **USWTI**: Bearish regime, VWAP 91.05 USD (Z = -1.22), ATR 0.34 USD, Bid 90.28 USD.

### Gate 3: Causal Taker CVD Delta Confirmation
- Inspect `cvd_1m_buckets`, 5m, 15m, and 60m taker CVD deltas:
  * Are aggressive market orders exhausting? Is there divergence between price and CVD indicating passive limit absorption?

### Gate 4: Orderbook Depth & L2 Whale Walls
- Inspect `orderbook_live_depth`:
  * Are there verified resting ask walls (for shorts) or bid walls (for longs) >= 150k USD with >= 180s persistence within 0.25x ATR of proposed entries?
  * Note data provenance: Binance Futures is sampled anonymous L2; non-crypto assets report broker L1 only.

### Gate 5: G-1 Floor Defense & Broker Geometry
- Verify MT5 sizing: `contract_size`, `tick_size`, `digits`, `stops_level`.
- Enforce strict Stop Loss >= 1.50x ATR and Take Profit >= 2.50R target.
- Enforce nominal dollar risk between 10.00 and 11.04 USD (preserving >= +20.00 USD buffer above 4,775.00 USD floor).

---

## ⚔️ 3. THE DIALECTIC DEBATE: ADVANCE PASSIVE STAGING VS. APPROACH TRIGGER GATING
The user states: *"We should push limit trades... Antigravity can do itself and we can ask Arena.ai as well and both can debate."*

Arena must directly engage in this dialectic debate with Antigravity:
1. **The Antigravity Staging Thesis**:
   - Resting a passive limit order in advance at an established structural confluence shelf (e.g. Session VWAP 83,795 - 83,820 USD on BTC) provides queue priority, ensures 0 slippage on fill, and captures rapid sweep wicks that market participants cannot catch manually.
   - Capital risk is actively managed by a **drift & regime sentry**: if price drifts > 2.0x ATR away or breaks structure, the order is cancelled.
2. **The Arena CRO Risk Thesis**:
   - A resting order creates contingent fill risk against our narrow 16.62 USD stressed headroom.
   - If an order is staged 2.5x ATR below entry without an observable top-20 ask wall, a fast momentum sweep could fill the order at the exact moment of a breakout.
   - Therefore, staging should only occur when price approaches within 0.75x ATR AND an entry-level wall (>= 150k USD / 180s) is confirmed.
3. **The Dialectic Synthesis**:
   - Under what exact conditions is Arena willing to authorize staging a limit order?
   - Can an order be pre-staged if it has an automatic TTL / cancellation policy?
   - Or what are the exact numeric trigger thresholds (price, CVD, wall size) that must be met before Antigravity punches the order into MT5?

---

## 📋 4. CANDIDATE LIMIT SETUPS EVALUATION
Evaluate the following candidate setups across the 24-asset matrix:

### Candidate A: BTCUSD.pi — Bearish Model 2 VWAP Pullback Short
- Direction: `SELL LIMIT`
- Proposed Entry: **83,795.00 to 83,820.00 USD** (Anchored at Session VWAP / Resistance)
- Stop Loss: **84,350.00 USD** (Risk Distance: 530.00 - 555.00 USD | ~2.5x 15m ATR 210.88)
- Take Profit: **82,432.00 USD** (Reward Distance: 1,388.00 USD | **exactly 2.50R target**)
- Volume: **0.02 lots** (Contract Size: 1.0)
- Nominal Dollar Risk: **10.60 to 11.10 USD** (0.22% on equity)
- Stressed Risk: 15.25 to 15.88 USD -> Post-Loss Equity: **4,795.74 to 4,796.37 USD** (>= 4,795.00 USD buffer!)
- *Audit Questions*: Spot is currently at ~83,260 USD (~535 pts below entry). Does Arena approve pre-staging this order NOW, or does it mandate an approach trigger at >= 83,637 USD (within 0.75x ATR)?

### Candidate B: BNBUSD.p — Bearish Model 2 VWAP Pullback Short
- Direction: `SELL LIMIT`
- Current Quote: Bid 769.00 / Ask 769.70 | Session VWAP: **769.16 USD** (Price is directly at VWAP!)
- Proposed Entry: **769.50 USD**
- Stop Loss: **771.80 USD** (Risk Distance: 2.30 USD | 1.53x 15m ATR 1.50)
- Take Profit: **763.75 USD** (+2.50R target)
- Sizing Analysis: At contract size 1.0, risking 10.50 USD requires 4.56 lots (~4.5 lots), which requires **1,732 USD margin** (36% account margin).
- *Audit Questions*: Does the margin utilization make BNB inadvisable despite price being at VWAP?

### Candidate C: USWTI.p — Bearish Model 2 Continuation Short
- Direction: `SELL LIMIT`
- Proposed Entry: **90.950 USD** (Session VWAP 91.05 USD shelf)
- Stop Loss: **91.500 USD** (Risk Distance: 0.550 USD | 1.60x 15m ATR 0.343)
- Take Profit: **89.575 USD** (+2.50R target)
- Volume: **0.19 lots** (Contract Size: 100.0)
- Nominal Dollar Risk: 0.19 * 100 * 0.550 USD = **10.45 USD** (Clears the >= 10.00 USD minimum risk rule!)
- *Audit Questions*: USWTI has `UNAVAILABLE_L1_ONLY`. Can USWTI be traded on structural VWAP geometry alone, or is lack of Binance-style L2 an absolute disqualifier?

### Candidate D: Indices (SP500.p / NAS100.p) — Bullish Model 2 Pullback Long
- In the bullish equities regime, pullbacks to Session VWAP / EMA 50 provide trend continuation long setups.
- What is Arena's evaluation of staging a long hook on SP500 or NAS100?

---

## 🏆 5. REQUIRED DELIVERABLES FROM ARENA.AI
1. **Ranked 24-Asset Scan Verdict**: Group the 24 assets into:
   - Disqualified (toxic spreads / hostile regime / missing evidence)
   - Watchlist / Standby (viable spread, awaiting pullback or wall)
   - Qualified / Actionable (meeting all 5 gates)
2. **Definitive Dialectic Ruling on Limit Staging**:
   - Provide an explicit verdict: **Should Antigravity push any limit order to MT5 right now?**
   - If YES: Provide the exact broker symbol, order type, volume, limit price, SL, TP, and comment.
   - If NO (PUNCH NONE): Provide the exact, unambiguous **Approach Trigger Price** and **Minimum Orderbook Wall Criteria** for Candidate A (BTC) and any alternative candidates so Antigravity knows the precise microsecond to punch the order.
3. **Commit Section 32 to Collaborative Desk**:
   - Write your full analysis and findings as **Section 32: Arena 24-Asset Telemetry Scan & Dialectic Limit Ruling** in `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`.
   - Commit and push to `origin/arena/83d03e3f-trading-2`.
```
