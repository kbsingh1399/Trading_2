# 🎯 ACTIVE GOAL: PASS BLUEBERRY MARKETS PHASE 1 EVALUATION
## Canonical Operational Mission Specification

> **Target Environment**: MetaTrader 5 (Blueberry Markets Account #5064568)  
> **Mission Objective**: Pass Phase 1 Funded Challenge by End of Friday, 23rd October 2026  
> **Status**: **ACTIVE & AUTONOMOUSLY EXECUTING**  
> **Canonical SOP**: Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md (Including Section 1.7 156-Asset Universe)  
> **Execution Checklist**: Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md  
> **Master Data Warehouse**: Data/DataBase_Trading.xlsx (33 Sheets) & Data/Manditory/

---

## 1. Quantitative Target Parameters

| Metric / Parameter | Value / Threshold | Notes / Governance |
|---|---|---|
| **Account Login** | **#5064568** | Blueberry Markets MT5 Live Server |
| **Initial Starting Balance** | 5,000.00 USD | Baseline evaluation capital |
| **Profit Target (Phase 1)** | **5,500.00 USD** (+500.00 USD / +10.0%) | Mandatory target to pass Phase 1 |
| **Current Balance** | **4,818.51 USD** | Realized balance on MT5 |
| **Current Equity** | **4,818.51 USD** | 100% Unencumbered liquid cash |
| **Equity Needed to Pass** | **+681.49 USD** | Required gains to reach 5,500.00 USD target |
| **Absolute Hard Floor** | **4,775.00 USD** | Inviolate liquidation boundary (Never breached) |
| **Operating Defense Buffer** | **4,795.00 USD** | Hard floor + 20.00 USD operating buffer |
| **Current Hard Floor Cushion** | **+43.51 USD** | Equity distance above 4,775.00 USD floor (+1.25%) |
| **Current Buffer Cushion** | **+23.51 USD** | Equity distance above 4,795.00 USD buffer (+0.83%) |
| **Target Deadline** | **23rd October 2026, 23:59 UTC** | End of trading week (Friday) (~20.05h remaining) |

---

## 2. Risk Management & Capital Allocation Rules (Operator Authorized Scale)

1. **Nominal Cash Risk Envelope (Operator Directive: Increase Risk for Confluence)**:
   - Standard Setup: **15.00 to 20.00 USD** per trade (Stressed loss: 20.75 to 27.00 USD).
   - Pristine Confluence Rights: Up to **25.00 to 35.00 USD** per trade for pristine 5-pillar setups.
   - Stressed Post-Loss Floor Invariant:
     Stressed Equity = Current Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD
   - Under current +23.51 USD buffer cushion, taking a 18.00 USD risk trade incurs 24.50 USD stressed loss, strictly preserving **+15.33 USD surplus** above the operating buffer and **+35.33 USD** above the hard floor.
2. **Position Capacity & Stressed Staging Rules**:
   - Authorized up to **4 concurrent running filled positions** across orthogonal asset clusters (Crypto, Indices, Metals, Forex).
   - Resting pending limit orders do **NOT** consume running slots! Up to 5 resting limits may be pre-staged at structural whale shelves.
   - Ratchet Headroom Release: When a live position hits Early-BE (+0.75R0) and SL moves to Entry + 0.10R0, risk drops to 0.00 USD, immediately releasing buffer capacity for secondary setups.
3. **Continuous Tri-Track Council (Antigravity Fable 5, Arena.ai GPT Astra & Z.ai GLM-5.3-Flash)**:
   - On every autonomous cycle, inject the canonical unified prompt `Arena_GLM_Standard_Prompt.md` simultaneously into Arena.ai (GPT Astra) and Z.ai (GLM-5.3-Flash) via Chrome CDP port 9222.
   - Completion daemons auto-harvest critiques and candidates into `docs/trade_plans/ARENA_LATEST_RAW.md` and `docs/trade_plans/ZAI_LATEST_RAW.md`.
   - Joint-Completion Lifecycle: Cycle X is complete ONLY when all 3 entities finish. Next cycle triggers strictly 20 minutes after completion (`T_finish + 20 min`), supervised by the 30-minute watchdog sentry (`0,30 * * * *`).
   - Conduct co-equal debate: Punch limit orders ONLY when all tracks confirm 5-pillar confluence with valid resting whale walls and positive solvency cushion.
4. **Execution Mode**:
   - Strictly passive limit orders (BUY_LIMIT / SELL_LIMIT) with broker-supported filling modes.
   - Non-marketable posture: BUY_LIMIT <= live bid, SELL_LIMIT >= live ask (Never cross the spread).

---

## 3. Dynamic Profit Ratchet Protocol (Frozen R0)

All open trades are governed by the non-negotiable piecewise ratchet:
- **Phase Early-BE (Adaptive Microstructure Breakeven)**: At +0.75R0 to +0.80R0 gain, move Stop Loss to Entry + 0.10R0. Trade becomes 100% risk-free.
- **Phase 0 (Risk Cut)**: At +1.25R0 gain, move Stop Loss to Entry + 0.15R0.
- **Phase 1 (Profit Lock)**: At +1.65R0 gain, move Stop Loss to Entry + 0.80R0.
- **Take Profit (TP)**: Front-run opposing high-density liquidation magnet or Daily VWAP by 5 to 10 bps (e.g. +2.0R0 to +2.8R0).
- **Time Decay Gate**: Exit at market if profit remains < +0.20R0 after 24 bars (6 hours).

---

## 4. Current Active Trade State & Candidate Radar (Cycle 256)

- **Account Status**: **100% FLAT CASH** | Realized Balance: 4,818.51 USD
- **Open Positions**: 0
- **Pending Orders**: 0
- **Candidate Trigger Radar Across 156-Asset Universe**:
  * **BTCUSD.pi Whale Shelf Sweep**: Buy Limit @ 81,040.00 | SL 80,590.00 | TP 81,950.00 | 0.04 lot (Risk: .00) | Trigger: Retail stop cascade at [81,050–81,150] swept, 15m CVD flips positive.
  * **XAUUSD.pi Bunker Reversal**: Buy Limit @ 4,048.00 | SL 4,040.50 | TP 4,068.50 | 0.02 lot (Risk: .00) | Trigger: Price tests 4,046.50 bunker, selling delta decelerates > 30%.
  * **SOLUSD.p Shelf Pullback**: Buy Limit @ 103.80 | SL 102.75 | TP 105.80 | 0.15 lot (Risk: .75) | Trigger: Flush into 103.75 shelf, absorption confirmed.
  * **NAS100.p Value Area Shelf**: Buy Limit @ 29,245.00 | SL 29,150.00 | TP 29,480.00 | 0.02 lot (Risk: .00) | Trigger: Reclaim of 29,228 VAL with positive volume delta.

---

## 5. Daily Compounding Pathway to 5,500.00 USD

To bridge the +681.49 USD requirement by Friday, 23rd October 2026:
- Target profit velocity: ~200 to 220 USD net across the remaining sessions (~33.0 hours runway).
- Compound risk-free ratchet wins while aggressively locking profits at +1.5R to +2.5R.
- Deploy across orthogonal clusters: Crypto (BTC, ETH, SOL), Indices (NAS100, DJ30, SP500, UK100), Metals (Gold, Silver), Forex (EURUSD, GBPUSD, USDJPY).
- Full autonomous execution enabled: Antigravity punches qualifying limit orders immediately without waiting for user confirmation.
