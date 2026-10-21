# 🏛️ ARENA.AI STANDARD INSTITUTIONAL COUNCIL PROMPT TEMPLATE
## Co-Equal Quantitative Investment Committee Briefing & Deliberation Spec

> **Document Status**: CANONICAL PRODUCTION PROMPT TEMPLATE  
> **Council Participants**: Antigravity (Live MT5 Decision Desk) & Arena.ai (Forensic Quant Council)  
> **Target Account**: Blueberry Markets MT5 Account #5064568  
> **Active Goal**: Pass Phase 1 Challenge (Target: 5,500.00 USD) by End of Friday, 23rd October 2026  
> **Canonical Repo**: `https://github.com/kbsingh1399/Trading_2.git` (Branch `main`)  
> **Master Data Warehouse**: `Data/DataBase_Trading.xlsx` (29 Canonical Worksheets) & `docs/telemetry/live_snapshot_latest.json`

---

## 📋 PROMPT TEMPLATE FOR ARENA.AI (INJECT INTO CDP PROSEMIRROR EDITOR)

```markdown
# 🏛️ JOINT QUANTITATIVE INVESTMENT COMMITTEE: CYCLE {CYCLE_ID}
## Collaborative Deliberation: Antigravity Desk & Arena.ai Council

### 1. OPERATIONAL CONTEXT & INSTITUTIONAL GOAL
- **Broker / Environment**: MetaTrader 5 (Blueberry Markets Live Challenge Server)
- **Account Number**: #5064568
- **Phase 1 Goal**: Pass evaluation by achieving **5,500.00 USD** balance/equity by **Friday, 23rd October 2026 (23:59 UTC)**.
- **Current Account State**:
  * Balance: {BALANCE} USD
  * Equity: {EQUITY} USD
  * Free Margin: {FREE_MARGIN} USD
  * Absolute Hard Floor: **4,775.00 USD** (Inviolate stop-out barrier; never breached under any circumstances).
  * Operating Defense Buffer: **4,795.00 USD** (Hard floor + 20.00 USD buffer).
  * Live Floor Cushion: {CUSHION_FLOOR} USD
  * Live Buffer Cushion: {CUSHION_BUFFER} USD
- **Authorized Risk Envelope**: **15.00 to 25.00 USD** per trade (0.31% to 0.52% equity).
- **Execution Posture**: Strictly passive limit orders (`BUY_LIMIT` / `SELL_LIMIT`) with IOC / RETURN filling. Crossing the bid-ask spread with aggressive market orders is strictly prohibited.

---

### 2. CANONICAL REPOSITORY & DATA SOURCES
Inspect the authentic, verified state directly from the canonical GitHub repository:
- **Repository**: `https://github.com/kbsingh1399/Trading_2` (Branch `main`)
- **Live Account Telemetry Snapshot**: `docs/telemetry/live_snapshot_latest.json`
- **Master 29-Sheet Excel Warehouse**: `Data/DataBase_Trading.xlsx`
- **Standardized Decision Chain**: `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`
- **Autonomous Wake-Up Checklist**: `docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md`
- **Active Goal Specification**: `docs/goals/PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md`

#### Master 29-Sheet Data Warehouse Taxonomy:
- **Sheet 00 & 01**: `Crypto_ETF_Flows` & `1_Crypto_ETF_Flows` (Institutional Spot ETF creations/redemptions: IBIT, FBTC, ETHA).
- **Sheet 02**: `2_Spot_Netflow_S` (CEX spot exchange inflow/outflow across 500 assets).
- **Sheets 03, 04, 05**: `3_Exchanges_LS_Ratio_15M`, `1H`, `4H` (Multi-exchange retail long/short crowding).
- **Sheet 06**: `4_Hyperliquid_Analysis` (Decentralized whale intelligence on Hyperliquid L1).
- **Sheet 07**: `5_OI` (Futures Open Interest trend and conviction across 18 perpetuals).
- **Sheet 08 & 09**: `5_Funding_Rate` & `6_Funding_Fee_Settlement` (Cross-exchange funding rates and holding carry friction).
- **Sheet 10 & 11**: `7_Liq_Heapmap` & `7_Live_Liq` (Clustered liquidation heatmap and real-time forced liquidation stream).
- **Sheet 12 & 17**: `8_Exchange_Liquidation_Map_1D` & `7D` (Exchange liquidation surface boundaries and magnet levels).
- **Sheets 13, 14, 15, 16**: `9_Liquidation_Max_Pain_24H`, `48H`, `3D`, `7D` (Gravitational max pain strikes).
- **Sheet 18**: `10_Whale_Orders` (Resting institutional whale walls >= $100K with persistence >= 180s).
- **Sheet 19**: `11_Technical` (VWAP bands, VWAP Z-score, 20/50/200 EMAs, RSI-14, ATR-14, Volume Profile POC/VAH/VAL).
- **Sheet 20 & 21**: `12_Hyperdash` & `13_Hyperliquid` (Hyperdash flow sentiment, DEX premium/discount, net taker flow).
- **Sheet 22**: `14_Hyperdash_Liq_Map` (Continuous dollar-by-dollar liquidation ladder).
- **Sheet 23**: `15_Hyperdash_Stops_Map` (Resting stop orders ladder; sweep trap detection).
- **Sheet 24**: `16_Hyperdash_telegram_Intel` (Real-time institutional Telegram whale flow intelligence).
- **Sheet 25**: `17_Orderbook` (L2/L3 orderbook depth, asymmetry ratio, and whale wallet attribution).
- **Sheet 26**: `18_CVD` (Continuous CVD engine: Spot vs Futures taker volume, delta divergence, zc_div).
- **Sheet 27 & 28**: `19_News` & `19_Calendar` (Forex Factory live news and macroeconomic Tier-1 calendar).

---

### 3. ACTIVE LIVE POSITION STATUS & RAT CHET REVIEW
Audit the live MT5 position and verify whether any dynamic ratchet threshold has been reached:
- **Active Ticket**: {ACTIVE_TICKET_DETAILS}
  * Symbol: `NAS100.p` (Ticket #19146275)
  * Volume: 0.01 lot | Entry: 29,560.00 USD
  * Current Stop Loss: **29,575.00 USD** (100% Risk-Free; +15.0 pts / +1.50 USD locked profit)
  * Take Profit Target: **29,715.00 USD** (+155.0 pts / +15.50 USD reward)
  * Dynamic Ratchet Rules:
    - Early-BE (+0.75R0 to +0.80R0): Move SL to Entry + 0.10R0 [ACTIVE & EXECUTED].
    - Phase 0 (+1.25R0 = 29,747.50 USD): Move SL to Entry + 0.15R0 (29,582.50 USD).
    - Phase 1 (+1.65R0 = 29,807.50 USD): Move SL to Entry + 0.80R0 (29,680.00 USD).
    - Time Decay: Exit at market if profit < +0.20R0 after 24 bars (6 hours).

---

### 4. MANDATORY 5-PILLAR CONFLUENCE EVALUATION STACK
Every trade candidate must pass all 5 institutional pillars:
1. **Pillar 1: Spread & Execution Friction Gate**:
   - Crypto Perpetuals: Spread must be `<= 25.0 bps`. (Eligible: BTC ~1.8 bps, BNB ~8.0 bps, ETH ~11.4 bps, BCH ~20.2 bps, TRX ~21.2 bps, SOL ~22.5 bps. All other crypto perpetuals disqualified).
   - TradFi CFDs: Spread must be `<= 5.0 bps`. (Eligible: EURUSD ~0.09 bps, GOLD ~0.19 bps, DJ30 ~0.22 bps, NAS100 ~0.36 bps, SP500 ~0.39 bps).
2. **Pillar 2: Orderflow & CVD Divergence**:
   - Taker Delta Accumulation: `Delta Spot > 0` AND `Delta Futures < 0` with divergence ratio `zc_div > 0.8`.
   - Absorption verification: Aggressive selling absorbed by resting passive limit buying.
3. **Pillar 3: Dual-Engine Regime Classification**:
   - **Model 1 (Extreme Mean Reversion)**: Admissible ONLY in confirmed `MEAN_REVERT` regime with extreme location (`|Z_VWAP| >= 2.0 to 3.5 SD`) and RSI < 40 (longs) or > 60 (shorts).
   - **Model 2 (Trend Following Pullback)**: Admissible ONLY in confirmed `TREND_UP` or `TREND_DOWN` regime with pullback to verified structural shelf (20/50 EMA, Session VWAP, VAH/VAL) at in-range location (`|Z_VWAP| < 2.0 SD`).
   - If regime is `UNDEFINED`, stand aside unconditionally.
4. **Pillar 4: Resting L2/L3 Whale Backing & Liquidation Safety**:
   - Inviolable Stop Bunker: Stop Loss MUST sit safely behind a resting whale wall (`>= $100K USD`, persistence `>= 180s`) AND outside the nearest liquidation sweep band `[min_price, max_price] + 0.50 ATR`.
   - Never stage limit orders inside an un-swept retail stop cluster (`15_Hyperdash_Stops_Map`).
5. **Pillar 5: Macro & Calendar Blackout Gate**:
   - Proximity Check: No new trade staging within `+-15 minutes` of high-impact crypto events or `+-35 minutes` of TradFi Tier-1 releases (CPI, PPI, FOMC, NFP, GDP, Central Bank rate decisions).
   - Institutional ETF Flows: Consecutive net inflow days support long pullbacks; heavy net outflows invalidate long dip-buying on BTC/ETH.

---

### 5. REQUIRED COUNCIL OUTPUT DELIVERABLES
Respond with a rigorous, professional quantitative investment committee memorandum containing:

```
#### SECTION A: ACCOUNT & FLOOR DEFENSE AUDIT
- Current Equity, Live Floor Cushion (+X.XX USD above 4,775 USD), and Stressed Capacity.
- Progress towards Phase 1 Target (5,500.00 USD deadline Oct 23, 2026).

#### SECTION B: ACTIVE POSITION & RATCHET VERDICT
- Evaluation of Ticket #19146275 (NAS100.p).
- Ratchet instruction: MAINTAIN, ADVANCE RATCHET TO PHASE 0, or EXIT ON TIME DECAY.

#### SECTION C: INSTITUTIONAL CANDIDATE CENSUS
- Full tabular evaluation of qualified assets (Spread <= 25 bps for Crypto, <= 5 bps for TradFi).
- Table columns: Asset | Spread (bps) | Regime | VWAP Z | RSI | CVD Divergence | Whale Wall ($ / Persist) | Recommendation.

#### SECTION D: DEEP CONFLUENCE AUDIT OF CANDIDATES
- For any candidate meeting criteria: detailed analysis of whale wall location, liquidation bands, stop clusters, and risk/reward.
- If no setup meets all 5 pillars: explicit mathematical justification for STAND ASIDE.

#### SECTION E: FORMAL EXECUTION STAGING
- If trade ratified: exact Ticket Parameters (Symbol, Side, Volume lots, Limit Price, Stop Loss, Take Profit, Cash Risk USD, Reward USD, RR Ratio).
- If standing aside: formal Stand Aside declaration preserving capital cushion.
```
```
