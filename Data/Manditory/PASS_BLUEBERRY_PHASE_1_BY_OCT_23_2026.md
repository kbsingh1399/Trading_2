# 🎯 ACTIVE GOAL: PASS BLUEBERRY MARKETS PHASE 1 EVALUATION
## Canonical Operational Mission Specification

> **Target Environment**: MetaTrader 5 (Blueberry Markets Account #5064568)  
> **Mission Objective**: Pass Phase 1 Funded Challenge by End of Friday, 23rd October 2026  
> **Status**: **ACTIVE & AUTONOMOUSLY EXECUTING**  
> **Canonical SOP**: `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`  
> **Execution Checklist**: `Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md`  
> **Master Data Warehouse**: `Data/DataBase_Trading.xlsx` (33 Sheets) & `Data/Manditory/`

---

## 1. Quantitative Target Parameters

| Metric / Parameter | Value / Threshold | Notes / Governance |
|---|---|---|
| **Account Login** | **#5064568** | Blueberry Markets MT5 Live Server |
| **Initial Starting Balance** | 5,000.00 USD | Baseline evaluation capital |
| **Profit Target (Phase 1)** | **5,500.00 USD** (+500.00 USD / +10.0%) | Mandatory target to pass Phase 1 |
| **Current Balance** | **4,834.83 USD** | Realized balance on MT5 |
| **Current Equity** | **4,834.83 USD** | 100% Unencumbered liquid cash |
| **Equity Needed to Pass** | **+665.17 USD** | Required gains to reach 5,500.00 USD target |
| **Absolute Hard Floor** | **4,775.00 USD** | Inviolate liquidation boundary (Never breached) |
| **Operating Defense Buffer** | **4,795.00 USD** | Hard floor + 20.00 USD operating buffer |
| **Current Hard Floor Cushion** | **+59.83 USD** | Equity distance above 4,775.00 USD floor (+1.25%) |
| **Current Buffer Cushion** | **+39.83 USD** | Equity distance above 4,795.00 USD buffer (+0.83%) |
| **Target Deadline** | **23rd October 2026, 23:59 UTC** | End of trading week (Friday) (~41.5h remaining) |

---

## 2. Risk Management & Capital Allocation Rules (Operator Authorized Scale)

1. **Nominal Cash Risk Envelope (Operator Directive: Increase Risk for Confluence)**:
   - Solo High-Conviction Setup: **15.00 to 20.00 USD** per trade (Stressed loss: $20.75 to $27.00 USD).
   - Stressed Post-Loss Floor Invariant:
     Stressed Equity = Current Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD
   - Under current +39.83 USD buffer cushion, taking a $18.00 risk trade incurs $24.50 stressed loss, strictly preserving **+15.33 USD surplus** above the operating buffer and **+35.33 USD** above the hard floor.
2. **Position Capacity & Stressed Staging Rules**:
   - Current Cushion (+39.83 USD): **1 Solo Position Maximum** at $15.00–$20.00 risk.
   - Dynamic Unlocking: Dual concurrent positions ($15.00 each) are unlocked as soon as live equity reaches **4,836.50 USD**.
   - Ratchet Headroom Release: When a live position hits Early-BE (+0.75R0) and SL moves to Entry + 0.10R0, risk drops to $0.00, immediately releasing buffer capacity for secondary setups.
3. **Continuous Co-Equal Council with Arena.ai**:
   - On every 20-minute cycle and prospective setup approach, inject the surgical red-team prompt into Arena.ai via Chrome CDP on port 9222.
   - Arena completion daemon auto-harvests critiques to `docs/trade_plans/ARENA_LATEST_RAW.md`.
   - Conduct joint debate: Punch limit orders ONLY when both internal fleet and Arena confirm 5-pillar confluence with valid resting whale walls.
4. **Execution Mode**:
   - Strictly passive limit orders (`BUY_LIMIT` / `SELL_LIMIT`) with broker-supported filling modes.
   - Non-marketable posture: `BUY_LIMIT <= live bid`, `SELL_LIMIT >= live ask` (Never cross the spread).

---

## 3. Dynamic Profit Ratchet Protocol (Frozen R0)

All open trades are governed by the non-negotiable piecewise ratchet:
- **Phase Early-BE (Adaptive Microstructure Breakeven)**: At `+0.75R0` to `+0.80R0` gain, move Stop Loss to `Entry + 0.10R0`. Trade becomes 100% risk-free.
- **Phase 0 (Risk Cut)**: At `+1.25R0` gain, move Stop Loss to `Entry + 0.15R0`.
- **Phase 1 (Profit Lock)**: At `+1.65R0` gain, move Stop Loss to `Entry + 0.80R0`.
- **Take Profit (TP)**: Front-run opposing high-density liquidation magnet or Daily VWAP by 3.8 to 10 bps (e.g. +2.0R0 to +2.5R0).
- **Time Decay Gate**: Exit at market if profit remains `< +0.20R0` after 24 bars (6 hours).

---

## 4. Current Active Trade State & Candidate Radar

- **Account Status**: **100% CASH** | Realized Profit Realized: EURUSD.pi Ticket #19164106 banked +$11.44 net profit at 1.12300.
- **Open Positions**: 0
- **Pending Orders**: 0
- **Candidate Trigger Radar**:
  * **BTCUSD.pi Pullback**: Buy Limit @ 83,550.00 | SL 83,280.00 | TP 84,225.00 | 0.07 lot (Risk: $18.90) | Trigger: Retail stop sweep concludes, CVD absorption.
  * **XAUUSD.pi Demand Shelf**: Buy Limit @ 4,108.00 | SL 4,092.00 | TP 4,148.00 | 0.01 lot (Risk: $16.00) | Trigger: Depth feed uncrosses, CVD deceleration.
  * **SOLUSD.p VWAP Shelf**: Buy Limit @ 104.80 | SL 103.20 | TP 108.80 | 0.15 lot (Risk: $18.00) | Trigger: Pullback to 1D VWAP, RSI < 42.
  * **EURUSD.pi Post-Rollover Long**: Buy Limit @ 1.12150 | SL 1.12050 | TP 1.12450 | 0.08 lot (Risk: $8.00) | Trigger: Post-22:30 UTC rollover normalization.

---

## 5. Daily Compounding Pathway to 5,500.00 USD

To bridge the +648.17 USD requirement by Friday, 23rd October 2026:
- Target daily profit: ~130 to 150 USD net over the remaining trading sessions (~51.8 hours runway).
- Compound risk-free ratchet wins while aggressively locking profits at +1.5R to +2.5R.
- Maximize high-probability setups across high-velocity instruments: `NAS100.p`, `DJ30.p`, `SP500.p`, `BTCUSD.pi`, and `XAUUSD.pi`.
- Full autonomous execution enabled: Antigravity punches qualifying limit orders immediately without waiting for user confirmation.
