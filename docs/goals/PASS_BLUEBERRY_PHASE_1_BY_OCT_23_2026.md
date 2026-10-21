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
| **Current Balance** | 4,824.89 USD | Realized balance |
| **Current Equity** | **~4,835.19 USD** | Live floating equity |
| **Equity Needed to Pass** | **+664.81 USD** | Required gains to reach 5,500.00 USD target |
| **Absolute Hard Floor** | **4,775.00 USD** | Inviolate liquidation boundary (Never breached) |
| **Operating Defense Buffer** | **4,795.00 USD** | Hard floor + 20.00 USD operating buffer |
| **Current Hard Floor Cushion** | **+60.19 USD** | Equity distance above 4,775.00 USD floor |
| **Current Buffer Cushion** | **+40.19 USD** | Equity distance above 4,795.00 USD buffer |
| **Target Deadline** | **23rd October 2026, 23:59 UTC** | End of trading week (Friday) |

---

## 2. Risk Management & Capital Allocation Rules

1. **Nominal Cash Risk Envelope**:
   - Standard Trade: **15.00 to 25.00 USD** per trade (0.31% to 0.52% of equity).
   - Stressed Post-Loss Floor Invariant:
     $$\text{Stressed Equity} = \text{Current Equity} - \sum (\text{Risk}_i \times 1.25 + 2.00) \ge 4,795.00\text{ USD}$$
2. **Position Capacity**:
   - Exactly **1 position** at up to 25.00 USD risk, OR
   - Up to **2 concurrent positions** at 15.00 USD risk each across the 18 perpetuals and TradFi assets.
   - When an open position achieves Early-BE (+0.75R0) and is locked risk-free, secondary capacity is immediately unlocked.
3. **Execution Mode**:
   - Strictly passive limit orders (`BUY_LIMIT` / `SELL_LIMIT`) with `ORDER_FILLING_IOC` / `ORDER_FILLING_RETURN`.
   - Never cross the bid-ask spread with aggressive market orders.

---

## 3. Dynamic Profit Ratchet Protocol (Frozen R0)

All open trades are governed by the non-negotiable piecewise ratchet:
- **Phase Early-BE (Adaptive Microstructure Breakeven)**: At `+0.75R0` to `+0.80R0` gain, move Stop Loss to `Entry + 0.10R0` (+15 pts on NAS100). Trade becomes 100% risk-free.
- **Phase 0 (Risk Cut)**: At `+1.25R0` gain, move Stop Loss to `Entry + 0.15R0`.
- **Phase 1 (Profit Lock)**: At `+1.65R0` gain, move Stop Loss to `Entry + 0.80R0`.
- **Take Profit (TP)**: Front-run opposing high-density liquidation magnet or Daily VWAP by 3.8 to 10 bps (e.g. +2.0R0 to +2.5R0).
- **Time Decay Gate**: Exit at market if profit remains `< +0.20R0` after 24 bars (6 hours).

---

## 4. Current Active Trade State

- **Symbol**: `NAS100.p` (Ticket #19146275)
- **Position Type**: BUY 0.01 lot
- **Entry Price**: 29,560.00 USD
- **Current Stop Loss**: **29,575.00 USD** (+15.0 pts above entry)
- **Risk Status**: **100% RISK-FREE** (Guaranteed minimum profit: +1.50 USD)
- **Take Profit**: **29,715.00 USD** (+155.0 pts / +15.50 USD target)
- **Floating Profit**: **+10.30 USD**

---

## 5. Daily Compounding Pathway to 5,500.00 USD

To bridge the +664.81 USD requirement by Friday, 23rd October 2026:
- Target daily profit: ~135 to 160 USD net over the remaining trading sessions.
- Compound risk-free ratchet wins while aggressively locking profits at +1.5R to +2.5R.
- Maximize high-probability setups across high-velocity instruments: `NAS100.p` (0.36 bps spread), `DJ30.p` (0.22 bps spread), `SP500.p` (0.39 bps spread), and `BTCUSD.pi` (1.80 bps spread).
- Full autonomous execution enabled: Antigravity punches qualifying limit orders immediately without waiting for user confirmation.
