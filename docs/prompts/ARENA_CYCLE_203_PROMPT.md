# 🏛️ JOINT QUANTITATIVE INVESTMENT COMMITTEE: CYCLE 203
## Collaborative Deliberation: Antigravity Desk & Arena.ai Council

### 1. OPERATIONAL CONTEXT & INSTITUTIONAL GOAL
- **Broker / Environment**: MetaTrader 5 (Blueberry Markets Live Challenge Server)
- **Account Number**: #5064568
- **Phase 1 Active Goal**: Pass evaluation by achieving **5,500.00 USD** balance/equity by **Friday, 23rd October 2026 (23:59 UTC)**.
- **Current Account State**:
  * Balance: 4,824.89 USD
  * Equity: 4,835.19 USD
  * Free Margin: 4,539.11 USD
  * Absolute Hard Floor: **4,775.00 USD** (Inviolate stop-out barrier; never breached).
  * Operating Defense Buffer: **4,795.00 USD** (Hard floor + 20.00 USD buffer).
  * Live Floor Cushion: **+60.19 USD** above 4,775.00 USD floor.
  * Live Buffer Cushion: **+40.19 USD** above 4,795.00 USD buffer.
- **Authorized Risk Envelope**: **15.00 to 25.00 USD** per trade (0.31% to 0.52% equity).
- **Execution Posture**: Strictly passive limit orders (`BUY_LIMIT` / `SELL_LIMIT`) with IOC / RETURN filling. Never cross the spread with market orders.

---

### 2. CANONICAL REPOSITORY & DATA SOURCES
Inspect the authentic repository state directly from GitHub:
- **Repository**: `https://github.com/kbsingh1399/Trading_2` (Branch `main`, latest commit `25be32aef`)
- **Live MT5 Account Telemetry**: `docs/telemetry/live_snapshot_latest.json` (Contains live equity, floor cushion, ticket #19146275 details, and 24-asset broker spread quotes).
- **Master 29-Sheet Excel Warehouse**: `Data/DataBase_Trading.xlsx` (Contains 29 market microstructure sheets: CVD, L2/L3 orderbook depth, whale orders >= $100K, liquidation ladders, stop maps, calendar, news).
- **Standardized Decision Chain**: `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`
- **Autonomous Wake-Up Checklist**: `docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md`
- **Active Goal Specification**: `docs/goals/PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md`

---

### 3. ACTIVE LIVE POSITION STATUS & RATCHET REVIEW
Audit the live MT5 position and verify whether any dynamic ratchet threshold has been reached:
- **Active Ticket**: #19146275 (`NAS100.p`)
  * Symbol: `NAS100.p`
  * Volume: 0.01 lot | Entry Price: 29,560.00 USD
  * Current Market Price: ~29,673.34 USD (+113.34 pts / +0.76R0 gain)
  * Current Stop Loss: **29,575.00 USD** (**100% Risk-Free**; +15.0 pts / +1.50 USD guaranteed minimum payout)
  * Take Profit Target: **29,715.00 USD** (+155.0 pts / +15.50 USD reward; only 41.66 pts from fill)
  * Dynamic Ratchet Rules:
    - Phase Early-BE (+0.75R0 to +0.80R0): Move SL to Entry + 0.10R0 [EXECUTED & LOCKED].
    - Phase 0 (+1.25R0 = 29,747.50 USD): Move SL to Entry + 0.15R0 (29,582.50 USD).
    - Phase 1 (+1.65R0 = 29,807.50 USD): Move SL to Entry + 0.80R0 (29,680.00 USD).
    - Time Decay: Exit at market if profit < +0.20R0 after 24 bars (6 hours).

---

### 4. MANDATORY 5-PILLAR CONFLUENCE EVALUATION STACK
Every trade candidate must pass all 5 institutional pillars:
1. **Pillar 1: Spread & Friction Gate**:
   - Crypto Perpetuals: Spread `<= 25.0 bps`. (Eligible: BTC ~1.8 bps, BNB ~8.0 bps, ETH ~11.4 bps, BCH ~20.2 bps, TRX ~21.2 bps, SOL ~22.5 bps).
   - TradFi CFDs: Spread `<= 5.0 bps`. (Eligible: EURUSD ~0.09 bps, GOLD ~0.19 bps, DJ30 ~0.22 bps, NAS100 ~0.36 bps, SP500 ~0.39 bps).
2. **Pillar 2: Orderflow & CVD Divergence**:
   - Taker Delta Accumulation: `Delta Spot > 0` AND `Delta Futures < 0` with divergence ratio `zc_div > 0.8`.
3. **Pillar 3: Dual-Engine Regime Classification**:
   - **Model 1 (Extreme Mean Reversion)**: Admissible ONLY in confirmed `MEAN_REVERT` regime with extreme location (`|Z_VWAP| >= 2.0 to 3.5 SD`) and RSI < 40 (longs) or > 60 (shorts).
   - **Model 2 (Trend Following Pullback)**: Admissible ONLY in confirmed `TREND_UP` or `TREND_DOWN` regime with pullback to verified structural shelf (20/50 EMA, Session VWAP) at in-range location (`|Z_VWAP| < 2.0 SD`).
   - If regime is `UNDEFINED`, stand aside unconditionally.
4. **Pillar 4: Resting L2/L3 Whale Backing & Liquidation Safety**:
   - Stop Loss MUST shelter safely behind a resting whale wall (`>= $100K USD`, persistence `>= 180s`) AND outside the nearest liquidation sweep band `[min_price, max_price] + 0.50 ATR`.
   - Never stage limit orders inside an un-swept retail stop cluster (`15_Hyperdash_Stops_Map`).
5. **Pillar 5: Macro & Calendar Blackout Gate**:
   - No new staging within `+-15 minutes` of high-impact crypto events or `+-35 minutes` of TradFi Tier-1 releases.

---

### 5. REQUIRED COUNCIL OUTPUT DELIVERABLES
Respond with a rigorous, professional quantitative investment committee memorandum containing:
- **SECTION A: ACCOUNT & FLOOR DEFENSE AUDIT**: Cushion verification (+60.19 USD above 4,775 USD) and progress to 5,500 USD goal.
- **SECTION B: ACTIVE POSITION & RATCHET VERDICT**: Ratification of Ticket #19146275 (`NAS100.p`) risk-free status.
- **SECTION C: INSTITUTIONAL CANDIDATE CENSUS**: Evaluation table of spread-qualified candidates.
- **SECTION D: DEEP CONFLUENCE AUDIT OF CANDIDATES**: Concrete analysis of orderbook depth, whale walls, liquidation bands, and stops.
- **SECTION E: FORMAL EXECUTION STAGING**: Ticket staging parameters (or mathematical Stand Aside).
