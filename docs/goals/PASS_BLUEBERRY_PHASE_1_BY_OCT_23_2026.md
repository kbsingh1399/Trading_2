# 🎯 ACTIVE GOAL: PASS BLUEBERRY MARKETS PHASE 1 EVALUATION
## Canonical Operational Mission Specification

> **Target Environment**: MetaTrader 5 (Blueberry Markets Account #5064568)  
> **Mission Objective**: Pass Phase 1 Funded Challenge by End of Friday, 23rd October 2026  
> **Status**: **ACTIVE & AUTONOMOUSLY EXECUTING**  
> **Canonical SOP**: docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md (Including Section 1.7 156-Asset Universe)  
> **Execution Checklist**: docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md  
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
| **Current Hard Floor Cushion** | **+43.51 USD** | Equity distance above 4,775.00 USD floor (+0.91%) |
| **Current Buffer Cushion** | **+23.51 USD** | Equity distance above 4,795.00 USD buffer (+0.49%) |
| **Target Deadline** | **23rd October 2026, 23:59 UTC** | End of trading week (Friday) (~21.65h remaining) |

---

## 2. Risk Management & Capital Allocation Rules (Operator Authorized Scale)

1. **Nominal Cash Risk Envelope (Operator Directive: Increase Risk for Confluence)**:
   - Standard Setup: **12.00 to 17.20 USD** per trade under current +23.51 USD buffer cushion.
   - Stressed Post-Loss Floor Invariant:
     Stressed Equity = Current Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD
   - Max allowable initial risk: `(23.51 - 2.00) / 1.25 = 17.20 USD`.
   - Pristine Confluence Rights: Up to **25.00 to 35.00 USD** unlocked via House Money once Trade #1 wins (+49.00 USD) and expands cushion to +72.89 USD.
2. **Position Capacity & Stressed Staging Rules**:
   - Single-Slot Risk Law: Exactly 1 active risk-bearing order allowed until Slot 1 reaches +0.75R0 Early-BE.
   - Fluid 4-Slot Dynamic Capacity: Once derisked, up to 4 concurrent running filled positions across orthogonal asset clusters (Crypto, Indices, Metals, Forex).
   - Resting pending limit orders do **NOT** consume running slots! Up to 5 resting limits may be pre-staged at structural shelves.
3. **Continuous Co-Equal Council with Arena.ai, Z.ai & Gemini Web2API**:
   - On every 20-minute cycle and prospective setup approach, inject surgical prompts into Arena.ai and Z.ai via Chrome CDP (port 9222) and Gemini Web2API (port 8081).
   - Automated completion daemons monitor responses and trigger reactive wakeups.
   - Cross-verify candidate setups against the canonical 10-Point Pre-Punch Checklist before order submission.
4. **Execution Mode**:
   - Strictly passive limit orders (BUY_LIMIT / SELL_LIMIT) with broker-supported filling modes.
   - Non-marketable posture: BUY_LIMIT <= live bid, SELL_LIMIT >= live ask (Never cross the spread).

---

## 3. Dynamic Profit Ratchet Protocol (Frozen R0)

All open trades are governed by the non-negotiable piecewise ratchet:
- **Phase Early-BE (Adaptive Microstructure Breakeven)**: At +0.75R0 to +0.80R0 gain, move Stop Loss to Entry + 0.10R0. Trade becomes 100% risk-free.
- **Phase 0 (Risk Cut)**: At +1.25R0 gain, move Stop Loss to Entry + 0.15R0.
- **Phase 1 (Profit Lock)**: At +1.65R0 gain, move Stop Loss to Entry + 0.80R0.
- **Take Profit (TP)**: Front-run opposing high-density liquidation magnet or Daily VWAP by 5 to 10 bps (e.g. +2.0R0 to +3.9R0).
- **Time Decay Gate**: Exit at market if profit remains < +0.20R0 after 24 bars (6 hours).

---

## 4. Current Active Trade State & Candidate Radar (Cycle 287)

- **Account Status**: **100% FLAT CASH** | Realized Balance: 4,818.51 USD
- **Open Positions**: 0/4
- **Pending Orders**: 0/10
- **Candidate Trigger Radar Across 156-Asset Universe**:
  * **BTCUSD.pi Supply Wall Retest Short**: Sell Limit @ 81,580.00 | SL 81,860.00 | TP 80,480.00 | 0.04 lot | Risk: -$11.20 nominal, -$16.75 stressed | 3.93R | Trigger: Price recovers into 81,550–81,580 ask wall with tape exhaustion during London pre-market.
  * **XAUUSD.pi Post-Sweep DVAL Resistance**: Live Price ~4,015.00 | Stand aside until structural consolidation confirms rejection vs reclamation above 4,017.00.
  * **UKBRENT.p London Shelf Pullback**: Standby for London Open @ 114.15 DVAL.
  * **NZDUSD.pi**: RETIRED / DISQUALIFIED after false breakout swept down to 0.56868.

---

## 5. Daily Compounding Pathway to 5,500.00 USD

To bridge the +681.49 USD requirement by Friday, 23rd October 2026:
- Compounding staircase:
  1. Seed Trade #1: 11.20–15.00 USD nominal risk (e.g. BTC short at 81,580, +3.93R = +$44.00), lifting equity to 4,862.51 USD and cushion to +67.51 USD.
  2. Phase 2 Scaled Risk: Sizing two concurrent positions at 25.00 USD nominal risk produces +125.00 USD per winner, closing the gap in 4-5 high-conviction trades across London and New York sessions.
  3. Deploy across orthogonal clusters: Crypto (BTC, ETH), Indices (NAS100, SP500), Metals (Gold), Forex (EURUSD, USDJPY).
- Full autonomous execution enabled: Antigravity punches qualifying limit orders immediately without waiting for user confirmation.
