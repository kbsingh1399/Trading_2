# 📊 LIVE PORTFOLIO & ORDER REGISTRY
**Authoritative Real-Time Position, Order & Solvency Registry**
*Maintained Continuously by Antigravity Autonomous Position Supervisor*

> **GOVERNANCE PURPOSE**:
> This registry serves as the single source of truth for all live running positions, resting pending maker limit orders, locked-in profit ratchets, and banked session profits.
> It is automatically updated by the dynamic position supervisor daemon and pushed to GitHub main every 60 seconds (`https://github.com/kbsingh1399/Trading_2.git`).
> 
> **RAW GITHUB FETCH URL FOR ARENA.AI & Z.AI**:
> `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`

---

## 🏛️ 1. ACCOUNT SOLVENCY & CAPITAL METRICS
- **Broker & Account**: Blueberry Markets MT5 Account #5064568 (`BlueberryMarketsSVG-Live`, Raw Spread)
- **Account Balance**: **4,742.31 USD**
- **Floating Equity**: **4,742.31 USD**
- **Free Margin**: **4,742.31 USD**
- **Margin Used**: **0.00 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor | Deficit: -32.69 USD)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor | Deficit: -52.69 USD)
- **Active Running Positions**: **0 ACTIVE (100% Flat Cash)**
- **Active Resting Pending Orders**: **7 LIVE PENDING MAKER LIMIT ORDERS**
- **Total Contingent Downside Risk**: **40.33 USD** (Max per-ticket risk capped at <= 10.00 USD)
- **Execution Posture**: **ARMED_MAKER_LIMITS_ACTIVE**
- **Last Synchronized (UTC)**: `2026-10-29 19:40:00 UTC` (`2026-10-30 01:10:00 IST`)

---

## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — 100% FLAT CASH)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| - | NONE | - | - | - | - | - | - | 0.00 USD | Flat | **Book is 100% Cash Defense. Zero open risk.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (7 LIVE BROKER TICKETS EXECUTED)

| Priority | Ticket | Symbol | Order Type | Volume | Limit Entry | Spread-Padded SL | Take Profit | Risk USD | Live Status & Forensic Armor |
|---|---|---|---|---|---|---|---|---|---|
| **Resting #1** | `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 0.01 lot | 81,084.00 | 81,446.00 | 80,180.00 | 3.62 USD | **LIVE_RESTING_PENDING** (Armored by 16.3M USD wall @ 81,500 & 9.65M @ 81,264) |
| **Resting #2** | `#19489156` | `USDJPY.pi` | SELL_LIMIT | 0.13 lot | 157.970 | 158.080 | 157.710 | 9.05 USD | **LIVE_RESTING_PENDING** (0.06 bps spread, VAH sweep fade) |
| **Resting #3** | `#19489157` | `BNBUSD.p` | SELL_LIMIT | 0.05 lot | 753.30 | 757.20 | 743.50 | 0.20 USD | **LIVE_RESTING_PENDING** (Armored by 1.04M USD wall @ 749.03 & 672K @ 753.71) |
| **Resting #4** | `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | 4040.50 | 4049.50 | 4018.00 | 9.00 USD | **LIVE_RESTING_PENDING** (Gold 0.20 bps spread, VAH sweep exhaustion) |
| **Resting #5** | `#19489159` | `NAS100.p` | SELL_LIMIT | 0.01 lot | 29,535.00 | 29,620.00 | 29,320.00 | 8.50 USD | **LIVE_RESTING_PENDING** (Nasdaq 0.34 bps spread, VAH fade) |
| **Resting #6** | `#19489160` | `DJ30.p` | SELL_LIMIT | 0.01 lot | 52,638.00 | 52,732.00 | 52,402.00 | 9.40 USD | **LIVE_RESTING_PENDING** (Dow 30 0.23 bps spread, VAH fade) |
| **Resting #7** | `#19489161` | `USWTI.p` | BUY_LIMIT | 0.01 lot | 101.550 | 100.990 | 102.930 | 0.56 USD | **LIVE_RESTING_PENDING** (WTI Crude 4.48 bps spread, VAL fade) |

---

## 📈 4. RECENT CLOSED TRADES & SESSION EQUITY LOG
- Ticket #19464650 (`BTCUSD.pi` SELL 0.01 @ 80,340.00, SL 80,563.50) closed for -2.24 USD.
- Account Solvency: Realized Balance 4,742.31 USD | Floating Equity 4,742.31 USD.
