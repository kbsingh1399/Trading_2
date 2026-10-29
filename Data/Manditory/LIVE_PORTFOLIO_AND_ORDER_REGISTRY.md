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
- **Account Balance**: **4,718.94 USD**
- **Floating Equity**: **4,743.66 USD**
- **Free Margin**: **4,362.54 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor)
- **Last Updated**: `2026-10-29 09:44:37 UTC`

---

## 🚀 2. LIVE RUNNING POSITIONS (2 ACTIVE)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| **#19437494** | `USDJPY.pi` | BUY | 0.08 | 157.62 | 157.951 | **157.764** | 158.05 | **+16.76 USD** | Stage 2 (+0.80R Profit Lock) | **LET IT RUN. Developing toward target; risk locked.** |
| **#19445579** | `UKBRENT.p` | BUY | 0.10 | 114.45 | 115.246 | **114.89** | 115.8 | **+7.96 USD** | Stage 2 (+0.80R Profit Lock) | **LET IT RUN. Developing toward target; risk locked.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (7 STAGED)

| Ticket | Symbol | Order Type | Volume | Limit Entry | Live SL | Take Profit | Staged Status |
|---|---|---|---|---|---|---|---|
| **#19444900** | `SP500.p` | BUY_LIMIT | 0.02 | **7705.5** | **7695.5** | 7728.5 | Resting passive maker order |
| **#19447583** | `NZDUSD.pi` | SELL_LIMIT | 0.12 | **0.5632** | **0.56388** | 0.5605 | Resting passive maker order |
| **#19448978** | `USDCAD.pi` | BUY_LIMIT | 0.10 | **1.3972** | **1.3961999999999999** | 1.3992 | Resting passive maker order |
| **#19448979** | `BNBUSD.p` | SELL_LIMIT | 0.70 | **762.5** | **772.5** | 747.0 | Resting passive maker order |
| **#19457311** | `XAUUSD.pi` | SELL_LIMIT | 0.01 | **4064.5** | **4088.5** | 3995.0 | Resting passive maker order |
| **#19457516** | `NAS100.p` | SELL_LIMIT | 0.01 | **29740.0** | **30025.0** | 29230.0 | Resting passive maker order |
| **#19457518** | `GBPUSD.pi` | SELL_LIMIT | 0.08 | **1.3348** | **1.3364** | 1.3312 | Resting passive maker order |
