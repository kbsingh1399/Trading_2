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
- **Account Balance**: **4,697.67 USD**
- **Floating Equity**: **4,721.77 USD**
- **Free Margin**: **4,191.34 USD**
- **Hard Capital Floor**: **4,775.00 USD** (Statutory Drawdown Defense Floor)
- **Operating Buffer**: **4,795.00 USD** (Solvency Kernel Floor)
- **Last Updated**: `2026-10-29 07:51:44 UTC`

---

## 🚀 2. LIVE RUNNING POSITIONS (3 ACTIVE)

| Ticket | Symbol | Type | Volume | Entry Price | Current Price | Live SL | Live TP | Floating PnL | Dynamic Ratchet State | Interrogation: "Should I let it run or cut it?" |
|---|---|---|---|---|---|---|---|---|---|---|
| **#19437063** | `AUDUSD.pi` | SELL | 0.10 | 0.70586 | 0.7045 | **0.70506** | 0.70368 | **+13.60 USD** | Stage 2 (+0.80R Profit Lock) | **LET IT RUN. Developing toward target; risk locked.** |
| **#19437494** | `USDJPY.pi` | BUY | 0.08 | 157.62 | 157.819 | **157.764** | 158.05 | **+10.09 USD** | Stage 2 (+0.80R Profit Lock) | **LET IT RUN. Developing toward target; risk locked.** |
| **#19437498** | `US2000.p` | SELL | 0.01 | 2846.5 | 2842.36 | **2858.0** | 2822.0 | **+0.41 USD** | Stage 0 | **LET IT RUN. Developing toward target; risk locked.** |

---

## 🎯 3. ACTIVE RESTING PENDING MAKER LIMIT ORDERS (6 STAGED)

| Ticket | Symbol | Order Type | Volume | Limit Entry | Live SL | Take Profit | Staged Status |
|---|---|---|---|---|---|---|---|
| **#19439188** | `EURGBP.pi` | SELL_LIMIT | 0.10 | **0.8381** | **0.8388** | 0.8368 | Resting passive maker order |
| **#19444900** | `SP500.p` | BUY_LIMIT | 0.02 | **7705.5** | **7695.5** | 7728.5 | Resting passive maker order |
| **#19445579** | `UKBRENT.p` | BUY_LIMIT | 0.10 | **114.45** | **113.9** | 115.8 | Resting passive maker order |
| **#19447583** | `NZDUSD.pi` | SELL_LIMIT | 0.12 | **0.5632** | **0.56388** | 0.5605 | Resting passive maker order |
| **#19448978** | `USDCAD.pi` | BUY_LIMIT | 0.10 | **1.3972** | **1.3961999999999999** | 1.3992 | Resting passive maker order |
| **#19448979** | `BNBUSD.p` | SELL_LIMIT | 0.70 | **762.5** | **772.5** | 747.0 | Resting passive maker order |
