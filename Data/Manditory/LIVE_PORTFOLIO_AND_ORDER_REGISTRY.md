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
- **Account Balance**: **4,744.55 USD**
- **Floating Equity**: **4,744.12 USD**
- **Free Margin**: **4,342.42 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor)
- **Last Updated**: `2026-10-29 14:17:19 UTC`

---

## 🚀 2. LIVE RUNNING POSITIONS (1 ACTIVE)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| **#19464650** | `BTCUSD.pi` | SELL | 0.01 | 80340.0 | 80383.0 | **80563.5** | 79663.5 | **-0.43 USD** | Stage 0 | **DEFEND. Structural invalidation check active.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (0 STAGED)

| Ticket | Symbol | Order Type | Volume | Limit Entry | Live SL | Take Profit | Staged Status |
|---|---|---|---|---|---|---|---|
| - | NONE | - | - | - | - | - | No resting limit orders. |
