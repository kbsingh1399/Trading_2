# 📋 INSTITUTIONAL ORDERFLOW & MICROSTRUCTURE LIVE EXECUTION CHECKLIST
> **Canonical Operational Checklist for 15-Minute Candle AI Trader & MT5 Bridge**  
> **Mandatory Reference for Order Placement, Dynamic SL Ratchets, and Smart TP Extensions**

---

## 🏛️ OVERVIEW & INVARIANT HIERARCHY
This checklist governs all trade admissions, pending order stagings, and live position modifications on MetaTrader 5 Account 5064568. Every decision must strictly satisfy each verification gate sequentially. If any gate fails, execution defaults to **HOLD** or **VETO**.

- **Inviolable Capital Floor**: 4,775.00 USD (anchored to 5,000.00 USD initial capital; 4.50% hard drawdown stop).
- **Risk Budget**: 10.00 to 20.00 USD per trade, dynamically scaled by orderflow confluence and resting L3 whale presence.
- **Maximum Concurrent Positions**: Strictly capped at 2 concurrent active positions across all 16 assets.
- **Zero Dollar Signs**: All monetary values are recorded in USD. No raw LaTeX delimiters.

---

## 🔍 SECTION 1: PRE-ORDER ADMISSION GATE (ENTRY CHECKLIST)
Before any market order is sent or limit order is staged, verify all 7 sub-gates:

### Gate 1.1: Price Action & Structural Geometry
- [ ] **15-Minute Candle Close Quality**:
  - For Longs: Candle closes in upper 30% of range (`(close - low) / (high - low) >= 0.70`).
  - For Shorts: Candle closes in lower 30% of range (`(close - low) / (high - low) <= 0.30`).
- [ ] **Higher Timeframe (HTF) Trend Alignment**:
  - 4-Hour 200 EMA slope must be strictly positive for longs (`ema200[t] >= ema200[t-12]` over 3 hours) and negative for shorts, evaluated with causal `shift(1)` backward-as-of join.
- [ ] **ICT Fair Value Gap (FVG) & Consequent Encroachment (CE)**:
  - Verify 3-bar imbalance zone.
  - Consequent Encroachment (50% midpoint) must be strictly untouched (`ce_untouched == True`).
- [ ] **Anchored VWAP & Sigma Band Dispersion**:
  - For Longs: Price discounted below session VWAP (`(price - vwap) / vwap_sigma <= -0.50`).
  - For Shorts: Price extended above session VWAP (`(price - vwap) / vwap_sigma >= +0.50`).
- [ ] **Daily Pivots & Swing Anchors**:
  - Identify Daily classical pivots (P, S1, R1, S2, R2) and rolling 8-bar swing extremes (`swing_high`, `swing_low`).

### Gate 1.2: Orderflow & Microstructure Footprints
- [ ] **Cumulative Volume Delta (CVD) Divergence**:
  - For Longs: Spot CVD rising while Futures price drops (`zc_div > 0.80`), indicating institutional spot absorption.
  - For Shorts: Spot CVD falling while Futures price pops, indicating institutional spot distribution.
- [ ] **Tick Aggressor Imbalance**:
  - Aggressive taker flow signed in trade direction (`(buys - sells) / total_volume` agrees with direction).
- [ ] **Absorption at Extremes**:
  - Large tick volume executed at candle wicks with minimal price continuation, signaling passive institutional limit defense.

### Gate 1.3: Level 2 (L2) Orderbook Depth & Micro-Spread
- [ ] **20-Level Depth Imbalance**:
  - Top-20 depth ratio `(bid_depth - ask_depth) / (bid_depth + ask_depth)` favors entry direction.
- [ ] **Broker Micro-Spread & Cost Gate**:
  - Live bid-ask spread `(ask - bid) / mid * 10,000 <= 15.0 bps`.
  - Rejects if spread exceeds stops level or freeze level.

### Gate 1.4: Level 3 (L3) Whale Order Verification
- [ ] **Minimum Whale Notional**: Single resting limit order must be `>= 150,000 USD`.
- [ ] **Persistence Gate (Anti-Spoofing)**: Order must maintain continuous presence for `>= 180 seconds`.
- [ ] **Freshness Gate**: Order verified on book within the last 30 seconds.
- [ ] **Corridor Proximity**: Resting wall located within `0.5 * ATR` of mid-price.
- [ ] **Execution Buffer (Front-Running)**:
  - Staging limit orders strictly 1 to 2 ticks inside the whale wall (front-running the queue rather than joining).

### Gate 1.5: Liquidation Corridors & Fuel-to-Friction Ratio (FFR)
- [ ] **Squeeze Exhaustion Veto**:
  - Strictly veto Short entries if `short_liq_zs >= 1.0` (active short squeeze).
  - Strictly veto Long entries if `long_liq_zs >= 1.0` (active long liquidation cascade).
- [ ] **Fuel-to-Friction Ratio (FFR)**:
  - Reachable forced liquidation dollar volume exceeds opposing resting book depth along the path to target.
  - Veto if target fuel is absent or opposing friction is dense.

### Gate 1.6: Macro Narrative & Economic Blackout Gate
- [ ] **Live NLP Sentiment Score**:
  - RSS headline sentiment score must not oppose trade direction (score >= -0.30 for longs; <= +0.30 for shorts).
- [ ] **Tier-1 Macro Blackout Shield**:
  - Ensure current time is OUTSIDE the `+/- 15-minute` blackout window for:
    * US CPI (Consumer Price Index)
    * Core PCE Price Index
    * FOMC Rate Decisions & Press Conferences
    * Non-Farm Payrolls (NFP)

### Gate 1.7: Cross-Asset Covariance & Drawdown Floor Sizing
- [ ] **Unencumbered Risk Room Check**:
  - Compute `Unencumbered Room = max(0, Equity - 4,775.00 USD - Active_Stop_Reserve) * 0.90`.
  - Required trade risk (stop loss distance + 41 bps friction) must be `<= Unencumbered Room`.
- [ ] **Portfolio Variance Budget**:
  - Incremental portfolio standard deviation via Ledoit-Wolf covariance matrix must satisfy `sigma <= 45.00 USD`.
- [ ] **Concurrency Slot Availability**:
  - Total active positions + pending staged limits must be `< 2` (or `< 3` in verified House Money mode).

### Gate 1.8: Unified 4-Tier Orderflow Confluence (Spikes, Pools & Depth)
- [ ] **Tier 1: L3 Resting Whale Orders**: Identify active limit walls `>= 150k USD` with `>= 180s` persistence that provide structural armor or target ceilings.
- [ ] **Tier 2: Liquidation Cascade Spikes**: Map reachable liquidation corridors (long liquidations below / short liquidations above). Ensure trade rides the cascade momentum toward the spike rather than entering into an opposing exhaustion spike.
- [ ] **Tier 3: Stop-Loss Run Pools**: Quantify major retail stop clusters (sell-stops below key swing lows / buy-stops above swing highs) that act as liquidity magnets.
- [ ] **Tier 4: Orderbook Resting Depth & Liquidity Vacuums**: Audit net L2 bid/ask depth between current price and target. Verify that target lies within or immediately after a liquidity vacuum where price accelerates friction-free.

---

## 🛡️ SECTION 2: SMART STOP LOSS (SL) MANAGEMENT & RATCHETS
Once a position is filled, manage protective stops using this deterministic 4-stage hierarchy:

### Stage 2.0: Protective Initial Stop Loss
- [ ] Placed at Entry minus 1.5 * ATR (or structural swing extreme / 2 ticks behind resting L3 whale shield).
- [ ] Stop loss price explicitly registered on the broker server upon order entry.

### Stage 2.1: Phase 0 Break-Even Lock (+0.80R Gain)
- [ ] **Trigger**: Floating gain reaches `+0.80R` (`sign * (price - entry) / initial_r >= 0.80`).
- [ ] **Action**: Advance Stop Loss to `Entry + 0.35R` (signed in trade direction).
- [ ] **Math Invariant**: Guarantees full coverage of 41 bps round-trip broker friction with positive locked profit.

### Stage 2.2: Phase 1 Profit Lock (+1.50R Gain)
- [ ] **Trigger**: Floating gain reaches `+1.50R`.
- [ ] **Action**: Advance Stop Loss to `Entry + 0.80R` (signed in trade direction).
- [ ] **Whale Shield Anchor**: If an L3 mega-whale wall (`>= 500k USD`) sits between Entry and Entry + 0.80R, tuck the Stop Loss 2 ticks behind the wall to use institutional resting orders as physical armor.

### Stage 2.3: Phase 2 Trailing Lock (+2.00R Gain)
- [ ] **Trigger**: Floating gain reaches `+2.00R`.
- [ ] **Action**: Trail Stop Loss at `max(1.50R, gain_r - max(0.50, ATR / initial_r))`.
- [ ] **Rule**: Stop Loss moves only in the favorable direction; never loosen a trailed stop.

---

## 🎯 SECTION 3: SMART TAKE PROFIT (TP) & VACUUM EXTENSIONS
Manage profit targets dynamically based on orderbook liquidity distribution:

### Stage 3.1: Structural Base Target (+2.00R to +2.50R)
- [ ] Base TP placed at `+2.00R to +2.50R` from entry.
- [ ] Front-run opposing mega-whale walls by 1 to 2 ticks (e.g. for shorts, place TP above resting whale bids).

### Stage 3.2: Liquidity Vacuum Extension Condition
- [ ] **Evaluation Criteria**: If price approaches base TP and Hyperdash L2/L3 orderbook shows a **complete liquidity vacuum** beyond it (opposing resting depth drops to near-zero with projected liquidation bands sitting lower):
  - [ ] **Action**: Extend TP into the next resting liquidity cluster (e.g. extending Silver TP from 60.650 to 59.800 USD).
  - [ ] **Mandatory Prerequisite**: The Stop Loss MUST simultaneously be advanced into Phase 2 trailing lock (minimum +1.50R locked) before any TP extension is committed. Never extend TP while leaving capital unprotected!

---

## ⏱️ SECTION 4: INVALIDATION & STALE ORDER PURGE PROTOCOL

### Rule 4.1: 24-Bar Time Decay (Stagnant Positions)
- [ ] If an open trade fails to reach `+0.20R` gain within 24 bars (6 hours / 360 minutes), exit immediately at market. Eliminates dead-capital opportunity cost.

### Rule 4.2: Staged Limit Order Invalidation
- [ ] Cancel and re-evaluate any pending limit order if:
  * The underlying L3 whale wall is cancelled or disappears for > 60 seconds.
  * Price moves away by more than `1.5 * ATR` without filling.
  * A Tier-1 macro blackout window activates.
  * Portfolio unencumbered drawdown room decreases below the required budget.

---

## 📊 OPERATIONAL SCORECARD SUMMARY FORMAT (Turn Output Template)
On every 14th-minute wake-up, format the in-session council report using this exact structure:

```markdown
### 🛡️ 15-Minute Candle AI Trader Telemetry Report (:XX UTC)

#### 1. Active Position Lifecycle (Pillar 8)
- Ticket #XXXXX: Asset [Direction] | Entry: X.XX USD | Current: X.XX USD | PnL: +XX.XX USD (+X.XXR)
- SL: X.XX USD [Phase X Lock] | TP: X.XX USD | Next Ratchet Trigger: X.XX USD

#### 2. Unified 4-Tier Orderflow Confluence Map (Microstructure Blueprint)
- Overhead Resistance: [L3 Whale Asks] + [Buy Stop Pools] + [Short Liquidation Spikes]
- Price Level: >>> Current Price <<<
- Downside Targets: [Long Liquidation Spikes] + [Sell Stop Cascades] + [L2/L3 Bids & Vacuums]

#### 3. Candidate Setup Evaluation (Pillars 1–6)
- Asset | Confluence | L3 Whale Backing | Liquidation FFR | Decision & Exact Rationale

#### 4. Capital & Risk Governance (Pillar 7)
- Equity: X,XXX.XX USD | Hard Floor: 4,775.00 USD | Buffer: XX.XX USD | Unencumbered Room: XX.XX USD
- Active Slots: X/2 Filled | Pending Limits: [Ticket #XXXXX]
```
