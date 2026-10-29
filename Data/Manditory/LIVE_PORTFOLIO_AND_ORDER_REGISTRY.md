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
- **Standing Risk Capacity**: **0.00 USD** (Capital Defense Invariant: No live market exposure while below 4,775.00 USD floor)
- **Execution Posture**: **STAGED_INTENT_ONLY**
- **Last Synchronized (UTC)**: `2026-10-29 18:27:00 UTC` (`2026-10-29 23:57:00 IST`)

---

## 🚀 2. LIVE RUNNING POSITIONS (0 ACTIVE — 100% FLAT CASH)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| - | NONE | - | - | - | - | - | - | 0.00 USD | Flat | **Book is 100% Cash Defense. Zero open risk.** |

*Note: Prior test trade #19464650 (`BTCUSD.pi` SELL 0.01 @ 80,340.00, SL 80,563.50) stopped out during afternoon expansion for -2.24 USD, leaving account at 4,742.31 USD.*

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (0 EXECUTED / 3 STAGED INTENT)

| Priority | Symbol | Order Type | Volume | Limit Entry | Spread-Padded SL | Take Profit | Risk USD | Staged Status |
|---|---|---|---|---|---|---|---|---|
| **Staged #1** | `BTCUSD.pi` | SELL_LIMIT | 0.02 | 81,084.34 | 81,446.12 | 80,179.89 | 7.24 USD | **STAGED_INTENT_ONLY** (Protected by 16.3M USD wall @ 81,500) |
| **Staged #2** | `USDJPY.pi` | SELL_LIMIT | 0.13 | 158.004 | 158.123 | 157.707 | 9.80 USD | **STAGED_INTENT_ONLY** (0.06 bps spread, VAH sweep fade) |
| **Staged #3** | `BNBUSD.p` | SELL_LIMIT | 2.55 | 753.31 | 757.22 | 743.53 | 9.97 USD | **STAGED_INTENT_ONLY** (Protected by 1.04M USD wall @ 749.03 & 672K wall @ 753.71) |
