# 🏛️ MASTER QUANTITATIVE COMMISSION & ARCHITECTURAL REVIEW DIRECTIVE
## Targeted to: GPT SOL 6.1 (Chief Quantitative Architect & Hedge Fund Risk Auditor)
### Desk: Blueberry Markets MT5 Autonomous Quant Desk (Account #5064568)
### Canonical Repository: https://github.com/kbsingh1399/Trading_2 (Branch `main`)

---

## 🎯 SECTION 1: MISSION CONTEXT & INVIOLABLE RISK BOUNDARIES

You are commissioned as the **Chief Quantitative Architect and Lead Quantitative Systems Auditor** for an institutional-grade, fully autonomous algorithmic trading desk running on MetaTrader 5 (Blueberry Markets, Account #5064568).

### 1.1 The Operational Objective
- **Target Goal**: Elevate account equity from current state to **5,500.00 USD** (+10.0% evaluation target) before the evaluation cutoff on **Friday, 23rd October 2026 (23:59 UTC)**.
- **Evaluation Rule**: Phase 1 Prop Firm Challenge (Blueberry Markets SVG-Live).

### 1.2 The Inviolable Triple Floor Governance (Zero-Tolerance Boundaries)
Under NO circumstances may any model proposal, trade staging, risk sizing, or rule alteration compromise or breach these three hard floors:
1. **Hard Capital Floor**: **4,600.00 USD** (Absolute broker liquidation breach level; inviolable).
2. **Operating Buffer Floor**: **4,650.00 USD** (Pre-emptive capital preservation circuit breaker).
3. **Canonical Solvency Kernel**: **4,795.00 USD** (Strict admission floor for new risk staging).

### 1.3 Ground-Truth Account State (Current Live Baseline)
- **Account Balance**: **4,799.88 USD**
- **Floating Equity**: **~4,838.85 USD** (Net floating profit: **+38.97 USD**)
- **Margin Used / Free Margin**: 2,451.00 USD / 2,387.85 USD (Margin Level: 197.42%)
- **Hard Floor Cushion**: **+238.85 USD**
- **Operating Buffer Cushion**: **+188.85 USD**
- **Solvency Kernel Cushion**: **+43.85 USD**
- **Net Realized Headroom**: **+2.88 USD** (Realized Balance 4,799.88 USD - Contingency Reserve 2.00 USD - Solvency Kernel 4,795.00 USD).
  * *Critical Governance Invariant*: Staging any new risk ticket requires minimum realized headroom of **11.38 USD** (the stressed loss of 1 minimum lot 0.01 at a standard stop). With +2.88 USD realized headroom, **NEW RISK ADMISSION IS HARD-LOCKED TO FALSE** until open profits are realized!
- **Active Position (Ticket #19267445)**:
  * Symbol: `BTCUSD.pi` | Side: `SELL` (Short) | Volume: `0.06 lot`
  * Entry: `81,700.00 USD` | Current Mark: `~81,037.00 USD` (Excursion: +663 points = +1.6575 R0)
  * Stop Loss: **`81,300.00 USD`** (Stage 2 Profit Lock locked in broker terminal; guaranteed banked payout upon stopout: **+$24.00 USD** gross / **+$23.19 USD** net). Downside capital risk is strictly **0.00 USD**.
  * Take Profit Target: **`80,600.00 USD`** (+2.75 R0 / **+$66.00 USD** gross profit realization).
  * Target Geometry: Sits at 80,600 USD to safely front-run massive on-chain whale bids resting at **80,483.00 USD** (66.79 BTC / $5.38M notional) and **80,427.00 USD** (32.06 BTC / $2.58M notional) by +117 USD, capturing the liquidation cascade before absorption stall.
  * Realized Balance Upon TP Realization: **4,865.88 USD** -> elevating realized headroom to **+68.88 USD**, unlocking Tier 2 House Money capacity for multi-asset expansion!

---

## 🏛️ SECTION 2: SYSTEM ARCHITECTURE & GOVERNANCE WAREHOUSE

The desk operates under strict institutional hedge fund governance where all rules, state machines, and checklists are centralized in the repository under `Data/Manditory/` (Canonical Single Source of Truth).

### 2.1 The Repository Map
Inspect the canonical GitHub repository:
`https://github.com/kbsingh1399/Trading_2` (Branch `main`)

Core Governance Files:
1. `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md`: Master 10-step institutional quantitative decision architecture.
2. `Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md`: 13-step autonomous execution and wake-up checklist.
3. `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md`: Unified 4-quant subagent prompt architecture (Role A: Regime, Role B: Microstructure, Role C: Solvency, Role D: Clock/Provenance).
4. `Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`: Protocol for seamless model and account switching with zero context amnesia.
5. `Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md`: PDCA-Ω continuous self-improvement framework and perpetual quant inquest.
6. `Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`: Forensic autopsy of the 10 lethal execution traps.
7. `Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`: 32 pre-trade verification questions.
8. `Data/Manditory/Arena_GLM_Standard_Prompt.md`: Standard dispatch prompt for external co-equal councils (Arena.ai GPT Astra & Z.ai GLM-5.3-Flash).

### 2.2 Data Warehouse Architecture
`Data/DataBase_Trading.xlsx`: 33-sheet real-time continuous data warehouse updated every 300 seconds by a persistent background daemon, tracking 156 assets across 6 asset classes (Crypto Majors/Alts, Global Indices, Precious/Industrial Metals, Energy, Forex Majors/Crosses).

### 2.3 The Co-Equal Tri-Council Consensus Engine
Every cycle (cycling every 20 minutes) executes a tri-track institutional deliberation:
1. **Track 1: Antigravity 4-Quant Swarm (Fable 5)**: Role A (Regime), Role B (Microstructure), Role C (Solvency), Role D (Market Clock/Provenance).
2. **Track 2: Arena.ai Council (GPT Astra)**: Independent frontier model review via Chrome CDP 9222.
3. **Track 3: Z.ai Sovereign Council (GLM-5.3-Flash)**: Independent frontier model review via Chrome CDP 9222.
Consensus Rule: Co-equal agreement required. Any Severity-1 or Severity-2 dispute results in `AUTHORIZATION = DENIED_DISPUTED`.

---

## 🔬 SECTION 3: THE MANDATE FOR GPT SOL 6.1 (PROBLEMS TO SOLVE)

As Chief Quantitative Architect, you are instructed to conduct an exhaustive, rigorous, line-by-line review of all files in `Data/Manditory/` and propose concrete, production-ready improvements and file updates. Specifically, resolve these four systemic quantitative challenges:

### Problem 1: Resolving Candidate Discovery Paralysis (Section 2.5 Inquest)
- **The Symptom**: Across 156 assets, 3.47M historical candles, and extensive real-time orderbook/CVD/liquidation data, the scanner frequently produces 0 candidate setups. Equity has hovered near 4,800 USD rather than aggressively compounding toward 5,500 USD.
- **The Diagnosis**: The 5-pillar confluence stack has historically suffered from "Conjunctive Sclerosis" — treating multiple indicators as binary, unweighted fail-closed vetoes rather than probabilistic evidence. Furthermore, secondary indicators (e.g. slight ATR distance deviations) were vetoing setups with strong positive expected value.
- **Your Mandate**:
  1. Audit Section 2 of `STANDARDIZED_TRADING_DECISION_CHAIN.md`.
  2. Refine the **Two-Tier Decision Architecture**:
     * **Tier 1 (Hard Binary Gates)**: Reserve binary fail-closed vetoes strictly for Solvency (Kernel >= 4,795 USD), Broker Session (Tradable), Event Blackout, and Data Freshness.
     * **Tier 2 (Soft Calibrated Ranking)**: For all hard-gate survivors, calculate true probabilistic Expected Value:
       `EV_net = P_fill * [P_TP * Gain_net - (1 - P_TP) * Loss_net - AS - Friction] - (1 - P_fill) * C_wait`
       Rank candidates by Utility = LCB_5%(EV_net) / Expected_Capital_Minutes.
  3. Define explicit statistical calibration standards so that probabilities are grounded in empirical walk-forward hit rates (e.g. Wilson score lower confidence bounds) rather than subjective confidence scores.

### Problem 2: Asset-Class Specific Microstructure Architecture
- **The Issue**: Early iterations suffered from template bias — attempting to apply crypto perpetual mechanics (Hyperliquid whale walls, CoinGlass liquidation heatmaps) to Forex Majors, Metals, and Equity Indices.
- **Your Mandate**:
  1. Clearly partition the decision chain in `STANDARDIZED_TRADING_DECISION_CHAIN.md` into 3 distinct asset-native execution regimes:
     * **Crypto Perpetuals (BTC, ETH, SOL, etc.)**: Orderbook depth imbalance, taker CVD z-score divergence, resting whale walls (persist >= 180s), Hyperdash stop cascades.
     * **Foreign Exchange & Precious Metals (EURUSD, GBPUSD, XAUUSD)**: Auction Market Structure (Sheet 33: Daily/Weekly Value Area High/Low, Point of Control), session liquidity sweeps (London/NY open sweeps), interbank rollover lockout (21:15-22:30 UTC).
     * **Global Equity Indices (SP500, NAS100, GER40)**: Regular cash session hours (14:30-21:00 UTC for US, 08:00-16:30 UTC for EU), Volume Profile POCs, Fair Value Gaps, opening range breakouts. Quarantining after-hours synthetic CFD quotes into WATCHLIST_ONLY.

### Problem 3: Broker-Native Quote-Conversion & Structural Lot Sizing
- **The Issue**: Generic contract math (e.g. `risk_usd / (pts * 100)`) frequently miscalculates pip values, index point values, and margin requirements on CFD brokers, leading to order rejection or margin over-allocation.
- **Your Mandate**:
  1. Strengthen Step 8 of `STANDARDIZED_TRADING_DECISION_CHAIN.md` to mandate broker-native calculation via MT5 primitives:
     `order_calc_profit(type, symbol, lot, entry, sl)`
     `order_calc_margin(type, symbol, lot, entry)`
     `order_check(request)`
  2. Specify the exact mathematical algorithm for lot snapping (`lot*`) that searches the legal broker volume grid `[volume_min, volume_max, volume_step]`, maximizing position size while guaranteeing that worst-case loss never breaches the 4,795.00 USD Solvency Kernel under ANY fill scenario.

### Problem 4: Model & Account Switching Resilience (`ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`)
- **The Issue**: When the human operator switches Gemini/LLM chat accounts, the incoming agent must be able to boot immediately without context amnesia, without closing running daemons, and without second-guessing established profit locks.
- **Your Mandate**:
  1. Audit `ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`.
  2. Ensure the 12-step bootstrap protocol provides immediate mathematical grounding: verifying all 5 background daemons, reading `cycle_envelope.json`, confirming Ticket #19267445 Stage 2 Profit Lock, and computing realized headroom (+2.88 USD) in step 1.

---

## 📝 SECTION 4: REQUIRED DELIVERABLES & FORMATTING STANDARDS

Please provide your complete, professional architectural response structured as follows:

1. **Executive Evaluation**: High-level quantitative critique of the desk's governance and decision chain.
2. **Concrete File Modifications & Upgrades**:
   - Provide exact, drop-in replacement sections or full-file markdown specifications for:
     * `Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md` (specifically Section 2, Step 2, Step 8).
     * `Data/Manditory/SUBAGENT_PROMPT_TEMPLATES.md` (verify the new 4 full prompt blocks and mathematical estimators).
     * `Data/Manditory/ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md` (audit for zero-friction account switching).
     * `Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md` (audit Part 5 & 6).
3. **Mathematical Formulation & Verification Code**:
   - Provide clean Python pseudo-code or production snippets for:
     * Lo-MacKinlay Variance Ratio `VR(q=4)` with heteroskedasticity correction.
     * Newey-West HAC Drift t-statistic.
     * Continuous Barrier Hitting Probability under GBM.
     * Broker-native structural lot snapping algorithm.
4. **Formatting Invariant**: Strictly plain text and unicode math formatting (NO raw LaTeX delimiters `$` or `$$` in explanations).
