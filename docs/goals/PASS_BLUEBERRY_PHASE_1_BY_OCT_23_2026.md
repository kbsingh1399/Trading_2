# 🎯 ACTIVE GOAL: PASS BLUEBERRY MARKETS PHASE 1 EVALUATION
## Canonical Operational Mission Specification

> **Target Environment**: MetaTrader 5 (Blueberry Markets Account #5064568)  
> **Mission Objective**: Pass Phase 1 Funded Challenge by End of Friday, 23rd October 2026  
> **Status**: **ACTIVE & AUTONOMOUSLY EXECUTING**  
> **Canonical SOP**: `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`  
> **Execution Checklist**: `docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md`  
> **Master Data Warehouse**: `Data/DataBase_Trading.xlsx` & `Data/Manditory/`

---

## 1. Quantitative Target Parameters

| Metric / Parameter | Value / Threshold | Notes / Governance |
|---|---|---|
| **Account Login** | **#5064568** | Blueberry Markets MT5 Live Server |
| **Initial Starting Balance** | 5,000.00 USD | Baseline evaluation capital |
| **Profit Target (Phase 1)** | **5,500.00 USD** (+500.00 USD / +10.0%) | Mandatory target to pass Phase 1 |
| **Current Balance** | **4,851.83 USD** | Realized balance (Session High-Water Mark) |
| **Current Equity** | **4,851.83 USD** | 100% Unencumbered liquid cash |
| **Equity Needed to Pass** | **+648.17 USD** | Required gains to reach 5,500.00 USD target |
| **Absolute Hard Floor** | **4,775.00 USD** | Inviolate liquidation boundary (Never breached) |
| **Operating Defense Buffer** | **4,795.00 USD** | Hard floor + 20.00 USD operating buffer |
| **Current Hard Floor Cushion** | **+76.83 USD** | Equity distance above 4,775.00 USD floor (+1.61%) |
| **Current Buffer Cushion** | **+56.83 USD** | Equity distance above 4,795.00 USD buffer (+1.18%) |
| **Target Deadline** | **23rd October 2026, 23:59 UTC** | End of trading week (Friday) (~51.8h remaining) |

---

## 2. Risk Management & Capital Allocation Rules

1. **Nominal Cash Risk Envelope**:
   - Standard Trade: **15.00 to 25.00 USD** per trade (0.31% to 0.52% of equity).
   - Stressed Post-Loss Floor Invariant:
     $$\text{Stressed Equity} = \text{Current Equity} - \sum (\text{Risk}_i \times 1.25 + 2.00) \ge 4,795.00\text{ USD}$$
2. **Position Capacity & Stressed Staging Rules**:
   - Up to **2 concurrent positions** at ~18.00–20.00 USD nominal risk each.
   - Dual-stopout stressed loss = $47.63 USD -> Stressed Equity = **4,804.20 USD** (+9.20 USD above buffer, +29.20 USD above hard floor).
   - When an open position achieves Early-BE (+0.75R0) and SL is moved to Entry + 0.10R0, risk drops to $0.00 and capital headroom is freed.
3. **Execution Mode**:
   - Strictly passive limit orders (`BUY_LIMIT` / `SELL_LIMIT`) with `ORDER_FILLING_IOC` / `ORDER_FILLING_RETURN`.
   - Never cross the bid-ask spread with aggressive market orders.

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
